import sys
import argparse
from datetime import datetime

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_absolute_error, mean_squared_error, make_scorer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler, scale

from statsmodels.tsa.stattools import pacf, acf

# Database connection
import datastore

import xgboost
import xgb_autotune

DEBUG=False
# ---------------
def input_cmd():
    # ---------------
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--hours", type=int, help="Number of hours to forecast")

    parser.add_argument("-c", "--company", type=int, help="The company id")

    parser.add_argument(
        "-d",
        "--direction",
        type=int,
        default=0,
        choices=[0, 1, 2],
        help="The traffic direction: 0-all; 1-in; 2-out",
    )

    parser.add_argument(
        "-b", "--begin", type=str, help="The start date in format YYYY-MM-DD"
    )

    parser.add_argument(
        "-e", "--end", type=str, help="The end date in format YYYY-MM-DD"
    )

    parser.add_argument(
        "-m", "--metric",
        type=str,
        default="RMSLE",
        choices=["RMSLE", "MAE", "MAPE", "ALL"],
        help="Error formula"
    )

    parser.add_argument(
        "-t",
        "--table",
        type=str,
        default="jangle_traffic_total",
        choices=["jangle_traffic_total", "radius_traffic_total"],
        help="The table",
    )

    args = parser.parse_args()
    return args


# -------------------------------------------------------------------------
def query(sql):
    # -------------------------------------------------------------------------
    datastore.start_transaction(readonly=True)
    d = datastore.query(sql)
    datastore.commit()
    return d


# -------------------------------------------------------------------------
def sql_hourly_traffic(table, start, end, company, direction=None):
    # -------------------------------------------------------------------------

    timescale = "%%Y-%%m-%%d %%H"
    if not direction:
        filter = "1=1"
    else:
        filter = "direction=" + str(direction)

    SQL = f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   SUM(bytes)  / (1024.0 * 1024.0)   as y
   FROM {table}
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company =  {company}
   and {filter}
   GROUP BY date
   ORDER BY date
  """

    return SQL


# -------------------------------------------------------------------------
def get_data_from_db(table, start_date, end_date, company, direction):
    # -------------------------------------------------------------------------

    sql = sql_hourly_traffic(table, start_date, end_date, company, direction)
    print(sql)
    df = query(sql)
    if df.empty:
        print("No data found")
        exit(0)

    date_range = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq="H")
    df["date"] = pd.to_datetime(df["date"])
    df.set_index("date", inplace=True)
    df = df.reindex(date_range)
    # TODO fillna(0)
    return df


# -------------------------------------------------------------------------
def generate_series(signal, start_day, number_of_days, amplitude=1, freq=1):
    # -------------------------------------------------------------------------

    PI = 3.14159
    number_of_hours = number_of_days * 24
    rng = pd.date_range(start_day, periods=number_of_hours, freq="H")

    if signal == "random":
        s = pd.Series(np.random.randn(number_of_hours), index=rng, name="y")
    elif signal == "sin":
        const = 0

        s = pd.Series(
            const + amplitude * (np.sin(rng.hour * freq * PI / 12.0)),
            index=rng,
            name="y",
        )

    elif signal == "linear":

        first_timepoint = rng[0]
        intersect = 0.0
        slope = 1.0

        hours_from_start = (rng - first_timepoint).astype("timedelta64[h]").astype(int)
        s = pd.Series(intersect + slope * hours_from_start, index=rng, name="y")

    elif signal == "linear_and_sin":

        first_timepoint = rng[0]
        intersect = 0.0
        slope = 1.0
        amplitude = 10
        hours_from_start = (rng - first_timepoint).astype("timedelta64[h]").astype(int)
        s = pd.Series(
            intersect
            + slope * hours_from_start
            + amplitude * (np.sin(rng.hour * freq * PI / 12.0)),
            index=rng,
            name="y",
        )

    else:
        print("signal=", signal, " not implemented")
        exit(1)

    s.plot(title=signal)
    plt.show()

    return s


# ------------------------
def detrend(s):
    # ------------------------
    y = s.values
    l = len(s)
    X = np.array(list(range(0, l))).reshape(-1, 1)

    model = LinearRegression().fit(X, y)
    print("intercept:", model.intercept_)
    print("slope:", model.coef_)
    trend = model.predict(X)

    if DEBUG:
        plt.plot(y)
        plt.plot(trend)
        plt.show()

    new_s = pd.Series(s.values - trend, s.index)

    if DEBUG:
        new_s.plot(title="detrended")
        plt.show()

    return new_s, model


# -----------------------------------------------
def forecast_split(data, n_steps=5, freq="1H"):
    # -----------------------------------------------
    """
       Returns
        t_target: pd.Series with the training data
        f_target: pd.Series with the forecast data
        fcast_range: pd.DateRange with the forecasting timestamps
      """

    # the complete time series
    c_target = data.copy()

    # data used for training
    date = c_target.index[-1] - pd.Timedelta(hours=n_steps)
    t_target = c_target[c_target.index <= date]

    # data used for forecasting
    f_target = c_target[c_target.index > date]
    fcast_initial_date = f_target.index[0]
    fcast_range = pd.date_range(fcast_initial_date, periods=n_steps, freq=freq)

    print(
        f"Full available time range: from {c_target.index[0]} to {c_target.index[-1]}"
    )
    print(f"Training time range: from {t_target.index[0]} to {t_target.index[-1]}")
    print(f"Forecasting time range: from {fcast_range[0]} to {fcast_range[-1]}")

    return t_target, f_target, fcast_range


# ---------------------------------------------------------
def get_features(y, opt, f_lags=True, lags=None):
    # ---------------------------------------------------------
    """
    Create the feature set for the time series

    Parameters
    ----------
    y: pd.Series with the target time series
    f_lags: boolean switch for turning on lags features

    lags: optional list of lags to create the lag features for

    Returns
    -------
    features: pd.DataFrame with the feature set
    target: pd.Series holding the target time series with the same index as the features
    """

    features = pd.DataFrame()

    ts = create_ts_features(y, opt)
    features = features.join(ts, how="outer").dropna()

    if f_lags:
        lags = create_lag_features(y, lags=lags, thres=0.2)
        features = features.join(lags, how="outer").dropna()

    target = y[y.index >= features.index[0]]

    return features, target


# -----------------------------
def create_ts_features(data, opt):
    # -----------------------------

    def get_shift(row):
        """
        shift: 3 shifts per day of 8 hours
        """
        if 6 <= row.hour <= 14:
            return 2
        elif 15 <= row.hour <= 22:
            return 3
        else:
            return 1

    features = pd.DataFrame()

    features["hour"] = data.index.hour
    features["weekday"] = data.index.weekday
    features["dayofyear"] = data.index.dayofyear
    features["is_weekend"] = data.index.weekday.isin([5, 6]).astype(np.int32)

    features["dayofweek"] = data.index.dayofweek

    features["shift"] = pd.Series(data.index.map(get_shift))

    features.index = data.index

    return features


# ----------------------------------------------------
def create_lag_features(target, lags=None, thres=0.2):
    # ----------------------------------------------------
    print("--- create_lag_features() lags=", lags)
    scaler = StandardScaler()
    features = pd.DataFrame()

    if lags is None:
        # PACF - partial autocorrelation functions.
        # consider lag features only when PACF is greater than 0.2 (5% relevance) to build the features
        try:
            partial = pd.Series(data=pacf(target, nlags=48))
            lags = list(partial[np.abs(partial) >= thres].index)

        except:
            print("error numpy.linalg.LinAlgError: Singular matrix")
            # return pd.DataFrame()

    df = pd.DataFrame()

    if not lags or len(lags) == 0:
        print("no lags")
        return df

    if 0 in lags:
        lags.remove(0)  # do not consider itself as lag feature

    for i in range(1,5):
        if i not in lags:
            lags.append(i)

    for l in lags:
        df[f"lag_{l}"] = target.shift(l)

    print("----  lags= --------")
    print(lags)
    print("len df=", len(df))

    features = pd.DataFrame(scaler.fit_transform(df[df.columns]), columns=df.columns)

    features = df
    features.index = target.index

    return features


# ---------------------------------------------------------------
def direct(y, train_fn, lags, n_steps, opt,  score_metric, step="1H"): # params=None):
    # ---------------------------------------------------------------
    """Multi-step direct forecasting using a machine learning model
        to forecast each time period ahead

        Parameters
        ----------
        y: pd.Series holding the input time-series to forecast
        train_fn: a function for training the model which returns as output the trained model
                and test score
        score_metric: metric the training function

        Returns
        -------
        fcast_values: pd.Series with forecasted values indexed by forecast horizon dates
        model: xgboost model
        """

    def one_step_features(date, step):

        # features must be obtained using data lagged
        # by the desired number of steps (the for loop index)
        tmp = y[y.index <= date]
        lags_features = create_lag_features(tmp, lags=lags)
        ts_features = create_ts_features(tmp, opt)
        if lags_features.empty:
            print("-----  no lags--------")

        features = ts_features.join(lags_features, how="outer").dropna()

        # build target to be ahead of the features built
        # by the desired number of steps (the for loop index)
        target = y[y.index >= features.index[0] + pd.Timedelta(hours=step)]
        assert len(features.index) == len(target.index)

        return features, target

    fcast_values = []
    fcast_range = pd.date_range(
        y.index[-1] + pd.Timedelta(hours=1),
        periods=n_steps,
        freq=step,
    )
    fcast_features, _ = one_step_features(y.index[-1], 0)

    for s in range(1, n_steps + 1):

        last_date = y.index[-1] - pd.Timedelta(hours=s)
        features, target = one_step_features(last_date, s)

        model = train_fn(features, target, score_metric)

        # use the model to predict s steps ahead
        predictions = model.predict(fcast_features)
        fcast_values.append(predictions[-1])

    return pd.Series(index=fcast_range, data=fcast_values), model


# https://github.com/dmlc/xgboost/blob/master/demo/guide-python/custom_rmsle.py
# --------------------------
def rmsle(real, predicted):
    # --------------------------
    sum = 0.0
    for x in range(len(predicted)):
        if predicted[x] < 0 or real[x] < 0:  # check for negative values
            continue
        p = np.log(predicted[x] + 1)
        r = np.log(real[x] + 1)
        sum = sum + (p - r) ** 2
    return (sum / len(predicted)) ** 0.5


# MAE computation
def mae(y, yhat):
    """
    Safe computation of the Mean Average Percentage Error
    Parameters
    ----------
    y: pd.Series or np.array holding the actual values
    yhat: pd.Series or np.array holding the predicted values
    perc: if True return the value in percentage
    Returns
    -------
    the MAE value
    """
    err = -1.
    try:
        m = len(y.index) if type(y) == pd.Series else len(y)
        n = len(yhat.index) if type(yhat) == pd.Series else len(yhat)
        assert m == n
        mae = []
        for a, f in zip(y, yhat):
                mae.append(np.abs((a - f)))
        mae = np.mean(np.array(mae))
        return mae

    except AssertionError:
        print(f"Wrong dimension for MAE calculation: y = {m}, yhat = {n}")
        return -1.


# MAPE computation
def mape(y, yhat, perc=True):
    """
    Safe computation of the Mean Average Percentage Error
    Parameters
    ----------
    y: pd.Series or np.array holding the actual values
    yhat: pd.Series or np.array holding the predicted values
    perc: if True return the value in percentage
    Returns
    -------
    the MAPE value
    """
    err = -1.
    try:
        m = len(y.index) if type(y) == pd.Series else len(y)
        n = len(yhat.index) if type(yhat) == pd.Series else len(yhat)
        assert m == n
        mape = []
        for a, f in zip(y, yhat):
            # avoid division by 0
            if np.abs(a) > 1e-3:
                mape.append(np.abs((a - f)/a))
        mape = np.mean(np.array(mape))
        return mape * 100. if perc else mape

    except AssertionError:
        print(f"Wrong dimension for MAPE calculation: y = {m}, yhat = {n}")
        return -1.
# -------------------------------------------------------------------
def train_autotune_model(X_train, y_train, score_metric):
    # -------------------------------------------------------------------


    fitted_model = xgb_autotune.fit_parameters(
        initial_model=xgboost.XGBRegressor(objective="reg:squarederror"),
        initial_params_dict={},
        X_train=X_train,
        y_train=y_train,
        min_loss=0.01,
        scoring=score_metric,
        n_folds=5,
    )

    return  fitted_model


# -------------------------------------------------------------------
def xgboost_model(features, target, score_metric, test_size=0.2,):
    # -------------------------------------------------------------------
    """
    features: pd.DataFrame holding the model features
    target: pd.Series holding the target values
    test_size: 20% by default
    Returns
    -------
    model: the optimized XGBoost model
    """

    X_train, X_test, y_train, y_test = train_test_split(
        features, target, test_size=test_size, shuffle=False
    )

    model  = train_autotune_model(X_train, y_train, score_metric)

    return model


# ------------------------------------
def multi_direct(c_target, f_steps, option, score_metric):
    # ------------------------------------

    t_target, f_target, fcast_range = forecast_split(c_target, n_steps=f_steps)
    features, target = get_features(t_target, option)

    print(
        "--- multi_direct() len(t_target) =",
        len(t_target),
        "len(f_target)=",
        len(f_target),
        "len(fcast_range)=",
        len(fcast_range),
    )

    lags = [int(f.split("_")[1]) for f in features if "lag" in f]

    t_target_detrended, model_detrended = detrend(t_target)

    fcast_xgb_detrended, model = direct(
        t_target_detrended, xgboost_model, lags, f_steps, option, score_metric
    )

    start = len(t_target)
    end = start + len(f_target)
    X = np.array(list(range(start, end))).reshape(-1, 1)
    fcast_xgb = model_detrended.predict(X) + fcast_xgb_detrended
    fcast_xgb[fcast_xgb < 0] = 0

    if DEBUG:

        xgboost.plot_importance(model, height=0.9)
        plt.show()


    return fcast_xgb


# ---------------------------------------------
def final_plot(c_target, predictions, labels, header):
    # ----------------------------------------------
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))

    ax.plot(c_target, color="blue", label="Real data", linestyle="-", marker="o")

    for i, pred in enumerate(predictions):
        ax.plot(pred, label=labels[i] , linestyle="--", marker="o")

    ax.set_title(header)
    ax.legend()
    plt.show()


# ------------
def help(s=None):
    # ------------
    if s:
        print(s)

    print("Usage example:")
    print("python xgb.py --hours 24 --company 3666 --begin 2020-12-01 --end 2021-12-05")
    print("--------")
    exit(0)


# ---------------
def main():
    # ---------------
    if len(sys.argv) == 1:
        help("")

    try:
        args = input_cmd()
        print(args)

        if not args.company:
            help("no company")
        if not args.begin:
            help("no begin")
        if not args.end:
            help("no end")
        if not args.hours:
            help("no hours")

        print("args.metric=", args.metric)

        company = args.company
        table = args.table

        begin = args.begin
        end = args.end

        f_steps = args.hours
        direction = args.direction

        d_begin = datetime.strptime(begin, "%Y-%m-%d")
        d_end = datetime.strptime(end, "%Y-%m-%d")

        n_days = (d_end - d_begin).days

        # The training interval should be longer at least twice than asked prediction hours
        print("n_days=", n_days)
        if  n_days * 24 < args.hours * 2:
            print(
                "The training interval is too short"
            )
            exit(1)

    except:
        print("Error in parsing input")
        e = sys.exc_info()[0]
        print(e)
        help()
        exit(1)

    if int(company) >= 0:
        datastore.connect()
        if direction not in [1, 2]:
            direction = None  # All directions
        data = get_data_from_db(table, begin, end, company, direction)
        if data.empty:
            print("No data found")
            exit(0)

        print(data)

        s = data["y"]  # make series
        s.fillna(0, inplace=True)
        s.name = "y"

    else:  # simulate input
        s = generate_series("linear_and_sin", begin, n_days)

    predictions = []
    labels = []
    metrics={
        "RMSLE": make_scorer(rmsle, greater_is_better=False),
        "MAE"  : make_scorer(mae, greater_is_better=False),
        "MAPE" : make_scorer(mape, greater_is_better=False)
    }

    for metric_name, metric_function in  metrics.items():
      if args.metric == 'ALL' or args.metric == metric_name:
        p = multi_direct(s, f_steps, None, metric_function)
        predictions.append(p)
        labels.append( metric_name)

    header = "Hourly traffic (MB). "
    header += str(f_steps) + " hours prediction. "
    if int(company) >= 0 and table:
        header += " Company " + str(company) + ". Table: " + table
        if direction:
            header +=  " . Direction=" + str(direction)

    final_plot(s, predictions, labels, header)


if __name__ == "__main__":
    main()

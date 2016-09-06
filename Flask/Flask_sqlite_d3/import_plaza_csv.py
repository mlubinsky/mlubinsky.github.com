"""
Read in BART ETD data from files and write to SQL.
"""
import sqlite3
import pandas as pd
import numpy as np

DATABASE = 'bart.db'
#FILES = ['plza.csv', 'mont.csv']
FILES = ['plza.csv' ]

def parse_time(timestamp):
    """Attempt to parse a timestamp (in seconds) into a pandas datetime in
    Pacific time, return the timestamp is parsing is successful, NaT (not a
    time) otherwise

    :return: Pandas timestamp in Pacific time, or NaT
    """
    try:
        dt = pd.to_datetime(float(timestamp), unit='s')
        return dt.tz_localize('UTC').tz_convert('US/Pacific')
    except (AttributeError, ValueError):
        return pd.NaT


def define_weekday(obs_time):
    """Return 0 if obs_time occurred on a weekday, 1 if a Saturday, 2 if a
    Sunday.

    :param obs_time: pandas timestamp
    """
    if obs_time.weekday() < 5:
        return 0
    elif obs_time.weekday() == 5:
        return 1
    elif obs_time.weekday() == 6:
        return 2


def parse_data(file_name, date_parser=parse_time, time_col=['time']):
    """Return a dataframe from csv file, with times parsed.

    :param file_name: csv file
    :param date_parser: function to convert time_col to datetime (default:
    parse time)
    :param time_col: the time of the column to parse as times
    :return: DataFrame from csv file
    """
    return pd.read_csv(file_name, parse_dates=time_col, date_parser=date_parser)


def time2minute_of_day(obs_time):
    """Return the minute of day (12:00 midnight = 0) of observation time

    :param obs_time: pandas datetime object
    """
    return obs_time.time().hour * 60 + obs_time.time().minute

def csv2sql(conn, files):
    """Read in BART ETD data from files and write that data to the SQL database
    accessed by conn.

    :param conn: SQL database connection
    :param files: the files to read data from
    """
    output_cols = ['dest', 'dir', 'etd', 'station', 'minute_of_day',
                   'day_of_week']
    conn.execute("DROP TABLE IF EXISTS etd")
    for sta_file in files:
        df = parse_data(sta_file)
        df['station'] = sta_file.split('.')[0]
        df['day_of_week'] = df['time'].apply(lambda x: define_weekday(x))
        df['etd'] = df['etd'].replace('Leaving', 0).dropna().astype(np.int)
        df['minute_of_day'] = df['time'].apply(time2minute_of_day)
        df[output_cols].to_sql('etd', conn, index=False, if_exists='append')

    conn.cursor().execute(
        """CREATE INDEX idx1
        ON etd(station, dest, minute_of_day, day_of_week)
        """
        )
    conn.commit()
    conn.close()

if __name__ == '__main__':
    conn = sqlite3.connect(DATABASE)
    csv2sql(conn, FILES)
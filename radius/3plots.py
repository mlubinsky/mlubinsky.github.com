import time
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from plotnine import *

import xgboost as xgb  # conda install py-xgboost-cpu
from xgboost import plot_importance, plot_tree

from adtk.data import validate_series
from adtk.visualization import plot
from adtk.detector import ThresholdAD
from adtk.detector import SeasonalAD
from adtk.detector import QuantileAD
from adtk.detector import InterQuartileRangeAD
from adtk.detector import PersistAD
from adtk.detector import LevelShiftAD
from adtk.detector import VolatilityShiftAD
from adtk.detector import  AutoregressionAD

import datastore

#--------------
def query(sql):
#-------------
  datastore.start_transaction(readonly=True)
  d=datastore.query(sql)
  datastore.commit()
  return d

#----------------------------------
def sql_traffic_hourly_per_day_of_week(  start, end, table, company):
#-----------------------------------
    SQL = f"""
    SELECT 
      CONCAT( 
            DAYOFWEEK(FROM_UNIXTIME(timebin, '%%Y-%%m-%%d')),
            '-',
            DAYNAME(FROM_UNIXTIME(timebin, '%%Y-%%m-%%d'))
      )
      as dayname,
      FROM_UNIXTIME(timebin, '%%H') as hour,
      SUM(bytes) / (1024.0 * 1024.0) as MB 
    FROM jangle_traffic_total
    WHERE
         timebin >=  UNIX_TIMESTAMP('{start}') and
         timebin  <  UNIX_TIMESTAMP('{end}') and
         company = {company}
    GROUP BY dayname, hour
    ORDER BY dayname, hour
    """
    #ORDER BY  DAYOFWEEK(FROM_UNIXTIME(timebin, '%%Y-%%m-%%d'))
    return SQL
#----------------------------------
def sql_top_device_count(  start, end, table):
#-----------------------------------  
    SQL = f"""
       SELECT
         CAST(company AS CHAR) as company,
         count(distinct msisdn) as n_msisdn
       FROM {table}
       WHERE
         timebin >=  UNIX_TIMESTAMP('{start}') and
         timebin  <  UNIX_TIMESTAMP('{end}')
       GROUP BY CAST(company AS CHAR)
       ORDER BY n_msisdn DESC
       LIMIT 10
    """
    return SQL

#----------------------------------
def sql_top_traffic_by_protocol(  start, end, table):
#-----------------------------------  
    SQL = f"""
       SELECT
         CAST(company AS CHAR) as company,
         SUM( 
           CASE 
             WHEN protocol = 1 THEN bytes
             ELSE 0
           END
         )    
          / (1024.0 * 1024.0 * 1024.0)   as  ICMP,

         SUM( 
           CASE 
             WHEN protocol = 6 THEN bytes
             ELSE 0
           END
         )    
          / (1024.0 * 1024.0 * 1024.0)   as  TCP,

         SUM( 
           CASE 
             WHEN protocol = 17 THEN bytes
             ELSE 0
           END
         )    
          / (1024.0 * 1024.0 * 1024.0)   as  UDP,

                  SUM( 
           CASE 
             WHEN protocol = 112 THEN bytes
             ELSE 0
           END
         )    
          / (1024.0 * 1024.0 * 1024.0)   as  VRRP

       FROM {table}
       WHERE
         timebin >=  UNIX_TIMESTAMP('{start}') and
         timebin  <  UNIX_TIMESTAMP('{end}')
       GROUP BY CAST(company AS CHAR)
       ORDER BY  SUM(bytes) DESC
       LIMIT 10
    """
    return SQL   

#----------------------------------
def sql_top_traffic_by_direction(  start, end, table):
#-----------------------------------  
    SQL = f"""
       SELECT
         CAST(company AS CHAR) as company,
         SUM( 
           CASE 
             WHEN direction = 1 THEN bytes
             ELSE 0
           END
         )    
          / (1024.0 * 1024.0 * 1024.0)   as GB_direction_1,
         SUM( 
           CASE 
             WHEN direction = 2 THEN bytes
             ELSE 0
           END
         )    
          / (1024.0 * 1024.0 * 1024.0)   as GB_direction_2

       FROM {table}
       WHERE
         timebin >=  UNIX_TIMESTAMP('{start}') and
         timebin  <  UNIX_TIMESTAMP('{end}')
       GROUP BY CAST(company AS CHAR)
       ORDER BY  SUM(bytes) DESC
       LIMIT 10
    """
    return SQL   
#----------------------------------
def sql_top_traffic(  start, end, table):
#-----------------------------------  
    SQL = f"""
       SELECT
         CAST(company AS CHAR) as company,
         SUM(bytes) * 1.0 / (1024.0 * 1024.0 * 1024.0)   as GB
       FROM {table}
       WHERE
         timebin >=  UNIX_TIMESTAMP('{start}') and
         timebin  <  UNIX_TIMESTAMP('{end}')
       GROUP BY CAST(company AS CHAR)
       ORDER BY GB DESC
       LIMIT 10
    """
    return SQL    
#----------------------------------
def sql_device_count(  start, end, table, companies=None): # granularity='hour'):
#-----------------------------------  
  #if granularity == 'hour':
  timescale= '%%Y-%%m-%%d %%H'
  #else: # day
  #       timescale= '%%Y-%%m-%%d'
  #if not table:
  #    table='jangle_traffic'

  #COMPANY_LIST=(3659,3116, 3666)
  filter="1=1"
  #if not direction:
  #  filter="1=1"
  #else:
  # filter="direction="+str(direction)

  if not companies:  # get top 5 
    companies = f"""
    ( SELECT company FROM (
       SELECT
         company,
         count(distinct msisdn) as n_msisdn
       FROM {table}
       WHERE
         timebin >=  UNIX_TIMESTAMP('{start}') and
         timebin  <  UNIX_TIMESTAMP('{end}')
       GROUP BY company
       ORDER BY n_msisdn DESC
       LIMIT 5
      ) TMP
    )
    """

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   company,
   count(distinct msisdn) as n_msisdn
   FROM {table}
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company in  {companies}
   and {filter}
   GROUP BY date, company
   ORDER BY date
  """

  return SQL
#--------------------------------------
def show_top_device_count(start, end):
#--------------------------------------  
   for table in ['jangle_traffic', 'radius_traffic', 'radius_active', 'jangle_active']:
      sql=sql_top_device_count(start, end, table)
      print(sql)
      df=query(sql)
      print(df)
      print(df.describe())
      print(df.columns)
      print(df.dtypes)

      df.set_index('company', inplace=True)
      header="Top 10 companies by number of distinct devices. Table " + table + ".  " + start + "   " + end
      df.plot(kind="bar", title=header)
      plt.show() 

#--------------------------------------
def show_traffic_hourly_per_day_of_week(start, end, company):
#--------------------------------------
   for table in ['jangle_traffic_total']: #, 'radius_traffic']:
      #sql=sql_top_traffic(start, end, table)
      sql=sql_traffic_hourly_per_day_of_week(start, end, table, company)
      print(sql)
      df=query(sql)
      
      print(df)
      print(df.describe())
      print(df.columns)
      print(df.dtypes)
      #df.set_index('hour', inplace=True)

      header="Company: " + str(company)+". Hourly traffic (MB) by day of week. Table: " + table + ". From " + start + " till " + end
      df.plot(x="hour",y="MB", title=header, linestyle='-', marker='o')
      plt.show()

      #fig = plt.figure()
      #ax = fig.add_subplot(111)
      #ax.plot(df['LimMag1.3'], df['ExpTime1.3'], label="1.3")
      #ax.plot(df['LimMag2.0'], df['ExpTime2.0'], label="2.0")
      #ax.plot(df['LimMag2.5'], df['ExpTime2.5'], label="2.5")
      df.pivot(index='hour', columns='dayname', values="MB").plot(title=header, linestyle='-', marker='o')
      plt.show()
      return
      ################################# 
      print("faced grip")
      g = (
        ggplot(df,
         aes(x="hour", y="MB") #, color="company")
        )
        + geom_point()
        + facet_grid('~dayname' )
        + labs(title=header + '  (facet_grid)')
      )
      print(g)
      print("faced wrap")
      g = (
        ggplot(df,
         aes(x="hour", y="MB") #, color="company")
        )
        + geom_point()
        + facet_wrap('~dayname' )
        + labs(title=header + '(facet_wrap)')
      )
      print(g)

      #df.set_index('dayname', inplace=True)

      #df.plot.barh(title=header, stacked=True)


      #print("2nd attempt")
      #ax=df.plot.bar(rot=0, subplots=True, stacked=True)
      #plt.show()

#--------------------------------------
def show_top_traffic(start, end):
#--------------------------------------
   for table in ['jangle_traffic', 'radius_traffic']:
      #sql=sql_top_traffic(start, end, table)
      sql=sql_top_traffic_by_direction(start, end, table)
      print(sql)
      df=query(sql)
      print(df)
      print(df.describe())
      print(df.columns)
      print(df.dtypes)

      df.set_index('company', inplace=True)
      header="Top 10 companies by traffic. Table " + table + ".  " + start + "   " + end
      df.plot(kind="bar", title=header)
      plt.show()       
      #df.plot(kind="bar", title=header, stacked=True)
      #plt.show()  
      sql=sql_top_traffic_by_protocol(start, end, table)
      print(sql)
      df=query(sql)
      print(df)
      print(df.describe())
      print(df.columns)
      print(df.dtypes)

      df.set_index('company', inplace=True)
      header="Top 10 companies by traffic. Table " + table + ".  " + start + "   " + end
      df.plot(kind="bar", title=header)
      plt.show() 

#--------------------------------------
def show_device_count(start, end, companies=None):
#--------------------------------------  
  for table in ['jangle_traffic', 'radius_traffic', 'radius_active', 'jangle_active']:
     sql=sql_device_count(start, end, table, companies)
     
     print(sql)
     df=query(sql)
     print(df)
     print(df.describe())

     #range  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
     df['date'] = pd.to_datetime(df['date'])
     print(df.columns)


     #print("fill NA with 0")
     #df=df.fillna(0)


     df2=pd.pivot_table(df, values='n_msisdn', columns='company' , index=['date'])
     print("df2.columns=")
 
     print(df2.columns)
 
     #range  = pd.date_range(start=df2["date"].min(), end=df2["date"].max(), freq='H')
  
     #df2.set_index('date', inplace=True)
     #d2f=df2.reindex(range)

     print(df2)
     print(df2.describe())
     print(df2.info())
     print(df2.columns) 
     
     header="Number of devices. Table " + table + ".  " + start + "   " + end
     df2.plot(title=header, style=".")
     plt.show() 

#-------------------------------------------
def show_traffic_protocol(start, end, companies=None, direction=None):
#-------------------------------------------
   #for table in ['jangle_traffic_total', 'radius_traffic_total']:
   for table in ['jangle_traffic_total']:  
     sql= sql_traffic_protocol(start, end, table, companies)
     print(sql)
     df=query(sql)
     print(df)
     print(df.dtypes)
     print(df.describe())

     #range  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
     df['date'] = pd.to_datetime(df['date'])
     print(df.columns)


     #print("fill NA with 0")
     #df=df.fillna(0)


     df2=pd.pivot_table(df, values='MB', columns='Protocol' , index=['date'])
     print("df2.columns=")
     print(df2.columns)

     #range  = pd.date_range(start=df2["date"].min(), end=df2["date"].max(), freq='H')

     #df2.set_index('date', inplace=True)
     #d2f=df2.reindex(range)

     print(df2)
     print(df2.describe())
     print(df2.info())
     print(df2.columns)
     header="Hourly Traffic (MB). Table: "+table+ ". From " + start + "  till " + end
     if companies:
        header += " Companies: "+str(companies)
     #df2.plot(title=header, style=".")
     #plt.show()

     df2.plot(title=header)
     plt.show()
#------------------
def show_adtk(s):
#------------------
     print("-----show_adtk----")
     print(s.dtypes)
     print(s)
     print(s.index)

     s = validate_series(s)
     #plot(s)

     print(" SeasonalAD() ")
     seasonal_ad = SeasonalAD()
     anomalies = seasonal_ad.fit_detect(s)
     plot(s, anomaly=anomalies, anomaly_color="red", anomaly_tag="marker")
     plt.show()

     print(" ThresholdAD(high=500, low=15) ")
     threshold_ad = ThresholdAD(high=500, low=15)
     anomalies = threshold_ad.detect(s)
     plot(s, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
     plt.show()

     print("QuantileAD(high=0.99, low=0.01) ")
     quantile_ad = QuantileAD(high=0.99, low=0.01)
     anomalies = quantile_ad.fit_detect(s)
     plot(s, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
     plt.show()

     print("InterQuartileRangeAD(c=1.5) ")
     iqr_ad = InterQuartileRangeAD(c=1.5)
     anomalies = iqr_ad.fit_detect(s)
     plot(s, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_markersize=5, anomaly_color='red', anomaly_tag="marker")
     plt.show()

     print(" PersistAD(c=3.0, side='positive')")
     persist_ad = PersistAD(c=3.0, side='positive')
     persist_ad.window = 4
     anomalies = persist_ad.fit_detect(s)
     plot(s, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red')
     plt.show()

     print(" LevelShiftAD(c=6.0, side='both', window=5) ")
     level_shift_ad = LevelShiftAD(c=6.0, side='both', window=5)
     anomalies = level_shift_ad.fit_detect(s)
     plot(s, anomaly=anomalies, anomaly_color='red')
     plt.show()

     print(" VolatilityShiftAD(c=6.0, side='positive', window=30) ")
     volatility_shift_ad = VolatilityShiftAD(c=6.0, side='positive', window=30)
     anomalies = volatility_shift_ad.fit_detect(s)
     plot(s, anomaly=anomalies, anomaly_color='red')
     plt.show()

     print("AutoregressionAD(n_steps=7*2, step_size=24, c=3.0) ")
     autoregression_ad = AutoregressionAD(n_steps=7*2, step_size=24, c=3.0)
     anomalies = autoregression_ad.fit_detect(s)
     plot(s, anomaly=anomalies, ts_markersize=1, anomaly_color='red', anomaly_tag="marker", anomaly_markersize=2)
     plt.show()

    # outlier_detector = OutlierDetector(LocalOutlierFactor(contamination=0.05))
    # anomalies = outlier_detector.fit_detect(df)
     #plot(df, anomaly=anomalies, ts_linewidth=1, ts_markersize=3, anomaly_color='red', anomaly_alpha=0.3, curve_group='all');

#-------------------------------------------
def show_traffic_total_per_direction(start, end, companies=None):
#-------------------------------------------
   #for table in ['jangle_traffic_total', 'radius_traffic_total']:
   for table in ['jangle_traffic_total']:  
     sql= sql_traffic_total_per_direction(start, end, table, companies)
     print(sql)
     df=query(sql)
     print(df)
     print(df.dtypes)
     print(df.describe())

     #range  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
     df['date'] = pd.to_datetime(df['date'])
     print(df.columns)
     print("companies=",companies)
     sns.histplot(df, x='MB', bins=70, hue='direction')
     plt.show()
     #print("fill NA with 0")
     #df=df.fillna(0)
     #show_adtk(df["MB"])
 

     df2=pd.pivot_table(df, values='MB', columns='direction' , index=['date'])
     print("df2.columns=")
     print(df2.columns)
     print(df2.dtypes)
     print(df2)

     df2.plot.hist(bins=100)
     plt.show()

     #sns.histplot(df2,x='MB', bins=50)
     #plt.show()
     #range  = pd.date_range(start=df2["date"].min(), end=df2["date"].max(), freq='H')

     #df2.set_index('date', inplace=True)
     #d2f=df2.reindex(range)

     print(df2)
     print(df2.describe())
     print(df2.info())
     print(df2.dtypes)

     header="Hourly Traffic (MB). Table: "+table+ ". From " + start + "  till " + end
     if companies:
       if len(companies) == 1:
           header += ". Company: "+str(companies[0])
       else:
           header += ". Companies: "+str(companies)
     #df2.plot(title=header, style=".") -- useful to see gaps
     #plt.show()
     print("show_traffic_total_per_direction()")
     df2.plot(title=header)
     plt.show()

     #for d in [1,2]:
        #df2[df2["direction"] == d].hist("MB",  bins=35, rwidth=0.9 ) # layout=(3,1) by='direction',
     #   df2[str(d)].hist("MB",  bins=35, rwidth=0.9 ) # layout=(3,1) by='direction',
      #  plt.show()
     # bins=25, grid=False, figsize=(12,8), color='#86bf91', zorder=2, rwidth=0.9
     #by='user_type', bins=25, grid=False, figsize=(8,10), layout=(3,1), sharex=True, color='#86bf91', zorder=2, rwidth=0.9)
     

     #df2.hist(column='MB', by='direction', bins=25, grid=False, figsize=(8,10), layout=(2,1), sharex=True,) 
     #plt.show()

#-------------------------------------------
def show_traffic_total(start, end, companies=None):
#-------------------------------------------
   #for table in ['jangle_traffic_total', 'radius_traffic_total']:
   for table in ['jangle_traffic_total']:  
     sql= sql_traffic_total(start, end, table, companies)
     print(sql)
     df=query(sql)
     print(df)
     print(df.dtypes)
     print(df.describe())

     #range  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
     df['date'] = pd.to_datetime(df['date'])
     print(df.columns)
     #df["MB"]=df["MB"].astype("float64")
     #print("after conversion df.columns=")
     #print(df.columns)

     for company in companies:
        s=str(company)
        df[df["company"] == company].hist(column="MB", rwidth=0.9, bins=30)
        plt.show()

        #show_adtk(df["MB"])
     #print("fill NA with 0")
     #df=df.fillna(0)


     df2=pd.pivot_table(df, values='MB', columns='company' , index=['date'])
     print("AFTER pivot_table()  df2.columns=")
     print(df2.columns)

     #range  = pd.date_range(start=df2["date"].min(), end=df2["date"].max(), freq='H')

     #df2.set_index('date', inplace=True)
     #d2f=df2.reindex(range)

     print(df2)
     print(df2.describe())
     print(df2.info())
     print(df2.columns)
     print("show_traffic_total")
     header="Hourly Traffic (MB). Table: "+table+ ". From " + start + "  till " + end
     if companies:
        header += " Companies: "+str(companies)
     #df2.plot(title=header, style=".")  -- useful too see gaps
     #plt.show()

     df2.plot(title=header)
     plt.show()

     
          

     print("reindex")
     interval  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
     df.set_index('date', inplace=True)
     d2=df.reindex(interval)
     for company in companies:
       print("company=",company)
       ts = df[df["company"] == company]
       show_adtk(ts["MB"])
     #   s=str(company)
     #   df2.hist(column=s )
     #   plt.show()
     
     y_max=input("Set Y-max to re-scale :")
     if not y_max:
        return
     else:
       y_max = int(y_max)
       df2.plot(title=header, ylim=(0,y_max))
       plt.show()
#----------------------------------
def sql_jangle_traffic_per_device(company, start, end, direction=None): # granularity='hour'):
#-----------------------------------

  timescale= '%%Y-%%m-%%d %%H'
  if not direction:
    filter="1=1"
  else:
    filter="direction="+str(direction) 

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   (SUM(bytes) * 1.0 / (1024.0 * 1024.0)  / count(distinct msisdn)) as MB,
   count(distinct msisdn) as n_msisdn
   FROM jangle_traffic
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company =  {company}
   and {filter}
   GROUP BY date
   ORDER BY date
  """

  return SQL


#----------------------------------
def sql_traffic_protocol(start, end, table, companies, direction=None): # granularity='hour'):
#-----------------------------------  
  #COMPANY_LIST=(3659,3116, 3666)
  timescale= '%%Y-%%m-%%d %%H'
  #else: # day
  #       timescale= '%%Y-%%m-%%d'

  #print(timescale)

  if companies and len(companies) == 1:
     companies="("+ str(companies[0]) +")"

  if not direction:
    direction_filter="1=1"
  else:
    direction_filter="direction="+str(direction)

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   company,
   CASE
       WHEN protocol=1 THEN 'ICMP'
       WHEN protocol=6 THEN 'TCP'
       WHEN protocol=17 THEN 'UDP'
       WHEN protocol=112 THEN 'VRRP'
       ELSE 'Others'
    END as Protocol,  
   SUM(bytes) * 1.0 / (1024.0 * 1024.0)  as MB
   FROM {table}
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company IN  {companies}
   and {direction_filter}
   GROUP BY date, company, Protocol
   ORDER BY date
  """

  return SQL


#----------------------------------
def sql_traffic_total_per_direction(start, end, table, companies): # granularity='hour'):
#-----------------------------------  
  #COMPANY_LIST=(3659,3116, 3666)
  timescale= '%%Y-%%m-%%d %%H'
  #else: # day
  #       timescale= '%%Y-%%m-%%d'

  #print(timescale)

  if companies and len(companies) == 1:
     companies="("+ str(companies[0]) +")"

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   company, 
   direction,
   SUM(bytes) * 1.0 / (1024.0 * 1024.0)  as MB
   FROM {table}
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company IN  {companies}
   GROUP BY date, company, direction
   ORDER BY date
  """

  return SQL

#----------------------------------
def sql_traffic_total(start, end, table, companies ): # granularity='hour'):
#-----------------------------------  
  #COMPANY_LIST=(3659,3116, 3666)
  timescale= '%%Y-%%m-%%d %%H'
  #else: # day
  #       timescale= '%%Y-%%m-%%d'

  #print(timescale)

  if companies and len(companies) == 1:
     companies="("+ str(companies[0]) +")"

  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as date,
   company,
   SUM(bytes) * 1.0 / (1024.0 * 1024.0)  as MB
   FROM {table}
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company IN  {companies}
   GROUP BY date, company
   ORDER BY date
  """

  return SQL

#-----------------------------------
def create_features(df, label=None, useLags=False):
#-----------------------------------
#  https://pandas-docs.github.io/pandas-docs-travis/reference/api/pandas.DatetimeIndex.html
    df['hour'] = df.index.hour
    df["morning"] = ((df['hour'] >= 7) & (df['hour'] <= 11)).astype('int')
    df["middleday"] = ((df['hour'] >= 12) & (df['hour'] <= 18)).astype('int')
    df["evening"] = ((df['hour'] >= 19) & (df['hour'] <= 23)).astype('int')
    df["night"] = ((df['hour'] >= 0) & (df['hour'] <= 6)).astype('int')

    df['dayofweek'] = df.index.dayofweek

    first_date=df.index.array[0]
    #print(first_date)
    #exit(0)

    df['daysfromstart'] = 1 + (df.index - first_date).astype('timedelta64[D]').astype(int)

    #print(df['daysfromstart'])
    print("Adding lag")
    if useLags:
      df["Lag_1"]=df["MB"].shift(1)
      df["Lag_2"]=df["MB"].shift(2)
      df["Lag_3"]=df["MB"].shift(3)
      df["Lag_4"]=df["MB"].shift(4)

      #print("Lag_1 NULL :", df['Lag_1'].isnull().sum())
      #print("Lag_2 NULL :", df['Lag_2'].isnull().sum())
      #print("Lag_3 NULL :", df['Lag_3'].isnull().sum())
      #print("Lag_4 NULL :", df['Lag_4'].isnull().sum())
      #print("before len(df)=", len(df) ) 
      
      #print("remove first 4 rows since no Lag data")
      
      #df=df[4:].copy()
      #print("Fill NA")
      df['Lag_1'] = df['Lag_1'].fillna(df["MB"])
      df['Lag_2'] = df['Lag_2'].fillna(df["MB"])
      df['Lag_3'] = df['Lag_3'].fillna(df["MB"])
      df['Lag_4'] = df['Lag_4'].fillna(df["MB"])

      #print("Lag_1 NULL :", df['Lag_1'].isnull().sum())
      #print("Lag_2 NULL :", df['Lag_2'].isnull().sum())
      #print("Lag_3 NULL :", df['Lag_3'].isnull().sum())
      #print("Lag_4 NULL :", df['Lag_4'].isnull().sum())

      #print("after len(df)=", len(df) )
      #print(df.head(5))
      X = df[[
            'hour',
            'dayofweek',
            'daysfromstart',
            'morning',
            'middleday',
            'evening',
            'night',
            'Lag_1',
            'Lag_2',
            'Lag_3',
            'Lag_4'
          ]]
    else: # not use Lags
      X = df[[
            'hour',
            'dayofweek',
            'daysfromstart',
            'morning',
            'middleday',
            'evening',
            'night'
      ]]

    #print (df.dtypes)

    if label:
        y = df[label]

        #print("len(X)=", len(X), "len(Y)=",len(y))
        #exit(0)

        return X, y


    return X

#----------------
def predict_xgboost(df, comment, useLags):
#-----------------

     if useLags:
        train_len = len(df)-1
     else:
        split=0.8  # between test and train
        train_len=int( split * len(df) )

     train=df[0:train_len].copy()
     test=df[train_len:].copy()
     test_len=len(test)
     print("train_len=", train_len, "test_len=", test_len)


     #print(test)

     #print(test.info())
     #print(test.describe())
     #print(test.columns)
     #print(test.dtypes)

     #print(train.head(5))



     #temps = pd.DataFrame(train.values)
     #dataframe = pd.concat([temps.shift(1), temps], axis=1)
     #dataframe = concat([temps.shift(3), temps.shift(2), temps.shift(1), temps], axis=1)
     #dataframe.columns = ['t-3', 't-2', 't-1', 't+1']
     #dataframe.columns = ['t-1', 't+1']
     #print(dataframe.head(5))

     #exit(0)

     concat= test.rename(columns={'MB':'TEST'}) \
     .join( train.rename(columns={'MB':'TRAIN'}) , how='outer')

     if False:
       concat.plot(title=comment + ' Train: '+str(train_len) + ' points and Test: '+str(test_len) + " points", linestyle='-', marker='o', figsize=(25, 5))
       plt.show()


     X_train, y_train = create_features(train, label='MB', useLags=useLags)
     print("len(X_train)=", len(X_train), "len(Y_train)=",len(y_train))

     X_test,  y_test  = create_features(test,  label='MB', useLags=useLags)
     print("len(X_test)=", len(X_test), "len(Y_test)=",len(y_test))

     # https://www.kaggle.com/robikscube/time-series-forecasting-with-prophet
     features_and_target = pd.concat([X_train, y_train], axis=1)
     #print(features_and_target.head())

     x_vars=[
              'hour',
              'dayofweek',
              'daysfromstart',
              'morning',
              'middleday',
              'evening',
              'night'
             ]
     if useLags:
             x_vars.append('Lag_1')
             x_vars.append('Lag_2')
             x_vars.append('Lag_3')
             x_vars.append('Lag_4')

     #sns.pairplot(features_and_target.dropna(),
     #        hue= 'hour',
     #        x_vars=x_vars,
     #        y_vars='MB',
     #        height=5 
     #       )
     #plt.suptitle('Traffic by Day of Month, Day of Week and Hour')
     #plt.show()

     #reg = xgb.XGBRegressor(n_estimators=1000)
     reg = xgb.XGBRegressor(
       n_estimators = 1600 ,
       random_state = 0 ,
       # objective='reg:squarederror',  # 'reg:linear'
       # 'booster':'gblinear'
       max_depth = 15)

     #reg = XGBRegressor(base_score=0.5, booster='gbtree', colsample_bylevel=1,
     #    colsample_bynode=1, colsample_bytree=0.3, gamma=0,
     #    importance_type='gain', learning_rate=0.1, max_delta_step=0,
     #    max_depth=15, min_child_weight=1, missing=None, n_estimators=1000,
     #   n_jobs=1, nthread=None, objective='reg:linear', random_state=0,
     #    reg_alpha=0, reg_lambda=1, scale_pos_weight=1, seed=None,
     #    silent=None, subsample=0.5, verbosity=1) 


     reg.fit(X_train, y_train,
        eval_set=[(X_train, y_train), (X_test, y_test)],
        early_stopping_rounds=50,
        verbose=False)

     # Feature importance
     if False:
       plot_importance(reg, height=0.9)
       plt.show()

     print("Before Prediction")
     test['Prediction'] = reg.predict(X_test)


     print("Before concat len(test)=",len(test), "  len(train)=",len(train))
     all = pd.concat([test, train], sort=False)
     print("After concat len(all)=",len(all))

     if not useLags:
       header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       all[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

     print ("Len all=", len(all))
     print (  "Train len=",   len(train), train.index[0], train.index[-1])
     print (  "Test  len=",   len(test),  test.index[0],  test.index[-1])

     predicted   = all.loc[test.index[0]:test.index[-1]]
     print("Len predicted =", len(predicted ))
     print( "predicted=" )
     print( predicted )

     if not useLags:
        predicted[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
        plt.show()
        return

     print("test.dtypes=")
     print(test.dtypes)
     print("df.dtypes=")
     print(df.dtypes)
     #test.drop('MB',axis=1)

     print("test=")
     print(test)
     cols=['MB','hour', 'morning', 'middleday', 'evening', 'night', 'dayofweek','daysfromstart', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4']
     test.drop(columns=cols, inplace=True)
     test.rename(columns = {'Prediction':'MB'}, inplace = True) 
     print("after drop test=")
     print(test)

     cc = pd.concat([df[:-1], test], sort=True)
     #print ("len(c)=", len(cc))
     #print(cc.dtypes)
     print("Check the sort order below after concat")
     print(cc.tail(10))
     print("Check the sort order above ")
     #exit(0)
     #cols=['hour', 'morning', 'middleday', 'evening', 'night', 'dayofweek','daysfromstart', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4']
     #cols=['hour', 'morning', 'middleday', 'evening', 'night', 'dayofweek','daysfromstart', 'Lag_1', 'Lag_2', 'Lag_3', 'Lag_4', 'Prediction']
     #cc.drop(columns=cols, inplace=True)
     return cc
#-----------------
def get_company():
#-----------------  
   DEFAULT_COMPANY=3659
   company_input=input("Company: (default 3659) :")
   if not company_input:
        return DEFAULT_COMPANY
   else:
       return int(company_input)
#----------------
def get_start():
#---------------
  start_input = input("Enter start day (YYYY-MM-DD) (default 2020-11-01) : ")
  if not start_input:
      return "2020-11-01"
  elif  len(start_input) != 10:
      print("Error in input- format is YYYY-MM-DD")
      exit(1)
  else:
      return start_input

#------------------
def get_duration():
#-----------------
      duration = input("""Enter duration in days (default 7 days) :  """)

      if not duration :
         return 7  # 1 week
      else:
         return int(duration)
#---------------------------
def device_count(start, end):
#---------------------------
     sql = sql_n_devices(start, end, companies)
     print(sql)
     df=query(sql)
     print(df)

#------------
def main():
#----------

  datastore.connect()

  width=20
  height=5
  plt.rcParams['figure.figsize'] = [width, height]

  #COMPANY_LIST=(3659,3116, 3666)
  #COMPANY_LIST=(3666,)
  #start='2020-10-01'
  #end  ='2021-01-01'

  #COMPANY_LIST=(3659,3116, 3666)
  #COMPANY_LIST=(3659,3116)
  #COMPANY_LIST=(3659,)
  #COMPANY_LIST=(3116, 3666)
  COMPANY_LIST=(3659,)

  start = get_start()
  n_days=get_duration()
  end = (datetime.strptime(start, '%Y-%m-%d') + timedelta(days=n_days)).strftime('%Y-%m-%d')

  if 0:
    for company in COMPANY_LIST:
      show_traffic_hourly_per_day_of_week(start, end, company)

   
  #show_top_traffic(start, end)
  #exit(0)
  #show_top_device_count(start, end)
  #exit(0)



  if  True:
    show_traffic_total(start, end, COMPANY_LIST)
    #exit(0)

    for company in COMPANY_LIST:
      single_company=list()
      single_company.append(company)
      #show_traffic_total(start, end, single_company)
      show_traffic_total_per_direction(start, end, single_company)
      #show_traffic_protocol(start, end, single_company)

  exit(0)

  #show_device_count(start, end)
  #show_device_count(start, end, COMPANY_LIST)
  # https://stackoverflow.com/questions/22483588/how-can-i-plot-separate-pandas-dataframes-as-subplots
  # https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html
  # TO DO: lag plot, autocorrelation plot
 

  #company=get_company()
  #COMPANY_LIST=[]
  #COMPANY_LIST.append(company)
  for company in COMPANY_LIST:
    for direction in [1,2]:
     print(company, direction)

     sql = sql_jangle_traffic_per_device(company, start, end, direction)
     print(sql)
     df=query(sql)
     print(df)
     print(df.describe())
#     df.plot(title="no indexed")
#     plt.show()

     # index
     date_range  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
     #df = df.set_index('date').reindex(r).fillna(1.0).rename_axis('date').reset_index()
     df['date'] = pd.to_datetime(df['date'])
     df.set_index('date', inplace=True)
     df=df.reindex(date_range)
     print(df.index)
     print(df.count())
     print( "df[MB].count()=")
     print(df["MB"].count())

     head="Company=" + str(company) + ". Hourly Traffic (MB) per device. " + start + ' - ' + end + "  direction="+str(direction)
     df.plot(title=head)
     plt.show()
     ######################################
     # continue
     ######################################

     print("fill NA with 0")
     df=df.fillna(0)
     #df.index.freq='H'

     print(df.count())
     print( "df[MB].count()=")
     print(df["MB"].count()) 

     print(df.describe())

     head="Company=" + str(company) + ". Hourly Traffic (MB) per device with filled gaps. " + start + ' - ' + end + "  direction="+str(direction)
     df.plot(title=head)
     plt.show()

     #df.plot(title=head, style=".") 
     #plt.show()

     #df.plot(title=head, ylim=(0,200))
     #plt.show()
     df=df.drop('n_msisdn', axis=1)
     useLags=True
     #useLags=False
     comment="XGBoost. Hourly Traffic (MB) per # of devices. Company "+ str(company) + " direction="+str(direction)
     if not useLags:
       predict_xgboost(df, comment, useLags)
       continue

     else:
        #feedto xgb  df[1...10] -> get back df[1,...,10xb]
        #add to df[1,...,10xb] df[11] ->  get back df[1,...,10xb, 11b]
       N_points=24
       head=df[:-N_points].copy()
       tail=df[-N_points:].copy()
         #head=df.copy()
       all = predict_xgboost(head, comment, useLags)
       print (all.tail())
       #for j in g(): #range(10):
       #    print(j)
       # continue
       print("i=0 after predict_xgboost len=",len(all))
     #if useLags:
       #for i in [0,1,2,3,4]:  # predict 1 point at the time
       #it=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]
       #it=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
       for i in range(0, N_points):
           print("---i=", i)


           print("-- step 1: tail.index[i]=")
           print(tail.index[i])
           print("one_rec=") 
           one_rec = tail[tail.index == tail.index[i]]
           print(one_rec)

           print("-- step 4a - BEFORE concatenate: all.tail(10)=")
           print (all.tail(10))
           all=pd.concat([all, one_rec], sort=True)
           print("-- step 4 - after concatenate: all.tail(10)=")
           print (all.tail(10))
           print("Make sure the order of time above is correct!!! ")
           #exit(0)
           all = predict_xgboost(all, comment, useLags)
           print("i=", i," after predict_xgboost len=",len(all))
       
       # Final plot
       pred = all[-i:].copy()
       pred.rename (columns={'MB':'Prediction'}, inplace=True)
       #  Plot
       x = pd.concat([df, pred], axis=1, join="outer")
       print("After concat join=outer len(x)=",len(x))
       print(x)
       print(x.index)
       print("x.tail(10)=")
       print(x.tail(10))
       print(" is sort good above join=outer")
       # https://realpython.com/pandas-merge-join-and-concat/
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       header="Company "+str(company) + " direction="+str(direction)
       x[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

      ## Concat
       #x_overlap = pd.concat([df[-N_points:], pred], axis=1, join="inner")
       x_overlap = pd.concat([df, pred], axis=1, join="inner")
       print("After concat len(x_overlap)=",len(x_overlap))
       print(x_overlap)
       print(x_overlap.index)
       # https://realpython.com/pandas-merge-join-and-concat/
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       #header="final _overlap sorted"
       x_overlap[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()

       ##  Merge
       #print("Merge")
       #x_merge = pd.merge( df[-N_points:], pred )
       #print("After merge len(x_merge)=",len(x_merge))
       #print(x_merge)
       #print(x_merge.index)
       # https://realpython.com/pandas-merge-join-and-concat/
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       #header="final _merge"
       #x_merge[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       #plt.show()

       ##  Join
       print("Join")
       #x_join = df[-N_points:].join(pred)
       x_join = df.join(pred)
       print("After join len(x_join)=",len(x_join))
       print(x_join)
       print(x_join.index)
       # https://realpython.com/pandas-merge-join-and-concat/
       #header= comment + " range " + str(test.index[0]) + " -  " + str(test.index[-1])
       header="final _join"
       x_join[['MB','Prediction']].plot(title=header, linestyle='-', marker='o', figsize=(25, 5))
       plt.show()


if __name__ == "__main__":
  main()

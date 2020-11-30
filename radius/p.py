import time
import numpy as np
import pandas as pd

from plotnine import *

import companies
import datastore
import mellycount
import radius
import timeseries
import read_traffic


def query(sql):
  datastore.start_transaction(readonly=True)
  d=datastore.query(sql)
  datastore.commit()
  return d

SQL_imei="""
SELECT company, msisdn, COUNT(imei) AS imei_count
FROM subscriber_imei
WHERE imei != 0 
GROUP BY company, msisdn
"""
 
SQL_imsi="""
SELECT company, msisdn, COUNT(imsi) AS imsi_count
FROM subscriber_imsi
WHERE imei != 0 
GROUP BY company, msisdn
"""
 
SQL_sgsn= """
SELECT company, msisdn, COUNT(sgsn_mccmnc) AS mccmncs
FROM subscriber_sgsn
WHERE sgsn_mccmnc != 0
GROUP BY company, msisdn
"""

SQL_location= """
SELECT company, msisdn, COUNT(*) AS locations
FROM subscriber_location
GROUP BY company, msisdn
"""

SQL_logins = """
SELECT company, msisdn, COUNT(*) AS logins
FROM subscriber_login 
GROUP BY company, msisdn
"""
SQL_failures = """
SELECT company, msisdn, COUNT(*) AS failures
FROM subscriber_login
WHERE status = 10 
GROUP BY company, msisdn
"""
SQL_traffic= """
SELECT company, msisdn, SUM(bytes) AS bytes_in
FROM radius_traffic 
WHERE 
direction = 1
AND company != 0
GROUP BY company, msisdn
"""

if __name__ == "__main__" :
  datastore.connect()
  q="SELECT count(*) FROM companies"
  q="SELECT company, count(*) as cnt FROM radius_traffic WHERE company > 0 GROUP BY company" # order by 2 "
  q="""
    select 'subscriber_imei' as tbl, 
           FROM_UNIXTIME(min(last_seen)), 
           FROM_UNIXTIME(max(last_seen)),
           HOUR(FROM_UNIXTIME(min(last_seen))) 
    from subscriber_imei
   """ 

  start='2020-01-01'
  end  ='2020-01-02' 

  for month in ['01','02', '03','04','05','06','07','08','09','10','11']:
   if 0>1:
      q_daily="""
       SELECT  FROM_UNIXTIME(timebin, '%%d') as day,
       SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB
       FROM jangle_traffic_total
       WHERE 
          FROM_UNIXTIME(timebin, '%%Y') = 2020
          AND 
          FROM_UNIXTIME(timebin, '%%m')  = '""" 
      q_daily += month +"'"
      q_daily += " GROUP BY FROM_UNIXTIME(timebin, '%%d')"

      print (q_daily)
      data=query(q_daily)
      print(data)


      g = (
        ggplot(data)
        + aes(x="day", y="GB")
        + geom_point()
        + labs(title="jangle_traffic_total month="+ month, y="GB", x='day')
      )
      print(g)
      g.save(month)

  for month in ['01','02', '03','04','05','06','07','08','09','10','11']:

      q_hourly="""
        SELECT 
         HOUR(FROM_UNIXTIME(timebin))  AS hour, 
         SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB
        FROM jangle_traffic_total 
        WHERE 
           FROM_UNIXTIME(timebin, '%%Y') = 2020
           AND 
           FROM_UNIXTIME(timebin, '%%m')  = '"""
      q_hourly += month +"'"
      q_hourly += " GROUP BY FROM_UNIXTIME(timebin, '%%H')"

  


      print (q_hourly)
      data=query(q_hourly)
      print(data)


      g = (
        ggplot(data)
        + aes(x="hour", y="GB")
        + geom_point()
        + labs(title="jangle_traffic_total group by hour, month="+ month, y="GB", x='hour')
      )
      print(g)
      g.save("hourly-month-"+month)

 
  exit(1)

  q_month_daily="""
       SELECT
           FROM_UNIXTIME(timebin, '%%m') as month,
           FROM_UNIXTIME(timebin, '%%d') as day,
           SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB
       FROM jangle_traffic_total
       WHERE FROM_UNIXTIME(timebin, '%%Y') = 2020
       GROUP BY 
          FROM_UNIXTIME(timebin, '%%m'),
          FROM_UNIXTIME(timebin, '%%d') 
  """

  print(q_month_daily)
  data=query(q_month_daily)
  print (data)

  g = (
        ggplot(data)
        + aes(x="day", y="GB")
        + geom_point()
        + facet_wrap('~month', ncol=3)
        + labs(title="jangle_traffic_total (faced_wrap)", y="GB", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="GB")
        + geom_point()
        + facet_wrap('~month', ncol=3, scales='free_y')
        + labs(title="jangle_traffic_total (facet_wrap, free_y)", y="GB", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="GB")
        + geom_point()
        + facet_grid('~month' )
        + labs(title="jangle_traffic_total (facet_grid)", y="GB", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="GB")
        + geom_point()
        + facet_grid('~month', scales='free_y' )
        + labs(title="jangle_traffic_total (facet_grid, free_y)", y="GB", x='day')
      )
  print(g)

  # exit(1)

  q_monthly="""
     SELECT 
         FROM_UNIXTIME(timebin, '%%m') as month,
          SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB
     FROM jangle_traffic_total
     WHERE FROM_UNIXTIME(timebin, '%%Y') = 2020
     GROUP BY FROM_UNIXTIME(timebin, '%%m') 
  """

  print(q_monthly)
  data=query(q_monthly)
  print (data)

  g = (
      ggplot(data)
      + aes(x="month", y="GB")
      + geom_point()
      + labs(title="jangle_traffic_total", y="GB", x='month')
    )
  print(g)

  exit(1)

  q_hourly="""
     SELECT 
         HOUR(FROM_UNIXTIME(timebin))  AS hour, 
         SUM(bytes) AS bytes, 
         direction 
     FROM jangle_traffic_total 
     WHERE timebin >= UNIX_TIMESTAMP('%s') 
           and timebin < UNIX_TIMESTAMP('%s')
     GROUP BY 
        HOUR(FROM_UNIXTIME(timebin)) , 
        direction
  """ % ( start , end )

  q_day_name="""
       SELECT
           DAYNAME(FROM_UNIXTIME(timebin))  AS dayname,
           SUM(bytes) AS bytes,
           direction
       FROM jangle_traffic_total
       WHERE timebin >= UNIX_TIMESTAMP('%s') 
             and timebin < UNIX_TIMESTAMP('%s')
       GROUP BY
          DAYNAME(FROM_UNIXTIME(timebin)) ,
          direction
  """ % ( start , end )


  print(q_monthly)
  data=query(q_monthly)
  print (data)  



  exit(1)

  print(q_hourly)
  data=query(q_hourly)
  print (data)  

  print(q_day_name)
  data=query(q_day_name)
  print (data)  

  exit(1)



  g = (
    ggplot(data)
    + aes(x="company", y="cnt")
    + geom_point()
    + labs(title="Head title", y="y_title")
  )
  print(g)   


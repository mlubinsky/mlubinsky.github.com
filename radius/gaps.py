import time
from datetime import datetime, timedelta

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


import xgboost as xgb  # conda install py-xgboost-cpu
from xgboost import plot_importance, plot_tree
import datastore

#--------------
def query(sql):
#-------------
  datastore.start_transaction(readonly=True)
  d=datastore.query(sql)
  datastore.commit()
  return d


def make_sql(table):

  sql=f"""
   SELECT 
      (timebin - prev_bin)/3600.0 as gap_hours, 
      FROM_UNIXTIME(timebin) as time, 
      FROM_UNIXTIME(prev_bin) as prev_time
   FROM  
   (   
     SELECT  timebin, LAG(timebin, 1) OVER (ORDER BY timebin) as prev_bin
     FROM {table}
     WHERE
        timebin >=  UNIX_TIMESTAMP('2020-10-01') and
        timebin  <  UNIX_TIMESTAMP('2021-01-01')  
     ) A  
     ORDER BY gap_hours desc limit 10
  """
  return sql



datastore.connect()
tables=['radius_traffic_total', 'radius_events_total', 'jangle_traffic_total', 'jangle_tcp_total', 'cdr_traffic_total']
for t in tables:
   print(t)
   sql=make_sql(t)
   print(sql)

   d=query(sql)
   print(d)



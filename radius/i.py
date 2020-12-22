import time
from datetime import datetime, timedelta
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

def all_company_total(start, end):

  SQL=f"""
   SELECT
   CAST(company as char(30)) AS company,
   SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB_company 
   FROM jangle_traffic_total
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}')
   and company IN {COMPANY_LIST}
   GROUP BY company
   ORDER BY GB_company desc
   LIMIT 5
  """ 

  return SQL

def all_company_daily(start=None, end=None, timescale=None):

  if timescale == "day-hour":
       timescale='%%d-%%H'
  elif timescale == "hours":
       timescale='%%H'
  else:
       timescale= '%%m-%%d'


  SQL=f"""
   SELECT
   FROM_UNIXTIME(timebin, '{timescale}') as timescale,
   CAST(company as char(30)) AS company,
   SUM(bytes) * 1.0 / (1024.0 * 1024.0) as MB_company 
   FROM jangle_traffic_total
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company IN {COMPANY_LIST}
   GROUP BY company, timescale
   ORDER BY timescale
  """

  return SQL

def single_company_all_directions(company, start, end, timescale=None):

  if timescale == "day-hour":
       timescale='%%d-%%H'
  elif timescale == "hours":
       timescale='%%H'
  elif timescale == "minutes":
      timescale='%%H:%%i'
  else:
      timescale= '%%m-%%d'


  SQL=f"""
   SELECT
     FROM_UNIXTIME(timebin, '{timescale}') as timescale,
     SUM(bytes) * 1.0 / (1024.0 * 1024.0 ) as MB,
     CAST(direction as char(10)) AS Direction
   FROM jangle_traffic_total
   WHERE
     timebin >=  UNIX_TIMESTAMP('{start}') and
     timebin  <  UNIX_TIMESTAMP('{end}') and
     company =  {company}
   GROUP BY timescale, Direction
   ORDER BY timescale
  """

  return SQL

#-----------------------------------------------------------------------
def single_company_single_direction(company, start, end, timescale, direction):
#-----------------------------------------------------------------------
  if timescale == "day-hour":
       timescale='%%d-%%H'
  elif timescale == "hours":
       timescale='%%H'
  elif timescale == "minutes":
      timescale='%%H:%%i'
  else:
      timescale= '%%m-%%d'

  SQL=f"""
   SELECT
     FROM_UNIXTIME(timebin, '{timescale}') as timescale,
     SUM(bytes) * 1.0 / (1024.0 * 1024.0 ) as MB
   FROM jangle_traffic_total
   WHERE
     timebin >=  UNIX_TIMESTAMP('{start}') and
     timebin  <  UNIX_TIMESTAMP('{end}') and
     company =  {company}
     and direction = {direction}
   GROUP BY timescale
   ORDER BY timescale
  """

  return SQL
#------------------------------------------------------------
def single_company_protocol(company, start, end, timescale):
#------------------------------------------------------------
  if timescale == "day-hour":
       timescale='%%d-%%H'
  elif timescale == "hours":
       timescale='%%H'
  elif timescale == "minutes":
      timescale='%%H:%%i'
  else:
      timescale= '%%m-%%d'


  SQL=f"""
   SELECT
     FROM_UNIXTIME(timebin, '{timescale}') as timescale,
     CAST(protocol as char(20)) AS   protocol,
     SUM(bytes) * 1.0 / (1024.0 * 1024.0 ) as MB
   FROM jangle_traffic_total
   WHERE
     timebin >=  UNIX_TIMESTAMP('{start}') and
     timebin  <  UNIX_TIMESTAMP('{end}') and
     company =  {company}
   GROUP BY timescale, protocol
   ORDER BY timescale
  """

  return SQL  

def devices(start, end, timescale):

  if timescale == "hours":
     timescale='%%H'
  else:
     timescale= '%%m-%%d'

  SQL=f"""
   SELECT 
     CAST(company as char(20)) AS company,  
     FROM_UNIXTIME(timebin, '{timescale}') as timescale,
     count(distinct msisdn) as n_msisdn,
     SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB_company,
     SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) / count(distinct msisdn) as GB_per_dev
   FROM jangle_traffic
   WHERE
     timebin >=  UNIX_TIMESTAMP('{start}') and
     timebin  <  UNIX_TIMESTAMP('{end}')  and
     company IN {COMPANY_LIST}
   GROUP BY company, timescale
   ORDER BY timescale
  """

  return SQL

def single_company_device(company, start, end, timescale=None):
  # Top 5 devices  
  # protocol, remote_ip, apn, direction, packets  

  if timescale == "day-hour":
       timescale='%%d-%%H'
  elif timescale == "hours":
     timescale='%%H'
  elif timescale == "minutes":
    timescale='%%H:%%i'
  else:
       timescale= '%%m-%%d'


  SQL=f"""
   SELECT
   CAST(msisdn as char(50)) AS msisdn,
   CAST(FROM_UNIXTIME(timebin, '{timescale}') as char(40)) as timescale,
   SUM(bytes) * 1.0 / (1024.0 * 1024.0 ) as MB
   FROM jangle_traffic
   WHERE
   timebin >=  UNIX_TIMESTAMP('{start}') and
   timebin  <  UNIX_TIMESTAMP('{end}') and
   company =  {company} and
   msisdn IN
   (
     SELECT msisdn from (
       SELECT 
          msisdn, 
          SUM(bytes)  as sum_bytes
       FROM jangle_traffic
       WHERE
         timebin >=  UNIX_TIMESTAMP('{start}') and
         timebin  <  UNIX_TIMESTAMP('{end}') and
         company =  {company}
       GROUP BY msisdn
       ORDER BY sum_bytes DESC
       LIMIT 5
     ) A
   )
   GROUP BY msisdn, timescale
   ORDER BY timescale
  """

  return SQL


#--------------------------------------
def plot_all_company_total(start, end, n_days):
#--------------------------------------
  q=all_company_total(start, end)
  print(q)
  data=query(q)
  print(data)

  g = (
        ggplot(data)
        + geom_bar(
            mapping=aes(x="company", 
                        y="GB_company", 
                        fill="company"),
            stat="identity"
          )
         + labs(title="Traffic: start="+start+ "  days="+str(n_days), x='company') 
        )
  print(g)

#--------------------------------------------------
def  plot_all_company_daily(start, end, n_days, granularity):
#--------------------------------------------------    
  q=all_company_daily(start,end, granularity)
  print(q)
  data=query(q)
  print(data)

  #print("BEFORE geom_col")
  #g = (
  #   ggplot(data, aes("timescale", "MB_company", fill="company"))
  #   + geom_col(position=position_stack(reverse=True))
  #   + labs(title="Traffic(geom_col) for top companies start="+start+ "  days="+str(n_days) , x='time')

  #)
  #print(g)

  print("BEFORE stat=identity")
  g = (
        ggplot(data)
        + geom_bar(
            mapping=aes(x="timescale",
                        y="MB_company",
                        fill="company"),
            stat="identity"
          )
          + labs(title="Traffic vs time:  start="+start+ "  days="+str(n_days) , x='time')

        )
  print(g)

  #----------------------------------
  print("Company Traffic vs time ")
  if n_days > 1: granularity="day-hour"
  q=all_company_daily(start,end, granularity)
  print(q)
  data=query(q)
  print(data)

  g = (
        ggplot(data,
         aes(x="timescale", y="MB_company", color="company")
        )
        + geom_point()
        + labs(title="Traffic:  start="+start+ "  days="+str(n_days) , x='time')
  )

  print(g)


#--------------------------------------------------
def  plot_single_company_protocol(company, start, end, n_days, granularity):
#--------------------------------------------------    

  print("Company Traffic / protocol vs time ")
  if n_days > 1: granularity="day-hour"
  q=single_company_protocol(company, start,end, granularity)
  print(q)
  data=query(q)
  print(data)

  g = (
        ggplot(data,
         aes(x="timescale", y="MB", color="protocol")
        )
        + geom_point()
        + labs(title="Traffic/protocol: company="+str(company)+"  start="+start+ "  days="+str(n_days) , x='time')
  )

  print(g)


#----------------------------------------
def  plot_devices(start, end, n_days, granularity):
#----------------------------------------
  q=devices(start,end, granularity)
  print(q)
  data=query(q)
  print(data)

  print("n_msisdn BEFORE geom_col")
  g = (
     ggplot(data, aes("timescale", "n_msisdn", fill="company"))
     + geom_col(position=position_stack(reverse=True))
     + labs(title="# of devices start="+start+ "  days="+str(n_days) + "  (geom_col)" , x='time')

  )
  print(g)

  #print("n_msisdn BEFORE stat=identity")
  #g = (
  #      ggplot(data)
  #      + geom_bar(
  #          mapping=aes(x="timescale",
  #                      y="n_msisdn",
  #                      fill="company"),
  #          stat="identity"
  #        )
  #        + labs(title="Number of devices start="+start+ "  days="+str(n_days) , x='time')

  #      )
  #print(g)

#----------------------------------------
def plot_single_company_all_directions(company, start, end, n_days,  granularity):
#----------------------------------------
 # for direction in [1,2]:
  q=single_company_all_directions(company, start, end, granularity)
  print(q)
  data=query(q)
  print(data)

  if data.empty:
    print (" NO DATA for direction=", direction, "  company=", company)
    return


  print("plot_single_company direction granularity=", granularity)

  #g = (
  #     ggplot(data)
  #      + geom_line(aes(x="timescale", y="MB", color="Direction"), group=1)
  #      + labs(title="company="+str(company)+"  start="+start+ "  days="+str(n_days) , x='time')
  #    )
  #print(g)

  print("SINGLE COMPANY trying to adjust the x-marks")
  # https://github.com/has2k1/plotnine/issues/335

  # geom_path.py:83: PlotnineWarning: geom_path: 
  # Each group consist of only one observation. Do you need to adjust the group aesthetic?
  #g = (
  #     ggplot(data,
  #            aes(x="timescale", y="MB", color="Direction")
  #            )
  #      + geom_line(group="ignored")
  #      + labs(title="company="+str(company)+"  start="+start+ "  days="+str(n_days) , x='time')
  #    )
  x_start=1  ## todo
  x_end = x_start + n_days

  g = (
        ggplot(data,
         aes(x="timescale", y="MB", color="Direction")
        )
        + geom_point()
        # + scale_x_continuous(breaks = np.arange(x_start, x_end, 1))
        + labs(title="Traffic by direction: company="+str(company)+"  start="+start+ "  days="+str(n_days) , x='time')
      )

  print(g)

  #  Histogram for directions 1,2
  # for direction in [1,2]:
  #   q=single_company_direction(company, start, end, granularity, direction)
  #   print(q)
  #   data=query(q)
  #   print(data)
  #   if not data: continue
  #   g = (
  #      ggplot(data,  aes("MB"))
  #      + geom_histogram(binwidth=1,
  #        colour="darkmagenta", fill="orchid")
  #      + labs(title="company="+str(company)+"  start="+start+ "  days="+str(n_days) + " direction="+str(direction), x='MB')
  #   )
  #   print(g)

#----------------------------------------
def  plot_single_company_device(company, start, end, n_days, granularity):
#----------------------------------------
  q=single_company_device(company, start, end, granularity)
  print(q)
  data=query(q)
  print(data)


  print("SINGLE COMPANY DEVICE")
  # Error AttributeError: 'float' object has no attribute 'layers'
  # PlotnineError: "Cannot add layer to object of type <class 'float'>"
  g = (
        ggplot(data,
         aes(x="timescale", y="MB", color="msisdn")
        )
        + geom_point()
        + labs(title="Top 5 traffic-heavy devices for company="+str(company)+"  start="+start+ "  days="+str(n_days) , x='time')
      )
  print(g)


#----------------------------------------
def dialog():
#----------------------------------------
 ####################
 ### get time range
 ####################

  start_input = input("Enter start day (YYYY-MM-DD) (default 2020-11-01) : ")
  if not start_input:
      start="2020-11-01"
  elif  len(start_input) != 10:
      print("Error in input- format is YYYY-MM-DD")
      return
  else:
      start=start_input

  print(" ")
  end_input = input("""Enter duration
       1 - one day (default)
       2 - one week
       3 - one month
   """
  )

  #print("end_input=",end_input)

  granularity = None
  if not end_input or end_input == '1':
      n_days=1
      granularity='minutes'
  elif end_input == '2': # week
      n_days=7
  elif end_input == '3': # month
      n_days=30 ## TODO
  else:
      print("wrong end input")
      return

  end = (datetime.strptime(start, '%Y-%m-%d') + timedelta(days=n_days)).strftime('%Y-%m-%d')

  #########################
  ### all_company_total
  #########################

  plot_all_company_total(start, end, n_days)

  ############################
  ###    all_company_daily
  ############################

  if  n_days == 1:
      granularity='hours'
  plot_all_company_daily(start, end, n_days, granularity)



  ############################
  ###    devices
  ############################
  if  n_days == 1:
      granularity='hours'

  plot_devices(start, end, n_days, granularity)

  ############################
  ###    single_company
  ############################
  company=3659
  company_str = input("Enter the company_id: \n (default - "+str(company)+") \n 2-3116 \n 3-3666 \n 4-3655 ")
  if company_str:
      company = int(company_str)
      if    company==2: company=3116
      elif  company==3: company=3666
      elif  company==4: company=3655

  if  n_days == 1:
      granularity='minutes'
  elif n_days < 60:
      granularity='day-hour'

  for company in COMPANY_LIST:
     plot_single_company_all_directions(company, start, end, n_days, granularity)


  for company in COMPANY_LIST:
     plot_single_company_protocol(company, start, end, n_days, granularity)
  #############################
  ####   SINGLE COMPANY_device
  #############################
  if  n_days == 1:
      granularity='minutes'
  elif n_days < 32:
      granularity='day-hour'

  for company in COMPANY_LIST:
     plot_single_company_device(company, start, end, n_days, granularity)



###  main

if __name__ == "__main__" :
  datastore.connect()
  COMPANY_LIST=(3666, 3659,3116)
  while True:
      dialog()

  exit(1)

####################


  q_single_company="""
   SELECT  
   FROM_UNIXTIME(timebin, '%%m-%%d') as month_day,
   SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB_company,
   CAST(direction as char(10)) AS Direction 
   FROM jangle_traffic_total
   WHERE 
   timebin >=  UNIX_TIMESTAMP('2020-01-01') and
   timebin  <  UNIX_TIMESTAMP('2020-11-02') and
   company =  %%d%%
   GROUP BY month_day, Direction
   ORDER BY month_day 
  """ % (company)
  
  print(q_single_company)
  data=query(q_single_company)
  print(data)
  exit(1)

  #########
  q_3116_Nov_dir  ="""
  SELECT 
  CAST(direction as char(10)) AS Direction_,  
  (timebin) as T, 
  sum(bytes)  * 1.0  / (1024 * 1024  * 1.0) AS MB_company
  FROM jangle_traffic_total
  WHERE company IN (3116)  
  and timebin  >= UNIX_TIMESTAMP('2020-11-01') and timebin  <  UNIX_TIMESTAMP('2020-11-02') 
  group by timebin, direction
  """
  print(q_3116_Nov_dir)
  data=query(q_3116_Nov_dir)
  print(data)

  g = (
        ggplot(data)
        + aes(x="T", y="MB_company", color="Direction_")
        + geom_point()
        # + facet_grid('~MONTH ')
        + labs(title=" # November 1 for company=3116 ", y="MB", x='timebin')
      )
  print(g)


  exit(1)

  #########
  q_3659_Nov_1_dir  ="""
  SELECT 
  CAST(direction as char(10)) AS Direction_,  
  (timebin) as T, 
  sum(bytes)  * 1.0  / (1024 * 1024  * 1.0) AS MB_company
  FROM jangle_traffic_total
  WHERE company IN (3659)  
  and timebin  >= UNIX_TIMESTAMP('2020-11-01') and timebin  <= UNIX_TIMESTAMP('2020-11-30') 
  group by timebin, direction
  """
  print(q_3659_Nov_1_dir)
  data=query(q_3659_Nov_1_dir)
  print(data)

  g = (
        ggplot(data)
        + aes(x="T", y="MB_company", color="Direction_")
        + geom_point()
        # + facet_grid('~MONTH ')
        + labs(title=" # November   for company=3659 ", y="MB", x='timebin')
      )
  print(g)


  exit(1)



  #########
  q_3659_Nov_1 ="""
  SELECT 
  CAST(company as char(20)) AS Company_,  
  (timebin) as T, 
  sum(bytes)  * 1.0  / (1024 * 1024  * 1.0) AS MB_company
  FROM jangle_traffic_total
  WHERE company IN (3659) and direction=1
  and timebin  >= UNIX_TIMESTAMP('2020-11-01') and timebin  < UNIX_TIMESTAMP('2020-11-02') 
  group by timebin
  """
  print(q_3659_Nov_1)
  data=query(q_3659_Nov_1)
  print(data)

  g = (
        ggplot(data)
        + aes(x="T", y="MB_company", color="Company_")
        + geom_point()
        # + facet_grid('~MONTH ')
        + labs(title=" # November 1 for company=3659 direction=1", y="MB", x='timebin')
      )
  print(g)


  exit(1)

  q_3659_Sep ="""
  SELECT 
  CAST(company as char(20)) AS Company_,  
  (timebin) as T, 
  (bytes  * 1.0 ) / (1024 * 1024  * 1.0) AS MB_company
  FROM jangle_traffic_total
  WHERE company IN (3659) and direction=1
  and timebin >= UNIX_TIMESTAMP('2020-09-01') and timebin <  UNIX_TIMESTAMP('2020-10-01')
  """
  print(q_3659_Sep)
  data=query(q_3659_Sep)
  print(data)

  g = (
        ggplot(data)
        + aes(x="T", y="MB_company", color="Company_")
        + geom_point()
        # + facet_grid('~MONTH ')
        + labs(title=" # September for company=3659 direction=1", y="MB", x='timebin')
      )
  print(g)

  #########
  q_3659_October ="""
  SELECT 
  CAST(company as char(20)) AS Company_,  
  (timebin) as T, 
  (bytes  * 1.0 ) / (1024 * 1024  * 1.0) AS MB_company
  FROM jangle_traffic_total
  WHERE company IN (3659) and direction=1
  and timebin >= UNIX_TIMESTAMP('2020-10-01') and timebin <  UNIX_TIMESTAMP('2020-11-01')
  """
  print(q_3659_October)
  data=query(q_3659_October)
  print(data)

  g = (
        ggplot(data)
        + aes(x="T", y="MB_company", color="Company_")
        + geom_point()
        # + facet_grid('~MONTH ')
        + labs(title=" # October for company=3659 direction=1", y="MB", x='timebin')
      )
  print(g)

  #########
  q_3659_Nov ="""
  SELECT 
  CAST(company as char(20)) AS Company_,  
  (timebin) as T, 
  (bytes  * 1.0 ) / (1024 * 1024  * 1.0) AS MB_company
  FROM jangle_traffic_total
  WHERE company IN (3659) and direction=1
  and timebin >= UNIX_TIMESTAMP('2020-11-01') and timebin <  UNIX_TIMESTAMP('2020-12-01')
  """
  print(q_3659_Nov)
  data=query(q_3659_Nov)
  print(data)

  g = (
        ggplot(data)
        + aes(x="T", y="MB_company", color="Company_")
        + geom_point()
        # + facet_grid('~MONTH ')
        + labs(title=" # Nov for company=3659 direction=1", y="MB", x='timebin')
      )
  print(g)

  exit(1)

  ################################################
  q_dev ="""
  SELECT 
  CAST(company as char(20)) AS Company_,  
  FROM_UNIXTIME(timebin, '%%m') as MONTH, 
  FROM_UNIXTIME(timebin, '%%m-%%d') as MONTH_DAY, 
  FROM_UNIXTIME(timebin, '%%d') as DAY, 
  count(distinct msisdn) as msisdn,
  SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB_company,
  SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) / count(distinct msisdn)   as GB_per_dev
  FROM jangle_traffic
  WHERE company IN (3659, 3116, 3666, 3655, 3579, 3061, 0)
  and timebin >= UNIX_TIMESTAMP('2020-10-01') and timebin <  UNIX_TIMESTAMP('2020-11-01')
  GROUP BY company, MONTH, MONTH_DAY, DAY 
  ORDER BY MONTH_DAY, Company_
  """

  print(q_dev)
  data=query(q_dev)
  print(data)

  g = (
        ggplot(data)
        + aes(x="DAY", y="msisdn", color="Company_")
        #+ geom_point()
        + geom_line(aes(x="DAY", y="msisdn", color="Company_"), group=1)
        #+ facet_grid('~MONTH')
        + labs(title=" # Devices per company  (October)", y="# of dev", x='DAY')
      )
  print(g)

  exit(1)
###  by company in last 4 month

  q_2 ="""
  SELECT 
  CAST(company as char(20)) AS Company_,  
  FROM_UNIXTIME(timebin, '%%m') as MONTH, 
  FROM_UNIXTIME(timebin, '%%m-%%d') as MONTH_DAY, 
  FROM_UNIXTIME(timebin, '%%d') as DAY, 
  count(distinct msisdn) as msisdn,
  direction,
  SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) AS GB_company,
  SUM(bytes) * 1.0 / (1024 * 1024 * 1024 * 1.0) / count(distinct msisdn)   as GB_per_dev
  FROM jangle_traffic
  WHERE company IN (3659, 3116, 3666, 3655, 3579, 3061, 0)
  and timebin >= UNIX_TIMESTAMP('2020-10-01') and timebin <  UNIX_TIMESTAMP('2020-12-01')
  GROUP BY company, MONTH, MONTH_DAY, DAY, direction
  ORDER BY MONTH_DAY, Company_
  """

# WHERE company IN (3659, 3116, 3666, 3655, 3579, 3061, 0)
  print(q_2)
  data=query(q_2)
  print(data)

  g = (
        ggplot(data)
        + aes(x="DAY", y="GB_company", color="Company_")
        + geom_point()
        + facet_grid('~MONTH+direction')
        + labs(title=" # GB per company  (faced_grid)", y="GB_company", x='MONTH_DAY')
      )
  print(g)

  exit(1)
  #############

  g = (
        ggplot(data)
        + aes(x="DAY", y="GB_per_dev", color="Company_")
        + geom_point()
        + facet_grid('~MONTH+direction')
        + labs(title=" # GB per company per device (faced_grid)", y="GB_company_per_dev", x='MONTH_DAY')
      )
  print(g)

  exit(1)
  #############
  g = (
        ggplot(data)
        + aes(x="DAY", y="GB_company", color="Company_")
        + geom_point()
        + facet_grid('~MONTH')
        + labs(title=" # GB per company  (faced_grid)", y="GB_company", x='MONTH_DAY')
      )
  print(g)

  exit(1)
  ############
  

  g = (
        ggplot(data)
        + aes(x="DAY", y="msisdn", color="Company_")
        + geom_point()
        + facet_grid('~MONTH')
        + labs(title=" # of devices  (faced_grid)", y="msisdn", x='MONTH_DAY')
      )
  print(g)

 # g = (
 #       ggplot(
 #           aes(x="DAY"), data=data
 #        )
 #       + geom_line(
 #                    aes( y="msisdn"),
 #                    # color="Company_",
 #                    data=data  
 #                  )
 #       + facet_grid('~MONTH')
 #       + labs(title=" # of devices  (faced_grid)", y="msisdn", x='MONTH_DAY')
 #     )
 # print(g)

  exit(1)   
  #####################
  g = (
        ggplot(data)
        + aes(x="MONTH_DAY", y="msisdn", color="Company_")
        + geom_point()
        + labs(title=" # of devices  (color=company)", y="msisdn", x='MONTH_DAY', color='company')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="DAY", y="msisdn",  color="Company_")
        + geom_point()
        + facet_wrap('~MONTH', ncol=1, scales='free')
        + labs(title=" # of devices  (faced_wrap)", y="msisdn", x='MONTH_DAY')
      )
  print(g)

 ###-------------------------------------
  q_jangle_active_daily="""
       SELECT
           FROM_UNIXTIME(timebin, '%%m') as month,
           FROM_UNIXTIME(timebin, '%%d') as day,
           count(distinct msisdn) as distinct_msisdn
       FROM jangle_active
       WHERE FROM_UNIXTIME(timebin, '%%Y') = 2020
       GROUP BY
          FROM_UNIXTIME(timebin, '%%m'),
          FROM_UNIXTIME(timebin, '%%d')
  """

  print(q_jangle_active_daily)
  data=query(q_jangle_active_daily)
  print (data)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_wrap('~month', ncol=3)
        + labs(title=" jangle_active  (faced_wrap)", y="distinct_msisdn", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_wrap('~month', ncol=3, scales='free_y')
        + labs(title="jangle_active (facet_wrap, free_y)", y="distinct_msisdn", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_grid('~month' )
        + labs(title="jangle_active (facet_grid)", y="distinct_msisdn", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_grid('~month', scales='free_y' )
        + labs(title="jangle_active (facet_grid, free_y)", y="distinct_msisdn", x='day')
      )
  print(g)

  exit(1)
 ###-------------------------------------
  q_radius_active_daily="""
       SELECT
           FROM_UNIXTIME(timebin, '%%m') as month,
           FROM_UNIXTIME(timebin, '%%d') as day,
           count(distinct msisdn) as distinct_msisdn
       FROM radius_active
       WHERE FROM_UNIXTIME(timebin, '%%Y') = 2020
       GROUP BY
          FROM_UNIXTIME(timebin, '%%m'),
          FROM_UNIXTIME(timebin, '%%d')
  """

  print(q_radius_active_daily)
  data=query(q_radius_active_daily)
  print (data)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_wrap('~month', ncol=3)
        + labs(title=" radius_active  (faced_wrap)", y="distinct_msisdn", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_wrap('~month', ncol=3, scales='free_y')
        + labs(title="radius_active (facet_wrap, free_y)", y="distinct_msisdn", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_grid('~month' )
        + labs(title="radius_active (facet_grid)", y="distinct_msisdn", x='day')
      )
  print(g)

  g = (
        ggplot(data)
        + aes(x="day", y="distinct_msisdn")
        + geom_point()
        + facet_grid('~month', scales='free_y' )
        + labs(title="radius_active (facet_grid, free_y)", y="distinct_msisdn", x='day')
      )
  print(g)

  exit(1)

 ###----------------------------------------

  for month in ['01','02', '03','04','05','06','07','08','09','10','11']:
   
    q_radius_active="""
       SELECT  FROM_UNIXTIME(timebin, '%%d') as day,
       count (distinct msidn)
       FROM  radius_active
       WHERE
          FROM_UNIXTIME(timebin, '%%Y') = 2020
          AND
          FROM_UNIXTIME(timebin, '%%m')  = '""" 
  
    q_radius_active += month +"'"
    q_radius_active += " GROUP BY FROM_UNIXTIME(timebin, '%%d')"

   



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


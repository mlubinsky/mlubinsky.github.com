'''

​
import getpass
from sshtunnel import SSHTunnelForwarder
import mysql.connector
​
import pandas as pd
import plotnine as p9
from plotnine import *
​
​
ssh_host='192.168.240.177'
ssh_port=22
db_host = '127.0.0.1'
db_port=3306
​
with SSHTunnelForwarder(
		(ssh_host,ssh_port),
		ssh_username=input('ssh username: '),
		ssh_password=getpass.getpass(prompt='ssh password'),
		remote_bind_address=(db_host,db_port)) as server:
​
	conn = mysql.connector.connect(
			host=db_host,
			user=input('database username: '),
			password=getpass.getpass(prompt='database password:'),
			database='analytics',
			port=server.local_bind_port
			)
​
​
	query = '''
			select 
				from_unixtime(timebin) as date,
				sum(bytes)/(1024*1024) as traffic
			from 
				jangle_traffic_total
				where direction=1
				and company=3116
				group by 1
​
	'''
	
	traffic = pd.read_sql_query(query, conn)
	print(traffic.head(10))	
	p1 = (ggplot(data=traffic) 
		+ geom_line(aes(x='date',y='traffic'),color='blue')
		+ p9.scales.ylim(0.5,4)
		+ theme(axis_text_x=element_text(rotation=45, hjust=1))
​
	  )
	print(p1)
​
	conn.close()
```  

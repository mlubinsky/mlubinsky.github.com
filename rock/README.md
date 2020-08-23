### Recovering data from 1970-01-02
```
CREATE EXTERNAL TABLE IF NOT EXISTS sbschema.r_1970
(
  server_event_ts  BIGINT  COMMENT 'server timestamp added by scribe',
  s STRING  COMMENT 'Type of experiment (segment/anonymous/user)'
)
COMMENT 'fact amoeba allocations table'
PARTITIONED BY (
  date_key STRING COMMENT 'year month day in yyyy-MM-dd format based on timestamp for allocation'
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '~'
STORED AS TEXTFILE
LOCATION 's3://roku-data-warehouse/roku/facts/fact_amoeba_allocation_events/'
;

alter table sbschema.r_1970 add partition (date_key='1970-01-02')
LOCATION 's3://roku-data-warehouse/roku/facts/fact_amoeba_allocation_events/date_key=1970-01-02';

grant select on table sbschema.r_1970 to role public;

select * from sbschema.r_1970 where date_key='1970-01-02' and server_event_ts > 1595721600 LIMIT 30;
```
## INSERT from 1970-01-02 using params 

hive -hiveconf p_date=2020-07-27 -f DEA-11291.hql

```
INSERT INTO roku.fact_amoeba_allocation_events
PARTITION (date_key = '${hiveconf:p_date}')
SELECT
server_event_ts,
split(s,',')[0] as allocation_ts,
split(s,',')[1] as event_type,
split(s,',')[2] as device_id,
split(s,',')[3] as account_id,
split(s,',')[4] as web_id,
split(s,',')[5] as layer_name,
split(s,',')[6] as experiment_id,
split(s,',')[7] as bucket_name,
split(s,',')[8] as bucket_configurations,
split(s,',')[9] as experiment_version,
split(s,',')[10] as experiment_type
FROM sbschema.r_1970
WHERE  date_key='1970-01-02'
and server_event_ts < 1596579529  --- 08/04/2020 @ 10:18pm (UTC)
and server_event_ts > 1595882141  --- 07/27/2020 @  8:35pm (UTC)
and date_format(from_unixtime(server_event_ts), 'yyyy-MM-dd') = '${hiveconf:p_date}'

```
### Other topics 

```
The # of records in Hive table roku.fact_amoeba_allocation_events
on July 9 is significantly less ( ~2.2 billions) compared with previous days ( > 5.5 billions).
Could you please have a look if there is any issues/delays in populating this table
(or tell us how we can monitor it without disturbing you)
```

```
select count(*) as cnt , count (distinct device_id) as dist_dev, date_key
from roku.fact_amoeba_allocation_events
where date_key >= '2020-07-01'
group by date_key
order by date_key
limit 15
```

Result: (look at 1st column)
```
8259983	 2555157	2020-07-01
6489805	 2035394	2020-07-02
8919267	 3891763	2020-07-03
5781696	 1469031	2020-07-04
4984972	 1010221	2020-07-05
7921315	 2070758	2020-07-06
5026874	 893706	    2020-07-07
14297518 8910610    2020-07-08
2234019	 1089297	2020-07-09

```




 

Krishna Chandolu  1:57 PM
Just reran the query, I get 3.3 Million for Jul-9
```
select date_key, count(*) as cnt 
from roku.fact_amoeba_allocation_events
where date_key >= '2020-07-01'
group by date_key order by date_key;

 
2020-07-01	8259983
2020-07-02	6489805
2020-07-03	8919267
2020-07-04	5781696
2020-07-05	4984972
2020-07-06	7921315
2020-07-07	5026874
2020-07-08	14297518
2020-07-09	3385679
```
 
Yep. Is it delayed and if those by how much time ?

 
This job is scheduled to run every hour and if it receives delayed data then it still puts it in respective old partition . 
so, counts could be updated through out until there is no delayed data. We are not calculating delay for abf job.
 But we are extracting similar num of records in the last 7 days .
 
<https://app.datadoghq.com/dashboard/guy-wuq-3wf?from_ts=1593810262021&live=true&to_ts=1594415062021>

 
I just extracted some records from Kafka.

```
1594415332~1594273414~allocation-v6~~~f703a2cf-edb4-47ca-a3b7-06c8aeee55fd:9ac4e0595584accfbce0e58fc95580bd~web~l8k1zRx-e~l8k1zRx-e#Test~~0~
1594415332~1594275053~allocation-v6~~~4aa11a25-d019-453e-89fc-6ccdd619b21a:fc2e72d3dd67b8aea09e2e650f7a8a6a~web~r79QQOSEg~r79QQOSEg#Control~~1~
1594415332~1594275052~allocation-v6~8L67D9263429~3BDE2E8C-87C7-4EF3-8564-A16C00F1444E~~grandcentral~k6U4N2L3H~k6U4N2L3H#Control~~1~
1594415332~1594275049~allocation-v6~~~d877424b-d849-4f08-9e3f-e4cc912a70dc:4c9d1eed1941ca17bd4b75ade8831551~web~t8KTbdUg3~t8KTbdUg3#control~~1~

 
Based on timestamps (2nd field)  i am seeing data from (Thursday, July 9, 2020 5 or 6 UTC) 
that means we are receiving data which is very delayed (>24 hrs) .
 
So, May be by tomorrow the data for 7/9 would have a full snapshot.

Abhinav Wagle   
Got it thanks a lot for the confirmation
 
and the datadog dashboard helps
2:14
just so that i understand the dashboard better, it means how may events were processed by bdp from scribe ?

Krishna Chandolu  2:18 PM
:+1: basically you need to multiply that number from datadog dashboard with 32.
We have 32 mappers for you abf Job in bdp. The datadog shows on avg. how many records bdp extracted from (kafka) . 
So, to get full picture you just need to multiply that number with 32.

2020-07-09T00:40:00.000Z	0
2020-07-09T01:40:00.000Z	9007
2020-07-09T02:40:00.000Z	0
2020-07-09T03:40:00.000Z	0
2020-07-09T04:40:00.000Z	9000
2020-07-09T05:40:00.000Z	9000
2020-07-09T06:40:00.000Z	0
2020-07-09T07:40:00.000Z	0
2020-07-09T08:40:00.000Z	9005
2020-07-09T09:40:00.000Z	9003
2020-07-09T10:40:00.000Z	9003
2020-07-09T11:40:00.000Z	9000
2020-07-09T12:40:00.000Z	0
2020-07-09T13:40:00.000Z	0
2020-07-09T14:40:00.000Z	9002
2020-07-09T15:40:00.000Z	0
2020-07-09T16:40:00.000Z	0
2020-07-09T17:40:00.000Z	9012
2020-07-09T18:40:00.000Z	9001
2020-07-09T19:40:00.000Z	0
2020-07-09T20:40:00.000Z	0
2020-07-09T21:40:00.000Z	0
2020-07-09T22:40:00.000Z	9005
2020-07-09T23:40:00.000Z	0


So, even before running query i just summed up records extracted by bdp on (7/9) from kafka and multiplied by 32. 
(99038 * 32 = 3.1 Million)  that almost matched with query results above for 7/9.
2:19
scribe -> kafka -> bdp -> fact tables. sequence of events.

Abhinav Wagle  2:19 PM
Got it ! that is super useful ! Makes sense to me now :slightly_smiling_face:
2:19
Now we can better estimate things

Krishna Chandolu  2:20 PM
yea you can bookmark that datadog link and change date range,
If BDP is extracting less records or if there are errors that graph will easily tell you from the trend……

Abhinav Wagle  2:21 PM
yeps just did that :slightly_smiling_face:
2:21
thanks a lot @kchandolu!!!

Krishna Chandolu  2:22 PM
cool. If the trend is consistent meaning job is running fine and may be data is delayed. If you still have issues reach out to us. (if you send more data to scribe obviously then there will be spike in the graph or else consistent).
:+1:
1


Abhinav Wagle  2:23 PM
Yeps AI for me is now try to reduce delay from our end :slightly_smiling_face: I will take that work up now

Krishna Chandolu  2:27 PM
one more tip for you to estimate lag. If you are familiar with kafka consumer client.

bin/kafka-console-consumer.sh --bootstrap-server kafka10-broker-1001.bdp.roku.com:9092,kafka10-broker-1002.bdp.roku.com:9092 --topic abf

just by running that command from your mac terminal you can read kafka messages yourself to estimate lag.

1594415332~1594273414~allocation-v6~~~f703a2cf-edb4-47ca-a3b7-06c8aeee55fd:9ac4e0595584accfbce0e58fc95580bd~web~l8k1zRx-e~l8k1zRx-e#Test~~0~
1594415332~1594275053~allocation-v6~~~4aa11a25-d019-453e-89fc-6ccdd619b21a:fc2e72d3dd67b8aea09e2e650f7a8a6a~web~r79QQOSEg~r79QQOSEg#Control~~1~
1594415332~1594275052~allocation-v6~8L67D9263429~3BDE2E8C-87C7-4EF3-8564-A16C00F1444E~~grandcentral~k6U4N2L3H~k6U4N2L3H#Control~~1~
1594415332~1594275049~allocation-v6~~~d877424b-d849-4f08-9e3f-e4cc912a70dc:4c9d1eed1941ca17bd4b75ade8831551~web~t8KTbdUg3~t8KTbdUg3#control~~1~...................................................

2nd field is timestamp and epoch convert it and subtract it from current UTC time then you can estimate lag by yourself ( in this ex:- is >24 hrs) .

```


I am using the   Redshift table  dea.agg_amoeba_allocation_events
which is derived from Hive table roku.fact_amoeba_allocation_events:
https://gitlab.eng.roku.com/dea/data-processing/blob/master/src/main/python/agg/agg_daily_non_bucketed/agg_amoeba_allocation_events_daily.hql

I expected to see the same # of distinct devices per day  in these tables.
But it is not always the case:

```
SELECT A.date_key, A.fact_cnt, B.dea_cnt FROM
( SELECT date_key,	count(distinct	device_id) as fact_cnt
from roku.fact_amoeba_allocation_events
WHERE date_key between '2020-05-20' and '2020-06-06'
group by date_key
) A
LEFT JOIN
( SELECT date_key,  count(distinct device_id) as dea_cnt
 from dea.agg_amoeba_allocation_events
 WHERE date_key between '2020-05-20' and '2020-06-06'
 group by date_key
) B
 ON A.date_key=B.date_key
 ORDER BY A.date_key
 LIMIT 100;
Result:
          fact_cnt  dea_cnt
---------  -------  -------- 
2020-05-20	965094	965094
2020-05-21	1355545	1355545
2020-05-22	1925684	1925684
2020-05-23	1226620	1226620
2020-05-24	970096	970096
2020-05-25	800109	800109
2020-05-26	8660952	2212133
2020-05-27	2572230	2
2020-05-28	1146441	1
2020-05-29	1066561	2
2020-05-30	1183667	1
2020-05-31	989431	96756
2020-06-01	13126852	2240214
2020-06-02	28716647	1960952
2020-06-03	4993031	1
2020-06-04	3539983	1
2020-06-05	4735329	4735329
2020-06-06	1603955	1603955
Why it is so? (edited) 




2 replies

Suvrath Penmetcha   
I’m guessing it could be that data is coming in later into older fact partitions. 
Looks like fact_amoeba_allocation_events is partitioned by allocation_ts 
and not event time so older fact partitions can be updated. 
You can try moving dea.agg_amoeba_allocation_events into agg_daily  or DVIS_agg 
which process dates from 2-3 days ago instead of agg_daily_non_bucketed which is 1 day ago.

Krishna Chandolu   
roku.fact_amoeba_allocation_events has late arriving events ranging from 1-2 days delayed data. 
 So, like suvrath suggested try increasing the agg/bucketing duration to 3 days instead of current 1.
``` 

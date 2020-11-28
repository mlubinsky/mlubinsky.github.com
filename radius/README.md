
### APN Acces Point Name
https://en.wikipedia.org/wiki/Access_Point_Name

## IMEI - International Mobile Equipment Identity
https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity

## IMSI - international mobile subscriber identity 
https://en.wikipedia.org/wiki/MSISDN

An international mobile subscriber identity (IMSI) number uniquely identifies a cellphone subscriber. It's usually stored in a SIM card. 
The IMSI is used internally within cellphone systems to identify a phone.

## MSISDN  number is a cellphone's phone number
https://en.wikipedia.org/wiki/MSISDN

A mobile subscriber integrated services digital network (MSISDN) number is a cellphone's phone number. 
Most users don't know their IMSIs, while the MSISDN can be dialed to reach the phone.

### RADIUS CDR

https://en.wikipedia.org/wiki/RADIUS

Remote Authentication Dial In User Service (RADIUS) for streaming the Call Detail Records (CDR).

Remote Access Dial-In User Service (RADIUS) is a networking protocol providing authentication, authorization, and accounting. 

https://docs.microsoft.com/en-us/windows/win32/nps/ias-radius-authentication-and-accounting

https://wiki.freeradius.org/Home

https://networkradius.com/doc/FreeRADIUS%20Technical%20Guide.pdf

https://habr.com/ru/post/51882/

https://www.dialogic.com/webhelp/BorderNet2020/2.2.0/WebHelp/radius_ov.htm

https://support.sonus.net/display/UXDOC61/Working+with+Call+Detail+Records

https://support.sonus.net/display/UXDOC61/Retreiving+Call+Detail+Records+From+a+RADIUS+Server

https://support.sonus.net/display/UXDOC61/Call+Detail+Records+Primer

https://wifisoft.zendesk.com/hc/en-us/articles/203566091-Understanding-RADIUS-session-records-CDRs-

### getTraffic
```
CREATE FUNCTION `_getTrafficQuery`(q_company INT unsigned, 
   q_msisdn BIGINT unsigned, 
   q_remote_ip INT unsigned, 
   q_data_type_in VARCHAR(1024), 
   q_protocol INT unsigned, 
   q_time_start INT unsigned, 
   q_time_end INT unsigned, 
   q_resolution INT unsigned, 
   q_graph_type_in VARCHAR(256), 
   q_split_by_in VARCHAR(256) 
  ) RETURNS text CHARSET utf8mb4
BEGIN
  DECLARE count_column VARCHAR(256);
  DECLARE data_type VARCHAR(256);
  DECLARE extra_columns VARCHAR(256);
  DECLARE graph_type VARCHAR(256);
  DECLARE group_by VARCHAR(256);
  DECLARE order_by VARCHAR(256);
  DECLARE table_prefix VARCHAR(256);
  DECLARE table_full VARCHAR(256);
  DECLARE table_total VARCHAR(256);
  DECLARE query_table VARCHAR(256);
  DECLARE query_timebin VARCHAR(256);
  DECLARE query_where VARCHAR(1024);
  DECLARE query VARCHAR(10240);
  DECLARE split_by VARCHAR(256);
  DECLARE where_company VARCHAR(256);
  DECLARE where_msisdn VARCHAR(256);
  DECLARE where_protocol VARCHAR(256);
  DECLARE where_remote_ip VARCHAR(256);
  DECLARE where_timebin VARCHAR(256);

  SET data_type := _validateDataType(q_data_type_in, "traffic");
  SET split_by := _validateSplitBy(q_split_by_in, data_type);
  SET graph_type := _validateGraphType(q_graph_type_in, data_type);

  SET where_timebin := _getWhereTimebin("t.timebin", q_time_start, q_time_end, q_resolution);
  SET where_company := IF(ISNULL(q_company), '', CONCAT(' AND t.company = ', q_company));
  SET where_msisdn := IF(ISNULL(q_msisdn), '', CONCAT(' AND t.msisdn = ', q_msisdn));
  SET where_remote_ip := IF(ISNULL(q_remote_ip), '', CONCAT(' AND t.remote_ip = ', q_remote_ip));
  SET where_protocol := IF(ISNULL(q_protocol), '', CONCAT(' AND t.protocol = ', q_protocol));

  SET query_where = CONCAT_WS('', where_timebin, where_company, where_msisdn, where_remote_ip, where_protocol);

  SET query_timebin := IF (q_resolution = 900 OR ISNULL(q_resolution), 'timebin', CONCAT('((timebin DIV ', q_resolution, ') * ', q_resolution, ')'));

  SET table_prefix := _getDataTypeTablePrefix(data_type);
  SET table_full := CONCAT(table_prefix, 'traffic');
  SET table_total := CONCAT(table_prefix, 'traffic_total');

  SET query_table := IF(ISNULL(q_msisdn) AND ISNULL(q_remote_ip) AND (ISNULL(split_by) OR (split_by != "msisdn" AND split_by != "remote_ip")) AND (graph_type = "time" OR graph_type = "direction" OR graph_type = "apn" OR graph_type = "protocol" OR graph_type = "nas" OR graph_type = "sgsn"), table_total, table_full);

  CASE data_type
    WHEN 'packets' THEN
      SET count_column := "SUM(packets)";
    ELSE
      SET count_column := "SUM(bytes)";
  END CASE;

  CASE graph_type
    WHEN 'msisdn' THEN
      SET extra_columns := "msisdn, max(timebin) AS last_seen";
      SET group_by := " GROUP BY msisdn";
      SET order_by := CONCAT(" ORDER BY ", count_column, " DESC");
    WHEN 'remote_ip' THEN
      SET extra_columns := "remote_ip, max(timebin) AS last_seen";
      SET group_by := " GROUP BY remote_ip";
      SET order_by := CONCAT(" ORDER BY ", count_column, " DESC");
    WHEN 'apn' THEN
      SET extra_columns := "apn";
      SET group_by := " GROUP BY apn";
      SET order_by := CONCAT(" ORDER BY ", count_column, " DESC");
    WHEN 'direction' THEN
      SET extra_columns := "direction";
      SET group_by := " GROUP BY direction";
      SET order_by := CONCAT(" ORDER BY ", count_column, " DESC");
    WHEN 'protocol' THEN
      SET extra_columns := "protocol";
      SET group_by := " GROUP BY protocol";
      SET order_by := CONCAT(" ORDER BY ", count_column, " DESC");
    WHEN 'nas' THEN
      SET extra_columns := "nas";
      SET group_by := " GROUP BY nas";
      SET order_by := CONCAT(" ORDER BY ", count_column, " DESC");
    WHEN 'sgsn' THEN
      SET extra_columns := "sgsn";
      SET group_by := " GROUP BY sgsn";
      SET order_by := CONCAT(" ORDER BY ", count_column, " DESC");
    ELSE
      SET extra_columns := CONCAT(query_timebin, " AS timebin");
      SET group_by := IF(ISNULL(q_resolution), '', CONCAT(" GROUP BY (t.timebin DIV ", q_resolution, ")"));
      SET order_by := '';
  END CASE;

  IF split_by IN ('apn', 'company', 'direction', 'msisdn', 'remote_ip', 'nas', 'protocol', 'sgsn') THEN
      SET extra_columns := CONCAT(extra_columns, ", ", split_by);
      SET group_by := CONCAT(group_by, ", ", split_by);
  ELSE
      SET group_by := group_by; 
  END IF;

  SET query := CONCAT('SELECT ', extra_columns, ', ', count_column, ' AS count FROM ', query_table, ' AS t', query_where);
  SET query := CONCAT(query, group_by, order_by);

  RETURN query;
END
```

### getActivity

```
CREATE PROCEDURE `getActivity`(q_company INT unsigned, 
   q_msisdn BIGINT unsigned, 
   q_apn INT unsigned, 
   q_data_type VARCHAR(256), 
   q_time_start INT unsigned, 
   q_time_end INT unsigned, 
   q_resolution INT unsigned, 
   q_split_by VARCHAR(256) 
   )
BEGIN
  CALL execQuery(_getActivityQuery(q_company, q_msisdn, q_apn, q_data_type, q_time_start, q_time_end, q_resolution, q_split_by));
END


CREATE FUNCTION `_getActivityQuery`(q_company INT unsigned, 
   q_msisdn BIGINT unsigned, 
   q_apn INT unsigned, 
   q_data_type_in VARCHAR(256), 
   q_time_start INT unsigned, 
   q_time_end INT unsigned, 
   q_resolution INT unsigned, 
   q_split_by_in VARCHAR(256) 
  ) RETURNS text CHARSET utf8mb4
BEGIN
  DECLARE count_column VARCHAR(256);
  DECLARE data_type VARCHAR(256);
  DECLARE extra_columns VARCHAR(256);
  DECLARE group_by VARCHAR(256);
  DECLARE table_prefix VARCHAR(256);
  DECLARE table_full VARCHAR(256);
  DECLARE table_total VARCHAR(256);
  DECLARE query_table VARCHAR(256);
  DECLARE query_timebin VARCHAR(256);
  DECLARE query_where VARCHAR(1024);
  DECLARE query VARCHAR(10240);
  DECLARE split_by VARCHAR(256);
  DECLARE where_company VARCHAR(256);
  DECLARE where_msisdn VARCHAR(256);
  DECLARE where_apn VARCHAR(256);
  DECLARE where_timebin VARCHAR(256);

  SET data_type := _validateDataType(q_data_type_in, "activity");
  SET split_by := _validateSplitBy(q_split_by_in, data_type);

  SET where_timebin := _getWhereTimebin("t.timebin", q_time_start, q_time_end, q_resolution);
  SET where_company := IF(ISNULL(q_company), '', CONCAT(' AND t.company = ', q_company));
  SET where_msisdn := IF(ISNULL(q_msisdn), '', CONCAT(' AND t.msisdn = ', q_msisdn));
  SET where_apn := IF(ISNULL(q_apn), '', CONCAT(' AND t.apn = ', q_apn));

  SET query_where = CONCAT_WS('', where_timebin, where_company, where_msisdn, where_apn);

  SET query_timebin := IF (q_resolution = 900 OR ISNULL(q_resolution), 'timebin', CONCAT('((timebin DIV ', q_resolution, ') * ', q_resolution, ')'));

  SET table_prefix := _getDataTypeTablePrefix(data_type);

  CASE data_type
    WHEN 'radius-activity' THEN
      SET table_full := CONCAT(table_prefix, "active");
      IF (q_apn IS NOT NULL OR split_by = "apn") THEN
        RETURN 'SELECT ''APN filtering/splitting is not available for RADIUS activity: please use mcaudit ''''mc-activity'''' instead.''';
      END IF;
    ELSE
      IF (q_apn IS NOT NULL OR split_by = "apn") THEN
        SET table_full := CONCAT(table_prefix, "traffic");
      ELSE
        SET table_full := CONCAT(table_prefix, "active");
      END IF;
  END CASE;
  SET table_total := table_full;

  

  SET count_column := IF(ISNULL(q_msisdn), IF(q_resolution = 900 AND (data_type != "mc-activity" OR split_by = "apn"), "count", "COUNT(DISTINCT msisdn)"), "1");

  

  SET query_table := IF(count_column = "count", table_total, table_full);

  SET extra_columns := CONCAT(query_timebin, " AS timebin");
  SET group_by := CONCAT(" GROUP BY (t.timebin DIV ", q_resolution, ")");

  CASE
    WHEN split_by = 'apn' THEN
      SET extra_columns := CONCAT(extra_columns, ", ", split_by);
      SET group_by := CONCAT(group_by, ", ", split_by);
    ELSE
      SET group_by := group_by; 
  END CASE;

  SET query := CONCAT('SELECT ', extra_columns, ', ', count_column, ' AS count FROM ', query_table, ' AS t', query_where);
  SET query := CONCAT_WS('', query, group_by);

  RETURN query;
END
```


### radius_traffic_total

select nas, count(*) from radius_traffic_total group by nas
```
0	           78543
168848919	  329462
168979991	  167293
1674043144	    14
1674043147	161089
2887712800	  3418
2887712817	  7192
```



select company, direction, sum(bytes)
from radius_traffic_total group by company, direction
order by 3 desc LIMIT 20
```
3659	1	743699779628
3116	2	625502775854
3659	2	308142231981
3655	2	134790896253
3666	1	108531627083
3579	2	86611320084
3655	1	81948915483
3116	1	74895556907
3612	2	74864970094
3682	1	41605071448
3061	1	20826023011
3361	2	20412815912
3445	2	18166636202
3579	1	17617781901
3445	1	15959060214
3453	1	14895019133
3666	2	11677578270
3529	2	11483282990
3641	2	10268251016
3641	1	9165600332
```

### jangle_traffic_total

select company, sum(bytes), sum(packets)
from jangle_traffic_total group by company
order by 2 desc LIMIT 20
```
3659	701642133246	1104855546
3116	391760761968	702240597
0	248696776779	1425366043
3655	118486445140	478850276
3666	105797937626	116212614
3579	68895397100	88301688
3612	27887382918	33089811
3361	26842374565	137841777
3061	23851373740	84456412
3445	23256692577	109534648
3641	19377452967	25491997
3682	18875245910	26680010
3529	4768060669	10127310
3678	4293640458	22261032
3413	3769986692	22853983
3611	2314936781	22859490
3002	2249148084	3209555
2944	1740339888	7495980
3652	1404562322	2547532
2924	473912651	1998715
```

select direction, count(*) from jangle_traffic_total group by direction
```
1	471291
2	716287
```
select protocol, count(*) from jangle_traffic_total group by protocol
```
1	  176853
2	      80
6	  510891
17	420284
47	  1832
54	     1
112	 77565
132	   143
```

## Hourly jangle_traffic_total

```

     SELECT
         HOUR(FROM_UNIXTIME(timebin))  AS hour,
         SUM(bytes) AS bytes,
         direction
     FROM jangle_traffic_total
     GROUP BY
        HOUR(FROM_UNIXTIME(timebin)) ,
        direction

    hour         bytes  direction
0      0  3.898591e+10          1
1      0  1.998000e+10          2
2      1  2.792496e+10          1
3      1  2.092122e+10          2
4      2  2.670810e+10          1
5      2  2.110084e+10          2
6      3  2.958978e+10          1
7      3  1.697634e+10          2
8      4  2.560659e+10          1
9      4  1.711182e+10          2
10     5  2.498675e+10          1
11     5  1.943292e+10          2
12     6  3.537730e+10          1
13     6  1.739486e+10          2
14     7  2.627113e+10          1
15     7  1.769755e+10          2
16     8  2.883663e+10          1
17     8  1.979429e+10          2
18     9  3.534325e+10          1
19     9  1.895512e+10          2
20    10  4.075442e+10          1
21    10  2.459932e+10          2
22    11  4.026227e+10          1
23    11  2.594304e+10          2
24    12  5.347469e+10          1
25    12  2.906245e+10          2
26    13  4.395315e+10          1
27    13  5.212066e+10          2
28    14  4.252053e+10          1
29    14  6.207521e+10          2
30    15  3.573091e+10          1
31    15  6.288073e+10          2
32    16  3.292392e+10          1
33    16  6.105943e+10          2
34    17  3.011516e+10          1
35    17  4.089404e+10          2
36    18  4.030139e+10          1
37    18  6.388262e+10          2
38    19  3.455620e+10          1
39    19  1.159381e+11          2
40    20  3.329009e+10          1
41    20  1.138664e+11          2
42    21  3.236177e+10          1
43    21  6.909064e+10          2
44    22  3.175402e+10          1
45    22  6.662082e+10          2
46    23  3.059383e+10          1
47    23  3.663575e+10          2
```

## Day of week jangle_traffic_total

```
       SELECT
           DAYNAME(FROM_UNIXTIME(timebin))  AS dayname,
           SUM(bytes) AS bytes,
           direction
       FROM jangle_traffic_total
       GROUP BY
          DAYNAME(FROM_UNIXTIME(timebin)) ,
          direction

      dayname         bytes  direction
0      Friday  1.379454e+11          1
1      Friday  2.155435e+11          2
2      Monday  1.141178e+11          1
3      Monday  1.486445e+11          2
4    Saturday  9.387554e+10          1
5    Saturday  8.004481e+10          2
6      Sunday  9.097196e+10          1
7      Sunday  4.993788e+10          2
8    Thursday  1.263057e+11          1
9    Thursday  2.779690e+11          2
10    Tuesday  1.215070e+11          1
11    Tuesday  1.228672e+11          2
12  Wednesday  1.255761e+11          1
13  Wednesday  1.142918e+11          2
```

## analyze_company_groups loc  640


## analyze_company_devices_radius loc 317

### radius_traffic = 2,882,647

```
  bytes_in = datastore.query(
        SELECT company, msisdn, SUM(bytes) AS bytes_in 
         FROM radius_traffic  
         WHERE timebin >= %(start)s AND timebin < %(end)s 
         AND direction = 1 
         AND company != 0 
         GROUP BY company, msisdn"
```        

select FROM_UNIXTIME(min(timebin)), FROM_UNIXTIME(max(timebin)) from radius_traffic 

2019-06-13 16:30:00	   2020-11-24 19:30:00

select company, count(*) from radius_traffic group by company order by 2

```
3663	6
3731	6
3681	8
3673	12
3748	16
3725	54
3494	102
3680	127
3694	176
3552	352
0	1164
3717	1418
3678	1892
3612	2542
3453	3050
3333	3603
3662	3677
3690	5262
3641	5720
3666	6475
3682	10972
3002	11608
3579	12377
2924	12971
3529	15638
3652	16790
2944	22229
2926	23318
3655	38783
3611	41193
3413	64312
3445	78744
3659	252380
3061	701037
3361	735208
3116	809452
```

### last_seen
```
select 'subscriber_imei' as tbl, FROM_UNIXTIME(min(last_seen)), FROM_UNIXTIME(max(last_seen)) from subscriber_imei 
UNION ALL
select 'subscriber_imsi',  FROM_UNIXTIME(min(last_seen)), FROM_UNIXTIME(max(last_seen)) from subscriber_imsi 
UNION ALL
select 'subscriber_sgsn'  , FROM_UNIXTIME(min(last_seen)), FROM_UNIXTIME(max(last_seen)) from subscriber_sgsn 
UNION ALL
select 'subscriber_location', FROM_UNIXTIME(min(last_seen)), FROM_UNIXTIME(max(last_seen)) from subscriber_location
UNION ALL
select 'subscriber_login', FROM_UNIXTIME(min(last_seen)), FROM_UNIXTIME(max(last_seen)) from subscriber_login

subscriber_imei	      2019-06-20 14:19:50	2020-11-24 20:05:00
subscriber_imsi	      2019-11-04 15:36:18	2020-11-24 20:05:00
subscriber_sgsn	      2019-06-13 16:42:00	2020-11-24 20:05:00
subscriber_location	  2019-09-12 12:06:26	2020-11-21 11:21:05
subscriber_login	     2019-06-13 16:42:13	2020-11-21 11:17:34
```

### subscriber_imei
 


### subscriber_imsi

### subscriber_sgsn

### subscriber_location

### subscriber_login



### proc getActivity
```
CREATE PROCEDURE `getActivity`(q_company INT unsigned, 
   q_msisdn BIGINT unsigned, -- None
   q_apn INT unsigned,       -- None  
   q_data_type VARCHAR(256), 
   q_time_start INT unsigned, 
   q_time_end INT unsigned, 
   q_resolution INT unsigned, 
   q_split_by VARCHAR(256) 
   )
```
### proc getTraffic
```
CREATE PROCEDURE `getTraffic`(IN q_company INT unsigned,
   IN q_msisdn BIGINT unsigned,   -- None
   IN q_remote_ip INT unsigned,   -- None
   IN q_data_type VARCHAR(1024), 
   IN q_protocol INT unsigned,    -- None
   IN q_time_start INT unsigned, 
   IN q_time_end INT unsigned, 
   IN q_resolution INT unsigned, 
   IN q_split_by VARCHAR(256) 
  )
```  




## analyze_company_gamma loc 445
```
def read_data(company, resolution, data_type):
   if "activity" in data_type:
       data = callproc("getActivity")
   else:    
       data=callproc("getTraffic")

  for company in companies
     for data_type in [jangle-activity, jangle-bytes, radius-activity, radius-bytes]
        analyze_company(company, data_type)
```



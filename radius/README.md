
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

## Plan:

- monthly  traffic


### MySQL time functions
```
select min(timebin), FROM_UNIXTIME(min(timebin)) from radius_traffic_total
1560443400	2019-06-13 16:30:00

SELECT UNIX_TIMESTAMP('2019-06-13')
1560384000
SELECT FROM_UNIXTIME(1560384000)
2019-06-13 00:00:00

SELECT count(*) FROM t WHERE FROM_UNIXTIME(timebin, '%Y') = 2020

SELECT FROM_UNIXTIME(1560443400)    -- 2019-06-13 16:30:00

select    FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i')  -- to get minutes, and eliminate sec
from jangle_active LIMIT 1   -- 2019-06-13 16:30

SELECT FROM_UNIXTIME(1560443400, '%H')  16
SELECT FROM_UNIXTIME(1560443400, '%d-%H')  13-16
 
SELECT FROM_UNIXTIME(1560443400, '%M-%d-%H') June 13-16

SELECT FROM_UNIXTIME(1560443400, '%m-%d-%H')  06-13-16
```
### Protocols
https://en.wikipedia.org/wiki/List_of_IP_protocol_numbers

6 - TCP

### Top max bytes jangle_traffic_total

```
   SELECT *, 
   FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'),
   DAYNAME(FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'))
   FROM jangle_traffic_total
   ORDER BY bytes desc
   LIMIT 20
 ```
 
 Result:

```
timebin   apn company protocol direction bytes packets time 
1601577000	5	3116	6	2	10520765373	7491495	2020-10-01 18:30	Thursday
1601579700	5	3116	6	2	10476941903	7457455	2020-10-01 19:15	Thursday
1601578800	5	3116	6	2	9983608418	7113062	2020-10-01 19:00	Thursday
1603397700	5	3116	6	2	9979289904	7092765	2020-10-22 20:15	Thursday
1601577900	5	3116	6	2	9929807492	7069128	2020-10-01 18:45	Thursday
1601580600	5	3116	6	2	9660529139	6878037	2020-10-01 19:30	Thursday
1603398600	5	3116	6	2	9377162481	6660161	2020-10-22 20:30	Thursday
1603395000	5	3116	6	2	8680442386	6153481	2020-10-22 19:30	Thursday
1598644800	2	3116	6	2	7408205094	5267305	2020-08-28 20:00	Friday
1598645700	2	3116	6	2	7348598469	5220708	2020-08-28 20:15	Friday
1598646600	2	3116	6	2	7291490638	5180611	2020-08-28 20:30	Friday
1598641200	2	3116	6	2	7082716542	5041431	2020-08-28 19:00	Friday
1596753000	2	3116	6	2	7042785943	5000179	2020-08-06 22:30	Thursday
1598643900	2	3116	6	2	6955617499	4946710	2020-08-28 19:45	Friday
1596753900	2	3116	6	2	6923592266	4914699	2020-08-06 22:45	Thursday
1598643000	2	3116	6	2	6509930005	4639749	2020-08-28 19:30	Friday
1601581500	5	3116	6	2	6165283124	4388315	2020-10-01 19:45	Thursday
1598642100	2	3116	6	2	5827357995	4154874	2020-08-28 19:15	Friday
1603396800	5	3116	6	2	5690717014	4051007	2020-10-22 20:00	Thursday
1596752100	2	3116	6	2	5239919119	3725440	2020-08-06 22:15	Thursday
```
### Top max bytes jangle_traffic 
```  
   SELECT *, 
   FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'),
   DAYNAME(FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'))
   FROM jangle_traffic  
   ORDER BY bytes desc
   LIMIT 20   
   
timebin   apn company msisdn protocol remote_ip direction bytes packets time    
1584133200	2	    0	    0	    6	3232356699	2	3921072930	2783444	2020-03-13 21:00	Friday
1584139500	2	    0	    0	    6	3232356699	2	3501680181	2481644	2020-03-13 22:45	Friday
1584134100	2	    0	    0	    6	3232356699	2	2766547457	1967634	2020-03-13 21:15	Friday
1584132300	2    	0	0	6	3232356699	2	2471983586	1751303	2020-03-13 20:45	Friday
1584140400	2	    0	0	6	3232356699	2	2024601694	1437569	2020-03-13 23:00	Friday
1608152400	5	    0	0	17	2899902849	2	1362252577	996714	2020-12-16 21:00	Wednesday
1584135000	2	0	0	6	3232356699	2	1280284769	910567	2020-03-13 21:30	Friday
1584388800	2	0	0	6	3232356699	2	1197331848	851393	2020-03-16 20:00	Monday
1584384300	2	0	0	6	3232356699	2	1160189224	824539	2020-03-16 18:45	Monday
1584469800	2	0	0	6	3232356699	2	1137729743	809016	2020-03-17 18:30	Tuesday
1584376200	2	0	0	6	3232356699	2	1132645022	803161	2020-03-16 16:30	Monday
1584138600	2	0	0	6	3232356699	2	1119702535	797737	2020-03-13 22:30	Friday
1608151500	5	0	0	17	2899902849	2	1099896152	802951	2020-12-16 20:45	Wednesday
1584389700	2	0	0	6	3232356699	2	1091797778	776666	2020-03-16 20:15	Monday
1606945500	5	3666	16229271536	17	3124787451	1	1074854423	886499	2020-12-02 21:45	Wednesday
1584386100	2	0	0	6	3232356699	2	1057945038	751397	2020-03-16 19:15	Monday
1584141300	2	0	0	6	3232356699	2	968078151	690617	2020-03-13 23:15	Friday
1584475200	2	0	0	6	3232356699	2	928824806	661311	2020-03-17 20:00	Tuesday
1596894300	2	3116	882350831625864	6	3232356699	2	918117879	648785	2020-08-08 13:45	Saturday
1584136800	2	0	0	6	3232356699	2	904359750	644785	2020-03-13 22:00	Friday
```

### top bytes for radius_traffic_total
```
   SELECT *, 
   FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'),
   DAYNAME(FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'))
   FROM radius_traffic_total
   ORDER BY bytes desc
   LIMIT 20
  
   
  timebin  company nas shotname sgsn mccmnc direction bytes time 
1596753000	3116	168848919	1	1254508369	302720	2	22224907969	2020-08-06 22:30	Thursday
1599091200	3116	168848919	1	1254508369	302720	2	18365814511	2020-09-03 00:00	Thursday
1598644800	3116	0	4	0	0	2	18291987328	2020-08-28 20:00	Friday
1596753000	3579	168848919	1	2794026947	310410	2	16957797870	2020-08-06 22:30	Thursday
1598646600	3116	0	4	0	0	2	15825058107	2020-08-28 20:30	Friday
1596753000	3116	168848919	1	1254508641	302720	2	14721199906	2020-08-06 22:30	Thursday
1606386600	3659	1674043147	5	2794058583	310410	1	13925834296	2020-11-26 10:30	Thursday
1599091200	3116	168848919	1	1254508641	302720	2	13695969110	2020-09-03 00:00	Thursday
1598643000	3116	0	4	0	0	2	12754886392	2020-08-28 19:30	Friday
1598641200	3116	0	4	0	0	2	10995448463	2020-08-28 19:00	Friday
1596749400	3116	168848919	1	1254508369	302720	2	10674895947	2020-08-06 21:30	Thursday
1596754800	3116	168848919	1	1254508369	302720	2	10078681923	2020-08-06 23:00	Thursday
1607412600	3116	168979991	1	1254508401	302720	2	8907350581	2020-12-08 07:30	Tuesday
1596751200	3116	168848919	1	1254508369	302720	2	8511857362	2020-08-06 22:00	Thursday
1596751200	3579	168848919	1	2794026947	310410	2	8398982578	2020-08-06 22:00	Thursday
1606384800	3659	1674043147	5	3353306488	311480	1	8296867444	2020-11-26 10:00	Thursday
1601578800	3116	168979991	1	1254508369	302720	2	8155727214	2020-10-01 19:00	Thursday
1591642800	3612	168848919	1	2794060243	310410	2	7890745314	2020-06-08 19:00	Monday
1601577000	3116	168979991	1	1254508369	302720	2	7810048834	2020-10-01 18:30	Thursday
1607416200	3116	168979991	1	1254508369	302720	2	7357551217	2020-12-08 08:30	Tuesday
 ```  

### top bytes for radius_traffic 
```
   SELECT *, 
   FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'),
   DAYNAME(FROM_UNIXTIME(timebin, '%Y-%m-%d %H:%i'))
   FROM radius_traffic 
   ORDER BY bytes desc
   LIMIT 20
   
   #	timebin	company	msisdn	nas	shortname	sgsn	mccmnc	direction	bytes	 timebin 
1	1,596,753,000	3,579	882,350,837,661,988	168,848,919	1	2,794,026,947	310,410	2	16,957,797,870	2020-08-06 22:30	Thursday
2	1,606,386,600	3,659	16,229,271,501	1,674,043,147	5	2,794,058,583	310,410	1	11,826,205,691	2020-11-26 10:30	Thursday
3	1,607,412,600	3,116	882,350,837,661,965	168,979,991	1	1,254,508,401	302,720	2	8,729,412,890	2020-12-08 07:30	Tuesday
4	1,596,751,200	3,579	882,350,837,661,988	168,848,919	1	2,794,026,947	310,410	2	8,398,982,578	2020-08-06 22:00	Thursday
5	1,591,642,800	3,612	882,350,837,661,984	168,848,919	1	2,794,060,243	310,410	2	7,890,745,314	2020-06-08 19:00	Monday
6	1,606,386,600	3,666	16,229,271,595	1,674,043,147	5	2,889,433,257	310,260	1	7,095,458,922	2020-11-26 10:30	Thursday
7	1,596,753,000	3,529	882,350,831,625,835	168,848,919	1	1,254,508,369	302,720	2	4,869,557,957	2020-08-06 22:30	Thursday
8	1,590,519,600	3,612	882,350,837,661,984	168,848,919	1	2,794,060,243	310,410	2	4,561,411,543	2020-05-26 19:00	Tuesday
9	1,607,416,200	3,116	882,350,831,625,812	168,979,991	1	1,254,508,369	302,720	2	4,489,664,175	2020-12-08 08:30	Tuesday
10	1,607,412,600	3,116	882,350,831,625,812	168,979,991	1	1,254,508,369	302,720	2	4,489,656,912	2020-12-08 07:30	Tuesday
11	1,607,418,000	3,116	882,350,837,661,965	168,979,991	1	1,254,508,401	302,720	2	4,364,903,030	2020-12-08 09:00	Tuesday
12	1,607,416,200	3,116	882,350,837,661,965	168,979,991	1	1,254,508,401	302,720	2	4,364,839,685	2020-12-08 08:30	Tuesday
13	1,607,414,400	3,116	882,350,837,661,965	168,979,991	1	1,254,508,401	302,720	2	4,364,772,052	2020-12-08 08:00	Tuesday
14	1,605,699,000	3,116	882,350,831,625,893	168,979,991	1	1,254,508,205	302,720	2	4,008,875,828	2020-11-18 11:30	Wednesday
15	1,605,697,200	3,116	882,350,831,625,893	168,979,991	1	1,254,508,205	302,720	2	4,008,823,254	2020-11-18 11:00	Wednesday
16	1,604,521,800	3,116	882,350,831,625,893	168,979,991	1	1,254,508,205	302,720	2	3,973,986,635	2020-11-04 20:30	Wednesday
17	1,604,275,200	3,116	882,350,831,625,893	168,979,991	1	1,254,508,205	302,720	2	3,966,838,585	2020-11-02 00:00	Monday
18	1,603,926,000	3,116	882,350,831,625,893	168,979,991	1	1,254,508,205	302,720	2	3,956,553,502	2020-10-28 23:00	Wednesday
19	1,603,711,800	3,116	882,350,831,625,893	168,979,991	1	1,254,508,205	302,720	2	3,950,586,518	2020-10-26 11:30	Monday
20	1,592,334,000	3,612	882,350,837,661,984	168,848,919	1	2,794,060,243	310,410	2	3,938,362,843	2020-06-16 19:00	Tuesday
   
   
```

###  timebin range for all tables
```
select 'radius_traffic_total' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from radius_traffic_total
union ALL
select 'radius_traffic' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from radius_traffic
union ALL
select 'radius_events_total' as T,  count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from radius_events_total
union ALL
select 'radius_events' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from radius_events
union ALL
select 'radius_active' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from radius_active

UNION ALL

select 'jangle_traffic_total' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from jangle_traffic_total
union all
select 'jangle_traffic' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from jangle_traffic
union all
select 'jangle_tcp_total' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from jangle_tcp_total
union all
select 'jangle_tcp' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from jangle_tcp

UNION ALL

select 'cdr_traffic_total' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from cdr_traffic_total
union ALL
select 'cdr_traffic' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from cdr_traffic
union ALL
select 'cdr_traffic_active' as T, count(*) as cnt, FROM_UNIXTIME(min(timebin)) as min, FROM_UNIXTIME(max(timebin)) as max from cdr_traffic_active

```
```
radius_traffic_total	758462	2019-06-13 16:30:00	2020-11-28 23:00:00
radius_traffic	     3081322	2019-06-13 16:30:00	2020-11-28 23:00:00

radius_events_total	  717655	2019-06-13 16:30:00	2020-11-28 23:00:00
radius_events	       2716174	2019-06-13 16:30:00	2020-11-28 23:00:00
radius_active	       1777863	2019-06-13 16:30:00	2020-11-28 23:00:00

jangle_traffic_total 1204256	2019-12-18 16:30:00	2020-11-28 23:15:00
jangle_traffic	    40171058	2019-12-18 16:30:00	2020-11-28 23:15:00

jangle_tcp_total	    788194	  2019-12-18 16:30:00	2020-11-28 23:15:00
jangle_tcp	        44822267	2019-12-18 16:30:00	2020-11-28 23:15:00

cdr_traffic_total	   2968854	2019-03-16 02:15:00	2020-11-28 10:45:00
cdr_traffic	         6861720	2019-03-16 02:15:00	2020-11-28 10:45:00
cdr_traffic_active	 6861720	2019-03-16 02:15:00	2020-11-28 10:45:00
```
### getDataTypeTablePrefix

```
CREATE FUNCTION `_getDataTypeTablePrefix`(q_data_type VARCHAR(256) 
  ) RETURNS text CHARSET utf8mb4
BEGIN
  DECLARE table_prefix VARCHAR(256);

  CASE q_data_type
    WHEN 'activity' THEN
      IF _tableExists('radius_traffic') THEN
        RETURN 'radius_events_';
      ELSEIF _tableExists('mc_traffic') THEN
        RETURN 'mc_';
      ELSEIF _tableExists('jangle_traffic') THEN
        RETURN 'jangle_';
      ELSE
        RETURN 'cdr_';
      END IF;
    WHEN 'bytes' THEN
      IF _tableExists('mc_traffic') THEN
        RETURN 'mc_';
      ELSEIF _tableExists('jangle_traffic') THEN
        RETURN 'jangle_';
      ELSEIF _tableExists('radius_traffic') THEN
        RETURN 'radius_';
      ELSE
        RETURN 'cdr_';
      END IF;
    WHEN 'cdr-activity' THEN
      RETURN 'cdr_traffic_';
    WHEN 'cdr-bytes' THEN
      RETURN 'cdr_';
    WHEN 'mc-activity' THEN
      RETURN 'mc_';
    WHEN 'mc-bytes' THEN
      RETURN 'mc_';
    WHEN 'jangle-activity' THEN
      RETURN 'jangle_';
    WHEN 'jangle-bytes' THEN
      RETURN 'jangle_';
    WHEN 'radius-activity' THEN
      RETURN 'radius_';
    WHEN 'radius-bytes' THEN
      RETURN 'radius_';
    WHEN 'radius-events' THEN
      RETURN 'radius_';
    ELSE
      RETURN NULL;
  END CASE;
END
```
### getTraffic
```
CREATE PROCEDURE `getTraffic`(IN q_company INT unsigned,
   IN q_msisdn BIGINT unsigned, 
   IN q_remote_ip INT unsigned, 
   IN q_data_type VARCHAR(1024), 
   IN q_protocol INT unsigned, 
   IN q_time_start INT unsigned, 
   IN q_time_end INT unsigned, 
   IN q_resolution INT unsigned, 
   IN q_split_by VARCHAR(256) 
  )
BEGIN
  CALL execQuery(_getTrafficQuery(q_company, q_msisdn, q_remote_ip, q_data_type, q_protocol, q_time_start, q_time_end, q_resolution, "time", q_split_by));
END



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



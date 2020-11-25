### RADIUS CDR
Remote Authentication Dial In User Service (RADIUS) for streaming the Call Detail Records (CDR).

https://wiki.freeradius.org/Home

https://networkradius.com/doc/FreeRADIUS%20Technical%20Guide.pdf

https://habr.com/ru/post/51882/

https://www.dialogic.com/webhelp/BorderNet2020/2.2.0/WebHelp/radius_ov.htm

https://support.sonus.net/display/UXDOC61/Working+with+Call+Detail+Records

https://support.sonus.net/display/UXDOC61/Retreiving+Call+Detail+Records+From+a+RADIUS+Server

https://support.sonus.net/display/UXDOC61/Call+Detail+Records+Primer

https://wifisoft.zendesk.com/hc/en-us/articles/203566091-Understanding-RADIUS-session-records-CDRs-


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


## IMEI - International Mobile Equipment Identity
https://en.wikipedia.org/wiki/International_Mobile_Equipment_Identity

https://en.wikipedia.org/wiki/MSISDN

## IMSI - international mobile subscriber identity 
An international mobile subscriber identity (IMSI) number uniquely identifies a cellphone subscriber. It's usually stored in a SIM card. 
The IMSI is used internally within cellphone systems to identify a phone.

## MSISDN  number is a cellphone's phone number
A mobile subscriber integrated services digital network (MSISDN) number is a cellphone's phone number. 
Most users don't know their IMSIs, while the MSISDN can be dialed to reach the phone.

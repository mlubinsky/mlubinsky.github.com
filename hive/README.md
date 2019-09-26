hive.exec.max.dynamic.partitions.pernode (default value being 100) is the maximum dynamic partitions that can be created by each mapper or reducer.

hive.exec.max.created.files 

hive.exec.max.dynamic.partitions

hive.merge.mapfiles=true 

hive.merge.mapredfiles=true

hive> set mapred.reduce.tasks=32;

## LEFT SEMI JOIN
In order check the existence of a key in another table, the user can use LEFT SEMI JOIN as illustrated by the following example.
```
INSERT OVERWRITE TABLE pv_users
SELECT u.*
FROM user u LEFT SEMI JOIN page_view pv ON (pv.userid = u.id)
WHERE pv.date = '2008-03-03';
```

##  Dynamic-Partition Insert

This is multi-insert:
```
FROM page_view_stg pvs
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country='US')
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip WHERE pvs.country = 'US'
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country='CA')
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip WHERE pvs.country = 'CA'
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country='UK')
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip WHERE pvs.country = 'UK';
```
Dynamic-partition insert (or multi-partition insert) :
In the dynamic partition insert, the input column values are evaluated to determine which partition this row should be inserted into. If that partition has not been created, it will create that partition automatically. Using this feature you need only one insert statement to create and populate all necessary partitions. 
```
FROM page_view_stg pvs
INSERT OVERWRITE TABLE page_view PARTITION(dt='2008-06-08', country)
       SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip, pvs.country
```       

If the input column value is NULL or empty string, the row will be put into a special partition, whose name is controlled by the hive parameter hive.exec.default.partition.name. The default value is HIVE_DEFAULT_PARTITION{}. Basically this partition will contain all "bad" rows whose value are not valid partition names


set hive.exec.dynamic.partition.mode=nonstrict;
```
beeline> FROM page_view_stg pvs
      INSERT OVERWRITE TABLE page_view PARTITION(dt, country)
             SELECT pvs.viewTime, pvs.userid, pvs.page_url, pvs.referrer_url, null, null, pvs.ip,
                    from_unixtimestamp(pvs.viewTime, 'yyyy-MM-dd') ds, pvs.country
             DISTRIBUTE BY ds, country;
```             
This query will generate a MapReduce job rather than Map-only job. The SELECT-clause will be converted to a plan to the mappers and the output will be distributed to the reducers based on the value of (ds, country) pairs. The INSERT-clause will be converted to the plan in the reducer which writes to the dynamic partitions.


## ARRAYS , explode, inline, stack  LATERAL VIEW

<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+LateralView>
Built-in Table-Generating Functions (UDTF):
* explode() takes in an array (or a map) as an input and outputs the elements of the array (map) as separate rows. \
* posexplode() is similar to explode ; it returns the element as well as its position in the original array.

* inline() explodes an array of structs to multiple rows. Returns a row-set with N columns (N = number of top level elements in the struct), one row per 

* stack() Breaks up n values V1,...,Vn into r rows. Each row will have n/r columns. r must be constant.

Lateral view is used in conjunction with user-defined table generating functions such as explode(). 
```
SELECT pageid, adid
FROM pageAds LATERAL VIEW explode(adid_list) adTable AS adid;

CREATE TABLE array_table (int_array_column ARRAY<INT>);

select explode(array('A','B','C'));
select explode(array('A','B','C')) as col;
select tf.* from (select 0) t lateral view explode(array('A','B','C')) tf;
select tf.* from (select 0) t lateral view explode(array('A','B','C')) tf as col;
select posexplode(array('A','B','C'));


select inline(array(struct('A',10,date '2015-01-01'),struct('B',20,date '2016-02-02')));
```

## Custom Map/Reduce Scripts

 TRANSFORM clause   embeds the mapper and the reducer scripts.
```
SELECT TRANSFORM(pv_users.userid, pv_users.date) USING 'map_script' AS dt, uid CLUSTER BY dt FROM pv_users;
```

## Keywords MAP and REDUCE
MAP and REDUCE are "syntactic sugar" for the more general select transform:

```
FROM (
     FROM pv_users
     MAP pv_users.userid, pv_users.date
     USING 'map_script'
     AS dt, uid
     CLUSTER BY dt) map_output
 
 INSERT OVERWRITE TABLE pv_users_reduced
     REDUCE map_output.dt, map_output.uid
     USING 'reduce_script'
     AS date, count;
 ```    
## Distribute by . Sort by
<https://cwiki.apache.org/confluence/display/Hive/LanguageManual+SortBy>

Hive uses the columns in SORT BY to sort the rows before feeding the rows to a reducer.

Difference between Sort By and Order By
Hive supports SORT BY which sorts the data per reducer. The difference between "order by" and "sort by" is that the former guarantees total order in the output while the latter only guarantees ordering of the rows within a reducer. If there are more than one reducer, "sort by" may give partially ordered final results.

Cluster By and Distribute By are used mainly with the Transform/Map-Reduce Scripts. But, it is sometimes useful in SELECT statements if there is a need to partition and sort the output of a query for subsequent queries.

Cluster By is a short-cut for both Distribute By and Sort By.

Hive uses the columns in Distribute By to distribute the rows among reducers. All rows with the same Distribute By columns will go to the same reducer. However, Distribute By does not guarantee clustering or sorting properties on the distributed keys.

## Co-Groups

```
FROM (
     FROM (
             FROM action_video av
             SELECT av.uid AS uid, av.id AS id, av.date AS date
 
            UNION ALL
 
             FROM action_comment ac
             SELECT ac.uid AS uid, ac.id AS id, ac.date AS date
     ) union_actions
     SELECT union_actions.uid, union_actions.id, union_actions.date
     CLUSTER BY union_actions.uid) map
 
 INSERT OVERWRITE TABLE actions_reduced
     SE
```

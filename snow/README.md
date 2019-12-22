### Overview

<http://dwgeek.com/snowflake-architecture-cloud-data-warehouse.html/>

<https://docs.snowflake.net/manuals/other-resources.html>

<https://nl.devoteam.com/wp-content/uploads/sites/15/2018/04/a-detailed-view-inside-snowflake.pdf>

<https://s3.amazonaws.com/snowflake-workshop-lab/Snowflake_free_trial_LabGuide.pdf>

<https://blog.getdbt.com/how-we-configure-snowflake/>

<https://hevodata.com/blog/snowflake-data-warehouse-features/>

<https://discourse.getdbt.com/t/structure-snowflake-database-schema/211/9>

<https://www.infoq.com/presentations/snowflake-automatic-clustering/>

 By default, Snowflake cluster is based on the order in which we receive the records. Just imagine a stream of records coming into the system and we just chop when we are able to create the file size. The only partitioning logic that we use is, "Are we able to create the file size that we want?" We keep collecting, let's say, we have 10 records when we can create the file size that we want, we chop at every 10 records and create this file and flush to S3. As you can see, it's the values are grouped only by one dimension and that is the dimension in which data is being loaded into the system. It's not grouped by any other logical dimension within the data. We don't look into the data itself and try to group it based on a specific column by default.

### Migration from Redshift
<https://community.snowflake.com/s/article/Migrating-from-Redshift-to-Snowflake>

<https://support.snowflake.net/s/article/How-To-Migrate-Data-from-Amazon-Redshift-into-Snowflake>

https://community.snowflake.com/s/article/Migrating-from-Redshift-to-Snowflake-in-Python

<https://snowflakesolutions.net/snowflake-vs-redshift/>

<https://discourse.getdbt.com/t/the-difference-between-users-groups-and-roles-on-postgres-redshift-and-snowflake/429>

<https://medium.com/@jthandy/how-compatible-are-redshift-and-snowflakes-sql-syntaxes-c2103a43ae84>

```
Warehouses” and “databases” are not the same thing within Snowflake. A database in Snowflake really 
just represents a storage partition, while warehouses are compute resources.

You can have multiple warehouses processing data in the same “database” concurrently. 
For example, you can have a “segment” warehouse writing to the “raw” database 
at the same time a “stitch” warehouse is writing to the “raw” database. 
I am not aware of any scaling considerations with “databases” within Snowflake. 
My understanding is that a database is just an organizational partition on top of the storage to help
with stuff like permissions. Your scaling would be handled with warehouses.
```


<https://docs.snowflake.net/manuals/sql-reference-commands.html>

<https://www.sigmacomputing.com/blog> . SIGMACOMPUTING

<https://yellowbrick.com/> .   YELLOWBRICK


https://towardsdatascience.com/machine-learning-in-snowflake-fdcff3bdc1a7

<https://docs.snowflake.net/manuals/user-guide/tables-micro-partitions.html>

<http://cloudsqale.com/2019/12/02/snowflake-micro-partitions-and-clustering-depth/>

<https://medium.com/hashmapinc/snowflakes-cloud-data-warehouse-what-i-learned-and-why-i-m-rethinking-the-data-warehouse-75a5daad271c>

<https://tech.instacart.com/migration-from-redshift-to-snowflake-the-path-for-success-4caaac5e3728>

<https://medium.com/@richiebachala/snowflake-redshift-bigquery-b84d2cb60168>


<https://www.alooma.com/answers/why-did-you-choose-snowflake-over-amazon-redshift-for-your-cloud-data-warehouse>

<https://www.alooma.com/blog/a-guide-to-selecting-the-right-cloud-data-warehouse>

<https://www.periscopedata.com/blog/interactive-analytics-redshift-bigquery-snowflake>

<https://hevodata.com/blog/snowflake-vs-redshift/>

<https://medium.com/@ubethke/comparing-snowflake-cloud-data-warehouse-to-aws-athena-query-service-4f0ea32ef6db>


<https://0x0fff.com/snowflake-the-good-the-bad-and-the-ugly/>

<https://www.snaplogic.com/blog/observations-from-the-snowflake-summit-19>

<https://www.reddit.com/r/aws/comments/6mm6p4/what_is_your_experience_using_snowflake/>

<https://www.reddit.com/r/bigdata/comments/e1g7jf/are_there_any_competitors_to_snowflake/>

## Data Load

<https://www.linkedin.com/pulse/building-etlelt-solutions-leverage-power-snowflake-2-van-schalkwyk/>

<https://www.linkedin.com/pulse/building-etlelt-solutions-leverage-power-snowflake-1-van-schalkwyk/> 
https://www.blendo.co/blog/etl-snowflake-data-warehouse/

 For example, you might want to exclude some PII related fields from loading into the data warehouse for privacy reasons.

Snowflake, allows you to perform some tasks like:

Filtering fields/columns out during COPY
Perform CASTING on your fields if you want to change your data types
Reorder your columns
Truncate data
Your COPY command for a bulk or Snowpipe loading process can contain a “SELECT” part which transforms the data based on your requirements.

Thatis is possible because of the great separation between storage and processing in Snowflake.

We saw that it is possible to perform some core transformation tasks during the loading of your data into Snowflake. Although this is a powerful mechanism, you might still need to transform further your data to make it ready for consumption for your analysts. For example, you might want to create fact and dimension tables as part of a star schema.



https://docs.snowflake.net/manuals/user-guide/data-load-snowpipe-intro.html

### Looker
<https://blog.redpillanalytics.com/managing-snowflake-data-warehouse-compute-in-looker-e445543987b2>

<https://github.com/llooker/snowflake-usage-block>

<https://medium.com/sevensenders-techblog/speaking-data-with-snowflake-and-looker-e4b219ed37aa>

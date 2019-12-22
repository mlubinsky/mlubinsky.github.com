<https://blog.getdbt.com/how-we-configure-snowflake/>

<https://hevodata.com/blog/snowflake-data-warehouse-features/>

<https://discourse.getdbt.com/t/structure-snowflake-database-schema/211/9>

### Migration from Redshift
<https://community.snowflake.com/s/article/Migrating-from-Redshift-to-Snowflake>

<https://support.snowflake.net/s/article/How-To-Migrate-Data-from-Amazon-Redshift-into-Snowflake>

https://community.snowflake.com/s/article/Migrating-from-Redshift-to-Snowflake-in-Python


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


### Looker
<https://blog.redpillanalytics.com/managing-snowflake-data-warehouse-compute-in-looker-e445543987b2>

<https://github.com/llooker/snowflake-usage-block>

<https://medium.com/sevensenders-techblog/speaking-data-with-snowflake-and-looker-e4b219ed37aa>

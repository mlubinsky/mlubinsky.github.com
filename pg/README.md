## Postgres

<https://www.youtube.com/watch?v=uhvqly8MtoI> Postgres12

<https://pynative.com/python-postgresql-tutorial/>

<https://habr.com/ru/company/postgrespro/blog/442462/>

<https://habr.com/ru/company/okko/blog/443276/>

<https://habr.com/ru/post/444018/>

<https://habr.com/ru/company/postgrespro/blog/443792/>

<https://cube.dev/blog/postgresql-query-optimization/>

<https://news.ycombinator.com/item?id=19765761>


<https://wiki.postgresql.org/wiki/Don%27t_Do_This>

<https://pgdash.io/blog/postgres-features.html>

```
CREATE TABLE Apt99_2016 (time TIMESTAMP WITH TIME ZONE NOT NULL, value REAL);

\copy Apt99_2016 (time, value) FROM '/home/michael/apartment/2016/Apt99_2016.csv' DELIMITER ',' CSV;

COPY 503760

select min(time), max(time) from Apt99_2016;
          min           |          max
------------------------+------------------------
 2016-01-01 00:00:00+00 | 2016-12-15 19:59:00+00
 
 
select date_trunc('hour', time) h_time , count(*) from Apt99_2016 group by  1;

select date_trunc('hour', time) h_time , count(*) from Apt99_2016 group by  h_time;

create TABLE Apt99_2016_hourly AS select date_trunc('hour', time) as time, sum(value) as value from Apt99_2016 group by  1;

8395

 select max(time) from Apt99_2016_hourly;
          max
------------------------
 2016-12-15 19:00:00+00


 select max(time) - interval '1680 hours' from Apt99_2016_hourly;
        ?column?
------------------------
 2016-10-06 19:00:00+00
 
 select count(*) from Apt99_2016_hourly WHERE time > '2016-10-06 19:00'::timestamp ;
 count
-------
  1680
``` 

<https://rob.conery.io/2018/08/13/transactional-data-operations-in-postgresql-using-common-table-expressions/>

$ sudo systemctl {status|stop|start} postgresql-11

$ brew services start postgresql (MacOS)
```
ALTER USER michael PASSWORD 'myPassword';
psql -d michael -U michael -p 5432 -h 18.221.216.253
(for postgres: changeme)
psql -h 18.188.19.105 -U postgres
```

### PORT
default port 5432 
The default port of Postgres is commonly configured in file postgresql.conf

SELECT * FROM pg_settings WHERE name = 'port';
 
$ psql -h localhost -U postgres -p 5433  #  connect to non-standard port

$ sudo -u postgres -i

```
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

```

$ sudo -u postgres createuser -s new_user

To create a superuser role and a database for your personal user account:
$ sudo -u postgres createuser -s $(whoami) .  # -s means: super user
$ createdb $(whoami)


\dt . is the same as SELECT * FROM pg_catalog.pg_tables

\l is the equivalent of show databases

$ psql --help
```
Connection options:
  -h, --host=HOSTNAME      database server host or socket directory (default: "local socket")
  -p, --port=PORT          database server port (default: "5432")
  -U, --username=USERNAME  database user name (default: "miclub01")
  -w, --no-password        never prompt for password
  -W, --password           force password prompt (should happen automatically)

For more information, type "\?" (for internal commands) or "\help" (for SQL
commands) from within psql, 
```
$ psql -l
```
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | miclub01 | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
 template0 | miclub01 | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/miclub01          +
           |          |          |             |             | miclub01=CTc/miclub01
 template1 | miclub01 | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/miclub01          +
           |          |          |             |             | miclub01=CTc/miclub01
           
```           
### Config files
```
# show hba_file;
------------------------------------
 /var/lib/pgsql/11/data/pg_hba.conf

# show config_file;
----------------------------------------
 /var/lib/pgsql/11/data/postgresql.conf
 

sudo grep host  /var/lib/pgsql/11/data/pg_hba.conf
host    all             all             127.0.0.1/32         ident
host    all             all             0.0.0.0/0            md5

ident authentication uses the operating system’s identification server running at TCP port 113 to verify the user’s credentials.

peer authentication on the other hand, is used for local connections and verifies that the logged in username of the operating system matches the username for the Postgres database.


```

## Grafana

<https://habr.com/ru/post/448676/>

<https://grafana.com/docs/reference/templating/#the-timefilter-or-timefilter-variable>
WHERE $__timeFilter(
<https://youtu.be/FhNUrueWwOk?list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2> . Variables in Grafana

<https://grafana.com/docs/reference/templating/>

<https://kb.groundworkopensource.com/display/DOC721/How+to+GroundWork+Grafana+dashboard+variables>

The templating feature allows you to create variables that can be used in your metric queries, series names and panel titles. Use this feature to create generic dashboards that can quickly be changed to show graphs for different servers or metrics.

<http://localhost:3000/>

<http://localhost:3000/datasources>

http://ec2-18-221-216-253.us-east-2.compute.amazonaws.com:3000/login . admin/admin1

<https://grafana.com/plugins/postgres>

<http://docs.grafana.org/features/datasources/postgres/>

<https://grafana.com/blog/2018/10/15/make-time-series-exploration-easier-with-the-postgresql/timescaledb-query-editor/>

<https://stackoverflow.com/questions/48512014/using-postgres-with-grafana>

<https://habr.com/ru/company/1cloud/blog/443006/>

<https://www.youtube.com/watch?v=sKNZMtoSHN4&index=7&list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2>

## Links

<http://www.interdb.jp/pg/index.html>

<https://www.qwertee.io/blog/postgresql-b-tree-index-explained-part-1/>

<https://pgdash.io/blog/postgres-features.html>

<https://tech.codeyellow.nl/blog/pg-timezones/>

<https://pgdash.io/blog/postgres-configuration-cheatsheet.html>

<http://www.craigkerstiens.com/2018/01/31/postgres-hidden-gems/>

<https://www.citusdata.com/blog/2018/10/31/materialized-views-vs-rollup-tables/>

<https://heapanalytics.com/blog/engineering/when-to-avoid-jsonb-in-a-postgresql-schema>

<https://explain.depesz.com/> .  Explain plan explained

<https://pgexercises.com/>

<https://severalnines.com/blog/my-favorite-postgresql-queries-and-why-they-matter>

<https://heapanalytics.com/blog/engineering/running-10-million-postgresql-indexes-in-production>

<https://postgresweekly.com/issues/286> .  Postgres in 2018 summary

<https://wiki.postgresql.org/wiki/Things_to_find_out_about_when_moving_from_MySQL_to_PostgreSQL>

Declarative Partitioning in version 11:
<https://www.postgresql.org/docs/11/static/ddl-partitioning.html#DDL-PARTITIONING-DECLARATIVE>

https://brandur.org/postgres-default
 
https://habr.com/post/419749/

https://wiki.postgresql.org/wiki/PostgreSQL_vs_SQL_Standard

https://pgdash.io/blog/postgres-features.html

http://www.databasesoup.com/2018/04/new-annotated-config-files-for.html    configs

https://severalnines.com/blog/postgresql-tuning-key-things-drive-performance

https://blog.2ndquadrant.com/scaling-iot-time-series-data-postgres-bdr/ time based partitioning

https://gist.github.com/Kartones/dd3ff5ec5ea238d4c546

https://www.youtube.com/watch?v=BgcJnurVFag Postgres at 20T and beyond

https://news.ycombinator.com/item?id=17638169

https://www.cybertec-postgresql.com/en/index-decreases-select-performance/#

https://pgdash.io/blog/partition-postgres-11.html

https://blog.timescale.com/scaling-partitioning-data-postgresql-10-explained-cd48a712a9a1

https://www.justwatch.com/blog/post/debugging-postgresql-performance-the-hard-way/

https://blog.algolia.com/building-real-time-analytics-apis/

https://github.com/bytefish/PgBulkInsert

https://severalnines.com/blog/my-favorite-postgresql-queries-and-why-they-matter

https://pgdash.io/blog/postgres-features.html

https://news.ycombinator.com/item?id=17356960

https://www.citusdata.com/blog/2018/01/24/citus-and-pg-partman-creating-a-scalable-time-series-database-on-PostgreSQL/

https://www.citusdata.com/blog/2016/09/09/pgcron-run-periodic-jobs-in-postgres/

https://www.citusdata.com/blog/2018/06/14/scalable-incremental-data-aggregation/

https://cldellow.com/2016/09/15/brin-indexes-in-postgres-9.5.html

https://blog.getbotmetrics.com/150x-speedup-in-real-time-dashboards-with-postgres-9-5-2e987a5b906e

https://www.citusdata.com/blog/2017/03/10/how-to-scale-postgresql-on-aws/

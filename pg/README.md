## Postgres

$ sudo systemctl {status|stop|start} postgresql-11
 
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
``` 

## Grafana

http://localhost:3000/



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

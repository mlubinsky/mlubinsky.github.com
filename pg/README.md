
https://dev.to/lnahrf/mastering-postgres-debugging-must-know-queries-for-database-troubleshooting-495a?fbclid=IwAR35x-9hEeFUeoJfv142jRBMB2SQTB2ndh77zvSfw628d27ITWGderkLTME


Postgre vs MySQL 
https://www.bytebase.com/blog/postgres-vs-mysql/


https://www.reddit.com/r/PostgreSQL/

https://planet.postgresql.org/

https://www.postgresonline.com/

stored procedure to rename tables and indexes:
https://habr.com/ru/articles/765484/

### Timezone
show timezone; -- America/Los_Angeles

 ALTER DATABASE db_name SET TIMEZONE TO 'new_timezone';


### Web Interface to Postgres PostREST, etc

https://habr.com/ru/articles/767442/

https://habr.com/ru/articles/757990/


https://github.com/apostoldevel/module-PGFetch

https://github.com/olifolkerd/tabulator

https://tabulator.info/docs/5.5

### Is it possible to pass params in view?

https://stackoverflow.com/questions/11401749/pass-in-where-parameters-to-postgresql-view

```
CREATE OR REPLACE FUNCTION param_labels(_region_label text, _model_label text)
  RETURNS TABLE (param_label text, param_graphics_label text)
  LANGUAGE sql AS
$func$
SELECT p.param_label, p.param_graphics_label
FROM   parameters      p 
JOIN   parameter_links l USING (param_id)
JOIN   regions         r USING (region_id)
JOIN   models          m USING (model_id)
WHERE  p.active
AND    r.region_label = $1 
AND    m.model_label = $2
ORDER  BY p.param_graphics_label;
$func$;
```
Another example:
```
create or replace function label_params(parm1 text, parm2 text)
  returns table (param_label text, param_graphics_label text)
as
$body$
  select ...
  WHERE region_label = $1 
     AND model_id = (SELECT model_id FROM models WHERE model_label = $2)
  ....
$body$
language sql;

Usage:

select *
from label_params('foo', 'bar')
```
Since Postgres 9.2 you can use the declared parameter names in place of $1 and $2 in SQL functions. 


### Passing array to function

```
create or replace function weekly_kpi (
_fix text, 
_source text, 
_chipset text[], 
_model text[], 
_category text, 
_metric text, 
_start_date DATE, 
_end_date DATE)
returns table (report_date DATE, description   text,  " "   float)
language sql as
$func$
select report_date, description,
CASE 
  WHEN _fix = 'AVG_ALL'     THEN kpi_value_avg
  WHEN _fix = 'AVG_VDR'     THEN kpi_value_avg_vdr
  WHEN _fix = 'AVG_NON_VDR' THEN kpi_value_avg_nonvdr
  WHEN _fix = 'STD_ALL'     THEN kpi_value_std
  WHEN _fix = 'STD_VDR'     THEN kpi_value_std_vdr
  WHEN _fix = 'STD_NON_VDR' THEN kpi_value_std_nonvdr
  WHEN _fix = 'MAX_ALL'     THEN kpi_value_max
  WHEN _fix = 'MAX_VDR'     THEN kpi_value_max_vdr
  WHEN _fix = 'MAX_NON_VDR' THEN kpi_value_max_nonvdr
 END  as " "
from kpi 
where kpi_source   = _source
  and chipset = ANY(_chipset)
  and model = ANY(_model)
  and kpi_category =  _category
  and kpi_metric= _metric
  and report_date >= _start_date and report_date <= _end_date
$func$;

select * from weekly_kpi(
'AVG_ALL', 
'Internal-RootEVT1', 
'{Apple,Berry, K43E1,Kiwi}'::text[], 
'{Apple_A15_Bionic,Full Android on S5E9945 ERD,Pixel_6_Pro,Pixel_7_Pro,RootEVT1,SM-G991N,SM-G996N,SM-S911N,SM-S916N}'::text[],
'VDR_ParkingGarage-HomePlus',
'2DError_CEP50',
DATE('2023-07-11T07:00:00Z') ,
DATE('2023-08-31T06:59:59Z')
)

------- Usage
select * from weekly_kpi(
'$value', 
'$source', 
 ARRAY[$chipset],
 ARRAY[$model],
'VDR_ParkingGarage-HomePlus',
'2DError_CEP50',
DATE($__timeFrom()) ,
DATE($__timeTo())
)
----------------------------------------
SELECT STRING_TO_ARRAY(
'HELLO WELCOME TO COMMAND PROMPT', ' ');

{HELLO,WELCOME,TO,COMMAND,PROMPT}

select * from weekly_kpi(
'$value', 
'$source', 
STRING_TO_ARRAY(ARRAY_TO_STRING(ARRAY[$chipset],','),',')::text[],
STRING_TO_ARRAY(ARRAY_TO_STRING(ARRAY[$model]  ,','),',')::text[],
'VDR_ParkingGarage-HomePlus',
'2DError_CEP50',
DATE($__timeFrom()) ,
DATE($__timeTo())
)
```




### Postgres queue

https://habr.com/ru/articles/763188/

https://adriano.fyi/posts/2023-09-24-choose-postgres-queue-technology/

https://tembo.io/blog/introducing-pgmq/  Message Queue

https://news.ycombinator.com/item?id=37636841

https://lobste.rs/s/rk3eft/choose_postgres_queue_technology

## Pub/Subscribe, queue, notify

https://news.ycombinator.com/item?id=37636841

https://ctodive.com/hooks-the-secret-feature-powering-the-postgres-ecosystem-f05b3b82e0ba hooks

https://blog.crunchydata.com/blog/message-queuing-using-native-postgresql

https://news.ycombinator.com/item?id=30119285

https://blog.arctype.com/postgres-notify-for-real-time-dashboards/


https://news.ycombinator.com/item?id=37610899  Ways to capture changes in Postgres

https://hakibenita.com/sql-for-data-analysis  

### EXECUTE format

https://www.postgresql.org/docs/current/plpgsql-statements.html

https://www.postgresql.org/docs/current/functions-string.html#FUNCTIONS-STRING-FORMAT

EXECUTE command-string [ INTO [STRICT] target ] [ USING expression [, ... ] ];

```
   EXECUTE 'SELECT count(*) FROM mytable WHERE inserted_by = $1 AND inserted <= $2'
   INTO c
   USING checked_user, checked_date;


   EXECUTE format('SELECT count(*) FROM %I '
   'WHERE inserted_by = $1 AND inserted <= $2', tabname)
   INTO c
   USING checked_user, checked_date;
```



https://stackoverflow.com/questions/11740256/refactor-a-pl-pgsql-function-to-return-the-output-of-various-select-queries/11751557#11751557

### Recursive SQL

A Different Type of SQL Recursion with PostgreSQL

https://github.com/vb-consulting/blog/discussions/1

https://indrajith.me/posts/recursive-queries-in-postgresql-for-hierarchial-data/

https://www.enterprisedb.com/postgres-tutorials/how-run-hierarchical-queries-oracle-and-postgresql

https://www.mendelowski.com/docs/postgresql/recursive-sql-queries/

```
WITH RECURSIVE cte AS (                                                                                                                                                          
SELECT emp_no, ename, manager_no, 1 AS level                                                                                                                                             FROM   dummy_table                                                                                                                                                                     
where manager_no is null                                                                                                                                                            
UNION  ALL                                                                                                                                                                               
SELECT e.emp_no, e.ename, e.manager_no, c.level + 1                                                                                                                                      FROM   cte c                                                                                                                                                                            
JOIN   dummy_table e ON e.manager_no = c.emp_no                                                                                  
)                                                                                                                                                                                     
SELECT *                                                                                                                                                                                 
FROM   cte;
```


### Postgres crosstab

https://learnsql.com/blog/creating-pivot-tables-in-postgresql-using-the-crosstab-function/

https://www.postgresonline.com/article_pfriendly/283.html

https://www.postgresql.org/docs/current/tablefunc.html
```
CREATE EXTENSION tablefunc;
select * from T;

CREATE TEMP TABLE T (dt DATE, name text, value float);
insert into T values ('2023-01-01', 'A', 100.0);
insert into T values ('2023-01-01', 'B', 200.0);
insert into T values ('2023-01-01', 'C', 300.0);

select * from crosstab( 'select dt, name, value from T order by 1,2')
as ct (dt DATE, val1 float, val2 float, val3 float);

|dt        |val1|val2|val3|
|----------|----|----|----|
|2023-01-01|100 |200 |300 |


select * from crosstab4( 'select dt::text, name, value::text from T order by 1,2');

|row_name  |category_1|category_2|category_3|category_4|
|----------|----------|----------|----------|----------|
|2023-01-01|100       |200       |300       |          |

```

https://stackoverflow.com/questions/15506199/dynamic-alternative-to-pivot-with-case-and-group-by/15514334#15514334

https://dba.stackexchange.com/questions/159280/how-do-i-generate-a-pivoted-cross-join-where-the-resulting-table-definition-is-u/159286#159286

### Postgress deep dive:

https://avestura.dev/blog/explaining-the-postgres-meme


### build dynamic SQL
```
Pivot this:
SELECT name, attr1, attr1, attr3, ... FROM T

Goal:   columns are: name_1, name_2, ...
Rows: attr1, attr2, attr_3,  etc


```


### PG function
```
CREATE OR REPLACE FUNCTION get_descriptions(category text, metric text = NULL, start_date DATE = NULL, end_date DATE = NULL)
-- returns setof varchar(255)
  returns setof kpi.description%TYPE
as $func$
DECLARE
 sql text := ' select distinct description from kpi where kpi_category = $1'; 
BEGIN
	sql := sql || ' AND kpi_metric =   $2 ';
 	sql := sql || ' AND report_date >= $3 '; 
 	sql := sql || ' AND report_date <= $4 ';
	RETURN QUERY EXECUTE sql using category, metric, start_date, end_date;
 
END;
$func$ language plpgsql IMMUTABLE;

SELECT get_descriptions('Driving_HighSpeed-Dongtan', 'Percentage_SpecIn_Speed(20Km/h)', '2022-01-01','2023-12-30')



create or replace function max_metrics(category text, metric text = NULL, start_date DATE = NULL, end_date DATE = NULL)
returns text
as $func$
declare
    kpi_source text :='MX'; -- TODO
    sql text := 'select distinct description from kpi where';
    result text := 'select report_date';
    description kpi.description%type;
--    all_desc setof text;
    all_desc varchar(50)[];
begin
--	sql := sql || ' kpi_category = $1 ';
    sql := sql || ' kpi_category = ' || quote_literal(category) ;
	sql := sql || ' AND kpi_source = '  || quote_literal(kpi_source); --  $2 '; -- MX OR Internal
--	sql := sql || ' AND kpi_metric =   $2 ';
    sql := sql || ' AND kpi_metric = '   || quote_literal(metric) ;
 	sql := sql || ' AND report_date >= ' ||  quote_literal(start_date) ; 
 	sql := sql || ' AND report_date <= ' ||  quote_literal(end_date) ;
    sql := sql || ' ORDER BY description ';
 
   
    --execute sql into all_desc;
    -- for description in all_desc
    for description in execute sql
--    loop
--    	raise notice '%' , description;
--    end loop
--    
--    for description in select * from exec(sql)  -- using category, metric, start_date, end_date
    loop
	     result := result || ', ';
    	 result := result || 'max(kpi_value) filter(where description=' || quote_literal(description)  || ') as ' || quote_ident(description);
    end loop;
   
    result := result || ' from kpi where kpi_source = ' || quote_literal(kpi_source) ;
    result := result || ' and kpi_category = '          || quote_literal(category)   ;
    result := result || ' and kpi_metric='              || quote_literal(metric)    ;
    result := result || ' and report_date >= '          || quote_literal(start_date) ; 
    result := result || ' and report_date <= '          || quote_literal(end_date)   ; 
    result := result || ' group by  report_date order by report_date asc';

    return result;
end
$func$ language plpgsql IMMUTABLE;

-------------------------------
 SELECT max_metrics('Driving_HighSpeed-Dongtan', 'Percentage_SpecIn_Speed(20Km/h)', '2022-01-01','2023-12-30')



There is a table with following columns:
   product,  vendor, date, price
 
I have to build an interactive report/dashboard (using Grafana).
to show 
max(price) per product  for every date within the user-provided interval.
 
So  SQL will look like 

SELECT date,
   max(price) filer(where product)='A') as A,
  max(price)  filer(where product)='B') as B,
  max(price)  filer(where product)='C') as C,
  ...
FROM T
where  
  date  BETWEEN $start_date and $end_date
group by date

The problem is that the product list is not fixed and cannot be hardcoded in SQL
It means that in SQL above the number of columns in SELECT list is not fixed.

To solve it I tried to build the dynamic SQL string inside Postgres.
As a first step I find out all products in given interval.
Then I build the final SQL by looping over products.
The issue is how to execute this SQL and return result to outsite wold?
As far as I know the Postgres function  signature allows to specify returns type as a table   ,
but in my case the number of columns in the table is defined dynamically, on fly

create or replace function max_price_per_product(start_date DATE, end_date DATE)
returns text
as $func$
declare
  prod T.product%type;
  prod_sql text;
  final_sql text = 'select date';
begin
  prod_sql = 'SELECT DISTINCT product from T';
  prod_sql := prod_sql || ' AND date >= ' ||  quote_literal(start_date);  
  prod_sql := prod_sql || ' AND date <= ' ||  quote_literal(end_date);
 
  for prod in execute prod_sql
  LOOP
     final_sql := final_sql || ', '
     final_sql := final_sql || 'max(price) filter(where product=' || quote_literal(prod) || ' ) as ' || quote_ident(prod)
  END LOOP;
 
    final_sql := final_sql || ' from T ' ;
    final_sql := final_sql || ' and date >= ' || quote_literal(start_date) ;
    final_sql := final_sql || ' and date <= ' || quote_literal(end_date)   ;
    final_sql := final_sql || ' group by  date order by  date asc';

    return final_sql;
end
$func$ language plpgsql IMMUTABLE;
But I do not know how to execute it 
```
### How do I get a list of column names from a psycopg2 cursor ?

https://stackoverflow.com/questions/10252247/how-do-i-get-a-list-of-column-names-from-a-psycopg2-cursor
```
curs.execute("Select * FROM people LIMIT 0")
cursor.fetchone()
colnames = [desc[0] for desc in curs.description]
```
### Schema
```
In Postgres, “public” is a Default schema. So, by default, Postgres users can access the "public" schema and create objects in it, such as views, tables, etc.

The SET SEARCH_PATH command, however, allows a user to set any other schema as the default schema. 

SHOW SEARCH_PATH;
SET SEARCH_PATH = example;
```
How to Change Default Schema Permanently at the Database Level?
```
ALTER DATABASE db_name SET search_path TO schema_name;
```
How to Change Default Schema Permanently at User Level?
```
To change a default schema at the user/role level, the “ALTER USER” or “ALTER ROLE” command is used with the “SET SEARCH_PATH” clause:

ALTER ROLE|USER role_name SET search_path TO schema_name;
```

### Less known Postgres features
https://hakibenita.com/postgresql-unknown-features

https://news.ycombinator.com/item?id=37309309

https://news.ycombinator.com/item?id=29163319

https://gist.github.com/ryanguill/101a19fb6ae6dfb26a01396c53fd3c66

https://medium.com/cognite/postgres-can-do-that-f221a8046e

https://news.ycombinator.com/item?id=37309309

https://pglocks.org/ PG locks

https://habr.com/ru/articles/756074/ PG columns alighnments

https://habr.com/ru/articles/753192/
```
create table order_data (
	order_date date,
	sales integer
);

insert into order_data
select date_trunc('day', dd), random() * 50000
from generate_series('2015-01-01'::date, '2025-01-01'::date, '1 minute') dd;
```

https://www.psycopg.org/docs/extras.html  Python Driver

### Audit table
https://www.heap.io/blog/how-postgres-audit-tables-saved-us-from-taking-down-production

### SQL optimization
https://towardsdatascience.com/how-we-optimized-postgresql-queries-100x-ff52555eabe


### Backup
https://www.postgresql.org/docs/current/backup.html

https://github.com/topics/postgresql-backup -- backup

https://github.com/fukawi2/pgsql-backup/blob/develop/src/pgsql-backup.sh

### tracing performance of individual queries inside stored procedure


RAISE NOTICE 'STEP X  timeofday= %',  timeofday();


### Is it guaranteed that bigserial column is unique across all partitions in Postgres 15 partitioned table?

https://stackoverflow.com/questions/76734370/is-it-guaranteed-that-bigserial-column-is-unique-across-all-partitions-in-postgr


https://luis-sena.medium.com/tuning-your-postgresql-for-high-performance-5580abed193d

### All constraints for given table:
https://reside-ic.github.io/blog/querying-for-foreign-key-constraints/
```

WITH unnested_confkey AS (
  SELECT oid, unnest(confkey) as confkey
  FROM pg_constraint
),
unnested_conkey AS (
  SELECT oid, unnest(conkey) as conkey
  FROM pg_constraint
)
select
  c.conname                   AS constraint_name,
  c.contype                   AS constraint_type,
  tbl.relname                 AS constraint_table,
  col.attname                 AS constraint_column,
  referenced_tbl.relname      AS referenced_table,
  referenced_field.attname    AS referenced_column,
  pg_get_constraintdef(c.oid) AS definition
FROM pg_constraint c
LEFT JOIN unnested_conkey con ON c.oid = con.oid
LEFT JOIN pg_class tbl ON tbl.oid = c.conrelid
LEFT JOIN pg_attribute col ON (col.attrelid = tbl.oid AND col.attnum = con.conkey)
LEFT JOIN pg_class referenced_tbl ON c.confrelid = referenced_tbl.oid
LEFT JOIN unnested_confkey conf ON c.oid = conf.oid
LEFT JOIN pg_attribute referenced_field ON (referenced_field.attrelid = c.confrelid AND referenced_field.attnum = conf.confkey)
WHERE tbl.relname ='PUT_TABLE_HERE'
;
```
simple
```
SELECT *
FROM
   information_schema.table_constraints 
   WHERE table_name='PUT_TABLE_NAME_HERE' 
```   
### Find all tables which are referencing the given table

https://stackoverflow.com/questions/5347050/postgresql-sql-script-to-get-a-list-of-all-tables-that-have-a-particular-column

https://dataedo.com/kb/query/postgresql/list-all-tables-refrenced-by-specific-table

```
SELECT
    r.table_name, 
    u.table_name,
    u.column_name,
    u.table_schema, 
    fk.*
FROM information_schema.constraint_column_usage       u
INNER JOIN information_schema.referential_constraints fk
           ON u.constraint_catalog = fk.unique_constraint_catalog
               AND u.constraint_schema = fk.unique_constraint_schema
               AND u.constraint_name = fk.unique_constraint_name
INNER JOIN information_schema.key_column_usage        r
           ON r.constraint_catalog = fk.constraint_catalog
               AND r.constraint_schema = fk.constraint_schema
               AND r.constraint_name = fk.constraint_name
WHERE
    u.table_name = 'PUT_TABLE_NAME_HERE'
```

### Find long-running query
```
SELECT
  pid,
  now() - pg_stat_activity.query_start AS duration,
  query,
  state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';
```

### How to find currently running SQL and kill it?
```
SELECT * FROM pg_stat_activity WHERE state = 'active';
So you can identify the PID of the hanging query you want to terminate, run this:

SELECT pg_cancel_backend(PID);
This query might take a while to kill the query, so if you want to kill it the hard way, run this instead:

SELECT pg_terminate_backend(PID);
```




https://www.postgresql.org/download/windows/

https://postgis.net/workshops/postgis-intro/installation.html PostGIS

https://www.yugabyte.com/postgresql/postgresql-high-availability/ High Availability

### Partitioning
https://www.postgresql.org/docs/current/ddl-partitioning.html

https://engineering.workable.com/postgres-live-partitioning-of-existing-tables-15a99c16b291

https://www.postgresql.org/docs/current/ddl-partitioning.html#DDL-PARTITIONING-DECLARATIVE

<https://habr.com/ru/company/barsgroup/blog/481694/> Partitioning

the upper bound is exclusive  !!!
```
CREATE TABLE t ( i int,  d DATE NOT NULL) PARTITION BY RANGE(d);
CREATE TABLE t_2022 PARTITION OF t for values from ('2022-01-01') to ('2023-01-01');
CREATE TABLE t_2023 PARTITION OF t for values from ('2023-01-01') to ('2024-01-01');
```
Also it is useful to create the default partition:

CREATE TABLE t_default PARTITION OF t DEFAULT;

https://alexey-soshin.medium.com/dealing-with-partitions-in-postgres-11-fa9cc5ecf466

can we create SERIAL column with UNIQUE constrain on table  partitioned by RANGE(date) ?
```
On partitioned tables, all primary keys, unique constraints and unique indexes must contain the partition expression.
 That is because indexes on partitioned tables are implemented by individual indexes on each partition,
and there is no way to enforce uniqueness across different indexes.
```
both the primary key and unique keys need to include the partition key

### Unique constraint
```
CREATE TABLE bar (
    pkey        SERIAL PRIMARY KEY,
    foo_fk      VARCHAR(256) NOT NULL REFERENCES foo(name), 
    name        VARCHAR(256) NOT NULL, 
    UNIQUE (foo_fk,name)
);

ALTER TABLE tablename ADD CONSTRAINT constraintname UNIQUE (columns);
```
### Serial column
https://stackoverflow.com/questions/244243/how-to-reset-postgres-primary-key-sequence-when-it-falls-out-of-sync


```
For serial column PostgreSQL will create a sequence with a name like tablename_colname_seq.
 Default column values will be assigned from this sequence. But when you explicitly insert a value into serial column,
it doesn’t affect sequence generator, and its next value will not change. So it can generate a duplicate value.

To prevent this after you inserted explicit values you need to change
the current value of a sequence generator either with ALTER SEQUENCE statement or with setval() function, e.g.:

ALTER SEQUENCE tablename_colname_seq RESTART WITH 52;
SELECT setval('tablename_colname_seq', (SELECT max(colname) FROM tablename));
```
If you do noit know the seq name then use this:
```
SELECT setval(pg_get_serial_sequence('tbl', 'tbl_id'), max(tbl_id)) FROM tbl;
```

### Primary key

ALTER TABLE table_name ADD CONSTRAINT some_constraint PRIMARY KEY(COLUMN_NAME1,COLUMN_NAME2);

### FK constraint
 foreign key must reference columns that either are a primary key or form a unique constraint
```
CREATE TABLE customers(
   customer_id INT GENERATED ALWAYS AS IDENTITY,
   customer_name VARCHAR(255) NOT NULL,
   PRIMARY KEY(customer_id)
);

CREATE TABLE contacts(
   contact_id INT GENERATED ALWAYS AS IDENTITY,
   customer_id INT,
   contact_name VARCHAR(255) NOT NULL,
   phone VARCHAR(15),
   email VARCHAR(100),
   PRIMARY KEY(contact_id),
   CONSTRAINT fk_customer
      FOREIGN KEY(customer_id) 
	  REFERENCES customers(customer_id)
);

Because the foreign key constraint does not have the ON DELETE and ON UPDATE action, they default to NO ACTION.
```

The RESTRICT action is similar to the NO ACTION. The difference only arises when you define the foreign key constraint as DEFERRABLE with an INITIALLY DEFERRED or INITIALLY IMMEDIATE mode.

ON DELETE SET NULL

ON DELETE CASCADE

ON DELETE SET DEFAULT

### Indexes
https://www.youtube.com/watch?v=mnEU2_cwE_s B-tree indexes (ru)

https://habr.com/ru/companies/otus/articles/747882/

https://kmoppel.github.io/2022-12-09-the-bountiful-world-of-postgres-indexing-options/




### Size of objects 

SELECT pg_size_pretty(pg_relation_size('t_test'));

###  JSON

https://habr.com/ru/companies/otus/articles/758010/

https://stackoverflow.com/questions/53086816/postgresql-aggregate-multiple-rows-as-json-array-based-on-specific-column/53087015#53087015
```
I would like to generate a JSON output, consisting of arrays of arrays, whereas each of the inner arrays contains the aggregated points of a trip (as indicated by trip_log_id).

SELECT json_agg(trips)
FROM (
    SELECT 
        json_agg(
            json_build_object(
                'recorded_at', created_at, 
                'latitude', latitude, 
                'longitude', longitude
            )
        ) as trips
    FROM data_tracks
    GROUP by trip_log_id
)s

1. json_build_object creates your main json objects
2. json_agg() ... GROUP BY trip_log_id groups these json objects into one trip object
3. second json_agg aggregates all trips into one array
```
### PG dump / restore

https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-pgdump-restore

Vaccum before backup:  https://www.postgresql.org/docs/current/sql-vacuum.html
```
select 
schemaname,
relname,
n_dead_tup,
n_live_tup,
round(n_dead_tup::float/n_live_tup::float*100) dead_pct,
autovacuum_count,
last_vacuum,
last_autovacuum,
last_autoanalyze,
last_analyze 
from pg_stat_all_tables 
where n_live_tup >0
order by n_dead_tup DESC
LIMIT 20;
```
The dead_pct column in this query is the percentage of dead tuples when compared to live tuples. 

A high dead_pct value for a table might indicate that the table isn't being properly vacuumed.


 
vacuum(analyze, verbose) <table_name> 



pg_restore is only compatible with compressed pg_dump files.

You MUST use psql to properly import plain-text backup files generated by pg_dump.
```
--jobs=njobs
Run the dump in parallel by dumping njobs tables simultaneously. This option may reduce the time needed to perform the dump
but it also increases the load on the database server. 
You can only use this option with the directory output format 
because this is the only output format where multiple processes can write their data at the same time.
```
https://docs.bit.io/docs/exporting-and-restoring-data-via-pg_dump-and-pg_restore

https://www.postgresql.org/docs/current/app-pgrestore.html

pd_dump Options: https://www.postgresql.org/docs/current/app-pgdump.html
```
-Fp   -F, --format=c|d|t|p output file format (custom, directory, tar, plain text (default)

c
custom
Output a custom-format archive suitable for input into pg_restore. Together with the directory output format, this is the most flexible output format in that it allows manual selection and reordering of archived items during restore. This format is also compressed by default.

d
directory
Output a directory-format archive suitable for input into pg_restore. 
This will create a directory with one file for each table and blob being dumped, 
plus a so-called Table of Contents file describing the dumped objects in a machine-readable format that pg_restore can read. 
A directory format archive can be manipulated with standard Unix tools; for example, 
files in an uncompressed archive can be compressed with the gzip tool. 
This format is compressed by default and also supports parallel dumps.

It is possible to dump multiple tables in parallel when using the directory dump format.
This is faster, but it also leads to a higher load on the database server. 
We control the number of tables exported in parallel using the '—jobs' option. 
In our example, we export three tables in parallel. It is not possible to redirect the output to a file as we are writing a directory.
We use the '—file' option instead with specification for the directory name:

The specified directory that the pg_dump will create must not exist. You can dump data into a specified directory by using the following command:

pg_dump -F d database_name -f database_directory
pg_dump --format=directory --jobs=3  --file=dump.dir database_name

```
Example of custom flag:
```
chcp 1252
set PGPASSWORD=my_password
pg_dump -h  ip_here -d dbname -U username -Fc --file=mydump.custom_format
```
### Restore using psql works only with plain text format (default)
 psql -U {user-name} -d {desintation_db}-f {dumpfilename.sql}



### Tune Postgres

https://wiki.postgresql.org/wiki/Don%27t_Do_This

work_mem is the maximum available memory per operation and not just per connection

set local work_mem = '50MB'

https://pgtune.leopard.in.ua/
 
 https://philbooth.me/blog/nine-ways-to-shoot-yourself-in-the-foot-with-postgresql
 
 https://news.ycombinator.com/item?id=35684220
 
### PgAdmin
 right click on database:
 ```
 psql tool
 query tool
```
### Create users and roles

https://chartio.com/learn/postgresql/create-a-user-with-pgadmin/
```
CREATE DATABASE xxx
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    
CREATE DATABASE yourdbname;
CREATE USER youruser WITH ENCRYPTED PASSWORD 'yourpass';
GRANT ALL PRIVILEGES ON DATABASE yourdbname TO youruser;    

```

## UI Clients 

<https://www.macpostgresclient.com/> . SQLPlus 

<https://eggerapps.at/postico/> Postico 

<https://tableplus.io/> TablePlus

https://retool.com/blog/best-postgresql-guis-in-2020/. Best UI tools for Postgres

https://arctype.com/

dbveaver https://dbeaver.io/



https://pganalyze.com/blog/how-postgres-chooses-index

https://www.crunchydata.com/blog/postgres-data-flow

https://www.youtube.com/watch?v=D8Q4n6YXdpk . Window function in Postgres

https://www.timescale.com/blog/how-postgresql-views-and-materialized-views-work-and-how-they-influenced-timescaledb-continuous-aggregates/

https://news.ycombinator.com/item?id=28776786. PG clustering /sharding

https://postgres.ai/blog/20220525-common-db-schema-change-mistakes

https://blog.crunchydata.com/blog/five-tips-for-a-healthier-postgres-database-in-the-new-year

https://news.ycombinator.com/item?id=29858083 . Tips for a Healthier Postgres Database 

https://habr.com/ru/company/tensor/blog/573214/ SQL optimization

https://habr.com/ru/company/tensor/blog/651407/. SQL optimization

https://habr.com/ru/post/657667/ TRY / CATCH в PostgreSQL

https://habr.com/ru/company/tensor/blog/675580/. working with NULL

https://habr.com/ru/company/tensor/blog/657895/ SQL HowTo: разные варианты работы с EAV

https://habr.com/ru/post/597651/ PostgreSQL: занимательный пример работы индексов, планировщика запросов и магии

https://www.pgmustard.com/blog/

https://news.ycombinator.com/item?id=29163319 	Lesser-known Postgres features

https://shekhargulati.com/2022/07/08/my-notes-on-gitlabs-postgres-schema-design/

https://hakibenita.com/tag/postgresql



sshtunnel to postgres

https://towardsdatascience.com/how-to-connect-to-a-postgresql-database-with-python-using-ssh-tunnelling-d803282f71e7

https://habr.com/ru/company/postgrespro/blog/579024/

https://habr.com/ru/company/tensor/blog/576894/

https://habr.com/ru/company/rostelecom/blog/566624/  Migration from Oracle to PG

https://habr.com/ru/company/timeweb/blog/562820/ do we need Redis if we have Postgres?

https://buttondown.email/nelhage/archive/notes-on-some-postgresql-implementation-details/

https://habr.com/ru/company/postgrespro/blog/576980/

https://habr.com/ru/company/postgrespro/blog/578196/ Запросы в PostgreSQL: 4. Индексное сканирование

## MySQL  
<https://realpython.com/python-mysql/>

https://ruddra.com/install-mysqlclient-macos/

https://habr.com/ru/post/539792/

connection via SSH tunneling

```
    pip install sshtunnel
    pip install mysql-connector-python
    pip install mysqlclient
```
connect via SSH 
```
import sshtunnel
import MySQLdb as db
import pandas as pd
ssh_host='192.168.240.177'
ssh_port=22
db_host = '127.0.0.1'
db_port=3306

SSH_USER='XXX'
SSH_PWD='YYY'
DB_USER=SSH_USER
DB_PWD='ZZZ'


def query(q):
     with sshtunnel.SSHTunnelForwarder(
          (ssh_host, ssh_port),
          ssh_username=SSH_USER,   
          ssh_password=SSH_PWD, 
          remote_bind_address=(db_host, db_port)
     ) as server:
          conn = db.connect(host=db_host,
          port=server.local_bind_port,
          user=DB_USER,
          passwd=DB_PWD,
          database='analytics')
          return pd.read_sql_query(q, conn)

df = query('select * from T')
print(df)
```
https://medium.com/@amirziai/query-your-database-over-an-ssh-tunnel-with-pandas-603ce49b35a1

https://stackoverflow.com/questions/21903411/enable-python-to-connect-to-mysql-via-ssh-tunnelling

```
SELECT DAYNAME('2008-05-15')

SELECT DAYOFWEEK(date)   1- Sunday 2 - Monday
```
Generate time series
```
select adddate('2020-01-01',  INTERVAL 1 HOUR)    
----------
select date from (
    select
        date_format(
        adddate('2011-01-01', INTERVAL @num:=@num+1 HOUR ),
        '%Y-%m-%d %H'
    ) date
    from
        radius_traffic_total ,
    (select @num:=-1) num
    limit
        366
) as dt
-----------------------------
select date from (
    select
        date_format(
        adddate('2011-01-01', @num:=@num+1),
        '%Y-%m-%d'
    ) date
    from
        radius_traffic_total ,
    (select @num:=-1) num
    limit
        366
) as dt
```
http://restsql.org/doc/Overview.html RestSQL

https://habr.com/ru/company/otus/blog/526400/ MySQL performance schema

https://news.ycombinator.com/item?id=24698660


###

https://spin.atomicobject.com/2021/02/04/redis-postgresql/

https://news.ycombinator.com/item?id=27482243

### Posthres Aggregator
https://planet.postgresql.org/

### PG and Python

https://khashtamov.com/en/postgresql-with-python-and-psycopg2/


## PG PG internals

https://habr.com/ru/articles/736154/ 
https://habr.com/ru/company/postgrespro/blog/574702/  PG internals

https://zerodha.tech/blog/working-with-postgresql/

https://habr.com/ru/company/tensor/blog/540572/

https://sql-info.de/postgresql/postgres-gotchas.html PG gotchas

https://wiki.postgresql.org/wiki/Don't_Do_This   Do not do it in PG

## Graph and tree extensions for postgres

https://hoverbear.org/blog/postgresql-hierarchical-structures/

https://news.ycombinator.com/item?id=27631765

https://news.ycombinator.com/item?id=26345755


### Time series on Postgress

https://age.apache.org/

https://www.postgresql.org/docs/current/ltree.html

https://blog.joshsoftware.com/2020/10/14/efficient-evenly-distributed-sampling-of-time-series-records-in-postgresql/

## PG on Mac
```
To have launchd start postgresql now and restart at login:
  brew services start postgresql
Or, if you don't want/need a background service you can just run:
  pg_ctl -D /usr/local/var/postgres start
```  
https://pgdash.io/blog/postgres-tips-and-tricks.html?p






<https://news.ycombinator.com/item?id=22718466> what is schema vs database in Postgres?

<https://habr.com/ru/company/tensor/blog/515786/> Antipatterns

<https://klotzandrew.com/blog/quickly-debugging-postgres-problems>

<https://bytes.yingw787.com/posts/2020/06/15/postgres_as_app_1/>

<https://hakibenita.com/sql-tricks-application-dba> 

<https://habr.com/ru/company/tensor/blog/511238/> GROUP SETs

<https://habr.com/ru/company/tensor/blog/508184/> Window functions

<http://www.interdb.jp/pg/>. internals

<https://medium.com/@rbranson/10-things-i-hate-about-postgresql-20dbab8c2791> What is wrong with Postgres?

<https://news.ycombinator.com/item?id=22775330>   What is wrong with Postgres?

<https://www.youtube.com/watch?v=xqTNceHxkIo> Postgres performance

<https://habr.com/ru/company/tensor/blog/498740/> SQL

<https://habr.com/ru/company/tensor/blog/494776/> SQL tricks

<https://habr.com/ru/company/tensor/blog/497008/>

<https://habr.com/ru/company/tensor/blog/492694/>


## Hierarhy

<https://towardsdatascience.com/recursive-sql-queries-with-postgresql-87e2a453f1b> Recursive SQL
<https://habr.com/ru/company/tensor/blog/501614/>.  how to manage the hierarhy of objects?

## Cube
https://www.postgresql.org/docs/current/cube.html

SP-Gist Index
https://habr.com/ru/company/postgrespro/blog/337502/

## Redis
<https://habr.com/ru/post/485672/>

## Materialize

Materialize is a streaming data warehouse. Materialize accepts input data from a variety of streaming sources (e.g. Kafka) and files (e.g. CSVs), and lets you query them using the PostgreSQL dialect of SQL.


<https://materialize.io/docs/>

<https://materialize.io/blog-olvm/>

## KeyDB

<https://habr.com/ru/company/flant/blog/478404/>

## Postgres

<https://www.graphile.org/postgraphile/postgresql-schema-design/>

<https://habr.com/ru/company/tensor/blog/492464/> 

<https://habr.com/ru/company/tensor/blog/492694/>

<https://towardsdatascience.com/recursive-sql-queries-with-postgresql-87e2a453f1b> Recursive SQL

<https://www.cybertec-postgresql.com/en/blog/>

<https://vladmihalcea.com/postgresql-triggers-isolation-levels/>


<http://www.interdb.jp/pg/index.html> PG internals

https://blog.crunchydata.com/blog/postgres-indexes-for-newbies index

<https://habr.com/ru/company/postgrespro/blog/479618/>

<https://begriffs.com/posts/2018-01-01-sql-keys-in-depth.html> PK, constraints, etc

<https://begriffs.com/posts/2017-10-21-sql-domain-integrity.html> constraints

<https://begriffs.com/posts/2017-08-27-deferrable-sql-constraints.html> deferrable constraints

<https://habr.com/ru/post/479920/> WITH ORDINALITY


https://habr.com/ru/post/481122/

<https://habr.com/ru/post/484670/> .  Query 

<https://habr.com/ru/post/479508/> PG antipatterns: JOINS

<https://habr.com/ru/post/485398/> hstore sv JSON

<https://habr.com/ru/post/479298/> PostgreSQL Antipatterns: CTE x CTE

<https://erthalion.info/2019/12/06/postgresql-stay-curious/> PG at low level

<https://news.ycombinator.com/item?id=21721832> PG at low level

<https://habr.com/ru/post/479656/> ANALYZE TABLE statistics

<https://habr.com/ru/post/488968/> Простое обнаружение проблем производительности в PostgreSQL
<https://habr.com/ru/company/tensor/blog/488104/>

<https://habr.com/ru/post/483460/> . Windows functions

<https://www.postgresql.org/docs/12/functions-aggregate.html>
```
select
    generate_series(1, 10) x,
    generate_series(4, 31, 3) y
into
    toy_example;
    
select
    regr_slope(y, x) as m,
    regr_intercept(y, x) as b
from
    toy_example;
    
    
select
    x, m * x + b as y
from
    generate_series(9, 14) as x,
    (
        select
            regr_slope(y, x) as m,
            regr_intercept(y, x) as b
        from
            toy_example
    ) as mb;    
```    

### Postgres in Docker

https://habr.com/ru/companies/piter/articles/736332/

<https://habr.com/ru/company/qiwi/blog/515692/>

https://habr.com/ru/post/578744/

https://habr.com/ru/post/581548/

<https://hub.docker.com/_/postgres>
```
docker pull postgres
docker run --name postgres -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=postgres -p 5432:5432 -d postgres
```
<https://pythonspeed.com/articles/faster-db-tests/>  

<https://towardsdatascience.com/tricks-for-postgres-and-docker-that-will-make-your-life-easier-fc7bfcba5082>

<https://github.com/karlkeefer/pngr>



<https://techcommunity.microsoft.com/t5/Azure-Database-for-PostgreSQL/Architecting-petabyte-scale-analytics-by-scaling-out-Postgres-on/ba-p/969685>

<https://github.com/sqitchers/sqitch> Database change management 

### stored procedures
<https://habr.com/ru/company/ruvds/blog/517302/>
<https://sivers.org/pg2> stored procedures

<https://news.ycombinator.com/item?id=21362190>

<https://www.cybertec-postgresql.com/en/joining-data-from-multiple-postgres-databases/>

<https://hakibenita.com/fast-load-data-python-postgresql>

### DISTINCT
<https://hakibenita.com/the-many-faces-of-distinct-in-postgre-sql> 

<https://www.yogeshchauhan.com/167/postgres/the-confusing-unique-and-useful-feature-in-postgres-distinct-on>

<https://news.ycombinator.com/item?id=22625642>


## Postgres 12

<https://www.cybertec-postgresql.com/en/discovering-less-known-postgresql-12-features/>

<https://rob.conery.io/2019/10/24/virtual-computed-columns-in-postgresql-12/>



<https://habr.com/ru/post/483014/>

<https://habr.com/ru/post/484978/>

<https://habr.com/ru/post/481556/>

<https://layerci.com/blog/postgres-is-the-answer/>

<https://news.ycombinator.com/item?id=21484215>

<https://threedots.tech/post/when-sql-database-makes-great-pub-sub/>

<https://news.ycombinator.com/item?id=21834152>

### Column store extension for PostgreSQL
<https://habr.com/ru/post/472396/>

<http://www.craigkerstiens.com/2019/11/13/postgres-interview-from-art-of-postgresql/>

## Merge Upsert

<https://pgdash.io/blog/postgres-insert.html>

<http://www.postgresqltutorial.com/postgresql-upsert/>

## Web dev on Postgres

<https://node-postgres.com> NodeJS driver/client

<https://www.npmjs.com/package/pg>

<https://github.com/aquametalabs/aquameta>

<https://news.ycombinator.com/item?id=21281042>

## Postgres schema

<https://www.cybertec-postgresql.com/en/tracking-view-dependencies-in-postgresql/>

<http://www.postgresqltutorial.com/postgresql-schema/>

<https://clarkdave.net/2015/06/aggregate-queries-across-postgresql-schemas/>

<https://severalnines.com/blog/postgresql-schema-management-basics>

<https://info.crunchydata.com/blog/demystifying-schemas-search_path-through-examples>

<https://dba.stackexchange.com/questions/185782/how-to-allow-user-access-to-non-owned-objects-in-postgres>

<https://knowledge.safe.com/articles/480/in-the-postgispostgres-reader-tables-from-a-differ.html>

```
SHOW search_path;
SET search_path TO myschema;
```
<https://stackoverflow.com/questions/34098326/how-to-select-a-schema-in-postgres-when-using-psql>

## Postgres 

<https://www.cybertec-postgresql.com/en/products/pg_timetable/> Job scheduling for Postgres

<http://www.postgresqltutorial.com/postgresql-cte/> CTE

<https://thebuild.com/presentations/not-your-job-pgconf-us-2017.pdf>

<http://www.craigkerstiens.com/2018/01/31/postgres-hidden-gems/>

<https://dev.to/heroku/postgres-is-underrated-it-handles-more-than-you-think-4ff3>

<https://lobste.rs/s/oqb6fu/postgres_is_underrated_it_handles_more>

<https://habr.com/ru/company/postgrespro/blog/443792/> Типичные ошибки при работе с PostgreSQL. Часть 2



<http://postgres-bits.herokuapp.com/#1>>

<https://wiki.postgresql.org/wiki/Don%27t_Do_This>


<https://www.youtube.com/watch?v=vFq9Yg8a3CE>

<https://gist.github.com/clhenrick/ebc8dc779fb6f5ee6a88>

<https://www.programming-books.io/essential/postgresql/>

<https://habr.com/ru/company/postgrespro/blog/330544/>

## Timeseries:

<https://github.com/ciconia/pmts>
PMTS is a collection of tools for working with time-series data in PostgreSQL written in SQL and PL/pgSQL, without needing to install extensions or work with outside tools. Its features include:

Automatic partitioning (sharding) of time-series tables by time range.
Automatic dropping of old partitions according to data retention settings.
Aggregation and summarizing utilities (WIP).

<https://www.cybertec-postgresql.com/en/postgresql-trivial-timeseries-examples/>

<https://www.cybertec-postgresql.com/en/timeseries-exclude-ties-current-row-and-group/>

## TimescalDB

<https://blog.timescale.com/blog/achieving-optimal-query-performance-with-a-distributed-time-series-database-on-postgresql/>

<https://habr.com/ru/company/oleg-bunin/blog/470902/>

## Indexes

<https://fosdem.org/2020/schedule/event/postgresql_a_deep_dive_into_postgresql_indexing/>

<https://fosdem.org/2020/schedule/event/postgresql_find_your_slow_queries_and_fix_them/>

```
select * from pg_indexes where tablename  = 'tracking';
```

<https://dzone.com/articles/looking-inside-postgres-at-a-gist-index> Gist

<https://habr.com/ru/company/postgrespro/blog/349224/>

<https://habr.com/ru/company/postgrespro/blog/330544/>

Combined index vs separate index 
<https://www.cybertec-postgresql.com/en/combined-indexes-vs-separate-indexes-in-postgresql/>

<https://habr.com/ru/company/mailru/blog/453046/> Indexes

<https://cube.dev/blog/postgresql-query-optimization/>

<https://news.ycombinator.com/item?id=19765761>


<https://wiki.postgresql.org/wiki/Don%27t_Do_This>

<https://pgdash.io/blog/postgres-features.html>


## Import JSON,XML files to postgres
https://github.com/okbob/pgimportdoc

## STORED PROCEDURES
<https://stackoverflow.com/questions/7945932/how-to-return-result-of-a-select-inside-a-function-in-postgresql>

<https://stackoverflow.com/questions/21662295/it-could-refer-to-either-a-pl-pgsql-variable-or-a-table-column>

## Python
<https://www.pgcli.com/> pgcli instead psql
<https://hakibenita.com/fast-load-data-python-postgresql>

<https://news.ycombinator.com/item?id=20399294>


https://blog.timescale.com/scaling-partitioning-data-postgresql-10-explained-cd48a712a9a1

http://www.craigkerstiens.com/categories/postgresql/

https://severalnines.com/blog/understanding-and-reading-postgresql-system-catalog

## Generate series

```
-- создаем миллион случайных чисел и строк
CREATE TABLE items AS
  SELECT
    (random()*1000000)::integer AS n,
    md5(random()::text) AS s
  FROM
    generate_series(1,1000000);
 ```   

```
  create table t(a integer, b text, c boolean);
  insert into t(a,b,c)
  select s.id, chr((32+random()*94)::integer), random() < 0.01
  from generate_series(1,100000) as s(id)
  order by random();
```  
<https://rob.conery.io/2018/08/01/simple-monthly-reports-in-postgresql-using-generate_series/>   

<https://habrahabr.ru/post/340460/>

<https://10clouds.com/blog/postgresql-10/>

<https://news.ycombinator.com/item?id=15634953>

```
select generate_series(1, 5);

SELECT RANDOM() AS tracking_id FROM generate_series(1, 5)


WITH full_dates as (
  --Select every date in range
  select generate_series(0,8) + date '2014-07-06' as fulldate
)
SELECT fulldate FROM full_dates;

-- use it with LEFT OUTER JOIN to eliminate gaps in data

WITH full_dates as (
  select generate_series(0,8) + date '2014-07-06' as fulldate
)
SELECT fulldate, COALESCE(temperature,0) as value 
FROM full_dates LEFT JOIN weather ON full_dates.fulldate=weather.date 
ORDER BY fulldate;
```

## Temporary view
http://vvvvalvalval.github.io/posts/using-postgresql-temporary-views-for-expressing-business-logic.html

https://severalnines.com/blog/using-kubernetes-deploy-postgresql

##  STORED PROCEDURES
<https://www.postgresql.org/docs/11/plpgsql-control-structures.html>
```
select n.nspname as schema_name,
       p.proname as specific_name,
       case p.prokind 
            when 'f' then 'FUNCTION'
            when 'p' then 'PROCEDURE'
            when 'a' then 'AGGREGATE'
            when 'w' then 'WINDOW'
            end as kind,
       l.lanname as language,
       case when l.lanname = 'internal' then p.prosrc
            else pg_get_functiondef(p.oid)
            end as definition,
       pg_get_function_arguments(p.oid) as arguments,
       t.typname as return_type
from pg_proc p
left join pg_namespace n on p.pronamespace = n.oid
left join pg_language l on p.prolang = l.oid
left join pg_type t on t.oid = p.prorettype 
where n.nspname not in ('pg_catalog', 'information_schema')
order by schema_name,
         specific_name;
```



## Trigger
<https://medium.com/@deb3007/trigger-function-in-postgresql-22e118bb082d>

## SQL
```
select distinct on (s.device_id) s.time, d.group_name, s.value 
from sensor_values s 
JOIN device_info d ON s.device_id=d.device_id 
ORDER BY s.device_id, time DESC;
```
 
<http://postgres-bits.herokuapp.com/#1>

<https://abelvm.github.io/sql/sql-tricks/>

<https://blog.jooq.org/2016/04/25/10-sql-tricks-that-you-didnt-think-were-possible/>

### LATERAL JOIN
 <https://heap.io/blog/engineering/postgresqls-powerful-new-join-type-lateral>
 
<https://abelvm.github.io/sql/sql-tricks/>

## Time Series analysis with postgres

<https://stackoverflow.com/questions/56863332/database-design-for-time-series>

<https://bytefish.de/blog/postgresql_interpolation/>
```
look for gaps in data greater than 1 hour.

CREATE OR REPLACE FUNCTION sample.datediff_seconds(start_t TIMESTAMP, end_t TIMESTAMP)
RETURNS DOUBLE PRECISION AS $$
    SELECT EXTRACT(epoch FROM $2 - $1) 
$$ LANGUAGE SQL;

SELECT  *
FROM (SELECT 
        weather_data.wban as wban, 
        weather_data.datetime as current_datetime,                 
        LAG(weather_data.datetime, 1, NULL) OVER (PARTITION BY weather_data.wban ORDER BY weather_data.datetime) AS previous_datetime
     FROM sample.weather_data) lag_select
WHERE sample.datediff_seconds (previous_datetime, current_datetime) > 3600;

```

<https://blog.hagander.net/finding-gaps-in-partitioned-sequences-203/> find gaps in sequences

<https://blog.jooq.org/2019/04/24/using-ignore-nulls-with-sql-window-functions-to-fill-gaps/>

<https://content.pivotal.io/blog/time-series-analysis-part-3-resampling-and-interpolation>

<https://tapoueh.org/blog/2018/02/find-the-number-of-the-longest-continuously-rising-days-for-a-stock/>


##  specify a password to psql non-interactively
```
PGPASSWORD=pass1234 psql -U MyUsername myDatabaseName

docker run -e PGPASSWORD="$(pbpaste)" --rm postgres psql -h www.example.com dbname username -c 'SELECT * FROM table;'
```

<https://habr.com/ru/company/oleg-bunin/blog/455248/>

<https://stackoverflow.com/questions/56552852/how-to-store-arrays-of-points-x-y-color-inside-postgres-array>

<https://stackoverflow.com/questions/56863332/database-design-for-time-series>

SELECT version();
```
cat docker-compose.yml
docker-compose up -d --no-deps --build postgrest
docker ps
docker log 5da443890939 
docker log 5da443890939 -f (like tail -f)


PGPASSWORD=changeme docker run -e PGPASSWORD=changeme -it --net=host --rm timescale/timescaledb psql -h localhost -U postgres -d timeseries -c "select * from sensor_info"

PGPASSWORD=changeme docker run -e PGPASSWORD=changeme -it --net=host --rm timescale/timescaledb psql -h localhost -U postgres -d timeseries -c "select * from device_info"
./pipeline.sh restart
curl -X POST -d 'json={"f":"1", "id": "016a0e2bf6bc000000000001001001d8", "d": [{"5000/0/5700": [{"t": 1555016324000, "v": {"current": 0.34444}}]}]}' http://localhost:8888/topic.test
PGPASSWORD=changeme docker run -e PGPASSWORD=changeme -it --net=host --rm timescale/timescaledb psql -h localhost -U postgres -d timeseries -c "select * from device_info"
PGPASSWORD=changeme docker run -e PGPASSWORD=changeme -it --net=host --rm timescale/timescaledb psql -h localhost -U postgres -d timeseries -c "select * from sensor_info"
PGPASSWORD=changeme docker run -e PGPASSWORD=changeme -it --net=host --rm timescale/timescaledb psql -h localhost -U postgres -d timeseries -c "select * from sensor_values"
  ```
## Functions
```
PostgreSQL NTILE Function
PostgreSQL PERCENT_RANK Function
PostgreSQL CUME_DIST Function
PostgreSQL Sequences
PostgreSQL LAG Function
PostgreSQL LEAD Function
PostgreSQL NTH_VALUE Function
PostgreSQL LAST_VALUE Function
PostgreSQL FIRST_VALUE Function
```

## LAG LEAD
```
DROP TABLE IF EXISTS weather;

CREATE TEMP TABLE weather(date date, temperature numeric);

INSERT INTO weather VALUES 
('2014-07-06', 86), ('2014-07-07', 88), 
('2014-07-08', 91), ('2014-07-09', 88), 
('2014-07-10', 86), ('2014-07-11', 84), 
('2014-07-12', 86), ('2014-07-13', 86);

SELECT date, temperature FROM weather ORDER BY date;

SELECT date, temperature, 
       LAG(temperature, 1) OVER(ORDER BY date) as day_before, 
       LEAD(temperature, 1) OVER(ORDER BY date) as day_after,
       (temperature - LAG(temperature, 1) OVER(ORDER BY date)) as difference_from_day_before
FROM weather ORDER BY date;
```

```
CREATE TABLE pay_history (
    employee_id int,
    fiscal_year INT,
    salary DECIMAL(10 , 2 ),
    PRIMARY KEY (employee_id, fiscal_year)
);
-- find both the current and previous year’s salary of all employees:
SELECT 
    employee_id, fiscal_year, salary,
    LAG(salary) OVER (
        PARTITION BY employee_id 
        ORDER BY fiscal_year) previous_salary
FROM
    pay_history;
```

##  DateTime,  timestamp и timestamptz , timezones

https://habr.com/ru/articles/772954/

select now()::timestamp, now();

SHOW timezone;

<https://phili.pe/posts/timestamps-and-time-zones-in-postgresql/>

<https://momjian.us/main/blogs/pgblog/2019.html#February_11_2019>

<https://tech.codeyellow.nl/blog/pg-timezones/>

<https://stackoverflow.com/questions/48069425/converting-between-timezones-in-postgre>
SET timezone TO 'Europe/Zurich';
SELECT now();
All timezone-aware dates and times are stored internally in UTC.
```
SELECT '2016-01-01 00:00+10'::timestamptz;
      timestamptz
------------------------
 2015-12-31 15:00:00+01
``` 
Timezone-aware dates and times are converted to local time in the zone specified by the TimeZone configuration parameter before being displayed to the client. 
 
This timezone configuration has another effect. When parsing a timestamp that has no time zone designator (e.g. Z or ±hhmm), it will be assumed to be local to the currently set timezone: 

Don't use BETWEEN (especially with timestamps)! Why not?
BETWEEN uses a closed-interval comparison: the values of both ends of the specified range are included in the result.
This is a particular problem with queries of the form
```
SELECT * FROM blah WHERE timestampcol BETWEEN '2018-06-01' AND '2018-06-08'
```
This will include results where the timestamp is exactly 2018-06-08 00:00:00.000000, but not timestamps later in that same day. So the query might seem to work, but as soon as you get an entry exactly on midnight, you'll end up double-counting it.

Instead, do:
```
SELECT * FROM blah WHERE timestampcol >= '2018-06-01' AND timestampcol < '2018-06-08'
```
<https://mode.com/blog/postgres-sql-date-functions>

<https://dba.stackexchange.com/questions/185192/join-2-tables-by-closest-time-postgresql-9-6>
approximate time match

<https://habr.com/ru/company/postgrespro/blog/459236/> tsrange

```
select extract(dow from date '2016-12-18');      -- 0
select extract(isodow from date '2016-12-18');   -- 7
```
SHOW datestyle;

SET datestyle = "ISO, DMY";

https://stackoverflow.com/questions/6123484/how-do-i-alter-the-date-format-in-postgres/6124387
```
Same outcome:
select time from tracking where time < '2019-06-12 23:00';
select time from tracking where time < '06-12-2019 23:00';

```

## Geometric data Types
```
CREATE TABLE GEO(
  p POINT,
  b BOX,
  c CIRCLE
);

INSERT INTO GEO(p) VALUES( POINT(1,10));
INSERT INTO GEO(b) VALUES( BOX( '(1,2), (10,20)' ));
INSERT INTO GEO(c) VALUES( CIRCLE('(1,10),20)' ));
```
## Recursive SQL
```
WITH RECURSIVE t(n) AS (
  VALUES (1)
UNION ALL
  SELECT n+1 FROM t WHERE n < 100
)
SELECT sum(n) FROM t;
```

### VIEW with parameters?

set returning function:
```
create or replace function label_params(parm1 text, parm2 text)
  returns table (param_label text, param_graphics_label text)
as
$body$
  select ...
  WHERE region_label = $1 
     AND model_id = (SELECT model_id FROM models WHERE model_label = $2)
  ....
$body$
language sql;
```
Then you can do:

select * . from label_params('foo', 'bar')


In most cases the set-returning function is the way to go, but in the event that you want to both read and write to the set, a view may be more appropriate. And it is possible for a view to read a session parameter:

CREATE VIEW widget_sb AS SELECT * FROM widget WHERE column = cast(current_setting('mydomain.myparam') as int)
```
SET mydomain.myparam = 0
select * from widget_sb
[results here]

SET mydomain.myparam = 1
select * from widget_sb
[distinct results here]
```
### JSON

SELECT ROW_TO_JSON(table_name) FROM table_name

 <https://habr.com/ru/post/475178/>

<https://vsevolod.net/postgresql-jsonb-index/>

<https://www.w3resource.com/PostgreSQL/postgresql-json-functions-and-operators.php>

json_to_recordset()
<https://dba.stackexchange.com/questions/98191/postgresql-json-data-type-used-as-nosql-but-view-as-relational-data-structure>
```
create table jsontable ( id integer, data json );
INSERT INTO jsontable VALUES (1,
  '[{"a": 1, "b": 2}, {"a": 3, "b":2}]');
INSERT INTO jsontable VALUES (2,
  '[{"a": 5, "b": 8}, {"a": 9, "b":0}]');

select * from jsontable;

select id, sum(a), sum(b)
  from jsontable j
    CROSS JOIN LATERAL
    json_to_recordset(j.data) as x(a integer, b integer)
group by id
```

<https://www.reddit.com/r/PostgreSQL/comments/2u6ah3/how_to_use_json_to_recordset_on_json_stored_in_a/>



```
CREATE TABLE X(
  id serial PRIMARY KEY,
  j JSONB
);


INSERT INTO X(j) VALUES(
'
{
"points" :
  [ 
     {"x":1, "y":2},
     {"x":10, "y":20}
  ]
}
'
);

select jsonb_array_elements_text(j->'points') FROM X;
select jsonb_array_elements_text((j->>'points')::jsonb) FROM X;
Same outcome for 2 SQL's above 
  
```  

 
### Arrays
```
CREATE TABLE people
 (
  id serial,
  name text,
  points geometry[]
 );
 


insert into people (name, points) values (
  'Lincoln', 
   ARRAY [
        ST_MakePoint(1,2),  
        ST_MakePoint(3,3)
   ]
 );  
 
 Arrays in Postgres are 1-based!
 
 SELECT points[1],  ST_X(points[1]) as X, ST_Y(points[1]) as Y from people;
                   points                   | x | y
--------------------------------------------+---+---
 0101000000000000000000F03F0000000000000040 | 1 | 2
 
 select UNNEST(points) p  from people;
 
 
 select ST_X(p) as x, ST_Y(p) as y FROM (select UNNEST(points) as p from people) AS U;
 
``` 
### array_agg() concatenates all the input values into a PostgreSQL array.
```
drop table data;
create table data (sensor_id INT, date date, value numeric, name TEXT );
insert into data values(1, '2014-07-06', 86, 'A1');
insert into data values(1, '2014-07-08', 99, 'A2');

select array_to_string(array_agg (value), ',') as all
from data ;

select array_to_string(array_agg (name), ',') as all
from data ;


select array_agg(lap)
from (
  select id, number, position, time, flag_type from laps
) lap;

{"(1,1,4,\"628.744\",\"Green\")","(2,2,4,\"614.424\",\"Green\")", ... }


To convert this PostgreSQL array into JSON, we can use the array_to_json

select array_to_json(array_agg(lap))
from (
  select id, number, position, time, flag_type from laps
) lap;

[{"id":1,
  "number":1,
  "position":4,
  "time":"628.744",
  "flag_type":"Green"},
  ...]
```


### PostGIS

SELECT postgis_full_version();

<https://gis.stackexchange.com/questions/58605/which-function-for-creating-a-point-in-postgis>

<https://stackoverflow.com/questions/57367822/issue-with-st-contains-and-st-within-in-postgis>
<https://lists.osgeo.org/pipermail/postgis-users/2019-August/043463.html>
<https://www.wyzant.com/resources/answers/704882/issue-with-postgis-st-within>

<https://www.postgis.us/presentations/FOSS4G2017_PostGISSpatialTricks.pdf>

```
CREATE TABLE m_polygon (id SERIAL PRIMARY KEY, bounds POLYGON);
INSERT INTO m_polygon(bounds) VALUES( 
  '(0.0, 0.0),  (0.0, 10.0), (10.0, 0.0), (10.0, 10.0), (0,0)' 
);

SELECT ST_WITHIN(m_polygon.bounds , m_polygon.bounds ) FROM m_polygon;

ERROR:  function st_within(polygon, polygon) does not exist 
HINT:  No function matches the given name and argument types. You might 
need to add explicit type casts.

The following works:

SELECT ST_WITHIN(ST_MakePoint(1,1), ST_MakePoint(1,1) ) ;

Answer:
POLYGON is Postgres native type. Geometry is the type used in PostGIS. ST_... functions are Postgis functions.

Note that you can restrict a PostGIS geometry to a specific subtype (geometry(POLYGON))
If you don't want PostGIS, you would need to use native geometry operators.
```
<https://www.postgresql.org/docs/current/functions-geometry.html>
```
If you are to use spatial data, and since you already have PostGIS, it is much better to switch to true geometries:

CREATE TABLE m_polygon (id SERIAL PRIMARY KEY, bounds geometry(POLYGON));
INSERT INTO m_polygon(bounds) VALUES( 
  st_geomFromText('POLYGON((0.0 0.0, 0.0 10.0, 10.0 0.0, 10.0 10.0, 0 0))') 
);

SELECT ST_WITHIN(m_polygon.bounds , m_polygon.bounds ) FROM m_polygon;
```
<https://stackoverflow.com/questions/42106271/geoalchemy2-st-within-type-mismatch-between-point-and-polygon>
<https://coder1.com/articles/postgis-query-point-within-polygon>

```
Possible solution: cast the Geography as a Geometry in the query because ST_Within,  do not support geographies, they only support geometries).
```
<http://www.postgis.net/docs/ST_GeomFromText.html>
<http://www.postgis.net/docs/ST_GeogFromText.html>
<https://gis.stackexchange.com/questions/284991/how-do-i-construct-a-geometry-point-in-srid-4326-from-lat-and-long/284994>
```
ST_Within(CAST (Store.location, Geometry), 
         ST_GeomFromEWKT('SRID=4326;POLYGON((150 -33, 152 -33, 152 -31, 150 -31, 150 -33))')
```

<https://www.bostongis.com/PrinterFriendly.aspx?content_name=postgis_tut01>
<https://www.youtube.com/watch?v=EBfjZgjyZmM> \
<http://postgis.refractions.net/docs/> \
<http://postgis.org/documentation/> \
<https://trac.osgeo.org/postgis/wiki/UsersWikiMain> \
<https://postgis.net/docs/> \
<http://postgis.net/workshops/postgis-intro/geometries.html#collections>

```
4.1.3. SQL-MM Part 3
The SQL Multimedia Applications Spatial specification extends the simple features for SQL spec by
defining a number of circularly interpolated curves.
The SQL-MM definitions include 3DM, 3DZ and 4D coordinates, 
but do not allow the embedding of SRID information.
The Well-Known Text extensions are not yet fully supported. 
Examples of some simple curved geometries are shown below:
CIRCULARSTRING(0 0, 1 1, 1 0)
CIRCULARSTRING(0 0, 4 0, 4 4, 0 4, 0 0)

The CIRCULARSTRING is the basic curve type, similar to a LINESTRING in the linear world. 
A single segment required three points, the start and end points (first and third) and any other point on the arc. The exception to this is for a closed circle, where the start and end points are the same. In this case the second point MUST be the center of the arc, ie the opposite side of the circle. To chain arcs together, the last point of the previous arc becomes the first point of the next arc, just like in LINESTRING. This means that a valid circular string must have an odd number of points greater than 1.

COMPOUNDCURVE(CIRCULARSTRING(0 0, 1 1, 1 0),(1 0, 0 1))

A compound curve is a single, continuous curve that has both curved (circular) segments and linear segments. That means that in addition to having well-formed components, the end point of every component (except the last) must be coincident with the start point of the following component.

CURVEPOLYGON(CIRCULARSTRING(0 0, 4 0, 4 4, 0 4, 0 0),(1 1, 3 3, 3 1, 1 1))

Example compound curve in a curve polygon: CURVEPOLYGON(COMPOUNDCURVE(CIRCULARSTRING(0 0,2 0, 2 1, 2 3, 4 3),(4 3, 4 5, 1 4, 0 0)), CIRCULARSTRING(1.7 1, 1.4 0.4, 1.6 0.4, 1.6 0.5, 1.7 1) )

A CURVEPOLYGON is just like a polygon, with an outer ring and zero or more inner rings. The difference is that a ring can take the form of a circular string, linear string or compound string.

As of PostGIS 1.4 PostGIS supports compound curves in a curve polygon.

MULTICURVE((0 0, 5 5),CIRCULARSTRING(4 0, 4 4, 8 4))

The MULTICURVE is a collection of curves, which can include linear strings, circular strings or compound strings.

MULTISURFACE(CURVEPOLYGON(CIRCULARSTRING(0 0, 4 0, 4 4, 0 4, 0 0),(1 1, 3 3, 3 1, 1 1)),((10 10, 14 12, 11 10, 10 10),(11 11, 11.5 11, 11 11.5, 11 11)))

This is a collection of surfaces, which can be (linear) polygons or curve polygons.
```



<https://postgis.net/docs/manual-2.5/postgis_installation.html#install_short_version>

<https://medium.com/@Umesh_Kafle/postgresql-and-postgis-installation-in-mac-os-87fa98a6814d>

<https://gist.github.com/clhenrick/ebc8dc779fb6f5ee6a88>

<https://stackoverflow.com/search?q=+postgis+extension+docker> PostGIS Docker

<https://hub.docker.com/r/mdillon/postgis/>

```
Common Spatial Queries
You may view more of these in my intro to Visualizing Geospatial Data with CartoDB.

Find all polygons from dataset A that intersect points from dataset B:

SELECT a.*
FROM table_a_polygons a, table_b_points b
WHERE ST_Intersects(a.the_geom, b.the_geom);
Find all rows in a polygon dataset that intersect a given point:

-- note: geometry for point must be in the order lon, lat (x, y)
SELECT * FROM nyc_tenants_rights_service_areas
where
ST_Intersects(
  ST_GeomFromText(
   'Point(-73.982557 40.724435)', 4326
  ),
  nyc_tenants_rights_service_areas.the_geom    
);
Or using ST_Contains:

SELECT * FROM nyc_tenants_rights_service_areas
where
st_contains(
  nyc_tenants_rights_service_areas.the_geom,
  ST_GeomFromText(
   'Point(-73.917104 40.694827)', 4326
  )      
);
Counting points inside a polygon:

With ST_Containts():

SELECT us_counties.the_geom_webmercator,us_counties.cartodb_id,
count(quakes.the_geom)
AS total
FROM us_counties JOIN quakes
ON st_contains(us_counties.the_geom,quakes.the_geom)
GROUP BY us_counties.cartodb_id;
To update a column from table A with the number of points from table B that intersect table A's polygons:

update noise.hoods set num_complaints = (
	select count(*)
	from noise.locations
	where
	ST_Intersects(
		noise.locations.geom,
		noise.hoods.geom
	)
);
Select data within a bounding box
Using ST_MakeEnvelope

HINT: You can use bboxfinder.com to easily grab coordinates of a bounding box for a given area.

SELECT * FROM some_table
where geom && ST_MakeEnvelope(-73.913891, 40.873781, -73.907229, 40.878251, 4326)
Select points from table a that do not fall within any polygons in table b
This method makes use of spatial indexes and the indexes on gid for better performance

SELECT
  a.gid,
  a.st_address,
  a.city,
  a.st_num,
  a.the_geom
FROM
  points AS a LEFT JOIN
  polygons AS b ON
  ST_Intersects(a.the_geom, b.the_geom)
WHERE b.gid IS NULL;

```
<https://gis.stackexchange.com/questions/192022/saving-array-of-objects-in-postgis-field>
```
{"type":"FeatureCollection","totalFeatures":1,"features":[
      {"type":"Feature",
       "id":1,"geometry":
          {
           "type":"LineString",
           "coordinates":
               [
                 [-74.103465, 4.80778], 
                 [-74.10410333333333, 4.8071633333333335], 
                 [-74.10492833333333, 4.806211666666667], 
                 [-74.10492833333333, 4.806211666666667]
               ]
          },
          "geometry_name":"the_geom",
          "properties":
            {
                "name":"test", "
                timestamps":                
                [358.0,1150.0,1705.0,1971.0,2385.0,3493.0,4506.0,4802]
            }
          },
  ]
}

CREATE TABLE spatial_table (
    name VARCHAR(20),
    timestamps timestamp[],
    the_geom geometry
)
```
psql -d [yourdatabase] -c "CREATE EXTENSION postgis;"

Topology is packaged as a separate extension and installable with command:

psql -d [yourdatabase] -c "CREATE EXTENSION postgis_topology;"

Many of the PostGIS functions are written in the PL/pgSQL procedural language. As such, the next step to create a PostGIS database is to enable the PL/pgSQL language in your new database. This is accomplish by the command below command. For PostgreSQL 8.4+, this is generally already installed

createlang plpgsql [yourdatabase]

Now load the PostGIS object and function definitions into your database by loading the postgis.sql definitions file (located in [prefix]/share/contrib as specified during the configuration step).

psql -d [yourdatabase] -f postgis.sql

For a complete set of EPSG coordinate system definition identifiers, you can also load the spatial_ref_sys.sql definitions file and populate the spatial_ref_sys table. This will permit you to perform ST_Transform() operations on geometries.

psql -d [yourdatabase] -f spatial_ref_sys.sql

SELECT postgis_full_version();

CREATE TABLE gtest (id serial primary key, name varchar(20), geom geometry(LINESTRING));


https://postgis.net/docs/manual-2.5/using_postgis_dbmanagement.html#RefObject

INSERT INTO geotable ( the_geom, the_name )
  VALUES ( ST_GeomFromText('POINT(-126.4 45.32)', 312), 'A Place');
  
  UPDATE artwork SET where_is = ST_POINT(X, Y);


```
create a new table for data from a CSV that has lat and lon columns:

create table noise.locations
(                                     
name varchar(100),
complaint varchar(100), descript varchar(100),
boro varchar(50),
lat float8,
lon float8,
geom geometry(POINT, 4326)
);
inputing values for the geometry type after loading data from a CSV:
update noise.locations set the_geom = ST_SetSRID(ST_MakePoint(lon, lat), 4326);

adding a geometry column in a non-spatial table:
select addgeometryColumn('table_name', 'geom', 4326, 'POINT', 2);

calculating area in EPSG 4326:
alter table noise.hoods set area = (select ST_Area(geom::geography));


SELECT ST_MakePoint(longitude,latitude) as geom FROM list_points

In order to use your new geometries with other PostGIS functions, you need to specify the coordinate system (SRID) of your points with the ST_SetSRID function. The most widely used system is SRID=4326; that is, GPS coordinates). If you have no idea where your data comes from, it’s probably this one.

So our request becomes:

SELECT ST_SetSRID(ST_MakePoint(longitude,latitude),4326) as geom
		 FROM list_points
Sometimes you may want to convert your data to a specific coordinate system. 
It is possible with the ST_Transform function, which moves the coordinates of a geometry from its current system to another one.


SELECT ST_AsText(geom) as points FROM list_geom
SELECT ST_X(geom) as longitude, ST_Y(geom) as latitude FROM list_geom

```



  
### PostgREST

https://news.ycombinator.com/item?id=25159097

<http://postgrest.org> 

<http://postgrest.org/en/v5.2/api.html#binary-output>

<https://gitter.im/begriffs/postgrest?source=all-rooms-list>

<https://github.com/dbohdan/automatic-api/>

PostgreSQL + PostgREST + react-admin == fantastic stack.

<https://gist.github.com/michelp/efc882ce86bd60d50dcf5f11442a2aaf>

<https://github.com/subzerocloud/postgrest-starter-kit>

REST call in postman: localhost:3000/sensor_info

<https://pynative.com/python-postgresql-tutorial/>

<https://habr.com/ru/company/postgrespro/blog/442462/>

<https://habr.com/ru/company/okko/blog/443276/>

<https://habr.com/ru/post/444018/>

<https://habr.com/ru/company/postgrespro/blog/443792/>



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
### Configuration

<https://www.cybertec-postgresql.com/en/setting-postgresql-configuration-parameters/> 

https://www.ongres.com/blog/postgresqlconf-configuration-for-humans/

<https://pgdash.io/blog/scaling-postgres.html> .  configuration

<https://pgdash.io/blog/postgres-configuration-cheatsheet.html>

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


## Links

<http://www.interdb.jp/pg/index.html>

<https://www.qwertee.io/blog/postgresql-b-tree-index-explained-part-1/>

<https://pgdash.io/blog/postgres-features.html>

## Scaling Postgres
<https://medium.com/avitotech/standby-in-production-scaling-application-in-second-largest-classified-site-in-the-world-97a79a1929de
>
<https://habr.com/ru/post/461997/> performance
<https://habr.com/ru/post/461071/>

## Explain plan

<https://fosdem.org/2020/schedule/event/postgresql_find_your_slow_queries_and_fix_them/>

<https://habr.com/ru/post/477624/>

<https://www.youtube.com/watch?v=IwahVdNboc8>

<https://pganalyze.com/ebooks/optimizing-postgres-query-performance?utm_source=PostgresWeeklySecondary>

<https://www.youtube.com/watch?v=uhvqly8MtoI> Postgres 12





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

https://blog.2ndquadrant.com/scaling-iot-time-series-data-postgres-bdr/ **time based partitioning**

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

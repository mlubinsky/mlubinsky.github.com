### Postgres Aggregator
<https://planet.postgresql.org/>

### Postgres Schema
```
In Postgres, “public” is a Default schema.  
So, by default, Postgres users can access the "public" schema and create objects in it,  
such as views, tables, etc.

The SET SEARCH_PATH command, however, allows a user to set any other schema as the default schema. 

SHOW SEARCH_PATH;
SET SEARCH_PATH = example;
```
How to Change Default Schema Permanently at the Database Level?
```sql
ALTER DATABASE db_name SET search_path TO schema_name;
```
How to Change Default Schema Permanently at User Level?

To change a default schema at the user/role level, the “ALTER USER” or “ALTER ROLE” command is used with the “SET SEARCH_PATH” clause:
```sql
ALTER ROLE|USER role_name SET search_path TO schema_name;
```
### Create users and roles

https://chartio.com/learn/postgresql/create-a-user-with-pgadmin/
```sql
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

### Size of Postgres objects 

SELECT pg_size_pretty(pg_relation_size('t_test'));

### All constraints for given table:
https://reside-ic.github.io/blog/querying-for-foreign-key-constraints/
```sql

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
Simple:

```sql
SELECT *
FROM
   information_schema.table_constraints 
   WHERE table_name='PUT_TABLE_NAME_HERE' 
```   
### Find all tables which are referencing the given table

https://stackoverflow.com/questions/5347050/postgresql-sql-script-to-get-a-list-of-all-tables-that-have-a-particular-column

https://dataedo.com/kb/query/postgresql/list-all-tables-refrenced-by-specific-table

```sql
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


### Unique constraint
```sql
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
```sql
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


### Find long-running query
```sql
SELECT
  pid,
  now() - pg_stat_activity.query_start AS duration,
  query,
  state
FROM pg_stat_activity
WHERE (now() - pg_stat_activity.query_start) > interval '5 minutes';
```

### How to find currently running SQL and kill it?
https://www.sheshbabu.com/posts/killing-long-running-queries-in-postgres/   Killing long running queries in Postgres

To find all the queries that are currently running:
```sql
SELECT
    pid,
    AGE(NOW(), query_start),
    query
FROM pg_stat_activity
WHERE query_start IS NOT NULL
ORDER BY age DESC
```
The above will list all the running queries with its pid, age and query,  
where age is how long the query has been running.

To cancel a specific query, pass its pid to pg_cancel_backend:

SELECT pg_cancel_backend(pid)

For example, if pid is 29212:

SELECT pg_cancel_backend(29212)

Note that sometimes pg_cancel_backend doesn’t work.  
In such cases, you will need to wait for the query to finish.


Killing a query:

```sql
SELECT * FROM pg_stat_activity WHERE state = 'active';
-- So you can identify the PID of the hanging query you want to terminate, run this:

SELECT pg_cancel_backend(PID);
-- This query might take a while to kill the query, so if you want to kill it the hard way, run this instead:

SELECT pg_terminate_backend(PID);
```




### SELECT DISTINCT ON (Postgres ONLY)

<https://stackoverflow.com/questions/46566602/what-does-distinct-on-expression-do>

<https://www.geekytidbits.com/postgres-distinct-on/>

<https://hakibenita.com/the-many-faces-of-distinct-in-postgre-sql> 

<https://www.yogeshchauhan.com/167/postgres/the-confusing-unique-and-useful-feature-in-postgres-distinct-on>

<https://news.ycombinator.com/item?id=22625642>

```sql
SELECT DISTINCT ON (url) url, request_duration
FROM logs
ORDER BY url, timestamp DESC
```
It is  telling PostgreSQL to “put the logs into groups unique by url (ON (url)),   
sort each of these groups by most recent (ORDER BY url, timestamp DESC)   
and then return fields for the **first record** in each of these groups (url, request_duration).
 

it is equvalent to:
```sql
WITH summary AS (
    SELECT p.id,  p.customer,   p.total, 
           ROW_NUMBER() OVER(PARTITION BY p.customer 
    ORDER BY p.total DESC) AS rank
    FROM PURCHASES p
)
SELECT * FROM summary WHERE rank = 1
```


```sql 
select distinct on (s.device_id) s.time, d.group_name, s.value 
from sensor_values s 
JOIN device_info d ON s.device_id=d.device_id 
ORDER BY s.device_id, time DESC;
```

### FETCH FIRST several ROWS WITH TIES
```sql
 SELECT * 
           FROM  t_test 
           ORDER BY id 
           FETCH FIRST 3 ROWS WITH TIES;

select *  from employees
order by salary desc
fetch first 1 rows with ties;

-- it is the same as: 
select *  from employees
where salary = (select max(salary) from employees);
```

### Working with comma-separated values

The content of  column A is the comma-separated numbers.
Write SQL which returns how many numbers in this column are greater then 7. 

```sql
SELECT SUM(t.num_count) AS total_numbers_gt_7
FROM (
  SELECT id, 
         array_position(array_remove(string_to_array(A, ','), NULL), x) AS idx,
         x AS num,
         CASE WHEN x > 7 THEN 1 ELSE 0 END AS num_count
  FROM T, unnest(string_to_array(A, ',')) AS x
) AS t
WHERE t.num_count = 1;


SELECT COUNT(*) AS count_greater_than_7
FROM (
    SELECT unnest(string_to_array(A, ','))::int AS number
    FROM T
) AS subquery
WHERE number > 7;

SELECT id, 
       COUNT(CASE WHEN number > 7 THEN 1 END) AS count_greater_than_7
FROM (
    SELECT id, unnest(string_to_array(A, ','))::int AS number
    FROM T
) AS subquery
GROUP BY id;
-------------------------------------------------
SELECT id, 
       COALESCE(COUNT(CASE WHEN number > 7 THEN 1 END), 0) AS count_greater_than_7
FROM (
    SELECT id, 
           CASE 
               WHEN A = '' THEN NULL
               ELSE unnest(string_to_array(A, ','))::int 
           END AS number
    FROM T
) AS subquery
GROUP BY id;

Error [0A000]: ERROR: set-returning functions are not allowed in CASE
  Hint: You might be able to move the set-returning function into a LATERAL FROM item.


SELECT t.id, 
       COUNT(CASE WHEN number > 7 THEN 1 END) AS count_greater_than_7
FROM T
LEFT JOIN LATERAL (
    SELECT unnest(string_to_array(t.A, ','))::int AS number
) AS subquery ON true
GROUP BY t.id;

```

### DELETING IN BATCHES

https://www.geekytidbits.com/batch-deletes-in-postgres/
```sql
DELETE FROM my_table
WHERE id IN (
  SELECT id
  FROM my_table
  WHERE created_at < now() - interval '30 days'
  -- Delete only 1000 rows at a time:
  LIMIT 1000
);
```
### SELECT FROM VALUES
```sql
select * from (values \
('S21', 'SM-G991N'), \
('S21', 'SM-G996N'), \
('S24', 'SM-S9260') \
)as t(device, dut_model))
```

### Python + Postgres
<https://www.psycopg.org/docs/extras.html>  Python Driver  
<https://khashtamov.com/en/postgresql-with-python-and-psycopg2/>  
<https://techbeamers.com/python-connect-postgresql/>  

https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries

https://python.plainenglish.io/demystifying-database-interactions-with-psycopg3-a-practical-guide-54f60d268211

### Insert one record at the time:
```sql
import psycopg2
df = pd.read_csv('dataframe.csv')

conn = psycopg2.connect(database = "postgres",
                        user = "postgres",
                        password = "12345",
                        host = "127.0.0.1",
                        port = "5432")

cur = conn.cursor()

for i in range(0 ,len(df)):
    values = (df['date'][i], df['open'][i], df['high'][i], df['low'][i], df['close'][i])
    cur.execute("INSERT INTO T (date, open, high, low, close) VALUES (%s, %s, %s, %s, %s)",
                values)

conn.commit()
print("Records created successfully")
conn.close()
```

#### Insert many records using cur.execute() in the loop
```python
data = [('Babita', 'Bihar'), ('Anushka', 'Hyderabad'), 
        ('Anamika', 'Banglore'), ('Sanaya', 'Pune'),
        ('Radha', 'Chandigarh')]

for d in data:
    cursor.execute("INSERT into employee(name, state) VALUES (%s, %s)", d)
```
#### Insert many records at once using cur.executemany()
```python
def insert_many(some list):
    sql = "INSERT INTO vendors(vendor_name) VALUES(%s)"
    conn = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.executemany(sql,vendor_list)
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# test:
    insert_many([
        ('AKM Semiconductor Inc.',),
        ('Asahi Glass Co Ltd.',),
        ('Daikin Industries Ltd.',),
        ('Dynacast International Inc.',),
        ('Foster Electric Co. Ltd.',),
        ('Murata Manufacturing Co. Ltd.',)
    ])
```

### Postgres Generate Series

```sql
SELECT * FROM generate_series(1, 5);
SELECT * from generate_series(0,10,2);
SELECT * from generate_series(1,10) a, generate_series(1,2) b;

-- dates
SELECT * from generate_series('2021-01-01','2021-01-02', INTERVAL '1 hour');
SELECT * from generate_series('2021-01-01','2021-01-02', INTERVAL '1 hour 25 minutes');

---
insert into order_data
select date_trunc('day', dd), random() * 50000
from generate_series('2015-01-01'::date, '2025-01-01'::date, '1 minute') dd;


SELECT time, device_id, random()*100 as cpu_usage 
FROM generate_series(
	  now() - INTERVAL '6 months',
    now(),
    INTERVAL '1 hour'
   ) as time, 
generate_series(1,4) device_id;

SELECT time, device_id, random()*100 as cpu_usage 
FROM generate_series(
	  '2021-08-01 00:00:00' - INTERVAL '6 months',
    '2021-08-01 00:00:00',
    INTERVAL '1 hour'
  ) as time, 
generate_series(1,4) device_id;

SELECT time, device_id, random()*100 as cpu_usage 
FROM generate_series(
	'2020-12-15 00:00:00',
    '2020-12-15 00:00:00' + INTERVAL '2 months',
    INTERVAL '1 hour'
  ) as time, 
generate_series(1,4) device_id;

--- CTE
WITH range_values AS (
  SELECT date_trunc('week', min(created_at)) as minval,
         date_trunc('week', max(created_at)) as maxval
  FROM users),

week_range AS (
  SELECT generate_series(minval, maxval, '1 week'::interval) as week
  FROM range_values
),

weekly_counts AS (
  SELECT date_trunc('week', created_at) as week,  count(*) as ct
  FROM users
  GROUP BY 1
)

SELECT week_range.week, weekly_counts.ct
FROM week_range
LEFT OUTER JOIN weekly_counts on week_range.week = weekly_counts.week;


SELECT G.n AS ID,
  G.n%100 AS SessionId,
  G.n%1000 AS Val,
  ((G.n/1000)%2)::boolean AS IsValidated
FROM generate_series(1,1000000) G(n);

CREATE TABLE tmp_sessions AS
SELECT G.n AS SessionId
FROM generate_series(30,49) G(n);
```

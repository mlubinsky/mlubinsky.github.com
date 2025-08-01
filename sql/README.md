https://www.db-fiddle.com/

https://sqlize.online/

https://blog.devgenius.io/master-sql-with-multiple-ctes-window-functions-frames-and-subquery-in-one-leetcode-challenge-882fd803d7e7

https://habr.com/ru/articles/913682/ локальный SQL-редактор в браузере на DuckDB и WASM

### FIRST_VALUE()  LAST_VALUE()
https://medium.com/towards-data-engineering/sql-first-and-last-value-functions-6e4519937965

```
There is Postgres table T with  3 columns :  user , timestamp and  status. 
The value in column  'status' can be 'YES' or  'NO'.   
Please write SQL which  returns for every user the number of consecutive  records
and the number of consecutive  groups
(by timestamp column) where status='NO'
```

```sql
WITH ranked AS (
  SELECT
    user,
    timestamp,
    status,
    -- Assign a group ID where consecutive statuses differ
    ROW_NUMBER() OVER (PARTITION BY user ORDER BY timestamp) -
    ROW_NUMBER() OVER (PARTITION BY user, status ORDER BY timestamp) AS grp
  FROM T
),
no_rows AS (
  SELECT *
  FROM ranked
  WHERE status = 'NO'
),
no_groups AS (
  SELECT user, grp
  FROM no_rows
  GROUP BY user, grp
)
SELECT
  user,
  COUNT(*) AS total_no_rows,
  COUNT(DISTINCT grp) AS total_no_groups
FROM no_rows
GROUP BY user
ORDER BY user;
```

```sql
WITH UserStatus AS (
    SELECT
        user,
        timestamp,
        status,
        LAG(status, 1, '') OVER (PARTITION BY user ORDER BY timestamp) AS prev_status
    FROM  T
),
ConsecutiveNoGroups AS (
    SELECT
        user,
        timestamp,
        status,
        CASE
            WHEN status = 'NO' AND prev_status <> 'NO' THEN ROW_NUMBER() OVER (PARTITION BY user ORDER BY timestamp)
            ELSE NULL
        END AS group_start_id,
        CASE
            WHEN status = 'NO' THEN ROW_NUMBER() OVER (PARTITION BY user, (CASE WHEN status = 'NO' AND prev_status <> 'NO' THEN 1 ELSE 0 END) ORDER BY timestamp)
            ELSE NULL
        END AS row_in_group
    FROM UserStatus
),
FilledGroups AS (
    SELECT
        user,
        timestamp,
        status,
        COALESCE(group_start_id, LAG(group_start_id IGNORE NULLS) OVER (PARTITION BY user ORDER BY timestamp)) AS filled_group_id
    FROM ConsecutiveNoGroups
WHERE status = 'NO'
)
SELECT
    user,
    COUNT(*) AS total_consecutive_no_records,
    COUNT(DISTINCT filled_group_id) AS number_of_consecutive_no_groups
FROM  FilledGroups
GROUP BY user
ORDER BY user;
```

```sql
WITH NoRecords AS (
    -- Select only records where status = 'NO'
    SELECT
        "user",
        "timestamp",
        "status"
    FROM T
    WHERE status = 'NO'
),
GroupAssignment AS (
    -- Assign group identifiers for consecutive 'NO' records
    SELECT
        "user",
        "timestamp",
        SUM(CASE
            WHEN LAG("timestamp") OVER (PARTITION BY "user" ORDER BY "timestamp") IS NULL
                 OR LAG("status") OVER (PARTITION BY "user" ORDER BY "timestamp") <> 'NO'
            THEN 1
            ELSE 0
        END) OVER (PARTITION BY "user" ORDER BY "timestamp") AS group_id
    FROM (
        -- Include all records to check transitions from 'YES' to 'NO'
        SELECT "user", "timestamp", "status"
        FROM T
    ) all_records
    WHERE status = 'NO'
)
SELECT
    "user",
    COUNT(*) AS consecutive_records,
    COUNT(DISTINCT group_id) AS consecutive_groups
FROM GroupAssignment
GROUP BY "user"
ORDER BY "user";
```

### LATERAL JOIN 

https://www.geeksforgeeks.org/lateral-keyword-in-sql/

https://medium.com/@goldengrisha/a-deep-dive-into-sql-lateral-join-7b09fcb3b745

https://www.crunchydata.com/developers/playground/lateral-join

https://www.edgedb.com/  Юрием Селивановым, CEO и co-founder Edgedb,

Regular expressions in SQL
https://habr.com/ru/companies/otus/articles/851942/

https://coffingdw.com/analytic-and-window-functions-for-all-systems-over-100-blogs/  
https://coffingdw.com/date-functions-date-formats-and-timestamp-formats-for-all-databases-45-blogs-in-one/

### NULL 
```
SELECT * FROM users WHERE title != 'manager' 
```
не вернёт строки, в которых title равен NULL, потому что NULL != 'manager' — это NULL.


### ACID

https://habr.com/ru/articles/843794/   
https://habr.com/ru/articles/860982/
```
1. Атомарность (atomicity). Транзакция фиксируется либо полностью, либо ни одна ее часть не фиксируется

2. Согласованность (consistency). Транзакция должна переводить базу данных из одного согласованного состояния в другое.

3. Изолированность (isolation). Во время выполнения транзакции другие транзакции не должны оказывать влияние на нее.
То есть они не должны изменять данные внутри транзакции.

4. Долговечность (durability).
После успешной фиксации, изменения сделанные транзакцией сохраняются в базе данных и остаются там даже если после этого произойдет сбой.

Этот набор свойств еще обозначают аббревиатурой ACID.

```


### The SQL isolation levels 

https://www.thenile.dev/blog/transaction-isolation-postgres

```
1. Serializable (most strict, expensive):
-------------------------------------------
A serializable execution produces the same effect as some serial execution of those transactions.
A serial execution is one in which each transaction executes to completion before the next transaction begins.
One note about Serializable level is that it is often implemented as “snapshot isolation” (e.g. Oracle)
 due to differences in interpretation and “snapshot isolation” is not represented in the SQL standard.

2. Repeatable reads:
----------------------
Uncommitted reads in the current transaction are visible to the current transaction
 but changes made by other transactions (such as newly inserted rows) won’t be visible.

3. Read committed:
-------------------------
 Uncommitted reads are not visible to the transactions. Only committed writes are visible but the phantom reads may happen.
If another transaction inserts and commits new rows, the current transaction can see them when querying.

4. Read uncommitted (least strict, cheap):
--------------------------------------------
Dirty reads are allowed, transactions can see not-yet-committed changes made by other transactions.
In practice, this level could be useful to return approximate aggregates, such as COUNT(*) queries on a table.
```
Why not SQL?
https://habr.com/ru/companies/lsfusion/articles/463095/

https://habr.com/ru/companies/cedrusdata/articles/843882/

### DB Diagrams 
https://dbdiagram.io/home . DB schema diagrams

https://news.ycombinator.com/item?id=43808803

https://habr.com/ru/post/456116/  yEd Graph Editor построить красивую схему базы данных

 https://github.com/chartdb/chartdb
 
https://schemaspy.org/ 

### Window functions

https://habr.com/ru/articles/846712/

https://www.crunchydata.com/blog/window-functions-for-data-analysis-with-postgres

### find the whole data for the row with some max value in a column per some group identifier. 
```sql
SELECT a.id, a.rev, a.contents
FROM YourTable a
INNER JOIN (
    SELECT id, MAX(rev) rev
    FROM YourTable
    GROUP BY id
) b ON a.id = b.id AND a.rev = b.rev

SELECT a.*
FROM YourTable a
LEFT OUTER JOIN YourTable b
    ON a.id = b.id AND a.rev < b.rev
WHERE b.id IS NULL;
```

### SELECT Top N Rows For Each Group

```sql
WITH CTE AS (
  SELECT
    <group_column>,
    <value_column>,
    ROW_NUMBER() OVER (PARTITION BY <group_column> ORDER BY <value_column> DESC) AS row_num
  FROM
    <Table>
)
SELECT * FROM CTE WHERE row_num <= N;

-- Retrieve top 2 salespersons per region
WITH  CTE  AS (
  SELECT *, ROW_NUMBER()  OVER (PARTITION BY  Region  ORDER BY  Revenue DESC)  AS  row_num
  FROM
    Sales
)
SELECT * FROM CTE WHERE row_num <= 2;
```

### GROUP BY vs Window Function OVER (Partition By ..)

https://stackoverflow.com/questions/2404565/what-is-the-difference-between-partition-by-and-group-by


https://www.linkedin.com/pulse/select-statement-snowflake-databricks-vincent-rainardi-5ynle/ 

### django-sql-explorer
https://github.com/explorerhq/django-sql-explorer
https://news.ycombinator.com/item?id=40857589

https://habr.com/ru/articles/825970/

### Database diagrams

https://wisser.github.io/Jailer/

https://news.ycombinator.com/item?id=36243926


### AsOf Join

https://duckdb.org/docs/guides/sql_features/asof_join.html

### Query optimizer

https://howqueryengineswork.com/

https://vldb.org/pvldb/vol14/p2383-fent.pdf A Practical Approach to Groupjoin and Nested Aggregates

https://xuanwo.io/2024/02-what-i-talk-about-when-i-talk-about-query-optimizer-part-1/

https://news.ycombinator.com/item?id=39176797


### 5 Challenging SQL Interview questions you must try before your interviews

Difficulty level - FAANG

1) Users By Average Session Time (Facebook ,Medium)

https://lnkd.in/gKneV29k

2) Videos Removed on Latest Date ( Google , Hard)

https://lnkd.in/gG3b4hXi

3) Employed at Google ( Company — linkedln ,Medium)

https://lnkd.in/g6jAGyRb

4) Recommendation System (Meta/Facebook, Medium)

https://lnkd.in/gPEfkEJx

5) Rank Variance Per Country (Facebook,Hard)

https://lnkd.in/gv753AiD



1. Amazon SQL Interview Question for Data Analyst Position [2-3 Year Of Experience ] | Data Analytics
https://lnkd.in/g2RzsKdq

2. Airbnb SQL Interview Question | Convert Comma Separated Values into Rows | Data Analytics
https://lnkd.in/gpMbU-dF

3. Adobe Interesting SQL Interview Question | Solving Using 2 Approaches | Data Analytics
https://lnkd.in/g_-_9ymd

4. Spotify SQL Interview Problem | Top 5 Artists | Aggregation and  Functions in SQL
https://lnkd.in/gtfaugd3

5. L&T SQL Interview Problem | Print Highest and Lowest Salary Employees in Each Department
https://lnkd.in/ggY82FJW

6. Ameriprise LLC Company SQL Interview Problem | Data Analytics
https://lnkd.in/gS_Yqq6c

7. Tiger Analytics SQL Interview Question for Data Engineering Position
https://lnkd.in/ghjE_CXp

8. PWC SQL Interview Question | BIG 4 |Normal vs Mentos Life 😎
https://lnkd.in/g9SkkX9x

9. Honeywell SQL Interview Question | Print Movie Stars (⭐ ⭐ ⭐ ⭐⭐) For best movie in each Genre
https://lnkd.in/gSDgB9Me

10. Angel One Easy-Peasy SQL Interview Question for a Data Science Position
https://lnkd.in/geaU3we7

11. Practice FAANG SQL Interview Questions For Free | Ace The SQL Interview | Data Analytics
https://lnkd.in/g4AFgen3

12. Accenture SQL Interview Question | Database Case Sensitivity vs Insensitivity
https://lnkd.in/gR6F_8zf

13. American Express SQL Interview Question and Solution | Page Recommendation
https://lnkd.in/g_sMN26m

14. Fractal Analytics SQL Interview Question (Game of Thrones Database) | SQL for Data Engineer
https://lnkd.in/gGcsBms5

15. Netflix Data Cleaning and Analysis Project | End to End Data Engineering Project (SQL + Python)
https://lnkd.in/gS8mT7Fn

16. Swiggy Data Analyst SQL Interview Question and Answer
https://lnkd.in/gSyhmmhd

17. Cracked Myntra as Data Analyst with 1 Year Experience
https://lnkd.in/gekpAit8

18. PWC SQL Interview Question for a Data Analyst Position | SQL For Analytics
https://lnkd.in/gyD5Pjny

19. PayPal Data Engineer SQL Interview Question (and a secret time saving trick)
https://lnkd.in/gAJ_Ug79

20. Adobe Interesting SQL Interview Question | Solving Using 2 Approaches | Data Analytics
https://lnkd.in/gEEAfi8j

21. Walmart Labs SQL Interview Question for Senior Data Analyst Position | Data Analytics
https://lnkd.in/gRBPb-ms

22. PayPal SQL Interview Problem (Level Hard) | Advanced SQL Problem
https://lnkd.in/gGZaYt6N

### Time series SQL

https://questdb.io/blog/olap-vs-time-series-databases-the-sql-perspective/

### Upsert

https://antonz.org/sql-upsert/

https://news.ycombinator.com/item?id=37641628

#### Max salary per department

https://habr.com/ru/articles/828728/
```sql
CREATE TABLE departments (
   department_id integer PRIMARY KEY,
   name text NOT NULL
);
CREATE TABLE employees (
   employee_id integer PRIMARY KEY,
   department_id integer NOT NULL REFERENCES departments(department_id),
   name text NOT NULL,
   salary money NOT NULL
);

SELECT name AS employee, salary 
FROM (
  SELECT department_id, max(salary) AS salary 
  FROM employees 
  GROUP BY department_id
) AS m 
JOIN employees AS e USING (department_id, salary);

SELECT name AS employee, salary 
FROM (
  SELECT name, salary, max(salary) OVER (PARTITION BY department_id) AS ms 
  FROM employees
) AS e 
WHERE salary=ms;

SELECT name AS employee, salary 
FROM (
  SELECT name, salary, rank() OVER (PARTITION BY department_id ORDER BY salary DESC)
  AS rnk FROM employees e
) AS e 
WHERE rnk=1;
```

### Filtering with NOT EXISTS and NOT IN
```sql
SELECT s.name FROM students s
WHERE NOT EXISTS (
    SELECT 1
    FROM courses c
    WHERE c.student_id = s.student_id

SELECT name FROM students
WHERE student_id NOT IN (
    SELECT student_id
    FROM courses
);
```

###   Interview questions



https://habr.com/ru/companies/otus/articles/811169/

https://blog.devgenius.io/sql-practice-questions-1-800ed65d99b2

https://blog.devgenius.io/sql-practice-questions-5-456cfb41757a

https://medium.com/towards-data-engineering/most-asked-complex-sql-queries-in-data-engineering-interviews-9fde381d23f8

###  Древовидные структуры в SQL
https://www.slideshare.net/slideshow/models-for-hierarchical-data/4179181#18

https://www.databasestar.com/hierarchical-data-sql/

https://habr.com/ru/articles/812601/ Древовидные структуры в SQL

https://medium.com/@mtrentz/answer-business-questions-effectively-with-these-sql-tricks-b20555db48c8

https://medium.com/illumination/this-is-exactly-how-i-use-sql-at-work-as-a-data-analyst-141f0d178d7c

Задача двумерной упаковки интервалов
https://habr.com/ru/companies/otus/articles/801487/

https://blog.devops.dev/top-10-advanced-sql-queries-dd5717b7e902

https://blog.stackademic.com/9-advanced-sql-queries-for-data-mastery-ce37ae78837e

https://habr.com/ru/articles/789420/

https://habr.com/ru/companies/tensor/articles/776834/

Let generate 1 mln random records for 1 year:

```sql
CREATE TABLE fact4agg AS
  SELECT
    now()::date - (random() * 365)::integer dt      -- дата "факта"
  , chr(ascii('a') + (random() * 26)::integer) code -- код агрегации
  FROM
    generate_series(1, 1e6);

CREATE INDEX ON fact4agg(dt);

WITH params(dtb, dte) AS (
  VALUES(now()::date - 30, now()::date)
)
SELECT
  dt::date
FROM
  params, generate_series(dtb, dte, '1 day') dt;


WITH params(dtb, dte) AS (
  VALUES(now()::date - 30, now()::date)
)
SELECT
	dt
,	code
,	count(*) qty
FROM
	params
,	fact4agg
WHERE
	dt BETWEEN dtb AND dte
GROUP BY
	1, 2;



DROP INDEX fact4agg_dt_idx;

CREATE INDEX ON fact4agg(dt)   INCLUDE(code);
```




https://www.youtube.com/watch?v=NKXH7o8m2x4

https://habr.com/ru/articles/588859/

### SELECT ROW IN EACH GROUP BY GROUP
https://stackoverflow.com/questions/3800551/select-first-row-in-each-group-by-group/7630564#7630564

### Qualify
https://medium.com/snowflake/how-qualify-works-with-in-depth-explanation-and-examples-bbde9fc742db

```
The QUALIFY clause has been introduced in a SELECT SQL query by Teradata years ago.
It’s been followed over the years by Oracle, Snowflake, Google BigQuery, Databricks and other relational database systems.
 It is not part of the SQL standard.

What Problem QUALIFY Solved
In a SQL statement, you cannot filter in the WHERE clause by a window function (e.g. a statistical function call, usually followed by an OVER clause).
 This is because any window function call is internally evaluated after the WHERE clause evaluation.

Try to execute any of the following queries in your Snowflake web UI, and you will get the
“Window function [ROW_NUMBER() OVER (ORDER BY FRUITS.NAME ASC NULLS LAST)] appears outside of SELECT, QUALIFY, and ORDER BY clauses” compilation error:
```
```sql
select name
from (values ('apples'), ('oranges'), ('nuts')) as fruits(name)
where row_number() over (order by name) >= 2
order by name;

select name, row_number() over (order by name) as rn
from (values ('apples'), ('oranges'), ('nuts')) as fruits(name)
where rn >= 2
order by name;
```
The typical fix was to separate a subquery, in which all window functions are evaluated.
The outer query was now applying the WHERE filter on fields already evaluated before:
```sql
with cte as (
  select name, row_number() over (order by name) as rn
  from (values ('apples'), ('oranges'), ('nuts')) as fruits(name)
  order by name)
select *
from cte
where rn >= 2;
```
QUALIFY is simply a convenient clause that allows you to filter on window functions in the same query,
but after the window function values have been calculated. All these correct versions return “nuts” and “oranges”, in this order.
```sql
select name, row_number() over (order by name) as rn
from (values ('apples'), ('oranges'), ('nuts')) as fruits(name)
qualify rn >= 2
order by name;

select name
from (values ('apples'), ('oranges'), ('nuts')) as fruits(name)
qualify row_number() over (order by name) >= 2
order by name;
```
The Order of Execution in a SQL Query
The order of the SQL clauses in a SELECT query is not the same as the internal order of execution and evaluation of these clauses.
The projection specified in the SELECT clause alone is evaluated by the end.

From the picture below, you can see that window functions (the OVER clauses) are evaluated well after the WHERE clause.
 So you cannot use the WHERE clause with window functions. The new QUALIFY clause acts like WHERE,
but it is executed after the window functions have been evaluated:
 

### Duplicates in table: 
https://blog.devgenius.io/duplicates-in-sql-e7a146d0131

```sql
SELECT col1, col2
FROM table_name
WHERE (col1, col2) IN (
    SELECT col1, col2 FROM table_name
    GROUP BY col1, col2 
    HAVING COUNT(*) > 1
    )
```
If the set of column values is unique in the table then the partition with that column set will have single rows. 
Conversely, partitions with more than one row denote the presence of duplicate values. We use ROW_NUMBER() to assign a sequential integer to each row within the partition of a result set. 
A sequence (appearance/occurrence) greater than one means that the value is appearing more than one time.
```sql
WITH dedup AS (
 SELECT col1, col2,
  ROW_NUMBER() OVER (PARTITION BY col1, col2 ORDER BY col3 ASC) AS occurrence
 FROM table_name
)
SELECT col1, col2
FROM dedup
WHERE occurrence > 1
```

### Find duplicate rows in a database
```sql
SELECT * FROM emp a WHERE rowid = (SELECT MAX(rowid) FROM EMP b WHERE a.empno=b.empno)
```
### Delete duplicates
```sql
DELETE FROM emp a WHERE rowid != (SELECT MAX(rowid) FROM emp b WHERE a.empno=b.empno);
```

### Delete duplicate records
```sql
DELETE    FROM T 
WHERE  ctid NOT IN
        (
        SELECT  MAX(ctid) 
        FROM  T 
        GROUP BY  T.*
        )
```


https://sqlfordevs.com/ebook



### RANK() vs DENSE_RANK()

RANK numbers are skipped so there may be a gap in rankings, and may not be unique. 

DENSE_RANK numbers are not skipped so there will not be a gap in rankings, and may not be unique

RANK gives you the ranking within your ordered partition. Ties are assigned the same rank, with the next ranking(s) skipped. So, if you have 3 items at rank 2, the next rank listed would be ranked 5.

DENSE_RANK again gives you the ranking within your ordered partition, but the ranks are consecutive. No ranks are skipped if there are ranks with multiple items.

#### Pivot

https://antonz.org/sqlite-pivot-table/

```sql
select
  product,
  sum(case when year = 2020 then income end) as "2020",
  sum(case when year = 2021 then income end) as "2021",
  sum(case when year = 2022 then income end) as "2022",
  sum(case when year = 2023 then income end) as "2023"
from sales
group by product
order by product;
```


### Window functions

https://www.crunchydata.com/blog/window-functions-for-data-analysis-with-postgres

https://towardsdatascience.com/understand-sql-window-functions-once-and-for-all-4447824c1cb4

https://habr.com/ru/post/664000/

https://www.youtube.com/watch?v=QenwDm5oWdU

RANK, DENSE_RANK, NTILE ROW_NUMBER, CUME_DIST

FIRST_VALUE, LAST_VALUE, LAG LEAD NTH_VALUE


### UNNEST - convert array to rows
```sql
create table test(
    p_name text[],
    p_id varchar(14),
    p_email varchar(50)
 );

INSERT INTO test (p_name, p_id, p_email)
VALUES (ARRAY['Peter Mont', 'Derak Powel'], 'PEMO-7894-OMEP', 'pmont1699@xyzmail.kom');


INSERT INTO test (p_name, p_id, p_email)
VALUES (ARRAY['Devid Hogg', 'Lusi Nail', 'Ben Knot'], 'DELU-8529-HONA', 'devlus2021@xyzmail.kom');
 

p_name                               |p_id          |p_email               |
-------------------------------------+--------------+----------------------+
{"Peter Mont","Derak Powel"}         |PEMO-7894-OMEP|pmont1699@xyzmail.kom |
{"Devid Hogg","Lusi Nail","Ben Knot"}|DELU-8529-HONA|devlus2021@xyzmail.kom|
 
 

SELECT p_id, unnest(p_name)
FROM test;
```

### Convert column to comma-separated list
```sql
  SELECT yt.userid,
         GROUP_CONCAT(yt.col ORDER BY yt.col SEPARATOR ' ') AS combined
    FROM YOUR_TABLE yt
GROUP BY yt.userid
```
 it can achieved using one of the spark function.. 
```
 concat_ws(', ',collect_set( col_name ))  
```
Another way:
```sql
select user, array_join(collect_list(department), ', ')
from tablenamehere
group by user
```
### Key-Value stores

https://notes.eatonphil.com/whats-the-big-deal-about-key-value-databases.html

https://news.ycombinator.com/item?id=32566851


### DBT
https://habr.com/ru/post/670062/

https://www.youtube.com/watch?v=9RCfz3ef19o

Database browser:

https://wisser.github.io/Jailer/

### Anti-join

https://towardsdatascience.com/why-is-nobody-talking-about-sql-anti-joins-f970a5f6cb54

An anti-join is when you would like to keep all of the records in the original table except those records that match the other table.
```sql
select * 
from admissions a
left join physicians p
  on a.attending_physician_id = p.physician_id
where TRUE
  and p.physician_id is null
```

https://www.postgresqltutorial.com/postgresql-except/ ( == MINUS in Oracele)
EXCEPT operator is, basically it takes a table and finds all records in the first table that aren’t in the second table. This is exactly the same purpose as an anti-join, 
but they are used in different scenarios:

Use the EXCEPT when you only need the columns you are comparing between the two tables
Use the anti-join when you need more columns than what you would compare when using the EXCEPT operator



https://itnext.io/filtering-by-dynamic-attributes-90ada3504361  Filtering by dynamic attributes

https://habr.com/ru/company/tensor/blog/667998/  SQL ANY / ALL / CASE optimization

https://habr.com/ru/company/querifylabs/blog/578842/ SQL plan

https://news.ycombinator.com/item?id=30323131  Dashboards for SQL database

https://habr.com/ru/company/tensor/blog/657895/ SQL HowTo: разные варианты работы с EAV

### ROWS BETWEEN vs RANGE BETWEEN (X PRECEDING AND Y FOLLOWING)
https://habr.com/ru/companies/otus/articles/904934/  Скользящие метрики без тормозов: SQL

Здесь каждый фрейм отбирает ровно 3 строки (текущую, предыдущую и следующую)

```sql
SELECT date,  expense,
  ROUND(
    AVG(expense) 
    OVER (
      ORDER BY date
      ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
    )
  , 2) AS moving_avg_3
FROM expenses
ORDER BY date;
```
Если же нужен временной интервал, допустим 7 дней, используют RANGE:
```sql
SELECT
  date,
  SUM(amount) 
    OVER (
      ORDER BY date 
      RANGE BETWEEN INTERVAL '6 days' PRECEDING AND CURRENT ROW
    ) AS sum_7d
FROM transactions;
```


### Moving Average
```sql
SELECT employee_id, salary,
       SUM(salary) OVER (ORDER BY employee_id ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING) AS salary_sum
FROM employees;
```

https://habr.com/ru/post/588859/  averaging and smoothing for noise reduction
```sql
SELECT
    Date
  , dailyConversions
  , AVG(dailyConversions) OVER (ORDER BY Date ROWS 10 PRECEDING) AS
    10_dayMovingAverage
FROM
    conversions
```
https://hakibenita.com/sql-for-data-analysis

### Jinja

https://towardsdatascience.com/jinja-sql-%EF%B8%8F-7e4dff8d8778 Jinja with SQL

https://medium.com/towards-data-science/advanced-sql-templates-in-python-with-jinjasql-b996eadd761d 

https://towardsdatascience.com/a-simple-approach-to-templated-sql-queries-in-python-adc4f0dc511

https://winand.at/sql-slides-for-developers

https://news.ycombinator.com/item?id=28425379  modern databases

https://github.com/dinedal/textql  SQL for CSV and TSV

https://habr.com/ru/company/otus/blog/541882/

### GROUPING SET
```sql
SELECT department_id, job_id, SUM(salary) AS total_salary
FROM employees
GROUP BY GROUPING SETS ((department_id), (department_id, job_id));
```
https://hakibenita.com/sql-for-data-analysis  ROLLUP, CUBE GROUPING_SET

https://hakibenita.com/sql-dos-and-donts Faux predicate

https://blog.jooq.org/10-cool-sql-optimisations-that-do-not-depend-on-the-cost-model/



## Running total
<https://habr.com/ru/post/474458/> . Нарастающий (накопительный) итог 

https://habr.com/ru/post/597963/ 

https://blog.jooq.org/2014/04/29/nosql-no-sql-how-to-calculate-running-totals/

https://betterprogramming.pub/4-ways-to-calculate-a-running-total-with-sql-986d0019185c

<https://stackoverflow.com/questions/63609219/best-way-to-get-1st-record-per-partition-first-value-vs-row-number>

<https://medium.com/better-programming/4-ways-to-calculate-a-running-total-with-sql-986d0019185c>

```sql
SELECT id,month
 , Amount
 , SUM(Amount) OVER (ORDER BY id) as total_sum
FROM bill
```

```sql
select
    a.date,
    sum(b.sales) as cumulative_sales
from sales_table a
join sales_table b on a.date >= b.date
group by a.date
order by a.date


SELECT city, month,
    SUM(amount) OVER (
        PARTITION BY city
        ORDER BY month
        RANGE UNBOUNDED PRECEDING
    ) as total_sale
FROM Sales;
```


Runnig total using window function:

https://blog.devgenius.io/sql-window-function-d39858e52784

```sql
select date,
    sum(sales) over (order by date rows unbounded preceding) as cumulative_sales
from sales_table;
```



```sql
SELECT
      t1.day
      ,t1.driver_id
      ,(
        Select sum(profit) from f_daily_rides t2 
        where t1.day >= t2.day and t1.driver_id = t2.driver_id
       )
   FROM f_daily_rides t1
```   

### LAG and LEAD
 
 ```
LAG is a window function that lets you access the value from a column in a row that lags (precedes) the current row. 
Such function receives three parameters: the first one is the column name you want to access (you may use a built-in function instead of a column). 
The second parameter determines an offset from the current row (it is an optional parameter and its default value is 1). 
The third parameter (optional with default value NULL) is the value to be returned if offset goes beyond the bound of the table.
LAG is used together with OVER, where the Partition By and Order By clauses may be used.


```
https://habr.com/ru/post/545870/

 the monthly percent change in costs
```sql
with monthly_costs as (
    SELECT
        date
      , monthlycosts
      , LEAD(monthlycosts) OVER (ORDER BY date) as
        previousCosts
    FROM
        costs
)
SELECT
    date
  , (monthlycosts - previousCosts) / previousCosts * 100 AS
    costPercentChange
FROM monthly_costs
```
Given: weather table  contains daily temperature   in different cities:
(date, city, temperature)
How can you create a table that also contains the temperature difference between the current day and the next day? For the first row, the difference column should contain the value 1.2.

```sql
WITH cte AS(
   SELECT
      W1.*, 
      LEAD(W2.temperature, 1) OVER(PARTITION BY W2.city ORDER BY 
      W2.date) AS temp_next                                                   
   FROM weather W1                                                                                                                                                   
   LEFT JOIN weather W2                                                                                                                                              
   ON W1.date = W2.date and W1.city = W2.city
)
  SELECT 
   *, 
   COALESCE((temp_next - temperature), 0) AS temp_diff 
FROM cte;
```

## LEAD, LAG, FIRST_GAP

find all numbers that appear at least three times consecutively.
 
 
| id | num |
|----|-----|
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
```sql
WITH cte as (
    SELECT num, 
        LEAD(num, 1) OVER() AS next_num, 
        LAG(num) OVER (ORDER BY id) AS prev_num
    FROM `Logs`
)
SELECT DISTINCT num as ConsecutiveNums 
FROM cte WHERE num=next_num and num=prev_num;
```

http://databasetips.net/2019/02/12/lead-and-lag-accessing-multiple-rows-without-self-join/

http://databasetips.net/2019/09/05/sql-3-ways-to-find-gaps-and-missing-values/

http://www.silota.com/docs/recipes/sql-gap-analysis-missing-values-sequence.html



###
```sql
SELECT 
  VARIANCE(amount) AS var_amount,
  VAR_POP(amount) AS var_pop_amount,
  VAR_SAMP(amount) AS var_samp_amount,
  STDDEV_SAMP(amount) as stddev_sample_amount,
  STDDEV_POP(amount) as stddev_pop_amount,
FROM bill
```

### Subtotal ROLLUP

It’s an extension of a GROUP BY clause with the ability to add subtotals and grand totals to your data.

```sql
SELECT  
  Type,
  id,
  SUM (Amount) AS total_amount
FROM bill
GROUP BY Type,id WITH ROLLUP
```


### Calculation AVG:
 - missing value
 - INT to float
```sql
with T as ( 
select 1 as i, 5 as v 
union all 
select 2, NULL 
union all 
select 3, 5 
)
select avg(v) from T.   ==> 5 (ignoring NULLs!!!)
select avg(COALESCE(v,0)) from T.  ==> 3 returns rounded to integer value
select avg(COALESCE(v,0)+0.0) from T.  ==> 3.333
```



### UNION

https://www.foxhound.systems/blog/sql-performance-with-union/



## First_ROW 

<https://stackoverflow.com/questions/63609219/best-way-to-get-1st-record-per-partition-first-value-vs-row-number>

```sql

SELECT   content_id,   store, 
FIRST_VALUE(kids_directed)   OVER( PARTITION BY content_id,   store   ORDER BY date_key desc rows unbounded preceding) 
FROM
(
SELECT 'c1' as content_id, 's1' as store, True as kids_directed, '2020-01-01' as date_key
UNION ALL
SELECT 'c1' as content_id, 's2' as store, False as kids_directed, '2020-01-02' as date_key
UNION ALL
SELECT 'c2' as content_id, 's1' as store, True as kids_directed, '2020-01-02' as date_key
UNION ALL
SELECT 'c2' as content_id, 's1' as store, False as kids_directed, '2020-01-02' as date_key
)

 
content_id	store	first_value
1	c1	s1	false
2	c1	s2	false
3	c2	s1	true
4	c2	s1	true


select  * from (
SELECT content_id, store, kids_directed,  ROW_NUMBER() OVER( PARTITION BY content_id,   store   ORDER BY date_key desc) as row_num
FROM
(
SELECT 'c1' as content_id, 's1' as store, True as kids_directed, '2020-01-01' as date_key
UNION ALL
SELECT 'c1' as content_id, 's2' as store, False as kids_directed, '2020-01-02' as date_key
UNION ALL
SELECT 'c2' as content_id, 's1' as store, True as kids_directed, '2020-01-02' as date_key
UNION ALL
SELECT 'c2' as content_id, 's1' as store, False as kids_directed, '2020-01-02' as date_key
)
) where row_num=1

Answer
content_id	store	kids_directed	row_num
 c1	       s2	        false     	1
 c1	       s1	        true	      1
 c2	       s1	        false	     1
```

# TablePlus DBeaver

<https://news.ycombinator.com/item?id=22908224>

## Datasette

<https://datasette.readthedocs.io/en/stable/>

## SQL vs GraphQL

<https://news.ycombinator.com/item?id=22892946>



## SQL
 Medium-Hard Data   SQL Interview Questions
<https://quip.com/2gwZArKuWk7W>
<https://habr.com/ru/company/dcmiran/blog/500360/>


<https://news.ycombinator.com/item?id=23053981>

<https://www.db-fiddle.com/>

<https://research.neustar.biz/2014/05/19/writing-analytics-sql-with-common-table-expressions/> CTE for analytics

<https://habr.com/ru/company/ruvds/blog/487878/> 

<https://winand.at/newsletter/2019-12/partiql-microsoft-licenses-volcano-model>

 <https://stackoverflow.com/questions/58828417/how-to-avoid-calculating-the-same-expression-several-times-in-sql>
 
 <https://habr.com/ru/company/otus/blog/479976/> SQL tricks
 
 <https://towardsdatascience.com/python-vs-sql-comparison-for-data-pipelines-8ca727b34032>
 

 
 
 <https://towardsdatascience.com/anomaly-detection-with-sql-7700c7516d1d> Anomaly detection with SQL

 <https://blog.jooq.org/2016/04/25/10-sql-tricks-that-you-didnt-think-were-possible/>

 <https://www.interviewbit.com/sql-interview-questions/>
 
 <https://habr.com/ru/post/461567/>
 
 <https://www.programmerinterview.com/database-sql/advanced-sql-interview-questions-and-answers/>
 
<https://www.java67.com/2013/04/10-frequently-asked-sql-query-interview-questions-answers-database.html>

<https://dankleiman.com/2018/02/06/3-ways-to-level-up-your-sql-as-a-software-engineer/>

<https://news.ycombinator.com/item?id=20855441>

<http://www.helenanderson.co.nz/sql-query-tweaks/>

You can use LAG() to reference previous rows

## DISTINCT
 <https://blog.jooq.org/2019/09/09/using-distinct-on-in-non-postgresql-databases/>

##  MAX per day
```sql
CREATE VIEW max_daily_view AS
SELECT
  time,
  date_trunc('day',   time) AS day,
  date_trunc('month', time) AS month,
  maximum
FROM
  (
    SELECT time, cnt, MAX (cnt) OVER ( PARTITION BY day ) AS maximum
    FROM
      (
        SELECT time, COUNT(*) AS cnt, DATE_TRUNC('day', time) AS day
        FROM T
        GROUP BY time
      )
      AS a
  )
  AS b
WHERE cnt = maximum;
```

## LEFT JOIN
```sql
create table T1 (x int);
insert into T1 VALUES (1),(2),(3);

create table T2 (y int);
insert into T2 VALUES (1),(1),(2); 

Number of rec in dest table > N of rec in left table 
SELECT T1.*, T2.* FROM T1 LEFT JOIN T2 ON ( T1.x=T2.y )
X Y
1	1
1	1
2	2
3	NULL

```
### COUNT() vs SUM()
```sql
create table events(event_type int, time timestamp);
insert into events values(1, '2019-07-25 17:50:00');
insert into events values(1, '2019-07-25 17:50:00');
insert into events values(2, '2019-07-25 17:50:00');
insert into events values(1, '2019-07-25 18:00:00');

select event_type, time, count(*) as cnt from events group by time, event_type;

 event_type |        time            | cnt  
    2       |   2019-07-25 17:50:00  | 1
    1       |   2019-07-25 17:50:00  | 2
    1       |   2019-07-25 17:50:00  | 1
    
select event_type,  sum(cnt) as total,  count(*) from 
( select event_type, time, count(*) as cnt from events group by time, event_type order by time) A
group by event_type;

event_type | total | count
2	            1	       1
1	            3	       2
    
    We want to count the missing timestamps as real records with count=0 for calculating the real average:
    
select A.event_type,  sum(A.cnt) as total,  count(*) , 
       avg(cnt), (sum(A.cnt) / B.number_of_distinct_timestamps) as real_average  from 
( select event_type, time, count(*) as cnt from events group by time, event_type order by time) A,
(select count (distinct time) as number_of_distinct_timestamps from events) B
group by event_type, B.number_of_distinct_timestamps    
```
## Example
```sql
CREATE TABLE D (dev_id int, name text);
INSERT INTO D VALUES(1,'a'),(2,'b'), (3,'c') ;

CREATE TABLE A (t timestamp, dev_id int, val int);
INSERT INTO A VALUES
('2015-01-20 17:45', 1, -10),
('2015-01-20 17:45', 1, -11),

('2015-01-20 17:55', 1, -7),
('2015-01-20 17:55', 2, -7),

('2015-01-20 18:10', 1, -5),
('2015-01-20 18:10', 1, -6)
;


-> get number of distinct timestamps per hourly interval
select date_trunc('hour',t) span, count(distinct t) as span_points FROM A GROUP BY span

-> get number of records  per hourly interval per device
SELECT  date_trunc('hour',t) span , dev_id, count(*) as dev_points FROM A GROUP BY dev_id, span

-> average load per device per timestamp = 
number of records  per hourly span per device / number of distinct timestamps per hourly interval

select X.span, X.dev_id, Y.dev_points, X.span_points, COALESCE(Y.dev_points/X.span_points::float,0) as load FROM
( 
  SELECT D.dev_id, B.span, B.span_points FROM (select date_trunc('hour',t) span, count(distinct t) as span_points FROM A GROUP BY span) B 
  CROSS JOIN D
) X
LEFT JOIN
(SELECT  date_trunc('hour',t) span , dev_id, count(*) as dev_points FROM A GROUP BY dev_id, span) Y
ON (X.span=Y.span AND X.dev_id=Y.dev_id)

span	           dev_id	 dev_points	span_points	load
2015-01-20 17:00:00	1	        3	      2	       1.5
2015-01-20 17:00:00	2	        1	      2	       0.5
2015-01-20 17:00:00	3	        NULL	   2	       0
2015-01-20 18:00:00	1	        2	      1	       2
2015-01-20 18:00:00	2	        NULL	   1       	0
2015-01-20 18:00:00	3	        NULL	   1	       0

```

## ISNULL() COALESCE()
PostgreSQL does not have the ISNULL() function. However, you can use the COALESCE function which provides the similar functionality. Note that the COALESCE function returns the first non-null argument, so the following syntax has the similar effect as the ISNULL function above: COALESCE(expression,replacement)
Also, in addition to COALESCE you can use CASE expression:

```sql
create table emp(id int , name text);
insert into emp VALUES (1,'A');
insert into emp VALUES (2,NULL);

select id, COALESCE(name,'x') FROM emp;

SELECT 
    CASE WHEN expression IS NULL 
            THEN replacement 
            ELSE expression 
    END AS column_alias
FROM emp    
```
RANK gives you the ranking within your ordered partition. Ties are assigned the same rank, with the next ranking(s) skipped. 
So, if you have 3 items at rank 2, the next rank listed would be ranked 5.

DENSE_RANK again gives you the ranking within your ordered partition, but the ranks are consecutive. 
No ranks are skipped if there are ranks with multiple items.

## Find the whole data for the row with some max value in a column per some group identifier.

GREATEST n PER GROUP question. <https://stackoverflow.com/questions/tagged/greatest-n-per-group>

<https://stackoverflow.com/questions/7745609/sql-select-only-rows-with-max-value-on-a-column/7745635#7745635>

Approach #1:
```sql
SELECT a.id, a.rev, a.contents
FROM YourTable a
INNER JOIN (
    SELECT id, MAX(rev) rev
    FROM YourTable
    GROUP BY id
) b ON a.id = b.id AND a.rev = b.rev
```

Approach #2:
```sql
SELECT a.*
FROM YourTable a
LEFT OUTER JOIN YourTable b
    ON a.id = b.id AND a.rev < b.rev
WHERE b.id IS NULL;
```
Approach #3:
```sql
SELECT * FROM t1 WHERE (id,rev) IN 
( SELECT id, MAX(rev) FROM t1 GROUP BY id)

```
Approach #4: correlated subquery
```sql
select yt.id, yt.rev, yt.contents
    from YourTable yt
    where rev = 
        (select max(rev) from YourTable st where yt.id=st.id)
```
Approach #5: RANK() or ROW_NUMBER()
```sql
SELECT a.id, a.rev, a.contents
  FROM (SELECT id, rev, contents,
               ROW_NUMBER() OVER (PARTITION BY id ORDER BY rev DESC) rank
          FROM YourTable) a
 WHERE a.rank = 1 
 ```

## Employee with max salary per each department
```sql
SELECT dept.dname, emp.empno, emp.ename, emp.sal FROM emp
inner join dept on emp.deptno = dept.deptno
inner join
( SELECT emp.deptno, max(emp.sal) sal FROM emp GROUP BY emp.deptno ) ss 
ON emp.deptno = ss.deptno and emp.sal = ss.sal
order by emp.sal desc
```

```sql
SELECT dept.name, MAX(e.salary) FROM emp e 
RIGHT JOIN dept d ON e.deptId = d.deptID GROUP BY dept.name;
```

```sql
create table emp(id int , name text, salary float, dept_id int);
insert into empl values(1,'Mike1', 100, 10);
insert into emp values(2,'Mike2', 200, 10);
insert into emp values(3,'Mike3', 400, 20);

select * from (
SELECT name, id, salary,
  rank() OVER(PARTITION BY dept_id ORDER BY salary DESC) as rank2,
  100.0*salary/sum(salary)  OVER (PARTITION BY dept_id) as percent
FROM emp
) A
where rank2=1;


  select department, first_name, salary
  from (
    select *, row_number() over (partition by department order by  salary desc) as n
    from salary
  ) _
  where n = 1
```



### Find the employees who have the second highest salary per department:
```sql 
 WITH payroll AS (
    SELECT 
        first_name, 
        last_name, 
        department_id,
        salary, 
        RANK() OVER (
            PARTITION BY department_id
            ORDER BY salary) salary_rank
    FROM 
        employees
)
SELECT 
    first_name, 
    last_name,
    department_name,
    salary
FROM 
    payroll p
    INNER JOIN departments d 
        ON d.department_id = p.department_id
WHERE 
    salary_rank = 2;  
```

## Retrieve the names of all people that have more than 1 order 
```sql
 Suppose we have 2 tables: \
 Person(id, name, age, salary) \
 Orders(num,date, person_id, amount): \
 Task: retrieve the names of all people that have more than 1 order 
``` 
### Answer 1:
```sql 
 SELECT name from person where id in (
   SELECT person_id from Orders group by preson_id having count(person_id) > 1
 )
``` 
 
### Answer 2:
```sql 
SELECT Name FROM Orders, Person
WHERE Orders.person_id = Person.id
GROUP BY Person_id, Name                  
HAVING COUNT(person_id) >1
```


## Hierarhy and  Recursive SQL

https://news.ycombinator.com/item?id=42230384

https://www.ibase.ru/treedb/

https://habr.com/ru/articles/812601/ Древовидные структуры в SQL 

https://habr.com/ru/company/bimeister/blog/672634/


https://www.databasestar.com/hierarchical-data-sql/

https://medium.com/learning-sql/some-of-the-useful-recursive-cte-examples-ddd63bced99a

https://blog.devgenius.io/recursive-cte-demystified-6adc0021813f

https://habr.com/ru/articles/794028/

https://medium.com/swlh/recursion-in-sql-explained-graphically-679f6a0f143b

https://habr.com/ru/company/tensor/blog/523812/

 https://stackoverflow.com/questions/4048151/what-are-the-options-for-storing-hierarchical-data-in-a-relational-database
 
 https://news.ycombinator.com/item?id=20027586 Hierarchy and RECURSIVE SQL


### Recursion in SQL

https://medium.com/swlh/recursion-in-sql-explained-graphically-679f6a0f143b

https://news.ycombinator.com/item?id=28018058
 
 
 https://github.com/bitnine-oss/agensgraph . Postgres extension  AgensGraph
 
 http://patshaughnessy.net/2017/12/13/saving-a-tree-in-postgres-using-ltree
 
 https://martinheinz.dev/blog/18 - recursive SQL
 
```sql 
 WITH RECURSIVE cte (id, message, author, path, parent_id, depth)  AS (
  SELECT  id,
          message,
          author,
          array[id] AS path,
          parent_id,
          1 AS depth
  FROM    comments
  WHERE   parent_id IS NULL

  UNION ALL
 
  SELECT  comments.id,
          comments.message,
          comments.author,
          cte.path || comments.id,
          comments.parent_id,
          cte.depth + 1 AS depth
  FROM    comments
          JOIN cte ON comments.parent_id = cte.id
  )
  SELECT id, message, author, path, depth FROM cte
  ORDER BY path;
``` 


https://www.youtube.com/watch?v=swR33jIhW8Q
https://habr.com/ru/post/448072/ . Joins
https://dankleiman.com/2017/11/07/more-efficient-solutions-to-the-top-n-per-group-problem/
https://habr.com/post/422461/ . examples of SQL with answers
http://www.sql-workbench.eu/dbms_comparison.html

## Difference between ON and WHERE clause:

https://blog.jooq.org/2019/04/09/the-difference-between-sqls-join-on-clause-and-the-where-clause/
```sql
CREATE TABLE A( i int, val int,  data varchar(16) );
CREATE TABLE B( i int, val int,  data varchar(16) );

INSERT INTO A values(1, 10, '2010-09-05');
INSERT INTO A values(2, 20, '2010-10-05');
INSERT INTO A values(3, 30, '2010-10-05');
INSERT INTO A values(3, 40, '2010-10-05');

INSERT INTO B values(2, 201, '2010-09-05');
INSERT INTO B values(2, 202, '2020-10-05');
INSERT INTO B values(3, 300, '2010-10-05');

select A.i, A.data, B.i, B.data from A LEFT JOIN B
ON A.i=B.i WHERE A.data='2010-10-05' and B.data='2010-10-05' ;
+------+------------+------+------------+
| i    | data       | i    | data       |
+------+------------+------+------------+
|    3 | 2010-10-05 |    3 | 2010-10-05 |
|    3 | 2010-10-05 |    3 | 2010-10-05 |
+------+------------+------+------------+
2 rows in set (0.00 sec)

select A.i, A.data, B.i, B.data from A LEFT JOIN B
ON ( A.i=B.i and A.data='2010-10-05' and B.data='2010-10-05') ;
+------+------------+------+------------+
| i    | data       | i    | data       |
+------+------------+------+------------+
|    3 | 2010-10-05 |    3 | 2010-10-05 |
|    3 | 2010-10-05 |    3 | 2010-10-05 |
|    1 | 2010-09-05 | NULL | NULL       |
|    2 | 2010-10-05 | NULL | NULL       |
+------+------------+------+------------+
4 rows in set (0.00 sec)
```

https://cs.uwaterloo.ca/~plragde/flaneries/FDS/ functional data structures



http://www.mysqltutorial.org/mysql-row_number/

https://news.ycombinator.com/item?id=13517490

https://vadimtropashko.wordpress.com/%e2%80%9csql-design-patterns%e2%80%9d-book/about/


## Window functions 

https://khashtamov.com/en/sql-window-functions/

https://dataschool.com/how-to-teach-people-sql/how-window-functions-work/

https://www.windowfunctions.com/

https://news.ycombinator.com/item?id=25656583

https://news.ycombinator.com/item?id=20872114

max salary per department:

```sql
SELECT * FROM (
         SELECT id,
                first_name,
                department,
                 salary,
                MAX(salary) OVER (PARTITION BY department) as max_salary
         FROM Salary
     ) t
WHERE max_salary = salary
ORDER BY id;


  select department, first_name, salary
  from (
    select *, row_number() over (partition by department order by  salary desc) as n
    from salary
  ) _
  where n = 1
```


<https://mjk.space/advances-sql-window-frames/>

<https://oracle-base.com/articles/misc/analytic-functions>

<https://hashrocket.com/blog/posts/sql-window-functions>

<https://www.fromdual.com/mariadb-10-2-window-function-examples>

<https://blog.jooq.org/2014/04/29/nosql-no-sql-how-to-calculate-running-totals/>

<https://blog.jooq.org/2013/11/03/probably-the-coolest-sql-feature-window-functions/>

<http://www.windowfunctions.com/>

## 10 question against 1 table:
```
CREATE TABLE cats(
   name varchar(10),
   breed varchar(10),
   weight float,
   color varchar(10),
   age int
);
```
### Q1 RUNNING TOTAL:
The cats must by ordered by name and will enter an elevator one by one. We would like to know what the running total weight is.
 
```
select name, sum(weight)
over (order by name) as running_total_weight
from cats order by name
```

### Q2: Partitioned Running Totals

The cats must by ordered first by breed and second by name. They are about to enter an elevator one by one. 
When all the cats of the same breed have entered they leave.

We would like to know what the running total weight of the cats is.

```
select name, breed, sum(weight)
over (partition by breed order by name) as running_total_weight from cats
```

### Q3: Counting

The cats form a line grouped by color. Inside each color group the cats order themselves by name. \
Every cat must have a unique number for its place in the line.

We must assign each cat a unique number while maintaining their color & name ordering.
```
select row_number() over (order by color,name) as unique_number, name, color from cats
```

### Q4: Ordering

We would like to find the fattest cat. Order all our cats by weight.

The two heaviest cats should both be 1st. The next heaviest should be 3rd.

Return: ranking, weight, name
Order by: ranking, name desc

```
select rank() over (order by weight desc) as ranking, weight, name
from cats order by ranking, name DESC
```

### Q5: Quartiles

We are worried our cats are too fat and need to diet.
We would like to group the cats into quartiles by their weight.
Return: name, weight, weight_quartile
Order by: weight
```
select name, weight, ntile(4) over ( order by weight) as weight_quartile from cats order by weight_quartile, name
```

### Q6: Ranking

For cats age means seniority, we would like to rank the cats by age (oldest first).
However we would like their ranking to be sequentially increasing.
Return: ranking, name, age
Order by: ranking, name
```
select dense_rank() over (order by age DESC) as r, name,age from cats order by r, name
```

### Q7: Compare to Previous Row

Cats are fickle. Each cat would like to lose weight to be the equivalent weight of the cat weighing just less than it.

Print a list of cats, their weights and the weight difference between them and the nearest lighter cat ordered by weight.

Return: name, weight, weight_to_lose
Order by: weight
```
select name, weight, coalesce(weight - lag(weight, 1) over (order by weight), 0) as weight_to_lose 
FROM cats order by weight
```

### Q8: Compare to Previous row using LAG()

The cats now want to lose weight according to their breed. Each cat would like to lose weight to be the equivalent weight of the cat in the same breed weighing just less than it.

Print a list of cats, their breeds, weights and the weight difference between them and the nearest lighter cat of the same breed.

Return: name, breed, weight, weight_to_lose
Order by: weight
```
SELECT name, breed, weight, coalesce(weight - LAG(weight, 1) 
OVER (partition by breed order by weight), 0) as weight_to_lose 
FROM cats order by weight, name
```

### Q9: First of each group: first_value

Cats are vain. Each cat would like to pretend it has the lowest weight for its color.

Print cat name, color and the minimum weight of cats with that color.

Return: name, color, lowest_weight_by_color
Order by: color, name
```
select name, color, first_value(weight) 
over (partition by color order by weight) as lowest_weight_by_color 
from cats order by color, name
```

### Q10: Using the Window clause

This SQL function can be made simpler by using the WINDOW statement. Please try and use the WINDOW clause.

Each cat would like to see what half, third and quartile they are in for their weight.

Return: name, weight, by_half, thirds, quartile
Order by: weight
```
select name, weight, ntile(2) over ntile_window as by_half, ntile(3) 
over ntile_window as thirds, ntile(4) over ntile_window as quart 
from cats window ntile_window AS ( ORDER BY weight)
```

### Visidata

VisiData can read sqlite:  

    vd test.sqlite3
    
### SQL UI client tools

https://dbgate.org/

https://www.dbcli.com/

https://datastation.multiprocess.io/docs/installation.html

HeidiSQL 

https://news.ycombinator.com/item?id=28489165

Sequel-Ace https://github.com/Sequel-Ace/Sequel-Ace

TablePlus  https://tableplus.com/

DBeaver

usql <https://github.com/xo/usql>

https://github.com/TaKO8Ki/gobang/

## Falcon UI

<https://github.com/plotly/falcon> UI

<https://news.ycombinator.com/item?id=22883429>



## CQRS

https://habr.com/ru/post/545128/

https://habr.com/ru/post/146429/  CQRS

https://habr.com/ru/post/149464/ CQRS

https://habr.com/ru/company/nix/blog/321686/

https://habr.com/ru/company/nix/blog/322214/

https://habr.com/ru/post/535452/

### Эффективная конструкция агрегатов

https://habr.com/ru/company/oleg-bunin/blog/329222/ . 10 способов достижения HighLoad'а и BigData на ровном месте

https://habr.com/ru/company/postgrespro/blog/351008/ Postgres and Oracle

https://habr.com/ru/post/177165/ Postgres Aggregate

https://habr.com/ru/company/tensor/blog/507056/

https://habr.com/ru/post/544514/

https://habr.com/ru/company/tensor/blog/539016/


https://habr.com/ru/company/tensor/blog/541374/

https://habr.com/ru/company/tensor/blog/540572/

https://habr.com/ru/company/tensor/blog/539638/

https://habr.com/ru/post/214643/

## My questions
https://stackoverflow.com/questions/64055906/how-to-combine-2-sqls-into-single-sql

https://mathoverflow.net/questions/372543/new-k-samples-added-to-set-calculate-new-stddev-given-the-old-avg-stddev-and-s

https://math.stackexchange.com/questions/3839472/new-k-samples-added-calculate-new-stddev-given-old-avg-stddev-and-sample-size

##  SQL + Jinja   (also there is jinjax)
https://geoffruddock.com/sql-jinja-templating/


### Когортный анализ, LTV и RFM в SQL 
https://habr.com/ru/companies/otus/articles/901114/

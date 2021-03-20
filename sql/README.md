https://habr.com/ru/company/otus/blog/541882/

### SQL UI client tools

Sequel-Ace https://github.com/Sequel-Ace/Sequel-Ace

TablePlus  https://tableplus.com/

DBeaver

usql <https://github.com/xo/usql>

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

##  SQL + Jinja
https://geoffruddock.com/sql-jinja-templating/


### Window function

https://www.youtube.com/watch?v=QenwDm5oWdU


### UNION

https://www.foxhound.systems/blog/sql-performance-with-union/

## LEAD, LAG, FIRST_GAP


http://databasetips.net/2019/02/12/lead-and-lag-accessing-multiple-rows-without-self-join/

```
LAG is a window function that lets you access the value from a column in a row that lags (precedes) the current row. 
Such function receives three parameters: the first one is the column name you want to access (you may use a built-in function instead of a column). 
The second parameter determines an offset from the current row (it is an optional parameter and its default value is 1). 
The third parameter (optional with default value NULL) is the value to be returned if offset goes beyond the bound of the table.
LAG is used together with OVER, where the Partition By and Order By clauses may be used.


```


http://databasetips.net/2019/09/05/sql-3-ways-to-find-gaps-and-missing-values/

http://www.silota.com/docs/recipes/sql-gap-analysis-missing-values-sequence.html


## First_ROW 

<https://stackoverflow.com/questions/63609219/best-way-to-get-1st-record-per-partition-first-value-vs-row-number>

```

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

# TablePlus DBeawer

<https://news.ycombinator.com/item?id=22908224>

## Datasette

<https://datasette.readthedocs.io/en/stable/>

## SQL vs GraphQL

<https://news.ycombinator.com/item?id=22892946>

## Running total

<https://stackoverflow.com/questions/63609219/best-way-to-get-1st-record-per-partition-first-value-vs-row-number>

<https://medium.com/better-programming/4-ways-to-calculate-a-running-total-with-sql-986d0019185c>

```
Select
      t1.day
      ,t1.driver_id
      ,(
        Select sum(profit) from f_daily_rides t2 
        where t1.day >= t2.day and t1.driver_id = t2.driver_id
       )
   FROM f_daily_rides t1
```   

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
 
 <https://habr.com/ru/post/474458/> . Нарастающий (накопительный) итог 
 
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
```
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
```
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
```
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
```
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

```
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
```
SELECT a.id, a.rev, a.contents
FROM YourTable a
INNER JOIN (
    SELECT id, MAX(rev) rev
    FROM YourTable
    GROUP BY id
) b ON a.id = b.id AND a.rev = b.rev
```

Approach #2:
```
SELECT a.*
FROM YourTable a
LEFT OUTER JOIN YourTable b
    ON a.id = b.id AND a.rev < b.rev
WHERE b.id IS NULL;
```
Approach #3:
```
SELECT * FROM t1 WHERE (id,rev) IN 
( SELECT id, MAX(rev) FROM t1 GROUP BY id)

```
Approach #4: correlated subquery
```
select yt.id, yt.rev, yt.contents
    from YourTable yt
    where rev = 
        (select max(rev) from YourTable st where yt.id=st.id)
```
Approach #5: RANK() or ROW_NUMBER()
```
SELECT a.id, a.rev, a.contents
  FROM (SELECT id, rev, contents,
               ROW_NUMBER() OVER (PARTITION BY id ORDER BY rev DESC) rank
          FROM YourTable) a
 WHERE a.rank = 1 
 ```

## Employee with max salary per each department
```
SELECT dept.dname, emp.empno, emp.ename, emp.sal FROM emp
inner join dept on emp.deptno = dept.deptno
inner join
( SELECT emp.deptno, max(emp.sal) sal FROM emp GROUP BY emp.deptno ) ss 
ON emp.deptno = ss.deptno and emp.sal = ss.sal
order by emp.sal desc
```

```
SELECT dept.name, MAX(e.salary) FROM emp e 
RIGHT JOIN dept d ON e.deptId = d.deptID GROUP BY dept.name;
```

```
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

### Find duplicate rows in a database
```
SELECT * FROM emp a WHERE rowid = (SELECT MAX(rowid) FROM EMP b WHERE a.empno=b.empno)
```
### Delete duplicates
```
DELETE FROM emp a WHERE rowid != (SELECT MAX(rowid) FROM emp b WHERE a.empno=b.empno);
```

### Find the employees who have the second highest salary per department:
``` 
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
 Suppose we have 2 tables: \
 Person(id, name, age, salary) \
 Orders(num,date, person_id, amount): \
 Task: retrieve the names of all people that have more than 1 order 
 
### Answer 1:
``` 
 SELECT name from person where id in (
   SELECT person_id from Orders group by preson_id having count(person_id) > 1
 )
``` 
 
### Answer 2:
``` 
SELECT Name FROM Orders, Person
WHERE Orders.person_id = Person.id
GROUP BY Person_id, Name                  
HAVING COUNT(person_id) >1
```


## Hierarhy  Recursive SQL

https://medium.com/swlh/recursion-in-sql-explained-graphically-679f6a0f143b

https://habr.com/ru/company/tensor/blog/523812/

 https://stackoverflow.com/questions/4048151/what-are-the-options-for-storing-hierarchical-data-in-a-relational-database
 
 https://news.ycombinator.com/item?id=20027586 Hierarchy and RECURSIVE SQL
 
 https://github.com/bitnine-oss/agensgraph . Postgres extension  AgensGraph
 
 http://patshaughnessy.net/2017/12/13/saving-a-tree-in-postgres-using-ltree
 
 https://martinheinz.dev/blog/18 - recursive SQL
 
``` 
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
```
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

## Delete duplicate records
```
DELETE    FROM T 
WHERE  ctid NOT IN
        (
        SELECT  MAX(ctid) 
        FROM  T 
        GROUP BY  T.*
        )
```

## Running total
```
select
    a.date,
    sum(b.sales) as cumulative_sales
from sales_table a
join sales_table b on a.date >= b.date
group by a.date
order by a.date;
```

Using window function:
```
select date,
    sum(sales) over (order by date rows unbounded preceding) as cumulative_sales
from sales_table;
```

## Window functions 

https://khashtamov.com/en/sql-window-functions/

https://dataschool.com/how-to-teach-people-sql/how-window-functions-work/

https://www.windowfunctions.com/

https://news.ycombinator.com/item?id=25656583

https://news.ycombinator.com/item?id=20872114

max salary per department:

```
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

### Q9: First of each group

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


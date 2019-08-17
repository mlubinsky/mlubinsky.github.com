
RANK gives you the ranking within your ordered partition. Ties are assigned the same rank, with the next ranking(s) skipped. 
So, if you have 3 items at rank 2, the next rank listed would be ranked 5.

DENSE_RANK again gives you the ranking within your ordered partition, but the ranks are consecutive. 
No ranks are skipped if there are ranks with multiple items.


GREATEST n PER GROUP question. <https://stackoverflow.com/questions/tagged/greatest-n-per-group>

This is a very common question in SQL: 
find the whole data for the row with some max value in a column per some group identifier.

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

Approach #3:
```
SELECT * FROM t1 WHERE (id,rev) IN 
( SELECT id, MAX(rev) FROM t1 GROUP BY id)

```




## Employee with max salary per each department
```
SELECT dept.dname, emp.empno, emp.ename, emp.sal FROM emp
inner join dept on emp.deptno = dept.deptno
inner join
( select emp.deptno, max(emp.sal) sal FROM emp GROUP BY emp.deptno ) ss 
ON emp.deptno = ss.deptno and emp.sal = ss.sal
order by emp.sal desc
```

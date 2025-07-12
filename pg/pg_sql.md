### Postgres Generate Series


```sql
SELECT * FROM generate_series(1, 5);
SELECT * from generate_series(0,10,2);
SELECT * from generate_series('2021-01-01','2021-01-02', INTERVAL '1 hour');
SELECT * from generate_series('2021-01-01','2021-01-02', INTERVAL '1 hour 25 minutes');
SELECT * from generate_series(1,10) a, generate_series(1,2) b;
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


WITH range_values AS (
  SELECT date_trunc('week', min(created_at)) as minval,
         date_trunc('week', max(created_at)) as maxval
  FROM users),

week_range AS (
  SELECT generate_series(minval, maxval, '1 week'::interval) as week
  FROM range_values
),

weekly_counts AS (
  SELECT date_trunc('week', created_at) as week,
         count(*) as ct
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

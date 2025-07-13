Book
https://postgrespro.ru/education/books/internals PostgreSQL 17 изнутри.  
https://edu.postgrespro.com/postgresql_internals-14_en.pdf    Egor Rogov

https://habr.com/ru/articles/923572/ PostgreSQL Mistakes and How to Avoid Them

https://devpro.blob.core.windows.net/presentations/2019/%D0%A7%D1%83%D0%B2%D0%B0%D1%88%D0%BE%D0%B2_%D0%98%D0%B2%D0%B0%D0%BD.pdf

https://volodymyrpotiichuk.com/blog/articles/unique-indexes-on-large-data-in-postgres-sql

PREPARE statement: https://habr.com/ru/articles/923352/

https://habr.com/ru/articles/76309/ Распараллеливание длительных операций

https://pgbootcamp.ru/ru/

https://github.com/PGBootCamp/Russia_2024/tree/main

https://github.com/PGBootCamp/Minsk_2024/tree/main

https://github.com/PGBootCamp/Russia_2023

https://engineering.usemotion.com/migrating-to-postgres-3c93dff9c65d

https://www.youtube.com/watch?v=r-vCQwEv3yY&list=PLFueB7duX_sA3JrMCvVNH_tt-67jUYepQ&index=10

SQL HowTo: алгоритмы на графах (Кирилл Боровиков) – PG BootCamp Russia 2023

https://habr.com/ru/articles/444018/ Как одно изменение конфигурации PostgreSQL улучшило производительность медленных запросов в 50 раз ( random_page_cost и seq_page_cost )

https://www.youtube.com/watch?v=2oUow8SWVaI Postgres Super Power on Practice

https://pgmodeler.io

### Scale Postgres
https://pgdog.dev/blog/you-can-make-postgres-scale

https://pgdog.dev/blog

https://news.ycombinator.com/item?id=43364668

https://habr.com/ru/companies/otus/articles/898114/  FILTER IFNULL A/B test



### GREATEST n per group
https://stackoverflow.com/a/123481/684229

### array_agg



https://stackoverflow.com/questions/3800551/select-first-row-in-each-group-by-group/7630564#7630564



### Partial Index
https://habr.com/ru/companies/otus/articles/900280/
```
CREATE INDEX idx_users_active_only ON users(id)
WHERE deleted_at IS NULL;
```

### GROUPING

https://habr.com/ru/articles/915056/

```sql
SELECT
 CASE WHEN GROUPING(created_at) = 1 THEN 'all' ELSE created_at END AS created_at,
 CASE WHEN GROUPING(zone_nm) = 1 THEN 'all' ELSE zone_nm END AS zone_nm,
 CASE WHEN GROUPING(service_nm) = 1 THEN 'all' ELSE service_nm END AS service_nm,
 SUM(duration) AS duration,
 COUNT(DISTINCT client_id) AS users_count
 FROM mytable
 GROUP BY GROUPING SETS (
 (created_at, zone_nm, service_nm),  -- 1 Полная детализация
 (created_at, zone_nm),              -- 2 Разрез по created_at + zone_nm
 (created_at, service_nm),           -- 3 Разрез по created_at + service_nm
 (zone_nm, service_nm),              -- 4 Разрез по zone_nm + service_nm
 (created_at),                       -- 5 Разрез только по created_at
 (zone_nm),                          -- 6 Разрез только по zone_nm
 (service_nm),                       -- 7 Разрез только по service_nm
 ()                                  -- Итоговая строка (если нужна)
 )
```




### What I wish someone told me about Postgres

https://mccue.dev/pages/3-11-25-life-altering-postgresql-patterns

https://mccue.dev/pages/3-11-25-life-altering-postgresql-patterns

https://www.shayon.dev/post/2025/40/scaling-with-postgresql-without-boiling-the-ocean/

https://github.com/Olshansk/postgres_for_everything?tab=readme-ov-file 

https://habr.com/ru/articles/878574/ Join 2 tables to get not matching recods (NOT IN, NOT EXISTS, LEFT JOIN)

https://habr.com/ru/companies/ruvds/articles/859422/

https://challahscript.com/what_i_wish_someone_told_me_about_postgres

https://news.ycombinator.com/item?id=42111896

https://habr.com/ru/companies/Linx/articles/859460/

https://philbooth.me/blog/nine-ways-to-shoot-yourself-in-the-foot-with-postgresql

https://notso.boringsql.com/

https://habr.com/ru/companies/tensor/articles/870222/

#### Composite index

To speed up SELECT queries that always use columns A and B in the WHERE clause, the best approach is to create a composite (multi-column) index on (A, B).

Recommended Index:

CREATE INDEX idx_t_a_b ON T (A, B);

### Postgres is enough:

https://github.com/Olshansk/postgres_for_everything?tab=readme-ov-file 

https://habr.com/ru/articles/794839/

https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb

https://mccue.dev/pages/8-16-24-just-use-postgres

https://spin.atomicobject.com/redis-postgresql/

https://event-driven.io/en/postgres_superpowers/


MERGE: https://habr.com/ru/companies/otus/articles/792396/

locking https://leontrolski.github.io/pglockpy.html

https://medium.com/redis-with-raphael-de-lio/can-postgres-replace-redis-as-a-cache-f6cba13386dc

Range column for time intervals:
https://supabase.com/blog/range-columns

### Graphs in Postgres

Graph in Postgres
https://news.ycombinator.com/item?id=43198520

### Dynamic SQL

https://habr.com/ru/companies/otus/articles/861240/


### Non-standard Correlation coeff extension

https://github.com/Florents-Tselai/pgxicor

https://github.com/Florents-Tselai/vasco


### Compare schemas 
```
Method 1

pg_dump -h host1 -U user1 -d db1 --schema-only > schema1.sql
pg_dump -h host2 -U user2 -d db2 --schema-only > schema2.sql
diff schema1.sql schema2.sql

Method 2

pip install pg-schema-diff
pg_schema_diff --source postgresql://user1:password@host1/db1 --target postgresql://user2:password@host2/db2

Method 3:

Use pgdiff or apgdiff Tools
pgdiff and apgdiff are third-party tools specifically for PostgreSQL schema comparison. You can run them on the SQL dumps created by pg_dump.

Method 4:
   
SELECT 
    table_schema,
    table_name,
    column_name,
    data_type,
    is_nullable,
    character_maximum_length,
    numeric_precision,
    numeric_scale
FROM 
    information_schema.columns
WHERE 
    table_schema NOT IN ('information_schema', 'pg_catalog')
ORDER BY 
    table_schema, table_name, ordinal_position;

```

https://habr.com/ru/articles/821993/ Статический анализ структуры базы данных  
https://habr.com/ru/articles/839402/ Статический анализ структуры базы данных  

https://habr.com/ru/companies/tensor/articles/842158/ query plan builder

https://www.naiyerasif.com/post/2024/09/04/stop-using-serial-in-postgres/

## Search

https://habr.com/ru/companies/sravni/articles/888534/ Postgres как поисковый движок

https://habr.com/ru/companies/rostelecom/articles/853124/

https://anyblockers.com/posts/postgres-as-a-search-engine

https://habr.com/ru/companies/karuna/articles/809305/

### Just use Postgres



https://habr.com/ru/articles/843324/

https://habr.com/ru/companies/otus/articles/817187/ Интеграция PostgreSQL с другими СУБД через dblink

https://postgres.ai/blog/20220525-common-db-schema-change-mistakes

https://news.ycombinator.com/item?id=40186752

https://habr.com/ru/companies/otus/articles/834314/

https://www.crunchydata.com/blog/postgres-constraints-for-newbies 

```
Фича №1: Массивы и работа с JSON
***********************************
Массивы в PostgreSQL позволяют хранить несколько значений одного типа данных в одной ячейке таблицы.

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    tags TEXT[] -- массив текстовых значений для тегов
);
Вставка данных в таблицу с массивами:

INSERT INTO products (name, tags)
VALUES ('Продукт 1', ARRAY['новинка', 'распродажа']),
       ('Продукт 2', ARRAY['популярное', 'скидка']);
Извлечение данных из массива:

-- найти все продукты, содержащие тег 'новинка'
SELECT * FROM products
WHERE 'новинка' = ANY(tags);
JSON предоставляет возможность хранения и манипуляции полуструктурированными данными.

Создание таблицы с JSON:

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    profile JSONB -- бинарное представление JSON
);
Вставка JSON-данных:

INSERT INTO users (name, profile)
VALUES ('Иван Иванов', '{"age": 30, "city": "Москва", "interests": ["футбол", "чтение"]}'),
       ('Мария Смирнова', '{"age": 25, "city": "Санкт-Петербург", "interests": ["музыка", "путешествия"]}');
Извлечение данных из JSON:

-- извлечь возраст и город пользователя
SELECT 
    name,
    profile->>'age' AS age,
    profile->>'city' AS city
FROM users;

-- Найти пользователей с интересом "музыка"
SELECT * FROM users
WHERE 'музыка' = ANY(profile->'interests');
Где использовать?

Хранение списков предпочтений, например избранные продукты или метки.

Хранение ответов API.

Хранение агрегированных данных, таких как статистика и аналитика, в формате JSON для простоты обработки.

Допустим, есть приложение для соц. сети.

Каждый пользователь имеет профиль, который может включать различные атрибуты: имя, возраст, город и интересы.
 Используя массивы и JSON в PostgreSQL, можно хранить и извлекать эти данные:

-- создание таблицы
CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    attributes JSONB,
    tags TEXT[]
);

-- вставка данных
INSERT INTO user_profiles (username, attributes, tags)
VALUES ('user1', '{"age": 28, "location": "NY", "preferences": {"newsletter": true}}', ARRAY['active', 'premium']),
       ('user2', '{"age": 34, "location": "LA", "preferences": {"newsletter": false}}', ARRAY['inactive']);

-- запрос для извлечения данных
SELECT 
    username,
    attributes->>'age' AS age,
    attributes->>'location' AS location
FROM user_profiles
WHERE 'active' = ANY(tags);

Фича №2: Расширения
********************

Одним из самых популярных расширений в PostgreSQL  
 pg_trgm, который позволяет реализовать полнотекстовый поиск.
 

Усановка и использование расширения pg_trgm:

-- установка расширения
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- создание индекса для полнотекстового поиска
CREATE INDEX trgm_idx ON articles USING gin (content gin_trgm_ops);

-- поиск похожих записей
SELECT * FROM articles
WHERE content % 'поиск';
Предположим, что есть база данных статей или блога, и хочется добавить возможность поиска по содержимому:

-- установка расширения
CREATE EXTENSION IF NOT EXISTS pg_trgm;

-- создание таблицы статей
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    content TEXT
);

-- вставка данных
INSERT INTO articles (title, content)
VALUES ('Статья 1', 'Это пример текста для полнотекстового поиска.'),
       ('Статья 2', 'Поиск похожих текстов в базе данных.');

-- создание индекса
CREATE INDEX content_trgm_idx ON articles USING gin (content gin_trgm_ops);

-- поиск статьи с использованием триграммного поиска
SELECT * FROM articles
WHERE content % 'поиск';



Фича №3: CTE и рекурсивные запросы
*************************************
Общие табличные выражения и рекурсивные запросы в PostgreSQL дают возможность упрощать и организовывать сложные SQL-запросы.

Преимущества:

CTE позволяет разбить сложные запросы на более простые и понятные части.

Возможность создавать временные результирующие наборы данных, которые могут использоваться в основном запросе.

Позволяет сократить повторяющийся код и улучшить производительность за счет разбивки операций на подзапросы.

Пример использования CTE для разбиения сложных запросов:

WITH top_products AS (
    SELECT id, name, sales
    FROM products
    WHERE sales > 1000
),
top_customers AS (
    SELECT id, name, purchases
    FROM customers
    WHERE purchases > 500
)
SELECT tp.name AS product_name, tc.name AS customer_name
FROM top_products tp
JOIN top_customers tc ON tp.id = tc.id;
Рекурсивные запросы позволяют работать с иерархическими структурами, например такими, как категории продуктов или организационная структура.

Рекурсивный запрос для создания иерархии категорий:

WITH RECURSIVE category_hierarchy AS (
    SELECT id, name, parent_id
    FROM categories
    WHERE parent_id IS NULL
    UNION ALL


    SELECT c.id, c.name, c.parent_id
    FROM categories c
    INNER JOIN category_hierarchy ch ON c.parent_id = ch.id
)
SELECT * FROM category_hierarchy;
Рассмотрим пример создания иерархической структуры для компании, где каждый сотрудник может иметь подчиненных:

-- создание таблицы сотрудников
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    manager_id INT REFERENCES employees(id)
);

-- вставка данных
INSERT INTO employees (name, manager_id)
VALUES ('CEO', NULL),
       ('Manager 1', 1),
       ('Manager 2', 1),
       ('Employee 1', 2),
       ('Employee 2', 2),
       ('Employee 3', 3);

-- рекурсивный запрос для иерархии сотрудников
WITH RECURSIVE employee_hierarchy AS (
    SELECT id, name, manager_id
    FROM employees
    WHERE manager_id IS NULL
    UNION ALL
    SELECT e.id, e.name, e.manager_id
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT * FROM employee_hierarchy;
```
### PgBouncer
```
PgBouncer — это приложение из экосистемы PostgreSQL, которое управляет пулом соединений с базой данных,
причем для клиента это происходит прозрачно, как будто соединение происходит с самим PostgreSQL-сервером.
PgBouncer принимает подключения, передает их СУБД-серверу или ставит в очередь,
когда все соединения в пуле (default_pool_size) заняты.
При освобождении соединений из пула очередь обрабатывается.
```
### PgPool
```
Также к СУБД добавили четыре сервера и создали СУБД-кластер из пяти нод.
Запросы по нодам распределялись с помощью PGPool — еще одного полезного приложения для PostgreSQL.
PgPool был настроен на балансировку нагрузки, причем так,
чтобы запросы на запись (INSERT, UPDATE, DELETE) направлялись только на master-ноду. 

# Enabling load balancing for read queries
load_balance_mode = on
# Enabling master-slave mode with streaming replication
master_slave_mode = on
master_slave_sub_mode = 'stream' 

Были также ограничены входящие запросы на самих PostgreSQL-нодах (max_connections).
```
 
https://habr.com/ru/companies/karuna/articles/809305/ pgvector

https://habr.com/ru/companies/postgrespro/articles/819911/ Built-in replanning как способ корректировать огрехи оптимизатора PostgreSQL

https://hakibenita.com/postgresql-get-or-create 


### В PostgreSQL есть следующие виды индексов:
```
• B-tree (поддерживает все стандартные операции сравнения и может применяться с большинством типов данных – для сортировки, ограничений уникальности и поиска по диапазону значений);

• Hash (обеспечивают быстрый доступ к данным по равенству; не поддерживают сортировку или поиск по диапазону значений); 

• GiST (обобщенные и многоцелевые индексы, которые нужны для работы со  сложными типами данных:
геометрическими объектами, текстами и массивами;
позволяют выполнять быстрый поиск по пространственным, текстовым и иерархическим данным);

• SP-GiST (нужны для работы с непересекающимися и неравномерно распределенными данными;
эффективны для поиска в геометрических и IP-адресных данных);

• GIN (используются для полнотекстового поиска и поиска по массивам, JSON и триграммам);

• BRIN (обеспечивают компактное представление больших объемов данных,
особенно когда значения в таблице расположены в определенном порядке;
эффективны для хранения и обработки временных рядов и географических данных). 
```

## https://habr.com/ru/articles/883916/   Effective JOIN
```
Nested Loop Join
Маленькие таблицы, есть индекс
Быстр для небольших данных
Медленный на больших таблицах

Hash Join
Нет индексов, достаточный work_mem
Эффективен для больших таблиц
Использует диск при нехватке work_mem

Merge Join
Таблицы отсортированы
Быстр, если данные отсортированы
Затраты на сортировку, если её нет
```
### BRIN index
https://habr.com/ru/companies/otus/articles/864896/


### Bulk operations: insert/ delete

https://habr.com/ru/companies/otus/articles/819043/

### Config

https://habr.com/ru/companies/softpoint/articles/869446/

https://tembo.io/blog/optimizing-memory-usage

https://news.ycombinator.com/item?id=40642803

https://habr.com/ru/companies/otus/articles/804281/  Config

https://habr.com/ru/companies/selectel/articles/807259/ Выжимаем максимум из PostgreSQL

https://habr.com/ru/companies/otus/articles/815893/

### queues in postgres
https://docs.hatchet.run/blog/multi-tenant-queues
https://news.ycombinator.com/item?id=40077233

https://news.ycombinator.com/item?id=43572733


Ten years of improvements in PostgreSQL's optimizer (rmarcus.info)
https://news.ycombinator.com/item?id=40060123

https://habr.com/ru/companies/otus/articles/881556/ мониторинг логов PostgreSQL

### Postgres extensions:

https://pgt.dev/

https://habr.com/ru/companies/otus/articles/791870/

https://www.youtube.com/watch?v=i1HYbATmWaw

https://habr.com/ru/companies/tensor/articles/782918/

https://dev.to/lnahrf/mastering-postgres-debugging-must-know-queries-for-database-troubleshooting-495a 

https://exaspark.medium.com/the-ultimate-guide-to-postgresql-data-change-tracking-c3fa88779572

https://www.crunchydata.com/blog/an-overview-of-distributed-postgresql-architectures

https://www.enterprisedb.com/postgres-tutorials/10-tools-every-developer-should-have-when-working-postgresql

Postgre vs MySQL 
https://www.bytebase.com/blog/postgres-vs-mysql/


https://www.reddit.com/r/PostgreSQL/

https://planet.postgresql.org/

https://www.postgresonline.com/

stored procedure to rename tables and indexes:
https://habr.com/ru/articles/765484/

### time_series extension

https://tembo.io/blog/pg-timeseries

https://news.ycombinator.com/item?id=40417347

### pg_cron pg_partman, etc

https://tembo.io/blog/tembo-data-warehouse

https://blog.sequinstream.com/build-your-own-sqs-or-kafka-with-postgres/

### Foreign data wrappers FDW

https://packagemain.tech/p/mastering-cross-database-operations-with-postgres-fdw

https://habr.com/ru/companies/otus/articles/817063/ Интеграция PostgreSQL и Hadoop

```sql
CREATE EXTENSION clerk_fdw;

CREATE FOREIGN DATA WRAPPER clerk_wrapper
  handler clerk_fdw_handler
  validator clerk_fdw_validator;

Next, we create a server object. This is where we configure the connection to the source data system.
In the case of Clerk.dev, we need to provide our API key.
The server object also needs to know which FDW to use, so we direct it to the clerk_wrapper we created above.

CREATE SERVER clerk_server
  foreign data wrapper clerk_wrapper
  options (
    api_key '<clerk secret Key>');

Finally, we create a foreign table. This is where we tell Postgres how to map the data from Clerk into a table.

CREATE FOREIGN TABLE clerk_users (
  user_id text,
  first_name text,
  last_name text,
  email text,
  gender text,
  created_at bigint,
  updated_at bigint,
  last_sign_in_at bigint,
  phone_numbers bigint,
  username text
  )
  server clerk_server
  options (
      object 'users'
  );

SELECT *
FROM information_schema.foreign_tables
```



### Read csv as tuples
```
import csv
with open('/tmp/test.csv') as f:
    data=[tuple(line) for line in csv.reader(f)]
```


### Range types

https://www.crunchydata.com/blog/better-range-types-in-postgres-14-turning-100-lines-of-sql-into-3


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

```sql
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

```sql
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

https://blog.sequinstream.com/build-your-own-sqs-or-kafka-with-postgres/

https://habr.com/ru/articles/763188/

https://adriano.fyi/posts/2023-09-24-choose-postgres-queue-technology/

https://tembo.io/blog/introducing-pgmq/  Message Queue

https://news.ycombinator.com/item?id=37636841

https://lobste.rs/s/rk3eft/choose_postgres_queue_technology

## Pub/Subscribe, queue, LISTEN / NOTIFY

https://dimitarg.github.io/joys-of-messaging/

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

```sql
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

https://www.crunchydata.com/blog/six-degrees-of-kevin-bacon-postgres-style

A Different Type of SQL Recursion with PostgreSQL

https://github.com/vb-consulting/blog/discussions/1

https://indrajith.me/posts/recursive-queries-in-postgresql-for-hierarchial-data/

https://www.enterprisedb.com/postgres-tutorials/how-run-hierarchical-queries-oracle-and-postgresql

https://www.mendelowski.com/docs/postgresql/recursive-sql-queries/

```sql
WITH RECURSIVE cte AS (                                                         
SELECT emp_no, ename, manager_no, 1 AS level                                                                         FROM   dummy_table                                                                       
WHERE manager_no is null                                                                                                                                                            
UNION  ALL                                                                                                                                                                               
SELECT e.emp_no, e.ename, e.manager_no, c.level + 1
FROM   cte c                                             
JOIN   dummy_table e ON e.manager_no = c.emp_no 
)                                                                                                                                                                                     
SELECT *  FROM   cte;
```


### Postgres crosstab

https://blog.aurelianix.com/2024/04/04/postgresql-and-its-annoying-crosstab/

https://learnsql.com/blog/creating-pivot-tables-in-postgresql-using-the-crosstab-function/

https://www.postgresonline.com/article_pfriendly/283.html

https://www.postgresql.org/docs/current/tablefunc.html
```sql
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
```sql
Pivot this:
SELECT name, attr1, attr1, attr3, ... FROM T

Goal:   columns are: name_1, name_2, ...
Rows: attr1, attr2, attr_3,  etc


```


### PG function
```sql
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
```python
curs.execute("Select * FROM people LIMIT 0")
cursor.fetchone()
colnames = [desc[0] for desc in curs.description]
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


## Performance tuning
https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb#performance-tuning

https://luis-sena.medium.com/tuning-your-postgresql-for-high-performance-5580abed193d

https://www.postgresql.org/download/windows/



https://www.yugabyte.com/postgresql/postgresql-high-availability/ High Availability

### Partitioning

https://supabase.com/blog/postgres-dynamic-table-partitioning

https://www.postgresql.org/docs/current/ddl-partitioning.html

https://engineering.workable.com/postgres-live-partitioning-of-existing-tables-15a99c16b291

https://www.postgresql.org/docs/current/ddl-partitioning.html#DDL-PARTITIONING-DECLARATIVE

<https://habr.com/ru/company/barsgroup/blog/481694/> Partitioning

the upper bound is exclusive  !!!
```sql
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

### Slow delete
https://ivdl.co.za/2024/05/29/achieving-a-100x-speedup-of-deletes-on-postgresql/

### Indexes
https://www.youtube.com/watch?v=mnEU2_cwE_s B-tree indexes (ru)

https://habr.com/ru/companies/otus/articles/747882/

https://kmoppel.github.io/2022-12-09-the-bountiful-world-of-postgres-indexing-options/






###  JSON

https://habr.com/ru/companies/tensor/articles/901216/

https://habr.com/ru/companies/tensor/articles/771406/

https://habr.com/ru/companies/tensor/articles/850522/

https://habr.com/ru/companies/otus/articles/758010/

https://stackoverflow.com/questions/53086816/postgresql-aggregate-multiple-rows-as-json-array-based-on-specific-column/53087015#53087015

How to generate a JSON output, consisting of arrays of arrays,   
whereas each of the inner arrays contains the aggregated points of a trip (as indicated by trip_log_id).
```sql
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
```
1. json_build_object creates your main json objects
2. json_agg() ... GROUP BY trip_log_id groups these json objects into one trip object
3. second json_agg aggregates all trips into one array
 
### PG dump / restore

https://learn.microsoft.com/en-us/azure/postgresql/flexible-server/how-to-pgdump-restore

Vaccum before backup:  https://www.postgresql.org/docs/current/sql-vacuum.html
```sql
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

 https://github.com/nexsol-technologies/pgassistant
 
### PgAdmin
 right click on database:
 ```
 psql tool
 query tool
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

```sql
SELECT DAYNAME('2008-05-15')

SELECT DAYOFWEEK(date)   1- Sunday 2 - Monday
```
Generate time series
```sql
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

### Postgres Aggregator
https://planet.postgresql.org/

### PG and Python

https://khashtamov.com/en/postgresql-with-python-and-psycopg2/


##  PG internals

https://habr.com/ru/articles/736154/ 
https://habr.com/ru/company/postgrespro/blog/574702/  PG internals

https://zerodha.tech/blog/working-with-postgresql/

https://habr.com/ru/company/tensor/blog/540572/

https://sql-info.de/postgresql/postgres-gotchas.html PG gotchas

https://wiki.postgresql.org/wiki/Don't_Do_This   Do not do it in PG

## Graph and tree extensions for postgres

https://www.richard-towers.com/2025/02/16/representing-graphs-in-postgres.html

https://news.ycombinator.com/item?id=43078100

https://www.sheshbabu.com/posts/graph-retrieval-using-postgres-recursive-ctes/

https://www.crunchydata.com/blog/six-degrees-of-kevin-bacon-postgres-style

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

<https://pgdash.io/blog/postgres-tips-and-tricks.html>

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

## Postgres performance

<https://www.youtube.com/watch?v=xqTNceHxkIo> Postgres performance

https://github.com/nexsol-technologies/pgassistant  pgAssistance

<https://habr.com/ru/company/tensor/blog/498740/> SQL

<https://habr.com/ru/company/tensor/blog/494776/> SQL tricks

<https://habr.com/ru/company/tensor/blog/497008/>

<https://habr.com/ru/company/tensor/blog/492694/>


## Hierarhy
https://www.sheshbabu.com/posts/graph-retrieval-using-postgres-recursive-ctes/

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

https://www.sheshbabu.com/posts/graph-retrieval-using-postgres-recursive-ctes/

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
```sql
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

```sql
-- создаем миллион случайных чисел и строк
CREATE TABLE items AS
  SELECT
    (random()*1000000)::integer AS n,
    md5(random()::text) AS s
  FROM
    generate_series(1,1000000);
 ```   

```sql
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

```sql
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
```sql
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


 
<http://postgres-bits.herokuapp.com/#1>

<https://abelvm.github.io/sql/sql-tricks/>

<https://blog.jooq.org/2016/04/25/10-sql-tricks-that-you-didnt-think-were-possible/>

### LATERAL JOIN
 <https://heap.io/blog/engineering/postgresqls-powerful-new-join-type-lateral>
 
<https://abelvm.github.io/sql/sql-tricks/>

## Time Series analysis with postgres

<https://stackoverflow.com/questions/56863332/database-design-for-time-series>

<https://bytefish.de/blog/postgresql_interpolation/>


<https://content.pivotal.io/blog/time-series-analysis-part-3-resampling-and-interpolation>

<https://tapoueh.org/blog/2018/02/find-the-number-of-the-longest-continuously-rising-days-for-a-stock/>


##  specify a password to psql non-interactively
```
PGPASSWORD=pass1234 psql -U MyUsername myDatabaseName

docker run -e PGPASSWORD="$(pbpaste)" --rm postgres psql -h www.example.com dbname username -c 'SELECT * FROM table;'
```

<https://habr.com/ru/company/oleg-bunin/blog/455248/>

<https://stackoverflow.com/questions/56552852/how-to-store-arrays-of-points-x-y-color-inside-postgres-array>




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
## Geometric data Types
```sql
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
https://www.sheshbabu.com/posts/graph-retrieval-using-postgres-recursive-ctes/
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
```sql
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

 https://www.architecture-weekly.com/p/postgresql-jsonb-powerful-storage

<https://vsevolod.net/postgresql-jsonb-index/>

<https://www.w3resource.com/PostgreSQL/postgresql-json-functions-and-operators.php>

json_to_recordset()
<https://dba.stackexchange.com/questions/98191/postgresql-json-data-type-used-as-nosql-but-view-as-relational-data-structure>
```sql
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



```sql
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
```sql
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
```sql
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

https://habr.com/ru/companies/spectr/articles/869472/

https://explain.dalibo.com/ 

https://substack.com/home/post/p-150506520

https://news.ycombinator.com/item?id=41903425

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

## Performance tuning
https://gist.github.com/cpursley/c8fb81fe8a7e5df038158bdfe0f06dbb#performance-tuning

https://luis-sena.medium.com/tuning-your-postgresql-for-high-performance-5580abed193d

https://severalnines.com/blog/postgresql-tuning-key-things-drive-performance





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

### Time series

https://blog.2ndquadrant.com/scaling-iot-time-series-data-postgres-bdr/ **time based partitioning**

https://www.citusdata.com/blog/2018/01/24/citus-and-pg-partman-creating-a-scalable-time-series-database-on-PostgreSQL/

https://www.citusdata.com/blog/2016/09/09/pgcron-run-periodic-jobs-in-postgres/

https://www.citusdata.com/blog/2018/06/14/scalable-incremental-data-aggregation/

https://cldellow.com/2016/09/15/brin-indexes-in-postgres-9.5.html

https://blog.getbotmetrics.com/150x-speedup-in-real-time-dashboards-with-postgres-9-5-2e987a5b906e

https://www.citusdata.com/blog/2017/03/10/how-to-scale-postgresql-on-aws/

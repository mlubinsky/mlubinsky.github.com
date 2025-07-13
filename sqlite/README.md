### SQLite and DuckDB

https://github.com/manzt/quak  quak is a scalable data profiler for quickly scanning large tables, capturing interactions as executable SQL queries.

https://github.com/uwdata/mosaic  framework for linking databases and interactive views.  https://idl.uw.edu/mosaic/

https://yeet.cx/play

https://perspective.finos.org/

https://prospective.co/

https://sql-workbench.com/


### DuckDB

https://github.com/manifold-systems/manifold/blob/master/docs/articles/duckdb_info.md

https://www.duckplot.com/

https://motherduck.com/blog/introducing-column-explorer/



https://codecut.ai/deep-dive-into-duckdb-data-scientists/

https://duckdb.org/2025/03/12/duckdb-ui.html

https://labs.quansight.org/blog/duckdb-when-used-to-frames

https://news.ycombinator.com/item?id=43342712

https://milescole.dev/data-engineering/2024/12/12/Should-You-Ditch-Spark-DuckDB-Polars.html

https://habr.com/ru/articles/829502/

https://habr.com/ru/companies/yoomoney/articles/840624/

https://www.youtube.com/watch?v=JoVHITW_WeE

https://duckdb.org/2024/08/19/duckdb-tricks-part-1

https://towardsdatascience.com/my-first-billion-of-rows-in-duckdb-11873e5edbb5

https://www.nikolasgoebel.com/2024/05/28/duckdb-doesnt-need-data.html

DuckDB Book https://www.manning.com/books/duckdb-in-action/

https://www.definite.app/blog/query-any-ducking-thing

https://medium.com/towards-data-science/duckdb-and-aws-how-to-aggregate-100-million-rows-in-1-minute-3634eef06b79

https://medium.com/codex/this-pandas-alternative-is-350x-faster-when-processing-100-million-rows-3f6ff992182d

https://towardsdev.com/sqlite-v-duckdb-e803add4f698  vs DuckDB


```
As DuckDB is an analytics database, it has only minimal support for transactions and parallel write access.
 You therefore couldn’t use it in applications and APIs that process and store input data arriving arbitrarily. Similarly when multiple concurrent processes read from a writeable database.
```

https://harlequin.sh/ DuckDB interface

https://github.com/duckdb/duckdb

https://duckdb.org/docs/data/csv

```
In Python,  DuckDB is for getting the data you want, in the form you want it, from a file / remote place. 
Polars is for when you want to do something with that data, like visualize it.
`duckdb.sql("SELECT foo, bar * 2 as bar_times_2 FROM ...").pl()` (now in polars format) -> other stuff
```


https://levelup.gitconnected.com/duckdb-vs-polars-2ff19cc7af41

### SQLite
https://www.youtube.com/watch?v=ZSKLA81tBis

https://mrsuh.com/articles/2024/sqlite-index-visualization-structure/ 
https://antonz.org/sqlite-3-44/

https://antonz.org/tags/modern-sqlite/

https://tenthousandmeters.com/blog/sqlite-concurrent-writes-and-database-is-locked-errors/

https://docs.python.org/3/library/sqlite3.html#command-line-interface

https://habr.com/ru/articles/792630/

https://kerkour.com/sqlite-for-servers

### VSCode extension for SQLite

https://marketplace.visualstudio.com/items?itemName=qwtel.sqlite-viewer

# Download file, unzip, load to sqlite and run SQL 
```
curl -s https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip \
| gunzip \
| sqlite3 -csv ':memory:' '.import /dev/stdin stdin' \
  "select Date from stdin order by USD asc limit 1;"
```


### Conversion from wide format to long format

https://csvbase.com/blog/5

"Wide:  format example: colunms are, date, list of currencies

Date,USD,JPY,BGN,CYP,CZK,DKK,EEK,GBP,HUF,LTL,LVL,MTL,[and on, and on]

"Long" format: just 3 columns like this:

Date,Currency,Rate

Converting from wide to long format is "meld" operation
```
curl -s https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip | \
gunzip | \
python3 -c 'import sys, pandas as pd
pd.read_csv(sys.stdin).melt("Date").to_csv(sys.stdout, index=False)'
```

https://architecturenotes.co/datasette-simon-willison/

https://habr.com/ru/post/687994/

### JSON in SQLite

https://rodydavis.com/sqlite/nosql 

https://www.sqlite.org/json1.html

https://news.ycombinator.com/item?id=37082941

### SQLite extensions

https://sqlpkg.org/

https://sqlite-utils.datasette.io/en/stable/cli.html 

https://antonz.org/sqlite-is-not-a-toy-database/

https://antonz.org/sqlean-py/
 
https://www.joseferben.com/posts/3-things-that-surprised-me-while-running-sqlite-in-production/

https://habr.com/ru/articles/754400/
```
import sqlite3
connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()
cursor.execute('SELECT * FROM Users')
users = cursor.fetchall()
connection.close()
# Преобразуем результаты в список словарей
users_list = []
for user in users:
  user_dict = {
    'id': user[0],
    'username': user[1],
    'email': user[2],
    'age': user[3]
  }
  users_list.append(user_dict)

for user in users_list:
  print(user)

```
Instead code above (for user in users):
```
connection.row_factory = sqlite3.Row
```

### GUI

https://sqlitebrowser.org/

https://github.com/sqlitebrowser/sqlitebrowser

https://sqlitestudio.pl/

https://github.com/little-brother/sqlite-gui

https://lobste.rs/s/k9hzrj/db_browser_for_sqlite

Sequel Ace - UI

https://github.com/lana-k/sqliteviz +Plotly

https://news.ycombinator.com/item?id=30610532. SQL Lite + CSV

https://medium.com/@JasonWyatt/squeezing-performance-from-sqlite-indexes-indexes-c4e175f3c346

https://medium.com/@JasonWyatt/squeezing-performance-from-sqlite-insertions-971aff98eef2

https://medium.com/@JasonWyatt/squeezing-performance-from-sqlite-explaining-the-virtual-machine-2550ef6c5db

https://phiresky.github.io/blog/2020/sqlite-performance-tuning/

https://antonz.org/sqlite-is-not-a-toy-database/

SQLite and DuckDB

https://harlequin.sh/  DuckDB interface

https://simonwillison.net/2022/Sep/1/sqlite-duckdb-paper/

https://news.ycombinator.com/item?id=32675861

https://antonz.org/sqlean/

https://blog.zachwf.com/posts/sqlite-is-dynamically-typed/

https://news.ycombinator.com/item?id=28050198

https://sqlite-utils.datasette.io/en/stable/cli.html#inserting-csv-or-tsv-data  Import from csv

https://unixsheikh.com/articles/sqlite-the-only-database-you-will-ever-need-in-most-cases.html

https://habr.com/ru/company/otus/blog/541820/.  SQLite with  Python and Go

https://github.com/simonw/sqlite-utils

```
  CREATE TABLE tIssue (
    id   INTEGER PRIMARY KEY NOT NULL CHECK (typeof(id) = 'integer'),
    col1 BLOB NOT NULL                CHECK (typeof(col1) = 'blob'),
    col2 TEXT                         CHECK (typeof(col2) = 'text' OR col2 IS NULL)
  );
  ```

### Fast insert
https://blog.metaobject.com/2021/07/inserting-130m-sqlite-rows-per.html

https://news.ycombinator.com/item?id=27944065

https://avi.im/blag/2021/fast-sqlite-inserts/

https://news.ycombinator.com/item?id=27872575


### Work with CSV files using SQL. For data scientists and engineers (superintendent.app)

https://news.ycombinator.com/item?id=27871574

## SQLite utils

https://habr.com/ru/post/553696/ 

https://github.com/simonw/sqlite-utils

### Internals
https://fly.io/blog/sqlite-internals-btree/

https://jvns.ca/blog/2014/09/27/how-does-sqlite-work-part-1-pages/

https://jvns.ca/blog/2014/10/02/how-does-sqlite-work-part-2-btrees/

http://carlosproal.com/ir/papers/p121-comer.pdf The Ubiquitous B-Tree




## JSON

https://dgl.cx/2020/06/sqlite-json-support

https://news.ycombinator.com/item?id=25226260

## Datasette , Dogsheep

https://github.com/simonw/datasette

https://simonwillison.net/

https://dogsheep.github.io/

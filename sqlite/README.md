https://architecturenotes.co/datasette-simon-willison/

https://habr.com/ru/post/687994/

### JSON in SQLite

https://www.sqlite.org/json1.html

https://news.ycombinator.com/item?id=37082941

### SQLite extensions

https://sqlpkg.org/

https://sqlite-utils.datasette.io/en/stable/cli.html 

https://antonz.org/sqlean-py/
 
https://www.joseferben.com/posts/3-things-that-surprised-me-while-running-sqlite-in-production/

### GUI
https://github.com/sqlitebrowser/sqlitebrowser

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


### DuckDB

https://github.com/duckdb/duckdb

https://duckdb.org/docs/data/csv


## JSON

https://dgl.cx/2020/06/sqlite-json-support

https://news.ycombinator.com/item?id=25226260

## Datasette , Dogsheep

https://github.com/simonw/datasette

https://simonwillison.net/

https://dogsheep.github.io/

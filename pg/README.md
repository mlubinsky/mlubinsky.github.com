## Postgres

<https://www.youtube.com/watch?v=uhvqly8MtoI> Postgres 12

<https://habr.com/ru/company/oleg-bunin/blog/455248/>

<https://stackoverflow.com/questions/56552852/how-to-store-arrays-of-points-x-y-color-inside-postgres-array>

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
##
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
##  DateTime

<https://mode.com/blog/postgres-sql-date-functions>

SHOW datestyle;

SET datestyle = "ISO, DMY";

https://stackoverflow.com/questions/6123484/how-do-i-alter-the-date-format-in-postgres/6124387
```
Same outcome:
select time from tracking where time < '2019-06-12 23:00';
select time from tracking where time < '06-12-2019 23:00';
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

<https://www.w3resource.com/PostgreSQL/postgresql-json-functions-and-operators.php>

json_to_recordset 
<https://www.reddit.com/r/PostgreSQL/comments/2u6ah3/how_to_use_json_to_recordset_on_json_stored_in_a/>

CROSS JOIN LATERAL

```
CREATE TABLE People2
(
  id serial,
  room_id INTEGER, 
  time  timestamp with time zone,
  j JSONB
);


{
"points" :
  [ 
     {"x":1, "y":2, "p":"Up"},
     {"x":10, "y":20, "p":"Down"}
  ]
}
  select jsonb_array_elements_text(j->'points') from People2
  select jsonb_array_elements_text((j->>'points')::jsonb) from People2;
  Same outcome for 2 SQL's above:
  
  {"S": "standing", "X": 105, "Y": 118}
  {"S": "standing", "X": 92, "Y": 139}
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
### PostGIS

SELECT postgis_full_version();

<http://postgis.refractions.net/docs/> \
<http://postgis.org/documentation/> \
<https://trac.osgeo.org/postgis/wiki/UsersWikiMain> \
<https://postgis.net/docs/> \
<http://postgis.net/workshops/postgis-intro/geometries.html#collections>

```
4.1.3. SQL-MM Part 3
The SQL Multimedia Applications Spatial specification extends the simple features for SQL spec by defining a number of circularly interpolated curves.

The SQL-MM definitions include 3DM, 3DZ and 4D coordinates, but do not allow the embedding of SRID information.

The Well-Known Text extensions are not yet fully supported. Examples of some simple curved geometries are shown below:

CIRCULARSTRING(0 0, 1 1, 1 0)

CIRCULARSTRING(0 0, 4 0, 4 4, 0 4, 0 0)

The CIRCULARSTRING is the basic curve type, similar to a LINESTRING in the linear world. A single segment required three points, the start and end points (first and third) and any other point on the arc. The exception to this is for a closed circle, where the start and end points are the same. In this case the second point MUST be the center of the arc, ie the opposite side of the circle. To chain arcs together, the last point of the previous arc becomes the first point of the next arc, just like in LINESTRING. This means that a valid circular string must have an odd number of points greater than 1.

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

<http://postgrest.org> 

<http://postgrest.org/en/v5.2/api.html#binary-output>

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

<https://habr.com/ru/company/mailru/blog/453046/> Indexes

<https://cube.dev/blog/postgresql-query-optimization/>

<https://news.ycombinator.com/item?id=19765761>


<https://wiki.postgresql.org/wiki/Don%27t_Do_This>

<https://pgdash.io/blog/postgres-features.html>

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

## Grafana

<https://habr.com/ru/post/448676/>

<https://grafana.com/docs/reference/templating/#the-timefilter-or-timefilter-variable>
WHERE $__timeFilter(
<https://youtu.be/FhNUrueWwOk?list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2> . Variables in Grafana

<https://grafana.com/docs/reference/templating/>

<https://kb.groundworkopensource.com/display/DOC721/How+to+GroundWork+Grafana+dashboard+variables>

The templating feature allows you to create variables that can be used in your metric queries, series names and panel titles. Use this feature to create generic dashboards that can quickly be changed to show graphs for different servers or metrics.

<http://localhost:3000/>

<http://localhost:3000/datasources>

http://ec2-18-221-216-253.us-east-2.compute.amazonaws.com:3000/login . admin/admin1

<https://grafana.com/plugins/postgres>

<http://docs.grafana.org/features/datasources/postgres/>

<https://grafana.com/blog/2018/10/15/make-time-series-exploration-easier-with-the-postgresql/timescaledb-query-editor/>

<https://stackoverflow.com/questions/48512014/using-postgres-with-grafana>

<https://habr.com/ru/company/1cloud/blog/443006/>

<https://www.youtube.com/watch?v=sKNZMtoSHN4&index=7&list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2>

## Links

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

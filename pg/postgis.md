### PostGIS

https://postgis.net/workshops/postgis-intro/installation.html  
```sql
CREATE EXTENSION IF NOT EXISTS postgis;

SELECT postgis_full_version();

CREATE TABLE locations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    coordinates GEOGRAPHY(POINT)
);

INSERT INTO locations (name, coordinates)
VALUES ('Place 1', ST_GeographyFromText('SRID=4326;POINT(-122.4194 37.7749)')),
       ('Place 2', ST_GeographyFromText('SRID=4326;POINT(-118.2437 34.0522)'));
```
 



<https://gis.stackexchange.com/questions/58605/which-function-for-creating-a-point-in-postgis>

<https://stackoverflow.com/questions/57367822/issue-with-st-contains-and-st-within-in-postgis>
<https://lists.osgeo.org/pipermail/postgis-users/2019-August/043463.html>
<https://www.wyzant.com/resources/answers/704882/issue-with-postgis-st-within>

<https://www.postgis.us/presentations/FOSS4G2017_PostGISSpatialTricks.pdf>

```sql
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
Possible solution: cast the Geography as a Geometry in the query because ST_Within,
 do not support geographies, they only support geometries).
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


#### Common Spatial Queries
You may view more of these in my intro to Visualizing Geospatial Data with CartoDB.

Find all polygons from dataset A that intersect points from dataset B:
```sql
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
```json
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
```


```sql
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

```sql
SELECT postgis_full_version();
CREATE TABLE gtest (id serial primary key, name varchar(20), geom geometry(LINESTRING));
```

https://postgis.net/docs/manual-2.5/using_postgis_dbmanagement.html#RefObject
```sql
INSERT INTO geotable ( the_geom, the_name )
  VALUES ( ST_GeomFromText('POINT(-126.4 45.32)', 312), 'A Place');
  
  UPDATE artwork SET where_is = ST_POINT(X, Y);
```

#### create a   table for data from a CSV that has lat and lon columns:
```sql
create table noise.locations
(                                     
name varchar(100),
complaint varchar(100), descript varchar(100),
boro varchar(50),
lat float8,
lon float8,
geom geometry(POINT, 4326)
);
 
-- inputing values for the geometry type after loading data from a CSV:
update noise.locations set the_geom = ST_SetSRID(ST_MakePoint(lon, lat), 4326);

-- adding a geometry column in a non-spatial table:
select addgeometryColumn('table_name', 'geom', 4326, 'POINT', 2);

-- calculating area in EPSG 4326:
alter table noise.hoods set area = (select ST_Area(geom::geography));


SELECT ST_MakePoint(longitude,latitude) as geom FROM list_points
```
In order to use your new geometries with other PostGIS functions,   
you need to specify the coordinate system (SRID) of your points with the ST_SetSRID function.   
The most widely used system is SRID=4326; that is, GPS coordinates).   
If you have no idea where your data comes from, it’s probably this one.  

So our request becomes:

SELECT ST_SetSRID(ST_MakePoint(longitude,latitude),4326) as geom FROM list_points
   
Sometimes you may want to convert your data to a specific coordinate system.   
It is possible with the ST_Transform function,  
which moves the coordinates of a geometry from its current system to another one.

```sql
SELECT ST_AsText(geom) as points FROM list_geom
SELECT ST_X(geom) as longitude, ST_Y(geom) as latitude FROM list_geom

```


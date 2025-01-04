### Trino

https://www.youtube.com/@TrinoDB


https://aws.amazon.com/blogs/big-data/top-9-performance-tuning-tips-for-prestodb-on-amazon-emr/

```
Example Metadata Registration with Hive
CREATE TABLE hive.schema_name.table_name (  
    id INT,  
    name STRING  
)  
WITH (  
    external_location = 's3a://my-bucket/path/',  
    format = 'PARQUET'  
);

Example Metadata Registration with Iceberg

CREATE TABLE iceberg.schema_name.table_name (  
    id INT,  
    name STRING  
)  
WITH (  
    location = 's3a://my-bucket/path/',  
    format = 'PARQUET'  
);

CREATE TABLE hive.schema_name.customer_data (  
    id INT,  
    name STRING  
)  
WITH (  
    external_location = 's3a://my-bucket/customer_data/',  
    format = 'PARQUET'  
);


Handling Partitioned Data
For partitioned datasets (e.g., organized by year and month), you can register all partitions under the same table.

Example: Partitioned Data Registration
Directory structure:

s3a://my-bucket/sales_data/year=2023/month=12/
Define the table with partitioning:

CREATE TABLE hive.schema_name.sales_data (  
    id INT,  
    amount DOUBLE,  
    sale_date DATE  
)  
WITH (  
    external_location = 's3a://my-bucket/sales_data/',  
    format = 'PARQUET',  
    partitioned_by = ARRAY['year', 'month']  
);


No Data Storage:
Trino acts purely as a query engine and does not manage data storage.
This requires an additional layer of data management, as you need to maintain other systems for actual data storage,
 which can increase complexity and overhead.


Not Optimised for Updates:
Trino is not designed for high-frequency small updates or transactions.
It is primarily optimized for read-heavy workloads and batch insertions,
making it less suitable for applications that require real-time data updates or transactional processing.


Resource Intensive:
Trino can be quite resource-intensive, especially in terms of memory usage.
Because it holds data in memory during query execution, large queries can require significant amounts of RAM, 
which might not be ideal for smaller setups or environments with limited resources.

Trino and Apache Iceberg
Trino offers robust support for Apache Iceberg. Trino’s integration with Iceberg allows users to leverage Iceberg’s features, including:

Time Travel: Access data snapshots at specific points in time.
Schema Evolution: Safely evolve table schema without affecting existing data.
Efficient Query Execution: Optimised execution plans using Iceberg’s table metadata.

Trino Arhitecture:
Like many other big data engines there is a form of a coordinator node that then manages
 multiple worker nodes to process all the work that needs to be done.

An analyst or general user would run their SQL which gets pushed to the coordinator.
In turn the coordinator then parses, plans, and schedules a distributed query.

```

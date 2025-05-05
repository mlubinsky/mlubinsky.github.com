### Trino
Trino is optimized for reading  Optimized Row Columnar (ORC) format,.

 it’s fairly easy to implement a custom UDF
 
https://habr.com/ru/articles/863854/

https://engineering.salesforce.com/how-to-etl-at-petabyte-scale-with-trino-5fe8ac134e36/

### тюнинг java virtual machine:
```
-server
-Xmx96G
-XX:InitialRAMPercentage=80
-XX:MaxRAMPercentage=80
-XX:G1HeapRegionSize=32M
-XX:+ExplicitGCInvokesConcurrent
-XX:+ExitOnOutOfMemoryError
-XX:-OmitStackTraceInFastThrow
-XX:ReservedCodeCacheSize=1024M
-XX:PerMethodRecompilationCutoff=10000
-XX:PerBytecodeRecompilationCutoff=10000
-Djdk.attach.allowAttachSelf=true
-Djdk.nio.maxCachedBufferSize=2000000
-XX:+UnlockDiagnosticVMOptions
-XX:+UseAESCTRIntrinsics
-Dfile.encoding=UTF-8
# Disable Preventive GC for performance reasons (JDK-8293861)
-XX:-G1UsePreventiveGC  
# Reduce starvation of threads by GClocker, recommend to set about the number of cpu cores (JDK-8192647)
-XX:GCLockerRetryAllocationCount=32

```

https://www.youtube.com/@TrinoDB


https://aws.amazon.com/blogs/big-data/top-9-performance-tuning-tips-for-prestodb-on-amazon-emr/

Config 
https://trino.io/docs/current/installation/deployment.html

### Example Metadata Registration with Hive
```sql
CREATE TABLE hive.schema_name.table_name (  
    id INT,  
    name STRING  
)  
WITH (  
    external_location = 's3a://my-bucket/path/',  
    format = 'PARQUET'  
);
```
### Example Metadata Registration with Iceberg
```sql
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
```
 
 
Trino queries them directly without additional setup.

Trino requires metadata (via Hive or Iceberg) to understand schema and structure.
A single table can point to a directory with multiple files.


### Handling Partitioned Data
For partitioned datasets (e.g., organized by year and month), you can register all partitions under the same table.

Example: Partitioned Data Registration
Directory structure:

s3a://my-bucket/sales_data/year=2023/month=12/  

Define the table with partitioning:
```sql
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
```

### No Data Storage:

Trino acts purely as a query engine and does not manage data storage.
This requires an additional layer of data management, as you need to maintain other systems for actual data storage,
 which can increase complexity and overhead.


### Not Optimised for Updates:
Trino is not designed for high-frequency small updates or transactions.
It is primarily optimized for read-heavy workloads and batch insertions,
making it less suitable for applications that require real-time data updates or transactional processing.


### Resource Intensive:
Trino can be quite resource-intensive, especially in terms of memory usage.
Because it holds data in memory during query execution, large queries can require significant amounts of RAM, 
which might not be ideal for smaller setups or environments with limited resources.

Trino and Apache Iceberg
Trino offers robust support for Apache Iceberg. Trino’s integration with Iceberg allows users to leverage Iceberg’s features, including:

### Time Travel: Access data snapshots at specific points in time.
Schema Evolution: Safely evolve table schema without affecting existing data.
Efficient Query Execution: Optimised execution plans using Iceberg’s table metadata.

### Trino Arhitecture:
Like many other big data engines there is a form of a coordinator node that then manages
 multiple worker nodes to process all the work that needs to be done.

An analyst or general user would run their SQL which gets pushed to the coordinator.
In turn the coordinator then parses, plans, and schedules a distributed query.


### Every INSERT in Trino is executed by a number of writer nodes (i.e. Trino workers), 
and each of these nodes can have multiple threads (labeled here as “task_writer”) doing the the actual writes.   
Each thread can potentially write to every partition (in this example, data for each partition is spread across all writers).

There are a few session properties (as of Trino 356) associated with these:

- task_writer_count – number of threads per writer per query.
- scale_writers – if true, Trino starts with a single writer, then adds additional writers as the writer_min_size threshold is surpassed for each writer.
   If false, all nodes (up to hash_partition_count) are used to write.
- use_preferred_write_partitioning – if true, each partition is written only by a single writer.
- 
The number of files that ends up getting created is thus a function of:

 num_writers * task_writer_count * num_partitions.

Getting good overall performance on both the write and read side is a matter of tuning all these variables to get reasonable file counts and sizes.
In the end, the right settings to use will depend on a multitude of variables, like the size of the data and skew.   
For example, we use scale_writers=true when we know a given INSERT will have a relatively small amount of data.  

Some final pointers to keep in mind as you go about your tuning process:

As described earlier, compaction can collate files after they are initially written.
Object stores like S3 typically throttle requests based on prefix.
Ensure your partitioning scheme results in a good distribution across prefixes.   
You may potentially want to work with e.g. AWS to pre-partition your bucket at the S3 level to ensure you don’t get throttled.  
Trino writes through the Hive connector are not transactional, but they are semi-transactional in the sense that files are first written out to object store,   
and only after all the files are successfully written is the partition committed to the metastore. Your system should account for this —   
for example, we write to a new s3 prefix on every retry attempt.

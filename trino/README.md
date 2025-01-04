### Trino
```

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
```

https://www.youtube.com/channel/UCZgt6AzoyjslHTC9dz0UoTw System design

https://designgurus.org/blog System Design

https://itnext.io/redis-stack-the-backbone-for-efficient-microservices-b632d1bc8055

### The Redis stack 

- Redis JSON, 
- Redis Search: uses Inverted index and Trie
- Redis Timeseries, 
- Redis Graph
- Redis Bloom

### RedisGraph

Under the hood, RedisGraph uses GraphBlas to implement the sparse adjacency. It uses an adaptation of the Property Graph Model where Nodes (vertices) and Relationships (edges) have attributes. Nodes can have multiple labels and Relationships have a relationship type. It uses an extension of the OpenCypher to query the database.


### Why is Redis so 𝐟𝐚𝐬𝐭?
.
.
The diagram below shows 3 main reasons:

1️⃣ Redis is RAM-based. Access to RAM is at least 1000 times faster than access to random disks. Redis can be used as a cache to improve application responsiveness and reduce database load when used as a cache.

2️⃣ Redis implements IO multiplexing and single-threaded execution.

3️⃣ A number of efficient lower-level data structures are leveraged by Redis. By keeping these data structures in memory, serialization and deserialization costs are reduced.

SortedSet, for example, makes the implementation of leaderboards so simple and efficient. On the other hand, a bitmap can be used to aggregate month-over-month login statuses.

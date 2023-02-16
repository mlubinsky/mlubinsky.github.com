
https://itnext.io/redis-stack-the-backbone-for-efficient-microservices-b632d1bc8055

Why is Redis so 𝐟𝐚𝐬𝐭?
.
.
The diagram below shows 3 main reasons:

1️⃣ Redis is RAM-based. Access to RAM is at least 1000 times faster than access to random disks. Redis can be used as a cache to improve application responsiveness and reduce database load when used as a cache.

2️⃣ Redis implements IO multiplexing and single-threaded execution.

3️⃣ A number of efficient lower-level data structures are leveraged by Redis. By keeping these data structures in memory, serialization and deserialization costs are reduced.

SortedSet, for example, makes the implementation of leaderboards so simple and efficient. On the other hand, a bitmap can be used to aggregate month-over-month login statuses.

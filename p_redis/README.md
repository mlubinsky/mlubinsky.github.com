https://www.youtube.com/channel/UCZgt6AzoyjslHTC9dz0UoTw System design

https://designgurus.org/blog System Design

https://itnext.io/redis-stack-the-backbone-for-efficient-microservices-b632d1bc8055

### Redis vs Postgres

https://habr.com/ru/company/cloud_mts/blog/716548/

### The Redis stack 

https://habr.com/ru/companies/nixys/articles/765694/
```
Строки — самый простой тип данных. Значения могут быть строками любого вида, например, можно хранить изображение в формате JPEG внутри значения.
Размер строки не может быть больше 512Mb. Большинство строковых операций выполняются за O(1). 

  для максимальной утилизации ресурсов, короткие строки, вроде имен, адресов электронных почт, номеров телефонов и т.д. лучше класть в хэши,

Списки (lists) — коллекции строк, упорядоченные в порядке добавления. Redis использует внутри связанные списки — каждый элемент содержит указатели на предыдущий и следующий элементы, а также указатель на строку внутри элемента. Это означает, что вне зависимости от количества элементов внутри списка, операция добавления нового элемента в начало или конец списка выполняется за O(1), так как для вставки необходимо только изменить ссылки. Также не стоит забывать, что команды, которые манипулируют элементами в списке (вроде LSET), обычно имеют сложность O(n), что может вызвать проблемы с производительностью при большом количестве элементов. Максимальная длина списка Redis —  4 294 967 295 элементов.

Наборы (sets) — это неупорядоченная коллекция уникальных элементов, которая эффективно подходит для отслеживания уникальных компонентов, а также для операций над множествами. Максимальный размер — 4 294 967 295 элементов, большинство операций над множествами выполняются за O(1).

Хэши (hashes) — это записи, структурированные как коллекции пар поле-значение. Каждый хэш может хранить до 4 294 967 295 пар поле-значение, большинство хэш-команд Redis имеют сложность O(1) и самое главное: хэши можно очень эффективно закодировать в памяти
```

https://blog.logrocket.com/guide-to-fully-understanding-redis/

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

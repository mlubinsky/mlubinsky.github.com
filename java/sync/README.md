https://en.wikipedia.org/wiki/Readers%E2%80%93writers_problem

 many threads try to access the same shared memory at one time. Some threads may read and some may write, with the constraint that no process may access the share for either reading or writing, while another process is in the act of writing to it. (In particular, it is allowed for two or more readers to access the share at the same time.) 

https://en.wikipedia.org/wiki/Producer%E2%80%93consumer_problem

The problem describes two processes, the producer and the consumer, who share a common, fixed-size buffer used as a queue. The producer's job is to generate a piece of data, put it into the buffer and start again. At the same time, the consumer is consuming the data (i.e., removing it from the buffer) one piece at a time. The problem is to make sure that the producer won't try to add data into the buffer if it's full and that the consumer won't try to remove data from an empty buffer.

The solution for the producer is to either go to sleep or discard data if the buffer is full. The next time the consumer removes an item from the buffer, it notifies the producer, who starts to fill the buffer again. In the same way, the consumer can go to sleep if it finds the buffer to be empty. The next time the producer puts data into the buffer, it wakes up the sleeping consumer. The solution can be reached by means of inter-process communication, typically using semaphores.

https://docs.oracle.com/javase/tutorial/essential/concurrency/
http://tutorials.jenkov.com/java-concurrency/locks.html
http://tutorials.jenkov.com/java-concurrency/read-write-locks.html
http://tutorials.jenkov.com/java-concurrency/starvation-and-fairness.html
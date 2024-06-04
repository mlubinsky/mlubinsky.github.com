### Apache Beam

https://jaehyeon.me/blog/2024-03-28-beam-local-dev-1/


### Books

https://leanpub.com/streamprocessingwithapacheflink

https://www.amazon.com/Stream-Processing-Apache-Flink-Implementation/dp/149197429X

https://data-flair.training/blogs/apache-flink-books/


https://datorios.com/

https://www.kdnuggets.com/how-to-digest-15-billion-logs-per-day-and-keep-big-queries-within-1-second

https://habr.com/ru/companies/ru_mts/articles/772898/

How to Digest 15 Billion Logs Per Day and Keep Big Queries Within 1 Second


https://www.youtube.com/@flinkforward

https://kavitmht.medium.com/building-a-real-time-data-streaming-pipeline-using-kafka-flink-and-postgres-stream-100k-records-365ea7b6c176

###  Kafka + Flink

https://mysteryweevil.medium.com/demystifying-stream-processing-with-apache-flink-a-practical-introduction-fa976c77d831

```
DataStream<T> dataStream = // your data stream
dataStream
    .assignTimestampsAndWatermarks(new YourTimestampExtractor())
    .windowAll(EventTimeSessionWindows.withGap(Time.minutes(5)))
    .process(new YourProcessWindowFunction());
```

https://medium.com/@muniandibaskaran/apache-flink-kafka-consumer-producer-example-0e657d8a3471

Through Watermark, the user can define the acceptable lateness allowed for processing elements with timestamps below the Watermark being left unprocessed.

 Flink comes in handy as it provides three characteristics 
 - IngestionTime
 - ProcessingTime
 - EventTime

https://medium.com/@siladityaghosh/apache-flink-an-overview-with-sample-code-84fe19113f21

pip install apache-flink

PyFlink to implement WordCount

```
# Import PyFlink modules
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, DataTypes
from pyflink.table.udf import udf

# Create a StreamExecutionEnvironment
env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

# Create a StreamTableEnvironment
t_env = StreamTableEnvironment.create(env)

# Define a Python UDF to split words
@udf(input_types=[DataTypes.STRING()], result_type=DataTypes.ARRAY(DataTypes.STRING()))
def split(words):
    return words.split()

# Register the Python UDF
t_env.register_function("split", split)

# Read a text file as a stream
t_env.execute_sql("""
    CREATE TABLE words (
        word STRING
    ) WITH (
        'connector' = 'filesystem',
        'path' = '/path/to/file',
        'format' = 'csv'
    )
""")

# Count the frequency of words
t_env.execute_sql("""
    SELECT word, COUNT(*) AS `count`
    FROM words, LATERAL TABLE(split(word)) AS T(word)
    GROUP BY word
""").print()

# Execute the job
t_env.execute("WordCount")
```


#### Flink cluster



 - Job Manager 
 - Task Manager


 - session-cluster - can process several jobs
 - job-cluster - can process 1 job


### FlinkCEP  - Complex Event Processing

https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/libs/cep/

https://habr.com/ru/post/471946/

https://dev.to/aws-builders/serverless-complex-event-processing-with-apache-flink-3dbm

#### Flink data  abstractions:

- DataSet  (like Datafame in Spark)  -  batch processing (Table, Jelly API  for Graph processing, FLINK ML API for Machine Learning)
- DataStream<T> - stream processing https://nightlies.apache.org/flink/flink-docs-release-1.2/api/java/org/apache/flink/streaming/api/datastream/DataStream.html

#### DataSources for DataStream API

- readFile(fileInputFormat, path, wathcType, interval, PathFilter)
- socketTextStream
addSource() 
- Kafka 
- Flume, etc

#### Data Sink

writeAs


#### Keyed DataStream

```
If you want to use keyed state, you first need to specify a key on a DataStream
that should be used to partition the state (and also the records in the stream themselves).
 You can specify a key using keyBy(KeySelector) in Java/Scala API
or key_by(KeySelector) in Python API on a DataStream.
This will yield a KeyedStream, which then allows operations that use keyed state.

A key selector function takes a single record as input
and returns the key for that record.
The key can be of any type and must be derived from deterministic computations.
```



#### Operators: DataSet/DataStream Tranformations

Operators transform one or more DataStreams into a new DataStream. Programs can combine multiple transformations into sophisticated dataflow topologies.

https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/operators/overview/

https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/operators/overview/

- filter (DataStream → DataStream)
- map: for every input eleement : 1 output element (DataStream → DataStream)
- flatmap:  returns a collection (which can hold none, one, or more elements). (DataStream → DataStream)
- groupby
- sum
- keyBy  (DataStream → KeyedStream)
- reduce (KeyedStream → DataStream)
- Window  (KeyedStream → WindowedStream )
```  
Windows can be defined on already partitioned KeyedStreams.
Windows group the data in each key according to some characteristic
(e.g., the data that arrived within the last 5 seconds). 
Java example:
dataStream
  .keyBy(value -> value.f0)
  .window(TumblingEventTimeWindows.of(Time.seconds(5))); 
```

#### Map: 
```
получает объект T и в результате возвращает объект типа R;
MapFunction строго однократно применяется с каждым элементом объекта DataStream.
```

SingleOutputStreamOperator<R> map(MapFunction<T,R> mapper)

```
All transformations require a user defined functions to be provided by application developer. 
For example, if we have to map String values to Integer from a data stream, 
we will transform each value using the MapFunction. 
MapFunction is used with the DataStreams and user has to implement the business logic 
for each value in the map method as follows:
```
Example:
```
class MyMapFunction implements MapFunction<String, Integer> {
  public Integer map(String value) { return Integer.parseInt(value); }
};
```

#### Reduce: 
```
получает два последовательных значения и возвращает один объект, 
скомбинировав их в объект того же типа; 
этот метод прогоняется по всем значениям в группе, пока из них не останется всего одно.
```
T reduce(T value1, T value2)

#### Filter: 
```
получает объект T и возвращает поток объектов T; 
этот метод прогоняется по всем элементам DataStream, 
но возвращает только те, для которых функция возвращает true.
```
SingleOutputStreamOperator<T> filter(FilterFunction<T> filter)




####  CoMapFunctions 
```
  CoMapFunctions are similar to MapFunction except they are used for the ConnectedStream 
  so we will map the values of both streams using respected map methods, map1, map2. 
  There is no guarantee that which map method will be called first. 
```  
  The following sample has two input streams of Integer and strings and it returns boolean.
```
connectedStreams.map(new CoMapFunction<Integer, String, Boolean>() {
    @Override
    public Boolean map1(Integer value) {
        return true;
    }

    @Override
    public Boolean map2(String value) {
        return false;
    }
});
```

  #### Rich functions 
  provide four additional methods  other than map methods:
 - open()
 - close() 
 - getRuntimeContext() 
 - setRuntimeContext()
 
 We can have both RichMap and RichCoMap.
```
open() is used to make function stateful by initializing the state. It’s only called once. 
RuntimeContext is used to access different state types e.g. ValueState, ListState. 
Similarly, we can clean up on the close method as it is called when processing is done.

Following is the example using RichFlatMapFunction to count average of all values over a count window of 5. 
It does use value state to store the running sum and count of the values. 
We will initialize the state using open method of the rich function. 
We have used gerRuntimeContext to get the state descriptor.
```
Code:
```
public class CountWindowAverage extends RichFlatMapFunction<Tuple2<Long, Long>, Tuple2<Long, Long>> {

    /**
     * The ValueState with count, a running sum.
     */
    private transient ValueState<Tuple2<Long, Long>> sum;

    @Override
    public void flatMap(Tuple2<Long, Long> input, Collector<Tuple2<Long, Long>> out) throws Exception {

        // access the state value
        Tuple2<Long, Long> currentSum = sum.value();
        currentSum.f0 += 1;
        currentSum.f1 += input.f1;
        sum.update(currentSum);

        // if the count is 5, emit the average and clear the state
        if (currentSum.f0 >= 5) {
            out.collect(new Tuple2<>(input.f0, currentSum.f1 / currentSum.f0));
            sum.clear();
        }
    }

    @Override
    public void open(Configuration config) {
        ValueStateDescriptor<Tuple2<Long, Long>> descriptor =
                new ValueStateDescriptor<>(
                        "average", // the state name
                        TypeInformation.of(new TypeHint<Tuple2<Long, Long>>() {}), // type information
                        Tuple2.of(0L, 0L)); // default value of the state, if nothing was set
        sum = getRuntimeContext().getState(descriptor);
    }
}
```
So to summarize, we have MapFunction for DataStreams and CoMapFunction for ConnectedStreams. 
Furthermore, appending Rich to these functions make them rich 
by adding four additional methods which are commonly used for state management.

#### Times 
https://nightlies.apache.org/flink/flink-docs-release-1.10/dev/event_time.html
  
- Processing time — time of a particular machine that will process the specific element. It could be different than the actual event time when the event is generated, and the order of events could be separate because of the network failures and delays.
- Event time — It is the time when an event is generated at the source. It’s the actual time of an event (embedded within record).
- Ingestion time — It is a time when the Flink receives an event for processing. It could be more reliable than the processing time since all the operators will see the same timestamp for the individual event;  helps to handle out of order events

keyBy() converts the DataStream into the KeyedDataStream 

#### State Management
https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/concepts/stateful-stream-processing/

https://habr.com/ru/company/neoflex/blog/573730/
  
The streaming application/transformation can be 
 - stateful- depends on current element and previous elements  : reduce, sum, aggregate
 - stateless - depends on current element only: map, flatmap, filter
 
In many cases, you can process application stream elements independently from each other, 
but some cases require managing state, referred to as _stateful stream processing_. 

For example, if we monitor the average running temperature of an IoT sensor, we need to store some values in the state. Also, the state is required to support Flink’s fault-tolerance behavior.

Out of the box, Flink bundles these state backends:

- HashMapStateBackend
- EmbeddedRocksDBStateBackend


#### There are two types of states
— Operator state: The operator state is related to a single operator - 2 sub types (Broadcast and List State)
- Keyed state: is shared across a keyed stream. Keyed states support different data structures to store the state values: 6 state sub-types:

 https://habr.com/ru/company/beeline/blog/648729/
 
 #### Keyed State 
 
 ```
    1. ValueState<T> стейт хранит само событие

    2. ListState<T> это список событий (тип также совпадает с типом события)

    3. ReducingState<T> хранит одно событие, отражающее все события по этому ключу, при добавлении события вызывается функция свертки ReduceFunction.

    4. AggregatingState<IN, OUT> также хранит одно событие, отражающее все события по этому ключу, но в отличие от ReducingState тип хранимого значения может отличаться от типа события в потоке, при добавлении вызывается функция агрегации AggregateFunction.

    5. MapState<UK, UV> хранит события в структуре ключ-значение, типы не зависят от типа событий в потоке.
    
    6. Broadcast State
```
#### RichFunction
```
Keyed State can only be used in RichFunction. 
The biggest difference between RichFunction and common and traditional Function is
that it has its own lifecycle. 
The use of Key State contains the following four steps:

 1. Declare the State as the instance variable in the RichFunction.
 2. Perform an initialization assignment operation for the State in the open() method corresponding to the RichFunction.
      2.a The first step of the assignment operation is to create a StateDescriptor and specify a name for the State during the creation. 
      2.b The second step is to call the getRuntimeContext().getState(…) in RichFunction to pass in the defined StateDescriptor so as to obtain the State.
3. Call State method: e.g. state.value() or state.update() to read and write
```

The state can be used with any of the transformations, but we have to use the Rich version of the functions 
such as _RichFlatMapFunction_ because it provides additional methods used to set up the state.


### Broadcast state:

 https://www.ververica.com/blog/a-practical-guide-to-broadcast-state-in-apache-flink  
 https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/fault-tolerance/broadcast_state/

#### DataStream join
  
https://selectfrom.dev/dynamic-filtering-in-flink-af6939f3da2e  
  
https://blog.knoldus.com/flink-join-two-data-streams/

 https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/operators/joining/
```  
 stream.join(otherStream)
    .where(<KeySelector>)
    .equalTo(<KeySelector>)
    .window(<WindowAssigner>)
    .apply(<JoinFunction>); 
```
  
https://medium.com/@knoldus/flink-join-two-data-streams-1cc40d18a7c7
  
```
  final DataStream<Tuple2<Integer, String>> departmentStream = executionEnvironment
                    .socketTextStream("localhost", 9001)
                    .map((MapFunction<String, Tuple2<Integer, String>>) departmentTextStream -> {
                        String[] salaryFields = departmentTextStream.split(" ");
                        if (salaryFields.length == 2 &&
                                !(salaryFields[0].isEmpty()
                                        || salaryFields[1].isEmpty())) {
                            return new Tuple2<>(Integer.parseInt(salaryFields[0]), salaryFields[1]);
                        } else {
                            throw new Exception("Not valid input passed");
                        }
                    }, TypeInformation.of(new TypeHint<Tuple2<Integer, String>>() {
                    }));
  ```
  
  Now, join the salary data stream and department data stream on a key id of an individual which is common in both the streams. After joining, 
  
 The resultant data stream will have all the information in one go -: id, name, salary, and department of an individual.
```
final DataStream<Tuple4<Integer, String, String, Double>> joinedStream =
                 salaryStream.join(departmentStream)
                 .where(getSalaryJoinKey -> getSalaryJoinKey.f0, TypeInformation.of(new TypeHint<Integer>() {}))
                 .equalTo((KeySelector<Tuple2<Integer, String>, Integer>) getDepartmentKey -> getDepartmentKey.f0)
                 .window(TumblingProcessingTimeWindows.of(Time.seconds(30)))
                 .apply((JoinFunction<Tuple3<Integer, String, Double>,
                         Tuple2<Integer, String>, Tuple4<Integer, String, String, Double>>) (salaryDetail, departmentDetail) ->
                                    new Tuple4<>(salaryDetail.f0, salaryDetail.f1, departmentDetail.f1, salaryDetail.f2),
                                    TypeInformation.of(new TypeHint<Tuple4<Integer, String, String, Double>>() {}));
```  
Here, using a common window for both the stream. We want a tumbling window and window to be based on processing time that’s why using TumblinProcessingTimeWindows Class. 

The window size is 30 sec which means all entities from both the streams that come within 10 seconds will be included in one window. 

Then apply JoinFunction to perform join on both the streams and get the resultant complete joined information of an individual.
  
  
#### Dataset Joins

 Following is an inner join for person (pid, personName) and location (pid,locationName) dataset.
```
DataSet<Tuple3<Integer, String, String>> joined = 
      personSet.join(locationSet, JoinOperatorBase.JoinHint.OPTIMIZER_CHOOSES)
      .where(0)
      .equalTo(0)
      .with((JoinFunction<Tuple2<Integer, String>, Tuple2<Integer, String>, 
            Tuple3<Integer, String, String>>) (personTuple, locationTuple) 
            -> new Tuple3<>(personTuple.f0, personTuple.f1, locationTuple == null? "NULL" :locationTuple.f1));
```            
Flink also let the app developers specify join hints. There are six type of join hints.

#### OPTIMIZER_CHOOSES: 
This will use the default system optimizations while doing the join operations. Hence it’s optional.

#### BROADCAST_HASH_FIRST: 
```
Flink is a distributed stream processing and when we are joining two different data sets or streams, both of those can be on different nodes. Joining data from different nodes can be quite expensive operation. If one of the dataset is small, we can move it to the memory of the other nodes so that whenever they are joining with each other they perform the join operation from the data in the memory and avoid the shuffling of data among different nodes. This hint will broadcast the first dataset to the different nodes before performing the join.
```
#### BROADCAST_HASH_SECOND: 
It is similar to the BROADCAST_HASH_FIRST except we move the second data set into the memory of the nodes for join operations to reduce shuffling.

#### REPARTITION_HASH_FIRST: 
This will create a hash table from the input dataset to optimize the lookup for the join operation. As data is large and distributed, having a hash table will help to quickly find the relevant column values when we are joining. This hint will built the hash table from the first input.

#### REPARTITION_HASH_SECOND: 
It is simlar to REPARTITION_HASH_FIRST but builds the hashtable for the second dataset. In general we use the hint for the data set that is small in size.

#### REPARTITION_SORT_MERGE: 
This hint is used to leverage the sorting to make joins faster. As we know if datasets are sorted and it’s just like serial reads on both of the datasets. This hint is passed to tell Flink that one of the dataset is already sorted and it can leverage the already sorted dataset.



#### Storage
- Files: local, HDFS. S3
- Databases: MongoDB, HBase
- Streams: Kafka, Flume, RabbitMQ


### Flink Table and SQL

https://habr.com/ru/companies/neoflex/articles/745730/

default_catalog and initial database default_database
 
https://dataai.udemy.com/course/apache-flink-a-real-time-hands-on-course-on-flink/

https://www.ververica.com/blog/apache-flink-sql-past-present-and-future

```
rom pyflink.table import (
    DataTypes, TableEnvironment, EnvironmentSettings, 
    CsvTableSource, CsvTableSink, WriteMode
)


def main():
    env_settings = EnvironmentSettings.new_instance()\
                        .in_batch_mode()\
                        .use_blink_planner()\
                        .build()
    tbl_env = TableEnvironment.create(env_settings)

    in_field_names = ['seller_id', 'product', 'quantity', 'product_price', 'sales_date']
    in_field_types = [DataTypes.STRING(), DataTypes.STRING(), DataTypes.INT(), DataTypes.DOUBLE(), DataTypes.DATE()]
    source = CsvTableSource(
        './input',
        in_field_names,
        in_field_types,
        ignore_first_line=True
    )
    tbl_env.register_table_source('locale_product_sales', source)

    out_field_names = ['seller_id', 'revenue']
    out_field_types = [DataTypes.STRING(), DataTypes.DOUBLE()]
    sink = CsvTableSink(
        out_field_names,
        out_field_types,
        './sql-output/revenue.csv',
        num_files=1,
        write_mode=WriteMode.OVERWRITE
    )
    tbl_env.register_table_sink('locale_revenue', sink)

    sql = """
      SELECT t.seller_id AS seller_id, SUM(t.sales) AS revenue
      FROM (
          SELECT seller_id, product, quantity, product_price, sales_date,
              quantity * product_price AS sales
          FROM locale_product_sales
      ) t
      GROUP BY t.seller_id
    """

    output_tbl = tbl_env.sql_query(sql)

    print('\nLocale Revenue Schema')
    output_tbl.print_schema()

    output_tbl.execute_insert('locale_revenue').wait()


if __name__ == '__main__':
    main()
```

### Keyed vs non-keyed stream

 Keying a stream shuffles all the records such that elements with the same key are assigned to the same partition. 
 This means all records with the same key are processed by the same physical instance of the next operator.

Keyed Stream (after keyBy() Operation) - window() 


Non-keyed stream - wnidowAll()

Window assigner defines how entities are assigned to windows

DataStream<Tuple5<String,String, String, Integer, Integer>> mapped = data.map(new Splitter())
```
DataStream<Tuple5<String,String, String, Integer, Integer>> mapped
 .keyBy(0)
 .window(TumblingProcessingTimeWindows.of(Time.seconds(2)))
 .reduce(new Reduce1());
```



### Window types
https://flink.apache.org/news/2015/12/04/Introducing-windows.html
  
https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/operators/windows/#window-assigners  

https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/operators/windows/

- Tumbling window - time based - no overlapped
```
// Tumbling window, without key
public AllWindowedStream<T,TimeWindow> timeWindowAll(Time size)
// Tumbling window, with key
public WindowedStream<T,KEY,TimeWindow> timeWindow(Time size)
```
- Sliding window - time based windows are overlappping (offset parameter)
```
dataStreamObject.timeWindow(Time.minutes(1), Time.seconds(30))
```

- Session window - created based on activity, does not have fixed start or end time, ended then there is gap in activity.  session window closes when it does not receive elements for a certain period of time, i.e., when a gap of inactivity occurred. A session window assigner can be configured with either a static session gap or with a session gap extractor function which defines how long the period of inactivity is. When this period expires, the current session closes and subsequent elements are assigned to a new session window.
  
```  
  // Определение фиксированного сеансового окна длительностью 2 секунды
dataStreamObject.window(ProcessingTimeSessionWindows.withGap(Time.seconds(2)))
// Определение динамического сеансового окна, которое может быть задано элементами потока 
dataStreamObject.window(EventTimeSessionWindows.withDynamicGap((elem) -> {
        // возвращается промежуток между сеансами, который может зависеть от событий потока 
    }))
```  
- Global window (window per key, do computation with trigger). This windowing scheme is only useful if you also specify a custom trigger. 
  
- Count window  - does not depend on time  
- User-defined window: You can also implement a custom window assigner by extending the WindowAssigner class.




### Triggers

- EventTimeTrigger
- ProcessingTimeTrigger
- CountTrigger
- PurgingTrigger


#### Trigger interface 
  has five methods that allow a Trigger to react to different events:

- The onElement() method is called for each element that is added to a window.
- The onEventTime() method is called when a registered event-time timer fires.
- The onProcessingTime() method is called when a registered processing-time timer fires.
- The onMerge() method is relevant for stateful triggers and merges the states of two triggers when their corresponding windows merge, e.g. when using session windows.
- Finally the clear() method performs any action needed upon removal of the corresponding window.
  
  
Trigger actions:
- CONTINUE - do nothing
- FIRE - trigger the computation (default)
- PURGE - clear content on Window
- FIRE_AND_PURGE


Default Trigger available for every Window type .... 
 
Window lifecycle 
 
1. Window created window() / windowAll
2. .Trigger()
3. .evictor() - optional; to remove elements from window before window function is applied
4. window function (redce/fold/aggregare/etc)
5. evictor() - optional; to remove elements from window after window function is applied
6. result

 ### Default evictors

 
 CountEvictor - keeps the user-specified number of elelemts from the window and discard the remaining 
 ```
 .evictor(CountEvictor.of(4))
 ```
DeltaEvictor: takes DeltaFunction and threshold  args, computes delta betweeen last element and remaining elements and then removes those elements whose delta > threshold
 ```
 .evictor(DeltaEvictor.of(threshold.new MyDelta())
 ```
 TimeEviictor 
 
 You cat create your own Evictor based on Evictoe interfacre
 
### Watermarks, allowed lateness, late elements

```
DataStream<Tuple5<String,String, String, Integer, Integer>> mapped
 .keyBy(0)
 .asssignTimestampsAndWatermarks(new DemoWatermark<MyEvent)
 .window(TumblingProcessingTimeWindows.of(Time.seconds(2)))
 .allowedLateness(time)
 .sideOutputLateDate(lateOutputTag)
 .reduce(new Reduce1());
  
  
final OutputTag<T> lateOutputTag = new OutputTag<T>("late-data"){};

DataStream<T> input = ...;

SingleOutputStreamOperator<T> result = input
    .keyBy(<key selector>)
    .window(<window assigner>)
    .allowedLateness(<time>)
    .sideOutputLateData(lateOutputTag)
    .<windowed transformation>(<window function>);
 
 here window function could be
 - ProcessFunction, 
 - CoProcessFunction
 - ProcessWindowFunction
 - ProcessAllWindowFunction

DataStream<T> lateStream = result.getSideOutput(lateOutputTag);  
```

### Split the stream

#### ProcessFunction()
https://github.com/liorksh/FlinkBasicDemo
 
```
В приведенном ниже фрагменте кода вызывается ProcessFunction, разделяющий поток на два боковых, 
в зависимости от свойства ввода. 
Для получения того же результата нам пришлось бы неоднократно использовать функцию filter.

Функция ProcessFunction собирает определенные объекты (на основе критерия)
и отправляет в главный выводной коллектор (заключается в SingleOutputStreamOperator), 
а остальные события передаются в боковые выводы. 
Поток DataStream разделяется по вертикали и публикует различные форматы для каждого бокового потока.

Обратите внимание: определение бокового потока вывода основано на уникальном теге вывода (объект OutputTag).

   // Определить отдельный поток для Исполнителей
            final OutputTag<Tuple2<String,String>> playerTag
                    = new OutputTag<Tuple2<String,String>>("player"){};

            // Определить отдельный поток для Певцов
            final OutputTag<Tuple2<String,Integer>> singerTag
                    = new OutputTag<Tuple2<String,Integer>>("singer"){};

            // Преобразовать каждую запись в объект InputData и разделить главный поток на два боковых.
            SingleOutputStreamOperator<InputData> inputDataMain
                    = inputStream
                    .process(new ProcessFunction<String, InputData>() {

                        @Override
                        public void processElement(
                                String inputStr,
                                Context ctx,
                                Collector<InputData> collInputData) {

                            Utils.print(Utils.COLOR_CYAN, "Received record : " + inputStr);

                            // Преобразовать строку в объект InputData 
                            InputData inputData = InputData.getDataObject(inputStr);

                            switch (inputData.getType())
                            {
                                case "Singer":
// Создать выходной кортеж со значениями имени и счета
                                    ctx.output(singerTag,
                                            new Tuple2<String,Integer>
                                                    (inputData.getName(), inputData.getScore()));
                                    break;
                                case "Player":
 // Создать выходной кортеж со значениями имени и типа;
// Если новоиспеченный кортеж не совпадает с типом playerTag, то выбрасывается ошибка компиляции ("вывод метода не может быть применен к указанным типам")
                                    ctx.output(playerTag,
                                            new Tuple2<String, String>
                                                    (inputData.getName(), inputData.getType()));
                                    break;
                                default:
                      // Собрать вывод основного потока как объекты InputData 
                                    collInputData.collect(inputData);
                                    break;
                            }
                        }
                    });


```

getSideOutput()

### Merge the streams
- connect()
https://github.com/liorksh/FlinkBasicDemo
```
// В описании возвращенного потока учтены типы данных обоих потоков 
        ConnectedStreams<Tuple2<String, Integer>, Tuple2<String, String>> mergedStream
                = singerStream
                .connect(playerStream);


        DataStream<Tuple4<String, String, String, Integer>> combinedStream
                = mergedStream.map(new CoMapFunction<
                        Tuple2<String, Integer>, // Поток 1
                        Tuple2<String, String>, // Поток 2
                        Tuple4<String, String, String, Integer> //Вывод
                        >() {

                            @Override
                            public Tuple4<String, String, String, Integer>  //Обработка потока 1
                            map1(Tuple2<String, Integer> singer) throws Exception {
                                return new Tuple4<String, String, String, Integer>
                                        ("Source: singer stream", singer.f0, "", singer.f1);
                            }

                            @Override
                            public Tuple4<String, String, String, Integer> 
// Обработка потока 2
                            map2(Tuple2<String, String> player) throws Exception {
                                return new Tuple4<String, String, String, Integer>
                                        ("Source: player stream", player.f0, player.f1, 0);
                            }
                 });
```

- map()


#### Build DataStream:
```
// Определение фиксированного сеансового окна длительностью 2 секунды
dataStreamObject.window(ProcessingTimeSessionWindows.withGap(Time.seconds(2)))
// Определение динамического сеансового окна, которое может быть задано элементами потока 
dataStreamObject.window(EventTimeSessionWindows.withDynamicGap((elem) -> {
        // возвращается промежуток между сеансами, который может зависеть от событий потока 
    }))
    
 // Каждая запись преобразуется в кортеж с именем и счетом 
        DataStream<Tuple2<String, Integer>> userCounts
                = inputDataObjectStream
                .map(new MapFunction<InputData,Tuple2<String,Integer>>() {

                    @Override
                    public Tuple2<String,Integer> map(InputData item) {
                        return new Tuple2<String,Integer>(item.getName() ,item.getScore() );
                    }
                })
                .returns(Types.TUPLE(Types.STRING, Types.INT))
                .keyBy(0)  // возвращает KeyedStream<T, Tuple> на основе первого элемента (поля 'name')
                //.timeWindowAll(Time.seconds(windowInterval)) // НЕ ИСПОЛЬЗОВАТЬ timeWindowAll с потоком на основе ключей
                .timeWindow(Time.seconds(2)) // вернуть WindowedStream<T, KEY, TimeWindow>
                .reduce((x,y) -> new Tuple2<String,Integer>( x.f0+"-"+y.f0, x.f1+y.f1));    
   
   
 // Определить временное окно и подсчитать количество записей
           DataStream<Tuple2<String,Integer>> inputCountSummary
                    = inputDataObjectStream
                    .map( item
                            -> new Tuple2<String,Integer>
                            (String.valueOf(System.currentTimeMillis()),1)) 
// для каждого элемента вернуть кортеж из временной метки и целого числа (1)
                    .returns(Types.TUPLE(Types.STRING ,Types.INT))
                    .timeWindowAll(Time.seconds(windowInterval)) // кувыркающееся окно
                    .reduce((x,y) -> // суммируем числа, и так до достижения единого результата
                            (new Tuple2<String, Integer>(x.f0, x.f1 + y.f1)));

            // Задаем в качестве стока для потокового файла каталог вывода 
            final StreamingFileSink<Tuple2<String,Integer>> countSink
                    = StreamingFileSink
                        .forRowFormat(new Path(outputDir),
                                new SimpleStringEncoder<Tuple2<String,Integer>>
                                        ("UTF-8"))
                        .build();

            // Добавляем поток стока к DataStream; при таком условии inputCountSummary будет вписан в путь countSink 
            inputCountSummary.addSink(countSink);   
```

#### Links
  
https://habr.com/ru/company/beeline/blog/648729/
  
https://habr.com/ru/company/piter/blog/531434/

https://flink.apache.org/news/2020/07/30/demo-fraud-detection-3.html

https://www.ververica.com/blog/flink-sql-queries-and-time

https://www.ververica.com/blog


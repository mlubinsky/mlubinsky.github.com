#### Flink data  abstractions:

- DataSet  (like Datafame in Spark)  -  batch processing (Table, Jelly API  for Graph processing, FLINK ML API for Machine Learning)
- DataStream - stream processing

#### DataSources for DataStream API

readFile(fileInputFormat, path, wathcType, interval, PathFilter)
socketTextStream
addSource() Kafka, Flume, etc

#### Data Sink

writeAs

#### DataSet Tranformations

- filter
- map
- flatmap
- groupby
- sum

#### Map 

All transformations require a user defined functions to be provided by application developer. For example, if we have to map String values to Integer from a data stream, we will transform each value using the MapFunction. MapFunction is used with the DataStreams and user has to implement the business logic for each value in the map method as follows
```
class MyMapFunction implements MapFunction<String, Integer> {
  public Integer map(String value) { return Integer.parseInt(value); }
};
```
CoMapFunctions are similar to MapFunction except they are used for the ConnectedStream so we will map the values of both streams using respected map methods, map1, map2. There is no guarantee that which map method will be called first. The following sample has two input streams of Integer and strings and it returns boolean.
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
Rich functions provide four additional methods open, close, getRuntimeContext and setRuntimeContext other than map methods. We can have both RichMap and RichCoMap.

Open is used to make function stateful by initializing the state. It’s only called once. RuntimeContext is used to access different state types e.g. ValueState, ListState. Similarly, we can clean up on the close method as it is called when processing is done.

Following is the example using RichFlatMapFunction to count average of all values over a count window of 5. It does use value state to store the running sum and count of the values. We will initialize the state using open method of the rich function. We have used gerRuntimeContext to get the state descriptor.
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
So to summarize, we have MapFunction for DataStreams and CoMapFunction for ConnectedStreams. Furthermore, appending Rich to these functions make them rich by adding four additional methods which are commonly used for state management.

#### Times 
 
- Processing time — time of a particular machine that will process the specific element. It could be different than the actual event time when the event is generated, and the order of events could be separate because of the network failures and delays.
- Event time — It is the time when an event is generated at the source. It’s the actual time of an event (embedded within record).
- Ingestion time — It is a time when the Flink receives an event for processing. It could be more reliable than the processing time since all the operators will see the same timestamp for the individual event;  helps to handle out of order events


#### State Management
https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/concepts/stateful-stream-processing/


The streaming application can be stateful or stateless. 
In many cases, you can process application stream elements independently from each other, but some cases require managing state, referred to as _stateful stream processing_. 

For example, if we monitor the average running temperature of an IoT sensor, we need to store some values in the state. Also, the state is required to support Flink’s fault-tolerance behavior.

#### There are two types of states

— Operator state: The operator state is related to a single operator
- Keyed state is shared across a keyed stream. Keyed states support different data structures to store the state values — ValueSate, ListSate, MapState, ReducingState.

The state can be used with any of the transformations, but we have to use the Rich version of the functions 
such as _RichFlatMapFunction_ because it provides additional methods used to set up the state.




#### Joins

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
Flink is a distributed stream processing and when we are joining two different data sets or streams, both of those can be on different nodes. Joining data from different nodes can be quite expensive operation. If one of the dataset is small, we can move it to the memory of the other nodes so that whenever they are joining with each other they perform the join operation from the data in the memory and avoid the shuffling of data among different nodes. This hint will broadcast the first dataset to the different nodes before performing the join.

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

Flink currently supports 3 main state primitives for keyed state:
- ValueState, 
-  ListState, 
-  MapState.

### Window types
https://flink.apache.org/news/2015/12/04/Introducing-windows.html

https://nightlies.apache.org/flink/flink-docs-release-1.16/docs/dev/datastream/operators/windows/

- Tumbling window - time based - no overlapped
- Sliding window - time based windows are overlappping (offset parameter)
- Session window - created based on activity, does not have fixed start or end time, ended then there is gap in activity
- Global window (window per key, do computation with trigger)





### Triggers

- EventTimeTrigger
- ProcessingTimeTrigger
- CountTrigger
- PurgingTrigger


Trigger actions:
- CONTINUE - do nothing
- FIRE - trigger the computation (default)
- PURGE - clear content on Window
- FIRE_AND_PURGE


1. Window created window() / windowAll
2. .Trigger()
3. .evictor() - optional; to remove elements from window before window function is applied
4. window function (redce/fold/aggregare/etc)
5. 3. .evictor() - optional; to remove elements from window after window function is applied
6. result


### Watermarks, allowed lateness, late elements

https://flink.apache.org/news/2020/07/30/demo-fraud-detection-3.html

https://www.ververica.com/blog/flink-sql-queries-and-time

https://www.ververica.com/blog


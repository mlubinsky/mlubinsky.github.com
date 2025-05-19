
https://mayursurani.medium.com/comprehensive-guide-to-production-grade-databricks-pyspark-applications-edba1cefb362

https://medium.com/@suffyan.asad1/introduction-to-aggregate-and-transform-functions-in-apache-spark-cfbdb0c57aa8

https://medium.com/@suffyan.asad1/spark-leveraging-window-functions-for-time-series-analysis-in-pyspark-03aa735f1bdf

### SQL CASE in PySpark: when ... otherwise
```python
df = df.withColumn(
    "dummy", \
    F.when(F.col("group_1")=="A", 100) \
    .when(((F.col("group_1")=="B") & (F.col("group_2")=="124")), 200) \
    .otherwise(300)
)
```
#### groupBy +  agg (avg, sum)

df.groupBy("department").agg({"salary": "avg","bonus": "sum"}).show()

### (agg, count, when) - all together 
```python 
counts = one_day_df.agg(
    F.count(F.when(F.col("percent_completed") > 1000, True)).alias("count_greater_than_1000"),
    F.count(F.when((F.col("percent_completed") >= 100) & (F.col("percent_completed") <= 1000), True)).alias("count_between_100_and_1000"),
    F.count(F.when((F.col("percent_completed") >= 50) & (F.col("percent_completed") <= 100), True)).alias("count_between_50_and_100"),
    F.count(F.when(F.col("percent_completed") < 50, True)).alias("count_less_than_50")
)

counts.show()

```
### MAX_BY: max_by(x, y) - Returns the value of x associated with the maximum value of y.

 SELECT max_by(x, y) FROM VALUES ('a', 10), ('b', 50), ('c', 20) AS tab(x, y);

 Result : b

MAX_BY in pyspark >= 3.3.0

Example: there is dataframe with 3 columns: category, datetime, value
Goal: add column which store datetime where max(value) is achieved

```python
from pyspark.sql.window import Window
from pyspark.sql import functions as F

w = (
    Window
    .partitionBy('category')
    .rangeBetween(Window.unboundedPreceding, Window.unboundedFollowing)
)
mdt = F.max_by('datetime', 'value').over(w)
df2 = df.withColumn('datetime_max', mdt)

### without using max_by it require more coding:

from pyspark.sql import Window
from pyspark.sql.functions import *

w = Window.partitionBy('category').orderBy(desc('value'))

df.withColumn("datetimeMax",max(when(row_number().over(w) == 1,col("datetime"))).over(w)).show(100,False)

```

#### selectExpr 

Instead of using multiple withColumn, use selectExpr for inline transformations.
```python
df = df.selectExpr("id", "upper(name) as name","salary * 1.1 as updated_salary")

sub_df = data.selectExpr("store_code as store_id",
                         "cast(product_code as int) as product_id",
                         "cast(sales_date as date) as date",       
                          "cast(sales_qty as int)")
```

#### To remove duplicates based on certain columns, use
 
 dropDuplicates.df = df.dropDuplicates(["name", "age"])



### withColumn  

df = df.withColumn("new_column",df["existing_column"] * 10)

### Cache vs persist
df.cache() # Stores the DataFrame in memory

df.persist() # Default stores in memory, can specifydifferent storage levels 

### Explode
If a column contains arrays, use explode to flatten them.
```python
from pyspark.sql.functions import explode
df_exploded = df.withColumn("exploded_column",explode(df["array_column"]))
```

#### Use coalesce for efficient Repartitioning If you have too many small partitions, use coalesce to reduce them efficiently.

df = df.coalesce(5) # Reduces partitions but avoids full shuffle

Use repartition for Evenly Distributed Data. When dealing with skewed data, use repartition to balance partitions.

df = df.repartition(10, "department")
 
Use rdd.mapPartitions for Efficient Row-Level Operations   
When working with large datasets, use mapPartitions instead of map for better performance.

df.rdd.mapPartitions(lambda partition:some_function(partition))

#### Optimize Writing with partitionByWhen writing large datasets, partition them to improve query performance.

 df.write.mode("overwrite").partitionBy("year","month").parquet("output_path")

### Use ThreadPoolExecutor with PySpark
```
def get_count(table):
    count =spark.read.format("delta").load(table).count()
    return (table,count)

# Code implementation using ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=4) as executor:
    result = list(executor.map(get_count, table_paths))

# creating a dataframe
results_df = spark.createDataFrame(result, ["table_name", "row_count"])
results_df.display()
```

## DROP NESTED COLUMNS
```
from pyspark.sql.functions import col
from pyspark.sql.types import StructType

columns_to_drop=["genres","names","artworks","credits","descriptions","entitled_artworks"]

df_event = spark.read.json(s3_event).limit(100)
columns_to_drop=["artworks","brands","credits","descriptions"]

# 1a: Drop the nested columns in one statement
df_event = df_event.withColumn("entity", col("entity").dropFields(*columns_to_drop))

# 1b: Drop the nested columns   one by one 
for col_name in columns_to_drop:
     df_extra = df_extra.withColumn("entity", col("entity").dropFields(col_name))
     
```
### Question: What following PySpark code does?
```python

merged_df.select(
    [F.coalesce(df_unique[col], prev_snapshot[col]).alias(col) for col in prev_snapshot.columns]
).distinct()
```

This PySpark code performs the following operations on merged_df:

Column Selection with Coalescing:

 
[F.coalesce(df_unique[col], prev_snapshot[col]).alias(col) for col in prev_snapshot.columns]

This list comprehension iterates over each column in prev_snapshot.columns.

For each column, it creates a new column using F.coalesce() between df_unique[col] and prev_snapshot[col].

F.coalesce() returns the first non-null value from the two columns: if df_unique[col] is null, it will take the value from prev_snapshot[col].

The result of F.coalesce() is given an alias matching the column name (col) so that the final DataFrame has the same column names as prev_snapshot.
Select and Distinct:

merged_df.select(...).distinct()

The .select(...) statement selects all the coalesced columns created in the list comprehension,   
generating a new DataFrame where each column contains either the non-null value from df_unique or prev_snapshot.
.distinct() removes any duplicate rows from the selected DataFrame.
 
This code creates a DataFrame that combines values from df_unique and prev_snapshot by filling in nulls in df_unique with corresponding values from prev_snapshot.   
It then removes duplicate rows from the result.

In essence, it’s merging the two DataFrames on a column-by-column basis,   
preferring values from df_unique while filling in any gaps with values from prev_snapshot, and ensuring no duplicate rows in the final output.
 





### Diff between dataframes
https://medium.com/@gollulikithraj/key-differences-in-spark-operations-2520db90696b

```

1) exceptALL :  returns all the rows that exist in the first DataFrame but do not appear in the second DataFrame , do not remove duplicates in df1
df1.exceptAll(df2).isEmpty() and df2.exceptAll(df1).isEmpty()
 
If the exceptAll operation on both DataFrames results in empty DataFrames, it suggests that they might be equal.

2) diff:
df1.diff(df2).isEmpty() and df2.diff(df1).isEmpty()

If the diff operation on both DataFrames results in empty DataFrames, it's a strong indication that they are equal

3) substract: removes  duplicates from df1 , so it is different from execptALL

df1.substract(df2).isEmpty() and df2.substract(df1).isEmpty()

```

### Analyze dataframe
```python
from pyspark.sql import functions as F

def analyze_dataframe(df, cols_of_interest, combinations_of_columns):
    # Total number of rows in the dataframe
    total_rows = df.count()
    print(f"Total number of rows: {total_rows}")
    
    # Analysis for each column in cols_of_interest
    for col in cols_of_interest:
        # Count of null values
        null_count = df.filter(F.col(col).isNull()).count()
        print(f"\nColumn: {col}")
        print(f"  Null values: {null_count}")
        
        # Count of unique values
        unique_count = df.select(col).distinct().count()
        print(f"  Unique values: {unique_count}")
        
        # Count of records per value (GROUP BY)
        value_counts = df.groupBy(col).count().orderBy(F.col("count").desc())
        print(f"  Records per value:")
        value_counts.show(truncate=False)
        
        # Min and max values
        min_val = df.agg(F.min(col)).collect()[0][0]
        max_val = df.agg(F.max(col)).collect()[0][0]
        print(f"  Min value: {min_val}")
        print(f"  Max value: {max_val}")
    
    # Analysis for each list of columns in combinations_of_columns
    for cols_combo in combinations_of_columns:
        # Count of unique combinations
        unique_combo_count = df.select(cols_combo).distinct().count()
        print(f"\nCombination of columns: {cols_combo}")
        print(f"  Unique combinations: {unique_combo_count}")
        
        # Count of records per combination (GROUP BY)
        combo_counts = df.groupBy(cols_combo).count().orderBy(F.col("count").desc())
        print(f"  Records per combination:")
        combo_counts.show(truncate=False)

```
### Example of usage:
```python
# Example DataFrame
data = [
    ("A", 1, None), 
    ("B", 2, 10), 
    ("A", 3, 30), 
    ("B", 2, 20), 
    (None, 1, None)
]
df = spark.createDataFrame(data, ["col1", "col2", "col3"])

# Define columns of interest and combinations of columns
cols_of_interest = ["col1", "col2"]
combinations_of_columns = [["col1", "col2"], ["col1", "col3"]]

# Call the function
analyze_dataframe(df, cols_of_interest, combinations_of_columns)

```

### Gemini
```python
import pyspark.sql.functions as F

def data_quality_analysis(df, cols_of_interest, list_of_cols_combinations):
  """
  Performs data quality analysis on a given DataFrame.

  Args:
    df: The DataFrame to analyze.
    cols_of_interest: A list of columns to analyze individually.
    list_of_cols_combinations: A list of lists, where each inner list represents a combination of columns to analyze together.

  Returns:
    None
  """

  # Print total number of rows
  print("Total number of rows:", df.count())

  # Analyze individual columns
  for col in cols_of_interest:
    print(f"\nColumn: {col}")
    print("Number of null values:", df.filter(F.col(col).isNull()).count())
    print("Number of unique values:", df.select(F.col(col)).distinct().count())
    print("Value counts:")
    df.groupBy(F.col(col)).count().show()
    print("Minimum value:", df.agg(F.min(col)).collect()[0][0])
    print("Maximum value:", df.agg(F.max(col)).collect()[0][0])

  # Analyze column combinations
  for cols_comb in list_of_cols_combinations:
    print(f"\nColumn combination: {cols_comb}")
    print("Number of unique combinations:", df.select(*cols_comb).distinct().count())
    print("Combination counts:")
    df.groupBy(*cols_comb).count().show()
```
### Gemini usage
```python
# Create a DataFrame
df = spark.createDataFrame(
    [
        (1, "A", "X"),
        (2, "B", "Y"),
        (3, "A", "X"),
        (4, "C", "Z"),
        (5, None, "X"),
    ],
    ["col1", "col2", "col3"]
)

# Define columns of interest and column combinations
cols_of_interest = ["col1", "col2", "col3"]
list_of_cols_combinations = [["col1", "col2"], ["col2", "col3"]]

# Call the function
data_quality_analysis(df, cols_of_interest, list_of_cols_combinations)
```


Here are 6 Python libraries you can use to make the EDA process easier:
```
- 𝗦𝘄𝗲𝗲𝘁𝘃𝗶𝘇: Generates comparative reports that visually analyze data and target features.
- 𝗣𝗮𝗻𝗱𝗮𝘀 𝗣𝗿𝗼𝗳𝗶𝗹𝗶𝗻𝗴: Creates comprehensive reports on datasets with detailed analyses of each column.
- 𝗔𝘂𝘁𝗼𝗩𝗶𝘇: Automatically visualizes data with minimal coding required, making it easier to identify trends and patterns.
- 𝗗-𝗧𝗮𝗹𝗲: Offers a web-based interface for detailed analysis, visualization, and diagnosis of data.
- 𝘆𝗱𝗮𝘁𝗮_𝗽𝗿𝗼𝗳𝗶𝗹𝗶𝗻𝗴: Focuses on data quality and profiling to ensure that your data is clean and ready for analysis.
- 𝗗𝗮𝘁𝗮𝗽𝗿𝗲𝗽: Simplifies the process of cleaning and preparing data for analysis, helping you to quickly get to the insights.
```

https://github.com/ydataai/ydata-profiling

### Different ways to read data into PySpark:
 
1.Reading from CSV Files:
 df = spark.read.csv("path/to/file.csv", header=True, inferSchema=True)

2. Reading from JSON Files:
 df = spark.read.json("path/to/file.json")

3. Reading from Parquet Files:
 df = spark.read.parquet("path/to/file.parquet")

4. Reading from Text Files:
 df = spark.read.text("path/to/file.txt")

5. Reading from Database:
 You can read from databases using JDBC:
 ```python
 df = spark.read.format("jdbc").options(
 url="jdbc:postgresql://host:port/dbname",
 driver="org.postgresql.Driver",
 dbtable="table_name",
 user="username",
 password="password"
 ).load()
```
6.Reading from Hive Tables:
 If you have a Hive context set up:
 df = spark.sql("SELECT * FROM hive_table_name")

7. Reading from ORC Files:
 df = spark.read.orc("path/to/file.orc")

8. Reading from Avro Files** (requires the Avro package):
 df = spark.read.format("avro").load("path/to/file.avro")

9. Reading from Kafka:
 To read streaming data from Kafka:
 df = spark.readStream.format("kafka").option("kafka.bootstrap.servers", "server:port").option("subscribe", "topic").load()

10. Reading from Delta Lake:
 If using Delta Lake:
 df = spark.read.format("delta").load("path/to/delta_table")
 



### Generate dataframe

```python
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, ArrayType, LongType
from pyspark.sql import Row

# Initialize Spark session
spark = SparkSession.builder.appName("Create DataFrame").getOrCreate()

# Define the schema
schema = StructType([
    StructField("profile_id", StringType(), nullable=True),
    StructField("watched_media_ids", ArrayType(StringType(), containsNull=False), nullable=False),
    StructField("sum_runtime_ms", LongType(), nullable=True),
    StructField("max_bitrate", LongType(), nullable=True)
])

# Create some sample data
data = [
    ("user_1", ["media_1", "media_2"], 5000000, 3000),
    ("user_2", ["media_3"], 1500000, 2500),
    ("user_3", ["media_4", "media_5", "media_6"], None, 4000),
]

# Create DataFrame using the defined schema
df = spark.createDataFrame([Row(*row) for row in data], schema)

# Show the DataFrame
df.show(truncate=False)
df.printSchema()
```
### Find the median salary for each department 
```python

from pyspark.sql import functions as F
from pyspark.sql.window import Window
 
Sample Data

emp_data = [
 (1, 101, 60000),
 (2, 101, 65000),
 (3, 101, 70000),
 (4, 102, 55000),
 (5, 102, 60000),
 (6, 102, 62000),
 (7, 103, 70000),
 (8, 103, 75000),
 (9, 103, 80000),
]

department_data = [
 (101, 'Sales'),
 (102, 'HR'),
 (103, 'IT'),
]

emp_df = spark.createDataFrame(emp_data, ['emp_id', 'dept_id', 'salary'])
dept_df = spark.createDataFrame(department_data, ['dept_id', 'dept_name'])

windowSpec = Window.partitionBy('dept_id').orderBy('salary')

# Add row number and total count for each department
emp_with_rank = emp_df.withColumn('row', F.row_number().over(windowSpec))\
 .withColumn('row_desc', F.count('salary').over(windowSpec.rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)) - F.row_number().over(windowSpec))

median_df = emp_with_rank.groupBy('dept_id')\
 .agg(F.expr("percentile_approx(salary, 0.5)").alias('median_salary'))

result_df = median_df.join(dept_df, 'dept_id').select('dept_name', 'median_salary')

result_df.show()

```



https://books.japila.pl/

https://www.linkedin.com/posts/riyakhandelwal_functions-in-databricks-activity-7231638740463411200-SrwX 

https://www.waitingforcode.com/apache-spark-sql/mapgroupswithstate-batch/read

https://www.linkedin.com/company/apachespark/posts/

https://hudi.apache.org/blog/2024/07/11/what-is-a-data-lakehouse/

https://www.youtube.com/@nextgenlakehouse?app=desktop

Data Cleaning using PySpark 
https://www.linkedin.com/posts/shwetank-singh-68023283_data-engineering-101-data-cleaning-using-activity-7234225860797505536-xLad 

PySpark in 2023

https://www.databricks.com/blog/pyspark-2023-year-review

```
You can now query a PySpark DataFrame with SQL directly without creating a temporary table or view.

Just query the DataFrame with a named parameter and it automatically works.

This makes it much easier to seamlessly switch from the PySpark DSL => SQL,
which is an amazing quality-of-life improvement for hashtag#spark users.
Before named parameter support, users had to manually register temporary views/tables
which was an annoying extra step.
Now you can seamlessly run SQL on a DataFrame object.

![image](https://github.com/user-attachments/assets/90c1c5c9-6ab6-4a06-b474-36fb16640be8)



```
![image](https://github.com/user-attachments/assets/a3a96e7b-2b40-4f60-899e-011b0773500e)


### distinct() or dropDuplicates()
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("example").getOrCreate()

data = [(1, "A"), (2, "B"), (1, "A"), (3, "C")]
df = spark.createDataFrame(data, ["id", "value"])

df_distinct = df.distinct() # Removes duplicate rows based on all columns
df_distinct.show()
# +---+-----+
# | id|value|
# +---+-----+
# |  1|    A|
# |  2|    B|
# |  3|    C|
# +---+-----+

df_drop_duplicates = df.dropDuplicates(["id"]) # Removes duplicates based on specified columns
df_drop_duplicates.show()
# +---+-----+
# | id|value|
# +---+-----+
# |  1|    A|
# |  2|    B|
# |  3|    C|
# +---+-----+

spark.stop()
```

### DataFrame equality

https://www.databricks.com/blog/simplify-pyspark-testing-dataframe-equality-functions

Exciting update for PySpark developers! Spark 3.5/4.0 and Databricks Runtime 14.3. introduce DataFrame equality functions. Highlights:

✅ Simplifies comparing expected and actual DataFrames.
✅ Provides detailed discrepancy insights.
✅ Enhances error detection in early stages.

Two equality test functions for PySpark DataFrames were introduced in Apache Spark 3.5: assertDataFrameEqual and assertSchemaEqual. Let's take a look at how to use each of them.

#### assertDataFrameEqual: 
This function allows you to compare two PySpark DataFrames for equality, checking whether the data and schemas match.  
It returns descriptive information when there are differences.
```
df_expected = spark.createDataFrame(data=[("Alfred", 1500), ("Alfred", 2500), ("Anna", 
500), ("Anna", 3000)], schema=["name", "amount"])

df_actual = spark.createDataFrame(data=[("Alfred", 1200), ("Alfred", 2500), ("Anna", 500), 
("Anna", 3000)], schema=["name", "amount"])

from pyspark.testing import assertDataFrameEqual

assertDataFrameEqual(df_actual, df_expected)
```


#### assertSchemaEqual: This function compares only the schemas of two DataFrames; it does not compare row data.
```
schema_actual = "name STRING, amount DOUBLE"

data_expected = [["Alfred", 1500], ["Alfred", 2500], ["Anna", 500], ["Anna", 3000]]
data_actual = [["Alfred", 1500.0], ["Alfred", 2500.0], ["Anna", 500.0], ["Anna", 3000.0]]

df_expected = spark.createDataFrame(data = data_expected)
df_actual = spark.createDataFrame(data = data_actual, schema = schema_actual)

from pyspark.testing import assertSchemaEqual

assertSchemaEqual(df_actual.schema, df_expected.schema)
```
 

### How to to discard the NULL values in a PySpark array 

rather than write own logic to deal with them:

array_compact makes getting rid of NULL values quite easy.
![image](https://github.com/user-attachments/assets/311b2f0d-1cad-44f1-a643-a6bb56ce64f8)

https://asrathore08.medium.com/pyspark-code-snippets-part-i-e2baf37a2e4

https://asrathore08.medium.com/pyspark-code-snippets-part-ii-e24996ffff3c

https://towardsdatascience.com/4-examples-to-take-your-pyspark-skills-to-next-level-2a04cbe6e630


https://towardsdatascience.com/best-data-wrangling-functions-in-pyspark-3e903727319e

https://blog.devgenius.io/leveraging-sql-capabilities-in-pyspark-simplifying-big-data-analysis-ff63fcfc82f0

https://medium.com/@maitreemanna8002/pyspark-optimization-technique-for-better-performance-47a7bcd6a72e

https://medium.com/@Zakbasil/pyspark-performance-improvement-part-1-04a2e3bed7bd




### Add an increasing ID column starting in 1
```python
display(
    df
    .limit(100)
    .withColumn('ID', F.monotonically_increasing_id()+1 )
)
```
### Aggregate group by
``` python 
df = df.groupBy('gender').agg(F.max('age').alias('max_age_by_gender'))

df = df.groupBy('age').agg(F.collect_set('name').alias('person_names'))
```
### Get the aggregated values and list them in a new variable
```python
display(
    df.limit(50)
    .groupBy('cut')
    .agg( F.array_agg('price'))
)


df
.groupBy('cut')
.agg( F.count('cut').alias('n_count'), #count of obervations
      F.countDistinct('price').alias('distinct') ) #distinct n prices
      
df
.groupBy('cut')
.agg( F.sum('price').alias('total'),
          F.mean('price').alias('avg_price'),
          F.min('price').alias('min_price'),
          F.max('price').alias('max_price') 
)
```
#### COUNT_IF
```python
display(
    df
    .groupBy('cut')
    .agg( F.count_if( col('price') > 18000))
)
```

### Median
```python
    df
    .groupBy('cut')
    .agg( F.median('price').alias('median'),
     F.percentile('price', 0.5).alias('50th pct'))
```

#### Moving Average using expr()
```python
expression = """
mean(sales_qty) over (partition by store_id, product_id order by date 
rows between 2 preceding and current row)
"""

sub_df = (
    sub_df
    .withColumn("moving_avg", F.round(F.expr(expression), 2))
)
```
#### String split()
```python
 display( df
        .select( col('carat').cast('string'))
        .select( F.split('carat', '\.')[0],
                 F.split('carat', '\.')[1] ) 
        )

```
#### Moving Average
```python
window = (
    Window
    .partitionBy("store_id", "product_id")
    .orderBy("date")
    .rowsBetween(-2, Window.currentRow)
)

# calculate mean over the window
sub_df = (
    sub_df
    .withColumn("moving_avg", F.round(F.mean("sales_qty").over(window), 2))
)
```
#### Explode array
```python

from pyspark.sql.functions import explode
data = [("Alice", [1, 2, 3]), ("Bob", [4, 5]), ("Charlie", [6])]
df = spark.createDataFrame(data, ["name", "numbers"])
# explode the numbers column
df_exploded = df.select("name", explode("numbers").alias("number"))
```
### Pivot 
```python
data = [("Alice", "apples", 10), ("Alice", "oranges", 5),
        ("Bob", "apples", 7), ("Bob", "oranges", 3),
        ("Charlie", "apples", 2), ("Charlie", "oranges", 1)]
df = spark.createDataFrame(data, ["name", "fruit", "quantity"])

# pivot the fruit column
df_pivoted = df.groupBy("name").pivot("fruit", ["apples", "oranges"]).agg(sum("quantity"))
```
###  Array
 
from pyspark.sql import functions as F, types as T

#### Column Array - F.array(*cols)
df = df.withColumn('full_name', F.array('fname', 'lname'))

#### Empty Array
df = df.withColumn('empty_array_column', F.array([]))

##### Get element at index
df = df.withColumn('first_element', F.col("my_array").getItem(0))

#### Array Size/Length
df = df.withColumn('array_length', F.size('my_array'))

#### Flatten Array
df = df.withColumn('flattened', F.flatten('my_array'))

##### Unique/Distinct
df = df.withColumn('unique_elements', F.array_distinct('my_array'))

##### Map over & transform array elements
# ["This", "is", "very", "verbose"] -> [4, 2, 4, 7]
df = df.withColumn("len_col", transform("array_col", lambda x: length(x)))

# Explode & collect
```python
from pyspark.sql.functions import explode, length, collect_list
df = df.withColumn("col_temp", explode("array_col")).withColumn("len_col_temp", length("col_temp"))
   .groupBy("unique_id").agg(collect_list("len_col_temp").alias("len_col")
```

### Window functions
https://towardsdatascience.com/5-examples-to-master-pyspark-window-operations-26583066e227

https://sairamdgr8.medium.com/acing-apache-spark-dataframes-interview-questions-series-using-pyspark-with-window-functions-4a38e6f80d19
```python
from pyspark.sql.window import Window
from pyspark.sql.functions import col, row_number, rank, dense_rank, lead,lag, percent_rank, ntile, mean
from pyspark.sql import functions as f

spark = SparkSession.builder.appName('Spark_window_functions').getOrCreate()
emp_df = spark.read.csv(r'emp.csv',header=True,inferSchema=True) 
emp_df.show(10)

win_func = Window.partitionBy(emp_df['DEPTNO']).orderBy(emp_df['SAL'].desc()) 

emp_df.withColumn('rank',row_number().over(win_func)).show()

# Equivalent SQL
# select e.*, row_number() over(partition by deptno order by sal desc) rank from emp e) rk 


win = Window.partitionBy(df1['channel_code']).orderBy(df1['sum_spent'].desc())

revenue_difference = (df1['sum_spent']-lead(df1['sum_spent']).over(win))
df1.select(df1['channel_code'],df1['prod_code'],
            df1['sum_spent'],revenue_difference.\ 
            alias('spent_diff_lead')).show(truncate=False)
            
winrow = Window.partitionBy(df1['channel_code']) \
                         .orderBy(df1['sum_spent'].desc()) \
                         .rowsBetween(Window.unboundedPreceding, 
                                              Window.currentRow)
revenue_difference =(f.max(df1['sum_spent']).over(winrow)-df1['sum_spent'])
df1.select(df1['channel_code'],df1['prod_code'],
              df1['sum_spent'],revenue_difference \
              .alias("spend_difference")).show(truncate=False)

winra=Window.partitionBy(df1['channel_code']) \
                        .orderBy(df1['sum_spent'].desc()) \
                        .rangeBetween(Window.unboundedPreceding,
                                       Window.currentRow) 
revenue_difference =(f.max(df1['sum_spent']).over(winra)-df1['sum_spent'])
df1.select(df1['channel_code'],df1['prod_code'],df1['sum_spent'],
             revenue_difference.alias("spend_difference")) \
             .show(truncate=False)
```

### Implementing Pyspark Real Time Application || End-to-End Project 

https://www.youtube.com/watch?v=wFOojyYvLRE

https://habr.com/ru/articles/765188/  Feature eng and cluster analysis 

https://towardsdatascience.com/did-you-know-this-in-spark-sql-a7398bfcc41e

### Books

https://www.amazon.com/Advanced-Analytics-PySpark-Patterns-Learning/dp/1098103653

https://www.amazon.com/Analysis-Python-PySpark-Jonathan-Rioux/dp/1617297208/

https://www.amazon.com/Data-Algorithms-Spark-Recipes-Patterns/dp/1492082384

https://runawayhorse001.github.io/LearningApacheSpark/pyspark.pdf


https://www.amazon.com/dp/1804612987 Causal Inference and Discovery in Python: Unlock the secrets of modern causal machine learning with DoWhy, EconML, PyTorch and more


https://www.youtube.com/watch?v=jWZ9K1agm5Y  PySpark Course: Big Data Handling with Python and Apache Spark

### Find the Highest & Lowest Salaried Employee in each Department
```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import min,max,col,rank,desc
from  pyspark.sql.window import Window
from pyspark.sql.types import *

spark=SparkSession.builder.appName("min_max").getOrCreate()
# finding the max salary
window_spec_1=Window.partitionBy("emp_dep_id").orderBy(desc("salary"))
df_1=df.withColumn("rnk",rank().over(window_spec_1))
df_1=df_1.filter(col("rnk") == 1)
df_1=df_1.withColumnRenamed("emp_name","emp_max_salary")

# finding the min salary
window_spec_2=Window.partitionBy("emp_dep_id").orderBy(("salary"))
df_2=df.withColumn("rnk",rank().over(window_spec_2))
df_2=df_2.filter(col("rnk") == 1)
df_2=df_2.withColumnRenamed("emp_name","emp_min_salary")
df_2=df_2.withColumnRenamed("emp_dep_id","emp_min_dep_id")


# final df
final_df=df_1.join(df_2,df_1.emp_dep_id == df_2.emp_min_dep_id,'inner')
final_df.select("emp_dep_id","emp_max_salary","emp_min_salary").display()
```
### Compute  total counts of each of  unique words on a spark: map() and flatMap()
```python
sc.textFile(“hdfs://user/bigtextfile.txt”);
def toWords(line):
      return line.split()

words = lines.flatMap(toWords)     We are going to flatMap instead of the map because our function is returning multiple values.

def toTuple(word):
     return (word, 1)

wordsTuple = words.map(toTuple)

def sum(x, y):
   return x+y

counts = wordsTuple.reduceByKey(sum)
```

### JOIN
 
When you join dataframes with the same column name, the resultant frame contains all columns from both DataFrames.   
We will end up with duplicate columns.  
To get a join result with out duplicate you have to use:

  
empDF.join(deptDF,["dept_id","branch_id"]).show()
 
https://sparkbyexamples.com/pyspark/pyspark-join-explained-with-examples/

https://sparkbyexamples.com/pyspark/pyspark-join-multiple-columns/

# PySpark join multiple columns syntax 1
```python
empDF.join(deptDF, (empDF["dept_id"] == deptDF["dept_id"]) &
   ( empDF["branch_id"] == deptDF["branch_id"])).show()
```
# PySpark join multiple columns syntax 2 using where  or filter:
```python
empDF.join(deptDF).where((empDF["dept_id"] == deptDF["dept_id"]) &
    (empDF["branch_id"] == deptDF["branch_id"])).show()
```

### F.lit and union example
```python

yesterday_df = spark.createDataFrame([
 (1,"hulu","90046"),
 (2,"hulu+disney" ,"90026"),
 (3,"hulu+disney" ,"90026")],
 ["user_id", "product_name","zip_code"])

 today_df = spark.createDataFrame([
 (1,"hulu+disney","90046"),
 (2,"hulu+disney" ,"90036"),
 (4,"hulu+disney" ,"90026")],
 ["user_id", "product_name","zip_code"])

import pyspark.sql.functions as F

df_old = yesterday_df.withColumn('date',F.lit("10/26"))
df_new = today_df.withColumn('date',F.lit("10/27"))
df_new.show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      1| hulu+disney|   90046|10/27|
|      2| hulu+disney|   90036|10/27|
|      4| hulu+disney|   90026|10/27|
+-------+------------+--------+-----+

df_new.union(df_old).show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      1| hulu+disney|   90046|10/27|
|      2| hulu+disney|   90036|10/27|
|      4| hulu+disney|   90026|10/27|
|      1|        hulu|   90046|10/26|
|      2| hulu+disney|   90026|10/26|
|      3| hulu+disney|   90026|10/26|
+-------+------------+--------+-----+


```

### INNER JOIN with renaming columns to avoid column names duplications:
```python
df_new.join(df_old, df_old.user_id == df_new.user_id, "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
).show()

+-------+----------------+----------------+------------+------------+----------+--------+
|user_id|old_product_name|new_product_name|old_zip_code|new_zip_code|start_date|end_date|
+-------+----------------+----------------+------------+------------+----------+--------+
|      1|            hulu|     hulu+disney|       90046|       90046|     10/26|   10/27|
|      2|     hulu+disney|     hulu+disney|       90026|       90036|     10/26|   10/27|
+-------+----------------+----------------+------------+------------+----------+--------+

df_inner = df_new.join(df_old, df_old.user_id == df_new.user_id, "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
)


df_new.join(df_old,
(df_old.user_id == df_new.user_id) , "inner").show()
```
### Find records with same id but different zip code or product_name:
```python
df_new.join(df_old,
(df_old.user_id == df_new.user_id) &
((df_old.product_name != df_new.product_name)  | (df_old.zip_code != df_new.zip_code )) , "inner").show()

df_inner_2 = df_new.join(df_old,
(df_old.user_id == df_new.user_id) &
((df_old.product_name != df_new.product_name) | (df_old.zip_code != df_new.zip_code )), "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
)

df_new.join(df_old, df_old.user_id == df_new.user_id , "inner").select(
df_old.user_id,
df_old.product_name,
df_old.zip_code,
df_old.date.alias("start_date"),
df_new.date.alias("end_date")
).show()


df_inner_2 = df_new.join(df_old,
(df_old.user_id == df_new.user_id) &
((df_old.product_name != df_new.product_name) | (df_old.zip_code != df_new.zip_code )), "inner").select(
 df_old.user_id,
 df_old.product_name.alias("old_product_name"),
 df_new.product_name.alias("new_product_name"),
 df_old.zip_code.alias("old_zip_code"),
 df_new.zip_code.alias("new_zip_code"),
 df_old.date.alias("start_date"),
 df_new.date.alias("end_date")
)

```
### Find records which exists in both  dfs and product_name and zip_code are the same:
 this syntax will eliminate duplicate column names
```python
df_new.join(df_old,["user_id","product_name","zip_code"]).show()

df_exact_match = df_new.join(df_old,["user_id","product_name","zip_code"])
```
### Find records with same id but different zip code or product_name:
```
step 1:

df_common_user_id = df_new.join(df_old, df_old.user_id == df_new.user_id , "inner").show()

step 2: remove exact match:

df_dup = df_common_user_id.join(df_exact_match , df_common_user.user_id == df_exact_match.user_id, "leftanti")

df_dup = df_common_user_id.join(df_exact_match , ["user_id"], "leftanti")
```
### Leftanti returns records which exists in left only
```
df_old.join(df_new, df_old.user_id == df_new.user_id, "leftanti").show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      3| hulu+disney|   90026|10/26|
+-------+------------+--------+-----+

df_new.join(df_old, df_old.user_id == df_new.user_id, "leftanti").show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      4| hulu+disney|   90026|10/27|
+-------+------------+--------+-----+

df_new_anti = df_new.join(df_old, df_old.user_id == df_new.user_id, "leftanti")
df_old_anti = df_old.join(df_new, df_old.user_id == df_new.user_id, "leftanti")
df_new_anti.union(df_old_anti).show()
+-------+------------+--------+-----+
|user_id|product_name|zip_code| date|
+-------+------------+--------+-----+
|      4| hulu+disney|   90026|10/27|
|      3| hulu+disney|   90026|10/26|
+-------+------------+--------+-----+
```


### In a very huge text file  check if a particular keyword exists.
```
result = “Not Set”
lock = threading.Lock()
accum = sc.accumulator(0)

def map_func(line):
    #introduce delay to emulate the slowness
    sleep(1);
    if line.find(“Adventures”) > -1:
              accum.add(1);
             return 1;
    return 0;

def start_job():
    global result
    try:
        sc.setJobGroup(“job_to_cancel”, “some description”)

        lines = sc.textFile(“hdfs://hadoop1.knowbigdata.com/user/student/sgiri/wordcount/input/big.txt”);

         result = lines.map(map_func);
         result.take(1);
         except Exception as e:
                  result = “Cancelled”
lock.release()

def stop_job():
    while accum.value < 3 :
          sleep(1);
          sc.cancelJobGroup(“job_to_cancel”)
          supress = lock.acquire()
          supress = thread.start_new_thread(start_job, tuple())
          supress = thread.start_new_thread(stop_job, tuple())
          supress = lock.acquire()
```

### UDF pandas

https://towardsdatascience.com/pyspark-or-pandas-why-not-both-95523946ec7c

https://medium.com/@suffyan.asad1/an-introduction-to-pandas-udfs-in-pyspark-a0a512bd00e2


### Update Dataframe
```python
import pyspark.sql.functions as F
from pyspark.sql.functions import col, when 
path= "s3://b2c-prod-dca-model-evaluate/oss/MPS_APPIQ_TAXONOMY_WEIGHTS_DS/version=0.3/"
aio_weights = spark.read.parquet(path)
updated_weights = aio_weights.withColumn("revenue_weight",
                 when(col("genre_id") == 2012, 0)
                .when(col("genre_id") == 2009004, 1)
                .otherwise(col("revenue_weight"))
              )  
aio_weights.printSchema()
updated_weights.printSchema()


version="1.1.0"
updated_weights = updated_weights.withColumn("version",F.lit(version))
new_path = "s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS"

updated_weights.write.format("delta").partitionBy("version").save(new_path)
```

### StructType 
 
StructType() constructor takes list of StructField, 
StructField takes a fieldname and type of the value.

### MapType
https://sparkbyexamples.com/pyspark/pyspark-maptype-dict-examples/


```python
from pyspark.sql.types import StructField, StructType, StringType, MapType
schema = StructType([
    StructField('name', StringType(), True),
    StructField('properties', MapType(StringType(),StringType()),True)
])

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
dataDictionary = [
        ('James',{'hair':'black','eye':'brown'}),
        ('Michael',{'hair':'brown','eye':None}),
        ('Robert',{'hair':'red','eye':'black'}),
        ('Washington',{'hair':'grey','eye':'grey'}),
        ('Jefferson',{'hair':'brown','eye':''})
        ]
df = spark.createDataFrame(data=dataDictionary, schema = schema)
print(df.schema)
df.printSchema()
 |-- name: string (nullable = true)
 |-- properties: map (nullable = true)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)

df.show(truncate=False)

## let read the same data without specifying schema:
df2 = spark.createDataFrame(data=dataDictionary)
print(df2.schema)
StructType([StructField('_1', StringType(), True), StructField('_2', MapType(StringType(), StringType(), True), True)])

df2.printSchema()
 |-- _1: string (nullable = true)
 |-- _2: map (nullable = true)
 |    |-- key: string
 |    |-- value: string (valueContainsNull = true)
 

```

### Explode
Explode properties column: will generate 2 columns: key and value
```python
from pyspark.sql.functions import explode
df.select(df.name,explode(df.properties)).show()

#  Get only keys:
from pyspark.sql.functions import map_keys
df.select(df.name,map_keys(df.properties)).show()

# Get only values:
from pyspark.sql.functions import map_values
df.select(df.name,map_values(df.properties)).show()


data = [(1, "John",  ["shirt", "shoes", None]),
        (2, "Alice", ["book", None])]
df = spark.createDataFrame(data, ["id", "name", "purchases"])
# Explode the "purchases" array
df_exploded = df.select(df.id, df.name, explode(df.purchases))
# Output
df_exploded.show()
+---+-------+----------+
| id| name  | purchases|
+---+-------+----------+
| 1 | John  | shirt    |
| 1 | John  | shoes    |
| 1 | John  | null     |
| 2 | Alice | book     |
| 2 | Alice | null     |
+---+-------+----------+

While PySpark explode() caters to all array elements, PySpark explode_outer() specifically focuses on non-null values.  
It ignores empty arrays and null elements within arrays, resulting in a potentially smaller dataset.

from pyspark.sql.functions import explode_outer
# Using explode_outer
df_exploded_outer = df.select(df.id, df.name, explode_outer(df.purchases))
# Output
df_exploded_outer.show()
+---+-------+----------+
| id| name  | purchases|
+---+-------+----------+
| 1 | John  | shirt    |
| 1 | John  | shoes    |
| 2 | Alice | book     |
+---+-------+----------+

split(): Split strings into lists based on delimiters.
posexplode(): Explode arrays and add a column indicating the original position of each element.
arrays_zip(): Combine multiple arrays into a single array of tuples.
```

### JSON schema

```
new_json="""{
 "contentID": { "S": "s-para"}
 }
"""
print(new_json)

# Read without schema:
df = spark.read.json(sc.parallelize([new_json]))
df.show()
df.printSchema()

print(df.schema)
The printed schema can be used "as is" to define the schema:

# Read with schema:
contentID_schema=StructType([
        StructField("S", StringType(), True)
])

beehive_schema = StructType([
   StructField("contentID", contentID_schema ,True)
])

df2 = spark.read.schema(beehive_schema).json(sc.parallelize([new_json]))
df2.printSchema()
root
 |-- contentID: struct (nullable = true)
 |    |-- S: string (nullable = true)

df2.show(truncate=False)

```
### получение медианы для каждой группы данных

```
# Pandas
df.groupby("col1")["col2"].median()

# PySpark
from pyspark.sql import Window
import pyspark.sql.functions as F

med_func = F.expr('percentile_approx(col2, 0.5, 20)')
df.groupBy('col1').agg(med_func).show()

```

### Window function to calculate sum and cumulative

```python
from pyspark.sql import Window
from pyspark.sql.functions import sum
l = [
  (1, 10, '2020-11-01'), 
  (1, 30, '2020-11-02'), 
  (1, 50, '2020-11-03')
]
df = spark.createDataFrame(l,['user_id', 'price', 'purchase_date'])
w1 = Window().partitionBy('user_id')
w2 = Window().partitionBy('user_id').orderBy('purchase_date')
(
  df
  .withColumn('total_expenses', sum('price').over(w1))
  .withColumn('cumulative_expenses', sum('price').over(w2))
).show()
+-------+-----+-------------+--------------+-------------------+
|user_id|price|purchase_date|total_expenses|cumulative_expenses|
+-------+-----+-------------+--------------+-------------------+
|      1|   10|   2020-11-01|            90|                 10|
|      1|   30|   2020-11-02|            90|                 40|
|      1|   50|   2020-11-03|            90|                 90|
+-------+-----+-------------+--------------+-------------------+

```


#### check_uniq in dataframe

```
+    def _check_uniq(df, msg):
+        cols = [ 'date', 'product_id', 'unified_product_id', 'country_code', 'device_code',
+                'market_code', 'genre_id']
+        logger.info(msg + " check_uniq total records=" + str(df.count()))
+        for c in cols:
+            if c not in df.columns:
+                logger.info("ERROR " + c + " not in " + str(df.columns))
+
+        df_gr = df.groupBy(*cols).count().filter(F.col('count') > 1)
+        cnt = df_gr.count()
+        if cnt > 0:
+            logger.info(msg + " check_uniq failed number of non-uniq keys= " + str(cnt))
+            logger.info(df_gr.limit(10).toPandas().to_string(index=False))
+        else:
+            logger.info(msg + " check_uniq OK")
+
```


### Partitions

https://habr.com/ru/company/otus/blog/686142/

### Skew joins
https://habr.com/ru/company/first/blog/678826/


/opt/homebrew/bin/pyspark


### Show verically (useful for wide table)
```
fname="/FileStore/uploads/reviews_20220822_hour_23/20600000009072.gz"
df = spark.read.options(header='False', inferSchema='True', delimiter='\t').schema(schema).csv(fname) 
df.show(n=3, truncate=250, vertical=True)
```

### For left join  find which join column doesn not have match
```
    df = df.join(df_genre_weights, on=["genre_id"], how="left")
    df_missing_genres = df.select('genre_id').filter(F.col("downloads_weight").isNull()).distinct().collect()
    missing_genres = [v['genre_id'] for v in df_missing_genres]

    print("missing genres =" + str(missing_genres))
```    
    
### Dataframe
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.html

pdf = df.toPandas()

### Pandas Dataframe to string
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html

panda_df.to_string()  -- accepts arg to print index:

print(df.select(F.count(F.when(F.isnan(c) | F.col(c).isNull(),c)).alias(c)).toPandas().to_string(index=False))  

Use limit:
df.limit(3).toPandas().to_string(index=False)


### Reading parquet and delta files
```
path="s3://aardvark-prod-dca-data/fact/APP_TOTAL_REVENUE/range_type=WEEK/date=2012-01-14/" 
df=spark.read.parquet(path)

df = spark.read.format(“delta”).load(path)

df.display()
```

### createOrReplaceTempView
https://spark.apache.org/docs/3.1.3/api/python/reference/api/pyspark.sql.DataFrame.createOrReplaceTempView.html
```
df=spark.read.format("delta").load("s3://aardvark-prod-dca-data/fact/APP_TOTAL_REVENUE/range_type=WEEK/")
df.createOrReplaceTempView("weekly_table")
spark.sql(SQL).show(55)
```
### print schema without show()
```
schema = df._jdf.schema().treeString()
print(schema)
```

### Group by
```python
df.filter(df.colname == 50.0).groupBy('another_colname').count().show()
from pyspark.sql.functions import avg

df.groupBy("category").agg(avg("sales")).show()
```


#### groupBy, sum, agg
```python
df.groupBy('genre_id').agg(
 F.sum( (F.col('monetization_score').isNull()).cast('int') ).alias('monetization_null_count'),
 F.sum( (F.col('monetization_score').isNotNull()).cast('int') ).alias('monetization_NOT_null_count'),   
).orderBy('genre_id').show(40)
```

#### GROUP BY HAVING COUNT() > 1


```python
df.groupBy(*cols).count().show()

df.groupBy(*cols).count().filter(F.col('count')>1).show()
```

### Question: how to convert this to PySpark?

```sql
sqlContext.sql("
select Category,count(*) as count from hadoopexam
where HadoopExamFee < 3200  
group by Category
having count>10
")
```
### Answer to question above:
```python
from pyspark.sql.functions import *

df.filter(df.HadoopExamFee<3200)
  .groupBy('Category')
  .agg(count('Category').alias('count'))
  .filter(col('count')>10)
```

### Generic answer:
```
df.groupBy(someExpr).agg(somAgg).where(somePredicate) 
```
### Get value from the df with single row and col:
```
df = spark.sql('select count(1) as count_check from schema.table')
value = df.collect()[0][0]
```
### head() vs first()
DataFrame.head(n=None)   (default - return 1 row)
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.head.html
```
df.head()
Row(age=2, name='Alice')
df.head(1)
[Row(age=2, name='Alice')]
```

```
df.first()
Row(age=2, name='Alice')
```
https://spark.apache.org/docs/3.1.1/api/python/reference/api/pyspark.sql.DataFrame.first.html


### Infinity:
```
def _replace_infs(c, v):
        is_infinite = c.isin(
            [
                F.lit("+Infinity").cast("float")
                , F.lit("-Infinity").cast("float")
            ]
        )
return F.when(c.isNotNull() & is_infinite, v).otherwise(c)
        
        
df = df.withColumn(
                s, self._replace_infs(F.col(s), F.lit(None))
)         
```
### Expression
https://www.nbshare.io/notebook/374005461/Pyspark-Expr-Example/
```python
from pyspark.sql.functions import (col, expr)
# here we update the column "Classify" using the CASE expression. 
# The conditions are based on the values in the Salary column
modified_df = df.withColumn("Classify", 
    expr("CASE WHEN Salary < 5000 THEN 1 "+
               "WHEN Salary < 10000 THEN 2 " +
                "ELSE 3 " + 
           END")
    )
    
modified_df = df.withColumn("New_Salary", expr("Salary + 500"))    

```

### JOIN

https://dzone.com/articles/pyspark-join-explained-with-examples

https://insaid.medium.com/eda-with-pyspark-1f29b7d1618

https://stackoverflow.com/questions/39067505/pyspark-display-a-spark-data-frame-in-a-table-format


### Example: F.expr, any(), head(), lit(), cast(), check for nulls

```python
        for col in df.columns:
            has_nulls = f"any({col} is null)"
            if df.select(F.expr(has_nulls)).head()[0]:
                df = df.withColumn(f"{col}_uniform_scaled", F.lit(None).cast("double"))
            else:
                ...
```


### Columns with nulls

https://stackoverflow.com/questions/37262762/filter-pyspark-dataframe-column-with-none-value

https://sparkbyexamples.com/pyspark/pyspark-find-count-of-null-none-nan-values/

```
import numpy as np
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()
data = [
    ("James","CA",np.NaN), ("Julia","",None),
    ("Ram",None,200.0), ("Ramya","NULL",np.NAN)
]
df =spark.createDataFrame(data,["name","state","number"])
df.show()


from pyspark.sql.functions import col,isnan, when, count
df.select(
         [
            count(when(isnan(c) | col(c).isNull(), c)).alias(c) for c in df.columns
         ]
   ).show()
   
   
 ### printing via toPandas()  
 print(df.select(F.count(F.when(F.isnan(c) | F.col(c).isNull(),c)).alias(c)).toPandas().to_string(index=False))  
   
```


### ANY
Pandas has ANY :
https://sparkbyexamples.com/pandas/pandas-check-if-any-value-is-nan-in-a-dataframe/

 PySpark has ANY - it  can check if any value of a column meets a condition.
 
```
from pyspark.sql import functions as F

data = [[1,2,3],[None, 5, 6], [7, None, 9]]
df = spark.createDataFrame(data, schema=["col1", "col2", "col3"])

cols = [f"any({col} is null) as {col}_contains_null" for col in df.columns]

df.selectExpr(cols).show()
```

### CSV

```python
from pyspark.sql.types import *

csv_schema = StructType(
   [   
       StructField('id', IntegerType(), True),
       StructField('genre_id', LongType(), True),
       StructField('downloads_weight', DoubleType(), True),
       StructField('mps_total_downloads_weight', DoubleType(), True),
       StructField('revenue_weight', DoubleType(), True),
       StructField('mps_total_revenue_weight', DoubleType(), True),
       StructField('mps_monetization_sov_weight', DoubleType(), True),
       StructField('rau_weight', DoubleType(), True),
       StructField('afu_weight', DoubleType(), True),
       StructField('adu_weight', DoubleType(), True),
       StructField('atu_weight', DoubleType(), True),
       StructField('ris_weight', DoubleType(), True),
       StructField('incremental_ratings_average_weight', DoubleType(), True),
       StructField('cumulative_ratings_average_weight', DoubleType(), True),
       StructField('cumulative_rating_count_weight', DoubleType(), True),
       StructField('incremental_rating_count_weight', DoubleType(), True)
   ]
)      
fname="file:/dbfs/FileStore/uploads/mlubinsky/20220728_mps_weights.csv"

df_csv = spark.read.option("header",True).option("delimiter",",").schema(csv_schema).csv(fname)

df_ordered=df_csv.select("genre_id","downloads_weight","mps_total_downloads_weight","revenue_weight")
```

### CLEAR

aws s3 rm --recursive s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS

### DELTA
```python
### WRITE
import pyspark.sql.functions as F
path = "s3://aardvark-prod-dca-data/oss/MPS_APPIQ_TAXONOMY_WEIGHTS/"
df_ordered.withColumn("version", F.lit("1.0.0")).write.partitionBy("version").format("delta").save(path)

###   READ
from bdp.common.spark.spark_utils import load_as_spark_df
genre_params={"version":"1.0.0"}
df_genre_weights = load_as_spark_df(spark, "MPS_APPIQ_TAXONOMY_WEIGHTS_O", genre_params)


```

Problem with duplicated columns:
```
df = spark.createDataFrame(
    [
        (1, 2, 3, 4, 5 ,6 , 7 ,8 , 9),   
    ],
    ["universal_app_id", "country_code", "product_id", "platform", "device_type", "range_type", "date", "app_name", "total_downloads"]
)

df_unified_totals = spark.createDataFrame(
    [ 
        (1, 2),   
    ],
    ["universal_app_id", "country_code"]
)

dim_cats = spark.createDataFrame(
        [
        (1, 2, 3, 4, 5),  
        (10, 20, 30, 40, 50),
    ],
    ["dim_legacy_category_id", "dim_id", "dim_platform", "dim_category_id", "dim_unified_category_id"]
)  

import pyspark.sql.functions as F   
df = df.join(
            df_unified_totals, on=["universal_app_id", "country_code"]
)

df = (
            df.alias("a")
            .join(
                dim_cats.alias("b"),
                [(F.col("a.product_id") == F.col("b.dim_id"))],
                "left",
            )
            .select("a.*", "b.dim_unified_category_id")
)
print("Step 3")
for c in df.columns:
    print(c)
```
Result:
```
universal_app_id
country_code
universal_app_id
country_code
product_id
platform
device_type
range_type
date
app_name
total_downloads
dim_unified_category_id
```

### https://towardsdatascience.com/2-silent-pyspark-mistakes-you-should-be-aware-of-de52c3a188c4
```
Let’s say we have a dataset with millions of rows.
We make a mistake in calculating the sales quantities.
Then, we create aggregate features based on the sales quantities such as weekly total,
 the moving average of the last 14 days, and so on.
 These features are used in a machine learning model that predicts the demand in the next week.

We evaluate the predictions and find out the accuracy is not good enough.
Then, we spend lots of time trying different things to improve the accuracy such as feature engineering or hyperparameter tuning.
 These strategies don’t have a big impact on the accuracy because the problem is in the data.

This is a scenario that we may encounter when working with large datasets.
In this article, we’ll go over two specific PySpark mistakes that might cause unexpected results.
For those who haven’t used PySpark yet, it is the Python API for Spark,
which is an analytics engine used for large-scale data processing.

We’ll create a small dataset for a few rows and columns.
It’s enough to demonstrate and explain the two cases we’ll cover. Both are applicable to much larger datasets as well.
```
```python
from pyspark.sql import SparkSession
from pyspark.sql import Window, functions as F

# initialize spark session
spark = SparkSession.builder.getOrCreate()

# create a spark dataframe using a list of dictionaries
data = [
    {"group_1": 'A', "group_2": 104, "id": 1211},
    {"group_1": 'B', "group_2": None, "id": 3001},
    {"group_1": 'B', "group_2": 105, "id": 1099},
    {"group_1": 'A', "group_2": 124, "id": 3380}
]

df = spark.createDataFrame(data)

# display the dataframe
df.show()

# output
+-------+-------+----+
|group_1|group_2|  id|
+-------+-------+----+
|      A|    104|1211|
|      B|   NULL|3001|
|      B|    105|1099|
|      A|    124|3380|
+-------+-------+----+
The DataFrame contains 4 rows and 3 columns and there is a missing value (i.e. NULL) in the second row of the second column.

1. concat and concat_ws
The concat and concat_ws functions are used for concatenating (i.e. combining) string columns.  
There is a small difference between them in the case of having Null values. We need to take it into consideration.
 Otherwise, the result of the concatenation operation might be misleading.

Let’s first use the concat function to combine the group_1 and group_2 columns to create a new column called group .

df = df.withColumn("group", F.concat("group_1", "group_2"))

df.show()

# output
+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211| A104|
|      B|   NULL|3001| NULL|
|      B|    105|1099| B105|
|      A|    124|3380| A124|
+-------+-------+----+-----+
Everything seems ok except for the second row. The group_2 value is null, which causes the group value to be null as well.

The output of the concat function is null if any of the concatenated values is null.

This is not the ideal behavior. If we only have the first group info,
then we’d except the group value to be equal to that value (i.e. “B”).
Just because we don’t have the subgroup info, we don’t want to lose information about the first level grouping.

In such cases, it’s better to use the concat_ws function. Let’s try it.

df = df.withColumn("group", F.concat_ws("group_1", "group_2"))

df.show()

# output
+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211|  104|
|      B|   NULL|3001|     |
|      B|    105|1099|  105|
|      A|    124|3380|  124|
+-------+-------+----+-----+
This is not the output we expect. The second row of the group column is empty,
which is not very different from having a null value. Also, the other group values are also wrong. This is worse than what the concat function did.

To solve this problem, we just need to specify a separator.
If we don’t need a character between groups, we can just provide an empty string as a separator.

df = df.withColumn("group", F.concat_ws("", "group_1", "group_2"))

df.show()

# output
+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211| A104|
|      B|   NULL|3001|    B|
|      B|    105|1099| B105|
|      A|    124|3380| A124|
+-------+-------+----+-----+
Now, the output is just as we expect.

2. Conditional column creation
Consider we want to create a new column based on the values in other columns. In PySpark, we can use the when function for this task.  
In the case of multiple conditions, we can chain the when functions and conclude with the otherwise function.

The order of conditions matter in some cases. It’s best explained with an example so let’s get to it.

We have the following DataFrame:

+-------+-------+----+-----+
|group_1|group_2|  id|group|
+-------+-------+----+-----+
|      A|    104|1211| A104|
|      B|   NULL|3001|    B|
|      B|    105|1099| B105|
|      A|    124|3380| A124|
+-------+-------+----+-----+
We want to create a dummy column according to the following conditions:

If group 1 is A, it is 100
If group 1 is A and group 2 is 124, it is 200
Otherwise it is 300
Using the when and otherwise functions, we can create this dummy column as follows:

df = df.withColumn(
    "dummy",
    F.when(F.col("group_1")=="A", 100)\
    .when(((F.col("group_1")=="A") & (F.col("group_2")=="124")), 200)\
    .otherwise(300)
)

df.show()

# output
+-------+-------+----+-----+-----+
|group_1|group_2|  id|group|dummy|
+-------+-------+----+-----+-----+
|      A|    104|1211| A104|  100|
|      B|   NULL|3001|    B|  300|
|      B|    105|1099| B105|  300|
|      A|    124|3380| A124|  100|
+-------+-------+----+-----+-----+
The output is not exactly correct. The last row fits the second condition (group 1 is A and group 2 is 124) so the value in the dummy column should be 200.

The reason for this problem is the order of conditions. Since we write the condition group_1=="A" before a more specific (or sub) condition group_1=="A" & group_2=="124" ,  
the latter is kind of ignored.

If we switch these two conditions, the output will actually be correct.

df = df.withColumn(
    "dummy",
    F.when(((F.col("group_1")=="A") & (F.col("group_2")=="124")), 200)\
    .when(F.col("group_1")=="A", 100)\
    .otherwise(300)
)

df.show()

# output
+-------+-------+----+-----+-----+
|group_1|group_2|  id|group|dummy|
+-------+-------+----+-----+-----+
|      A|    104|1211| A104|  100|
|      B|   NULL|3001|    B|  300|
|      B|    105|1099| B105|  300|
|      A|    124|3380| A124|  200|
+-------+-------+----+-----+-----+
Now the last value of the dummy column is 200, which is correct.

This is hard to notice when working with larger datasets. But, it might have a big impact on the downstream tasks. The output might be completely wrong. Thus, we should always pay attention to the order of conditions in such cases.

Final words
Data cleaning and processing are very important steps in a workflow as they affect downstream processes. A small mistake we make in these steps might lead to erroneous results.

Be aware of silent mistakes that do not raise an error but have the potential to fail your model or product.
```
### Catalyst Optimizer in PySpark
```


The Catalyst Optimizer in PySpark is a query optimization engine that enhances the performance of Spark SQL queries and DataFrame operations.  
Developed as a part of Spark SQL, it leverages advanced optimization techniques to generate efficient execution plans, enabling faster query processing across distributed data.

🚀 Key Roles of the Catalyst Optimizer:

✅ Logical Plan Optimization:
The Catalyst Optimizer starts by creating a logical plan for the query, which represents what needs to be computed without focusing on how to compute it. The optimizer then applies various transformations, like predicate pushdown, and pruning, to streamline the logical plan and eliminate redundant computations.

✅ Physical Plan Optimization:
Once the logical plan is optimized, Catalyst generates multiple physical plans, representing different ways of executing the query. It then evaluates these plans and selects the most efficient one based on factors such as data distribution, partitioning, and resource requirements.

✅ Column Pruning:
Catalyst optimizes queries by pruning unnecessary columns, so only the required columns are read and processed. This reduces I/O operations and improves query performance, especially when working with wide tables or large datasets.

✅ Predicate Pushdown:
Catalyst pushes down filter conditions as close to the data source as possible. This means that filtering is done at the data source level (such as in Parquet files or databases) rather than after loading data into memory, which reduces the amount of data Spark needs to process.

✅ Cost-Based Optimization (CBO):
With CBO, the Catalyst Optimizer uses statistics about data (such as row count, column cardinality, and data distribution) to estimate the cost of different physical plans. It chooses the most efficient plan based on these estimates, which improves performance for complex queries involving joins and aggregations.

✅ Join Optimization:
The optimizer analyzes join conditions to decide the most efficient join strategy (such as broadcast join, sort-merge join, or shuffle join). For example, if a small table is joined with a large table, Catalyst may use a broadcast join, where the smaller table is distributed to all nodes, reducing data shuffling.
```

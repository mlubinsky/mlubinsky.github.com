### Submit
https://spark.apache.org/docs/latest/submitting-applications.html
```
./bin/spark-submit \
  --class com.example.MainClass \
  --master spark://cluster-url:7077 \
  --executor-memory 2g \
  --total-executor-cores 4 \
  /path/to/your/app.jar \
  arg1 arg2
```

### Code


Get column description:
```
df_data.describe().show()

df_data.columns
```

Handling missing values
```
from pyspark.sql.functions import col,isnan,when,count
df2 = df_data.select([
         count(  \
               when( \
                     col(c).contains('None') | \
                                 col(c).contains('NULL') | \
                                 (col(c) == '' ) | \
                                 col(c).isNull() | \
                                 isnan(c), c \
                  ) \
         ).alias(c) \
 for c in df_data.columns])
 
df2.show()
```
### Count of missing values in a single column
```
df_data.filter(df_data.column_name.isNull()).show()
```
### Filter null on multiple columns
```
df_data.filter(df_data.column_name1.isNull() & df_data.column_name2.isNull()).show()
```

### DROP function

The drop function has three parameters namely how, thres, subset.

how parameter accepts two values namely 
-i) all: to drop a record when all the values are null ; 
ii) any: to drop a record if any one of it’s value is null

thres parameter is used to specify the minimum number of null values required to drop a record.

subset parameter is used to specify the dataset subset which needs to be checked.

### DROP the entire record if all the values are null:
```
df_data = df_data.na.drop(how=’all’)
DROP the entire record if it contains a null value:

df_data = df_data.na.drop(how=’any’)
```

### FILL function:

The fill function has two parameters namely value and subset.
```
df_data = df_data.na.fill('missing')
```
The above code will replace the null values with the keyword ‘missing’

### IMPUTER function:

To use the imputer function we first need to import it

from pyspark.ml.feature import Imputer

imputer parameters
inputsCols is used to specify a list of columns and inputCol is used to specify a single column that needs to be considered while checking for null values.

Similarly, outputCol and outputCols are used to specify the single or multiple output columns depending on the inputs.

strategy parameter defines the technique that needs to be applied on the target column to impute it’s null values. Acceptible values are ‘mean’, ‘median’, ‘mode’
```
#import imputer library
from pyspark.ml.feature import Imputer
#set input columns
inputCols = ['cname1', 'cname2', 'cname3']
#define imputer
imputer = Imputer(
inputCols = inputCols,
outputCols = ["{}_imputed".format(c) for c in                inputCols]).setStrategy("mean")
#apply imputer
imputer.fit(df_data).transform(df_data)
```

### Filter dataframe:

We can use the filter function to extract the required data from a dataframe

 
df_data.filter(“year > 2010”).show(5)
 
df_data.filter(df_data['year'] > 2010).show(5)

query 1 and 2 give the same data that is the top 5 rows where year is greater than 2010

We can use the ~ symbol to get the inverse of a filter
```
df_data.filter(~(df_data[‘year’] > 2010)).show(5)
```
The above code gives the top 5 rows where year is less than 2010

To filter the dataframes based on more than one condition we can use the & | operators
```
df_data.filter((df_data[‘selling_price’]>200000)&(df_data[‘selling_price’]< 400000)).show(5)
```
The above code filters dataframe where selling price is between 2lakh and 4lakh
```
df_data.filter((df_data[‘transmission’]==’Automatic’)|(df_data[‘transmission’]==’Manual’)).show(5)
```
The above code filters dataframe where the transmission is either manual or automatic.

### Get distinct values from a column:
```
df_data.select(‘column_name’).distinct().collect()
```
### Group data and get count:

```
df_data.groupBy(‘column_name’).count().show()
```

### Group data to get mean values:
```
df_data.groupBy(‘column_name’).mean().show()
```
### Group data to get sum:
```
df_data.groupBy(‘column_name’).sum().show()
```


### Exploding array column:

```

val df = Seq((1, "A", Seq(1,2,3)), (2, "B", Seq(3,5))).toDF("col1", "col2", "col3")
df.show()
+----+----+---------+
|col1|col2|     col3|
+----+----+---------+
|   1|   A|[1, 2, 3]|
|   2|   B|   [3, 5]|
+----+----+---------+

val df2 = df.withColumn("col3", explode($"col3"))
df2.show()
+----+----+----+
|col1|col2|col3|
+----+----+----+
|   1|   A|   1|
|   1|   A|   2|
|   1|   A|   3|
|   2|   B|   3|
|   2|   B|   5|
+----+----+----+

val df3 = df.withColumn("new_col4", explode($"col3"))
df3.show()
+----+----+---------+--------+
|col1|col2|     col3|new_col4|
+----+----+---------+--------+
|   1|   A|[1, 2, 3]|       1|
|   1|   A|[1, 2, 3]|       2|
|   1|   A|[1, 2, 3]|       3|
|   2|   B|   [3, 5]|       3|
|   2|   B|   [3, 5]|       5|
+----+----+---------+--------+

val df5 = df.withColumn("new_col4", explode($"col3")).select("col1","col2", "new_col4")
df5.show()
+----+----+--------+
|col1|col2|new_col4|
+----+----+--------+
|   1|   A|       1|
|   1|   A|       2|
|   1|   A|       3|
|   2|   B|       3|
|   2|   B|       5|
+----+----+--------+


val df7=df.select(col("col1"),col("col2"), explode(col("col3")))
 
 df7.show()
+----+----+---+
|col1|col2|col|
+----+----+---+
|   1|   A|  1|
|   1|   A|  2|
|   1|   A|  3|
|   2|   B|  3|
|   2|   B|  5|
+----+----+---+


creating alias for exploded column:
-------------------------------------
val df8=df.select(col("col1"),col("col2"), explode(col("col3")).alias("my_alias"))
 

scala> df8.show()
+----+----+--------+
|col1|col2|my_alias|
+----+----+--------+
|   1|   A|       1|
|   1|   A|       2|
|   1|   A|       3|
|   2|   B|       3|
|   2|   B|       5|
+----+----+--------+



Filter  example
------------------
val df = Seq(
  ("thor", "new york"),
  ("aquaman", "atlantis"),
  ("wolverine", "new york")
).toDF("superhero", "city")


df.show()
+---------+--------+
|superhero|    city|
+---------+--------+
|     thor|new york|
|  aquaman|atlantis|
|wolverine|new york|
+---------+--------+

df.printSchema()

// creating new column:

df.withColumn("city_starts_with_new", $"city".startsWith("new")).show()
+---------+--------+--------------------+
|superhero|    city|city_starts_with_new|
+---------+--------+--------------------+
|     thor|new york|                true|
|  aquaman|atlantis|               false|
|wolverine|new york|                true|
+---------+--------+--------------------+


println(df.schema.fieldNames.contains("city"))
println(df.schema.contains(StructField("city",StringType,true)))


https://stackoverflow.com/questions/47657072/importing-schema-from-json-with-optional-value

:paste
// Entering paste mode (ctrl-D to finish) 

import org.apache.spark.sql.expressions.scalalang._
import org.apache.spark.sql.types._
import org.apache.spark.sql.{DataFrame, Dataset, SparkSession}    
val schema = StructType(Seq(
  StructField("k1", StringType, false),
  StructField("optK", StructType(Seq(StructField("nestedK", StringType, false))), false)
))    
val df = spark.read.option("allowUnquotedFieldNames",true).schema(schema).json("s3 location of data.json")       

df: org.apache.spark.sql.DataFrame = [k1: string, optK: struct<nestedK: string>]

scala> df.show
+--------------+------+
|            k1|  optK|
+--------------+------+
|     someValue|[optV]|
|someOtherValue|  null|
+--------------+------+

A Column object corresponding with the city column can be created using the following three syntaxes:

$"city"
df("city")
col("city") (must run import org.apache.spark.sql.functions.col first)


This is tha same:

val s1 = df.select("city")
val s2 = df.select($"city")


```


 https://habr.com/ru/company/otus/blog/653033/
 
```
df.show(n=2, truncate=False, vertical=True)

df.display()


// read csv 
val raw = spark
        .read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(s"$basePath/data/BankChurners.csv")

val columns: Array[String] = raw.columns
val columnsLen: Int = columns.length

// Переменная colsToDrop – это массив имён колонок, которые надо исключить из загруженного набора данных.
val colsToDrop: Array[String] = columns.slice(columnsLen - 2, columnsLen) :+ columns.head
//Для удаления колонок из DataFrame используется метод drop, аргументами которого является одно или несколько названий колонок – аргументы переменной длины. Чтобы преобразовать массив в аргументы метода в Scala применяется конструкция array: _*
val df = raw.drop(colsToDrop: _*)

df.show(5, truncate = false)
df.printSchema
// Выведем в удобном виде названия колонок и их тип:
df.dtypes.foreach { dt => println(f"${dt._1}%25s\t${dt._2}") }
// посмотрим сколько колонок каждого типа:
df.dtypes.groupBy(_._2).mapValues(_.length).foreach(println)

// Выделим числовые колонки и применим к ним метод summary. Этот метод вычисляет такие статистики как:
// count mean stddev min max
// arbitrary approximate percentiles specified as a percentage (e.g. 75%)

val numericColumns: Array[String] = df.dtypes.filter(!_._2.equals("StringType")).map(_._1)
df.select(numericColumns.map(col): _*).summary().show


//посмотрим на значения колонки Customer_Age

df.groupBy($"Customer_Age").count().show(100)

//введём новую колонку target, которая будет равна 0, когда значение Attrition_Flag равно “Existing Customer”, и 1 в остальных случаях.
val dft = df.withColumn("target", when($"Attrition_Flag" === "Existing Customer", 0).otherwise(1))

dft.groupBy("target").count.show

Выделим в отдельные переменные данные разных классов и сохраним количество записей в каждом классе.

val df1 = dft.filter($"target" === 1)
val df0 = dft.filter($"target" === 0)
 
val df1count = df1.count
val df0count = df0.count

Нужно увеличить количество записей в наборе df1 в df0count / df1count раз:

val df1Over = df1
        .withColumn("dummy", explode(lit((1 to (df0count / df1count).toInt).toArray)))
        .drop("dummy")
Давайте рассмотрим это подробнее.

Конструкция (1 to (df0count / df1count).toInt).toArray создаёт массив со значениями от 1 до (df0count / df1count)

(1 to (df0count / df1count).toInt).toArray
res77: Array[Int] = Array(1, 2, 3, 4, 5)

Функция lit создаёт колонки с определённым значением. Мы добавляем колонку с именем dummy, значением которой является массив:

df1
        .withColumn("dummy", lit((1 to (df0count / df1count).toInt).toArray))
        .select("Attrition_Flag", "Customer_Age", "dummy")
        .show(10)
        
Функция explode создаёт новую строку для каждого элемента массива:

df1
        .withColumn("dummy", explode(lit((1 to (df0count / df1count).toInt).toArray)))
        .select("Attrition_Flag", "Customer_Age", "dummy")
        .show(10)
        
Итак, df1Over – это набор, содержащий записи класса target = 1, увеличенный в df0count / df1count раз.

Объединим этот новый набор с набором записей второго класса и проверим сбалансированность исходного набора:

val data = df0.unionAll(df1Over)
data.groupBy("target").count.show 
```

### SparkSQL
https://habr.com/ru/company/alfastrah/blog/481924/

https://spark.apache.org/docs/latest/sql-programming-guide.html

```
select A.people, B.state, count(*) from A join B on A.state_id=B.state_id group by B.state
```
Since there are only 50 states we cannot achieve better parallelism by adding > 50 cores also since California is the biggest state the data is skewed - use broadcast join

https://habr.com/ru/company/vk/blog/442688/
```
val train = sqlContext.read.parquet("/events/hackatons/SNAHackathon/2019/collabTrain")

z.show(train.groupBy($"date").agg(
        functions.count($"instanceId_userId").as("count"),
        functions.countDistinct($"instanceId_userId").as("users"),
        functions.countDistinct($"instanceId_objectId").as("objects"),
        functions.countDistinct($"metadata_ownerId").as("owners"))
      .orderBy("date"))
      
      or like this:
     
val train = sqlContext.read.parquet("/events/hackatons/SNAHackathon/2019/collabTrain")

z.show(
   train groupBy $"date" agg(
        count($"instanceId_userId") as "count",
        countDistinct($"instanceId_userId") as "users",
        countDistinct($"instanceId_objectId") as "objects",
        countDistinct($"metadata_ownerId") as "owners")
   orderBy "date"
)
```
### SQL hints
https://jaceklaskowski.gitbooks.io/mastering-spark-sql/content/spark-sql-hint-framework.html
```
COALESCE and REPARTITION Hints
Spark SQL 2.4 added support for COALESCE and REPARTITION hints (using SQL comments):

SELECT /*+ COALESCE(5) */  

SELECT /*+ REPARTITION(3) */  

Broadcast Hints
Spark SQL 2.2 supports BROADCAST hints using broadcast standard function or SQL comments:

SELECT /*+ MAPJOIN(b) */  

SELECT /*+ BROADCASTJOIN(b) */  

SELECT /*+ BROADCAST(b) */
```

### Extracting values from Row
```
val transactions = Seq((1, 2), (1, 4), (2, 3)).toDF("user_id", "category_id")

val transactions_with_counts = transactions
  .groupBy($"user_id", $"category_id")
  .count

There are a few ways to access Row values and keep expected types:

a) 
transactions_with_counts.map(
  r => Rating(r.getInt(0), r.getInt(1), r.getLong(2))
)

b)
transactions_with_counts.map(r => Rating(
  r.getAs[Int]("user_id"), r.getAs[Int]("category_id"), r.getAs[Long](2)
))

c)
import org.apache.spark.sql.Row

transactions_with_counts.map{
  case Row(user_id: Int, category_id: Int, rating: Long) =>
    Rating(user_id, category_id, rating)
} 

d) Converting to statically typed Dataset (Spark 1.6+ / 2.0+):

transactions_with_counts.as[(Int, Int, Long)]

e)
case class Rating(user_id: Int, category_id:Int, count:Long)
val transactions_with_counts = transactions.groupBy($"user_id", $"category_id").count

val rating = transactions_with_counts.as[Rating]
```
This way you will not run into run-time errors in Spark because your Rating class column name is identical to the 'count' column name generated by Spark on run-time.

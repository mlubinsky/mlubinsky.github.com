### Code

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

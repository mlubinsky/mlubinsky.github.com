Free online book: Python for data analysis:
https://wesmckinney.com/book/



https://habr.com/ru/companies/ru_mts/articles/738208/  Plotting 

1. 5 Hidden Apache Spark Facts That Fewer People Talk About
https://lnkd.in/guvSUKCs

2. CDC Replication: What It Is, How It Works, & Best Practices
https://bit.ly/3H6Uze6

3. What Is Trino And Why Is It Great At Processing Big Data
https://lnkd.in/gXkuZm6C

4. Should You Use Apache Airflow?
https://lnkd.in/gvvxBVKc

5. Intro To Databricks - What Is Databricks
https://lnkd.in/gAaavFEJ

6. Data Governance for Modern Organizations, Part 1 by Shinji Kim
https://lnkd.in/gJNsExQY

7. The Truth about Prefect, Mage, and Airflow by Daniel Beach
https://lnkd.in/gEimhmzK

### Python libs:
https://tryolabs.com/blog/2022/12/26/top-python-libraries-2022 

https://habr.com/ru/articles/795785/

https://pypi.org/project/adix/ Data Exploration Made Easy & Colorful 

## Reading from DB to pandas dataframe

```
import pandas as pd
import psycopg2

# Define the connection parameters
conn_params = {
    'dbname': 'your-db-name',
    'user': 'user-name',
    'password': 'password',
    'host': 'localhost',
    'port': '5432'
}

# Establish the connection
conn = psycopg2.connect(**conn_params)

# Retrieve data into a Pandas DataFrame
user_posts_df = pd.read_sql('SELECT * FROM user_posts', conn)
```

### Working with parquet
```
import sys
import panadas as pd

df = pd.read_parquet(sys.argv[1], engine="fastparquet")
```

https://lobste.rs/s/c49sak/which_embedded_olap_database_pick

https://clickhouse.com/blog/apache-parquet-clickhouse-local-querying-writing

https://www.tadviewer.com/  A fast viewer for CSV and Parquet files and SQLite and DuckDb databases that supports large files.

https://til.simonwillison.net/duckdb/parquet

https://github.com/domoritz/arrow-tools

https://habr.com/ru/companies/skillfactory/articles/720530/

https://csvbase.com/blog/3

https://clickhouse.com/blog/extracting-converting-querying-local-files-with-sql-clickhouse-local

https://news.ycombinator.com/item?id=35418933

https://www.linkedin.com/pulse/all-you-need-know-parquet-file-structure-depth-rohan-karanjawala/

If you want to see the gory details of the format, try the _parquet-tools_ package on PyPI with a sample file:

https://pypi.org/project/parquet-tools/
```
pip install -U parquet-tools
curl -O "https://csvbase.com/meripaterson/stock-exchanges.parquet"
parquet-tools inspect --detail stock-exchanges.parquet
 parquet-tools cat <your file.parquet> | grep etc
```

### Polars

 https://pola.rs/

 https://www.youtube.com/watch?v=aiHSMYvoqYE&list=PLTsu3dft3CWiow7L7WrCd27ohlra_5PGH&index=6&t=689s

You can use Polars in spark with arrow udfs

Cloud support.

Example:
```
pl.scan_parquet("s3://polars-inc-test/tpch/scale-10/lineitem/*.parquet")
```
Polars comes with a SQL front-end that converts to polars LazyFrames (think query plans).
```
You can even mix and match the SQL and the LazyFrame API.

df = pl.DataFrame({
    "foo": [1, 2, 3],
    "bar": [1, 2, 3],
})


ctxt = pl.SQLContext({"table_1": df})

# returns a LazyFrame
lf = ctxt.execute("""SELECT sum(foo), bar FROM table_1 GROUP BY bar""")

# explain query plan
lf.explain()

# continue with LazyFrame API
lf = lf.with_columns(some_computation = pl.col("bar").diff() * pl.col("foo"))

# get result
lf.collect()
```


https://habr.com/ru/companies/spectr/articles/738766/

https://www.parand.com/a-practical-introduction-to-polars.html

https://itnext.io/the-fastest-way-to-read-a-csv-file-in-pandas-2-0-532c1f978201

https://dev.to/ranggakd/polars-vs-pandas-a-brief-tale-of-two-dataframe-libraries-lli


https://www.reddit.com/r/Python/comments/13bb59x/test_on_4_concurrent_jobs_using_pythonpolars/

https://datashader.org/ Fast plotting of million of points

https://ponder.io/ponder-on-duckdb/ Ponder and DuckDB

### Pandas

https://stackabuse.com/how-to-efficiently-convert-data-types-in-pandas/

https://stackabuse.com/handling-duplicate-values-in-a-pandas-dataframe/  duplicates findings

https://stackabuse.com/reading-and-writing-sql-files-in-pandas/

https://www.pythonforbeginners.com/basics/pandas-map-vs-apply-method-in-python map() vs apply()

https://datascientyst.com/

#### Z-score
```
import pandas as pd

data = {'score': [56, 65, 67, 74, 75, 42, 76, 63, 67, 85, 120]}
df = pd.DataFrame(data)

# расчет z-оценки
df['z_score'] = (df['score'] - df['score'].mean()) / df['score'].std()

# фильтрация выбросов
df_filtered = df[(df['z_score'] > -3) & (df['z_score'] < 3)]  # same as df['z_score'].abs() < 3
```

### Интерквартильный размах (IQR method)
```
IQR — это мера разброса данных, равная разнице между третьим Q3 и первым квартилями Q1. Формула для расчета IQR:

IQR = Q3 - Q1

Выбросами считаются значения, выходящие за пределы:

Q1 - 1.5 \times IQR (нижний предел) и Q3 + 1.5 \times IQR (верхний предел).

Пример на Python:

import numpy as np

data = {'score': [56, 65, 67, 74, 75, 42, 76, 63, 67, 85, 120]}
df = pd.DataFrame(data)

# расчет квартилей
Q1 = df['score'].quantile(0.25)
Q3 = df['score'].quantile(0.75)
IQR = Q3 - Q1

# определение границ выбросов
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# фильтрация выбросов
df_filtered = df[(df['score'] >= lower_bound) & (df['score'] <= upper_bound)]

```


df.describe(include=object).T

Find maximum values of Age and Amount_spent by Gender:
```
df[['Age', 'Amount_spent']].groupby(df['Gender']).max()
```

Find mean, count, and max values of Age and Amount_spent by Gender then we can use agg() function with groupby() .
```
state_gender_res = df[['Age','Gender','Amount_spent']].groupby(['Gender']).agg(['count', 'mean', 'max'])
```

https://realpython.com/pandas-dataframe/

https://github.com/noklam/dtype_diet/tree/master/ Save memory

  https://www.webpages.uidaho.edu/~stevel/cheatsheets/Pandas%20DataFrame%20Notes_12pages.pdf
  
https://pub.towardsai.net/pandas-cheat-sheet-functions-for-data-analysis-2cf4923266aa  

https://habr.com/ru/companies/otus/articles/728118/

https://www.youtube.com/watch?v=-tU7fuUiq7w

https://habr.com/ru/search/?q=pandas&target_type=posts&order=relevance

https://www.youtube.com/watch?v=DKZ2XmYsY3E

Correlation matrix:
https://habr.com/ru/articles/708468/

https://towardsai.net/p/data-science/pandas-complete-tutorial-for-data-science-in-2022

Counting total missing values in each column in ascending order we use .sum() and sort_values(ascending=False) function.

df.isna().sum().sort_values(ascending=False)

Find not-numerical data in columns:
https://towardsdatascience.com/pandas-cheat-sheet-for-data-preprocessing-cd1bcd607426
```
col_miss = ['DIS', 'B']
for i_col in col_miss:
    for j in df_X[i_col].unique():
        try:
            float(j)
        except ValueError:
            print(j)
```

 Imputing forward fill or backfill by ffill and bfill. In ffill missing value impute from the value of the above row and for bfill it’s taken from the below rows value.

df['Referal'].fillna(method='ffill', inplace=True)


value_counts()   tells us the distribution of a column or dataframe as a number of times it occurs in the data.

 merge two data frames horizontally:
 pd.concat([ df1, df2],axis=0)
 
 df['tall_male'] = np.where(
                              df['Male Height in Ft'] > 6.0,
                              1,
                              0)
 #### Join
 https://pub.towardsai.net/deep-dive-into-pandas-dataframe-join-pd-join-4cc2adee351d
 
### Reading csv

https://pandas.pydata.org/docs/user_guide/scale.html

```
df_train = pd.read_csv('data/train.csv',
                        dtype={'content_id': 'int16',
                               'content_type_id': 'int8',
                               'task_container_id': 'int16',
                               'user_answer': 'int8',
                               'answered_correctly': 'int8',
                               'prior_question_elapsed_time': 'float32'})
                               
```

```
import pandas as pd
import re

df = pd.read_csv('data_with_errors.csv')
df.head()
df.info()
```
Observe the data column has type string,
Following attempt to fix it may fail if some records have not obey the expected format:
```
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
```
Another attempt to fix:
```
search = lambda x: x if re.search(r"\d{4}-\d{2}-\d{2}", x) else 'not found'
df['date'] = df['date'].map(search)
df.query('date == "not found"').count()
```
Let delete records where data are not valid
```
df = df.drop(df.query('date == "not found"').index)
df.query('date == "not found"').count()
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
df.info()
```
Now we expect the data column has type datetime

To convert string column to number:

df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df.query('quantity < 0')

Convert negative numbers to positive:

df.loc[df['quantity'] < 0,'quantity'] = abs(df['quantity'])

#### Duplicates:

how many different values (number of unique values) are contained in each column using “nunique”:

df_X.nunique()

df[df.duplicated()]

Remove duplicates:

df = df.drop(df[df.duplicated()].index)

Show unique values:

df.product_name.unique()

df.to_csv('processed_data.csv',index=False, header=True)

### Pandas 2.0

https://datapythonista.me/blog/pandas-20-and-the-arrow-revolution-part-i

https://news.ycombinator.com/item?id=35423569
```
strings as objects and integers turning into floats when NaNs are introduced have been a much bigger annoyance to me, than it ought to.
I'm excited to try out the new pyarrow dtypes, but it also sounds confusing that there are now 2 classes of types


Yeah, I stopped using pandas entirely for ETL for this exact reason. 
If you are trying to maintain the fidelity of the data while cleaning, automatic casting is awful. 
If the new backend prevents automatic casting, it might be worth reconsidering for me.

```

### Data Cleaning Cheat Sheet in Python - By Eugenia Anello
```
Table of Contents:
1. Dealing with Missing Data
2. Dealing with Duplicates
3. Outlier Detection
4. Encode Categorical Features
5. Transformation
```
#### 1. Dealing with Missing data
```
Check missing data in each column of the dataset
df.isnull().sum()
Delete missing data
df.dropna(how='all')
Drop columns that have missing values
df.dropna(how='columns')
Drop specific columns that have missing values
df.dropna(subset=[‘municipal,'city'])
Replace missing values with Mean/Median/Mode
df[‘price’].fillna(df[‘price’].mean())
df[‘age’].fillna(df[‘age’].median())
df[‘type_building’].fillna(df[‘type_building’].mode())
Replace missing values with Mean/Median/Mode of the group
df['price'].fillna(df.group('type_building')['price'].transform(‘mean’),
inplace=True)
Forward Fill - Fill missing values with values before them
df['stock_price'].fillna(method='ffill')
Forward Fill within Groups
df['stock_price'] = df.groupby('type_stock').ffill()
Backward Fill - FIll missing values with values after them
df['stock_price'].fillna(method='bfill')
Backward Fill within Groups
df['stock_price'] = df.groupby('type_stock')['stock_price'].bfill()
Fill missing values using the interpolation method
df['stock_price'] =
df['stock_price'].interpolate(method='polynomial',order=2)
Fill missing values using the interpolation method within groups
df['stock_price'] = df.groupby('type_stock')['stock_price'].apply(lambda
x: x.interpolate(method='polynomial',order=2))
```
#### 2. Dealing with Duplicates
```
Check if there are duplicates
df.duplicated().sum()
Extract duplicate rows from the dataframe
df[df.duplicated()]
Drop duplicates
df.drop_duplicates()
Aggregate data
df.groupby('id').agg({'price':'mean'}).reset_index()
```
####  3.Outlier detection
```
Detect range of values for each column of the dataset
df.describe([x*0.1 for x in range(10)])
Display boxplot to display the distribution of a column
import seaborn as sns
sns.boxplot(x=df['age'])
Display histogram to display the distribution of a column
sns.displot(data=df[‘column1’])
Remove outliers
df = df[df['age']<df[‘age'].quantile(0.9)]
Outlier detection with machine learning models, like Isolation Forest
if = IsolationForest(random_state=42)
if.fit(X)
y_pred = if.predict(X)
```

#### 4. Encode categorical features
```
Apply one-hot-encoding to a categorical column
from sklearn.prepreprocessing import OneHotEncoder
ohe = OneHotEncoder()
encoded_data = pd.DataFrame(ohe.fit_transform(df[[‘type_build’]]).toarray())
new_df = df.join(encoded_data)
Apply label-encoding to a categorical column
from sklearn.prepreprocessing import LabelEncoder
le = LabelEncoder()
df[‘type_build’] = le.fit_transform(df[‘type_build’])
Apply ordinal-encoding to a categorical column to retain its ordinal nature
from sklearn.prepreprocessing import OrdinalEncoder
le = OrdinalEncoder()
df['price_level'] = le.fit_transform(df['price_level'])
```

#### 5. Transformation
```
Standardize features by removing the mean and scaling to unit variance
from sklearn.processing import StandardScaler
X_std = StandardScaler().transform(X)
Rescale features into the range [0,1]
from sklearn.processing import MinMaxScaler
X_mms = MinMaxScaler().transform(X)
Scale features exploiting statistics that are robust to outliers
from sklearn.processing import RobustScaler
X_rs = RobustScaler().transform(X)
```

https://stackoverflow.com/questions/50821312/meaning-of-python-m-flag

https://betterprogramming.pub/pandas-illustrated-the-definitive-visual-guide-to-pandas-c31fa921a43

https://medium.com/@finndersen/the-ultimate-guide-to-pandas-read-csv-function-5377874e27d5

https://medium.com/@finndersen/guide-to-pandas-extension-types-and-how-to-create-your-own-3b213d689c86

```
In Python, everything is an object, so even a simple number value incurs all of the associated overheads. For example, representing a small integer value such as 120 requires 28 bytes of memory:

>> sys.getsizeof(120)
28
This is 3.5x the space required to store the same value as an 8-bit integer in a lower-level, stricter programming language such as C/C++. Also, the mathematical arithmetic performance will be poor due to the dynamic and interpreted nature of Python compared to strictly typed and compiled languages.

NumPy addresses these shortcomings by bringing the memory efficiency and computational power of languages like C to Python. It consists of an ndarray data structure which stores data efficiently as a homogeneous block in memory (similar to C arrays), as well as providing functions and operators for high-performance arithmetic and algorithmic computation on these arrays. NumPy is particularly efficient at handling large scale datasets which makes it suitable for data science, statistical, and machine learning use cases.

Pandas higher-level library which leverages the power of the somewhat primitive NumPy ndarray and makes it more accessible through the more comprehensive DataFrame data structure, with more advanced data manipulation and analysis capabilities. However, since Pandas uses NumPy’s ndarray for storing data, it inherits its limitations; such as:

Limited data types — NumPy only supports basic data types such as boolean, integers and floats. More complex data types and objects are often used when working with Python; these will be stored as the object dtype in an array and will not benefit from the memory efficiency or high-performance, vectorised operations available with the native data types.
Integer type ndarrays do not support null values — By default, creating a Series from a list of integers with a null value will cause the data to be stored as float type array, which is not ideal for many reasons (e.g. some integers do not even have an accurate floating point representation)
No support for timezones or UTC offsets for datetime types
To address these limitations, Pandas includes the Extension Types interface since version 0.23.0, which enables the creation of custom data types to add additional capabilities beyond that of NumPy’s existing type system.

Extension Types
The Extension Types interface allows specifying a new custom Pandas array data type, with complete control over behaviour, including:

How the array is constructed from different types of raw data
How the data is stored (may be backed by none, one or many NumPy arrays)
Behaviour of operators (e.g. for efficient vectorised arithmetic operations)
How the array is constructed from or converted to Apache Arrow data
Pandas itself uses the extension types system to create some useful built-in types such as:

Categorical — Used to store categorical variables, which take on a limited number of possible values. This allows for much more efficient storage of categorical type data such as gender, country, eye colour, etc. The CategoricalDtype extension type is implemented using two NumPy arrays; one to store the limited set of category values (like a lookup table), and another to store the codes which map to these values.
Nullable Integer Type — As mentioned previously, Pandas historically forces an array of integers with any missing values to become floating point to accomodate the NaN value. This extension type allows creating an integer array with nulls, by using one NumPy array to store the integer values and another which acts as a boolean mask to indicate which values are null.
Timezone-aware Datetime — The DatetimeTZDtype extension type allows associating a timezone with an array of datetime data.
Dedicated String Type — Prior to Pandas v1.0.0, string data could only be stored as the object dtype, with no type-specific optimisations or capabilities. The new StringDtype aims to address this, with future enhancements expected to “significantly increase the performance and lower the memory overhead of StringArray”.
Creating a Custom Extension Type
Now let’s explore creating a new basic custom extension type, using the process described here. It involves creating two class definitions:

An ExtensionDtype subclass — Describes the data type, including specifying the associated scalar type (type for each element) and the array type (custom ExtensionArray type).
An ExtensionArray subclass — Defines the array-like behaviour, such as how it is initialised from input data, how the data is stored and retrieved, operator implementations, and any other custom methods.
In the following example we will create a custom Extension Type in order to store 2D vector data and provide efficient arithmetic support and some custom methods. Below is the definition of a custom Vector class which will be the scalar type of each element in the array:

I have added some operator overload methods to enable arithmetic and comparison with other Vectors or scalar values. The @total_ordering functools decorator is used to fill in the remaining set of equality/comparison operator overload methods. Here are some usage examples:

# Initialise with x, y components
v = Vector(3, 14) 

# Vector addition; (x, y) tuple is automatically converted to a Vector
v + (10, 2)              # Result: Vector(13.0, 16.0)
# Scalar Multiplication
v * 2                    # Result: Vector(6.0, 28.0)
# Magnitude
v.magnitude()            # Result: 14.317821063276353
# Dot Product
v.dot(Vector(-5, 11.3))  # Result: 143.20
Define the ExtensionDtype
Usually the point of creating a custom Extension Type is to enable the construction of an array of objects with a more complex data type than those already provided by NumPy. In this case we’re making an Extension Type to support storing an array of Vector objects. To do this, first we need to create and register a custom ExtensionDtype subclass for the data type, defining at least 3 necessary attributes:

type — Attribute or property which returns the scalar type for the array
name — Attribute or property which returns a string identifying the data type
construct_array_type — Attribute or class method which returns the array type (ExtensionArray subclass). Often implemented as a classmethod so that the array type can be dynamically imported when defined in another module (to avoid circular imports).
For more details check the ExtensionDtype source code documentation, and below is the example VectorDtype definition:

VectorDType Definition
The @register_extension_dtype decorator is used to register the Dtype with Panda’s type framework so that it can work with pd.array() and pd.Series() constructors and Series.astype() method.

Define the ExtensionArray
The ExtensionArray subclass contains most of the logic for the behaviour of the custom Extension Type, such as how the array data is initialised, stored and accessed. This is implemented by defining the following required attributes:

_from_sequence() — Class method which defines how to initialise a new ExtensionArray instance from a sequence of scalar values (such as values provided to pd.array() or pd.Series() constructors). Used internally by Pandas when reconstructing a Series from values resulting from some transformation. Can also optionally provide a specific Dtype (instance of Dtype compatible with this ExtensionArray)
_from_factorized() — Class method which defines how to reconstruct an ExtensionArray after factorization (this can be skipped if you’re not going to use this functionality)
__getitem__() — Method which defines how to select and return a single element or subset of data from the array
__len__() — Method which returns length of the array
__eq__() — Method which implements element-wise equality with a scalar value to return a boolean numpy ndarray
dtype — Property method which returns an ExtensionDtype instance for this ExtensionArray
nbytes — Property method which calculates and returns the number of bytes used to store the array data in memory (e.g. sum of memory usage of all underlying NumPy ndarrays containing data for theExtensionArray)
isna() — Method which returns a boolean array indicating if each value is missing
take() — Method to implement logic for taking a subset of elements from the array using positional indexing. Called by Series.__getitem__, .loc, .iloc, when indices is a sequence of values.
copy() — Method which returns a copy of the array (usually by initialising a new instance with copies of underlying data)
_concat_same_type() — Method to concatenate multiple arrays of this type and return a merged result
Other methods can be defined for additional functionality, or optionally overridden with a more efficient implementation specific to the Extension Array for improved performance. See the ExtensionArray source code documentation for more details, and below for how the basic example VectorArray is defined:

As mentioned here, the ExtensionScalarOpsMixin is used to automatically add comparison and arithmetic operator method definitions for the array, which will use the implementation defined on the scalar type for each element (Vector in this case). This will be explored in more detail later.

Using the VectorArray
A VectorArray can be constructed directly by using the class, or the pd.array() constructor and specifying the type name. Values can be provided as either a sequence of Vector instances, or a sequence of coordinate pairs which will be converted to Vectors inside VectorArray._from_sequence() for convenience, such as:

coords = [(1,2), (-5, 20), (234.5, 90.44), (34, -19.5)]
arr = VectorArray.from_vectors(coords)
# OR
arr = pd.array(coords, dtype='vector')
arr

# <VectorArray> [Vector(1.0, 2.0), Vector(-5.0, 20.5), Vector(234.5, 90.44)] 
# Length: 3, dtype: vector
A Series can be initialised from an existing VectorArray, or from a sequence of values similar to pd.array():

s = pd.Series(arr)
# OR
s = pd.Series(coords, dtype='vector')
s

# 0 Vector(1.0, 2.0) 
# 1 Vector(-5.0, 20.5) 
# 2 Vector(234.5, 90.44) 
# dtype: vector
When a single element is accessed, a Vector instance is returned:

s[1]

# Vector(-5.0, 20.5)
Whereas a slice, boolean or positional indexing returns another VectorArray or Series:

s[1:3]
# OR
s[[False, True, True]]
# OR
s[[[1,2]]

# 1    Vector(-5.0, 20.5)
# 2    Vector(234.5, 90.44)
# dtype: vector
The custom magnitude() and dot() methods can be used like:

arr.magnitude()
# OR
s.array.magnitude()

# array([  2.23606798,  21.10094785, 251.33571891])

arr.dot(Vector(2, -5))
# OR 
s.array.dot(Vector(2, -5))

# array([  -8. , -112.5,   16.8])
Array Arithmetic and Comparison
As mentioned earlier, the ExtensionScalarOpsMixin used with VectorArray adds arithmetic and comparison operator support using the logic defined in the Vector class. For example:

# Multiply by scalar value
s * 5

# 0        Vector(5.0, 10.0)
# 1     Vector(-25.0, 102.5)
# 2    Vector(1172.5, 452.2)
# dtype: vector

# Add Vector 
s + Vector(5, 10)

# 0        Vector(6.0, 12.0)
# 1        Vector(0.0, 30.5)
# 2    Vector(239.5, 100.44)
# dtype: vector

# Compare with Vector 
s == Vector(1, 2)

# 0     True
# 1    False
# 2    False
# dtype: bool
This is very convenient, however it works by iterating through every element in the array to create Vector instances and perform element-wise arithmetic or comparison — which is very inefficient. For example, adding a Vector to a VectorArray with 3 million elements took almost 16 seconds on my machine:

s_large = pd.Series(coords*1000000, dtype='vector')
s_large + Vector(5, 10)  # Duration: 15.9s
To improve performance, we can explicitly add operator overload methods to the VectorArray class to implement the arithmetic logic in an efficient, vectorised way. Here is a basic example for the addition operator overload method which can be added to VectorArray:

    def __add__(self, other):
        """
        Perform addition with either single Vector or VectorArray
        """
        if isinstance(other, Vector):
            # Addition with single Vector
            return VectorArray(self.x_values + other.x, self.y_values + other.y)
        elif isinstance(other, VectorArray) and self.size == other.size:
            # Element-wise addition with other VectorArray
            return VectorArray(self.x_values + other.x_values, self.y_values + other.y_values)
        else:
            raise TypeError('Cannot perform vector addition with {}'.format(other))
To get this method to work, we must remove ExtensionScalarOpsMixin as well as the VectorArray._add_arithmetic_ops() and VectorArray._add_comparison_ops() calls, because they currently replace any existing defined operator overload methods with their own. Unfortunately, this means if we want to implement any custom operator overload method on VectorArray, we must abandon ExtensionScalarOpsMixin entirely and define all required operator overload methods ourselves. I personally believe it would make more sense if ExtensionScalarOpsMixin did not add an operator overload method that is already defined on the ExtensionArray class; this way a developer could add some subset of operator overload methods with more efficient implementation if desired, and all others would use element-wise fallback from ExtensionScalarOpsMixin. I’ve raised a Pandas feature enhancement suggestion for this functionality here.

Back to the new addition operator implementation, it causes the same above Vector addition operation to take only 10ms, which is 1590x faster than the element-wise approach of ExtensionScalarOpsMixin. This shows it’s definitely worthwhile defining your own efficient vectorised operator overload methods on your custom ExtensionArray class!

Parameterised ExtensionDtypes
In this simple example, there is only a single variation ofCoordinateDtype, meaning all instances of the data type behave the same. However, it is possible to create an ExtensionDtype which takes initialisation parameters used to configure the nature and behaviour of the data type. For example, the DatetimeTZDtype mentioned earlier can take two initialisation parameters: the precision of the datetime data, and the timezone.

When creating a parametized Dtype, you must also:

Define name as a property method, which can generate a dynamic string representation including parameter values, e.g. ‘datetime64[ns, UTC]’
Define the construct_from_string(string) class method, which specifies how a Dtype instance should be initialised from a string representation (which may contain parameter values). For example, ‘datetime64[ns, UTC]’ would be a string representation used to initialise an DatetimeTZDtype(unit=‘ns’, tz=‘UTC’) instance. Regex pattern matching is often used to achieve this.
Define the_metadata class attribute as a tuple of parameter attribute names, which will be used during hashing and comparison of Dtype instances.
Here is another example of a basic custom Extension Type with a parametized ExtensionDtype, and you can also take a look at how Panda’s internal extension types are implemented.

Next Steps
So far I’ve demonstrated a basic custom Extension Type example with just the bare minimum required to get it working, however there are some further enhancements that could be made to increase its usefulness:

The VectorDtype and VectorArray could be enhanced by adding a ‘dimensions’ parameter to support 3 (or even higher) dimensional vectors instead of just the current 2.
Implement the full set of arithmetic and comparison operator overload methods on VectorArray
Implement VectorArray.__setitem__() to allow assigning one or more Vector values to an existing array
Add better null-value support including initialising with sequence of values that may contain None
Override the following ExtensionArray methods for improved performance: fillna(), dropna(), unique(), factorize(), _values_for_factorize(), argsort(), argmax(), argmin(), _values_for_argsort(), searchsorted()
Implement VectorArray._from_sequence_of_strings() to handle parsing array data from strings such as in read_csv()
Add better type-checking and error handling in VectorArray methods
Explore potential alternative options to NumPy for storing array data such as Apache Arrow
Conclusion
The aim of this guide was to clarify what Pandas Extension Types are and how they can be used to add powerful new functionality to the popular data processing library. I hope you are now better equipped to create your own custom Extension Types to use in your projects!

If you enjoyed this article, please consider checking out my others and following me for future ones :)
```






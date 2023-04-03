### Working with parquet

https://www.tadviewer.com/  A fast viewer for CSV and Parquet files and SQLite and DuckDb databases that supports large files.

https://csvbase.com/blog/3

https://www.linkedin.com/pulse/all-you-need-know-parquet-file-structure-depth-rohan-karanjawala/

If you want to see the gory details of the format, try the _parquet-tools_ package on PyPI with a sample file:

https://pypi.org/project/parquet-tools/
```
pip install -U parquet-tools
curl -O "https://csvbase.com/meripaterson/stock-exchanges.parquet"
parquet-tools inspect --detail stock-exchanges.parquet
```

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






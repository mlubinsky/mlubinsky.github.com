### Book
Python for Data Analysis, 3E
https://wesmckinney.com/book/

### Marimo

https://github.com/marimo-team/marimo

###  PyArrow
https://arrow.apache.org/docs/python/index.html

 PyArrow library provides pandas with its own optimized data types, which are faster and less memory-intensive than the traditional NumPy types that pandas uses by default.

### DF with types
```
for col in df.columns:
    print(f"name = {col}, type = {df[col].dtype}")

df = pd.DataFrame(columns=['A', 'B', 'C']).astype({'A': int, 'B': float, 'C': str})

print(df.dtypes)

You can convert a Pandas DataFrame column from object (string) to float using the .astype() method or pd.to_numeric().

Method 1: Using .astype(float)
 
df["column_name"] = df["column_name"].astype(float)

Method 2: Using pd.to_numeric() (Handles Errors)
If your column contains non-numeric values, use pd.to_numeric() to handle errors:

df["column_name"] = pd.to_numeric(df["column_name"], errors="coerce")
"coerce": Converts invalid values to NaN instead of raising an error.

Convert Multiple Columns
To convert multiple object columns to float:

df[["col1", "col2"]] = df[["col1", "col2"]].astype(float)
Or, for all object columns:

df = df.astype({col: float for col in df.select_dtypes(include=["object"]).columns})

```

### Handling NaN
NaN can appear in object (string) columns as well, not just in numeric (float64) columns.  
This typically happens when Pandas encounters missing values in text-based columns.  
 If you manually convert a column type (astype(str)), missing values remain NaN
```
df["column_name"].fillna("", inplace=True)

df.fillna(0, inplace=True) 

```
### Rename columns
```
import pandas as pd

def rename_empty_columns(df, prefix="Unnamed"):
    """Rename empty or unnamed columns in a DataFrame with a specified prefix."""
    df.columns = [f"{prefix}_{i}" if not col.strip() or str(col).startswith("Unnamed") else col 
                  for i, col in enumerate(df.columns)]
    return df
```
### Read  CSV top and bottom:
```
def load_csv_top_part(filename, end_row):
    return pd.read_csv(filename, nrows=end_row, header=None)

def load_csv_from_row(file_name , start_row )  :
    return pd.read_csv(file_name, skiprows=start_row-1, header=None)
```

###  
```
There is pandas dataframe with columns
TEST
ITEM
TYPE
A_1
A_2
A_..
B_1
B2_..
 
If value in column TEXT if empty or NaN then it should be populated with non-empty value in row above.
The same logic should be implemented for column ITEM 

import pandas as pd

# Sample DataFrame
data = {
    "TEST": ["A", None, None, "B", None, "C"],
    "ITEM": [None, "X", None, None, "Y", None],
    "TYPE": ["T1", "T2", "T3", "T4", "T5", "T6"]
}

df = pd.DataFrame(data)

# Fill NaN values with the last non-null value above
df[['TEST', 'ITEM']] = df[['TEST', 'ITEM']].fillna(method='ffill')

# Display the updated DataFrame
print(df)


There is pandas dataframe with columns
TEST
ITEM
TYPE
A_1
A_2
A_..
B_1
B_2_..

The possible values in TYPE column are: score, val, avg
The name of rest of the columns after TYPE colums starts from A or from B
The number of A* and B* columns is not fixed.

Please create dataframe from previous one with the following columns:

1. TEST
2. ITEM
3. is start_from_A (boolean) -  based on 1st letter of columns which starts from A or B
4. suffix (extract the part of column name which starts from A or B)
5. score - should take value from corresponding A* pr B* column where  column TYPE=score
6. val - should take value from corresponding A* pr B* col where  column TYPE=val
7. avg - should take value from corresponding A* pr B* col where  column TYPE=avg

import pandas as pd

def transform_dataframe(df):
    # Identify columns starting with 'A' or 'B'
    ab_columns = [col for col in df.columns if col.startswith(('A', 'B'))]

    # Melt the DataFrame to bring A* and B* columns into rows
    df_melted = df.melt(id_vars=['TEST', 'ITEM', 'TYPE'], value_vars=ab_columns, var_name='AB_col', value_name='Value')

    # Extract the suffix from column names (A* or B*)
    df_melted['suffix'] = df_melted['AB_col'].str[2:]  # Extract after 'A_' or 'B_'

    # Determine if the first letter is A (True) or B (False)
    df_melted['is_start_from_A'] = df_melted['AB_col'].str.startswith('A')

    # Pivot to get 'score', 'val', and 'avg' values in separate columns
    df_final = df_melted.pivot_table(index=['TEST', 'ITEM', 'is_start_from_A', 'suffix'],
                                     columns='TYPE', values='Value', aggfunc='first').reset_index()

    # Rename TYPE columns properly
    df_final.columns.name = None  # Remove multi-index
    df_final = df_final.rename(columns={'score': 'score', 'val': 'val', 'avg': 'avg'})

    return df_final

# Example Usage
data = {
    "TEST": ["T1", "T2", "T3"],
    "ITEM": ["I1", "I2", "I3"],
    "TYPE": ["score", "val", "avg"],
    "A_1": [10, 20, 30],
    "A_2": [40, 50, 60],
    "B_1": [15, 25, 35],
    "B_2": [45, 55, 65]
}

df = pd.DataFrame(data)
df_transformed = transform_dataframe(df)
print(df_transformed)

```

### Melt
```
import pandas as pd

def transform_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Identify columns with prefix 'A' or 'B'
    value_columns = [col for col in df.columns if col.startswith('A') or col.startswith('B')]

    # Melt the DataFrame
    df_melted = df.melt(id_vars=['DATE', 'TEST'], value_vars=value_columns, 
                         var_name='full_col_name', value_name='value')

    # Extract prefix and suffix
    df_melted['is_prefix_A'] = df_melted['full_col_name'].str.startswith('A')
    df_melted['suffix'] = df_melted['full_col_name'].str[1:]  # Extract suffix

    # Select final columns
    df_result = df_melted[['DATE', 'TEST', 'is_prefix_A', 'suffix', 'value']]

    return df_result

# Example usage
file_path = "your_file.csv"  # Update with the actual file path
df_transformed = transform_csv(file_path)
print(df_transformed)


melt() reshapes the DataFrame, moving A* and B* columns into two new columns:
full_col_name → contains original column names.
value → contains corresponding values.
```



### Pandas to_sql()
```
Indexes & Primary Keys:
to_sql() does not automatically create primary keys or indexes.
You need to define them manually when creating the table.

Performance Tip: Use method='multi' for batch inserts.
 
df.to_sql('my_table', engine, if_exists='append', index=False, method='multi')
```
### Reset pandas index

https://realpython.com/pandas-reset-index/

https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas-index
```
DataFrames are two-dimensional data structures similar to spreadsheets or database tables.
A pandas DataFrame can be considered a set of columns, with each column being a pandas Series.
Each column also has a heading, which is the name property of the Series,
and each row has a label, which is referred to as an element of its associated index object.

 The default index labels are a sequence of integers, but you can use strings to make them more meaningful.
You can actually use any hashable type for your index, but integers, strings, and timestamps are the most common.
```

### There is Python pandas dataframe d1 with columns: A 
```
I need to add to d1 new columns dut, score, value and I need to populate it 
from another pandas dataframe d2 with columns A, dut, score, value
I need to add records to d1 from d2 based on matching of column A:
   add columns score and value to d1 from d2
   for rec in df2.iterrows():
       # add  rec['dut], red['score], rec['value'] to df1

import pandas as pd

# Example function for computing score
def func(c_value):
    return c_value * 2  # Replace this with your actual function

# Sample DataFrames
d1 = pd.DataFrame({'A': [1, 2, 3]})
d2 = pd.DataFrame({'A': [1, 2, 3, 4], 'b': ['x', 'y', 'z', 'w'], 'c': [10, 20, 30, 40]})

# Iterate over rows in d2 and update d1
for _, rec in d2.iterrows():
    score = func(rec['c'])
    d1.loc[d1['A'] == rec['A'], ['b', 'score']] = rec['b'], score

print(d1)

Explanation:
Define func(c_value) → This calculates the score based on column c in d2.
Iterate over d2 using iterrows().
For each row in d2, find the matching A value in d1.
Update d1 with:
b from d2
score calculated from func(d2['c'])

Alternative (Vectorized Approach - Faster)
Instead of iterrows(), you can use merge and apply the function more efficiently:

 
# Merge d1 with d2 on column A
d1 = d1.merge(d2[['A', 'b', 'c']], on='A', how='left')

# Apply function to compute score
d1['score'] = d1['c'].apply(func)

# Drop 'c' since it's not needed in d1
d1.drop(columns=['c'], inplace=True)

print(d1)
✅ This is much faster than using iterrows(), especially for large datasets.


```
### Filter out rows where column 'B' starts with 'abc'

df_filtered = df[~df['B'].str.startswith('abc')]


```
There is Pandas dataframe df with columns 
- Test (string type, unique in dataframe )
- Criteria(string) - should be ignored 
All other columns are having datatype float.

Between all float columns we are interested only with columns which names do not start from "REF" and the names ends with "score" 
For every value  in Test column (which is unique)   we need to calculate 2 numbers :
N_1 : The number of  float  columns  of interest where value in below  given threshold T=90.0
N_2 : The total number of  float  columns  of interest

The result should be a python dictionary where key is the value of Test column
and the value of disctionary is a tuple of 2 elements:
The second element of tuple is a string which stores 2 numbers described above in format "N_1 / N2 "
The 1 element of tuple is a string which should be assigned to "Fail" if N1 > 0 or "Pass"  if  N_1 = 0.


import pandas as pd

# Sample DataFrame
# Assuming `df` is the DataFrame with the structure as described
# and columns ['Test', 'Criteria', ...] with float columns like 'abc_score', 'REF_something', etc.

# Define the threshold T
T = 90.0

# Filter float columns that do not start with 'REF' and end with 'score'
columns_of_interest = [col for col in df.columns if col.endswith('score') and not col.startswith('REF')]

# Initialize the result dictionary
result = {}

# Iterate over each row
for index, row in df.iterrows():
    # Extract the unique value in the 'Test' column
    test_value = row['Test']
    
    # N_1: The number of columns of interest where the value is below the threshold T
    N_1 = sum(row[col] < T for col in columns_of_interest)
    
    # N_2: The total number of columns of interest
    N_2 = len(columns_of_interest)
    
    # Determine the status: 'Pass' if N_1 == 0, else 'Fail'
    status = 'Pass' if N_1 == 0 else 'Fail'
    
    # Format the second element as "N_1 / N_2"
    ratio = f"{N_1} / {N_2}"
    
    # Assign the result in the dictionary
    result[test_value] = (status, ratio)

# Print or use the result dictionary
print(result)
```


```
There is Python pandas dataframe with columns A,B, C, D, E, F, G
Values in column A  are not unique;  the records are sorted by value in A, the repeated values are in adjusted rows.
 
Values in columns  C ,  E and G are numeric.
We need to calculate the average in column C per value in column A.
The same average calculation should be done for columns E and G.

We need to create new row in dataframe after every group in A and put 
In column A the word “Average” and populate in this row the columns C, E and G with calculated average value.

Gemini

#------------------------
def add_average_gemini(df):
#------------------------
# Group by column A and calculate averages for columns C, E, and G
 grouped_df = df.groupby('A')[['C', 'E', 'G']].mean().reset_index()

# Add a new column to indicate the group for the average rows
 grouped_df['A'] = grouped_df['A'] + '_Average'

# Combine the original DataFrame with the averaged rows
 result_df = pd.concat([df, grouped_df], sort=False)

# Sort the result DataFrame by column A and a new column indicating if it's an average row
 result_df['IsAverage'] = result_df['A'].str.endswith('_Average')
 result_df.sort_values(['A', 'IsAverage'], inplace=True)

# Drop the temporary 'IsAverage' column
 result_df.drop(columns=['IsAverage'], inplace=True)

 print(result_df)

GhatGPT
--------
import pandas as pd 
data = {
    'A': ['X', 'X', 'Y', 'Y', 'Z', 'Z', 'Z'],
    'B': [1, 2, 3, 4, 5, 6, 7],
    'C': [10, 20, 30, 40, 50, 60, 70],
    'D': [15, 25, 35, 45, 55, 65, 75],
    'E': [100, 200, 300, 400, 500, 600, 700],
    'F': [150, 250, 350, 450, 550, 650, 750],
    'G': [1000, 2000, 3000, 4000, 5000, 6000, 7000]
}

df = pd.DataFrame(data)

def add_average_rows(df):
    # Create an empty list to store the new DataFrame rows
    new_rows = []
    
    # Group by column 'A'
    for key, group in df.groupby('A'):
        # Append the original rows to new_rows
        new_rows.append(group)
        
        # Calculate the averages for columns C, E, and G
        avg_c = group['C'].mean()
        avg_e = group['E'].mean()
        avg_g = group['G'].mean()
        
        # Create a new row with 'Average' in column 'A' and the calculated averages
        average_row = {
            'A': 'Average',
            'B': None,
            'C': avg_c,
            'D': None,
            'E': avg_e,
            'F': None,
            'G': avg_g
        }
        
        # Append the average row to new_rows
        new_rows.append(pd.DataFrame([average_row]))
    
    # Concatenate all the rows (including the new average rows) into a new DataFrame
    new_df = pd.concat(new_rows, ignore_index=True)
    
    return new_df

# Apply the function to the DataFrame
new_df = add_average_rows(df)
print(new_df)
```
### pandas map()
```
import pandas as pd
columns=['A','B']
data=[['tom',10], ['mike',20]]
df=pd.DataFrame(data, columns=columns)
d={}
d['tom']='A'
d['mike']='B'
df['x'] = df['A'].map(d).fillna('default')
 
df
      A   B  x
0   tom  10  A
1  mike  20  B
```


https://jakevdp.github.io/blog/2017/03/03/reproducible-data-analysis-in-jupyter/

https://habr.com/ru/articles/805271/   Pandas

https://github.com/adamerose/pandasgui

https://habr.com/ru/companies/otus/articles/805801/ Time series

https://arrow.apache.org/datafusion/user-guide/introduction.html  Apache DataFusion 

https://github.com/DataForScience/   Interesting jupyter notebooks to study

### Export Jupyter notebooks to other formats

https://nbconvert.readthedocs.io/en/latest/usage.html#supported-output-formats

jupyter nbconvert --to FORMAT notebook.ipynb

FORMAT can be : html, pdf, etc

### SQL from Jupyter notebooks

https://github.com/ploomber/jupysql

https://jupysql.ploomber.io/

https://habr.com/ru/companies/wunderfund/articles/792970/

pip install jupysql sqlalchemy-redshift redshift-connector 'sqlalchemy<2'

 следующий фрагмент кода для создания объекта sqlalchemy.engine для Redshift:
```
from os import environ
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
 
user = environ["REDSHIFT_USERNAME"]
password = environ["REDSHIFT_PASSWORD"]
host = environ["REDSHIFT_HOST"]
 
url = URL.create(
    drivername="redshift+redshift_connector",
    username=user,
    password=password,
    host=host,
    port=5439,
    database="dev",
)
 
engine = create_engine(url)

%sql engine --alias redshift-sqlalchemy
```

С этого момента всё выглядит крайне просто — берём «магическую» команду и пишем любые запросы, которые нужно выполнить. Их результаты попадут в выходные данные ячейки:

%sql
SELECT * FROM public.ecommerce_purchases WHERE product_id = 123

### Data Science Portfolio

https://dagshub.com/kingabzpro

https://www.datascienceportfol.io/abid

https://www.youtube.com/watch?v=D9CLhQdLp8w  How to Make a Data Science Portfolio With GitHub Pages (2023)

https://www.youtube.com/watch?v=MRGw1dq43hQ


https://www.kdnuggets.com/5-free-platforms-for-building-a-strong-data-science-portfolio

https://365datascience.com/career-advice/how-to-build-a-data-science-portfolio/

convert Jupyter notebook to pdf, laxet pypdf

https://habr.com/ru/companies/lanit/articles/777514/


https://medium.com/@techlatest.net/using-jupyter-notebook-with-big-data-a-guide-on-how-to-use-jupyter-notebook-with-big-data-f473af87185b


 GitHub doesn't render large Jupyter Notebooks, so just in case, here is an nbviewer link to the notebook:

https://nbviewer.jupyter.org/url/github.com/pathwaycom/pathway-examples/blob/main/showcases/live-data-jupyter.ipynb

Want to run the code yourself? Here is a binder link to start your own Jupyter server and try it out!

https://mybinder.org/v2/gh/pathwaycom/pathway-examples/main?filepath=showcases%2Flive-data-jupyter.ipynb

### Numpy

https://habr.com/ru/articles/784978/

https://realpython.com/numpy-example/

### PyGWalker

https://medium.com/@fareedkhandev/best-data-analysis-library-in-python-ad2572288017

https://www.youtube.com/watch?v=ogyxjkYRgPE 

### How to share Jupyter notebook
https://medium.com/@techlatest.net/sharing-jupyter-notebooks-a-blog-post-on-how-to-share-jupyter-notebooks-with-others-including-how-2f5632a54f2d

https://www.fast.ai/2022/07/28/nbdev-v2/

###  Dataframe visualizer
https://docs.profiling.ydata.ai/   Data quality   it supports both Pandas Dataframes and Spark Dataframes.

https://towardsdatascience.com/awesome-data-science-tools-to-master-in-2023-data-profiling-edition-29d29310f779

https://www.bitrook.com/blog/exploratory-data-analysis-comparison

https://pub.towardsai.net/5-python-packages-for-effortless-eda-94abddac3bc5


### Git and Jupyter notebooks
https://news.ycombinator.com/item?id=36629055
https://www.reviewnb.com/git-jupyter-notebook-ultimate-guide


Start every notebook as
```
    %load_ext autoreload
    %autoreload 2
```    

One alternative to loading models in .py scripts is making use of joblib's dump() and load() methods for pipelines.  
https://joblib.readthedocs.io/en/latest/generated/joblib.dump.html
That way, if you put your classifiers in joblib pipelines, once you're done with fitting steps you can just export your trained classifier with:
```
    joblib.dump(pipe, "trained_classifier.dump")
And resume your work with:
    joblib.load("trained_classifier.dump")
    
 ````   
Considering this works for any Python object, a lot of heavy lifting can be exported 
for later (swift) use this way.



https://github.com/mwouts/jupytext  Notebook which works with regular .py files

Как встроить блокнот Jupyter на любой сайт
https://habr.com/ru/company/skillfactory/blog/659279/

https://github.com/topics/big-data?l=jupyter+notebook

Useful extension for Jupyter: hinterland

https://towardsdatascience.com/the-only-auto-completion-extension-youll-ever-need-for-your-jupyter-notebooks-87bbaecb7126

### Read big csv file fast - use datatable
```
import datatable as dt
import pandas as pd
def read_fast_csv(f):
    frame = dt.fread(f)
    ds = frame.to_pandas()
    return ds
```



### Polars Lightning-fast DataFrame library for Rust and Python

https://www.pola.rs/

https://github.com/ddotta/awesome-polars

https://news.ycombinator.com/item?id=30589250

https://github.com/machow/siuba

###   Ibis   Python dataframe library
https://ibis-project.org/

### NumPy

https://betterprogramming.pub/a-comprehensive-guide-to-numpy-data-types-8f62cb57ea83

https://www.labri.fr/perso/nrougier/from-python-to-numpy/

https://www.youtube.com/watch?v=DcfYgePyedM

https://www.youtube.com/watch?v=DcfYgePyedM . NumPy


<https://habr.com/ru/post/469355/> NumPy
```
http://scipy.github.io/old-wiki/pages/NumPy_for_Matlab_Users.html
https://realpython.com/numpy-array-programming/	
http://nbviewer.jupyter.org/github/vlad17/np-learn/blob/master/presentation.ipynb?flush_cache=true NumPy
http://www.labri.fr/perso/nrougier/from-python-to-numpy/
https://docs.scipy.org/doc/numpy-1.10.0/user/basics.broadcasting.html
https://www.analyticsvidhya.com/blog/2017/02/top-28-cheat-sheets-for-machine-learning-data-science-probability-sql-big-data/
http://www.labri.fr/perso/nrougier/teaching/numpy.100/index.html
https://www.datacamp.com/community/tutorials/python-numpy-tutorial
https://www.dataquest.io/blog/numpy-tutorial-python/
https://www.python-course.eu/numpy.php
https://github.com/Kyubyong/numpy_exercises
 
http://cs231n.github.io/python-numpy-tutorial/
https://github.com/HIPS/autograd
https://www.machinelearningplus.com/101-numpy-exercises-python/
```

https://medium.com/codex/how-to-set-up-and-run-python-data-science-development-environment-with-jupyter-on-docker-17e04e11d6c



### Vectorized pandas operations:

https://solothought.com/tutorial/python-pandas-visual/

Use pandas best practises:
  
https://habr.com/ru/company/wunderfund/blog/682388/

https://newtechaudit.ru/pochemu-vash-pandas-rabotaet-v-3000-raz-medlennee/

https://python.plainenglish.io/pandas-how-you-can-speed-up-50x-using-vectorized-operations-d6e829317f30


https://cdanielaam.medium.com/essential-mathematical-equations-for-predictive-models-fcb79630ec96

### Exploratory Data Analysis (EDA)
https://lux-api.readthedocs.io/en/latest/index.html  visual data exploration

https://towardsdatascience.com/summarize-pandas-data-frames-b9770567f940 Skimpy is a convenient way to generate quick summaries of any dataset, even without writing any code.

https://pkghosh.wordpress.com/2020/07/13/learn-about-your-data-with-about-seventy-data-exploration-functions-all-in-one-python-class/

https://medium.com/trymito/9-simple-python-functions-that-will-speed-up-your-exploratory-data-analysis-efaa6de9f8bb

<https://realpython.com/python-statistics/>

<https://realpython.com/pandas-python-explore-dataset/>


<https://hi-bumblebee.com/> Visually explore and analyze Big Data from any Jupyter Notebook

https://subhash-achutha.medium.com/10-automating-eda-tools-65e1065636ae
 

<https://cloudblogs.microsoft.com/opensource/2019/10/10/microsoft-open-sources-sanddance-visual-data-exploration-tool/>
SandDance   visualization tool from Microsoft Research

### SQLite
```
import pandas as pd
from sqlite3 import connect
df = pd.DataFrame([['a', 'b', 'c', 'd', 'e'], [100, 200, 300, 400, 500]]).T
df

conn = connect(':memory:')
df.to_sql('test_data', conn)
pd.read_sql('SELECT [0] FROM test_data WHERE [1]>200', conn)
```

### Jupyter books
https://jupyterbook.org/intro.html

https://executablebooks.org/en/latest/gallery.html

https://www.pola.rs/ - fast dataframe

### Panda tricks

https://tomaugspurger.github.io/

https://towardsdatascience.com/4-pandas-functions-that-i-wish-i-knew-earlier-1edcc3a491bb


https://medium.com/gustavorsantos/pandas-query-the-easiest-way-to-filter-data-39e0163ef35a

https://towardsdatascience.com/25-pandas-functions-you-didnt-know-existed-p-guarantee-0-8-1a05dcaad5d0 

https://habr.com/ru/company/skillfactory/blog/573154/

https://towardsdatascience.com/heres-the-most-efficient-way-to-iterate-through-your-pandas-dataframe-4dad88ac92ee

https://levelup.gitconnected.com/my-favorite-pandas-method-chains-1cf36483e6c9

https://realpython.com/python-pandas-tricks/

https://medium.com/gustavorsantos/8-things-you-dont-know-about-pandas-groupby-8df17c2281e4

https://tomaugspurger.github.io/modern-1-intro.html modern Pandas

https://towardsdatascience.com/a-better-way-for-data-preprocessing-pandas-pipe-a08336a012bc

https://pandas.pydata.org/pandas-docs/stable/pandas.pdf Documentation

Add style to dataframe cells:
https://www.analyticsvidhya.com/blog/2021/06/style-your-pandas-dataframe-and-make-it-stunning/


https://stackoverflow.com/questions/36921951/truth-value-of-a-series-is-ambiguous-use-a-empty-a-bool-a-item-a-any-o

https://stackoverflow.com/questions/19124601/pretty-print-an-entire-pandas-series-dataframe

https://towardsdatascience.com/do-you-use-apply-in-pandas-there-is-a-600x-faster-way-d2497facfa66

https://duckdb.org/2021/05/14/sql-on-pandas.html Pandas frame + DuckDB

https://github.com/MathInspector/MathInspector

https://habr.com/ru/company/skillfactory/blog/542870/ Jupyter add-ins

https://towardsdev.com/tricks-and-best-practices-from-kaggle-794a5914480f

https://pythonnumericalmethods.berkeley.edu/notebooks/chapter25.03-Regression.html


https://jbencook.com/binary-cross-entropy/ 

The most common loss function for training a binary classifier is binary cross entropy (sometimes called log loss). You can implement it in NumPy as a one-liner:
```
def binary_cross_entropy(yhat: np.ndarray, y: np.ndarray) -> float:
    """Compute binary cross-entropy loss for a vector of predictions

    Parameters
    ----------
    yhat
        An array with len(yhat) predictions between [0, 1]
    y
        An array with len(y) labels where each is one of {0, 1}
    """
    return -(y * np.log(yhat) + (1 - y) * np.log(1 - yhat)).mean()
```

### Reading file (json, Excel, parquet , csv, etc) into DataFrame

https://gretel.ai/blog/a-guide-to-load-almost-anything-into-a-dataframe

https://towardsdatascience.com/all-pandas-json-normalize-you-should-know-for-flattening-json-13eae1dfb7dd

https://www.kaggle.com/jboysen/quick-tutorial-flatten-nested-json-in-pandas

### Sorting in pandas

https://realpython.com/pandas-sort-python/

https://jbencook.com/pandas-query/

### Dropping rows and columns

https://www.wrighters.io/how-to-remove-a-column-from-a-dataframe/

```
df.drop('b', axis=1)         # drop a column
df.drop('b', axis='columns') # same
df.drop(columns='b')         # same
df.drop(columns=['b'])       # same
```

### pandas melt
https://pub.towardsai.net/understanding-pandas-melt-pd-melt-362954f8c125
```
The Pandas melt() function is within many other methods used to reshape the pandas DataFrames 
from wide to a long format which is particularly useful in data science. 
However, the pd.melt() function is the most efficient and flexible among them. 
The pd.melt() function unpivots/melts the pandas DataFrame from a wide to a long format.
```

### pandas query
https://jbencook.com/pandas-query/
```
df.query("region == 'APAC' and revenue < 300")

avg_revenue = df.revenue.mean()
std_revenue = df.revenue.std()
df.query("revenue > @avg_revenue + @std_revenue")

df.query("revenue > revenue.mean() + revenue.std()").   # same as 3 lines above

valid_dates = ["1999-01-02", "1999-01-03", "1999-01-04"]
df.query("date in @valid_dates")
```


```
np.random.seed(0)
x = 10 * np.random.rand(100)

def model(x, sigma=0.3):
    fast_oscillation = np.sin(5 * x)
    slow_oscillation = np.sin(0.5 * x)
    noise = sigma * np.random.randn(len(x))

    return slow_oscillation + fast_oscillation + noise

plt.figure(figsize = (10,8))
y = model(x)
plt.errorbar(x, y, 0.3, fmt='o') .   ----- use it!
plt.show()


from sklearn.neural_network import MLPRegressor

mlp = MLPRegressor(hidden_layer_sizes=(200,200,200), \
                   max_iter = 2000, solver='lbfgs', \
                   alpha=0.01, activation = 'tanh', \
                   random_state = 8)

xfit = np.linspace(0, 10, 1000)
ytrue = model(xfit, 0)
yfit = mlp.fit(x[:, None], y).predict(xfit[:, None])

plt.figure(figsize = (10,8))
plt.errorbar(x, y, 0.3, fmt='o')
plt.plot(xfit, yfit, '-r', label = 'predicted', \
         zorder = 10)
plt.plot(xfit, ytrue, '-k', alpha=0.5, \
         label = 'true model', zorder = 10)
plt.legend()
plt.show()
```


### Julia
<https://habr.com/ru/post/519930/> Julia language

https://datasciencejuliahackers.com/

https://lwn.net/SubscriberLink/835930/47c363bef07134a4/  Pluto - Notebook for Julia (similar to Jupyter)


### Correlation
https://www.codementor.io/@ng3687/correlation-matrix-in-excel-python-and-r-1a6i5puowo. correlation matrix

https://towardsdatascience.com/the-fastest-way-to-visualize-correlation-in-python-ce10ed533346

df.corr().style.background_gradient(cmap="Blues")


<https://github.com/alandefreitas/matplotplusplus> C++

<http://scidavis.sourceforge.net/>

### Scipy

http://scipy-lectures.org/index.html


### Pandas

https://pythonspeed.com/articles/pandas-sql-chunking/ solve out of memory problem


If you absolutely must iterate over the rows in your DataFrame, use the .itertuples() method:
```
for row in df.itertuples():
    print(row.Index, row.date)
```    


https://chrisalbon.com/

https://github.com/jvns/pandas-cookbook

https://pandas.pydata.org/docs/getting_started/index.html

https://hackersandslackers.com/series/data-analysis-pandas/

https://towardsdatascience.com/pandas-full-tutorial-on-a-single-dataset-4aa43461e1e2

https://nbviewer.jupyter.org/github/changhiskhan/talks/blob/master/pydata2012/pandas_timeseries.ipynb

A Series has one axis, the index. A DataFrame has two axes, the index and the columns.

It’s useful to note here that in all the DataFrame functions that can be applied to either rows or columns,
an axis of 0 refers to the index, an axis of 1 refers to the columns



 Jake Vanderplas . <https://jakevdp.github.io/PythonDataScienceHandbook/>
 ```
 df.info() 
 df.describe()
 df.dtypes   
 df.index    
 df.shape   
 df.columns 
 ```
 
 <https://realpython.com/courses/idiomatic-pandas-tricks-features-you-may-not-know/>
 
 
<https://towardsdatascience.com/pandas-tips-that-will-save-you-hours-of-head-scratching-31d8572218c9>

 
https://stackoverflow.com/questions/29432629/correlation-matrix-using-pandas

https://github.com/adamerose/pandasgui


<https://machinelearningmastery.com/calculate-feature-importance-with-python/>


### pivot transpose assign


https://spapas.github.io/2016/09/21/pandas-pivot-table-primer/

https://machinelearningknowledge.ai/pandas-assign-pandas-transpose-pandas-pivot/


### data describe


https://medium.com/spatial-data-science/4-tools-to-speed-up-exploratory-data-analysis-eda-in-python-e240ebcd18de

https://github.com/adamerose/pandasgui

https://github.com/data-describe/data-describe

###  pandas-profiling:
https://github.com/JosPolfliet/pandas-profiling

https://habr.com/ru/company/ruvds/blog/451478/ 
 

Результаты её работы выражаются не в виде неких отдельных показателей,
а в форме довольно подробного HTML-отчёта, содержащего большую часть тех сведений об анализируемых данных, 
которые может понадобиться знать перед тем, как приступать к более плотной работе с ними.


http://www.dataschool.io/easier-data-analysis-with-pandas/

https://news.ycombinator.com/item?id=16473482

http://nbviewer.jupyter.org/github/pybokeh/jupyter_notebooks/blob/master/pandas/PandasCheatSheet.ipynb

https://jakevdp.github.io/PythonDataScienceHandbook/

https://www.kaggle.com/learn/data-visualisation

https://medium.com/dunder-data/selecting-subsets-of-data-in-pandas-6fcd0170be9c

Summarizing data with Pandas crosstab

https://towardsdatascience.com/summarizing-data-with-pandas-crosstab-efc8b9abecf


https://towardsdatascience.com/how-to-learn-pandas-108905ab4955

http://blog.enthought.com/python/pandas/cheat-sheets-pandas-the-python-data-analysis-library/#.WjSdBlQ-dp9
'
https://habrahabr.ru/company/ods/blog/322626/

https://www.dataquest.io/blog/pandas-big-data/

https://www.dataquest.io/blog/machine-learning-python/

https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python

http://hypertools.readthedocs.io/en/latest/index.html


### Scatter matrix plot (Pair Plot) in Pandas

  the relationship of every pair of parameters. If you've worked with other libraries, this type of plot might be familiar to you as a pair plot.

To plot Scatter Matrix, we'll need to import the scatter_matrix() function from the pandas.plotting module.

The syntax for the scatter_matrix() function is:

```
pandas.plotting.scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, grid=False, diagonal='hist', marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05, **kwargs)

 
Since we're plotting pair-wise relationships for multiple classes, on a grid - 

all the diagonal lines in the grid will be obsolete since it compares the entry with itself. Since this would be dead space, 
diagonals are replaced with a univariate distribution plot for that class.

The diagonal parameter can be either 'kde' or 'hist' for either Kernel Density Estimation or Histogram plots.

Let's make a Scatter Matrix plot:

import pandas as pd 
import matplotlib.pyplot as plt
import scipy
from pandas.plotting import scatter_matrix

menu = pd.read_csv('indian_food.csv')

scatter_matrix(menu,diagonal='kde')

plt.show()
```
### DSP

https://greenteapress.com/thinkdsp/html/index.html

<https://github.com/capitanov/dsp-theory> . DSP ins Jupiter (ru)

https://diegoinacio.github.io/computer-vision-notebooks/ Comp vision, DSP and ML

<https://habr.com/ru/post/460445/> DSP Signal Processing

### Jupyter


<https://ljvmiranda921.github.io/notebook/2020/03/16/jupyter-notebooks-in-2020-part-2/>

https://habr.com/ru/company/ruvds/blog/505624/. HiSpeed DataFrames: Dask Vuex

<https://habr.com/ru/post/500162/>

<https://www.dataschool.io/cloud-services-for-jupyter-notebook/>

<https://habr.com/ru/post/485318/> Добавляем в Jupyter Notebooks красоту и интерактивность

https://towardsdatascience.com/how-to-produce-interactive-matplotlib-plots-in-jupyter-environment-1e4329d71651   Interactive Matplotlib Plots in Jupyter  


<https://towardsdatascience.com/integrate-jupyter-into-your-data-pipeline-9a02fab3cee5>


<https://youtu.be/0Ol3QkdCyAk>. Pair Plot for multivariable analysis


```
import os
import platform
from platform import python_version
import jupyterlab
import numpy as np
import pandas as pd
print("System")
print("os name: %s" % os.name)
print("system: %s" % platform.system())
print("release: %s" % platform.release())
print()
print("Python")
print("version: %s" % python_version())
print()
print("Python Packages")
print("jupterlab==%s" % jupyterlab.__version__)
print("pandas==%s" % pd.__version__)
print("numpy==%s" % np.__version__)
```
### Check duplicates in DataFrame
```
assert len(df[df.index.duplicated()]) == 0, "Dataframe has duplicates")
```
### Set defalut plot size:
```
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rc('figure', figsize=(10, 8))

x = [5, 2, 9, 4, 7]   
y = [10, 5, 8, 4, 2]
width=30
height=10
plt.rcParams['figure.figsize'] = [width, height]
plt.plot(x, y)


mpl.__version__
```
### Merge  dataframes in Pandas  merge() join() append() concat()

https://realpython.com/pandas-merge-join-and-concat/

https://www.dataquest.io/blog/pandas-concatenation-tutorial/
 
https://stackabuse.com/how-to-merge-dataframes-in-pandas/

```
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
	 
df3_merged = pd.merge(df1, df2)	 

```
If both of our DataFrames have the column user_id with the same name, the merge() function automatically joins two tables matching on that key. If we had two columns with different names, we could use left_on='left_column_name' and right_on='right_column_name' to specify keys on both DataFrames explicitly.	 

When the default value of the how parameter is set to inner, a new DataFrame is generated from the intersection of the left and right DataFrames. 

There are times we want to use one of the DataFrame as the main DataFrame and include all the rows from even if they don't all intersect with each other. 
```
df_left = pd.merge(df2, df1, how='left', indicator=True)
df_outer = pd.merge(df2, df1, how='outer', indicator=True)
```

We also added the indicator flag and set it to True so that Pandas adds an additional column _merge to the end of our DataFrame.

This column tells us if a row was found in the left, right or both DataFrames.


#### Merge DataFrames Using join()

Unlike merge() which is a method of the Pandas instance, join() is a method of the DataFrame itself. This means that we can use it like a static method on the DataFrame: DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False).

The DataFrame we call join() from will be our left DataFrame. The DataFrame in the other argument would be our right DataFrame.

The on parameter can take one or more (['key1', 'key2' ...]) arguments to define the matching key, while how parameter takes one of the handle arguments (left, right, outer, inner), and it's set to left by default.

Let's try to join df2 to df1:
```
df_join = df1.join(df2, rsuffix='_right')
```

#### Indexing time series in Pandas
https://www.wrighters.io/indexing-time-series-data-in-pandas/  

#### Filling the gaps - and resample:

```
import pandas as pd

df = pd.DataFrame({
 'Time': [ '2019-08-01', '2019-08-02', '2019-08-03', '2019-08-06',  '2019-08-09'  ],
 'Val': [ 10, 20, 30, 40, 50 ],
 'Name':['A','B','C','D','E']
})
df['Time'] = pd.to_datetime(df['Time'])
df.set_index('Time', inplace=True)
idx=pd.date_range(start=df.index[0], end=df.index[-1], freq='D')  # assumes it sorted by index?
df=df.reindex(idx)
print(df)

             Val Name
2019-08-01  10.0    A
2019-08-02  20.0    B
2019-08-03  30.0    C
2019-08-04   NaN  NaN
2019-08-05   NaN  NaN
2019-08-06  40.0    D
2019-08-07   NaN  NaN
2019-08-08   NaN  NaN
2019-08-09  50.0    E

# fill NA  with 0
df=df.fillna(0) .  
print(df)
```

Convert time column to datetime:
```
df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df = df.set_index('Timestamp')
```
When you reindex as below, any missing index labels become NaN values

```
df.reindex(pd.date_range(start=df.index[0], end=df.index[-1], freq='3H'))
```

### Generate sequences of fixed-frequency dates and time spans: pd.date_range()
The following generates 3 record:
```
dt  = pd.date_range("2018-01-01", periods=3, freq="H")
```
another example:
```
date_from = "2019-01-01"
date_to = "2019-01-12"
date_range = pd.date_range(date_from, date_to, freq="D")
date_range
```

### Generate data:

```
import datetime

todays_date = datetime.datetime.now().date()
from=todays_date-datetime.timedelta(10)
print(from)
size=10
dates = pd.date_range(from, periods=size, freq='D')

rando_nums = np.random.normal(size=size)

columns = ['rando']
df = pd.DataFrame(rando_nums, index=dates, columns=columns)
print (df)
df.plot().get_figure()
```
### Resample

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.resample.html

https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook-resample

resample() is a time-based groupby, followed by a reduction method on each of its groups.

Resampling or converting a time series to a particular frequency:

```
idx = pd.date_range("2018-01-01", periods=5, freq="H")

rng = pd.date_range("1/1/2012", periods=100, freq="S")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample("5Min").sum()
```

Another resampling example:

```
df.groupby('house').resample('D').mean().head(4)
```

https://predictivehacks.com/how-to-unlock-the-power-of-datetime-in-pandas/




https://stackoverflow.com/questions/40419060/search-missing-timestamp-and-display-in-python



Step 1: create the range with fixed: 
```
r  = pd.date_range(start=df["date"].min(), end=df["date"].max(), freq='H')
```
Step 2: reindex and fill the gaps with any value (2.0 below):
```
df = df.set_index('date').reindex(r).fillna(2.0).rename_axis('date').reset_index()
```

#### Create DatetimeIndex and resampling example

```
import pandas as pd

df = pd.DataFrame({
 'Time': [ '2019-08-01', '2019-08-02', '2019-08-03', '2019-08-04',  '2019-08-04 00:10'  ],
 'Val': [ 10, 20, 30, 40, 50 ],
 'Name':['A','B','C','D','E']
})


print(df.info())
print(df.dtypes)
print("-- to date --")

df['tmp']=pd.to_datetime(df['Time'])
df.set_index('tmp', inplace = True)
df.drop('Time', axis=1, inplace=True)


print( df['Val'].agg(['sum', 'mean']) )


d=df['Val'].resample('D').sum()
w=df['Val'].resample('W').sum()
m=df['Val'].resample('M').sum()

print(" resample day ")
print(d)
print(" resample week ")
print(w)
print(" resample month ")
print(m)

h=df['Val'].resample('1H').sum()
print(" resample 1 hour sum ")
print(h)
```
Result of resample('1H')  - it fills gaps:
```
 resample 1 hour sum
tmp
2019-08-01 00:00:00    10
2019-08-01 01:00:00     0
2019-08-01 02:00:00     0
2019-08-01 03:00:00     0
2019-08-01 04:00:00     0
                       ..
2019-08-03 20:00:00     0
2019-08-03 21:00:00     0
2019-08-03 22:00:00     0
2019-08-03 23:00:00     0
2019-08-04 00:00:00    90
Freq: H, Name: Val, Length: 73, dtype: int64
```


### Groupby apply map lambda

https://predictivehacks.com/pandas-groupby-tips/
```
df.groupby('Gender')['ColA'].mean().   -> will create Index 'Gender'

df.groupby('Gender')['ColA'].mean().reset_index().  -> will NOT create Index 'Gender'

df.groupby('Gender', as_index=False)['ColA'].mean(). ->  -> will NOT create Index 'Gender'

df.groupby(['Gender', 'Type'])['ColA'].mean()


grouped = df.groupby('Type')
for g in grouped:
    print(g)


grouped.get_group('b')

df.groupby('Gender').agg({'ColA':['mean', 'var'], 
                          'ColB':['min', 'max'] })


df.groupby('Gender').agg({'ColA':[('ColA_Mean','mean'), ('ColA_Var', 'var')], 
                          'ColB':[('ColB_Min','min'), ('ColB_Max', 'max')] })

```
https://queirozf.com/entries/pandas-dataframe-groupby-examples

<https://pbpython.com/groupby-agg.html>

### Create a scatter plot of a column against the index
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.DataFrame({'Col': np.random.uniform(size=1000)})
plt.scatter(dataframe.index, dataframe['Col'])

df.reset_index().plot.scatter(x='level_0', y='price')


rng = date_range('1/1/2011', periods=72, freq='H')
ts =pd.Series(np.random.randn(len(rng)), index=rng)

>>> rng.freq
<1 Hour>
>>> rng.freqstr
'H'
Similary for series indexed with this index

>>> ts.index.freq

import pandas as pd
pd.infer_freq(ts.index)
```

On a DataFrame, a single argument to .loc will return a Series for the row matching the label.

 .loc attribute  is intended for selection and indexing by label
.iloc is a   method for use with purely integer based indexing, starting from 0. 

## filter

http://heydenberk.com/blog/posts/demystifying-pandas-numpy-filtering/

<https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html>

<https://kanoki.org/2020/01/21/pandas-dataframe-filter-with-multiple-conditions/> filter dataframes

```


newdf = df[(df.origin == "JFK") & (df.carrier == "B6")]
newdf = df.query('origin == "JFK" & carrier == "B6"')
newdf = df.loc[(df.origin == "JFK") & (df.carrier == "B6")]

 include all the flight details where origin is either JFK or LGA.
 newdf = df[df.origin.isin(["JFK", "LGA"])]
```

<https://habr.com/ru/company/ruvds/blog/492220/>. Pandas

<https://towardsdatascience.com/stop-persisting-pandas-data-frames-in-csvs-f369a6440af5>

https://habr.com/ru/company/ruvds/blog/500428/

<https://habr.com/ru/post/475210/>. Pandas



### Filling gaps in data
```
df[‘day_time’] = pd.to_datetime(df[‘day_time’], format=’%Y-%m-%d %H:%M:%S’)

full_idx = pd.date_range(start=df[‘day_time’].min(), end=df[‘day_time’].max(), freq=’30T’)
df = (
 df
 .groupby(‘LCLid’, as_index=False) 
 .apply(lambda group: group.reindex(full_idx, method=’nearest’)) 
 .reset_index(level=0, drop=True) 
 .sort_index() 
)
```

### Caching pandas dataframe to local disk (pickle):
```
An example for a pandas.DataFrame:

  Store your DataFrame
df.to_pickle('cached_dataframe.pkl') # will be stored in current directory

  Read your DataFrame
df = pandas.read_pickle('cached_dataframe.pkl') # read from current directory
The same methods also work for pandas.Series:

  Store your Series
series.to_pickle('cached_series.pkl') # will be stored in current directory

  Read your DataFrame
series = pandas.read_pickle('cached_series.pkl') # read from current directory
```
## Access Databases from Pandas

<https://medium.com/jbennetcodes/how-to-use-pandas-to-access-databases-e4e74e6a329e> 
```
import MySQLdb as mdb
user = 'YOURUSERNAME'
passwd = 'YOURPASSWORD'
con = mdb.connect(
                host = '127.0.0.1', user = user, passwd = passwd) #optional - db="schema_name"
cursor = con.cursor() 
cursor.execute("SHOW DATABASES")  # running SQL
print  (cursor.fetchall())
cursor.execute("USE world")
cursor.execute("SELECT * FROM country WHERE population>200000000")
for i in range(cursor.rowcount):
    row = cursor.fetchone()
    print (row)
    
cursor.execute("SELECT * FROM students ")
print cursor.fetchall()

cursor.close()
con.close()    
```
## Virtual env in Jupyter Notebook
https://janakiev.com/blog/jupyter-virtual-envs/

##   Pandas NumPy Scikit

<https://habr.com/ru/company/plarium/blog/512332/>. scikit

<https://www.youtube.com/playlist?list=PL5-da3qGB5IBITZj_dYSFqnd_15JgqwA6>








<https://github.com/pandas-profiling/pandas-profiling>

```
jupyter notebook
http://localhost:8888/tree

https://realpython.com/python-statistics/


import math
import statistics
import numpy as np
import scipy.stats
import pandas as pd


to do:
there are 100 cvs files without headers6 columns;   group them by 1st digits in 10 groups
make report with columns:
    file_name 
    # of records
    col1 min/max/avg
    col2 min/max/avg
    ..
    col6 min/max/avg

import glob
files= glob.glob('./*.csv')
files.sort() 
print(files)

col_names =  ['file', 'records', 'aX-avg','aY-avg','aZ-avg','gX-avg','gY-avg','gZ-avg' ]
# https://stackoverflow.com/questions/13784192/creating-an-empty-pandas-dataframe-then-filling-it

summary_frame = pd.DataFrame(columns=col_names)
frames={}
for f in files:
   print (f)
   df = pd.read_csv('1_1.csv', delimiter = ',', header=None, names=['aX','aY','aZ','gX','gY','gZ'])
   frames[f] = df
   n_records=len(frames[f])
   summary_frame.loc[len(summary_frame)]=[
            f, 
	    n_records, 
            df["aX"].mean(), 
            df["aY"].mean(), 
            df["aZ"].mean(),
            df["gX"].mean(), 
            df["gY"].mean(), 
            df["gZ"].mean()  
	    ]
	    
import glob
files= glob.glob('./*.csv')
files.sort() 
print(files)	    

print("file, n_records, aX_mean, aX_min, aX_max,  aY_mean, aY_min, aY_max, aZ_mean, aZ_min, aZ_max, gX_mean, gX_min, gX_max,  gY_mean, gY_min, gY_max, gZ_mean, gZ_min, gZ_max")
for f in files:
   df = pd.read_csv(f, delimiter = ',', header=None, names=['aX','aY','aZ','gX','gY','gZ'])
   print( f, s, len(df), s,
            df["aX"].mean(), s,  df["aX"].min(), s, df["aX"].max(), s,
            df["aY"].mean(), s,  df["aY"].min(), s, df["aY"].max(), s,
            df["aZ"].mean(), s,  df["aZ"].min(), s, df["aZ"].max(), s,
            df["gX"].mean(), s,  df["gX"].min(), s, df["gX"].max(), s,
            df["gY"].mean(), s,  df["gY"].min(), s, df["gY"].max(), s,
            df["gZ"].mean(), s,  df["gZ"].min(), s, df["gZ"].max() 
```


To convert the data to parquet we are going to use pandas to read the csv and store it in one large parquet file:
```
import glob
import pandas as pd

files = glob.glob("input/yellow_tripdata_2018-*.csv")

def read_csv(filename):
    return pd.read_csv(
        filename,
        dtype={"store_and_fwd_flag": "bool"},
        parse_dates=["tpep_pickup_datetime", "tpep_dropoff_datetime"],
        index_col=False,
        infer_datetime_format=True,
        true_values=["Y"],
        false_values=["N"],
    )
dfs = list(map(read_csv, files))
df = pd.concat(dfs)
df.to_parquet("yellow_tripdata_2018.parquet")

The resulting parquet file has a size of 2.2GiB, while the sum of the original CSV files was 11GiB. 
Pandas supports two parquet implementations, fastparquet and pyarrow. They both have strengths and weaknessess
```
<http://peter-hoffmann.com/2020/understand-predicate-pushdown-on-rowgroup-level-in-parquet-with-pyarrow-and-python.html>
 
<https://habr.com/ru/post/486756/> .  pandas example : reads CSVs,JSOns combines, filter them



<https://pbpython.com/natural-breaks.html>

<https://www.aicheatsheets.com/>

<https://jakevdp.github.io/PythonDataScienceHandbook/>

<http://www.scikit-yb.org/en/latest/index.html> . Yellowbrick extends the Scikit-Learn API to make model selection and hyperparameter tuning easier. Under the hood, it’s using Matplotlib.





<https://habr.com/ru/post/460557/>

<https://habr.com/ru/post/470864/> Web UI for Jupiter 



<https://www.udemy.com/deep-learning-prerequisites-the-numpy-stack-in-python> free course

https://www.reddit.com/r/Python/comments/cop2cr/new_data_visualization_with_python_course_up_on/>

<https://habr.com/ru/post/460321/> ML Notebooks


<https://habr.com/ru/company/mailru/blog/445834/>


 
## Cloud Notebooks 
 
 <https://www.dataschool.io/cloud-services-for-jupyter-notebook/amp/> . Jupyter Notebook in the cloud
 
 <https://medium.com/machine-learning-world/useful-snippets-for-google-colaboratory-free-gpu-included-d976d6b3e6de>
 
## Plotting the time series

https://nbviewer.jupyter.org/github/changhiskhan/talks/blob/master/pydata2012/pandas_timeseries.ipynb

<https://kanoki.org/2019/10/09/working-with-pandas-datetime/> Working with timeseries in Pandas

<https://www.dataquest.io/blog/tutorial-time-series-analysis-with-pandas/> . Time Series

<https://www.kdnuggets.com/2020/09/introduction-time-series-analysis-python.html>

<https://analyzingalpha.com/time-series-analysis-with-python>

<https://mlcourse.ai/articles/topic9-part1-time-series/>


```
import datetime

df = pd.read_csv(‘Data/UMTMVS.csv’, index_col=’DATE’)
df.head()
df.index 
df.index = pd.to_datetime(df.index)
df.index

Now we can see that dtype of our dataset is datetime64[ns]. T
his “[ns]” shows that it is precise in nanoseconds.
We can change it to “Days” or “Months” if we want.

Alternatively, to avoid all this fuss, we can load data in single line of code using Pandas as follows.

df = pd.read_csv(‘Data/UMTMVS.csv’, index_col=’DATE’, parse_dates=True)

Here we have added parse_dates=True, so it will automatically use our index as dates.

df.index


df['Date'] = pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime('%d.%m.%Y')
df['year'] = pd.DatetimeIndex(df['Date']).year
df['month'] = pd.DatetimeIndex(df['Date']).month
df['day'] = pd.DatetimeIndex(df['Date']).day
df['dayofyear'] = pd.DatetimeIndex(df['Date']).dayofyear
df['weekofyear'] = pd.DatetimeIndex(df['Date']).weekofyear
df['weekday'] = pd.DatetimeIndex(df['Date']).weekday
df['quarter'] = pd.DatetimeIndex(df['Date']).quarter
df['is_month_start'] = pd.DatetimeIndex(df['Date']).is_month_start
df['is_month_end'] = pd.DatetimeIndex(df['Date']).is_month_end
print(df.info())

df = df.drop(['Date'], axis = 1)  -- drop column
```

 ### time-based indexing 
 ```
 df.loc['2017-08-10'] - entire  day
 df.loc['2012-02'] - entire month
 df.loc['2014-01-20':'2014-01-22'].  - inclusive!!
```
plots:
```
cols_plot = ['Consumption', 'Solar', 'Wind']
axes = opsd_daily[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)
for ax in axes:
    ax.set_ylabel('Daily Totals (GWh)')
```
year plot:
```
ax = df.loc['2017', 'Consumption'].plot()
ax.set_ylabel('Daily Consumption (GWh)');
```
<https://chrisalbon.com/python/data_wrangling/pandas_time_series_basics/>

<https://machinelearningmastery.com/time-series-data-visualization-with-python/>

<https://jakevdp.github.io/PythonDataScienceHandbook/03.11-working-with-time-series.html>

<https://machinelearningmastery.com/resample-interpolate-time-series-data-python/>

The Series Pandas object provides an interpolate() function to interpolate missing values

Between time:
<https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.between_time.html>

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.between_time.html#pandas.DataFrame.between_time
```
from datetime import datetime
# example of formatting
date = datetime.strptime('01 Jan 2016', '%d %b %Y')
print(date)
date = datetime.strptime('2017-05-04',"%Y-%m-%d")
print(date)

# generate the date objects: 2 points per day  for entire year
from datetime import timedelta  
i=0
times=[]
v=[]
date = datetime.strptime('01 Jan 2016', '%d %b %Y')

while i < 365:
  new_date= date+timedelta(hours=i*12) 
  print (i, new_date, new_date.month)  # new point every 12 hours
  times.append(new_date)
  v.append ( new_date.month)
  i+=1  
  
  
df = pd.DataFrame({'keys':times,'vals':v})  

# Grouping

# Group by Month
df.index=df["keys"]
per_month=df.groupby(pd.Grouper(freq='M'))

print (type(per_month))
print (per_month.sum())
print (type(per_month.sum()))

# Group by day of week
day_of_week= df.groupby(df.index.dayofweek).sum()

# Group by Day
per_day=df.groupby(pd.Grouper(freq='D')) - does not require index, can use several columns in groupby
per_day_sum=per_day.sum()

per_day_sum= df.resample('D').sum() --- consider this instead line above, requires df.index = DateTimeIndex

#   Plotting

import matplotlib.pyplot as plt

## Plot 1
per_day_sum.plot()

## Plot 2
df.resample('D').sum().plot()  

## Plot 3
X=per_day_sum.index
Y=per_day_sum.values
plt.plot(X,Y)
plt.show() . # issue - ticks and X labels

## Split data in separate dataframes per month

first_days = [
  datetime.date (2016, 1,1),
  datetime.date (2016, 2,1),
  datetime.date (2016, 3,1),
  datetime.date (2016, 4,1),
  datetime.date (2016, 5,1),
  datetime.date (2016, 6,1),
  datetime.date (2016, 7,1),
  datetime.date (2016, 8,1),
  datetime.date (2016, 9,1),
  datetime.date (2016, 10,1),
  datetime.date (2016, 11,1),
  datetime.date (2016, 12,1)
  ]
  
  
from pandas.tseries.offsets import MonthEnd
from datetime import timedelta 

 

per_month={}
for first_day in first_days:
    last_day=first_day+MonthEnd(1)+timedelta(hours=23, minutes=59, seconds=59)
    m=first_day.strftime('%b') . # human-readable month
    per_month[m]=per_day_sum[first_day : last_day]

# I think it is better then code above
daily_per_month={}
Month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep', 'Oct','Nov','Dec']
for i in range(0,12):
    print (i, Month[i])
    m=Month[i]
    daily_per_month[m] = per_day_sum[per_day_sum.index.month==i+1]


# Plot every month on separate figure:
per_month.plot(subplots=True, legend=True)
plt.show()

# Plot every month on the same figure:
fig, ax = plt.subplots()

for k, v in per_month.items():
 x = v.index.day
 y = v.y.values  
 ax.plot(x, y, label=k)

ax.legend(loc='upper left', frameon=False)


# Group by day of week within the month
# Make new df with index in [0-6] - (Monday-Sunday]
v=per_month['Jan']
v.rename(columns={'y': 'Jan'}, inplace=True)
df_per_dayofweek=v.groupby(v.index.dayofweek).sum()

for k, v in per_month.items():
    if k != 'Jan':
       d=v.groupby(v.index.dayofweek).sum()
       d.rename(columns={'y': k}, inplace=True)

       df_per_dayofweek = pd.merge(df_per_dayofweek, d, on='ds' )

print (df_per_dayofweek)  

df_per_dayofweek.plot.bar(rot=0)
```

## Group By and resample

<https://pbpython.com/pandas-grouper-agg.html>

<http://benalexkeen.com/resampling-time-series-data-with-pandas/>

df=df.resample(rule='W').last().  - last day of the week

if you were interested in summarizing all of the sales by month, you could use the resample function. 

The tricky part about using resample is that it only operates on an index.  In order to make it work, use set_index to make the date column an index and then resample:
```
df.set_index('date').resample('M')["ext price"].sum() .      monthly

weekly_summary = pd.DataFrame()
weekly_summary['speed'] = df["speed"].resample('W').mean() .  weekly mean
weekly_summary['price'] = df["preice"].resample('W').mean() .  weekly mean
```
<http://cmdlinetips.com/2019/03/how-to-write-pandas-groupby-function-using-sparse-matrix/>

GroupBy() is not based on dataframe  index. 


https://www.kaggle.com/learn/overview  Pandas, TensorFlow, etc

<https://github.com/Yorko/mlcourse_open/tree/master/jupyter_russian>     Jupiter Russian notebooks

<https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks#statistics-machine-learning-and-data-science>

<https://radimrehurek.com/data_science_python/>

<https://github.com/hangtwenty/dive-into-machine-learning>

<https://sadanand-singh.github.io/posts/pyplotsmultivariables/>


## Scikit-learn
<https://medium.com/analytics-vidhya/scikit-learn-a-silver-bullet-for-basic-machine-learning-13c7d8b248ee>

<https://habr.com/ru/post/456294/> One Hot Encoding

<https://www.youtube.com/watch?v=irHhDMbw3xo> categorical encoding

<https://www.youtube.com/watch?v=L7R4HUQ-eQ0>

<http://scikit-learn.org/stable/tutorial/>

<https://www.interviewqs.com/blog/intro_to_scikit_learn>

<https://stackoverflow.com/questions/40845304/runtimewarning-numpy-dtype-size-changed-may-indicate-binary-incompatibility>

## Linear interpolation

```
import numpy as np

points = [-2, -1, 0, 1, 2]
values = [4, 1, 0, 1, 4]

x = np.linspace(-2, 2, num=10)
y = np.interp(x, points, values)

import matplotlib.pyplot as plt

plt.plot(points, values, 'o')
plt.plot(x, y, 'o', alpha=0.5)

plt.xlabel("x")
plt.ylabel("y");
```

## Linear model

```
import warnings
warnings.filterwarnings("ignore", message="numpy.dtype size changed")
warnings.filterwarnings("ignore", message="numpy.ufunc size changed")
```
```
import matplotlib.pyplot as plt
from sklearn import linear_model
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
# data:
ar = np.array([[[1],[2],[3]], [[2],[4],[6]]]) # y=2*x
x = ar[0,:]
y = ar[1,:]

reg = linear_model.LinearRegression()
reg.fit(x,y)
print('Coefficients: \n', reg.coef_)

xTest = np.array([[4],[5],[6]])
ytest =  np.array([[8],[10],[12]])
preds = reg.predict(xTest)
print("Mean squared error: %.2f" % mean_squared_error(ytest,preds))
print("Variance score: %.2f" % r2_score(ytest,preds))
plt.scatter(xTest,preds, color='black')
plt.plot(xTest,preds,color='blue', linewidth=3)

plt.show()
```


```

	
http://www.zavtech.com/morpheus/docs/  DataFrames in Java

## Jupyter Enterprise Gateway 

<https://blog.jupyter.org/introducing-jupyter-enterprise-gateway-db4859f86762>

<https://jupyter-enterprise-gateway.readthedocs.io/en/latest/getting-started.html>

<https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html>

<https://github.com/jupyterhub/jupyterhub-deploy-docker>

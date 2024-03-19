### version 0
```
import pandas as pd

# Example DataFrame
data = {
    'A': ['nominator1', 'denominator1', 'nominator2', 'denominator2'],
    'float_col1': [10.0, 20.0, 0.0, 40.0],
    'float_col2': [5.0, 15.0, 0.0, 35.0]
}

df = pd.DataFrame(data)

# List of tuples
tuples_list = [('nominator1', 'denominator1'), ('nominator2', 'denominator2')]

# Create a dictionary to store the results
results_dict = {}

# Iterate over each tuple
for tup in tuples_list:
    nominator_row = df[df['A'] == tup[0]].iloc[0]
    denominator_row = df[df['A'] == tup[1]].iloc[0]

    nominator_values = nominator_row.drop('A')
    denominator_values = denominator_row.drop('A')

    # Calculate division
    result_values = nominator_values / denominator_values
    
    # Handling the case where both nominator and denominator are zero
    result_values[(nominator_values == 0) & (denominator_values == 0)] = 1

    # Store the results in the dictionary
    results_dict[tup] = result_values.values

# Create a DataFrame from the dictionary
result_df = pd.DataFrame(results_dict, index=df.columns[1:]).T
result_df.index = result_df.index.map(str)
```



### Divide row by row with handling 0/0 as 1 (version 1)
```
import pandas as pd
import numpy as np  # Import NumPy for division by zero handling

# Sample DataFrame (replace with your actual data)
data = {'A': ['Value1', 'Value2', 'Value3', 'Nominator', 'Denominator'],
        'B': [1.2, 3.4, 5.6, 7.8, 9.1],
        'C': [2.5, 4.7, 6.9, 10.2, 11.4],
        # Add more float columns as needed
        'D': [3.8, 5.1, 7.4, 12.6, 13.8]}
df = pd.DataFrame(data)

# Define list of tuples for nominator-denominator pairs (replace with your actual list)
ratio_list = [('Nominator', 'Denominator'), ('Value1', 'Value3')]

# Create an empty dictionary to store division results
division_results = {}

# Iterate through each tuple in the list
for nominator, denominator in ratio_list:
    # Filter rows based on specific values in column A
    nominator_row = df[df['A'] == nominator]
    denominator_row = df[df['A'] == denominator]

    # Check if both nominator and denominator rows are found
    if len(nominator_row) != 1 or len(denominator_row) != 1:
        print(f"Error: Nominator '{nominator}' or denominator '{denominator}' row not found, or multiple rows found.")
        continue  # Skip to the next iteration if rows not found

    # Select only float columns (excluding column A) for division
    float_cols = df.select_dtypes(include=[np.float64])

    # Calculate division element-wise for float columns
    division_result = np.true_divide(nominator_row[float_cols].iloc[0], denominator_row[float_cols].iloc[0])

    # Replace 0 / 0 with 1 using NumPy's where function
    division_result = np.where((division_result == 0) & (denominator_row.iloc[0]['A'] == 0), 1, division_result)

    # Store the division result for the specific tuple (string representation)
    division_results[(nominator, denominator)] = division_result.values.reshape(1, -1)

# Create a new DataFrame from the division results dictionary
new_df = pd.DataFrame(division_results).T  # Transpose to have ratios as columns

# Create the first column with string presentation of tuples
new_df.insert(0, 'Ratio', [f"{nom}/{denom}" for nom, denom in ratio_list])

# Print the new DataFrame
print(new_df)

```


### Divide row by row with handling 0/0 as 1 (version 2)
```
import pandas as pd
import numpy as np  # Import NumPy for division by zero handling

# Sample DataFrame (replace with your actual data)
data = {'A': ['Value1', 'Value2', 'Value3', 'Nominator', 'Denominator'],
        'B': [1.2, 3.4, 5.6, 7.8, 9.1],
        'C': [2.5, 4.7, 6.9, 10.2, 11.4],
        # Add more float columns as needed
        'D': [3.8, 5.1, 7.4, 12.6, 13.8]}
df = pd.DataFrame(data)

# Define values for nominator and denominator rows (replace with your actual values)
nominator_value = 'Nominator'
denominator_value = 'Denominator'

# Filter rows based on specific values in column A
nominator_row = df[df['A'] == nominator_value]
denominator_row = df[df['A'] == denominator_value]

# Check if both nominator and denominator rows are found
if len(nominator_row) != 1 or len(denominator_row) != 1:
    print("Error: Nominator or denominator row not found, or multiple rows found.")
else:
    # Calculate division element-wise for each column (excluding column A)
    division_result = np.true_divide(nominator_row.iloc[0], denominator_row.iloc[0])
    division_result = division_result.drop('A')  # Remove column A from the result

    # Replace 0 / 0 with 1 using NumPy's where function
    division_result = np.where((division_result == 0) & (denominator_row.iloc[0]['A'] == 0), 1, division_result)

    # Create a new DataFrame with the calculated division
    new_df = pd.DataFrame(division_result.values.reshape(1, -1), columns=division_result.index)

    print(new_df)
```


###   Apply 360 modulo to rows where metric name starts from specific pattern V1
```
import pandas as pd

# Sample DataFrame
data = {'metric': ['XXX123', 'YYY456', 'XXX789'],
        'float_column1': [100.0, 200.0, 300.0],
        'float_column2': [150.0, 250.0, 350.0]}

df = pd.DataFrame(data)

# Find the names of all float columns dynamically
float_columns = df.select_dtypes(include=['float']).columns

# Define a function to update float columns based on the condition
def update_float_columns(row):
    if row['metric'].startswith('XXX'):
        for col in float_columns:
            row[col] = row[col] % 360
    return row

# Apply the function to each row of the DataFrame
df = df.apply(update_float_columns, axis=1)

print(df)
```


### Apply 360 modulo to rows where metric name starts from specific pattern V2
```
import pandas as pd

def update_dataframe(df):
  """
  This function updates a DataFrame by applying modulo 360 to float columns
  for rows where the 'metric' column value starts with 'XXX'.

  Args:
      df (pandas.DataFrame): The DataFrame to modify.

  Returns:
      pandas.DataFrame: The modified DataFrame.
  """

  # Filter rows where 'metric' starts with 'XXX'
  filtered_df = df[df['metric'].str.startswith('XXX')]

  # Ensure float columns exist (optional)
  if not any(df.dtypes[col] == np.float64 for col in df.columns if col != 'metric'):
      print("No float columns found (excluding 'metric').")
      return df  # Return original DataFrame if no float columns

  # Select float columns (excluding 'metric')
  float_cols = [col for col in df.columns if col != 'metric' and df[col].dtypes == np.float64]

  # Apply modulo 360 for selected columns in filtered rows
  filtered_df[float_cols] = filtered_df[float_cols] % 360

  # Update the original DataFrame with the modified rows
  df.update(filtered_df)

  return df

# Create a sample DataFrame
data = {'metric': ['ABC', 'XXX_data1', 'DEF', 'XXX_data2'], 'col1': [180, 270, 390, 45], 'col2': [10, 20, 30, 90]}
df = pd.DataFrame(data)

# Apply the function to modify the DataFrame
df_modified = update_dataframe(df.copy())  # Use a copy to avoid modifying original df

print(df_modified)
```



### Apply modulo 360  to all columns containing the target string in their names
```
import pandas as pd

def apply_modulo_360(df, target_str):
  """
  This function takes a DataFrame and a target string and applies modulo 360
  to all columns containing the target string in their names.

  Args:
      df (pandas.DataFrame): The DataFrame to modify.
      target_str (str): The target string to identify columns for modification.

  Returns:
      pandas.DataFrame: The modified DataFrame with modulo 360 applied to target columns.
  """

  # Filter columns containing the target string
  filtered_cols = [col for col in df.columns if target_str in col]

  # Ensure all filtered columns have numeric data type (float)
  if not all(df[col].dtypes == np.float64 for col in filtered_cols):
      raise ValueError("Not all target columns have numeric data type (float).")

  # Apply modulo 360 operation for selected columns
  df[filtered_cols] = df[filtered_cols] % 360

  return df

# Create a sample DataFrame
data = {'col1': [180, 270, 390], 'XXX_col2': [45, 90, 135], 'col3': [10, 20, 30]}
df = pd.DataFrame(data)
target_str = "XXX"

# Apply the function to modify the DataFrame
df_modified = apply_modulo_360(df.copy(), target_str)  # Use a copy to avoid modifying original df

print(df_modified)
```



### Rename df columns
```
# Create a sample DataFrame with prefixed columns
data = {'XXX_col1': [1, 2, 3], 'XXX_col2': [4, 5, 6]}
df = pd.DataFrame(data)

Approach 1
# Remove prefix using str.replace with regex
df.columns = df.columns.str.replace('^XXX_', '', regex=True)

Approach 2

# Remove prefix using list comprehension
new_column_names = [col.replace('XXX_', '') for col in df.columns]
df.columns = new_column_names
```

### Extract val from dataframe with 1 row
```
There are two main ways to extract values for specific columns from a pandas DataFrame with exactly one row into a Python variable:

Method 1: Using .iloc[0]

This method uses integer-based indexing to access the first (and only) row of the DataFrame. You can then access specific columns by their names.

Python
import pandas as pd

# Create a DataFrame with one row
data = {'col1': [10], 'col2': ['apple']}
df = pd.DataFrame(data)

# Extract values using `.iloc[0]`
col1_value = df.iloc[0]['col1']
col2_value = df.iloc[0]['col2']

# Print the extracted values
print(f"col1 value: {col1_value}")
print(f"col2 value: {col2_value}")
Use code with caution.
Method 2: Using .squeeze()

The .squeeze() method attempts to convert the DataFrame to a Series (a one-dimensional labeled array), effectively returning the single row as a dictionary-like object. You can then access columns by their names.

Python
# Extract values using `.squeeze()`
single_row_dict = df.squeeze()
col1_value = single_row_dict['col1']
col2_value = single_row_dict['col2']

# Print the extracted values
print(f"col1 value: {col1_value}")
print(f"col2 value: {col2_value}")

```


### rows division 
pandas 1.0.5
```
    ddd = {
    'A': ['a', 'b'],
    'X': [100.0, 20.0],
    'Y': [6.0, 2.0]
}
    df = pd.DataFrame(ddd)
    df1 = df[df['A'] =='a'].reset_index(drop=True)
    df2 = df[df['A'] == 'b'].reset_index(drop=True)

    print(df1)
    print(df2)
    # do we need to specify axis=?
# below we eliminate 1st column, because it is not float , but string
    axis0 = df1.iloc[:, 1:].div(df2.iloc[:, 1:], axis=0) 
    axis1 = df1.iloc[:, 1:].div(df2.iloc[:, 1:], axis=0)





ddd = {'A': ['a', 'b'], 'X': [100.0, 20.0], 'Y': [6.0, 2.0]}
df = pd.DataFrame(ddd)

# Ensure both 'a' and 'b' exist in 'A' column before division
if ('a' not in df['A'].tolist()) or ('b' not in df['A'].tolist()):
  print("Elements 'a' and 'b' not found in column A. Division cannot be performed.")
else:
  # Select rows by value, ensuring correct alignment
  df1 = df.loc[df['A'] == 'a'].reset_index(drop=True)
  df2 = df.loc[df['A'] == 'b'].reset_index(drop=True)

  # Calculate ratios (excluding 'A' column)
  res = df1.iloc[:, 1:].div(df2.iloc[:, 1:], axis=0)
  print(res)




import pandas as pd

ddd = {
    'A': ['a', 'b'],
    'X': [100.0, 20.0],
    'Y': [6.0, 2.0]
}
df = pd.DataFrame(ddd)

# Ensure that both 'a' and 'b' are present in the original DataFrame
df = df[df['A'].isin(['a', 'b'])]

df1 = df[df['A'] == 'a']
df2 = df[df['A'] == 'b']

# Check if both 'a' and 'b' rows exist
if len(df1) == 1 and len(df2) == 1:
    res = df1.iloc[:, 1:].div(df2.iloc[:, 1:], axis=1)
    print(res)
else:
    print("Both 'a' and 'b' rows are required for division.")
```


### Calc ratio 1
```
import pandas as pd


def calculate_ratios(df, N):
  """Calculates ratios for each tuple in a new DataFrame

  Args:
      df (pandas.DataFrame): The DataFrame to filter.
      N (list): A list of tuples containing elements to match in column 'A'.

  Returns:
      pandas.DataFrame: A new DataFrame with ratios for each tuple.
  """

  result = pd.DataFrame()
  for t in N:
    # Filter rows based on tuple elements
    filtered_df = df[df['A'].isin(t)]
    # Ensure both elements from the tuple exist (at least one row in each filter)
    if len(filtered_df) == 2:
      # Select rows corresponding to tuple elements
      df1 = filtered_df[filtered_df['A'] == t[0]].reset_index(drop=True)
      df2 = filtered_df[filtered_df['A'] == t[1]].reset_index(drop=True)
      # Calculate ratios (excluding 'A' column)
      ratio_df = df1.iloc[:, 1:].div(df2.iloc[:, 1:], axis=0)
      # Create a new row with tuple string and ratios
      ratio_df = pd.DataFrame({'T': str(t), **ratio_df.to_dict()})
      result = pd.concat([result, ratio_df], ignore_index=True)
  return result


# Example usage (replace with your DataFrame and list of tuples)
df = pd.DataFrame(...)  # Create your DataFrame
N = [('X', 'Y'), ('Y', 'Z')]  # Replace with your list of tuples

result = calculate_ratios(df.copy(), N.copy())
print(result)
```
### Calc ratio 2

```
import pandas as pd

# Sample DataFrame
data = {
    'A': ['a', 'b', 'c', 'd'],
    'X': [10.0, 20.0, 30.0, 40.0],
    'Y': [5.0, 10.0, 15.0, 20.0],
    'Z': [2.0, 4.0, 6.0, 8.0]
}

df = pd.DataFrame(data)

# Sample list of tuples
tuple_list = [('a', 'b'), ('c', 'd')]

# New DataFrame
new_data = []

# Iterating over each tuple in the list
for pair in tuple_list:
    # Selecting rows corresponding to tuple[0] and tuple[1]
    row1 = df[df['A'] == pair[0]].reset_index(drop=True)
    row2 = df[df['A'] == pair[1]].reset_index(drop=True)
    
    # Calculating division for each float column
    division_result = row1.iloc[:, 1:] / row2.iloc[:, 1:]
    
    # Combining the tuple into a single string
    tuple_string = str(pair)
    
    # Appending to the new data list
    new_data.append([tuple_string] + division_result.values.tolist()[0])

# Constructing the new DataFrame
columns = ['T'] + list(division_result.columns)
new_df = pd.DataFrame(new_data, columns=columns)

print(new_df)


```


### Divide REF by other column
```
import pandas as pd

# Sample DataFrame
data = {
    'A': ['a', 'b', 'c'],
    'REF': [10.0, 20.0, 30.0],
    'X': [5.0, 10.0, 15.0],
    'Y': [2.0, 4.0, 6.0],
    'Z': [1.0, 2.0, 3.0]
}

df = pd.DataFrame(data)

# New DataFrame
new_df = pd.DataFrame()

# Copying the 'A' column
new_df['A'] = df['A']

# Calculating division for each float column except 'REF'
for col in df.columns:
    if col != 'A' and col != 'REF':
        new_df[col] = df['REF'] / df[col]

# Adding the 'REF' column
new_df['REF'] = df['REF']


```
### X
```
I have pythons pandas dataframe with following columns : column A (string datatype) and many other columns with float datatype.
Also I have python list named N which contains  the tuples.
Tuple has 2 elements.

One of the  float column names is named REF.
Please create new dataframe with the same columns as dataframe above 
Take from original dataframe  only rows where value in column A  exists in python list on tuples
The  float columns in new 
dataframe should be calculated as division of  REF column by float column in original dataframe .

import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'A': ['X', 'Y', 'X', 'Z', 'Y'],
                   'B': [1, 2, 3, 4, 5],
                   'C': [6, 7, 8, 9, 10],
                   'REF': [100, 200, 300, 400, 500]})

# Create a list of tuples
N = [('X', 'Y'), ('Y', 'Z')]


def filter_and_calculate(df, N):
  """Filters rows and calculates ratios in a new DataFrame

  Args:
      df (pandas.DataFrame): The DataFrame to filter.
      N (list): A list of tuples containing elements to match in column 'A'.

  Returns:
      pandas.DataFrame: A new DataFrame with filtered rows and calculated ratios.
  """

  filtered_df = df[df['A'].isin([i[0] for i in N]) & df['A'].isin([i[1] for i in N])]
  # Calculate ratios (excluding 'REF' and 'A' columns)
  ratios = filtered_df.iloc[:, 2:].div(filtered_df['REF'], axis=0)

  # Combine filtered DataFrame with calculated ratios
  result = pd.concat([filtered_df[['A']], ratios], axis=1)
  return result


result = filter_and_calculate(df.copy(), N.copy())
print(result)
```


###
```
data_source: blank
adhoc_label: P2P
test_date: 2024-02-26
test_dir: V:\LabTestLogs\Lab_Test\Eng_Test\TestReq-3601\02_26_2024
imu_dir:  V:\LabTestLogs\Lab_Test\Eng_Test\TestReq-3601\02_26_2024\IMU
TestCity: SF SanJose
TestType: Driving Run  Ped
TestSpot: Underbridge Tunnels  Downtown SJ HQ
TestEnv: UC OpenSky Tunnel LowSpeedGarage  Tunnel-UC
StartTOW:  163356
EndTOW: 166780
```


### MIN / MAX PER GROUP
```
import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {'date': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-02-01'],
        'dut': ['A', 'B', 'C', 'A', 'D'],
        'target': [10.5, 12.3, 8.7, 15.2, 9.1]}
df = pd.DataFrame(data)

# Group by date, find min and max values for target and dut
grouped_df = df.groupby('date').agg({'target': ['min', 'max'], 'dut': ['min', 'max']})

# Rename columns for clarity
grouped_df.columns = ['target_min', 'target_max', 'dut_min', 'dut_max']

# Reset index to create separate columns
grouped_df = grouped_df.reset_index()

print(grouped_df)
```

### Min/Max per group again

```
# Assuming df is your pandas DataFrame with columns 'date', 'dut', and 'target'

# Find the index of the row with the minimum value in the 'target' column for each date
min_indices = df.groupby('date')['target'].idxmin()

# Find the index of the row with the maximum value in the 'target' column for each date
max_indices = df.groupby('date')['target'].idxmax()

# Extract the corresponding records for min and max targets
min_records = df.loc[min_indices]
max_records = df.loc[max_indices]

# Merge min and max records based on 'date'
result_df = pd.merge(min_records, max_records, on='date', suffixes=('_min', '_max'))

# Rename columns
result_df.rename(columns={'dut_min': 'dut_min', 'target_min': 'target_min', 'dut_max': 'dut_max', 'target_max': 'target_max'}, inplace=True)

# Reorder columns if needed
result_df = result_df[['date', 'dut_min', 'target_min', 'dut_max', 'target_max']]


```

### Find dates with min and max  value per date (1)
```
import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {'date': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-02'],
        'number': [5, 2, 8, 2]}
df = pd.DataFrame(data)

# Find the index of the minimum and maximum values
min_index = df['number'].idxmin()
max_index = df['number'].idxmax()

# Get the corresponding dates
min_date = df.loc[min_index, 'date']
max_date = df.loc[max_index, 'date']

# Print the results
print(f"Date with minimum number: {min_date}")
print(f"Date with maximum number: {max_date}")
```
### Find dates with min and max  value per date (2)
```
import pandas as pd

# Assuming df is your pandas DataFrame with columns 'date' and 'number'

# Find the row with the minimum value in the 'number' column
min_row = df.loc[df['number'].idxmin()]

# Find the row with the maximum value in the 'number' column
max_row = df.loc[df['number'].idxmax()]

# Extract the dates corresponding to the min and max numbers
date_min = min_row['date']
date_max = max_row['date']

print("Date with minimum number:", date_min)
print("Date with maximum number:", date_max)
```

### Find uniq numbers per group
```
import pandas as pd

# Sample DataFrame
data = {'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'David'],
        'date': ['2023-01-01', '2023-01-01', '2023-02-02', '2023-03-03', '2023-03-03', '2023-03-03'],
        'val': [10.5, 12.3, 8.7, 15.2, 9.1, 10.5]}
df = pd.DataFrame(data)

# Group by name and date, calculate the number of unique values in 'val'
name_date_counts = df.groupby(['name', 'date'])['val'].nunique()

# Reset index to create separate columns
name_date_counts = name_date_counts.reset_index()

print(name_date_counts)

```


### Find names with min and max values per date 1
```
import pandas as pd

# Sample DataFrame
data = {'name': ['John', 'Jane', 'John', 'Jane', 'John', 'Jane'],
        'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03'],
        'value': [10.5, 20.3, 15.2, 18.6, 12.7, 22.1]}

df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and aggregate min and max values for each group
agg_df = df.groupby('date').agg({'name': ['min', 'max'], 'value': ['min', 'max']})

# Flatten the multi-index columns
agg_df.columns = ['_'.join(col).strip() for col in agg_df.columns.values]

# Rename columns
agg_df = agg_df.rename(columns={'name_min': 'name_min_value', 'name_max': 'name_max_value', 'value_min': 'min_value', 'value_max': 'max_value'})

# Reset index to make date a column again
agg_df = agg_df.reset_index()

print(agg_df)

```

### Find names with min and max values per date 2
```
import pandas as pd

# Sample DataFrame (replace with your actual data)
data = {'name': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'David', 'Alice'],
        'date': ['2023-01-01', '2023-01-01', '2023-02-02', '2023-03-03', '2023-03-03', '2023-03-03', '2023-03-03'],
        'value': [10.5, 12.3, 8.7, 15.2, 9.1, 10.5, 11.2]}
df = pd.DataFrame(data)

# Group by date, find min and max values for each name-date combination
grouped_df = df.groupby(['date', 'name'])[['value']].agg(['min', 'max'])

# Reset index
grouped_df.columns = ['min_value', 'max_value']
grouped_df = grouped_df.reset_index()

# Sort by date and name
grouped_df = grouped_df.sort_values(by=['date', 'name'])

# Identify minimum value rows
min_value_rows = grouped_df[grouped_df['value'] == grouped_df['min_value']]

# Identify maximum value rows
max_value_rows = grouped_df[grouped_df['value'] == grouped_df['max_value']]

# Create a new column 'record_type'
min_value_rows['record_type'] = 'min'
max_value_rows['record_type'] = 'max'

# Combine min and max value DataFrames
min_max_df = pd.concat([min_value_rows, max_value_rows])

print(min_max_df)
```


# Fid min and max  in group 3 

To have all names with the minimum and maximum values  per day are included,

```
import pandas as pd

# Sample DataFrame
data = {'name': ['John', 'Jane', 'John', 'Jane', 'Alice', 'Jane', 'Alice'],
        'date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-03', '2024-01-03'],
        'value': [10.5, 20.3, 15.2, 20.3, 12.7, 20.3, 22.1]}

df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Group by date and aggregate min and max values for each group
agg_df = df.groupby('date').agg({'name': ['min', 'max'], 'value': ['min', 'max']})

# Flatten the multi-index columns
agg_df.columns = ['_'.join(col).strip() for col in agg_df.columns.values]

# Rename columns
agg_df = agg_df.rename(columns={'name_min': 'name_min_value', 'name_max': 'name_max_value', 'value_min': 'min_value', 'value_max': 'max_value'})

# Reset index to make date a column again
agg_df = agg_df.reset_index()

# Filter to include all names with the minimum and maximum values
min_values = df.groupby('date')['value'].transform(min)
max_values = df.groupby('date')['value'].transform(max)
agg_df = df[(df['value'] == min_values) | (df['value'] == max_values)]

print(agg_df)
```

### Read some columns only:
```
import pandas as pd

# Path to your CSV file
file_path = "your_file.csv"

# Specify the desired columns by name
desired_columns = ["column1", "column3", "column5"]

# Read the CSV file, selecting only the specified columns
df = pd.read_csv(file_path, header=0, usecols=desired_columns)

print(df)

```

### Parse string and populate new columns
```
import pandas as pd
import re  # Import regular expressions library

# Sample DataFrame
data = {'A': ['text1 2023-11-21 some text lsi\name1# text2', 'other text 2024-05-03 lsi\name2# more text']}
df = pd.DataFrame(data)

# Define regular expressions to extract date and name
date_pattern = r'(\d{4}-\d{2}-\d{2})'  # Matches pattern YYYY-MM-DD
name_pattern = r'lsi\\(.*?)#'  # Matches "lsi\" followed by any characters until "#"

# Extract date and name using regular expressions
df['date'] = df['A'].str.extract(date_pattern)
df['name'] = df['A'].str.extract(name_pattern)

# Drop the original column A (optional)
df = df.drop('A', axis=1)

print(df)
```

### Parse string and populate new columns 2
```
import pandas as pd
import re

# Sample DataFrame
data = {'A': ['Some text lsiJohn Doe # other text 2023-05-10 more text',
              'Another text 2022-12-15 lsiJane Smith # additional text']}

df = pd.DataFrame(data)

# Function to extract date and name
def extract_info(text):
    # Extracting date
    date_match = re.search(r'\d{4}-\d{2}-\d{2}', text)
    if date_match:
        date = date_match.group()
    else:
        date = None
    
    # Extracting name
    name_match = re.search(r'lsi(.*?)#', text)
    if name_match:
        name = name_match.group(1).strip()
    else:
        name = None
    
    return date, name

# Apply function to DataFrame and create new columns
df['date'], df['name'] = zip(*df['A'].apply(extract_info))

print(df)
```

#### Create dictionary from list of tuples
```
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
dictionary_from_list = dict(list_of_tuples)

print(dictionary_from_list)



dictionary_from_list = {t[0]: t[1:] for t in list_of_tuples}
```

### Division in pandas with replacing None
```
import pandas as pd
import numpy as np  # Import NumPy for missing value handling

# Sample DataFrame (replace with your actual data)
data = {'col1': [1.5, None, 3.2, 0, 4.1],
        'col2': [2.3, 5, 1.8, None, 7.2],
        'col3': [None, 4.7, 0, 2.1, None],
        'col4': [6.4, 0, None, 8.3, 1.9],
        'col5': [0, 3.8, None, 5.1, None]}
df = pd.DataFrame(data)

# Number for division
divisor = 10

# Create a new empty DataFrame with the same shape as the original
new_df = pd.DataFrame(index=df.index, columns=df.columns)

# Efficient division with handling for None and 0 using NumPy
new_df = df.div(divisor, fill_value=np.NAN)  # Replace with None if you prefer None over NaN

# Replace NaN with None (optional)
new_df = new_df.fillna(None)  # Uncomment if you prefer None over NaN

print(new_df)
```
### Safe Division in pandas 2 using apply()
```
import pandas as pd
import numpy as np

# Assuming df is your original DataFrame
# Replace 'given_number' with your desired number
given_number = 10

# Create a sample DataFrame for demonstration
data = {
    'col1': [1.0, 2.0, None, 0, 5.0],
    'col2': [4.0, 0, 6.0, None, 8.0],
    'col3': [0, 3.0, None, 2.0, 1.0],
    'col4': [7.0, 0, 9.0, None, 0],
    'col5': [None, 5.0, 0, 4.0, None]
}

df = pd.DataFrame(data)

# Function to perform division with handling None and 0 values
def safe_divide(x, y):
    if y == 0 or pd.isna(y):
        return None
    else:
        return x / y

# Apply safe_divide function element-wise on the DataFrame
new_df = df.apply(lambda x: safe_divide(given_number, x))

print(new_df)
```


https://www.pythonexcel.com/

https://realpython.com/openpyxl-excel-spreadsheets-python/

https://blog.aspose.com/cells/create-excel-xls-xlsx-using-python-excel-api/

https://stackoverflow.com/questions/13437727/how-to-write-to-an-excel-spreadsheet-using-python

https://www.xlwings.org/

https://openpyxl.readthedocs.io/en/stable

https://github.com/jmcnamara/XlsxWriter

https://xlsxwriter.readthedocs.io/

https://forum.codewithmosh.com/t/creating-a-graph-in-excel/21607/7

https://stackoverflow.com/questions/44234905/customized-series-title-in-openpyxl-python


###  Merging cells
```
from openpyxl import Workbook

# Create a new workbook and worksheet
workbook = Workbook()
sheet = workbook.active

# Define your Python dictionary
data_dict = {"Key1": ["Value A1", "Value A2", "Value A3"],
             "Key2": ["Value B1", "Value B2"],
             "Key1": ["Value A4"]}  # Duplicate key for merging

# Write headers
sheet["A1"] = "Key"
sheet["B1"] = "Value"

# Variables for merging
start_row = 2  # Track starting row for each key
current_key = None  # Store previous key

# Loop through dictionary items
for row, (key, value_list) in enumerate(data_dict.items(), start=2):
    if key != current_key:  # New key encountered
        sheet["A" + str(row)] = key
        start_row = row
        current_key = key
    else:  # Same key as previous row, merge cells
        sheet.merge_cells(start_row=start_row, start_column=1, end_row=row, end_column=1)

    for value in value_list:
        row += 1
        sheet["B" + str(row)] = value

# Save the workbook
workbook.save("dict_to_excel_merged.xlsx")
```

### Cell colors:

```
Both Color and PatternFill classes in the openpyxl.styles module are used for formatting cells in Excel spreadsheets,
but they target different aspects of cell appearance:

Color Class:

Defines a single, solid color for the cell's background.
Useful for simple color fills without any patterns.
Properties:
rgb: A string representing the RGB color code (e.g., "FFFF99" for orange).
PatternFill Class:

Defines a pattern for the cell's background, which can be a solid color fill (achieved through patternType="solid"),
a gradient fill, or various other pre-defined patterns.
Offers more flexibility in cell aesthetics.
Properties:
patternType: The type of pattern to apply (e.g., "solid", "diagonal", "linearGradient").
fgColor: The foreground color used in the pattern (applicable to all pattern types).

red_fill = PatternFill(patternType="solid", start_color="FF0000")

Bright Red:
-------------
#FF0000: Pure red, the most vibrant shade.
#F00: Shorthand version of #FF0000.
Lighter Reds:

#E04A5F: Coral red, with a hint of warmth.
#FF6347: Tomato red, a slightly toned-down red.
#FF7F50: Coral, a vibrant orange-red.
Darker Reds:

#8B0000: Dark red, a deep and intense shade.
#C62828: Crimson, a rich and luxurious red.
#A52A2A: Brown red, with a touch of earthiness.
Variations:

#FF1493: Deep Pink, a vivid and feminine shade.
#DC143C: Crimson Red, a bright and regal color.
#B22222: Firebrick, a subdued and elegant red.

Orange
--------
Bright orange: "#FFA500" (This is a common shade of orange used for reference)
Light orange: "#FFCC99" (A lighter and warmer shade)
Dark orange: "#FF7F00" (A deeper and more intense orange)

Green
------
Light green: "#90EE90"
Lime green: "#00FF00" (same as pure green)
Dark green: "#006400"
Forest green: "#228B22"
Lawn green: "#7CFC00"
Sea green: "#2E8B57"


Bright Blues:
-------------
#0000FF: True blue, the most classic shade.
#00F: Shorthand version of #0000FF.
#007FFF: Azure, a sky blue with a hint of green.
#4169E1: Royal blue, a rich and vibrant shade.
Lighter Blues:

#ADD8E6: Light blue, a soft and calming shade.
#87CEFA: Sky blue, reminiscent of a clear sky.
#ACE5EE: Light steel blue, with a touch of grey.
Darker Blues:

#00008B: Dark blue, a deep and mysterious shade.
#191970: Midnight blue, evocative of the night sky.
#0047AB: Navy blue, a classic and elegant color.
Variations:

#6495ED: Cornflower blue, a soft and delicate shade.
#7B68EE: Medium slate blue, with a touch of purple.
#4682B4: Steel blue, a greyish-blue with a metallic feel.

```
#### PatternFill example
```
from openpyxl import Workbook
from openpyxl.styles import PatternFill

# Pattern definitions (replace with desired patterns)
orange_fill = PatternFill(patternType="solid", fgColor="FFFF99")
blue_fill = PatternFill(patternType="solid", fgColor="007FFF")
green_fill = PatternFill(patternType="solid", fgColor="00FF00")
red_fill = PatternFill(patternType="solid", fgColor="FF0000")

# Create a new workbook and worksheet
workbook = Workbook()
sheet = workbook.active

# Sample dictionary (key: value, pattern)
data_dict = {"A1": ("Value A1", orange_fill),
             "A2": ("Value A2", blue_fill),
             "A3": ("Value A3", green_fill),
             "B2": ("Value B2", red_fill)}

# Write data and set background patterns
for cell, (value, pattern) in data_dict.items():
    sheet[cell].value = value
    sheet[cell].fill = pattern

# Save the workbook
workbook.save("patterned_cells.xlsx")
```
#### Color example
```
from openpyxl import Workbook
from openpyxl.styles import Color, Fill

# Color definitions (replace with desired RGB values for customization)
orange = Color(rgb="FFFF99")
blue = Color(rgb="007FFF")
green = Color(rgb="00FF00")
red = Color(rgb="FF0000")

# Create a new workbook and worksheet
workbook = Workbook()
sheet = workbook.active

# Sample dictionary (key: value, color)
data_dict = {"A1": ("Value A1", orange),
             "A2": ("Value A2", blue),
             "A3": ("Value A3", green),
             "B2": ("Value B2", red)}

# Write data and set background colors
for cell, (value, color) in data_dict.items():
    sheet[cell].value = value
    fill = Fill(start_color=color, fill_type="solid")
    sheet[cell].fill = fill

# Save the workbook
workbook.save("colored_cells.xlsx")
```

### LineChart Example 0:

```
import random
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

workbook = Workbook()
sheet = workbook.active

# Let's create some sample sales data
rows = [
    ["", "January", "February", "March", "April",
    "May", "June", "July", "August", "September",
     "October", "November", "December"],
    ['XX', ],
    ['YY', ],
    ['ZZ', ],
]

for row in rows:
    sheet.append(row)

for row in sheet.iter_rows(min_row=2,
                           max_row=4,
                           min_col=2,
                           max_col=13):
    for cell in row:
        cell.value = random.randrange(5, 100)

chart = LineChart()
data = Reference(worksheet=sheet,
                 min_row=2,
                 max_row=4,
                 min_col=1,  # first column has titles XX YY ZZ
                 max_col=13)

chart.add_data(data, from_rows=True, titles_from_data=True)
sheet.add_chart(chart, "B6")

# Add categories: this is 1st row with names
cats = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=1,
                 min_col=2,
                 max_col=13)
chart.set_categories(cats)

workbook.save("line_chart.xlsx")

```


### Example 1
```
from openpyxl import Workbook
from openpyxlchart import LineChart

# Sample data (replace with your actual data)
data = [
    [2, 4, 7, 5],  # Series data (values)
    ["Apple", "Orange", "Banana", "Pear"]  # Category labels (separate row)
]

# Create a workbook and chart object
wb = Workbook()
chart = LineChart()

# Add data to the chart (assuming data starts from A1 in your worksheet)
chart.add_data(data, titles_from_rows=True)  # Titles from the first row (category labels)

# Attach the chart to the worksheet
ws = wb.active
ws.add_chart(chart, "E5")  #の位置 (E5) to specify the chart location

```
### Example 2

```
import openpyxl
from openpyxlchart import LineChart

# Sample data (replace with your actual data)
data = [
    [2, 4, 7, 5],  # Series data (values in a column)
    ["Apple", "Orange", "Banana", "Pear"]  # Category labels (can be in a row or column)
]

# Create a workbook and chart object
wb = openpyxl.Workbook()
chart = LineChart()

# Add data to the chart, assuming data starts from A1
# If category labels are in a row (starting from row 2):
chart.add_data(data, titles_from_rows=True)

# If category labels are in a column (starting from B1):
# chart.add_data([data[0]], titles_from_rows=False, titles=[data[1]])

# Attach the chart to the worksheet
ws = wb.active
ws.add_chart(chart, "E5")  # Specify the chart location (E5)

wb.save("line_chart.xlsx")
```

### titles_from_data
```
 The titles_from_data argument in the add_data method of openpyxl's LineChart (and other chart types)
 is indeed a useful feature for handling chart titles. Here's how it works:

When titles_from_data is set to True (default):

openpyxl assumes the first row or column (depending on the data orientation) contains titles for the data series.
It will automatically extract those titles and use them as the labels for the data series in the chart.

Example:

# Assuming your data (y-values) starts from cell B2 and titles (series names) are in row A1:A2

data = Reference(worksheet, min_col=2, min_row=2, max_col=2, max_row=10)
line_chart.add_data(data, titles_from_data=True)
 
In this example, line_chart will use the values in cells A1 and A2 (assuming they contain series names) as titles for the data series in the chart.

When titles_from_data is set to False:

openpyxl will not use any data for titles.
You'll need to define custom titles separately using the chart object's properties.

Example:

Python
data = Reference(worksheet, min_col=2, min_row=2, max_col=2, max_row=10)
line_chart.add_data(data, titles_from_data=False)

# Set custom titles (optional)
line_chart.title = "My Line Chart"
line_chart.series[0].title = "Series 1"  # Set title for the first series (indexing starts from 0)
 
Choosing the Right Approach:

If your data has titles in the first row/column, using titles_from_data=True is convenient.
If your titles are elsewhere or you want custom titles, set titles_from_data=False and define titles manually.
By effectively using the titles_from_data argument, you can streamline your chart creation process and ensure proper labeling of your data series.
```

```
Unfortunately, openpyxl currently doesn't offer a direct way to set custom x-axis labels for charts. However, there are a couple of workarounds you can use to achieve a similar effect:
```
### Workaround 1: Use Separate Data Series
```
Prepare Your Data: Instead of using a single data series for your y-values, create two separate series:

One series will hold your actual y-values.
The other series will hold your custom x-axis labels (placed in a separate row/column).
Add Data Series: When adding data to your LineChart object, use the add_data method twice:
```
Python
```
y_values = Reference(worksheet, min_col=2, min_row=2, max_col=2, max_row=10)
label_values = Reference(worksheet, min_col=1, min_row=2, max_col=1, max_row=10)  # Assuming labels in A2:A10

# Add y-values with optional labels (assuming labels are in the first column)
line_chart.add_data(y_values, titles=label_values)

# Add custom labels as a separate data series (without y-values)
line_chart.add_data(label_values)  # Add labels without a second set of y-values
```

```
This will create a line chart with your y-values connected by lines,
and your custom labels displayed at the corresponding positions on the x-axis.
However, the line for the label series will be invisible as it has no y-values.
```
### Workaround 2: Format X-Axis Tick Labels
```
Prepare Your Data: Keep your data in the usual format (y-values with corresponding x-values in the same row/column).

Set Categories: Use the set_categories method on your LineChart object, referencing the cells containing your x-values.

Format Tick Labels: Access the chart object's x_axis property and then the tick property.
You can format the tick labels using properties like label_font and rotation.
```
Python
```
categories = Reference(worksheet, min_col=1, min_row=2, max_col=1, max_row=10)
line_chart.set_categories(categories)

# Access and format x-axis tick labels (optional)
line_chart.x_axis.tick.label_font = openpyxl.styles.Font(name="Calibri", size=10)
line_chart.x_axis.tick.label_rotation = 45  # Optional rotation for long labels
```

```
This approach uses the existing x-values as data points but allows some formatting of the tick labels displayed on the x-axis.
```

Choosing the Right Workaround:
```
Workaround 1 is better if you need complete control over the x-axis labels and their positions.
 However, it creates an invisible line series, which might not be ideal.

Workaround 2 is more suitable if you want to format the existing x-values displayed as tick labels.
```






### Assign custom colors to various elements of your LineChart using openpyxl. 

#### 1. Accessing Chart Elements:

Once you've created your LineChart object, you can access individual elements you want to color. Here are some common properties:
series: This holds information about each data series in the chart.
fill: This property applies to the area enclosed by the lines in a line chart.
line: This property applies to the actual lines in the chart.

####  2. Color Choice:

openpyxl uses the ColorChoice class to represent colors. You can define colors in a few ways:
Preset colors: Use pre-defined color names like "red", "blue", etc.
Indexed colors: Use an index value corresponding to the color palette used in Excel (limited options).
RGB values: Define custom colors using a tuple of red, green, and blue values (e.g., (255, 0, 0) for red).

#### 3. Applying Colors:

Series Color: Access a specific data series within the series property (indexing starts from 0). Then, set the fill or line property of the series to a ColorChoice object:
 
Assuming you have two data series in your chart
```
line_chart.series[0].fill = openpyxl.drawing.colors.ColorChoice('blue')
line_chart.series[1].line = openpyxl.drawing.colors.ColorChoice(rgb=(0, 128, 0))  # Green using RGB
```

#### Line Chart Fill: Set the fill property of the entire chart object to color the background area:
```
line_chart.fill = openpyxl.drawing.colors.ColorChoice('yellow')
```
 
Additional Tips:
```
Explore the openpyxl.drawing.colors module for a list of available preset color names and how to define RGB colors.
You can also customize the color of other chart elements like axes and legend text using similar approaches. Refer to the openpyxl documentation for details on properties of different chart elements.
Here are some resources for further reference:
```
Openpyxl LineChart API: https://openpyxl.readthedocs.io/en/stable/api/openpyxl.chart.reader.html

openpyxl ColorChoice Class: https://openpyxl.readthedocs.io/en/stable/api/openpyxl.drawing.colors.html



###  in openpyxl, there isn't a direct way to specify which data series acts as the x-axis in a LineChart. 
```
Line charts inherently treat both provided data series as y-values connected by lines.

However, there are a couple of workarounds you can employ to achieve an effect similar to having a designated x-axis series:
```
#### Workaround 1: Arrange Data for Sorting
```
Data Organization: Organize your data such that the intended x-axis values are in the first column (column A). Place your y-values for each data series in subsequent columns (e.g., B, C, etc.).

Sorting Data (Optional): While not strictly necessary, you can sort the data in your worksheet by the first column (x-axis values) to ensure a sequential order on the chart.

Adding Data Series: When adding data to your LineChart object, reference the data ranges for both series:

 
x_values = Reference(worksheet, min_col=1, min_row=2, max_col=1, max_row=10)
y_values1 = Reference(worksheet, min_col=2, min_row=2, max_col=2, max_row=10)
y_values2 = Reference(worksheet, min_col=3, min_row=2, max_col=3, max_row=10)  # Assuming multiple data series

line_chart.add_data(y_values1, titles_from_data=True)
line_chart.add_data(y_values2, titles_from_data=True)
 
Explanation:

By placing the x-axis values in the first column and referencing them first when adding data, openpyxl will typically plot them on the x-axis. The subsequent data series (y-values) will be connected to these x-axis values, creating a line chart with the desired appearance.
```
#### Workaround 2: Mimic an X-Axis with Labels (for Categorical Data)
````
Data Format: If your x-axis data represents categories (e.g., weekdays, months), you can keep them in a separate row (e.g., row 1). Place your y-values for each data series in subsequent rows.

Adding Data and Categories: When adding data to your LineChart, reference the y-values and set the categories using the set_categories method:

y_values1 = Reference(worksheet, min_col=2, min_row=2, max_col=2, max_row=10)
y_values2 = Reference(worksheet, min_col=3, min_row=2, max_col=3, max_row=10)
categories = Reference(worksheet, min_row=1, min_col=1, max_row=1, max_col=len(y_values1.cols))  # Assuming all series have same length

line_chart.add_data(y_values1, titles_from_data=True)
line_chart.add_data(y_values2, titles_from_data=True)
line_chart.set_categories(categories)
 
Formatting X-Axis Labels (Optional): You can format the x-axis tick labels (categories) using the x_axis.tick property for improved readability.
```
#### Choosing the Right Workaround:
```
Workaround 1 is suitable for numerical or sequential x-axis data.
Workaround 2 is better for categorical x-axis data where labels are more important than a strict linear order.

Remember, these are workarounds, and the ideal approach depends on your specific data and chart requirements.

```

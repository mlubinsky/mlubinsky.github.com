RangeIndex: 53 entries, 0 to 52
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   TEST           53 non-null     object
 1   Category       53 non-null     object
 2   ITEM           53 non-null     object
 3   VAL_SCORE_AVG  53 non-null     object
 4   REF            53 non-null     object
 5   DUT            53 non-null     object
dtypes: object(6)
memory usage: 2.6+ KB
None
STEP 0001 df.shape= (53, 6)  len(df)= 53



RangeIndex: 53 entries, 0 to 52
Data columns (total 6 columns):
 #   Column         Non-Null Count  Dtype
---  ------         --------------  -----
 0   TEST           53 non-null     object
 1   Category       53 non-null     object
 2   ITEM           53 non-null     object
 3   VAL_SCORE_AVG  53 non-null     object
 4   REF            53 non-null     object
 5   DUT            53 non-null     object
dtypes: object(6)
memory usage: 2.6+ KB
None
STEP 0001 df.shape= (53, 6)  len(df)= 53

STEP 00001 df.shape= (37, 6)
df_value_score = df[df["VAL_SCORE_AVG"].isin(["Value", "Score"])].pivot(index=["TEST", "Category", "ITEM"], columns="VAL_SCORE_AVG", values=["REF", "DUT"])
pandas                 1.0.5   # pandas                 1.0.5  ValueError: Shape of passed values is (46, 2), indices imply (3, 2)


pandas                 1.3.4 STEP 0001 df.shape= (53, 6)

GROK
#-----

Solution for Pandas 1.0.5
To make this work in pandas 1.0.5, you can try one of the following approaches:

Approach 1: Pivot for Each Value Column Separately
Instead of passing multiple values to a single pivot call, perform the pivot operation separately for "REF" and "DUT", 
then combine the results. This avoids the multi-value reshaping issue:
 
# Filter the dataframe
df_filtered = df[df["VAL_SCORE_AVG"].isin(["Value", "Score"])]

# Pivot for REF
df_ref = df_filtered.pivot(
    index=["TEST", "Category", "ITEM"], 
    columns="VAL_SCORE_AVG", 
    values="REF"
)

# Pivot for DUT
df_dut = df_filtered.pivot(
    index=["TEST", "Category", "ITEM"], 
    columns="VAL_SCORE_AVG", 
    values="DUT"
)

# Combine the results
df_value_score = pd.concat([df_ref, df_dut], axis=1, keys=["REF", "DUT"])
This approach ensures compatibility with pandas 1.0.5 by breaking the problem into simpler steps that the older version can handle.

Approach 2: Use pivot_table Instead of pivot
The pivot_table function is more flexible than pivot and often handles multi-value cases better in older pandas versions.
It also allows aggregation (e.g., mean by default), but if your data has unique combinations of index and columns, it will behave similarly to pivot. Try this:
 
df_value_score = pd.pivot_table(
    df[df["VAL_SCORE_AVG"].isin(["Value", "Score"])],
    index=["TEST", "Category", "ITEM"],
    columns="VAL_SCORE_AVG",
    values=["REF", "DUT"]
)
If your data has duplicate entries for the same index and columns combination, pivot_table will aggregate them (e.g., by taking the mean). If you need to avoid aggregation and ensure the behavior matches pivot, you’ll need to confirm your data has no duplicates, or use Approach 1.

Why This Happens
In pandas 1.0.5, the pivot function was less robust when dealing with multiple values columns compared to later versions like 1.3.4. 
The shape mismatch error indicates that the reshaping logic couldn’t reconcile the number of rows in the resulting pivot table with the expected structure.
By pandas 1.3.4, this behavior was improved, which is why your original code works fine there.

Recommendation
Use Approach 1 if you need an exact match to pivot behavior and your data has no duplicate index-column combinations.
Use Approach 2 if your data might have duplicates and you’re okay with aggregation (or can ensure uniqueness).
 
#-----
There is pandas dataframe with columns  Category, ITEM, V_S_A, REF, DUT
The every combination of  (Category, ITEM) may exist up to 3 rows with different values in V_S_A column                                  
"Value", "Score", "AVG".
Please transform this dataframe into new dataframe as below
 using  pandas 1.0.5
1)
The rows with values "Value", "Score" in V_S_A column  for the same (Category, ITEM) need to be collapsed into the single row 
and the corresponding values in REF, DUT column need to be stored into new columns:
 REF_value, REF_Score, DUT_value, DUT_score.
2)
The rows with "AVG" value in V_S_A  column need to be preserved; the values of  REF, DUT column for such rows  need to be in REF_Score, DUT_score columns.
#-----

def transform_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    # Filter out rows where V_S_A is "Value" or "Score" and keep only "AVG" rows
    df_avg = df[df["V_S_A"] == "AVG"].copy()
    
    # Create pivoted columns for Value and Score
    df_value_score = df[df["V_S_A"].isin(["Value", "Score"])].pivot(index=["TEST", "Category", "ITEM"], columns="V_S_A", values=["REF", "DUT"])
    
    # Flatten the column names
    df_value_score.columns = [f"{col[0]}_{col[1].lower()}" for col in df_value_score.columns]
    df_value_score.reset_index(inplace=True)
    
    # Merge with AVG data, placing REF and DUT values into REF_Score and DUT_Score
    df_avg.rename(columns={"REF": "REF_Score", "DUT": "DUT_Score"}, inplace=True)
    df_avg.drop(columns=["V_S_A"], inplace=True)
    
    # Merge both dataframes
    df_transformed = pd.merge(df_avg, df_value_score, on=["TEST", "Category", "ITEM"], how="left")
    
    return df_transformed


#---------
To transform your Pandas DataFrame according to the specified requirements,
we’ll need to reshape the data by pivoting or filtering rows based on the V_S_A column and then creating new columns (REF_value, REF_Score, DUT_value, DUT_score) 
with the appropriate values from REF and DUT. Here's how we can do it step-by-step:

Problem Breakdown

For rows where V_S_A is "Value" or "Score":
Eliminate these rows from the final DataFrame.
Store their REF values in new columns: REF_value (for "Value") and REF_Score (for "Score").
Store their DUT values in new columns: DUT_value (for "Value") and DUT_score (for "Score").
For rows where V_S_A is "AVG":
Keep these rows as the base of the final DataFrame.
Move their REF values to REF_Score and DUT values to DUT_score.

Assumptions
The DataFrame has unique combinations of TEST, Category, and ITEM that can be used to align the "Value", "Score", and "AVG" rows.
The transformation should result in a DataFrame where each row corresponds to the "AVG" case, augmented with new columns from "Value" and "Score" rows.

Here’s the code to achieve this transformation:

 
import pandas as pd

# Example DataFrame (replace this with your actual DataFrame)
data = {
    'TEST': ['T1', 'T1', 'T1', 'T2', 'T2', 'T2'],
    'Category': ['C1', 'C1', 'C1', 'C2', 'C2', 'C2'],
    'ITEM': ['I1', 'I1', 'I1', 'I2', 'I2', 'I2'],
    'V_S_A': ['Value', 'Score', 'AVG', 'Value', 'Score', 'AVG'],
    'REF': [10, 20, 30, 40, 50, 60],
    'DUT': [15, 25, 35, 45, 55, 65]
}
df = pd.DataFrame(data)

# Step 1: Split the DataFrame based on V_S_A values
df_value = df[df['V_S_A'] == 'Value'][['TEST', 'Category', 'ITEM', 'REF', 'DUT']].rename(columns={'REF': 'REF_value', 'DUT': 'DUT_value'})
df_score = df[df['V_S_A'] == 'Score'][['TEST', 'Category', 'ITEM', 'REF', 'DUT']].rename(columns={'REF': 'REF_Score', 'DUT': 'DUT_score'})
df_avg = df[df['V_S_A'] == 'AVG'][['TEST', 'Category', 'ITEM', 'REF', 'DUT']].rename(columns={'REF': 'REF_Score', 'DUT': 'DUT_score'})

# Step 2: Merge the "Value" and "Score" data into the "AVG" DataFrame

result = df_avg.merge(df_value[['TEST', 'Category', 'ITEM', 'REF_value', 'DUT_value']],
                      on=['TEST', 'Category', 'ITEM'],
                      how='left')\
               .merge(df_score[['TEST', 'Category', 'ITEM', 'REF_Score', 'DUT_score']],
                      on=['TEST', 'Category', 'ITEM'],
                      how='left',
                      suffixes=('_avg', '_score'))

# Step 3: Combine REF_Score and DUT_score from "AVG" and "Score" rows
# If there's a conflict, prioritize "AVG" values for REF_Score and DUT_score (as per requirement 2)
result['REF_Score'] = result['REF_Score_avg'].combine_first(result['REF_Score_score'])
result['DUT_score'] = result['DUT_score_avg'].combine_first(result['DUT_score_score'])

# Step 4: Drop temporary columns and clean up
result = result.drop(columns=['REF_Score_avg', 'REF_Score_score', 'DUT_score_avg', 'DUT_score_score'])

# Final result
print(result)


Explanation
------------
Filtering Rows:

df_value: Contains rows where V_S_A == "Value", with REF and DUT renamed to REF_value and DUT_value.
df_score: Contains rows where V_S_A == "Score", with REF and DUT renamed to REF_Score and DUT_score.
df_avg: Contains rows where V_S_A == "AVG", with REF and DUT renamed to REF_Score and DUT_score.

Merging:
---------
Merge df_avg with df_value and df_score using TEST, Category, and ITEM as keys to align the data.
Use how='left' to keep all rows from df_avg (the base DataFrame).
Handling REF_Score and DUT_score:
After merging, there are two sets of REF_Score and DUT_score columns (from "AVG" and "Score" rows).
Use combine_first() to prioritize the "AVG" values (REF_Score_avg, DUT_score_avg) over the "Score" values (REF_Score_score, DUT_score_score), as per requirement 2.

Cleanup:
--------------
Drop temporary columns created during the merge to get the final structure.
Example Output
For the example DataFrame:

   TEST Category ITEM V_S_A  REF  DUT
0    T1       C1   I1 Value   10   15
1    T1       C1   I1 Score   20   25
2    T1       C1   I1   AVG   30   35
3    T2       C2   I2 Value   40   45
4    T2       C2   I2 Score   50   55
5    T2       C2   I2   AVG   60   65

The result will be:

  TEST Category ITEM  REF_Score  DUT_score  REF_value  DUT_value
0   T1       C1   I1         30         35         10         15
1   T2       C2   I2         60         65         40         45

Notes
Uniqueness: This assumes that TEST, Category, and ITEM uniquely identify groups of "Value", "Score", and "AVG" rows. If there are duplicates, you might need to adjust the merge logic (e.g., using aggregation or additional keys).
Missing Data: If some groups lack "Value" or "Score" rows, the corresponding new columns will contain NaN.
Requirement Interpretation: I interpreted "REF, DUT column values for rows with 'AVG' need to be in REF_Score, DUT_score" as meaning these values take precedence in the final REF_Score and DUT_score columns.


### JOIN


# There are 2 pandas dataframes: df1 and df2. There is column DUT in df1 and there columns DUT_NUM, date, test_loc, chipset, dut_model   in df2.
# Do left join between df1 and d2 based on matching DUT and DUT_NUM column.
# Add columns date, test_loc, chipset, dut_model  to df1 and populate it from df2

df1 = df1.merge(df2, left_on='DUT', right_on='DUT_NUM', how='left')

# Drop DUT_NUM since it's redundant after merging
df1.drop(columns=['DUT_NUM'], inplace=True)

#  if df1 and df2 have common column names (other than the join keys), 
#pandas automatically suffixes the overlapping column names with
#_x  (for df1) and _y (for df2).

### DROP SEVERAL COLUMNS
columns_to_drop = ['B', 'D']
df_dropped = df.drop(columns=columns_to_drop)

### REORDER COLUMNS
#------------------

df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

# Define the new column order
new_order = ['C', 'A', 'B']

# Reorder columns
df = df[new_order]

print(df)

import pandas as pd

def reorder_columns(df, new_order):
    """
    Reorders the columns of a pandas DataFrame.

    Args:
        df (pd.DataFrame): The DataFrame to reorder.
        new_order (list): A list of column names in the desired order.

    Returns:
        pd.DataFrame: The DataFrame with reordered columns.
    """

    # Check if all columns in new_order exist in the DataFrame
    if not all(col in df.columns for col in new_order):
        raise ValueError("One or more columns in 'new_order' not found in the DataFrame.")

    # Check for duplicate column names in new_order.
    if len(new_order) != len(set(new_order)):
        raise ValueError("Duplicate column names found in 'new_order'.")

    # Check if all original columns are included in new_order.
    if len(new_order) != len(df.columns):
        raise ValueError("Not all original columns are included in 'new_order'.")

    return df[new_order]

# Example usage:
data = {'col1': [1, 2, 3], 'col2': ['a', 'b', 'c'], 'col3': [True, False, True]}
df = pd.DataFrame(data)

new_order = ['col3', 'col1', 'col2']
reordered_df = reorder_columns(df, new_order)

print("Original DataFrame:")
print(df)

print("\nReordered DataFrame:")
print(reordered_df)

#Example of an error being raised.
try:
  bad_order = ['col3', 'col1', 'col4']
  reordered_df = reorder_columns(df, bad_order)
except ValueError as e:
  print(f"\nError: {e}")

try:
  bad_order = ['col3', 'col1', 'col1']
  reordered_df = reorder_columns(df, bad_order)
except ValueError as e:
  print(f"\nError: {e}")

try:
  bad_order = ['col3', 'col1']
  reordered_df = reorder_columns(df, bad_order)
except ValueError as e:
  print(f"\nError: {e}")

### CASE-INSENITIVE JOIN
#--------------------------
import pandas as pd

# Sample DataFrames
df1 = pd.DataFrame({
    'key': ['Apple', 'BANANA', 'Cherry'],
    'value1': [1, 2, 3]
})

df2 = pd.DataFrame({
    'key': ['apple', 'Banana', 'CHERRY'],
    'value2': [10, 20, 30]
})

# Perform case-insensitive join by converting 'key' columns to lowercase
df_merged = pd.merge(
    df1,
    df2,
    left_on=df1['key'].str.lower(),
    right_on=df2['key'].str.lower(),
    how='inner'  # or 'left', 'right', 'outer' depending on your needs
)

# Drop the duplicate 'key' column from df2 if needed
df_merged = df_merged.drop(columns=['key_y']).rename(columns={'key_x': 'key'})

print(df_merged)


import pandas as pd

def case_insensitive_join(df1, df2, left_on, right_on, how='left'):
    """
    Performs a case-insensitive join of two pandas DataFrames.

    Args:
        df1 (pd.DataFrame): The left DataFrame.
        df2 (pd.DataFrame): The right DataFrame.
        left_on (str): The column name in df1 to join on.
        right_on (str): The column name in df2 to join on.
        how (str, optional): The type of join to perform. Defaults to 'left'.

    Returns:
        pd.DataFrame: The joined DataFrame.
    """

    df1_copy = df1.copy()
    df2_copy = df2.copy()

    df1_copy[left_on + '_lower'] = df1_copy[left_on].str.lower()
    df2_copy[right_on + '_lower'] = df2_copy[right_on].str.lower()

    merged_df = pd.merge(df1_copy, df2_copy, left_on=left_on + '_lower', right_on=right_on + '_lower', how=how, suffixes=('_df1', '_df2'))

    merged_df.drop([left_on + '_lower', right_on + '_lower'], axis=1, inplace=True)

    return merged_df

# Example usage:
data1 = {'A': ['Apple', 'banana', 'Cherry', 'dATE'], 'Value1': [1, 2, 3, 4]}
df1 = pd.DataFrame(data1)




import csv
import numpy as np
import pandas as pd
fname=r"a.csv"
#--------------------
def read_csv(fname):
#--------------------
  date='2025-01-02'
  current_section="TEST SUMMARY"
  with open(fname, 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    print("Header:", header, ' len(header)=', len(header))
    for i, row in enumerate(csvreader, start=1):
        print(i, row, ' len(row)=', len(row))
        if i == 1: # 1st line after header
            test_loc = row[0]

        if row[0] =='TEST INFO':
           print("\n !!! TEST INFO  \n")
           current_section="TEST INFO"

        if row[0] =='TEST':
           current_section="TEST DETAIL"
           ref_count = 0
           dut_count = 0
           print("\n\n  2nd section,  \n\n", current_section)
           for col in row:
                if col.startswith('(REF)'):
                  ref_count +=1
                if col.startswith('(DUT)'):
                  dut_count +=1

           #break
        if row[1].strip():
           #location, date, Test, Category, is_ref, val, score
           #location, date, Test, Category, ref_val, ref_score, dut_val, dut_score
           category=row[1]


        if row[2].strip(): # ITEM
           item=row[2]


        val_score_avg=row[3]

        if val_score_avg=='Value':
           is_val_score_avg = False
           ref_val=float(row[4])
           dut_val=float(row[5])
        elif  val_score_avg=='Score':
           is_val_score_avg = False
           ref_score=float(row[4])
           dut_score=float(row[5])
           if current_section=='TEST INFO': # there is no avg, so build record here
              row=[test_loc, date, category, item, ref_val, ref_score, dut_val, dut_score, 0.0, 0.0]
              print(row)
        elif  val_score_avg=='AVG': #the whole record is available

           ref_avg=float(row[4])
           dut_avg=float(row[5])
           if is_val_score_avg:
              # This is avg row again:  across all categories
              print("this is AVG again  without item")
              item=''

           is_val_score_avg = True
           print('category=', category,' item=', item)
           row=[test_loc, date, category, item, ref_val, ref_score, dut_val, dut_score, ref_avg, dut_avg]
           print(row)
        else:
            print("Warning - unrecognized val_score_avg=", val_score_avg)

#-----------------------------------------
def load_csv_top(filename, end_row):
    return pd.read_csv(filename, nrows=end_row )

def load_csv_bottom(file_name, start_row )  :
    return pd.read_csv(file_name, skiprows=start_row-1, na_values=' ' ) 


#read_csv(fname)
#df_top = load_csv_top(fname, 37)
#print(df_top)
#print(df_top.info())
#for col in df_top.columns:
#   print (col) #, df_top.dtypes(col))
#------------------
def fill_na(fname, line=39, location="Urban Driving"):
#------------------
  df_bottom = load_csv_bottom(fname, line)
  print('df_bottom.empty=', df_bottom.empty)
  print('len(df_bottom)=', len(df_bottom))

  df_bottom.columns = [ 'VAL_SCORE_AVG' if (not col.strip() and i==3) else col
                  for i, col in enumerate(df_bottom.columns)]

  print(df_bottom.info())

  df_bottom["TEST"]=location
  df_bottom["TEST"]= df_bottom["TEST"].fillna(location)
  df_bottom[['Category', 'ITEM']] = df_bottom[['Category', 'ITEM']].fillna(method='ffill')

  #print(df_bottom)
  return df_bottom

#-----------------------------
def pivot_score_avg_value(df):
#------------------------------
  ref_dut_columns = [col for col in df.columns if col.startswith(('(REF)', '(DUT)'))]
  df_melted = df.melt(id_vars=['TEST', 'Category', 'ITEM', 'VAL_SCORE_AVG'], value_vars=ref_dut_columns, var_name='REF_DUT_col', value_name='Value')
  print(df_melted.info())
  print(df_melted)

   # Extract the suffix from column names ((REF)* or (DUT)*)
  df_melted['dut'] = df_melted['REF_DUT_col'].str[5:]  # Extract after 'A_' or 'B_'

  # Determine if the first letters (REF)
  df_melted['is_ref'] = df_melted['REF_DUT_col'].str.startswith('(REF)')

  # Pivot to get 'score', 'val', and 'avg' values in separate columns
  df_final = df_melted.pivot_table(index=['TEST', 'Category', 'ITEM', 'is_ref', 'dut'],
                                     columns='VAL_SCORE_AVG', values='Value', aggfunc='first').reset_index()

    # Rename TYPE columns properly
  df_final.columns.name = None  # Remove multi-index
  df_final = df_final.rename(columns={'score': 'score', 'val': 'val', 'avg': 'avg'})
  print('\n \n df_final')
  print(df_final)
#########################################################
#if name=='__main__':
df_filled=fill_na(fname)
print("df filled = ")
print(df_filled)
pivot_score_avg_value(df_filled)
# TODO: add date column
# Goal: build records like this:
#      location, date, Test, Category, dut_name, is_ref, val,  score

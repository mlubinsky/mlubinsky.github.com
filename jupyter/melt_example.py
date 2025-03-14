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

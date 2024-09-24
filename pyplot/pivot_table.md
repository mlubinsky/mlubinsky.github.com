### pivot vd pivot_table
```
 the issue likely arises because the build_num column may contain multiple rows with the same combination of criteria and Test,
which leads to duplicates.
Pivoting requires unique combinations of criteria and Test for each value in build_num.

To solve this issue, we should ensure that the pivot operation is valid and that there are no duplicates
that could lead to a mismatch in the expected shape of the data.

Fix for the pivot() error:
Ensure the data can be pivoted without duplicates: We can try using pivot_table() instead of pivot() to handle potential duplicates by specifying an aggregation function (like mean or first).

Ensure that the build_num values are valid and mapped correctly: If needed, we can drop or handle invalid or NaN values before pivoting.
```
```
import pandas as pd

# Input DataFrames with 'Test' column added to df2
df1 = pd.DataFrame({
    'dut_num': ['dut1', 'dut2', 'dut3', 'dut4'],
    'build_num': ['b_1', 'b_2', 'b_1', None]
})

df2 = pd.DataFrame({
    'criteria': ['c_1', 'c_2'],
    'Test': ['test1', 'test2'],   # New 'Test' column
    'dut1': [10, 20],
    'dut2': [30, 40],
    'dut3': [100, 200],
    'dut4': [50, 60]
})

# Step 1: Create a mapping of 'dut_num' to 'build_num' from df1
build_map = df1.set_index('dut_num')['build_num'].to_dict()

# Step 2: Melt df2 to make it long format for easier processing
df2_melted = df2.melt(id_vars=['criteria', 'Test'], var_name='dut_num', value_name='dut_value')

# Step 3: Map the 'dut_num' to the corresponding 'build_num' from the build_map, fill None with 'unknown'
df2_melted['build_num'] = df2_melted['dut_num'].map(build_map).fillna('unknown')

# Ensure 'dut_value' is numeric, coercing any errors to NaN
df2_melted['dut_value'] = pd.to_numeric(df2_melted['dut_value'], errors='coerce')

# Step 4: Group by 'criteria', 'Test', and 'build_num', and calculate the mean for each group
df_grouped = df2_melted.groupby(['criteria', 'Test', 'build_num']).agg(
    avg_value=('dut_value', 'mean')
).reset_index()

# Step 5: Use pivot_table to handle possible duplicates in 'criteria' and 'Test' combination
df3 = df_grouped.pivot_table(index=['criteria', 'Test'], columns='build_num', values='avg_value', aggfunc='mean').reset_index()

# Step 6: Sort the build columns alphabetically
df3 = df3[['criteria', 'Test'] + sorted(df3.columns.drop(['criteria', 'Test']))]

# Optional: Rename columns for clarity (remove hierarchical name)
df3.columns.name = None

print(df3)
```

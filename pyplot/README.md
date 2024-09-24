scientific visualization book
https://github.com/rougier/scientific-visualization-book



### Question - weithed average bar chart

```
 I have Python pandas datafrane with  columns like this:

 (avg_value, 4.14.17_7o)  float64
 (avg_value, REF)         float64
 (dut_count, 4.14.17_7o)  int64
 (dut_count, REF)         int64
 etc
 (date, )
 

Every column is a tuple with 2 elements.
The second element in tuple is not unique, For any  value in column (date, '') there is only one pair of (ag_value, build) , (dut_count, build)
where variable "build"  above is an arbitrary string.

I need to agregate it based on the matching the second element in the tuple:
New dataframe should  have 2 columns:
1-st column named "build": should be populated as unique second element in the tuple where 1st element is 'avg_value'
2nd column named "value": please calculate it as weighted average: 
 value =   sum ( dut_count * avg_value) / sum(dut_count)

Then please plot the barchart using matplotlib and seaborn
The x-axis on barchart is the "build" columns
The Y-axis  is "value" column

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample dataframe for illustration
data = {
    ('avg_value', '4.14.17_7o'): [10, 15],
    ('avg_value', 'REF'): [20, 25],
    ('dut_count', '4.14.17_7o'): [100, 150],
    ('dut_count', 'REF'): [200, 250],
    ('date', ''): ['2024-09-23', '2024-09-24']
}

df = pd.DataFrame(data)

# Step 1: Extract unique builds from the second element in the column tuples where the first element is 'avg_value'
builds = [col[1] for col in df.columns if col[0] == 'avg_value']

# Step 2: Create a new dataframe for aggregation
results = []

for build in builds:
    # Calculate weighted average for each build
    avg_value_col = ('avg_value', build)
    dut_count_col = ('dut_count', build)
    
    # Ensure both columns exist to avoid key errors
    if avg_value_col in df.columns and dut_count_col in df.columns:
        # Weighted average: sum(dut_count * avg_value) / sum(dut_count)
        weighted_avg = (df[dut_count_col] * df[avg_value_col]).sum() / df[dut_count_col].sum()
        results.append({'build': build, 'value': weighted_avg})

# Convert results to a DataFrame
df_result = pd.DataFrame(results)

# Step 3: Plot the bar chart using matplotlib and seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='build', y='value', data=df_result)

# Set labels and title
plt.xlabel('Build')
plt.ylabel('Weighted Avg Value')
plt.title('Weighted Average of avg_value by Build')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()
plt.show()

 
```
#### Customize bar chart colors and orders

```
# Step 3: Sort by build name, with 'REF' always being the first if it exists
df_result = df_result.sort_values('build')
if 'REF' in df_result['build'].values:
    ref_row = df_result[df_result['build'] == 'REF']
    df_result = pd.concat([ref_row, df_result[df_result['build'] != 'REF']])

# Step 4: Generate colors excluding 'red'
n_colors = len(df_result) - 1  # Exclude 'REF' which will be assigned red
unique_colors = sns.color_palette('husl', n_colors)  # Generate unique colors for all other builds

# Create color mapping where 'REF' gets red
colors_dict = {}
colors_dict['REF'] = 'red'
non_ref_builds = df_result['build'][df_result['build'] != 'REF']
for i, build in enumerate(non_ref_builds):
    colors_dict[build] = unique_colors[i]  # Assign the unique colors to other builds

# Step 5: Generate the list of colors for plotting
colors = [colors_dict[build] for build in df_result['build']]

# Step 6: Plot the bar chart using matplotlib and seaborn
plt.figure(figsize=(8, 6))
sns.barplot(x='build', y='value', data=df_result, palette=colors)

# Step 7: Add a legend for the colors
legend_patches = [mpatches.Patch(color=colors_dict[build], label=build) for build in df_result['build']]
plt.legend(handles=legend_patches, title='Build')

# Set labels and title
plt.xlabel('Build')
plt.ylabel('Weighted Avg Value')
plt.title('Weighted Average of avg_value by Build')

# Show the plot
plt.xticks(rotation=45)  # Rotate x-axis labels if needed
plt.tight_layout()
plt.show()



```



### Multi-index issue



```
i=0 metric =  "1. Horizontal Error"
group len= 1

--------------------------------
0 1. Horizontal Error
print(group)
                          Test Criteria  avg_value         dut_count            date
build_num                               4.14.17_7o    REF 4.14.17_7o REF
0          1. Horizontal Error  Average      83.59  91.85          6   3  2024-09-12

group.info()=
<class 'pandas.core.frame.DataFrame'>
Int64Index: 1 entries, 0 to 0
Data columns (total 7 columns):
 #   Column                   Non-Null Count  Dtype
---  ------                   --------------  -----
 0   (Test, )                 1 non-null      object
 1   (Criteria, )             1 non-null      object
 2   (avg_value, 4.14.17_7o)  1 non-null      float64
 3   (avg_value, REF)         1 non-null      float64
 4   (dut_count, 4.14.17_7o)  1 non-null      int64
 5   (dut_count, REF)         1 non-null      int64
 6   (date, )                 1 non-null      object
dtypes: float64(2), int64(2), object(3)
memory usage: 64.0+ bytes
None
group.index=
Int64Index([0], dtype='int64')
group.dtypes=
           build_num
Test                      object
Criteria                  object
avg_value  4.14.17_7o    float64
           REF           float64
dut_count  4.14.17_7o      int64
           REF             int64
date                      object
dtype: object
0 col= ('Test', '')
1 col= ('Criteria', '')
2 col= ('avg_value', '4.14.17_7o')
3 col= ('avg_value', 'REF')
4 col= ('dut_count', '4.14.17_7o')
5 col= ('dut_count', 'REF')
6 col= ('date', '')
DEBUG EXIT 10

build_columns = [col for col in df_per_location.columns if col not in ['Test', 'Criteria', 'date']]
build_columns=
[('Test', ''), ('Criteria', ''), ('avg_value', '4.14.17_7o'), ('avg_value', 'REF'), ('dut_count', '4.14.17_7o'), ('dut_count', 'REF'), ('date', '')]

for i, (metric, group) in enumerate(metric_groups):
   group_avg = group[build_columns].mean()  # NotImplementedError: isna is not defined for MultiIndex
   
```


###  pivot_table() vs pivot()

```

ChatGPT said:

pivot() and pivot_table() in pandas are similar, but there are key differences in when you should use each.

Use pivot() when:
There is exactly one value per group. If your data is already in a format where each combination of index and columns
has only one unique value, then pivot() works perfectly.
You want to create a simple reshaped dataframe without aggregating the data.
Example:

 
df.pivot(index=['Test', 'Criteria'], columns='build_num', values='avg_value')
This works fine if there's exactly one value of avg_value for each combination of Test, Criteria, and build_num.


df = pd.DataFrame({
    'Test': ['T1', 'T2'],
    'Criteria': ['Average', 'Average'],
    'build_num': ['build_1', 'build_2'],
    'avg_value': [10, 15],
    'cnt': [100, 200]
})

print(df)

  Test Criteria build_num  avg_value  cnt
0   T1  Average   build_1         10  100
1   T2  Average   build_2         15  200

df_pivoted = df.pivot(index=['Test', 'Criteria'], columns='build_num', values='avg_value')

for i, col in enumerate(df_pivoted.columns):
    print (i, col)

0 build_1
1 build_2

print(df_pivoted)

build_num      build_1  build_2
Test Criteria
T1   Average      10.0      NaN
T2   Average       NaN     15.0

But following fails:
import pandas as pd
df = pd.DataFrame({
    'Test': ['T1', 'T1', 'T2'],
    'Criteria': ['Average', 'Average', 'Average'],
    'build_num': ['build_1', 'build_2', 'build_1'],
    'avg_value': [10, 15, 20],
    'cnt': [100, 200,30]
})
print(df)
#0   T1  Average   build_1         10  100
#1   T1  Average   build_2         15  200
#2   T2  Average   build_1         20   30

df_pivoted = df.pivot(index=['Test', 'Criteria'], columns='build_num', values='avg_value')

ValueError: Length of passed values is 3, index implies 2.
print(df_pivoted)



Use pivot_table() when:
There are multiple values for a combination of index and columns. If there are duplicate entries for a combination
of Test, Criteria, and build_num, then pivot() will raise an error, while pivot_table() will allow you to handle
the duplicates by applying an aggregation function (e.g., mean, sum, count, etc.).
You want to apply an aggregation function during the reshaping process (e.g., calculating averages, sums, etc.).
You want to fill missing values (using the fill_value parameter).
You want to aggregate multiple columns at once (using the aggfunc parameter).
Example:
Let’s assume that there are duplicate entries in the data for a given combination of Test, Criteria, and build_num:

 
import pandas as pd

# Example dataframe with duplicate values
df = pd.DataFrame({
    'Test': ['T1', 'T1', 'T1', 'T2', 'T2', 'T2'],
    'Criteria': ['C1', 'C1', 'C1', 'C2', 'C2', 'C2'],
    'build_num': ['build_1', 'build_1', 'build_2', 'build_1', 'build_2', 'build_2'],
    'avg_value': [10, 15, 20, 30, 35, 40],
    'cnt': [100, 150, 200, 300, 350, 400]
})

# Using pivot_table to calculate the average avg_value and sum of cnt for each combination
df_pivot_table = df.pivot_table(index=['Test', 'Criteria'], columns='build_num',
                                values=['avg_value', 'cnt'], aggfunc={'avg_value': 'mean', 'cnt': 'sum'})

# Reset the index
df_pivot_table = df_pivot_table.reset_index()

# Show the result
print(df_pivot_table)
Explanation:
pivot_table() allows you to specify an aggregation function. In this case, we calculate the average of avg_value
and the sum of cnt for each combination of Test, Criteria, and build_num.
aggfunc allows specifying which aggregation function to apply (e.g., mean for avg_value and sum for cnt).
Output:
plaintext
 
build_num Test Criteria avg_value         cnt      
                         build_1 build_2 build_1 build_2
0           T1      C1      12.5    20.0     250     200
1           T2      C2      30.0    37.5     300     750
Summary:
Use pivot() when you know that each combination of the index and columns has only one value (i.e., no duplicates).
Use pivot_table() when there might be duplicate values and you need to apply an aggregation function,
or if you want additional flexibility like filling missing values or aggregating multiple columns at once.







```


### Generate list of dates in the range
```
from datetime import datetime, timedelta

def f1(start, end):
    # Convert the input strings to datetime objects
    start_date = datetime.strptime(start, '%Y-%m-%d')
    end_date = datetime.strptime(end, '%Y-%m-%d')
    
    # Create an empty list to store the dates
    date_list = []
    
    # Generate the list of dates between start and end, excluding the end date
    current_date = start_date + timedelta(days=1)
    while current_date < end_date:
        date_list.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)
    
    return date_list
```
### There are 2 pandas data frames
```
There are 2 python pandas data frames
1-st dataframe df1 has 2 columns: dut_num (string), build_num (string). 
The values in  dut_num  column are unique.
The values in  build_num are not unique. The examle of values in build_num are:
  b_1, b_2, b_3, b_2, 

The build_num may be empty. None

2-nd dataframe df2 has columns: 
   criteria(string), 
   dut1(float), 
   dut2(float), 
   dut3(float), 
   ...,
Number of columns in second dataframe is not fixed, for every value in dut_num column in 1st dataframe there is corresponding column in 2nd dataframe.

The some column names in 2nd dataframe  are present as values in 1st dataframe column "dut_num"

Goal: Create   dataframe df3 with columns: 
    criteria,
    for every build value  should be the separate column in df3, for example: b_1 (float), b_2 (float), b_3 (float)
 
The columns b_1, b_2, b_3, etc in d3 dataframe should be calculated as average from 2-nd dataframe across all columns dut* with the same build value (extracted from 1st dataframe).
Example of input:

df1 = pd.DataFrame({'dut_num': ['dut1', 'dut2', 'dut3', 'dut3'], 'build_num': ['b_1', 'b_2', 'b_1', None]})
df2 = pd.DataFrame({
    'criteria': ['c_1', 'c_2'],
    'dut1': [10, 20],
    'dut2': [30, 40],
    'dut3': [100, 200]
})
```
### Chat GPT
```
 import pandas as pd

# Input DataFrames
df1 = pd.DataFrame({
    'dut_num': ['dut1', 'dut2', 'dut3', 'dut3'],
    'build_num': ['b_1', 'b_2', 'b_1', None]
})

df2 = pd.DataFrame({
    'criteria': ['c_1', 'c_2'],
    'dut1': [10, 20],
    'dut2': [30, 40],
    'dut3': [100, 200]
})

# Step 1: Create a mapping of 'dut_num' to 'build_num' from df1
build_map = df1.set_index('dut_num')['build_num'].to_dict()

# Step 2: Melt df2 to make it long format for easier processing
df2_melted = df2.melt(id_vars=['criteria'], var_name='dut_num', value_name='dut_value')

# Step 3: Map the 'dut_num' to the corresponding 'build_num' from the build_map
df2_melted['build_num'] = df2_melted['dut_num'].map(build_map)

# Step 4: Group by 'criteria' and 'build_num', and calculate the mean for each group
df_grouped = df2_melted.dropna(subset=['build_num']).groupby(['criteria', 'build_num']).agg(
    avg_value=('dut_value', 'mean')
).reset_index()

# Step 5: Pivot the dataframe to have a column for each 'build_num'
df3 = df_grouped.pivot(index='criteria', columns='build_num', values='avg_value').reset_index()

# Step 6: Sort the build columns alphabetically
df3 = df3[['criteria'] + sorted(df3.columns.drop('criteria'))]


# Optional: Rename columns for clarity (e.g., 'b_1', 'b_2', etc.)
df3.columns.name = None  # Remove the hierarchical index name

print(df3)

  criteria    b_1   b_2
0      c_1   55.0   30.0
1      c_2  110.0   40.0

In the current implementation, the rows where the build_num is None are excluded when calculating the averages, because of the dropna() step:


df2_melted.dropna(subset=['build_num'])
This ensures that any DUT values corresponding to a None build in df1 will not be considered in the final result.
 If there are None values in the build_num, they will not appear in the final dataframe (df3),
and their corresponding DUT values will not be averaged.

If you want to include DUTs with None build values:
You could handle the None values differently depending on your desired behavior. For example, you could:
Treat None as a separate "build" and include it in the final dataframe.
Fill the None values with some default or placeholder build value (e.g., 'unknown').
Here’s how you can modify the code to include rows where build_num is None and treat it as a separate build:

Modified Code to Include None Builds as 'unknown':
python
Copy code
# Step 3 (modified): Map 'dut_num' to 'build_num', filling None values with 'unknown'
df2_melted['build_num'] = df2_melted['dut_num'].map(build_map).fillna('unknown')

# The rest of the steps remain the same
df_grouped = df2_melted.groupby(['criteria', 'build_num']).agg(
    avg_value=('dut_value', 'mean')
).reset_index()

df3 = df_grouped.pivot(index='criteria', columns='build_num', values='avg_value').reset_index()

df3.columns.name = None

print(df3)


```
### Gemini
```
import pandas as pd

def gemini( df1, df2):
  """
  Creates a new dataframe with criteria and build-specific columns.

  Args:
    df1: A pandas DataFrame with columns dut_num and build_num.
    df2: A pandas DataFrame with columns criteria, dut1, dut2, ...

  Returns:
    A pandas DataFrame with columns criteria, b_1, b_2, ...
  """

  # Merge df1 and df2 based on dut_num and corresponding dutN columns
  merged_df = pd.merge(df1, df2, left_on='dut_num', right_on=df2.columns[1:], how='left')

  # Pivot the merged dataframe
  pivoted_df = merged_df.pivot_table(index='criteria', columns='build_num', values=df2.columns[1:])

  # Fill missing values with a default value (e.g., 0)
  pivoted_df = pivoted_df.fillna(0)

  return pivoted_df

# Example usage
df1 = pd.DataFrame({'dut_num': ['dut1', 'dut2', 'dut3', 'dut3'], 'build_num': ['b_1', 'b_2', 'b_1', None]})
df2 = pd.DataFrame({
    'criteria': ['c_1', 'c_2'],
    'dut1': [10, 20],
    'dut2': [30, 40],
    'dut3': [100, 200]
})

df3 = gemini(df1, df2)
print(df3)

The provided code handles the case where the build_num is None by filling the missing values with a default value of 0.
This is done in the line:

pivoted_df = pivoted_df.fillna(0)

When the pivot table is created, any rows where the build_num is None will have missing values.
By filling these missing values with 0, we ensure that the resulting DataFrame df3 has a column
for every unique build_num and that the average calculations are performed correctly,
even if some build_num values are missing in the original data.

If you prefer a different default value, you can replace 0 with the desired value in the fillna function.
For example, to use -1 as the default value, you would write:

Python
pivoted_df = pivoted_df.fillna(-1)
```

### Image size
```
figsize=(8, 6) # width = 8 inches and the height = 6 inches. 

import matplotlib.pyplot as plt
import seaborn as sns

#Create  a figure with 2 rows and 2 columns of subplots.
# Adjust the figsize tuple to control the overall size of the figure.
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(10, 8))

#Replace 'x_values', 'y_values', and data1, data2, data3, data4 with your actual data.

# Plot 1
sns.barplot(x='x_values', y='y_values', data=data1, ax=axs[0, 0])
# Plot 2
sns.lineplot(x='x_values', y='y_values', data=data2, ax=axs[0, 1])
# Plot 3
sns.scatterplot(x='x_values', y='y_values', data=data3, ax=axs[1, 0])
# Plot 4
sns.histplot(x='x_values', data=data4, ax=axs[1, 1])

# Adjust figure and subplot parameters:

plt.tight_layout()  # Adjust spacing between subplots
# Customize subplot sizes (optional)
axs[0, 0].set_size_inches(3, 2)
axs[0, 1].set_size_inches(3, 2)
# ... adjust other subplot sizes as needed

#This saves the plot as a PNG image with a resolution of 150 dots per inch (dpi).
#The bbox_inches='tight' argument ensures the image is saved with the minimum #necessary dimensions to contain the plot.

plt.savefig('my_plot.png', dpi=150, bbox_inches='tight')



Additional tips:

Experiment with different figsize values to find the optimal size for your notebook screen.
Consider using plt.subplots_adjust() for finer control over subplot spacing.
Explore other image formats like JPEG or SVG if needed.
For larger plots, you might need to adjust the DPI or consider using a higher-resolution display.
By following these steps and adjusting the parameters as needed, you can create a visually appealing plot with subplots that is optimized for notebook screens.


### Horizontal line
```
import seaborn as sns
import matplotlib.pyplot as plt

# Create your Seaborn plot (replace with your actual plot)
sns.lineplot(x='x_values', y='y_values', data=your_data)

# Add a horizontal dotted line at y = 3 (adjust the y-value as needed)
plt.axhline(y=3, color='gray', linestyle='dotted')

plt.show()

```


```
There is Python pandas dataframe with following columns:

- date ( string in format YYYY-MM-DD)
- device (string)
- build (string)
- metric (string)
- number (float).

For every date in dataframe there are many builds, metrics and devices.

Please create separate bar chart for every metric value in dataframe.

The x-axis should be the build column and the y-axis is average(number) per build.

All bars should have a different colors  per build and the legend should provide the mapping between the

build and the bar color  
```
### Gemini:
```
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have your DataFrame named 'df'
# Replace 'your_data.csv' with your actual file path if using a CSV
# df = pd.read_csv('your_data.csv')

# Group by metric and build, calculate average number
grouped_data = df.groupby(['metric', 'build'])['number'].mean().reset_index()

# Unique metrics for iteration
unique_metrics = grouped_data['metric'].unique()

# Create a separate bar chart for each metric
for metric in unique_metrics:
    filtered_data = grouped_data[grouped_data['metric'] == metric]

    plt.figure(figsize=(10, 6))
    plt.bar(filtered_data['build'], filtered_data['number'], color=plt.cm.tab20(range(len(filtered_data))))
    plt.title(f"Average Number per Build for Metric: {metric}")
    plt.xlabel("Build")
    plt.ylabel("Average Number")

    # Create a legend
    legend_labels = [f"{build}: {color}" for build, color in zip(filtered_data['build'], plt.cm.tab20(range(len(filtered_data))))]
    plt.legend(legend_labels, title="Build Legend")

    plt.show()

```
### Gemini  - save for png or jpeg :
```
Please also save all bar charts created in code above in one  image file in jpeg or png format.

The image dimensions  should be a configurable parameters.

Using a Subplot Grid:

To efficiently combine multiple charts into a single image, we can use a subplot grid. This allows us to arrange the charts in a specified layout.

Updated Code:

Python
import matplotlib.pyplot as plt

# ... (rest of your code)

# Set image dimensions (adjust as needed)
image_width = 12
image_height = 8

# Calculate number of rows and columns based on number of metrics
num_metrics = len(unique_metrics)
num_rows = int(num_metrics / 3) + 1
num_cols = 3

# Create a subplot grid
fig, axs = plt.subplots(num_rows, num_cols, figsize=(image_width, image_height))

# Iterate over metrics and plot
for i, metric in enumerate(unique_metrics):
    row = i // num_cols
    col = i % num_cols

    filtered_data = grouped_data[grouped_data['metric'] == metric]

    axs[row, col].bar(filtered_data['build'], filtered_data['number'], color=plt.cm.tab20(range(len(filtered_data))))
    axs[row, col].set_title(f"Average Number per Build for Metric: {metric}")
    axs[row, col].set_xlabel("Build")
    axs[row, col].set_ylabel("Average Number")

    # Create a legend
    legend_labels = [f"{build}: {color}" for build, color in zip(filtered_data['build'], plt.cm.tab20(range(len(filtered_data))))]
    axs[row, col].legend(legend_labels, title="Build Legend")

# Adjust spacing between subplots
plt.tight_layout()

# Save the figure as an image
plt.savefig("combined_charts.png")  # Replace 'combined_charts.png' with your desired filename
Use code with caution.

Explanation:

Image Dimensions: Set image_width and image_height to control the size of the combined image.
Subplot Grid: Create a subplot grid using plt.subplots(). The number of rows and columns is calculated based on the number of metrics.
Iterating and Plotting: Iterate over metrics, plot each chart on the corresponding subplot using axs[row, col].
Layout Adjustment: Use plt.tight_layout() to adjust spacing between subplots.
Saving: Save the figure as an image using plt.savefig().
This code will create a single image containing all the bar charts, arranged in a grid, with adjustable dimensions. You can customize the filename and image format as needed.
```
### Gemini: On x-axis should be the date and for every date calculate and plot avg(number) per build;so it should be several bars per date.


```

On x-axis should be the date and for every date calculate and plot avg(number) per build;so it should be several bars per date.

Creating Bar Charts with Average Number per Build per Date
Understanding the Task:

We need to:

- Group the data by date and build.
- Calculate the average number for each combination.
- Create a bar chart with date on the x-axis and average number on the y-axis.
- Group bars by build and color-code them accordingly.



import pandas as pd
import matplotlib.pyplot as plt

# ... (rest of your code)

# Group by date and build, calculate average number
grouped_data = df.groupby(['date', 'build'])['number'].mean().reset_index()

# Create a bar chart
plt.figure(figsize=(12, 6))
plt.bar(grouped_data['date'], grouped_data['number'], color=plt.cm.tab20(grouped_data['build'].astype(int)))
plt.title("Average Number per Build per Date")
plt.xlabel("Date")
plt.ylabel("Average Number")

# Create a legend
legend_labels = [f"Build {build}" for build in grouped_data['build'].unique()]
plt.legend(legend_labels, title="Build Legend")

plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.show()
```


### ChatGPT
```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

# Function to generate bar charts for each metric
def plot_metrics(df, image_size=(10, 10), output_file="metrics_plots.png"):
    # Set the style of seaborn for better visualizations
    sns.set(style="whitegrid")
    
    # Get unique metrics
    metrics = df['metric'].unique()
    
    # Calculate the number of rows and columns for subplots
    num_metrics = len(metrics)
    ncols = 2  # We fix the number of columns to 2
    nrows = math.ceil(num_metrics / ncols)

    # Create subplots
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=image_size)
    axes = axes.flatten()  # Flatten the axes for easier indexing
    
    # Loop over each metric
    for i, metric in enumerate(metrics):
        ax = axes[i]
        
        # Filter dataframe for the current metric
        metric_df = df[df['metric'] == metric]
        
        # Group by build and calculate the average of the number column
        avg_df = metric_df.groupby('build')['number'].mean().reset_index()
        
        # Plot the bar chart
        sns.barplot(x='build', y='number', data=avg_df, ax=ax, palette="husl")

        # Set title and labels
        ax.set_title(f"Metric: {metric}")
        ax.set_xlabel('Build')
        ax.set_ylabel('Average Number')
        ax.legend(title="Build", loc='best')
        
        # Rotate x labels for better readability
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot as a file
    fig.savefig(output_file, format=output_file.split('.')[-1])
    plt.close()

# Example usage
# Assuming df is your pandas dataframe
# df = pd.read_csv("your_dataframe.csv")
# plot_metrics(df, image_size=(20, 10), output_file="metrics_plots.png")
```

### ChatGPT: plot bar charts where the x-axis is the date, and for each date, it shows the average number for each build. Multiple bars will be plotted per date, one for each build.

```
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Function to generate bar charts with x-axis as dates and multiple bars for builds
def plot_avg_per_build_per_date(df, image_size=(12, 8), output_file="avg_build_per_date.png"):
    # Set the style of seaborn for better visualizations
    sns.set(style="whitegrid")
    
    # Group by date and build, calculate the average of 'number'
    avg_df = df.groupby(['date', 'build'])['number'].mean().reset_index()

    # Create the barplot
    plt.figure(figsize=image_size)
    sns.barplot(x='date', y='number', hue='build', data=avg_df, palette="husl")
    
    # Set title and labels
    plt.title('Average Number per Build per Date')
    plt.xlabel('Date')
    plt.ylabel('Average Number')

    # Rotate x labels for better readability
    plt.xticks(rotation=45, ha='right')

    # Adjust the layout
    plt.tight_layout()

    # Save the plot to file
    plt.savefig(output_file, format=output_file.split('.')[-1])
    plt.close()

# Example usage
# Assuming df is your pandas dataframe
# df = pd.read_csv("your_dataframe.csv")
# plot_avg_per_build_per_date(df, image_size=(15, 10), output_file="avg_build_per_date.png")

```


https://pyvista.org/  (on top of VTK)

https://python-graph-gallery.com/

https://habr.com/ru/companies/astralinux/articles/814881/ HoloViews + Flask

https://holoviews.org/user_guide/Deploying_Bokeh_Apps.html#combining-bokeh-application-and-flask-application

https://github.com/rougier/scientific-visualization-book .  BOOK!

https://habr.com/ru/companies/ru_mts/articles/738208/ Plotting

https://habr.com/ru/companies/ru_mts/articles/738208/ matplotlib

https://github.com/TutteInstitute/datamapplot

https://towardsdatascience.com/professionally-visualize-data-distributions-in-python-09481e1493b2

https://python.plainenglish.io/data-visualization-for-exploratory-data-analysis-eda-in-python-4aea402648e7

https://towardsdatascience.com/declarative-vs-imperative-plotting-3ee9952d6bf3

### Visro
https://github.com/mckinsey/vizro

## PyVis

https://medium.com/@stephanhausberg/graph-networks-visualization-with-pyvis-and-keyword-extraction-cd973d372e2c

https://github.com/garrettj403/SciencePlots

https://lets-plot.org/

https://proplot.readthedocs.io/en/stable/ proplot

https://dataviz.dylancastillo.co/

https://habr.com/ru/company/otus/blog/682500/.  Python based dashboards

https://www.youtube.com/watch?v=cTJBJH8hacc matplotlib tutorial

https://github.com/ponnhide/patchworklib subplot manager

https://github.com/lux-org/lux

https://towardsdatascience.com/the-easiest-way-to-make-beautiful-interactive-visualizations-with-pandas-cdf6d5e91757

https://sophiamyang.github.io/DS/visualization/holoviz/holoviz.html


https://shiny.rstudio.com/py/ 
### EDA 


https://www.zenrows.com/blog/exploratory-data-analysis-in-python

https://towardsdatascience.com/exploratory-sensor-data-analysis-in-python-3a26d6931e67

https://towardsdatascience.com/exploratory-data-analysis-visualization-and-prediction-model-in-python-241b954e1731


https://towardsdatascience.com/complete-guide-to-data-visualization-with-python-2dd74df12b5e

https://github.com/marcskovmadsen/panel-highcharts

https://xcorr.net/2021/06/02/dynamic-scientific-visualizations-in-the-browser-for-python-users/

https://github.com/rougier/scientific-visualization-book

https://plotly.com/python/

https://pypi.org/project/autoplotter/ (using Dash)

https://pypi.org/project/sweetviz/

https://geekyhumans.com/draw-various-types-of-charts-and-graphs-using-python/ Matplotlib and Plotly

https://habr.com/ru/company/otus/blog/558478/

https://python-graph-gallery.com/ Pandas, Seaborn, Matplotlib examples!

https://pythonplot.com/  Pandas, Seaborn, Matplotlib examples!

https://matplotlib.org/stable/gallery/index.html Matplotlib examples

https://towardsdatascience.com/a-practical-summary-of-matplotlib-in-13-python-snippets-4d07f0011bdf

https://github.com/matplotlib/cheatsheets

https://machinelearningmastery.com/seaborn-data-visualization-for-machine-learning

https://habr.com/ru/post/557424/

https://github.com/antonlopezr/mpl_plotter

https://medium.com/codex/beyond-matplotlib-and-seaborn-python-data-visualization-tools-that-work-3ef7f8d1500e

https://www.machinelearningplus.com/plots/top-50-matplotlib-visualizations-the-master-plots-python/

https://www.practicaldatascience.org/html/plotting_part2.html



https://stackabuse.com/matplotlib-draw-vertical-lines-on-plot/ vertical line in matplotlib

https://towardsdatascience.com/a-simple-guide-to-beautiful-visualizations-in-python-f564e6b9d392

https://pypi.org/project/dama/

http://pyviz.org/

http://vispy.org/

https://datavizcatalogue.com/

http://datavizproject.com/

https://towardsdatascience.com/plotting-with-python-c2561b8c0f1f

https://kite.com/blog/python/data-analysis-visualization-python

## Python plotting code examples

https://towardsdatascience.com/advanced-pandas-plots-e2347a33d576 . Advanced Pandas Plots

https://www.youtube.com/watch?v=mZOIeOeswB0


https://pythonplot.com/

https://python-graph-gallery.com/

https://cmdlinetips.com/2020/01/tips-to-make-common-plots-with-pandas/

https://www.kite.com/blog/python/data-analysis-visualization-python/

https://github.com/lux-org/lux

### HVPLOT
https://hvplot.holoviz.org/ hvplot !!!

https://github.com/antonlopezr/mpl_plotter

## Seaborn

http://seaborn.pydata.org/examples/index.html

https://habr.com/ru/company/otus/blog/540526/

<https://view.datalore.jetbrains.com/notebook/v8mLoENq8XTfmStTCLNMV6> seaborn

<https://soliddata.io/index.php/2020/03/31/how-to-do-data-visualization-with-python/> seaborn

<https://mlwhiz.com/blog/2019/04/19/awesome_seaborn_visuals/> .  seaborn


https://jbencook.com/pandas-melt/    pd.melt(wide_df)

https://jbencook.com/seaborn-histogram/

To see multiple distributions in the same plot. 
If your Pandas DataFrame is in long format, 
you can do this by passing in a categorical column to the hue argument:
```
ax = sns.histplot(df, x="revenue", bins=30, stat="probability", hue="region")
ax.set(ylabel="$p(x)$")
```
## Pandas plotting 

https://opendatascience.com/how-to-pivot-and-plot-data-with-pandas/

https://cmdlinetips.com/2020/01/tips-to-make-common-plots-with-pandas/

https://jbencook.com/pandas-melt/

https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#cookbook-plotting

https://pandas.pydata.org/pandas-docs/stable/user_guide/visualization.html


https://www.shanelynn.ie/bar-plots-in-python-using-pandas-dataframes/

https://queirozf.com/entries/pandas-dataframe-plot-examples-with-matplotlib-pyplot

 
Line plot, multiple columns:
Just reuse the Axes object.
```
import matplotlib.pyplot as plt
import pandas as pd

# gca stands for 'get current axis'
ax = plt.gca()

df.plot(kind='line',x='name',y='num_children',ax=ax)
df.plot(kind='line',x='name',y='num_pets', color='red', ax=ax)

plt.show()
```

## Pivot, pivot_table() and transpose()

https://opendatascience.com/how-to-pivot-and-plot-data-with-pandas/

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot.html

df.pivot(index='hour', columns='dayname', values="MB").plot(title=header)

df2=pd.pivot_table(df, index=['date'], columns='company' values='MB'  )

## Heatmaps

https://blog.algorexhealth.com/2017/09/10-heatmaps-10-python-libraries/

https://medium.com/@kbrook10/day-4-data-visualization-how-to-use-seaborn-for-heatmaps-bf8070e3846e Heatmap


### Heatmaps in plotnine

https://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_tile.html

https://plotnine.readthedocs.io/en/stable/generated/plotnine.geoms.geom_bin2d.html


### Lag plot , Autocorrelated plot

https://www.kaggle.com/residentmario/time-series-plotting-optional

https://www.statology.org/autocorrelation-python/

https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.autocorr.html

https://machinelearningmastery.com/gentle-introduction-autocorrelation-partial-autocorrelation/

https://stackoverflow.com/questions/56028461/calculate-autocorrelation-as-a-function-of-lag-in-python

https://pythontic.com/visualization/charts/autocorrelation

https://medium.com/@dganais/autocorrelation-in-time-series-c870e87e8a65

https://www.geeksforgeeks.org/autocorrelation-plot-using-matplotlib/


## Matplotlib

https://github.com/rougier/matplotlib-tutorial

https://github.com/rougier/scientific-visualization-book

<https://habr.com/ru/post/468295/>

<https://realpython.com/python-matplotlib-guide/>

<https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f>

<https://nbviewer.jupyter.org/urls/gist.githubusercontent.com/Jwink3101/e6b57eba3beca4b05ec146d9e38fc839/raw/f486ca3dcad44c33fc4e7ddedc1f83b82c02b492/Matplotlib_Cheatsheet>

<http://blog.adnansiddiqi.me/tag/matplotlib/>

https://github.com/fonnesbeck/Bios8366/blob/master/notebooks/Section0_2-Plotting-and-Visualization.ipynb

https://medium.com/100-free-udemy-coupons/udemy-making-graphs-in-python-using-matplotlib-for-beginners-free-be3df23bdabe

https://github.com/matplotlib/AnatomyOfMatplotlib

http://www.labri.fr/perso/nrougier/teaching/matplotlib/matplotlib.html

https://www.numfocus.org/blog/matplotlib-lead-developer-explains-why-he-cant-fix-the-docs-but-you-can/

<https://github.com/antonkorbalev/simplesysmon>  Matplotlib +  Flask

http://queirozf.com/entries/matplotlib-pylab-pyplot-etc-what-s-the-different-between-these

http://hypertools.readthedocs.io/en/latest/index.html
	
https://towardsdatascience.com/data-visualization-with-bokeh-in-python-part-one-getting-started-a11655a467d4

<https://www.youtube.com/watch?v=z7ZINBk8EUk&list=PL998lXKj66MpNd0_XkEXwzTGPxY2jYM2d>

<https://habr.com/ru/post/468295/> matplotlib

<https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f>

<https://github.com/mcastorina/graph-cli> .  plottting from CSV



### Plotnine

https://evamaerey.github.io/ggplot_flipbook/ggplot_flipbook_xaringan.html#1

https://youtu.be/z6xNKZZMWgU

<https://plotnine.readthedocs.io/en/stable/> 

https://github.com/has2k1/plotnine-examples/

<https://leanpub.com/plotnine-guide> . book

https://dputhier.github.io/jgb53d-bd-prog_github/practicals/intro_ggplot/intro_ggplot.html

https://datascienceworkshops.com/blog/plotnine-grammar-of-graphics-for-python/

https://www.practicaldatascience.org/html/plotting_part2.html

<https://github.com/has2k1/plotnine> as ggplot2

https://realpython.com/ggplot-python/

https://www.kaggle.com/residentmario/grammar-of-graphics-with-plotnine-optional

https://github.com/has2k1/plotnine-examples/blob/master/plotnine_examples/examples/facet_grid.ipynb

<https://towardsdatascience.com/how-to-use-ggplot2-in-python-74ab8adec129>

what is hstack?
```
 import numpy as np
 x=np.array((3,5,7))
 y=np.array((30,50,70))
 np.hstack((x,y))
 array([ 3,  5,  7, 30, 50, 70])
 xx=np.array([[3],[5],[7]])
>>> xx
array([[3],
       [5],
       [7]])
yy=np.array([[30],[50],[70]])
>>> np.hstack((xx,yy))
array([[ 3, 30],
       [ 5, 50],
       [ 7, 70]])

```
Plotnine works best with tidy data, i.e each variable is a column and each observation a row.
https://stackoverflow.com/questions/62900745/how-to-add-legend-in-ggplot-plotnine-for-multiple-curves
```
from plotnine import *
import numpy as np
import pandas as pd

str_metric = 'metric'
metric = np.array([0.127, 0.1715, 0.19166667, 0.21583333, 0.24866667, 0.24216667, 0.24433333,
                   0.255, 0.291, 0.30966667, 0.32033333, 0.2415, 0.33833333, 0.30583333, 0.34433333])

metric2 = metric * 2

iterations2 = [i for i in range(len(metric))]

# tidy data
df = pd.DataFrame({
    'iterations': np.hstack([iterations2, iterations2]),
    'value': np.hstack([metric, metric2]),
    'type': np.repeat(['metric', 'metric2'], len(iterations2))   
})

p = (ggplot(df, 
     aes(x='iterations', y='value', color='type'))
     + geom_smooth(method='lm', span=0.10, se=True, level=0.80)
     # Then you can change the colour using a scale
    )
```    



### facet grid and other examples:
 
https://github.com/has2k1/plotnine-examples/tree/master/plotnine_examples 

Facet a discrete variable into rows: 
```
facet_grid('drv ~ .')
```
Facet a discrete variable into columns:
```
facet_grid('. ~ cyl')
```

Facet two discrete variables into rows and columns:
```
facet_grid('drv ~ cyl')
```

You can choose if the scale of x- and y-axes are fixed or variable by using the scales argument within the facet_grid() command:
```
(
    ggplot(mpg, aes(x='displ', y='hwy')) 
    + geom_point()
    + facet_grid('drv ~ .', scales = 'free')
    + labs(x='displacement', y='horsepower')
)
```

2-dimentional grid
```
facet_grid('drv + transmission ~ .')
```


https://www.anaconda.com/blog/developer-blog/python-data-visualization-2018-why-so-many-libraries/

https://codeburst.io/overview-of-python-data-visualization-tools-e32e1f716d10

https://youtu.be/FytuB8nFHPQ

http://pbpython.com/python-vis-flowchart.html


### Pywedge
https://towardsdatascience.com/pywedge-a-complete-package-for-eda-data-preprocessing-and-modelling-32171702a1e0

https://pypi.org/project/pywedge/

<https://github.com/JetBrains/lets-plot/blob/master/README_PYTHON.md> as ggplot2


### Datapane 
is a Python framework for building beautiful data science documents for your company, clients, or community.
<https://datapane.com>

<http://haifengl.github.io/vegalite.html>

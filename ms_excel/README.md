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

### Example 0:

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

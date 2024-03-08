https://www.pythonexcel.com/

https://realpython.com/openpyxl-excel-spreadsheets-python/

https://blog.aspose.com/cells/create-excel-xls-xlsx-using-python-excel-api/

https://stackoverflow.com/questions/13437727/how-to-write-to-an-excel-spreadsheet-using-python

https://www.xlwings.org/

https://openpyxl.readthedocs.io/en/stable

https://github.com/jmcnamara/XlsxWriter

https://xlsxwriter.readthedocs.io/

https://forum.codewithmosh.com/t/creating-a-graph-in-excel/21607/7


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

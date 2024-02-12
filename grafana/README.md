### AWS CloudWatch  
https://aws.plainenglish.io/observability-in-aws-cloudwatch-ed60a2c4fdcd

### Clickhouse + Grafana

https://habr.com/ru/companies/ozontech/articles/774712/


### Tooltip customization

1. 
https://stackoverflow.com/questions/77984607/how-to-add-extra-info-in-tooltips-on-grafana-time-series-dashboard-based-on-sql

2.
https://community.grafana.com/t/how-to-add-extra-info-in-tooltips-on-grafana-time-series-dashboard-based-on-sql/114297
 
3.  
 https://github.com/grafana/grafana/issues/73989

### Datasource as variable, repeat and other Grafana tricks

https://habr.com/ru/companies/karuna/articles/771134/

variable name: datasource

variable type:  Data Source
$(datasource)

### import dashboard

http://105.140.16.223:3000/dashboard/import

### grafana.ini
./System/Volumes/Data/opt/homebrew/etc/grafana/grafana.ini
./System/Volumes/Data/opt/homebrew/Cellar/grafana/10.1.1/.bottle/etc/grafana/grafana.ini
```
[date_formats]
# For information on what formatting patterns that are supported https://momentjs.com/docs/#/displaying/

# Default system date format used in time range picker and other places where full time is displayed
;full_date = YYYY-MM-DD HH:mm:ss
;full_date = YYYY-MM-DD


;default_timezone = browser
default_timezone = UTC
```

### Date Selector  in Grafana variable 
```
select $__timeFrom()        -- 2023-01-01T08:00:00Z

select substr($__timeFrom(), 1, 10 );

select DATE($__timeFrom())  -- 1672531200000

select ${__from} -- 1672560000000
select ${__from:date:YYYY-MM-DD}  -- 2021

Postgres:
SELECT to_char(to_timestamp(1195374767),'YYYY-MM-DD');

So combining:

select
to_char(to_timestamp(${__from}),'YYYY-MM-DD');

select metric from daily_kpi where dt = DATE(substr($__timeFrom(), 1, 10) );
 

```

### How to Embedd external Webpage to Grafana
https://stackoverflow.com/questions/65847384/embedding-a-website-in-a-grafana-dashboard
```
<!--
<iframe style="width: 100%; height: 100%" src="http://gnss-spotlight.ssi.samsung.com:8090/daily_main_container.php?test_date=2023-10-06"></iframe>
-->
<iframe style="width: 100%; height: 100%" src="http://gnss-spotlight.ssi.samsung.com:8090/daily_main_container.php?test_date=${__from:date:YYYY-MM-DD}"></iframe>
```


### Grafana release notes

https://habr.com/ru/companies/kts/articles/782940/ Grafana 10 new features

https://grafana.com/blog/2023/06/13/grafana-10-release-all-the-new-features-to-know/
 
https://grafana.com/blog/2023/08/24/grafana-10.1-release-all-the-latest-features/

https://grafana.com/blog/2023/10/24/grafana-10.2-release-grafana-panel-title-generator-interactive-visualizations-and-more

### Stack overflow

https://stackoverflow.com/questions/77304277/grafana-does-not-update-the-variable-which-depends-on-datetime-picker

https://community.grafana.com/t/grafana-does-not-update-the-variable-which-depends-on-datetime-picker/105690

https://community.grafana.com/t/issue-with-transformation-prepare-time-series-multi-frame-time-series/105397

https://stackoverflow.com/questions/77276225/grafana-dashboard-bar-chart-for-time-series

https://stackoverflow.com/questions/77268256/grafana-dashboard-how-to-avoid-typing-similar-sqls-which-are-different-only-by

https://community.grafana.com/t/how-to-avoid-typing-similar-sqls-which-are-different-only-by-filter-value-in-where-clause/105296

https://community.grafana.com/t/bar-char-based-on-sql-with-2-items-in-group-by/103510

https://stackoverflow.com/questions/77100024/grafana-bar-chart-based-on-sql-with-2-items-in-group-by


### Mac

brew install postgresql@15

brew services start postgresql@15

brew install grafana

brew services start grafana


### Color mapping

Bar chart -> Overrides -> fields with name -> In dropdown select description -> value mapping


### Bar chart: how to plot categorial values  (not time) on X - axis

Bar chart allows to plot categorical values on X-axis:

https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/bar-chart/

https://play.grafana.org/d/ktMs4D6Mk/5-bar-charts-and-pie-charts?orgId=1

https://www.youtube.com/watch?v=ky78RZ2f7oc
```
select metric, DUT, v  from daily_kpi where dt='2023-01-01' order by metric
Let make: X-axis: metric legend - DUT 

Apply transformation: "Grouping to matrix" to make the bar chart where X-axis is not the date
****************************************
 Column: dut
 Row: metric <-- will be X-axis
 Cell value : V
```

If data is present in following table format (dt, dut, metric1 int, metric2 int, metric3 int)
we need to convert it to format (dut, metric, value) to feed to grafana:

```
select dut, 'm1' as metric, m1  as value from daily 
union all
select dut, 'm2' as metric, m2  as value from daily 

```

https://www.youtube.com/watch?v=Bu-MxNJT44c

https://community.grafana.com/t/plotting-non-time-series-on-x-axis/70913/9

```
Hide x axis legend 
xAxis: {
show: false },
```

### Grafana date/time picker: 
press Ctrl button to set the range

### Formatting dates

File: defaults.ini 
```
[date_formats]
# For information on what formatting patterns that are supported https://momentjs.com/docs/#/displaying/

# Default system date format used in time range picker and other places where full time is displayed
full_date = YYYY-MM-DD HH:mm:ss
```
### ChatGPT

```

SELECT product,
       date,
       MAX(price) AS max_price
FROM T
WHERE date BETWEEN :start_date AND :end_date
GROUP BY product, date

Create a Grafana Panel:

Open your Grafana dashboard and create a new panel.
Choose "Table" as the visualization type for now. We'll change it to a bar chart later.
Configure the Data Source:

In the "Query" section of your panel, select your PostgreSQL data source.
Write the SQL query that retrieves the data as discussed earlier, including product, date, and MAX(price).
Use $start and $end as variables for the user-provided date range (replace these variables with the appropriate syntax if your Grafana version uses different placeholders).
Convert to a Bar Chart:

After configuring the data source query, change the visualization type from "Table" to "Graph."

```
#### Configure the x-axis and y-axis settings:
```
For the x-axis, select the date field.
For the y-axis, select the max_price field.
Set the "Mode" to "Bars."
Choose "product" for "Group by."
Customize the Chart:

Customize the appearance of the chart as desired, including labels, axis names, and legends.
```
#### Set Label Names (Alias By):
```
Scroll down to the "Legend" section of the panel settings.
In the "Alias By" field, you can specify how you want to label the bars on the x-axis. You can use template variables to dynamically generate the labels.
To label the bars by the product field, simply enter $product in the "Alias By" field. This will use the product values as the labels for the bars.
Customize the Chart:

Time Range Picker:

Make sure your Grafana dashboard has a time range picker that allows users to select the date range. This ensures that the $start and $end variables are populated correctly.
Save and View:

Save your panel and view it on your dashboard. Users can now select a date range using the time range picker,
 and the bar chart will display the maximum price per product for each date within the selected range.
By following these steps, you can create a Grafana bar chart that visualizes the maximum price per product for each date within a user-provided date range.

```
### Consistent Colors

```
To ensure consistent colors for the same attribute name in different Grafana panels, you can use Grafana's built-in alias pattern and color mapping options. Here's how you can achieve this:

Define an Alias Pattern:

In each of your panels, go to the "Query" or "Visualization" settings where you configure the display of your data.
Look for an "Alias" or "Legend" setting. Grafana allows you to specify an alias pattern using variables and labels.
Create a consistent alias pattern that includes a label from your data that remains constant for the same attribute name across different panels. For example, if you have an attribute named "AttributeName," your alias pattern might be something like Attribute Name: $Attribute.
Set Up Color Mapping:

In Grafana, you can set up color mapping based on the alias pattern.
Go to the "Panel" settings (not the query settings) for each panel.
Look for a "Legend" or "Display" section, depending on the visualization type.
In this section, you'll find an option to define colors based on series or aliases.
Create color mappings that specify consistent colors for specific alias patterns. For example, you can assign the color blue to all series with the alias pattern Attribute Name: A and red to Attribute Name: B, and so on.
Apply the Alias Patterns:

Ensure that you apply the same alias pattern to the same attribute name in different panels. This consistency will ensure that Grafana assigns the same color to the same attribute name across panels.
By following these steps, you can achieve consistent coloring for the same attribute name in different Grafana panels. Grafana will use the alias patterns you defined to assign colors, making it easier to visually identify and compare data across panels.
```

###  Repeat  Panel
```
Question #1: Avoiding Long and Repetitive SQL Queries
--------------------------------------
To avoid typing 12 very similar but long SQL queries, you can use Grafana's built-in support for templating and dynamic queries.
Grafana allows you to create dynamic dashboards using variables. Here's how you can achieve this:

Create a Template Variable for Month:

Create a template variable named "Month" as previously described.
activate SHOW ALL

Modify Your SQL Queries:

In your SQL queries for each panel, you can use the template variable like this:
 
WHERE month_column = $Month

This SQL clause ensures that each panel filters data for the selected month.
Use Repeat Panels Feature:

Grafana offers a "Repeat Panels" feature that allows you to create a single panel
and repeat it for each value of the template variable (in your case, 12 months). Here's how to set it up:
Edit your dashboard.
Click on the panel you want to repeat.
In the "Panel Title" section, click the "Repeat" checkbox.
Select the "Month" template variable from the dropdown.
Grafana will automatically create 12 panels, one for each month, and apply the appropriate SQL filter for each panel.
This approach significantly reduces the need for repetitive SQL queries and allows you to manage all 12 panels efficiently.

Question #2: Avoiding Dropdown Selection for All 12 Months
---------------------
If you have exactly 12 months and you want to display all of them without asking the user to select them via a dropdown list,
you can use the "Repeat Panels" feature as mentioned above. This will automatically create and display all 12 panels,
each filtered for a different month,
without requiring user interaction.

With the "Repeat Panels" feature, you can achieve your goal of displaying data for all 12 months simultaneously without redundant dropdown selections.


Panel Title: Suppose you have a panel with a title like "My Panel."

Repeat Panels: When you enable the "Repeat" feature for this panel and select a template variable, Grafana will create multiple panels,
one for each value of the template variable.

Generated Titles: Grafana generates titles for the repeated panels by appending the selected variable values to the original panel title.
 For example, if your variable is "Month" and has values like "January," "February," "March," etc., Grafana will create panels with titles like:

"My Panel - January"
"My Panel - February"
"My Panel - March"
and so on for each selected month.

This naming convention allows you to easily identify and differentiate the repeated panels based on the values of the template variable.
It's especially useful when you have a dashboard with many panels, each representing different subsets of data or time periods.



you have pairs of panels for each month, with a bar chart on the left and a table on the right, and the table uses the data from the left panel.
If you want to create similar pairs of panels for all 12 months efficiently, you can still use Grafana's "Repeat Panels" feature along with template variables. Here's how you can achieve this:

Create a Template Variable for Month:

Create a template variable named "Month" as previously described.
Create Your Left Panel (Bar Chart):

Create the left panel (bar chart) as you normally would, using the "Month" template variable in your SQL queries to filter data for the selected month.
Create Your Right Panel (Table):

Create the right panel (table) next to the left panel.
In the SQL query for the right panel, use the "Month" template variable as a filter, just like in the left panel.
Since the right panel is designed to use the same month as the left panel, you can use the same "Month" template variable.
Enable "Repeat Panels" for Both Panels:

Edit the left panel, and in the "Panel Title" section, click the "Repeat" checkbox.

Select the "Month" template variable from the dropdown.

Similarly, edit the right panel and enable the "Repeat" checkbox with the same "Month" template variable.

Now, when you enable "Repeat Panels" for both the left and right panels using the same template variable, Grafana will automatically create pairs of panels for all 12 months. You'll have pairs of bar charts and tables, with each pair representing a different month. The right table panel in each pair will use the same month selected in the corresponding left bar chart panel.

This approach allows you to efficiently create and manage pairs of panels for all 12 months without manually duplicating them.

If you have set up your Grafana dashboard to use the "Repeat Panels" feature with a template variable for months and you've configured it to display all 12 months simultaneously, Grafana will not show a dropdown list with template variable values on top of the dashboard. The dropdown list is typically used when you want users to select a specific value from the variable, but in this case, the dashboard will automatically display all 12 panels corresponding to the 12 months without requiring user interaction.

When you enable the "Repeat Panels" feature and use a template variable, Grafana will generate the panels for each value of the variable (in your case, each month) and display them side by side on the dashboard without the need for a dropdown selection. Users will see all the data for all 12 months at once.  


```
### Deploy to another machine:

```
Deploying a Grafana dashboard from one machine to another typically involves exporting the dashboard configuration a
nd then importing it on the target machine.
Here are the general steps to achieve this:

Export the Dashboard:
--------------------
Open the Grafana Dashboard: Make sure you are logged in to the Grafana instance where your dashboard is located.

Select the Dashboard: Click on the dashboard you want to export to select it.

Export the Dashboard JSON: To export the dashboard configuration, click on the gear icon (⚙️) in the top right corner of the dashboard, then select "Export."

Save the JSON File: This will generate a JSON file containing your dashboard configuration. Save this file to your local machine.

Transfer the Dashboard JSON File:

Copy the exported JSON file to the target machine where you want to deploy the dashboard. You can use methods such as SCP, SFTP,
or any file-sharing mechanism to transfer the file to the target machine.

Import the Dashboard:
---------------------
Open Grafana on the Target Machine: Make sure you are logged in to the Grafana instance on the target machine.

Access the Dashboard Section: In Grafana, go to the "Dashboards" section.

Import the Dashboard: Click the "Import" button to open the import dashboard dialog.

Upload the JSON File: In the import dashboard dialog, you can either paste the JSON content or upload the JSON file you exported earlier.
To upload the file, click "Upload JSON File" and select the file from your local machine.

Import the Dashboard: After uploading the JSON file, click the "Load" button. Grafana will parse the JSON file and display a preview of the dashboard.
----------------------------------------------------------------------------
Configure the Import Settings: Review and configure the import settings as needed. You may need to map data sources, variables, or other settings to match your target Grafana instance.

Import the Dashboard: Once you are satisfied with the import settings, click the "Import" button to create the dashboard on the target machine.

Your dashboard should now be available and accessible on the target machine's Grafana instance with all its panels and settings intact.

Keep in mind that the target machine should have the necessary data sources and configurations set up to ensure the dashboard functions correctly.
If there are any differences in data sources or environment settings between the two machines, you may need to adjust the dashboard configuration accordingly.
```

### Grafana Plugins

https://grafana.com/grafana/plugins/volkovlabs-echarts-panel/  Apache ECharts plugin

https://grafana.com/grafana/plugins/

https://habr.com/ru/companies/flant/articles/423851/

https://gapit-htmlgraphics-panel.gapit.io/
Благодаря связке JavaScript с HTML и CSS он позволяет реализовывать любую логику и визуализацию панелей. Код можно править прямо в настройках панели и без дополнительных манипуляций на стороне Grafana.

### Grafana
http://localhost:3000/login   admin/admin

https://grafana.com/grafana/download

https://www.metricfire.com/blog/grafana-dashboards-from-basic-to-advanced/

https://sbcode.net/grafana/

https://medium.com/grafana-tutorials/graphing-non-time-series-sql-data-in-grafana-8a0ea8c55ee3

### Transformation

#### Transformation: Preparing time series
Bat chart color scheme: Classic Palette
For bar chart  grouping by date:
```
Bat chart color scheme: Classic Palette
Transform: Prepare time series
Format: Multi-frame time series

select report_date, description, kpi_value as " "
from kpi 
where kpi_category = 'SemiShadedVDR-SuwonStation' 
and kpi_metric='SpeedError_Max'
and report_date >= DATE($__timeFrom()) 
and report_date <= DATE($__timeTo()) 
order by report_date, description;

```

#### Grouping to matrix (pivoting) - for Table Pallete

For Table panel to get 1 row and many columns (as many columns ar many unique descriptions in following SQL
```
select CAST(report_date AS TEXT) as report_date, description, value
Transormation: Grouping to matrix
Column: description
Row: report_date
Cell value: value
```
https://volkovlabs.io/blog/transformations-grafana-20230519/

https://grafana.com/docs/grafana/latest/panels-visualizations/query-transform-data/transform-data/

https://www.youtube.com/watch?v=aoAmRHq3vhU


### Grafana as  a code

https://medium.com/@tarantool/grafana-as-code-b642cac9ae75

https://andidog.de/blog/2022-04-21-grafana-dashboards-best-practices-dashboards-as-code

### Variables

https://grafana.com/docs/grafana/latest/dashboards/variables/add-template-variables/

https://nightingaledvs.com/how-to-in-grafana%E2%80%8A-%E2%80%8Apart-2-creating-interactive-dashboards/
```
Go to the dashboard Settings -> Variables and create a new variable with the type set to Query. Select your   data source as Data Source. Then you can write a SQL query that returns one column with all your test names. Save the variable.

Then there should be a dropdown at the top of the dashboard where you can choose the test name you want from. Then use the variable in your query, for example in the WHERE clause to filter for those test names only.

Variable drop-down lists are displayed in the order they are listed in the variable list in Dashboard settings.
Put the variables that you will change often at the top, so they will be shown first (far left on the dashboard).
By default, variables don’t have a default value. This means that the topmost value in the drop-down is always preselected. If you want to pre-populate a variable with an empty value, you can use the following workaround in the variable settings:
Select the Include All Option checkbox.
In the Custom all value field, enter a value like +.
```


 There are 7 types of variables
 Query variables:
 ```
SELECT answer, count(distinct respondent) as value
FROM survey_data
WHERE application = '$application'
AND question = '$question'
GROUP BY answer
```
https://www.timescale.com/blog/grafana-variables-101/

https://fmancardi.wordpress.com/2021/01/16/learning-grafana-using-url-variables-in-sql-queries/

https://grafana.com/docs/grafana/latest/dashboards/variables/variable-syntax/#time-range-variables

### Macros / Postgres

https://grafana.com/docs/grafana/latest/datasources/postgres/#macros

```
Macros
Macros can be used within a query to simplify syntax and allow for dynamic parts.

Macro example	Description
$__time(dateColumn)	Will be replaced by an expression to convert to a UNIX timestamp and rename the column to time_sec. For example, UNIX_TIMESTAMP(dateColumn) as time_sec
$__timeEpoch(dateColumn)	Will be replaced by an expression to convert to a UNIX timestamp and rename the column to time_sec. For example, UNIX_TIMESTAMP(dateColumn) as time_sec
$__timeFilter(dateColumn)	Will be replaced by a time range filter using the specified column name. For example, dateColumn BETWEEN FROM_UNIXTIME(1494410783) AND FROM_UNIXTIME(1494410983)
$__timeFrom()	Will be replaced by the start of the currently active time selection. For example, FROM_UNIXTIME(1494410783)
$__timeTo()	Will be replaced by the end of the currently active time selection. For example, FROM_UNIXTIME(1494410983)
$__timeGroup(dateColumn,'5m')	Will be replaced by an expression usable in GROUP BY clause. For example, *cast(cast(UNIX_TIMESTAMP(dateColumn)/(300) as signed)*300 as signed),*
$__timeGroup(dateColumn,'5m', 0)	Same as above but with a fill parameter so missing points in that series will be added by grafana and 0 will be used as value.
$__timeGroup(dateColumn,'5m', NULL)	Same as above but NULL will be used as value for missing points.
$__timeGroup(dateColumn,'5m', previous)	Same as above but the previous value in that series will be used as fill value if no value has been seen yet NULL will be used (only available in Grafana 5.3+).
$__timeGroupAlias(dateColumn,'5m')	Will be replaced identical to $__timeGroup but with an added column alias (only available in Grafana 5.3+).
$__unixEpochFilter(dateColumn)	Will be replaced by a time range filter using the specified column name with times represented as Unix timestamp. For example, dateColumn > 1494410783 AND dateColumn < 1494497183
$__unixEpochFrom()	Will be replaced by the start of the currently active time selection as Unix timestamp. For example, 1494410783
$__unixEpochTo()	Will be replaced by the end of the currently active time selection as Unix timestamp. For example, 1494497183
$__unixEpochNanoFilter(dateColumn)	Will be replaced by a time range filter using the specified column name with times represented as nanosecond timestamp. For example, dateColumn > 1494410783152415214 AND dateColumn < 1494497183142514872
$__unixEpochNanoFrom()	Will be replaced by the start of the currently active time selection as nanosecond timestamp. For example, 1494410783152415214
$__unixEpochNanoTo()	Will be replaced by the end of the currently active time selection as nanosecond timestamp. For example, 1494497183142514872
$__unixEpochGroup(dateColumn,'5m', [fillmode])	Same as $__timeGroup but for times stored as Unix timestamp (only available in Grafana 5.3+).
$__unixEpochGroupAlias(dateColumn,'5m', [fil



Min time interval
A lower limit for the $__interval and $__interval_ms variables. Recommended to be set to write frequency, for example 1m if your data is written every minute. This option can also be overridden/configured in a dashboard panel under data source options. It’s important to note that this value needs to be formatted as a number followed by a valid time identifier, e.g. 1m (1 minute) or 30s (30 seconds). The following time identifiers are supported:

Identifier	Description
y	year
M	month
w	week
d	day
h	hour
m	minute
s	second
ms	millisecond

```


https://grafana.com/blog/2023/07/07/how-to-visualize-time-series-from-sql-databases-with-grafana/

```
SELECT
$__timeGroupAlias(payment_date, 1h),
sum(amount) AS "amount"
FROM payment
WHERE
$__timeFilter(payment_date)
GROUP BY 1
ORDER BY $__timeGroup(payment_date, 1h)
```

 Query Inspector in the top right. This shows us the full expansion of the SQL query,

### Plotly extension for graphana

https://github.com/NatelEnergy/grafana-plotly-panel

https://corpglory.com/s/timescaledb-grafana-plotly-time-series-analysis/

https://grafana.com/grafana/plugins/ae3e-plotly-panel/


###  grafonnet - библиотека для написания дашбордов Grafana с помощью кода на языке jsonnet

https://habr.com/ru/company/mailru/blog/577230/

### Install Grafana  on Mac:
https://grafana.com/docs/grafana/latest/installation/mac/

https://grafana.com/docs/grafana/latest/getting-started/getting-started/

brew install grafana

To have launchd start Grafana now and restart at login:
```
brew services start grafana
```   
Or, if you don't want/need a background service you can just run:
```
  grafana-server --config=/usr/local/etc/grafana/grafana.ini --homepath /usr/local/share/grafana --packaging=brew cfg:default.paths.logs=/usr/local/var/log/grafana cfg:default.paths.data=/usr/local/var/lib/grafana cfg:default.paths.plugins=/usr/local/var/lib/grafana/plugins
```
http://localhost:3000/

Connecting to Prometeus: https://prometheus.io/docs/visualization/grafana/

## Prometheus

https://blog.pvincent.io/tags/prometheus/


https://habr.com/ru/company/timeweb/blog/562378/  PromQL

### Metric 
Metric is an identifier linking data points together over time. 
For example, the metric `http_requests_total` denotes all the data points collected by Prometheus 
for services exposing http requests counters
 
### Labels 

Labels are key-value pairs associated with time series that, in addition to the metric name, 
uniquely identify them.  

As there is likely to be multiple services exposing the same http_requests_total metric, 
labels can be added to each data point to specify which service this counter applies to:
```
# Request counter for the User Directory service
http_requests_total{service="users-directory"}

# Request counter for the Billing History Service
http_requests_total{service="billing-history"}

# Overall request counter regardless of service
sum(http_requests_total) 
```
### Install Prometheus
```
brew install prometheus
```
When run from `brew services`, `prometheus` is run from
`prometheus_brew_services` and uses the flags in:
   /usr/local/etc/prometheus.args

To have launchd start prometheus now and restart at login:
```
  brew services start prometheus
```  
Or, if you don't want/need a background service you can just run:
```
  prometheus --config.file=/usr/local/etc/prometheus.yml
```  


https://prometheus.io/docs/introduction/first_steps/

https://prometheus.io/download/

Node_exporter

https://github.com/prometheus/node_exporter/blob/master/README.md
```
  ./prometheus --config.file=prometheus.yml
  http://localhost:9090
  http://localhost:9090/metrics
  http://localhost:9090/graph
```

https://coralogix.com/blog/promql-tutorial-5-tricks-to-become-a-prometheus-god/

https://blog.pvincent.io/2017/12/prometheus-blog-series-part-1-metrics-and-labels/

### Show all available metrics:

Show all available metrics:

```
localhost:9090/api/v1/label/__name__/values
```
Data for the  specific metric name:

https://utils.us-east-1.mbedcloud.com/prometheus/api/v1/query?query=update_service_publisher_metrics


### VictoriaMetrics

<https://habr.com/ru/post/494034/>

<https://medium.com/@teebr/iot-with-an-esp32-influxdb-and-grafana-54abc9575fb2>>


<https://habr.com/ru/post/448676/>

<https://news.ycombinator.com/item?id=21343521>

<https://itnext.io/javascript-real-time-visualization-of-high-frequency-streams-d6533c774794>

<https://medium.com/@xaviergeerinck/building-a-real-time-streaming-dashboard-with-spark-grafana-chronograf-and-influxdb-e262b68087de>

https://github.com/creativetimofficial/material-dashboard

<https://grafana.com/docs/reference/templating/#the-timefilter-or-timefilter-variable>

https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019

https://habr.com/ru/post/482272/

 

<https://grafana.com/docs/reference/templating/#the-timefilter-or-timefilter-variable>

WHERE $__timeFilter  

<https://youtu.be/FhNUrueWwOk?list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2> . Variables in Grafana

<https://grafana.com/docs/reference/templating/>

<https://kb.groundworkopensource.com/display/DOC721/How+to+GroundWork+Grafana+dashboard+variables>

The templating feature allows you to create variables that can be used in your metric queries, series names and panel titles. Use this feature to create generic dashboards that can quickly be changed to show graphs for different servers or metrics.

https://github.com/ricardbejarano/graphql_exporter

http://localhost:3000/

http://localhost:3000/datasources

http://ec2-18-221-216-253.us-east-2.compute.amazonaws.com:3000/login . admin/admin1

<https://grafana.com/plugins/postgres>

http://docs.grafana.org/features/datasources/postgres/

https://grafana.com/blog/2018/10/15/make-time-series-exploration-easier-with-the-postgresql/timescaledb-query-editor/

https://stackoverflow.com/questions/48512014/using-postgres-with-grafana

https://habr.com/ru/company/1cloud/blog/443006/

https://www.youtube.com/watch?v=sKNZMtoSHN4&index=7&list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2


https://www.youtube.com/watch?v=sKNZMtoSHN4&index=7&list=PLDGkOdUX1Ujo3wHw9-z5Vo12YLqXRjzg2


## Prometheus - for system monitoring 


https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019

https://habr.com/ru/post/482272/

https://github.com/danielfm/prometheus-for-developers

https://habr.com/ru/company/southbridge/blog/455290/

 https://habr.com/ru/company/itsumma/blog/350200/
 
В состав Prometheus входят следующие компоненты:
* сервер, который считывает метрики и сохраняет их в темпоральной (time series) базе данных;
* клиентские библиотеки для различных языков программирования (Go, Java, Python, Ruby, ...)
* Pushgateway — компонент для приёма метрик кратковременных процессов;
* PROMDASH — дашборд для метрик;
* инструменты для экспорта данных из сторонних приложений (Statsd, Ganglia, HAProxy и других);
* менеджер уведомлений AlertManager (на текущий момент находится на стадии бета-тестирования);
* клиент командной строки для выполнения запросов к данным.

Большинство из них написаны на Go, а совсем небольшая часть — на Ruby и Java. 

Все компоненты Prometheus взаимодействуют между собой по протоколу HTTP:

Сбор метрик в Prometheus осуществляется с помощью механизма pull. 
Имеется также возможность сбора метрик с помощью механизма push (для этого используется специальный компонент pushgateway, 
который устанавливается отдельно). Это может понадобиться в ситуациях, 
когда сбор метрики с помощью pull по тем или иным причинам невозможен: например, при наблюдении за сервисами, защищёнными фаерволлом. Также механизм push может оказаться полезным при наблюдении за сервисами, 
подключающихся к сети периодически и на непродолжительное время.
 
Prometheus использует pull модель сбора метрик: у него есть список экспортеров и он опрашивает их по HTTP, 
собирая с них список метрик и кладя их к себе в хранилище.


Экспортер — это агент, который занимается сбором метрик непосредственно с сущности 
(сервера в целом, или конкретного приложения), которую надо мониторить. 
У Prometheus богатые возможности для инструментации, поэтому экспортеры есть для большинства популярных приложений, 
и написать свой в случае надобности не представляет особого труда.

https://habr.com/ru/post/345370/
postgres_exporter работает следующим образом: он подключается к PostgreSQL, выполняет запросы к служебным таблицам 
и выставляет результаты в специальном формате с помощью внутреннего HTTP-сервера для забора их Prometheus'ом. 
Важный момент: помимо большого набора дефолтных запросов, можно определить свои и собирать любые данные, 
которые можно получить с помощью SQL, включая какие-нибудь бизнес-метрики. 
 
https://habr.com/ru/company/selectel/blog/275803/
https://habr.com/ru/company/otus/blog/358588/

https://habr.com/ru/post/441136/ .  How to store metrics for a long time
https://habr.com/ru/company/funcorp/blog/445370/


Writing: Скорость накопления данных стремится к стабильной величине: обычно сервисы, которые вы мониторите, 
посылают примерно одинаковое количество метрик, и инфраструктура меняется относительно медленно. 

Integration with Grafana
https://grafana.com/dashboards/7901



https://utcc.utoronto.ca/~cks/space/blog/sysadmin/PrometheusGrafanaSetup-2019
https://habr.com/ru/post/482272/

https://github.com/danielfm/prometheus-for-developers
https://habr.com/ru/company/southbridge/blog/455290/
 
 
http://micrometer.io/ . JVM Application Monitoring
https://habr.com/ru/post/442080/

https://habr.com/ru/post/420633/ . GeoIP plotting (WorldMap)
https://habr.com/ru/post/412897/

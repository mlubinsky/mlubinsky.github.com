https://habr.com/ru/companies/itsumma/articles/912804/ Какие есть альтернативы Prometheus, если для метрик его стало недостаточно


https://stackoverflow.com/questions/74729503/how-to-configure-https-for-grafana-on-windows-server-2022

http://localhost:3000


https://blog.devops.dev/10-must-have-grafana-dashboards-for-devops-engineers-299e9041ab24

https://medium.com/@devlink/grafana-12-just-leveled-up-observability-as-code-and-dashboards-that-think-f6dd76a0dbfa

### Prometheus HTTP API compatible server Python server 
designed to statelessly connect Grafana to almost anything by implementing simple plugins.
https://pages.fscherf.de/prometheus-virtual-metrics/  
https://github.com/fscherf/prometheus-virtual-metrics  

### How to pass date range picker to SQL
If your database uses a DATETIME or DATE format, 
you can convert Grafana's UNIX timestamps using specific SQL functions:
```
WHERE timestamp_column BETWEEN TO_TIMESTAMP($__timeFrom) AND TO_TIMESTAMP($__timeTo)
```
### How to eliminate the date conversion to local time zone: 

On Dashboard -> Settings for  "Time zone" -> Select "Coordinated Universal Time"

On Panel -> Edit -> Panel Options  
Axis -> Time Zone

In dropdown select : Coordinated Universal Time

Ensure PostgreSQL Dates are Stored as DATE or TIMESTAMP WITHOUT TIME ZONE
If your column B is of type TIMESTAMP WITH TIME ZONE, PostgreSQL applies time zone conversions. 
To prevent this, explicitly cast it in your query:

 
SELECT A, B::DATE AS B FROM T;

 or 
 
SELECT A, B::TIMESTAMP WITHOUT TIME ZONE AS B FROM T;
✅ This ensures PostgreSQL does not store or apply unwanted timezone conversions.

4️⃣ Set the Grafana Data Source Time Zone
Open Grafana → Configuration (⚙️) → Data Sources.
Select your PostgreSQL data source.
Find the "Time zone" setting.
Set it to "UTC".
✅ This prevents time conversion at the data source level.

C:\Program Files\GrafanaLabs\grafana\conf\defaults.ini
```
[date_formats]
# For information on what formatting patterns that are supported https://momentjs.com/docs/#/displa$

# Default system date format used in time range picker and other places where full time is displayed
full_date = DD-MM-YYYY HH:mm:ss

# Used by graph and other places where we only show small intervals
interval_second = HH:mm:ss
interval_minute = HH:mm
interval_hour = DD/MM HH:mm
interval_day = DD/MM
interval_month = MM-YYYY
interval_year = YYYY
```
###  Modify  tooltip in Grafana Time Series to display only the month and date
To modify the tooltip in a Grafana Time Series panel to display only the month and date (without hours, minutes, and seconds), 
Grafana itself does not provide a direct built-in option to customize the tooltip date format granularly through the UI as of the latest versions. 
However, you can achieve this by adjusting how your data is queried or processed before it reaches the visualization.
```
SELECT DATE_FORMAT(time_column, '%Y-%m-%d') AS time, value_column
FROM your_table
WHERE $__timeFilter(time_column)
```


### Using variables is SQL

#### single choice:
```
SELECT * 
FROM your_table
WHERE column_name =
CASE
    WHEN '$X' = 'ALL' THEN column_name
    ELSE '$X'
END;
```
#### Multiple choise:
```
SELECT * 
FROM your_table
WHERE column_name IN ($X);

SELECT * FROM your_table
WHERE ($X = 'all' OR your_column IN ($X));
```
### SQL example
```
WITH A as (
SELECT "Test" as test, "Criteria" as criteria, 
avg(val) as val,  -- may be max() for some criteria 
avg(score) as score, 
is_ref 
-- CASE    WHEN is_ref THEN 'REF' ELSE 'DUT' END as is_ref   
--, build,
FROM kpi_score  
WHERE date='$date' -- '2025-02-20'
and 
GROUP BY  test, criteria, is_ref 
-- , build
)
,
B as (
SELECT test, 'Average' as criteria, 
cast ( null as double precision) as val,  
avg(score) as score, 
is_ref 
--, build,build in ($build)
FROM A
group by test, is_ref
)
,
C as (
select * from A 
union
select * from B
)
--select * from C order by test, criteria DESC -- to keep Average at the bottom of group
SELECT 
    test as "Test",
    criteria as "Criteria",
    MAX(CASE WHEN is_ref   THEN val END) AS "REF_val",
    MAX(CASE WHEN is_ref   THEN score END) AS "REF_score",
    MAX(CASE WHEN not is_ref THEN val END) AS "DUT_val",
    MAX(CASE WHEN not is_ref THEN score END) AS "DUT_score"

FROM C
GROUP BY test, criteria
ORDER BY test, criteria DESC;

```
### Config
```
The default settings for a Grafana instance are stored in the $WORKING_DIR/conf/defaults.ini file. 
Do not change this file.

Depending on your OS, your custom configuration file is either the
$WORKING_DIR/conf/custom.ini file or the
/usr/local/etc/grafana/grafana.ini file.

The custom configuration file path can be overridden using the --config parameter.

Default Behavior When Uninstalling Grafana on Windows
Dashboards Stored in the Database:

By default, Grafana stores dashboards and settings in its database:
SQLite (grafana.db) – located in the data folder of the installation directory.
MySQL or PostgreSQL – if configured to use an external database.
Uninstalling Grafana does not delete the database file or external databases unless you explicitly delete them.

Dashboards Stored as JSON Files:

If you exported or saved your dashboards as JSON files, those files remain unaffected by uninstalling Grafana.
Configuration and Plugins:

The conf, data, and plugins folders may also remain on your system after uninstallation. 
However, some uninstallers offer an option to delete these directories, which could erase your data.
How to Prevent Dashboard Loss

To ensure your dashboards and other data are preserved:

Back Up Important Files:

Database: If using SQLite, back up the grafana.db file (located in the data folder of your installation directory).
Configuration: Back up grafana.ini (in the conf folder) if you’ve made custom changes.
Plugins: If you installed plugins, back up the plugins folder.

Use an External Database:

If you configured Grafana to use MySQL or PostgreSQL,
the dashboards and settings are stored in the external database and will remain intact after uninstalling Grafana.
Reinstalling Grafana After Uninstallation

If you uninstall Grafana and reinstall it later:

Place the backed-up grafana.db file or connect to your existing external database during setup.
Grafana will automatically detect and load your saved dashboards.

Summary
Uninstalling Grafana 10 does not automatically delete your dashboards unless you manually delete the database or the data folder.
To be safe, back up the data folder (or your external database) before uninstalling.

```
https://grafana.com/docs/grafana/latest/setup-grafana/configure-grafana/

Grafana's default login credentials are username: "admin" and password: "admin"

### Hide date-range selector

```
In Grafana, the date range selector is part of the top navigation bar and is enabled by default.
However, you can hide it by adjusting the dashboard settings.

How to Hide the Date Range Selector in Grafana

Option 1: Use "Time Range Controls" in Dashboard Settings
Open your Grafana Dashboard.
Click the gear icon (⚙️) → "Settings".
Scroll down to the "Time range controls" section.
Disable the toggle "Show time picker".
Click "Save".
🚀 Result: The date range selector will no longer be visible in the UI.
```

## Grafana's Time series panel uses the dashboard's time range 
(from the date/time picker  or default dashboard settings) to define the x-axis, 
not the data returned from the SQL query.   
So, even if your query returns a small date range, the time series plot will still show the full dashboard time range !!!

### Grok
To make the Grafana Time Series panel's X-axis date range dynamically adjust based on the SQL query results (i.e., the date column from your SELECT date, val FROM T query), you need to ensure Grafana recognizes the query output as a proper time series and that the dashboard's time range is configured to adapt to the data. Since you've removed the date range selector from the dashboard, you'll need to rely on Grafana's ability to infer the time range from the query results or use a workaround to set the time range dynamically.

Here’s how you can achieve this:

If the X-axis is rendering correctly with DATE (e.g., assuming midnight for each date), you may not need to cast, but casting is recommended for reliability and to avoid edge cases.

How to Cast the DATE Column
You can modify your SQL query to cast the DATE column to a TIMESTAMP or UNIX timestamp. Here are two approaches:

#### Option 1: Cast to TIMESTAMP
Convert the DATE column to a TIMESTAMP by adding a time component (e.g., midnight). This is the most straightforward approach and works well with Grafana’s time series format.
```sql
SELECT date::TIMESTAMP AS time, val
FROM T
ORDER BY date ASC;
```

date::TIMESTAMP: Converts the DATE to a TIMESTAMP 
(e.g., 2023-01-01 becomes 2023-01-01 00:00:00).
Alias time: Grafana recognizes the time alias as the X-axis time column.
Why it works: Grafana natively supports TIMESTAMP for time series, 
and this ensures the X-axis reflects the date range of your data.

Alternative Syntax: If you prefer using CAST, you can write:

```sql
SELECT CAST(date AS TIMESTAMP) AS time, val
FROM T
ORDER BY date ASC;
```

####  Option 2: Convert to UNIX Timestamp

Convert the DATE column to a UNIX timestamp (in seconds or milliseconds), which Grafana also supports.

`SELECT EXTRACT(EPOCH FROM date) * 1000 AS time, val FROM T ORDER BY date ASC;`

-   **EXTRACT(EPOCH FROM date)**: Returns the UNIX timestamp in seconds (e.g., 1672531200 for 2023-01-01 00:00:00).
-   **\* 1000**: Converts seconds to milliseconds (e.g., 1672531200000), which Grafana prefers for higher precision.
-   **Alias time**: Ensures Grafana uses this column for the X-axis.

#### Option 3: Add Explicit Time Component

If you want to be explicit about the time (e.g., always midnight), you can use:


`SELECT (date || ' 00:00:00')::TIMESTAMP AS time, val FROM T ORDER BY date ASC;`

-   **date || ' 00:00:00'**: Concatenates the date with a 00:00:00 time to form a string like 2023-01-01 00:00:00.
-   **::TIMESTAMP**: Converts the string to a TIMESTAMP.

### Additional Steps

1.  **Set Query Format**:
    -   In the Grafana query editor, ensure the **Format** is set to **Time Series** (not Table). This tells Grafana to treat the time column as the X-axis and val as the Y-axis.
2.  **Verify Data in Query Inspector**:
    -   Use the **Query Inspector** in Grafana’s query editor to check the data returned by your query. Ensure:
        -   The time column contains values like 2023-01-01 00:00:00 (for TIMESTAMP) or 1672531200000 (for UNIX timestamp).
        -   The val column contains numeric values (e.g., INTEGER, FLOAT).
3.  **Check X-Axis Range**:
    -   After casting, the X-axis should reflect the range of dates in your query results. If it’s still fixed, ensure the dashboard time range isn’t overriding the panel’s range (see below).
4.  **Handle Dashboard Time Range**:
    -   Since you’ve removed the date range selector, Grafana may use a default time range (e.g., last 24 hours). To make the X-axis fully dynamic:
        -   Use a dashboard variable to query the min/max dates:
            
            sql
            
            Copy
            
            `SELECT EXTRACT(EPOCH FROM MIN(date)) * 1000 AS __value, EXTRACT(EPOCH FROM MAX(date)) * 1000 AS __text FROM T;`
            
        -   Manually set the dashboard URL with ?from=$variable&to=$variable (as described in the previous response).
        -   Alternatively, use the Grafana API to set the time range dynamically.

### Testing Without Casting

If you want to test whether DATE works without casting:

-   Run your original query:
    
 
    
    `SELECT date, val FROM T ORDER BY date ASC;`
    
-   Check the Query Inspector to see if Grafana interprets date as a valid time (e.g., 2023-01-01 00:00:00).
-   If the X-axis range is incorrect or fixed, this confirms that casting to TIMESTAMP or UNIX timestamp is necessary.

### Recommendation

For reliability and compatibility with Grafana’s Time Series panel, **cast the DATE column to TIMESTAMP** using:



`SELECT date::TIMESTAMP AS time, val FROM T ORDER BY date ASC;`




### 1\. **Ensure Proper Time Series Format**

Grafana requires time series data to have a column representing time (in a format it can parse, such as a SQL DATETIME or UNIX timestamp) and a numeric value. Your query SELECT date, val FROM T should meet these requirements:

-   **Column date**: Ensure this is a SQL DATETIME, TIMESTAMP, or UNIX timestamp (in seconds or milliseconds). If it’s a string or another format, Grafana may not interpret it correctly.
-   **Column val**: Ensure this is a numeric value (e.g., INTEGER, FLOAT, or DECIMAL).

**Action**:

-   Verify the data type of the date column in your database. For example, in MySQL, you can check with:
    
    `DESCRIBE T;`
    
-   If date is not a DATETIME or TIMESTAMP, convert it in your query. For example, if date is a string like 2023-01-01, use:
    
    `SELECT STR_TO_DATE(date, '%Y-%m-%d') AS time, val FROM T;`
    
-   If date is a UNIX timestamp, ensure it’s in a format Grafana understands (e.g., milliseconds). If it’s in seconds, convert it:
    
    `SELECT FROM_UNIXTIME(date) AS time, val FROM T;`
    
-   Ensure val is numeric. If it’s stored as a string, cast it:
    
    `SELECT date AS time, CAST(val AS DECIMAL) AS value FROM T;`
    

In the Grafana query editor, set the **Format** to **Time Series** (not Table) to ensure Grafana interprets the data correctly.

### 2\. **Dynamically Set Dashboard Time Range Based on Query Results**

Since you’ve removed the date range selector, Grafana’s default behavior is to use a fixed or last-selected time range for the dashboard. To make the X-axis reflect the date range of your SQL query results, you need to dynamically set the dashboard or panel time range based on the minimum and maximum values of the date column in your query.

Unfortunately, Grafana does not natively support automatically setting the dashboard time range to the exact range of query results without the time picker. However, you can use one of the following workarounds:

#### **Option A: Use a Hidden Dashboard Variable to Set Time Range**

You can create a dashboard variable that queries the minimum and maximum dates from your table and use it to set the dashboard’s time range programmatically.

**Steps**:

1.  **Create a Dashboard Variable**:
    -   Go to **Dashboard Settings** (gear icon) > **Variables** > **Add Variable**.
    -   Set the following:
        -   **Name**: time\_range (or similar).
        -   **Type**: Query.
        -   **Data Source**: Your SQL data source.
        -   **Query**:

            
 `SELECT UNIX_TIMESTAMP(MIN(date)) * 1000 AS __value, UNIX_TIMESTAMP(MAX(date)) * 1000 AS __text FROM T`
            
            This query returns the min and max dates as UNIX timestamps in milliseconds (required by Grafana for time ranges).
        -   **Refresh**: Set to On Dashboard Load to ensure it updates when the dashboard loads.
        -   **Hide**: Set to Hide so the variable doesn’t appear on the dashboard.
    -   Save the variable.
2.  **Set Dashboard Time Range Using the Variable**:
    -   Grafana doesn’t directly allow variables to set the dashboard time range in the UI, but you can use a URL parameter or a script to apply the time range.
    -   Modify the dashboard URL to include the time range based on the variable:
        -   Query the min and max dates in your SQL database to get the values.
        -   Append to the dashboard URL:
            
            
      `?from=<min_date_in_ms>&to=<max_date_in_ms>`
            
            For example, if your min date is 2023-01-01 00:00:00 (UNIX timestamp 1672531200000 in ms) and max date is 2023-12-31 23:59:59 (UNIX timestamp 1704067199000 in ms), use:
            
 
            
            `http://your-grafana-url/d/your-dashboard?from=1672531200000&to=1704067199000`
            
    -   Alternatively, use a Grafana API or script to set the time range dynamically (see Option C below).
3.  **Update the Panel Query**:
    -   Ensure your panel query uses the dashboard time range:
 
        
        `SELECT date AS time, val FROM T WHERE $__timeFilter(date);`
        
        The $\_\_timeFilter macro ensures the query respects the dashboard’s time range, though it’s less critical if your data already spans the desired range.

#### **Option B: Use Panel Time Range Override**

You can override the time range for the specific Time Series panel to match the data range of your query results.

**Steps**:

1.  **Edit the Panel**:
    -   Open the Time Series panel in the dashboard.
    -   Go to the **Query** tab.
2.  **Use a Relative Time Override**:
    -   In the **Query Options** section, enable **Relative Time** or **Time Shift**.
    -   This approach is manual and requires you to know the approximate range of your data. For example, set a relative time range like from now-2y to now if your data spans two years.
    -   This is less dynamic and requires updating if your data range changes.
3.  **Alternative: Use a Transformation**:
    -   If you want the panel to visually reflect only the data range, you can use a Grafana transformation to filter data within the min/max dates:
        -   Go to the **Transform** tab in the panel editor.
        -   Add a **Filter by name** or **Filter data by query** transformation to ensure only the relevant time range is displayed.
        -   However, this doesn’t adjust the X-axis range itself, just the data points shown.

#### **Option C: Use Grafana API to Set Time Range**

For a fully automated solution, you can use the Grafana HTTP API to update the dashboard’s time range based on the query results. This requires scripting outside of Grafana.

**Steps**:

1.  **Query Min/Max Dates**:
    -   Write a script (e.g., in Python) to query your SQL database for the min and max dates:
        
        `SELECT MIN(date), MAX(date) FROM T;`
        
    -   Convert these to UNIX timestamps in milliseconds.
2.  **Update Dashboard Time Range**:
    -   Use the Grafana API to update the dashboard’s time range. Send a request to the Grafana API endpoint for updating dashboard settings, specifying the time field:
        
        
        `curl -X POST \ -H "Authorization: Bearer <your-api-key>" \ -H "Content-Type: application/json" \ -d '{"time":{"from":"2023-01-01T00:00:00.000Z","to":"2023-12-31T23:59:59.999Z"}}' \ http://your-grafana-url/api/dashboards/db/your-dashboard`
        
    -   Replace <your-api-key> with a valid Grafana API key and adjust the URL and dashboard ID.
3.  **Automate**:
    -   Schedule the script to run periodically (e.g., using a cron job) to keep the time range updated as new data is added.

### 3\. **Verify X-Axis Configuration**

Ensure the Time Series panel’s X-axis is configured to display the time range correctly:

-   Go to the **Panel** tab in the panel editor.
-   Under **Axis** > **X-Axis**, ensure:
    -   **Mode** is set to Time (default for time series).
    -   **Show** is enabled to display the X-axis labels.
    -   **Label** is optional but can be set to something like Date for clarity.
-   Under **Standard Options**, ensure the **Unit** for the X-axis is set to a time format (e.g., Date Time).

### 4\. **Debugging Tips**

If the X-axis still shows a fixed date range:

-   **Check Query Results**:
    -   Use the **Query Inspector** in the Grafana query editor to verify the data returned by your query. Ensure the time column contains valid timestamps and the data spans the expected range.
-   **Check Dashboard Time Range**:
    -   Even without the time picker, the dashboard may have a default time range (e.g., last 24 hours). Check the dashboard settings or URL parameters (from and to) to confirm.
-   **Test with Time Picker**:
    -   Temporarily re-enable the time picker to test if manually setting the range to the min/max of your data works. This can help diagnose if the issue is with the data or the dashboard configuration.
-   **Clear Cache**:
    -   If your SQL data source has caching enabled, clear the cache or set the **Cache Timeout** to a low value in the query options to ensure fresh data is used.

### 5\. **Example Query**

Here’s an example of a complete query that should work with a MySQL/PostgreSQL data source:

`SELECT date AS time, val AS value FROM T WHERE $__timeFilter(date) ORDER BY date ASC;`

-   **Alias time**: Grafana expects a column named time for the X-axis.
-   **Alias value**: The numeric column should be aliased to a meaningful name.
-   **$\_\_timeFilter**: This macro ensures compatibility with any dashboard time range, though it’s optional if you’re setting the range dynamically.
-   **Order by time**: Ensures data points are plotted in chronological order.

### 6\. **Limitations**

-   Grafana Ascending without the time picker, Grafana’s dashboard time range cannot be directly set to the query result range in the UI. You must use variables, URL parameters, or the API as described.
-   If your data range changes frequently (e.g., new data is appended), you’ll need to refresh the variable or update the API call to reflect the new range.
-   For non-time-series data (e.g., if date is not a proper timestamp), you may need to preprocess the data or use a different visualization (e.g., Bar Chart with X-axis as a non-time field).[
    
    ![](https://imgs.search.brave.com/IY5wVtB6VKwwSg7YDkUyFtQtc2_JxBCDWSDVqrU85qI/rs:fit:64:0:0:0/g:ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvNWU3Zjg0ZjA1/YjQ3ZTlkNjQ1ODA1/MjAwODhiNjhjYWU0/OTc4MjM4ZDJlMTBi/ODExYmNiNTkzMjdh/YjM3MGExMS9zdGFj/a292ZXJmbG93LmNv/bS8)
    
    ](https://stackoverflow.com/questions/64669533/grafana-show-non-datatime-date-time-field-on-x-axis)

### 7\. **Recommended Solution**

The most practical solution is **Option A (Hidden Dashboard Variable)** combined with a URL parameter to set the time range. This approach is relatively simple, works within Grafana’s UI, and can be refreshed on dashboard load. For example:

-   Variable query:
        
    `SELECT UNIX_TIMESTAMP(MIN(date)) * 1000 AS __value, UNIX_TIMESTAMP(MAX(date)) * 1000 AS __text FROM T`
    
-   Manually set the dashboard URL:
    
    
    `?from=$time_range&to=$time_range`
    
-   Panel query:
    
    
    `SELECT date AS time, val AS value FROM T ORDER BY date ASC;`
    

If you need a fully automated solution and have scripting capabilities, **Option C (Grafana API)** is more robust but requires external setup.

### Sources

-   Grafana Documentation: Time Series[
    
    ![](https://imgs.search.brave.com/eHO3EVegIIx7TwFbGpV7TD-vUQ8uYSE4kBCnKrwHcvw/rs:fit:64:0:0:0/g:ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvYTU2NWYwNDU1/ZjJlZWQxY2M4ZGQ2/YWUwMTM3NDg0Y2Ey/ODJmMDZkMDU1NWNj/OTZiOTg3NDQ3Y2Yz/NjRkMmQ2Yi9ncmFm/YW5hLmNvbS8)
    
    ](https://grafana.com/docs/grafana/latest/panels-visualizations/visualizations/time-series/)
-   Grafana Community Forums: Set Time Range To Query Results[
    
    ![](https://imgs.search.brave.com/8nJ955Ew6IjsckilHpnmFY11fwqY4Qvck1IudUJ-tlc/rs:fit:64:0:0:0/g:ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvZTM4MDVmNDBl/ODU2NjJlMjdkMTE3/OTM5MjUwNmI2YmRj/MDBiNWM0OGFlZTFh/ODMwOGIxOTY0YzM1/OGY0MDE3MC9jb21t/dW5pdHkuZ3JhZmFu/YS5jb20v)
    
    ](https://community.grafana.com/t/set-time-range-to-query-results/61062)
-   Grafana Documentation: MySQL Data Source[
    
    ![](https://imgs.search.brave.com/eHO3EVegIIx7TwFbGpV7TD-vUQ8uYSE4kBCnKrwHcvw/rs:fit:64:0:0:0/g:ce/aHR0cDovL2Zhdmlj/b25zLnNlYXJjaC5i/cmF2ZS5jb20vaWNv/bnMvYTU2NWYwNDU1/ZjJlZWQxY2M4ZGQ2/YWUwMTM3NDg0Y2Ey/ODJmMDZkMDU1NWNj/OTZiOTg3NDQ3Y2Yz/NjRkMmQ2Yi9ncmFm/YW5hLmNvbS8)
    
    ](https://grafana.com/docs/grafana/latest/datasources/mysql/)
-   Grafana Documentation: Query and Transform Data


### Gemini
To make the X-axis date range in your Time Series panel adapt to the actual dates returned by your SQL query, you'll need to configure the panel specifically. Here's how you can achieve this:

1.  **Edit the Time Series Panel:** Click on the title of your Time Series panel to open the panel editor.
    
2.  **Navigate to the "Axes" Tab:** In the panel editor, look for a tab labeled "Axes." Click on it.
    
3.  **Configure the Time Axis:** Within the "Axes" tab, you'll find settings related to both the X (Time) and Y axes. Focus on the X-axis settings.
    
4.  **Set "Mode" to "Auto":** You should see an option labeled "Mode" for the X-axis. Ensure this is set to **"Auto"**. When set to "Auto," Grafana will attempt to automatically determine the appropriate time range based on the data it receives.
    
5.  **Consider "Soft Min" and "Soft Max" (Optional but Recommended):** While "Auto" often works well, you might want to provide Grafana with hints about the expected minimum and maximum time values. Look for fields like "Soft min" and "Soft max" under the X-axis settings. You can set these to `$__timeFrom()` and `$__timeTo()` respectively. Even though you've removed the dashboard selector, these variables can sometimes still be used within the panel context to influence the automatic range calculation based on the data.
    
6.  **Save and Apply:** Once you've made these changes, click the "Save" button at the top of the panel editor and then "Apply" to see the changes on your dashboard.
    

**Explanation:**

By setting the X-axis "Mode" to "Auto," you're telling Grafana to look at the timestamps present in the data returned by your SQL query and automatically adjust the start and end points of the X-axis accordingly.




### ChatGPT
### **Use a Transformation to limit the x-axis**

If your SQL query returns only the data you're interested in (e.g., a small time window), and you don't want Grafana to force the axis to a broader time range, then:

1.  Go to the **"Transform"** tab in the panel.
    
2.  Add a **"Convert field type"** or **"Organize fields"** transform to ensure `date` is treated as a `time` field.
    
3.  Then add a **"Time series" transformation** if needed.
    
4.  Grafana should now auto-adjust the x-axis to just the returned data range.
    

* * *

### ✅ **Alternative Hack: Use a "Stat" or "Table" panel**

If you're only returning a small fixed set of time-based data, and dynamic time navigation isn't necessary:

-   Consider using the **Table** or **Bar chart** panel instead of Time series.
    
-   These don’t stretch the x-axis based on the dashboard’s time range.
    

* * *

### ✅ Summary

To make the x-axis of a Grafana **Time Series** panel match the SQL data returned:

-   Either **enable the time picker** and use `WHERE $__timeFilter(date)` in your SQL, or
    
-   **Set a custom relative time** in the panel query options, or
    
-   **Use transformations** to ensure Grafana treats your `date` field as a true time field and scales the axis accordingly.





### Grafana + Jira integration

https://grafana.com/docs/grafana/latest/setup-grafana/configure-security/configure-authentication/generic-oauth 

```

http://localhost:3000/connections/datasources/new - add Jira as datasource: No valid Grafana Enterprise license detected.


1. Verify Jira OAuth 2.0 Support

Check Jira Version: Ensure your Jira version supports OAuth 2.0.
Jira Documentation: Refer to the official Jira documentation for specific instructions on enabling and configuring OAuth 2.0.

2. Create a Jira Application

Jira Administration: Access Jira's administration panel.   
Create Application: Create a new application within Jira specifically for Grafana.
This process will generate a Client ID and Client Secret.
Carefully store these credentials securely.

3. Configure Grafana for OAuth 2.0

Access Grafana: Log in to your Grafana instance as an administrator.
Navigate to Authentication: Go to Configuration > Data Sources > Authentication.
Select "Generic OAuth 2.0": Choose the "Generic OAuth 2.0" option.
Fill in the Form:

   Name: Give your configuration a descriptive name (e.g., "Jira OAuth").
   Enabled: Toggle the "Enabled" switch to "On."
   Client ID: Enter the Client ID obtained from Jira.
   Client Secret: Enter the Client Secret obtained from Jira.
   Authorization Endpoint: The URL for Jira's OAuth 2.0 authorization endpoint (usually something like 
      https://<your_jira_domain>/plugins/servlet/oauth/authorize).
   Token Endpoint: The URL for Jira's OAuth 2.0 token endpoint (usually something like 
         https://<your_jira_domain>/plugins/servlet/oauth/accessToken).
   Scopes (optional): If Jira requires specific scopes for the application, enter them here.
    Allowed Domains (optional): If you want to restrict logins to specific domains, enter them here.

Save the Configuration: Click "Save" to apply the changes.

4. Test the Integration

Log Out and Log In: Log out of Grafana and try logging in again.
Jira Authorization: You should be redirected to the Jira authorization page.
Grant Permissions: Grant the necessary permissions to the Grafana application.
Return to Grafana: You should be redirected back to Grafana and successfully logged in.

```




### How to configure Grafana to accept my Jira credentials?
```
I am using Grafana. Also I am using Jira.
Grafana login page asks for user and password.
I know HTTP end point for Jira login.

ChatGPT said:
 
To configure Grafana to accept your Jira credentials, you can use Jira as an authentication provider for Grafana
via Generic OAuth2 or HTTP-based authentication.

Here's how you can set it up using the Jira login HTTP endpoint:

Steps to Configure Grafana for Jira Authentication:

Enable OAuth2 in Grafana Configuration:
------------------------------------------------
Open Grafana's configuration file (grafana.ini).

Navigate to the [auth.generic_oauth] section.

Add the following configuration details:

[auth.generic_oauth]
enabled = true
name = Jira
allow_sign_up = true
client_id = <your_client_id>
client_secret = <your_client_secret>
auth_url = <jira_auth_endpoint>
token_url = <jira_token_endpoint>
api_url = <jira_user_info_endpoint>
scopes = openid profile email

Replace the <jira_auth_endpoint>, <jira_token_endpoint>, and <jira_user_info_endpoint> with the corresponding Jira OAuth2 endpoints.

Set Up OAuth2 App in Jira:
--------------------------
Log in to Jira as an admin.
Navigate to the OAuth2 settings in your Jira admin panel.
Create a new OAuth2 application:
Provide a name.
Specify the redirect URL as http://<grafana-url>/login/generic_oauth.
Jira will generate a Client ID and Client Secret. Copy these and use them in the grafana.ini file.
Restart Grafana:

Save your changes in grafana.ini.
Restart the Grafana service:

 
sudo systemctl restart grafana-server
Test the Configuration:

Open the Grafana login page.
----------------------------------
You should now see the "Sign in with Jira" option.
Clicking it will redirect you to Jira for authentication.
Once authenticated, you will be redirected back to Grafana.

Troubleshoot:

If there are issues, check the Grafana server logs (/var/log/grafana/grafana.log) for errors.

```

https://jira.readthedocs.io/
https://pypi.org/project/jira/

```
import jira
from jira import exceptions
#---------------------------------
def jiraLogin(username, password):
#----------------------------------
    input = {"jira_host": "http://105.128.81.140:8080", "jira_user": "{}".format(username),"jira_password": "{}".format(password)}
    jira_host_url = input["jira_host"]
    try:
          jiraRes = jira.JIRA(server=jira_host_url, basic_auth=(input["jira_user"], input["jira_password"]), max_retries=0)
    except exceptions.JIRAError as e:
        output["jira_operation_success"] = False
        output["exception_type"] = "JIRAError"
        output["failure_exception_url"] = str(e.url)
        output["failure_exception_sent_headers"] = str(e.response.request.headers)
        output["failure_exception_response_headers"] = str(e.response.headers)
    except Exception as e:
        output["jira_operation_success"] = False
        output["exception_type"] = "Exception"
        output["failure_exception"] = str(e)
    if jiraRes:
        print("Jira login successful.")
        return jiraRes.user(input["jira_user"]).emailAddress
    else:
        return ""
#---------------------------------------
def loginhandler(user, directory=None):
#---------------------------------------
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        directory = request.form['scanresultdirectory']
        ssi = 'ssi' in request.form and request.form['ssi'] == 'on'
        if ssi:
            try:
                user = jiraLogin(username, password)

```



https://habr.com/ru/articles/857258/  Вышла Grafana 11.3

https://community.grafana.com/t/how-to-add-extra-info-in-tooltips-on-grafana-time-series-dashboard-based-on-sql/114297

https://grafana.com/go/webinar/building-advanced-grafana-dashboards/

Wednesday, February 21, 2024 09:30 PST

https://grafana.com/files/building-advanced-grafana-dashboards.pdf?pg=webinar-building-advanced-grafana-dashboards&plcmt=related-content-2

https://www.reddit.com/r/grafana/comments/jpnbhb/grafana_best_practices_and_advanced_techniques/

https://github.com/FlxPeters/awsome-grafana

https://grafana.com/blog/2022/06/06/grafana-dashboards-a-complete-guide-to-all-the-different-types-you-can-build/

https://www.metricfire.com/blog/grafana-dashboards-from-basic-to-advanced/

https://logit.io/blog/post/top-grafana-dashboards-and-visualisations/

https://habr.com/ru/articles/803527/

### AWS CloudWatch  
https://aws.plainenglish.io/observability-in-aws-cloudwatch-ed60a2c4fdcd

### Clickhouse + Grafana

https://habr.com/ru/companies/ozontech/articles/774712/


### Export Grafana result to file
CharGPT suggests
 
#### Exporting Dashboards and Panels as Images

##### Export as PNG:
```
Open the Grafana dashboard.
Click on the panel title to open the panel menu.
Select "Share" from the panel menu.
In the "Share" panel, go to the "Direct link rendered image" tab.
Click on the "Render" button to generate a PNG image of the panel.
Save the rendered image to your local file system.
```
##### Export as PDF:
```
Open the Grafana dashboard.
Click on the dashboard title to open the dashboard menu.
Select "Share dashboard" from the dashboard menu.
In the "Share" panel, go to the "Export" tab.
Choose "Export to PDF" and follow the prompts to generate and download the PDF file.
```
#### Exporting Data from Tables

##### Export as CSV:
```
Open the Grafana dashboard and navigate to the table panel.
Click on the panel title to open the panel menu.
Select "Inspect" from the panel menu.
In the "Inspect" panel, go to the "Data" tab.
Click on the "Download CSV" button to export the table data as a CSV file.
```
#### Using Plugins and External Tools
```
Grafana Plugins: Some plugins may offer additional export features.
Check the Grafana Plugin catalog for plugins that support enhanced exporting capabilities.
API and Scripting: Advanced users can use Grafana's HTTP API to programmatically export data and visualizations.
This approach requires some scripting knowledge and can be integrated into automated workflows.
 
```
Gemini suggests
```
Grafana allows exporting the data behind the visualizations,
but not the visualizations themselves as images.
Here's how a Grafana user can export the data from your barchart and table to a CSV file:
```
#### For Barchart:
```
1.  The user should hover over the **three-dot menu** in the top right corner of the barchart panel.
2.  Select **Inspect** > **Data**.
3.  This opens a panel on the right side displaying the data in a table format.
4.  Click the blue **Download CSV** button to download the data associated with the barchart.
```
#### For Table:
```
1.  Similar to the barchart, the user can click the **three-dot menu** in the top right corner of the table panel.
2.  Select **Inspect** > **Data**.
3.  This will again display the data in a table format on the right side.
4.  Click the blue **Download CSV** button to download the data from the table.
```
#### Additional Notes:
```
* By default, the downloaded CSV will include all data series in the panel and a timestamp column.
* Users can configure export options within the "Data" tab that appears after selecting "Inspect" > "Data".
 This allows them to:
    * Enable "Apply panel ation" to utilize any ations applied within the panel before export.
    * Choose between "Formatted data" (including labels) or "Raw data" (numerical values).

While this method doesn't provide a direct export of the chart image,
it offers a way for users to obtain the underlying data for further analysis or manipulation outside of Grafana. 
```
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

https://community.grafana.com/t/issue-with-ation-prepare-time-series-multi-frame-time-series/105397

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

Transform: "Grouping to matrix" to make the bar chart where X-axis is not the date
****************************************
 Column: dut
 Row: metric <-- will be X-axis
 Cell value : V

select 'm1' as metric, 'A' as dut, 10 as value
union ALL
select 'm1' as metric, 'B' as dut, 20 as value
union ALL
select 'm2' as metric, 'C' as dut, 30 as value
```

If data is present in following table format (dt, dut, metric1 int, metric2 int, metric3 int)
we need to convert it to format (dut, metric, value) to feed to grafana:

```
select dut, 'm1' as metric, m1  as value from daily 
union all
select dut, 'm2' as metric, m2  as value from daily 



How to build barchart: date, build, group, score
----------------------------------------------
Transformation: Grouping to Matrix
Column: group name
Row: (X-axis)  CONCAT(date, build)
Cell value: (Y-axis) score

Rows in SQL are sorted by CONCAT_WS(n,build)
How I build barchart: 
I am using Grafana's Transformation "Grouping to Matrix"
- Row (x-axis)  shows  CONCAT_WS(' ', n, build)
- Column: group_name
- Cell value: score

The problem is:
I  need all bars with the same n (which are numbers from 1 till 31 in string format)
to be displayed next to each other in the same bin, which is not the case with my solution. 


To group bars with the same n (numbers 1 to 31) next to each other in the same bin on your Grafana bar chart, you need to adjust how the X-axis is defined so that it uses only n for binning, while still displaying the concatenated CONCAT_WS(' ', n, build) as labels or tooltips. The current setup with Grouping to Matrix is treating the concatenated string as the X-axis value, which creates separate bins for each unique n + build combination. Here's how to fix it:

Solution
Modify the SQL Query:

Add n as a separate column in the query output so it can be used for binning.
Keep the concatenated string for display purposes.
Updated SQL query:

sql

Collapse

Wrap

Copy
SELECT
    n,  -- Keep n as a separate column for binning
    build,
    group_name,
    value,
    CONCAT_WS(' ', n, build) AS x
FROM your_table
ORDER BY n, build;
Configure the Bar Chart in Grafana:

Go to the Panel settings in Grafana.
Use the Grouping to Matrix transformation:
Row (X-axis): Set to n (this ensures bars are binned by n, so all bars with the same n are grouped together).
Column: Set to group_name (this creates separate bars for each group within the same n bin).
Cell value: Set to value (this determines the height of the bars).
This setup groups bars by n on the X-axis, placing all bars with the same n next to each other.
Display the Concatenated Label:

To show CONCAT_WS(' ', n, build) in the chart (e.g., as a label or tooltip):
Go to the Field tab > Standard options > Value mappings or Tooltip settings.
Map the x field to display in tooltips or use it in a custom label format if needed.
Alternatively, you can use a Value override to display x as a custom label for each bar, though this depends on your Grafana version.
If you want the X-axis labels to show only n, they’re already set correctly by using n as the row.
Optional: Adjust Bar Chart Settings:

In the Panel settings, go to the Bar chart options:
Enable Show values or Stacking if you want to differentiate bars within the same n bin by group_name.
Adjust Bar width or Group width to ensure bars are visually distinct within each n bin.
If bars are still not grouping as expected, ensure Sort by in the transformation is set to n (ascending).
Set Y-Axis Max (from Your Previous Question):

Since you mentioned wanting a specific Y-axis max, go to Field tab > Standard options > Max and set your desired number (e.g., 100).
Save and Test:

Apply the changes and verify that bars with the same n are now grouped together in the same X-axis bin, with different group_name values displayed as adjacent bars.
Why This Works
By using n as the Row in the matrix transformation, Grafana bins the X-axis by n, ensuring all bars with the same n (e.g., 1) are grouped together.
The group_name as the Column creates separate bars within each n bin, colored differently for clarity.
The x field (CONCAT_WS(' ', n, build)) can still be used for labels or tooltips without affecting the binning.
If It Still Doesn’t Work
Check Data Types: Ensure n is consistently formatted (e.g., no leading zeros or spaces) in the SQL output, as Grafana treats strings literally.
Transformation Order: If you have multiple transformations, ensure Grouping to Matrix is applied after any filtering or sorting transformations.
Debug Data: Use Grafana’s Inspect feature (Panel > Inspect > Data) to verify the transformed data has n as the row key and group_name as columns.
Alternative Approach: If the matrix transformation still causes issues, consider pivoting the data directly in SQL (using CASE or PIVOT if your database supports it) to pre-format the matrix, then use a standard bar chart without transformations.

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

## Grouping to matrix (pivoting) - for Table Pallete

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

```
There is table T with columns :  test, criteria, val, score, build, is_ref
Calculate avg(score) per A / per is_ref / (and per build?):

WITH A as (
SELECT "Test" as test, "Criteria" as criteria, avg(val) as val,  avg(score) as score ,  is_ref  --, build,
FROM kpi_score  GROUP BY  test, criteria, is_ref -- , build
)
,
B as (
SELECT test, 'Average' as criteria, cast ( null as double precision) as val,  avg(score) as score, is_ref --, build,
FROM A
group by test, is_ref
)
,
C as (
select * from A 
union
select * from B
)
select * from C
order by test, criteria DESC

How we have table with columns:
test, criteria, val, score, is_ref, (-- build)
we want to transform it to table

test, criteria,  val_(for_is_ref=TRUE), score_(for_is_ref=TRUE), val_(for_is_ref=FALSE), score_(for_is_ref=FALSE)   -- per build


Apply "Grouping to Matrix" Transformation
After running the query in Grafana, follow these steps:

Go to the "Transform" tab in Grafana.
Click "Add transformation" and select "Grouping to matrix".
Configure it as follows:

Rows: Set to test.

Columns: Set to (build + is_ref) (you may need to combine them using a CONCAT() function in SQL).

Values: Use val and score (aggregated as MAX or SUM).
Grafana will dynamically pivot the build and is_ref columns into separate columns.

When using the "Grouping to Matrix" transformation in Grafana, you need to define how multiple values should be aggregated when they belong to the same test and build combination.

Choosing Aggregation for val and score
Since there can be multiple rows for the same (test, build, is_ref) combination,
Grafana needs a way to merge them into a single value per cell.
This is where you choose an aggregation function (e.g., MAX, SUM, AVG, etc.).

Options for Aggregation:

MAX(val) → Takes the highest value for val per (test, build, is_ref).
SUM(val) → Adds up all val values for (test, build, is_ref).
AVG(val) → Computes the average value.
FIRST(val) or LAST(val) → Takes the first or last encountered value.

Similarly, you can choose the aggregation method for score.


Pure SQL solution, not Grafana (and no build column!!!):

SELECT 
    test,
    criteria,
    MAX(CASE WHEN is_ref = FALSE THEN val END) AS val_false,
    MAX(CASE WHEN is_ref = FALSE THEN score END) AS score_false,
    MAX(CASE WHEN is_ref = TRUE THEN val END) AS val_true,
    MAX(CASE WHEN is_ref = TRUE THEN score END) AS score_true

FROM kpi_score
GROUP BY test, criteria;

Postgres specific implementation using filter
SELECT 
    test,
    criteria,
    MAX(val) FILTER (WHERE is_ref = TRUE) AS val_true,
    MAX(score) FILTER (WHERE is_ref = TRUE) AS score_true,
    MAX(val) FILTER (WHERE is_ref = FALSE) AS val_false,
    MAX(score) FILTER (WHERE is_ref = FALSE) AS score_false
FROM kpi_score
GROUP BY test, criteria;


DO $$
DECLARE
    sql_query TEXT;
BEGIN
    -- Generate dynamic column names for each unique criteria
    SELECT STRING_AGG(
        format(
            'MAX(CASE WHEN criteria = %L AND is_ref = TRUE THEN val END) AS val_true_%I,
             MAX(CASE WHEN criteria = %L AND is_ref = TRUE THEN score END) AS score_true_%I,
             MAX(CASE WHEN criteria = %L AND is_ref = FALSE THEN val END) AS val_false_%I,
             MAX(CASE WHEN criteria = %L AND is_ref = FALSE THEN score END) AS score_false_%I',
            criteria, criteria, criteria, criteria, criteria, criteria, criteria, criteria
        ), ', ')
    INTO sql_query
    FROM (SELECT DISTINCT criteria FROM your_table) sub;

    -- Construct and execute the full query
    sql_query := format(
        'SELECT test, %s FROM your_table GROUP BY test', sql_query
    );

    EXECUTE sql_query;
END $$;


Grafana does not support executing dynamic SQL directly in its query editor,
especially when using PostgreSQL as the data source.
However, you can work around this limitation in one of the following ways:

Option 1: Create a Materialized View in PostgreSQL
-----------------------------------------------------
Since Grafana queries are usually static,
you can store the dynamic pivot as a materialized view and query it from Grafana.

Step 1: Create a Materialized View
--------------------------------------
Modify the PL/pgSQL script to store the results in a materialized view:

DROP MATERIALIZED VIEW IF EXISTS pivoted_table;
DO $$
DECLARE
    sql_query TEXT;
BEGIN
    -- Generate dynamic column names for each unique criteria
    SELECT STRING_AGG(
        format(
            'MAX(CASE WHEN criteria = %L AND is_ref = TRUE THEN val END) AS val_true_%I,
             MAX(CASE WHEN criteria = %L AND is_ref = TRUE THEN score END) AS score_true_%I,
             MAX(CASE WHEN criteria = %L AND is_ref = FALSE THEN val END) AS val_false_%I,
             MAX(CASE WHEN criteria = %L AND is_ref = FALSE THEN score END) AS score_false_%I',
            criteria, criteria, criteria, criteria, criteria, criteria, criteria, criteria
        ), ', ')
    INTO sql_query
    FROM (SELECT DISTINCT criteria FROM your_table) sub;

    -- Create materialized view
    sql_query := format(
        'CREATE MATERIALIZED VIEW pivoted_table AS 
         SELECT test, %s FROM your_table GROUP BY test', sql_query
    );

    EXECUTE sql_query;
END $$;

Step 2: Refresh the Materialized View
----------------------------------------
Since the view is materialized, you need to refresh it when new data arrives:

REFRESH MATERIALIZED VIEW pivoted_table;

Step 3: Query from Grafana
---------------------------
Now, in Grafana, use:

SELECT * FROM pivoted_table WHERE test = $__variable;
You can add filters using Grafana variables ($__variable).

Option 2: Use a Fixed Pivot Query
###################################
If the number of criteria values is small and known,
you can manually create the pivoted SQL query in Grafana without dynamic SQL.

Example:

SELECT 
    test,
    MAX(CASE WHEN criteria = 'criteria_1' AND is_ref = TRUE THEN val END) AS val_true_criteria_1,
    MAX(CASE WHEN criteria = 'criteria_1' AND is_ref = TRUE THEN score END) AS score_true_criteria_1,
    MAX(CASE WHEN criteria = 'criteria_1' AND is_ref = FALSE THEN val END) AS val_false_criteria_1,
    MAX(CASE WHEN criteria = 'criteria_1' AND is_ref = FALSE THEN score END) AS score_false_criteria_1,
    MAX(CASE WHEN criteria = 'criteria_2' AND is_ref = TRUE THEN val END) AS val_true_criteria_2,
    MAX(CASE WHEN criteria = 'criteria_2' AND is_ref = TRUE THEN score END) AS score_true_criteria_2,
    MAX(CASE WHEN criteria = 'criteria_2' AND is_ref = FALSE THEN val END) AS val_false_criteria_2,
    MAX(CASE WHEN criteria = 'criteria_2' AND is_ref = FALSE THEN score END) AS score_false_criteria_2
FROM your_table
GROUP BY test;

Replace 'criteria_1', 'criteria_2', etc., with actual values from your data.
Use this query directly in Grafana.
Which Option is Best?
If criteria values change frequently → Use Option 1 (Materialized View).
If criteria values are fixed → Use Option 2 (Fixed Pivot Query).


```

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

https://habr.com/ru/companies/sportmaster_lab/articles/872204/

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

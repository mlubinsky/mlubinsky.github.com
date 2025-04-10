```
There is Postgres table with following 3 columns:
Date
Name
value

This Postgres table is a datasource for Grafana dashboard with table panel.
On Grafana UI user selects the dates range.
The Grafana should  filter results from table and pivot it to format
with individual column per date, so the columns in Grafana will be : 

Name
date_1
date_2
date_3,
etc

How to do it?
 

To achieve this in Grafana with a PostgreSQL datasource,
 where you want to pivot a table based on a date range selected by the user into a format
with individual columns per date (e.g., Name, date_1, date_2, date_3, etc.),
you’ll need to use a combination of PostgreSQL’s crosstab function (from the tablefunc extension) and Grafana’s query builder with variables. Here’s a step-by-step solution:

1. Enable the tablefunc Extension in PostgreSQL
The crosstab function is part of the tablefunc module, which is not enabled by default in PostgreSQL. Run the following SQL command in your PostgreSQL database to enable it:

sql
CREATE EXTENSION IF NOT EXISTS tablefunc;

2. Understand the Data and Desired Output
Your table has:

Date (e.g., '2025-04-01', '2025-04-02', etc.)
Name (e.g., 'Alice', 'Bob', etc.)
value (e.g., 10, 20, etc.)
For a selected date range (e.g., '2025-04-01' to '2025-04-03'), you want the output in Grafana to look like:

Name	2025-04-01	2025-04-02	2025-04-03
Alice	10	15	20
Bob	5	8	12

3. Set Up Grafana Variables for Date Range
Grafana will pass the selected date range to your query via variables like $timeFilter,
 or you can use custom variables for the start and end dates:

Go to your Grafana dashboard settings.
Add two variables:
start_date: Set it as a "Custom" or "Query" type, tied to your time range
(e.g., $__from:date:YYYY-MM-DD).
end_date: Similarly, set it to $__to:date:YYYY-MM-DD.

These variables will dynamically capture the date range selected by the user.

4. Write the PostgreSQL Query with crosstab
The crosstab function pivots rows into columns. It requires two SQL queries:

A source query that provides the data in a "row_name, column_name, value" format.
A category query that defines the dynamic column names (the dates).
Here’s an example query:

sql

SELECT *
FROM crosstab(
  -- Source query: Select Name, Date, and value, filtered by the date range
  'SELECT Name, Date, value
   FROM your_table
   WHERE Date BETWEEN ''$start_date'' AND ''$end_date''
   ORDER BY 1, 2',
  -- Category query: Generate the list of dates as column names
  'SELECT DISTINCT Date
   FROM your_table
   WHERE Date BETWEEN ''$start_date'' AND ''$end_date''
   ORDER BY 1'
) AS ct (
  Name text,  -- First column is the row name
  -- Dynamically list the dates as columns (you'll need to adjust this part)
  "2025-04-01" numeric,
  "2025-04-02" numeric,
  "2025-04-03" numeric
  -- These column names must match the dates in your range
);
Problem: Dynamic Column Names
The crosstab function requires you to explicitly define the column names in the AS ct (...) clause. However, since the date range is dynamic (based on user input), you can’t hardcode the dates like "2025-04-01". To solve this, you have two options:

Option 1: Use a Fixed Number of Columns
--------------------------------------
If the date range is predictable (e.g., always 7 days), you can predefine a fixed number of columns and use Grafana’s $__timeFrom and $__timeTo to shift the dates. However, this isn’t ideal for variable ranges.

Option 2: Use a Dynamic SQL Query with a Script
Since Grafana’s basic query editor doesn’t handle dynamic column names well, you can:

Write a server-side script (e.g., in Python or Node.js) t
hat generates the SQL query dynamically based on the date range.
Use a PostgreSQL function to handle the pivoting.
Here’s an example of a PostgreSQL function:

sql


CREATE OR REPLACE FUNCTION pivot_table(start_date date, end_date date)
RETURNS TABLE (name text, dynamic_values numeric[]) AS $$
DECLARE
  date_list text;
BEGIN
  -- Generate the list of dates as an array
  SELECT string_agg('"' || d::text || '" numeric', ', ')
  INTO date_list
  FROM generate_series(start_date, end_date, interval '1 day') AS d;

  -- Execute the crosstab query dynamically
  RETURN QUERY EXECUTE
    'SELECT *
     FROM crosstab(
       ''SELECT Name, Date, value
        FROM your_table
        WHERE Date BETWEEN ''' || start_date || ''' AND ''' || end_date || '''
        ORDER BY 1, 2'',
       ''SELECT DISTINCT Date
        FROM your_table
        WHERE Date BETWEEN ''' || start_date || ''' AND ''' || end_date || '''
        ORDER BY 1''
     ) AS ct (Name text, ' || date_list || ')';
END;
$$ LANGUAGE plpgsql;
Then, in Grafana, use:

sql


SELECT * FROM pivot_table('$start_date'::date, '$end_date'::date);
This approach still requires the client (Grafana) to handle dynamic column names,
which Grafana’s table panel can interpret if the query returns consistent results.

5. Configure the Grafana Table Panel
In the Grafana query editor, paste your SQL query (either the static crosstab or the function-based one).
Set the query format to “Table” in the query options.
In the “Panel” tab:
Choose the “Table” visualization.
Grafana will automatically display the columns returned by your query (Name, date_1, date_2, etc.).
6. Final Notes
Dynamic Columns Limitation: Grafana’s table panel works best with a predictable set of columns. If the number of dates varies significantly, you might need a custom plugin or a different visualization (e.g., a heatmap).
Performance: For large datasets, ensure your table is indexed on Date and Name.
Testing: Test with a small date range first (e.g., 2-3 days) to verify the pivoting works.
If you’re still stuck, let me know your exact table name and a sample of the data, and I can refine the query further!


### Search subfolders in folder
```
import os

def find_nested_folder(target_folder, prefix, pattern):
  """
  Searches for a nested folder within the target folder based on the given prefix and pattern.

  Args:
    target_folder: The root folder to search.
    prefix: The prefix of the first-level folders to consider (SF or G2).
    pattern: The pattern to search for in the nested folder names.

  Returns:
    The full path of the found nested folder, or None if not found.
  """

  for root, dirs, files in os.walk(target_folder):
    if root.startswith(os.path.join(target_folder, prefix)):
      for dir in dirs:
        if pattern in dir:
          return os.path.join(root, dir)

  return None
```

### SQL
```sql
with 
T as ( 
select   
date, test, group_name , score,  is_ref 
from kpi_score_gdc_summary 
where criteria = '_Average' 
and test_loc = '$location' 
and (folder_up like '%DEV%' or test_loc not like 'DSK%')
and folder like '%Flip%'
and to_char(date,'YYYY-MM') = '$month'
and group_name ilike '%b%'
),
C as ( 
select concat_ws(' ', test, group_name) as test, score, date, is_ref from T where not is_ref
union all 
select concat_ws(' ', test, group_name) as test, score, date, is_ref from T where   is_ref and group_name not ilike '%Ultra%'
)

SELECT
  test,
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=1) AS "1",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=2) AS "2",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=3) AS "3",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=4) AS "4",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=5) AS "5",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=6) AS "6",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=7) AS "7",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=8) AS "8",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=9) AS "9",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=10) AS "10",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=11) AS "11",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=12) AS "12",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=13) AS "13",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=14) AS "14",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=15) AS "15",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=16) AS "16",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=17) AS "17",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=18) AS "18",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=19) AS "19",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=20) AS "20",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=21) AS "21",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=22) AS "22",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=23) AS "23",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=24) AS "24",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=25) AS "25",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=26) AS "26",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=27) AS "27",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=28) AS "28",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=29) AS "29",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=30) AS "30",
  AVG(score) FILTER (WHERE  EXTRACT(DAY FROM date)=31) AS "31"
FROM C
GROUP BY test --, is_ref
ORDER BY test --, is_ref DESC
```





### Construct the SQL WHERE clause with the values from your Python list 

```
x = ['a', 'b']
sql_string = "WHERE col IN ({})".format(', '.join(f"'{item}'" for item in x))
print(sql_string)

This will output:

WHERE col IN ('a', 'b')
```
### Read SQL to pandas dataframe: pd.read_sql_query

```
from sqlalchemy import create_engine
import psycopg2, os
import pandas as pd
import configparser

    def dbFetchAllDF(self, sql):
        engine = create_engine('postgresql://{}:{}@{}:{}/{}'.format(self.username, self.password, self.host, self.port, self.dbname))
        df = pd.read_sql_query(sql, con=engine)
        return df
```
### Defaults in command line help:

https://stackoverflow.com/questions/12151306/argparse-way-to-include-default-values-in-help

parser.add_argument('-o', '--output_dir',  required=False, default=OUTPUT_DIR, help = " default: %(default)s")

parser.add_argument("--type", default="toto", choices=["toto","titi"],  help = "type (default: %(default)s)")
 
### Python command line parsing  and read from SQLite
```
There is SQLite table T with 3 string columns: date, build, value.
Python program should fetch records from table T based on command line arguments.

Please create python program which will accept the following command line parameters

--date  (string in format YYYY-MM-DD)
--end_date (string in format YYYY-MM-DD)
-–back (number of days back from --date
--build (string, it is used to detect the start date as min(date) in table T where this build exists
--ignore_builds (list of build to ignore)
--only_builds (list of builds to process)

If --date  and --and_date are provided then filter records in the range
[ --date ,  --and_date]

If --date  and --back are provided then filter records in the range
[ --date ,  --date -  -- back]

If --back_date is provided and --date is not provided then use current date for --date.

If --build is provided then start date should be detected as min(date) in table T where this build exists

If --date is provided then --build should not be provided and vice versa.
If --back is provided then --end_date should not be provided and vice versa.

```
### Solution for SQLite
```
import argparse
import sqlite3
from datetime import datetime, timedelta
import sys

def valid_date(date_str):
    """Validate the date format is YYYY-MM-DD."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: '{date_str}'. Expected format: YYYY-MM-DD.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch records from SQLite table T.")
    
    # Adding command line arguments
    parser.add_argument('--date', type=valid_date, help='Start date in format YYYY-MM-DD.')
    parser.add_argument('--end_date', type=valid_date, help='End date in format YYYY-MM-DD.')
    parser.add_argument('--back', type=int, help='Number of days back from --date.')
    parser.add_argument('--build', type=str, help='Build name to detect the start date.')
    parser.add_argument('--ignore_builds', nargs='*', help='List of builds to ignore.')
    parser.add_argument('--only_builds', nargs='*', help='List of builds to process.')
    
    args = parser.parse_args()

    # Validations
    if args.date and args.build:
        print("Error: --date and --build cannot be provided together.")
        sys.exit(1)
    
    if args.back and args.end_date:
        print("Error: --back and --end_date cannot be provided together.")
        sys.exit(1)
    
    return args

def fetch_start_date_from_build(conn, build):
    """Fetch the minimum date for a given build."""
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(date) FROM T WHERE build = ?", (build,))
    result = cursor.fetchone()
    if result and result[0]:
        return result[0]
    else:
        print(f"No records found for build '{build}'.")
        sys.exit(1)

def fetch_records(conn, start_date, end_date, only_builds, ignore_builds):
    """Fetch records based on the start date, end date, and build filters."""
    query = "SELECT * FROM T WHERE date >= ? AND date <= ?"
    params = [start_date, end_date]
    
    if only_builds:
        query += " AND build IN ({})".format(','.join(['?'] * len(only_builds)))
        params.extend(only_builds)
    
    if ignore_builds:
        query += " AND build NOT IN ({})".format(','.join(['?'] * len(ignore_builds)))
        params.extend(ignore_builds)
    
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

def main():
    args = parse_arguments()
    
    conn = sqlite3.connect('your_database.db')  # Connect to SQLite database
    cursor = conn.cursor()

    # Determine the start date
    if args.build:
        start_date = fetch_start_date_from_build(conn, args.build)
    elif args.date:
        start_date = args.date.strftime('%Y-%m-%d')
    elif args.back and not args.date:
        start_date = (datetime.now() - timedelta(days=args.back)).strftime('%Y-%m-%d')
    else:
        print("Error: Either --date or --build must be provided.")
        sys.exit(1)

    # Determine the end date
    if args.end_date:
        end_date = args.end_date.strftime('%Y-%m-%d')
    elif args.back:
        end_date = (datetime.strptime(start_date, '%Y-%m-%d') - timedelta(days=args.back)).strftime('%Y-%m-%d')
    else:
        end_date = start_date

    # Fetch records from the table
    records = fetch_records(conn, start_date, end_date, args.only_builds, args.ignore_builds)
    
    for record in records:
        print(record)

    conn.close()

if __name__ == "__main__":
    main()

```

### Solution for Postgres
```
Parameterized Queries:

The placeholder for parameters in PostgreSQL queries uses %s instead of ? as in SQLite.
This applies both to fetch_start_date_from_build() and fetch_records().
 
Cursor and Execution:

The PostgreSQL adapter uses a similar method for executing SQL queries but with cursor.execute(query,
params) where params is a list of parameters to be safely injected into the query.



import argparse
import psycopg2
from datetime import datetime, timedelta
import sys

def valid_date(date_str):
    """Validate the date format is YYYY-MM-DD."""
    try:
        return datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid date format: '{date_str}'. Expected format: YYYY-MM-DD.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Fetch records from PostgreSQL table T.")
    
    # Adding command line arguments
    parser.add_argument('--date', type=valid_date, help='Start date in format YYYY-MM-DD.')
    parser.add_argument('--end_date', type=valid_date, help='End date in format YYYY-MM-DD.')
    parser.add_argument('--back', type=int, help='Number of days back from --date.')
    parser.add_argument('--build', type=str, help='Build name to detect the start date.')
    parser.add_argument('--ignore_builds', nargs='*', help='List of builds to ignore.')
    parser.add_argument('--only_builds', nargs='*', help='List of builds to process.')
    
    args = parser.parse_args()

    # Validations
    if args.date and args.build:
        print("Error: --date and --build cannot be provided together.")
        sys.exit(1)
    
    if args.back and args.end_date:
        print("Error: --back and --end_date cannot be provided together.")
        sys.exit(1)
    
    return args

def fetch_start_date_from_build(conn, build):
    """Fetch the minimum date for a given build from PostgreSQL."""
    cursor = conn.cursor()
    cursor.execute("SELECT MIN(date) FROM T WHERE build = %s", (build,))
    result = cursor.fetchone()
    if result and result[0]:
        return result[0]
    else:
        print(f"No records found for build '{build}'.")
        sys.exit(1)

def fetch_records(conn, start_date, end_date, only_builds, ignore_builds):
    """Fetch records based on the start date, end date, and build filters."""
    query = "SELECT * FROM T WHERE date >= %s AND date <= %s"
    params = [start_date, end_date]
    
    if only_builds:
        query += " AND build IN ({})".format(','.join(['%s'] * len(only_builds)))
        params.extend(only_builds)
    
    if ignore_builds:
        query += " AND build NOT IN ({})".format(','.join(['%s'] * len(ignore_builds)))
        params.extend(ignore_builds)
    
    cursor = conn.cursor()
    cursor.execute(query, params)
    return cursor.fetchall()

def main():
    args = parse_arguments()
    
    # Connect to PostgreSQL database
    conn = psycopg2.connect(
        dbname="your_database",
        user="your_user",
        password="your_password",
        host="your_host",
        port="your_port"
    )

    # Determine the start date
    if args.build:
        start_date = fetch_start_date_from_build(conn, args.build)
    elif args.date:
        start_date = args.date.strftime('%Y-%m-%d')
    elif args.back and not args.date:
        start_date = (datetime.now() - timedelta(days=args.back)).strftime('%Y-%m-%d')
    else:
        print("Error: Either --date or --build must be provided.")
        sys.exit(1)

    # Determine the end date
    if args.end_date:
        end_date = args.end_date.strftime('%Y-%m-%d')
    elif args.back:
        end_date = (datetime.strptime(start_date, '%Y-%m-%d') - timedelta(days=args.back)).strftime('%Y-%m-%d')
    else:
        end_date = start_date

    # Fetch records from the table
    records = fetch_records(conn, start_date, end_date, args.only_builds, args.ignore_builds)
    
    for record in records:
        print(record)

    conn.close()

if __name__ == "__main__":
    main()


```


### Delete folders

Recursively deletes a folder and its contents, and then removes empty parent folders.

Args:   folder_name (str): The name of the folder to delete.
 

```
import os
import shutil

def delete_folder(folder_path):
    # Remove the folder and all its contents
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    
    # Move up the directory hierarchy, deleting empty directories
    parent_path = os.path.dirname(folder_path)
    while parent_path:
        try:
            os.rmdir(parent_path)  # Remove the directory if empty
        except OSError:
            break  # Stop if the directory is not empty or an error occurs
        parent_path = os.path.dirname(parent_path)
```
Gemini
```
import os
import shutil

def delete_folder(folder_name):

    full_path = os.path.abspath(folder_name)

    try:
        # Remove the specified folder and its contents
        shutil.rmtree(full_path)

        # Check if the parent folder is empty
        parent_folder = os.path.dirname(full_path)
        while os.path.exists(parent_folder) and not os.listdir(parent_folder):
            os.rmdir(parent_folder)
            parent_folder = os.path.dirname(parent_folder)

    except OSError as e:
        print(f"Error deleting folder: {e}")

if __name__ == "__main__":
    folder_to_delete = "path/to/your/folder"  # Replace with the actual folder path
    delete_folder(folder_to_delete)
```


### Search in subfolder
```
import os
import fnmatch

def find_files_in_subfolders(folder_name, file_suffix, subfolder_pattern):
    matching_files = []
    
    for root, dirs, files in os.walk(folder_name):
        # Check if the current directory matches the subfolder pattern
        if fnmatch.fnmatch(os.path.basename(root), subfolder_pattern):
            for file in files:
                if file.endswith(file_suffix):
                    matching_files.append(os.path.join(root, file))
                    
    return matching_files



import os
import fnmatch

def find_files(folder_name, file_suffix, subfolder_pattern):


  file_list = []
  for root, _, files in os.walk(folder_name):
    if fnmatch.fnmatchcase(root, os.path.join(folder_name, subfolder_pattern)):
      for file in files:
        if file.endswith(file_suffix):
          file_list.append(os.path.join(root, file))
  return file_list
```


### Parse csv 
```
import csv

def get_unique_values_first_column(csv_file_name):
    unique_values = set()
    
    with open(csv_file_name, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header line
        
        for row in reader:
            if row:  # Check if the row is not empty
                unique_values.add(row[0])
    
    return list(unique_values)


import csv

def get_unique_values(csv_file):
  unique_values = set()
  with open(csv_file, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    for row in reader:
      unique_values.add(row[0])
  return list(unique_values)
```

### subprocess.Popen()
https://realpython.com/python-subprocess/
Gemini
```
 Execute a long-running batch file from Python, capture its output in real-time,
 and display it to the console. keep last 100 records in queue

 
import subprocess
from collections import deque
#-----------------------------------------
def run_bat_and_get_returncode(bat_file):
#-----------------------------------------
  output_deque = deque(maxlen=100)
  with subprocess.Popen(bat_file, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True,  cwd=cwd) as process:
    while True:
      output = process.stdout.readline()
      if output == '' and process.poll() is not None:
        break
      if output:
        print(output.strip())
        output_deque.append(output.strip())

  last_100_records = list(output_deque)
  return process.returncode

# Example usage:
bat_file = "path/to/your/a.bat"
return_code = run_bat_and_get_returncode(bat_file)
print("Return code:", return_code)

```
ChatGPT

```
When you use subprocess.run() with capture_output=True, the output is captured and not immediately displayed in the console. If you want to see the output in real-time, you can use the subprocess.Popen method instead. This allows you to read the output line by line and print it to the console as it is generated.

Here's how you can do it:

python
Copy code
import subprocess

with subprocess.Popen("a.bat", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as process:
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
    rc = process.poll()
This script will invoke a.bat and print each line of output to the console as it is produced. The while loop continuously reads from the stdout pipe until there is no more output and the process has finished.

Here's a more detailed explanation of each part of the script:

subprocess.Popen: This function is used to execute a subprocess and provides more flexibility than subprocess.run().
stdout=subprocess.PIPE: This captures the standard output.
stderr=subprocess.PIPE: This captures the standard error.
text=True: This makes sure that the output is treated as text (str) instead of bytes.
while True loop: This reads the output line by line.
output = process.stdout.readline(): Reads a single line from the standard output.
if output == '' and process.poll() is not None:: Checks if the process has finished.
if output:: If there is output, it prints it to the console.
process.poll(): This checks the return code of the process.
This way, you can see the output of the .bat file in real-time in the console while it is being executed by Python.
```



### Grafana - assign color to bar chart
```
ooking for a solution that automatically assigns different colors to bars without manual configuration, especially since  data is dynamically extracted from a database table. Let's explore some options that might work better for your case:

Color scheme: Continuous color

If "Classic palette (by series name)" isn't working as expected, try using "Continuous color" instead. This option should assign different colors based on the series name.
To set this up:

Go to the "Field" tab in your panel settings.
Under "Color scheme", select "Continuous color".
Choose a color range that suits your needs (e.g., "Red-Yellow-Green" or "Blue-Purple").
Use a Transformation

If the above doesn't work, you can try using a transformation to add a numeric index to your data, then use that for coloring:

Go to the "Transform" tab in your panel settings.
Add a new transformation: "Add field from calculation".
Set "Mode" to "Row index".
Give it a name like "ColorIndex".
Go back to the "Field" tab.
Under "Color scheme", choose "Continuous color" or "From numerical field".
Select your "ColorIndex" field as the source for the color.
Override rules

If the above methods don't work, you can try using override rules:

Go to the "Overrides" tab in your panel settings.
Click "Add field override".
For "Fields with name", select your "name" field.
Add an override property: "Color scheme".
Choose "Classic palette" or another scheme that provides multiple colors.
Check Grafana version and update

If none of these methods work, it's possible that you're using an older version of Grafana that doesn't support automatic color assignment for bar charts. Consider updating to the latest version if possible.

Custom plugin or scripting

As a last resort, you might need to look into custom plugins or scripting solutions that can assign colors programmatically based on your data.
If you try these methods and still face issues, it would be helpful to know your Grafana version and any error messages or unexpected behaviors you're seeing. Also, double-check that your SQL query is indeed returning different names for each bar, as this is crucial for most automatic coloring methods to work correctly.
```


### Find matching - ChatGPT
```
import os
import glob

# Define input and output base directories
input_base_dir = r"C:\FieldTestLogs\spotlight"
output_base_dir = r"C:\RegressionLibrary\SPOT-ACE"

def get_matching_output_folder(input_folder):
    # Extract the year, month, and day from the input folder path
    parts = input_folder.split(os.sep)
    year, month, day = parts[-3], parts[-2], parts[-1]
    output_folder = os.path.join(output_base_dir, year, month, day)
    return output_folder

def check_subfolder_existence(input_folder, output_folder, subfolder_name):
    input_subfolder = os.path.join(input_folder, subfolder_name)
    if os.path.exists(input_subfolder):
        output_subfolders = glob.glob(os.path.join(output_folder, f"{subfolder_name}*"))
        if not output_subfolders:
            print(f"Missing matching output subfolder for: {input_subfolder}")

def main():
    for root, dirs, files in os.walk(input_base_dir):
        if len(dirs) == 0 and len(files) == 0:
            # This is an empty directory
            continue
        
        if len(dirs) == 2 and all(d in dirs for d in ['SF', 'G2']):
            input_folder = root
            output_folder = get_matching_output_folder(input_folder)
            
            if not os.path.exists(output_folder):
                print(f"No matching output folder for: {input_folder}")
            else:
                check_subfolder_existence(input_folder, output_folder, 'G2')
                check_subfolder_existence(input_folder, output_folder, 'SF')
        elif 'SF' in dirs or 'G2' in dirs:
            input_folder = root
            output_folder = get_matching_output_folder(input_folder)
            
            if not os.path.exists(output_folder):
                print(f"No matching output folder for: {input_folder}")
            else:
                if 'G2' in dirs:
                    check_subfolder_existence(input_folder, output_folder, 'G2')
                if 'SF' in dirs:
                    check_subfolder_existence(input_folder, output_folder, 'SF')

if __name__ == "__main__":
    main()
```

### Find the matching - Gemini:
```

import os

def find_matching_output(input_folder):
  """
  Finds the matching output folder for a given input folder based on MM-DD.

  Args:
      input_folder (str): Path to the input folder.

  Returns:
      str: Path to the matching output folder or None if not found.
  """
  # Extract month and day from input folder path
  _, _, month_day = input_folder.split("\\")[-2:]

  # Construct matching output folder path
  output_folder = os.path.join(
      "C:\\RegressionLibrary\\SPOT-ACE", month_day, month_day
  )

  # Check if output folder exists
  if not os.path.exists(output_folder):
    return None

  return output_folder

def check_subfolder_match(input_folder, subfolder, output_folder):
  """
  Checks if the output folder has a subfolder starting with the specified name.

  Args:
      input_folder (str): Path to the input folder.
      subfolder (str): Name of the subfolder to check (e.g., "G2", "SF").
      output_folder (str): Path to the output folder.

  Returns:
      bool: True if a matching subfolder is found, False otherwise.
  """
  matching_subfolders = [
      d for d in os.listdir(output_folder) if d.startswith(subfolder)
  ]
  return len(matching_subfolders) > 0

def main():
  """
  Main function to iterate through input folders and perform checks.
  """
  base_path = "C:\\FieldTestLogs\\spotlight"

  for year in range(2024, 2025):
    for month in range(1, 13):
      month_str = f"{month:02d}"
      for day in range(1, 32):
        day_str = f"{day:02d}"
        input_folder = os.path.join(base_path, year, month_str, day_str)

        # Check if input folder exists
        if not os.path.exists(input_folder):
          continue

        # Find matching output folder
        output_folder = find_matching_output(input_folder)

        if not output_folder:
          # No matching output folder found
          print(f"Input folder: {input_folder} (no matching output)")
          continue

        # Check for G2 subfolder mismatch
        if os.path.exists(os.path.join(input_folder, "G2")) and not check_subfolder_match(input_folder, "G2", output_folder):
          print(f"Input G2 mismatch: {os.path.join(input_folder, 'G2')}")

        # Check for SF subfolder mismatch
        if os.path.exists(os.path.join(input_folder, "SF")) and not check_subfolder_match(input_folder, "SF", output_folder):
          print(f"Input SF mismatch: {os.path.join(input_folder, 'SF')}")

if __name__ == "__main__":
  main()
```

### Geolocation 1
```
First, you need to sign up for an API key from OpenCage: OpenCage Geocoding API.

Here is the Python function:

python
Copy code
import requests

def get_geolocation(api_key, latitude, longitude):
    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "key": api_key,
        "q": f"{latitude},{longitude}",
        "pretty": 1
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['components']
            address = data['results'][0]['formatted']
            city = location.get('city', '')
            state = location.get('state', '')
            country = location.get('country', '')
            country_code = location.get('country_code', '').upper()
            return {
                "address": address,
                "city": city,
                "state": state,
                "country": country,
                "country_code": country_code
            }
        else:
            return "No results found for the given coordinates."
    else:
        return f"Error: {response.status_code}"

# Example usage
api_key = "YOUR_API_KEY"
latitude = 51.5074
longitude = -0.1278

geolocation = get_geolocation(api_key, latitude, longitude)
print(geolocation)

```


### Geolocation 2
```
import requests

def get_geolocation(longitude, latitude, api_key=None):
  """
  Retrieves geolocation information based on longitude and latitude.

  Args:
      longitude (float): Longitude coordinate.
      latitude (float): Latitude coordinate.
      api_key (str, optional): API key for an external service (if needed). Defaults to None.

  Returns:
      dict: Dictionary containing geolocation information (may vary depending on service).
  """

  # Example using Google Maps Geocoding API (replace with your preferred service)
  if api_key:
    url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={latitude},{longitude}&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
      data = response.json()
      if data['status'] == 'OK':
        # Extract relevant information from the response (may vary based on service)
        address = data['results'][0]['formatted_address']
        for component in data['results'][0]['address_components']:
          if 'administrative_area_level_2' in component['types']:
            city = component['long_name']
          elif 'administrative_area_level_1' in component['types']:
            state = component['long_name']
          elif 'country' in component['types']:
            country = component['long_name']
        return {
          'address': address,
          'city': city,
          'state': state,
          'country': country,
        }
      else:
        print(f"Geocoding error: {data['status']}")
    else:
      print(f"API request failed with status code: {response.status_code}")
  else:
    print("Warning: No API key provided. Geolocation lookup may not be available.")

  return {}

# Example usage (replace with your actual API key or use a different service)
geolocation = get_geolocation(longitude=-122.4194, latitude=37.7749, api_key='<YOUR_API_KEY>')
if geolocation:
  print(geolocation)
else:
  print("Geolocation information unavailable.")
Use code with caution.
content_copy
Remember to replace '<YOUR_API_KEY>' with your actual API key if you're using an external service.  This function provides a basic framework, and you'll need to adapt it to the specific service you choose.

For a purely local approach, you'd need to explore local geocoding databases or libraries that might be available for your use case. These may have their own installation and usage instructions.

```


### Debug print in PHP

echo nl2br("\n command=" . $command ) ;

echo json_encode($_REQUEST); for hash arrays

### Pandas
```
error_types_interests = ['_position2DError', '_xTrackError', '_alongTrackError', 'SOG_Error', '_headingError', 'dist_error']

df1_lsi_tmp = df1_LSI.loc[df1_LSI['Error_Type'].isin(error_types_interests)].groupby(['Chipset','Model','Signal_Bands','Error_Type']).agg('mean')
```


### Javascript HTTP POST  - PHP

```
var str = JSON.stringify(obj, null, 2);
consol.log(str)
```
https://stackoverflow.com/questions/45426158/send-data-from-html-form-to-php

 https://www.w3schools.com/php/php_forms.asp

### Redirect output to file

Take care to add 2>&1 at the end of the instruction because on Windows, the order of redirection is important as command 2>&1 > logfile will produce an empty file

#### To combine ERR and STDOUT
``` 
command > logfile 2>&1 
```
##### To separate ERR and STDOUT
```
dir test.exe > output.txt 2> err.txt
```


###  Setup Superset
https://apache-superset.readthedocs.io/en/latest/installation.html
```
py --list
  *               Active venv
 -V:3.12          Python 3.12 (64-bit)
 -V:3.10          Python 3.10 (64-bit)
 -V:3.8           Python 3.8 (64-bit)
 -V:2.7           Python 2.7
 -V:2.7-32        Python 2.7-32

cd c:\ALL_VENV
cd c:\CODE\all_venv

rmdir /S /Q SUPERSET
python -m venv SUPERSET 
SUPERSET\Scripts\activate.bat
python.exe -m pip install --upgrade pip --index-url=http://105.128.27.80/PYPI/web/simple --trusted-host 105.128.27.80    
pip install apache-superset==1.3.2  --index-url=http://105.128.27.80/PYPI/web/simple --trusted-host 105.128.27.80


deactivate
```


#### Redirect to NULL
```
dir test.exe 1> myoutput.txt 2>nul
```
### File Compare Utils
winmerge

Compare It!
https://www.grigsoft.com/wincmp3.htm


### Inertial Measurement Unit - IMU

INS (inersial  navigational systems) -  инерциальные навигационные системы (ИНС)

 Блок инерциальных измерений (БИИ, или от англ. IMU — Inertial Measurement Unit) состоит из гироскопов и акселерометров позволяющих отслеживать вращательные и поступательные движения.
 
https://habr.com/ru/companies/whoosh/articles/765628/


https://habr.com/ru/articles/255661/ Фильтр Маджвика

### TODO
```
Weekly MX KPI
AGPS (m)  labels are wrong  
TODO
****** Order for MX
1 Percentage Total fix count
2 Percentage SpecIn 2D Error 30 m
3 Percentage Speed 20 km/h
4 Percentage VDR Engage count

Add for Internal dashboard (Heading | 2DError| Speed) 90 panel

Fix Type: All, VDR, non_VDR for MX and Internal

Add CEP90 for Daily

How to populate programmatically threshold and max ?


Daily dashboard:  model variable should be populated based on the selected date
```
### Install Apache on Windows

LoadModule libpq_module /usr/lib/apache/1.3/mod_libpq.so  http.conf

https://www.sitepoint.com/how-to-install-apache-on-windows/

Microsoft have new version of vc_redist for apps developed with Microsoft Visual Studio 2022.
Version: 14.30.30704

x64 - https://aka.ms/vs/17/release/VC_redist.x64.exe

Download Apache (x64)  https://www.apachelounge.com/

Open an “Administrator” command prompt
```
mkdir c:/Apache24
cd  c:/Apache24/bin
httpd.exe -t
httpd.exe
 http://localhost
 
Install Apache Service
 httpd.exe -k install -n "Apache HTTP Server"

Edit conf/httpd.conf 
Line 60, listen to all requests on port 80:
Listen *:80
Line 162, enable mod-rewrite by removing the # (optional, but useful):

LoadModule rewrite_module modules/mod_rewrite.so
Line 227, specify the server domain name:

ServerName localhost:80
Line 224, allow .htaccess overrides:

AllowOverride All
```
### WAMPSERVER

https://www.wampserver.com/en/

https://stackoverflow.com/questions/32922816/install-two-instance-of-wampserver-on-same-pc

https://superuser.com/questions/994013/run-two-wamp-servers-installed-in-different-drives-simultaneously

### GNSS, RINEX,  NMEA  (National Marine Electronics Association)

https://docs.novatel.com/OEM7/Content/Logs/GPRMC.htm
```
field 10 is the date: Date: dd/mm/yy xxxxxx 210307
Fixes can come from 3 possible message types.  For each fix UTC, we will choose exactly one of GPGGA, GPRMC, and GNRMC, in that priority order.
```
The date field is in GPRMC and GNRMC, but not the GPGGA sentence

https://www.sparkfun.com/datasheets/GPS/NMEA%20Reference%20Manual-Rev2.1-Dec07.pdf NMEA

https://home.csis.u-tokyo.ac.jp/~dinesh/Dinesh_T_files/GNSS_10_Introduction_DataFormats.pdf

https://en.wikipedia.org/wiki/NMEA_0183

https://www.gpsworld.com/what-exactly-is-gps-nmea-data/

https://cddis.nasa.gov/Data_and_Derived_Products/GNSS/GNSS_data_holdings.html

https://gage.upc.edu/en/learning-materials/library/gnss-format-descriptions

https://psmsl.org/data/gnssir/fileinfo.php

https://frontierprecision.com/the-power-of-gnss-metadata/

Receiver Independent Exchange format (RINEX)

https://gssc.esa.int/navipedia/index.php/Interfaces_and_Protocols RINEX

## KML format

https://developers.google.com/kml/documentation/kmlreference#polygon

https://sites.google.com/site/kmltouring/google-earth-tools/polygons

https://sites.google.com/site/kmltouring/editing-kml

https://sites.google.com/site/kmltouring/google-earth-tools/placemarks-pins

https://renenyffenegger.ch/notes/tools/Google-Earth/kml/index

https://developers.google.com/kml/documentation/kml_tut

### Web
 ```
<!DOCTYPE html>
<html>
<head>
  <title>Vertical Radio Buttons with Conditional Text Input</title>
  <script>
    function handleRadioChange() {
      var option1Radio = document.getElementById("option1");
      var option2Radio = document.getElementById("option2");
      var textInput1 = document.getElementById("text-input1");
      var textInput2 = document.getElementById("text-input2");

      if (option1Radio.checked) {
        textInput1.style.display = "block";
        textInput2.style.display = "none";
      } else if (option2Radio.checked) {
        textInput1.style.display = "none";
        textInput2.style.display = "block";
      } else {
        textInput1.style.display = "none";
        textInput2.style.display = "none";
      }
    }
  </script>
  <style>
    .text-input {
      display: none;
    }
  </style>
</head>
<body>
  <h2>Choose an Option:</h2>
  <label for="option1">
    <input type="radio" id="option1" name="options" value="option1" onchange="handleRadioChange()"> Option 1
  </label>
  <br>
  <label for="option2">
    <input type="radio" id="option2" name="options" value="option2" onchange="handleRadioChange()"> Option 2
  </label>
  <br>
  <label for="text-input1">Text Input 1:</label>
  <input type="text" id="text-input1" name="text-input1" class="text-input">
  <br>
  <label for="text-input2">Text Input 2:</label>
  <input type="text" id="text-input2" name="text-input2" class="text-input">
</body>
</html>



```


Same as above but with Angular 1

```
<!DOCTYPE html>
<html ng-app="myApp">
<head>
  <title>Vertical Radio Buttons with Conditional Text Input (AngularJS)</title>
  <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.7.9/angular.min.js"></script>
  <style>
    .text-input {
      display: none;
    }
  </style>
</head>
<body ng-controller="myController">
  <h2>Choose an Option:</h2>
  <label for="option1">
    <input type="radio" id="option1" name="options" value="option1" ng-model="selectedOption" ng-change="handleRadioChange()"> Option 1
  </label>
  <br>
  <label for="option2">
    <input type="radio" id="option2" name="options" value="option2" ng-model="selectedOption" ng-change="handleRadioChange()"> Option 2
  </label>
  <br>
  <label for="text-input1">Text Input 1:</label>
  <input type="text" id="text-input1" name="text-input1" class="text-input" ng-show="selectedOption === 'option1'">
  <br>
  <label for="text-input2">Text Input 2:</label>
  <input type="text" id="text-input2" name="text-input2" class="text-input" ng-show="selectedOption === 'option2'">

  <script>
    angular.module('myApp', [])
      .controller('myController', function($scope) {
        $scope.handleRadioChange = function() {
          var option1 = 'option1';
          var option2 = 'option2';

          var textInput1 = document.getElementById("text-input1");
          var textInput2 = document.getElementById("text-input2");

          if ($scope.selectedOption === option1) {
            textInput1.style.display = "block";
            textInput2.style.display = "none";
          } else if ($scope.selectedOption === option2) {
            textInput1.style.display = "none";
            textInput2.style.display = "block";
          } else {
            textInput1.style.display = "none";
            textInput2.style.display = "none";
          }
        };
      });
  </script>
</body>
</html>
```
Explanation:
```
In this example, we start by including the AngularJS library using a script tag.
The ng-app directive is added to the html element to initialize the AngularJS application.

We define an AngularJS module called "myApp" and create a controller called "myController" using the controller method.
 The controller function is then attached to the ng-controller directive in the body tag.

Inside the controller function, we define the handleRadioChange function, which will be triggered whenever a radio button is selected or deselected.
You can implement the necessary logic within this function to handle the visibility of the text input elements based on the selected radio button.

In the HTML code, the ng-model directive is used to bind the selected radio button value to the $scope.selectedOption variable.
The ng-change directive is used to call the handleRadioChange function whenever the selected option changes.

The ng-show directive is applied to each text input element to conditionally show or hide them based on the value of $scope.selectedOption.
 If the selected option matches the desired option for each text input, the respective input will be displayed.

Note: AngularJS is an older version of the Angular framework and is no longer actively developed or recommended for new projects.
 It's recommended to use the latest version of Angular (Angular 2+) for new projects.
````

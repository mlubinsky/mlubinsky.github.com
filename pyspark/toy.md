There is a file were every line is json.
Example of 1 line:
```
{"headers":{"VIN":"GKO9000"},"vehicleModel":"RAV4","sensorData":{"label":["TripIndex","TripIndex","Fuel","TripIndex","Fuel","Fuel","Fuel","TripIndex","Fuel","TripIndex","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","TripIndex","Fuel","Fuel","Fuel","Fuel","Fuel","Odometer"],"value":["325","325","0.09463525000000002","325","0.031545083333333335","0.031545083333333335","0.05257513888888889","325","0.15772541666666667","325","0.07360519444444445","0.031545083333333335","0.07360519444444445","0.04206011111111111","0.07360519444444445","0.06309016666666667","0.04206011111111111","0.031545083333333335","0.031545083333333335","325","0.07360519444444445","0.04206011111111111","0.05257513888888889","0.05257513888888889","0","20003"],"dateTime":["1693274786.0","1693274786.05","1693274786.08","1693274786.1","1693274786.11","1693274786.14","1693274786.19","1693274786.2","1693274786.34","1693274786.4","1693274786.41","1693274786.44","1693274786.51","1693274786.55","1693274786.62","1693274786.68","1693274786.72","1693274786.75","1693274786.78","1693274786.8","1693274786.85","1693274786.89","1693274786.94","1693274786.99","1693274786.99","1693274786.99"]},"identifier":"436a0117-7d09-497f-a367-e6d9c3ad202a"}

```


JSON  has the following nested structure:  
● headers:MapType() that contains a unique vehicle identifier.  
● vehicleModel:StringType() that contains each vehicle's model type.  

??? ● vehicleData:ArrayType() that contains vehicle data.  It has the following fields:  

● sensorData:StructType() that contains simulated vehicle sensor data.  
In this struct you will find arrays of sensor data that were logged during each second of recording.  
```
    ○ label:ArrayType() with the labels of the logged sensors.
        The three sensors names we've simulated here are:  
        ■ Odometer: Odometer value in miles (total miles the vehicle has driven since it was built).  
        ■ Fuel: Amount of fuel consumed (in milliliters) since the last Fuel value was recorded.  
        ■ TripIndex: Unique number that indexes the number of trips that have occured. This trip index increases by one with each new trip.   

     ○ value:ArrayType() with the sensor values(e.g.,odometermiles, fuel ml, trip index).
     ○ dateTime:ArrayType() with unix timestamp of when each sensor value was logged.
```

### Assignment Questions
1) Data aggregation  
Please aggregate the data into a format where we have summaries for each TripIndex completed by each VIN.  
We would like you to provide the following summaries for each trip:

● Start_Time: the unix timestamp for when the trip started  
● End_Time: unix timestamp for when the trip ended  
● Odo_min: minimum odometer value during each trip  
● Odo_max: maximum odometer value during each trip  
● Fuel_ml: sum of the milliliters of fuelconsumed during each trip  

We would also like you to include a column for vehicleModel.
 
Below is an example of the column headers we are expecting,   
with each row representing summaries for each trip completed by each vehicle.
 

  |VIN|vehicleModel|TripIndex|Start_Time|End_Time|Odo_min|Odo
  _max|Fuel_ml|  
  |---|------------|---------|----------|--------|-------|---
  ----|-------|

```
 VIN
vehicleModel
TripIndex
Start_Time
End_Time
Odo_min
Odo _max
Fuel_ml|
```
  
  Insert code here for Q1 here --- add as many cells below as needed
 Write your thought process for the above code and the optimizations you would like to do


```python
# Databricks notebook using PySpark to read the described JSON structure into a DataFrame
# and prepare for structured processing

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, MapType, ArrayType

# Initialize Spark session (Databricks already provides spark by default)
spark = SparkSession.builder.appName("ReadVehicleJson").getOrCreate()

# Define the schema explicitly for better performance and clear structure
schema = StructType([
    StructField("headers", MapType(StringType(), StringType()), True),
    StructField("vehicleModel", StringType(), True),
    StructField("sensorData", StructType([
        StructField("label", ArrayType(StringType()), True),
        StructField("value", ArrayType(StringType()), True),
        StructField("dateTime", ArrayType(StringType()), True)
    ]), True),
    StructField("identifier", StringType(), True)
])

# Adjust the path to your file in DBFS, e.g., "/FileStore/tables/vehicle_data.json"
file_path = "/dbfs/FileStore/tables/vehicle_data.json"

# Read the JSON file with the specified schema
df = spark.read.schema(schema).json(file_path)

# Show a few records for verification
df.show(truncate=False)

df.printSchema()

# If you want to select and flatten some columns for further analysis
flattened_df = df.select(
    df["headers"].getItem("VIN").alias("VIN"),
    "vehicleModel",
    "sensorData.label",
    "sensorData.value",
    "sensorData.dateTime",
    "identifier"
)

flattened_df.show(truncate=False)


```



###2) Architect a Data Pipeline

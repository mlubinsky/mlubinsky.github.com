There is a file were every line is json.
Example of 1 line:
```
{"headers":{"VIN":"GKO9000"},"vehicleModel":"RAV4","sensorData":{"label":["TripIndex","TripIndex","Fuel","TripIndex","Fuel","Fuel","Fuel","TripIndex","Fuel","TripIndex","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","Fuel","TripIndex","Fuel","Fuel","Fuel","Fuel","Fuel","Odometer"],"value":["325","325","0.09463525000000002","325","0.031545083333333335","0.031545083333333335","0.05257513888888889","325","0.15772541666666667","325","0.07360519444444445","0.031545083333333335","0.07360519444444445","0.04206011111111111","0.07360519444444445","0.06309016666666667","0.04206011111111111","0.031545083333333335","0.031545083333333335","325","0.07360519444444445","0.04206011111111111","0.05257513888888889","0.05257513888888889","0","20003"],"dateTime":["1693274786.0","1693274786.05","1693274786.08","1693274786.1","1693274786.11","1693274786.14","1693274786.19","1693274786.2","1693274786.34","1693274786.4","1693274786.41","1693274786.44","1693274786.51","1693274786.55","1693274786.62","1693274786.68","1693274786.72","1693274786.75","1693274786.78","1693274786.8","1693274786.85","1693274786.89","1693274786.94","1693274786.99","1693274786.99","1693274786.99"]},"identifier":"436a0117-7d09-497f-a367-e6d9c3ad202a"}

```


JSON  has the following nested structure:
● headers:MapType()thatcontainsauniquevehicleidentifier.
● vehicleModel:StringType()thatcontainseachvehicle'smodeltype.
● vehicleData:ArrayType()that contains vehicle data. It has the following
fields:
● sensorData:StructType()that contains simulated vehicle sensordata.
In this
struct you will find arrays of sensor data that were logged during each second of recording.
○ label:ArrayType()with the labels of the logged sensors.The three sensors we've simulated here are:
■ Odometer:Odometer value in miles(totalmilesthe vehicle has driven since it was built).
■ Fuel:Amountoffuelconsumed(inmilliliters)sincethe last Fuel value was recorded.
■ TripIndex:Unique number that indexes the numberof trips that have occured. This trip index increases by one with each new trip.
○ value:ArrayType() with the sensor values(e.g.,odometermiles, fuel ml, trip index).
○ dateTime:ArrayType() withunixtimestampofwheneachsensor value was logged.
Assignment Questions
1) Data aggregation
Please aggregate the data into a format where we have summaries for each TripIndex completed by each VIN. We would like you to provide the following summaries for each trip:
● Start_Time:theunixtimestampforwhenthetripstarted ● End_Time:unixtimestampforwhenthetripended
● Odo_min:minimumodometervalueduringeachtrip
● Odo_max:maximumodometervalueduringeachtrip
● Fuel_ml:sumofthemillilitersoffuelconsumedduringeachtrip We would also like you to include a column for vehicleModel.
Below is an example of the column headers we are expecting, with each row representing summaries for each trip completed by each vehicle.
None
  +---+------------+---------+----------+--------+-------+---
  ----+-------+
  |VIN|vehicleModel|TripIndex|Start_Time|End_Time|Odo_min|Odo
  _max|Fuel_ml|
  +---+------------+---------+----------+--------+-------+---
  ----+-------+
 # Insert code here for Q1 here --- add as many cells below as needed
# Write your thought process for the above code and the optimizations you would like to do
2) Architect a Data Pipeline

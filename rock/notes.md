
### Looker
```
https://docs.looker.com/reference/explore-params/cancel_grouping_fields
Bucket is pivoted
Un-hide measure
Remove calculations
Leave 1 dimension only ???


dim_device_detail:  dim_product (product_id, product_segment here is device_type: TV /Players /Whole Home
```

### Git pull
```
If you are working for longer duration on your branch, you may want to pull in changes 
from master every now and then to make sure you are not too far behind and in conflict with someone else' deployed changes.
$ git checkout DEA-xxxx
$ git pull origin master
```

### Development Hive table:
```
LOCATION 's3://roku-dea-dev/sand-box/roku-data-warehouse/roku/dimensions/dim_experiment' 
Should be:
[s3://roku-data-warehouse/roku/dimensions/dim_experiment]

Table name in dev:
sbschema.roku_<table>
```


### Spark shell
 
 Invoke spark shell. Replace jar location
```
spark-shell --jars /tmp/pogupta/sr_cap/sr_cap-artifacts.jar --driver-memory 6G --executor-memory 6G --conf spark.dynamicAllocation.enabled=true --conf spark.dynamicAllocation.maxExecutors=60
```
 Sample code snippet 
```
import com.roku.dea.spark.sr_cap.SrCap2DataIngestApp
import com.roku.dea.spark.sr_cap.SrCapHelper
import com.roku.utils.run_modes.RunModes
val s3IngestPath = "s3://cap-data-886239521314/11f9ffc1b11a51a7ba2792269111d081"
val capSchema = SrCapHelper.getSrCap2Schema()
val rawDF = spark.sqlContext.read.schema(capSchema).json(s3IngestPath)
val validDF = rawDF.filter(SrCapHelper.validSearchContentTypesUDF($"type")).persist()
val runModeStr = "TEST"
val runMode: RunModes = RunModes.getMode(runModeStr)
val searchContentIngestApp = new SrCap2DataIngestApp(spark, runMode)
val episodeIndex = (spark.read.option("header", true).csv("s3://cap-data-meta-886239521314/types/episode/latest.csv")).persist()
val episodeDF = searchContentIngestApp.ingestEpisode(validDF, "", episodeIndex)
episodeDF.show(false)
```

### Build locally and scp to server
```
cd ~
source ide_virtual_env/bin/activate  

cd ~/CODE/GIT/data-processing
./pants lint binary src/main/python:roku-dag-bag

Copy to server
scp dist/roku-dag-bag.pex data-processing-dev-emr-5-21.bdp.roku.com:/tmp/mlubinsky/
or
scp dist/roku-dag-bag.pex 10.220.11.182:/tmp/mlubinsky/

This script does it:
cat c
------
./pants lint binary src/main/python:roku-dag-bag
status=$?
echo "status=$status"
[ $status -eq 0 ]  || exit 1
scp dist/roku-dag-bag.pex data-processing-dev-emr-5-21.bdp.roku.com:/tmp/mlubinsky/
-------
```


### Kafka

```
kafka-console-consumer --bootstrap-server kafka-dev-1.bdp.roku.com:9092,kafka-dev-2.bdp.roku.com:9092 --topic amoeba --from-beginning --max-messages 100
```

use this one in gobblin dev branch:
```
export KAFKA_BROKERS=kafka-dev-1.bdp.roku.com:9092,
                     kafka-dev-2.bdp.roku.com:9092
```

This one is consistent with prod
```
                     
export KAFKA_BROKERS=
             kafka-bootstrap-a.bdp.roku.com:9092,
             kafka-bootstrap-b.bdp.roku.com:9092,
             kafka-bootstrap-c.bdp.roku.com:9092
```

### Start Airflow DEV SERVER

```
ssh data-processing-dev-emr-5-21.bdp.roku.com

Observe that the airflow process usuallly looks like:
nohup airflow webserver -p ${PORT} --pid /tmp/airflow${PORT}.pid



Start Airflow on    free port (once)
cd /tmp/mlubinsky
sudo chpst -u airflow -e /etc/sv/airflow-service-env sh
source /opt/airflow/airflow-virtual-env/bin/activate

export PORT=2200
export PORT=2290
export PORT=2299
export PORT=2294
export PORT=2300

ps -ef | grep airflow | grep pid | grep $PORT

check what port is not in use:

lsof -i -P -n | grep LISTEN | grep $PORT
ls /tmp/airflow${PORT}.pid


export AIRFLOW__CORE__DAGS_FOLDER=/tmp/mlubinsky
touch /tmp/airflow${PORT}.pid   
nohup airflow webserver -p ${PORT} --pid /tmp/airflow${PORT}.pid & 
tail -f /home/airflow/nohup.out

http://data-processing-dev-emr-5-21.bdp.roku.com:${PORT}/admin/
```

### Run Airflow DEV DAG
```
schedule_interval='30 10 * * *',

schedule_interval='9 0,8 * * *’    “At minute 9 past hour 0 and 8.”


“Rendered” button shows the source code for the task - check it.

Make sure what the DAG  with the same name is not running, because 2 identical DAGS cannot run in parallel:

Browse -> Dug Runs > Search
Type DAG name, e.g.:  CON_ux_agg

http://data-processing-dev-emr-5-21.bdp.roku.com:2294/admin/dagrun/?search=CON_ux_agg

If there is running DAG then kill it before backfilling, 
 Go to Browse->Dag runs see the state for you dag

or you will get 
the message what max_active_runs for this DAG already achieved, waiting for completion

If dag is running  do not run backfill
You will have an error
[2020-01-30 21:09:50,662] {jobs.py:2539} INFO - max_active_runs limit for dag CON_search_agg has been reached  - waiting for other dag runs to finish
[2020-01-30 21:09:51,670] {jobs.py:2539} INFO - max_active_runs limit for dag CON_search_agg has been reached  - waiting for other dag runs to finish

Kill this process:
/opt/airflow/airflow-virtual-env/bin/python2.7 /opt/airflow/airflow-virtual-env/bin/airflow backfill --rerun_failed_tasks CON_search_agg -s 2020-01-15T09:14 -e 2020-01-15T09:14 -sd /tmp/mlubinsky/

Prepare backfill command

/Users/mlubinsky/CODE/GIT/data-processing/src/main/python/CON/CON_ux_agg/con_ux_agg_dag.py
 dag = dag_utils.create_dag(
      'CON_ux_agg', args=args, schedule_interval='9 0,8 * * *')


Use https://crontab.guru/ to populate backfill date

1) Mark all previous steps for the tested task in DAG as complete to speed up: 
2) Mark all downstream from parent node of tested task as “Mark Success”
3) Mark  “Clear” for Downstream/Recursive for the tested task

The following command run under my account (not Airflow!)

nohup sudo /opt/airflow/airflow backfill --rerun_failed_tasks  CON_ux_agg  -s 2020-01-12T08:09  -e 2020-01-12T08:09 -sd /tmp/mlubinsky/ &

nohup sudo /opt/airflow/airflow backfill --rerun_failed_tasks  CON_ux_agg  -s 2020-01-15T08:09  -e 2020-01-15T08:09 -sd /tmp/mlubinsky/ &

select date_key, count(*) from roku.fact_device_ux_logs
where event_type like 'cfui%'
group by date_key;

```
### SCP
```
export PYTHONPATH=.
https://stackoverflow.com/questions/338768/python-error-importerror-no-module-named

scp -r . mlubinsky@data-processing-dev-emr-5-21.bdp.roku.com:/home/mlubinsky/DEA-9486/python/utils/
scp dim_experiment.py mlubinsky@data-processing-dev-emr-5-21.bdp.roku.com:/home/mlubinsky/DEA-9486/python/dim/dim_hourly_non_partitioned/

```

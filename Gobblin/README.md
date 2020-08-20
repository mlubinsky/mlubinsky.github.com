## Documentation

https://gobblin.readthedocs.io/en/latest/

https://gobblin.apache.org/

## Gobblin  consumes data from Kafka Topics 

Gobblin  consumes data from Kafka Topics 
then organizes that data and writes it to S3 for long term storage and access via HUE, Hive, and other tools.

##  Scribe endpoint  

<https://confluence.portal.roku.com:8443/display/DEA/Adding+Scribe+Endpoint+and+Gobblin+Kafka+Consumer>

   
https://console.aws.amazon.com/sqs/v2/home?region=us-east-1#/queues/https%3A%2F%2Fsqs.us-east-1.amazonaws.com%2F911173767732%2Famoeba-bdp-prod  


### abf.job

https://jira.portal.roku.com:8443/browse/DEA-11280
   
https://gitlab.eng.roku.com/dea/GoblineConsumers/blob/master/external/jobconfig/abf/abf.job#L23   
```
cd ~/CODE/GIT

git clone git@gitlab.eng.roku.com:dea/scribe-api.git
cd scribe-api
```

##  GoblinConsumers   

<https://gitlab.eng.roku.com/dea/GoblineConsumers/>

```
git clone git@gitlab.eng.roku.com:dea/GoblineConsumers.git
cd GoblineConsumers
pwd
/Users/mlubinsky/CODE/GIT/GOBBLIN/GoblineConsumers
 
find . -name device.job
./src/test/resources/job/device/device.job
 
find . -name device_logs_v2.job
./external/jobconfig/device_logs_v2/device_logs_v2.job

```

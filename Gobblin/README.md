## Scribe
```
cd scribe-api/
./gradlew clean build

 (DEA-11300)$ pwd
/Users/mlubinsky/GIT/scribe-api/scribe-web/build/distributions
 (DEA-11300)$ ls
scribe-web-1.0-SNAPSHOT.tar scribe-web-1.0-SNAPSHOT.zip

rsync scribe-web-1.0-SNAPSHOT.tar mlubinsky@scribe-dev-1002.bdp.roku.com:/home/mlubinsky/
```

Error
```

com.roku.dea.util.FailedPropertyUtilTest > testFailedProperty[1] PASSED

> Task :scribe-service:test FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':scribe-service:test'.
> Process 'Gradle Test Executor 1' finished with non-zero exit value 1
  This problem might be caused by incorrect test process configuration.
  Please refer to the test execution section in the User Manual at https://docs.gradle.org/5.4.1/userguide/java_testing.html#sec:test_execution

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output. Run with --scan to get full insights.

* Get more help at https://help.gradle.org

Deprecated Gradle features were used in this build, making it incompatible with Gradle 6.0.
Use '--warning-mode all' to show the individual deprecation warnings.
See https://docs.gradle.org/5.4.1/userguide/command_line_interface.html#sec:command_line_warnings

```

## Gobblin

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

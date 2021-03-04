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

```
[mlubinsky@scribe-dev-1002 ~]$ 
sudo /usr/local/bin/getFromS3AndRun.sh scribe-server_DEA-11300_LATEST.rsei

Downloading [scribe-server_DEA-11300_LATEST.rsei] from S3...
download: s3://roku-dea-devops/rsei/scribe-server_DEA-11300_LATEST.rsei to ../../tmp/rsei/scribe-server_DEA-11300_LATEST.rsei
User [mlubinsky] is Running [scribe-server_DEA-11300_LATEST.rsei]...
Extracting Metadata from: scribe-server_DEA-11300_LATEST.rsei
scribe-server_DEA-11300_LATEST.rsei contains no installer metadata. Using defaults.
Extracting files into / ...
./
./rsei_tmp/
./rsei_tmp/user_crontabs/
./rsei_tmp/user_crontabs/roku
./etc/
./etc/dd-agent/
./etc/dd-agent/conf.d/
./etc/dd-agent/conf.d/kafka.yaml
./etc/dd-agent/conf.d/directory.yaml
./etc/sv/
./etc/sv/scribe-server/
./etc/sv/scribe-server/env/
./etc/sv/scribe-server/env/JAVA_HOME
./etc/sv/scribe-server/env/DATA_DOG_REPORT_SCHEDULE
./etc/sv/scribe-server/env/DATADOG_API_KEY
./etc/sv/scribe-server/env/JAVA_OPTS
./etc/sv/scribe-server/env/CSV_REPORT_SCHEDULE
./etc/sv/scribe-server/env/SCRIBE_WEB_PORT
./etc/sv/scribe-server/env/SCRIBE_JMX_OPTS
./etc/sv/scribe-server/env/JMX_PORT
./etc/sv/scribe-server/env/MONITORING_STRATEGY
./etc/sv/scribe-server/run
./etc/sv/scribe-server/log/
./etc/sv/scribe-server/log/run
./etc/sv/scribe-server/log/main/
./etc/sv/scribe-server/log/main/config
./etc/sv/scribe-server/log/main/.donotdelete
./etc/sv/scribe-server/conf/
./etc/sv/scribe-server/conf/service.yaml
./etc/sv/scribe-server/conf/application.properties
./opt/
./opt/scribe-web-906005/
./opt/scribe-web-906005/http2-server-9.3.9.M1.jar
./opt/scribe-web-906005/javax-websocket-server-impl-9.3.9.M1.jar
./opt/scribe-web-906005/websocket-common-9.3.9.M1.jar
./opt/scribe-web-906005/javax.annotation-api-1.2.jar
./opt/scribe-web-906005/jsr305-3.0.0.jar
./opt/scribe-web-906005/scribe-web-906005.jar
./opt/scribe-web-906005/jackson-databind-2.5.1.jar
./opt/scribe-web-906005/jetty-deploy-9.3.9.M1.jar
./opt/scribe-web-906005/jetty-security-9.3.9.M1.jar
./opt/scribe-web-906005/jetty-quickstart-9.3.9.M1.jar
./opt/scribe-web-906005/javax.transaction-api-1.2.jar
./opt/scribe-web-906005/jetty-util-9.3.9.M1.jar
./opt/scribe-web-906005/jetty-jaspi-9.3.9.M1.jar
./opt/scribe-web-906005/httpclient-4.3.6.jar
./opt/scribe-web-906005/scribe-service-906005.jar
./opt/scribe-web-906005/javax.mail.glassfish-1.4.1.v201005082020.jar
./opt/scribe-web-906005/jackson-datatype-jdk7-2.5.1.jar
./opt/scribe-web-906005/log4j2.xml
./opt/scribe-web-906005/s3FileCopier.sh
./opt/scribe-web-906005/asm-commons-5.0.1.jar
./opt/scribe-web-906005/dropwizard-jackson-0.8.1.jar
./opt/scribe-web-906005/slf4j-api-1.8.0-alpha2.jar
./opt/scribe-web-906005/jboss-logging-3.1.3.GA.jar
./opt/scribe-web-906005/http2-common-9.3.9.M1.jar
./opt/scribe-web-906005/jetty-servlet-9.3.9.M1.jar
./opt/scribe-web-906005/log4j-slf4j-impl-2.11.0.jar
./opt/scribe-web-906005/jetty-server-9.3.9.M1.jar
./opt/scribe-web-906005/log4j-api-2.11.0.jar
./opt/scribe-web-906005/jetty-xml-9.3.9.M1.jar
./opt/scribe-web-906005/zstd-jni-1.4.0-1.jar
./opt/scribe-web-906005/websocket-server-9.3.9.M1.jar
./opt/scribe-web-906005/websocket-api-9.3.9.M1.jar
./opt/scribe-web-906005/asm-5.0.1.jar
./opt/scribe-web-906005/dropwizard-util-0.8.1.jar
./opt/scribe-web-906005/protobuf-java-3.2.0.jar
./opt/scribe-web-906005/guava-19.0.jar
./opt/scribe-web-906005/javax.websocket-api-1.0.jar
./opt/scribe-web-906005/metrics-core-3.1.1.jar
./opt/scribe-web-906005/jackson-datatype-joda-2.5.1.jar
./opt/scribe-web-906005/jetty-webapp-9.3.9.M1.jar
./opt/scribe-web-906005/hibernate-validator-5.1.3.Final.jar
./opt/scribe-web-906005/jetty-http-9.3.9.M1.jar
./opt/scribe-web-906005/classmate-1.0.0.jar
./opt/scribe-web-906005/metrics-datadog-1.1.2.jar
./opt/scribe-web-906005/jetty-jndi-9.3.9.M1.jar
./opt/scribe-web-906005/jetty-io-9.3.9.M1.jar
./opt/scribe-web-906005/java-dogstatsd-client-2.0.9.jar
./opt/scribe-web-906005/commons-io-2.4.jar
./opt/scribe-web-906005/kafka-clients-2.3.0.jar
./opt/scribe-web-906005/javax.el-3.0.0.jar
./opt/scribe-web-906005/jackson-module-afterburner-2.5.1.jar
./opt/scribe-web-906005/jetty-servlets-9.3.9.M1.jar
./opt/scribe-web-906005/joda-time-2.7.jar
./opt/scribe-web-906005/http2-hpack-9.3.9.M1.jar
./opt/scribe-web-906005/snakeyaml-1.8.jar
./opt/scribe-web-906005/snappy-java-1.1.7.3.jar
./opt/scribe-web-906005/http2-client-9.3.9.M1.jar
./opt/scribe-web-906005/commons-lang3-3.4.jar
./opt/scribe-web-906005/validation-api-1.1.0.Final.jar
./opt/scribe-web-906005/jackson-core-2.5.1.jar
./opt/scribe-web-906005/javax.activation-1.1.0.v201105071233.jar
./opt/scribe-web-906005/jackson-annotations-2.5.0.jar
./opt/scribe-web-906005/javax.servlet-api-3.1.0.jar
./opt/scribe-web-906005/jetty-alpn-client-9.3.9.M1.jar
./opt/scribe-web-906005/jetty-client-9.3.9.M1.jar
./opt/scribe-web-906005/commons-codec-1.6.jar
./opt/scribe-web-906005/fluent-hc-4.3.6.jar
./opt/scribe-web-906005/commons-logging-1.1.3.jar
./opt/scribe-web-906005/httpcore-4.3.3.jar
./opt/scribe-web-906005/jetty-continuation-9.3.9.M1.jar
./opt/scribe-web-906005/dropwizard-metrics-datadog-1.1.2.jar
./opt/scribe-web-906005/jetty-annotations-9.3.9.M1.jar
./opt/scribe-web-906005/asm-tree-5.0.1.jar
./opt/scribe-web-906005/jetty-rewrite-9.3.9.M1.jar
./opt/scribe-web-906005/websocket-servlet-9.3.9.M1.jar
./opt/scribe-web-906005/dropwizard-metrics-0.8.1.jar
./opt/scribe-web-906005/dropwizard-validation-0.8.1.jar
./opt/scribe-web-906005/jetty-jmx-9.3.9.M1.jar
./opt/scribe-web-906005/javax-websocket-client-impl-9.3.9.M1.jar
./opt/scribe-web-906005/scribe-api.sh
./opt/scribe-web-906005/jackson-datatype-guava-2.5.1.jar
./opt/scribe-web-906005/javax.security.auth.message-1.0.0.v201108011116.jar
./opt/scribe-web-906005/log4j-core-2.11.0.jar
./opt/scribe-web-906005/websocket-client-9.3.9.M1.jar
./opt/scribe-web-906005/dropwizard-lifecycle-0.8.1.jar
./opt/scribe-web-906005/jetty-plus-9.3.9.M1.jar
./opt/scribe-web-906005/protobuf-java-format-1.4.jar
./opt/scribe-web-906005/lz4-java-1.6.0.jar
./opt/.donotdelete
Stopping scribe-sever. If it's not installed already an error may follow. That's okay.
fail: -w: unable to change to service directory: file does not exist
fail: 301: unable to change to service directory: file does not exist
timeout: run: scribe-server: (pid 18925) 691930s, want down, got TERM
Creating [roku] user and group...
groupadd: group 'roku' already exists
useradd: user 'roku' already exists
download: s3://roku-dea-devops/rpm/java/jdk-8u144-linux-x64.rpm to ../../tmp/jdk-8u144-linux-x64.rpm
	package jdk1.8.0_144-2000:1.8.0_144-fcs.x86_64 is already installed
Stopping Datadog Agent (using killproc on supervisord):    [  OK  ]
Starting Datadog Agent (using supervisord):                [  OK  ]
timeout: run: scribe-server: (pid 18925) 691946s, got TERM
Post Install Complete.
Finished
Done running [scribe-server_DEA-11300_LATEST.rsei].
```

Error on other Mac:
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

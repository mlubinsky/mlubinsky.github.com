## TLS MQTT 

<https://os.mbed.com/users/vpcola/code/HelloMQTT/>   Vergil Cola

<https://os.mbed.com/users/coisme/code/HelloMQTT/> Osamu
 
## Cloud
<https://cloud.mbed.com/docs/current/connecting/qs-credentials.html>  get mbed_cloud_dev_credentials.c

<https://cloud.mbed.com/docs/current/account-management/users.html>

<https://cloud.mbed.com/docs/current/connecting/qs-compiling.html>


<https://tedium.co/2018/06/07/acorn-arm-holdings-history/>  ARM history

## Cortex-A76
<https://www.anandtech.com/show/12785/arm-cortex-a76-cpu-unveiled-7nm-powerhouse>

<https://www.extremetech.com/computing/270550-are-arm-cpu-cores-finally-ready-to-fight-intel-for-the-laptop-market> 

## Trilllium
https://www.anandtech.com/show/12791/arm-details-project-trillium-mlp-architecture

## Rasberry
<https://www.macworld.co.uk/how-to/mac/how-to-set-up-raspberry-pi-3-with-mac-3637490/>

## Multithreading
https://os.mbed.com/docs/v5.8/reference/thread.html


## AWS
The solution deploys an AWS IoT rule that sends device data to Amazon Kinesis Data Firehose, which archives the data in Amazon S3 and sends it to an Amazon Kinesis Data Analytics application that computes metrics in real-time. The solution uses Amazon DynamoDB to durably store the computed data. The solution also features a customizable dashboard that visualizes your device connectivity and activity metrics in real-time. 
<https://aws.amazon.com/about-aws/whats-new/2018/05/introducing-real-time-iot-device-monitoring-with-kinesis-data-analytics/>

<https://aws.amazon.com/about-aws/whats-new/2016/01/aws-iot-now-supports-websockets-custom-keepalive-intervals-and-enhanced-console/>

<https://serverless.com/blog/realtime-updates-using-lambda-websockets-iot/>

<https://hackernoon.com/serverless-websockets-with-aws-lambda-fanout-15384bd30354>

<https://medium.com/signiant-engineering/real-time-aggregation-with-dynamodb-streams-f93547cfb244>

## Mosquitto

<https://mcuoneclipse.com/2017/04/14/enable-secure-communication-with-tls-and-the-mosquitto-broker/>

<https://dzone.com/articles/secure-tls-communication-with-mqtt-mbedtls-and-lwip-part-1>

<http://rockingdlabs.dunmire.org/exercises-experiments/ssl-client-certs-to-secure-mqtt>

<https://dzone.com/articles/mbedtls-ssl-certificate-verification-with-mosquitto-lwip-and-mqtt>

<https://dzone.com/articles/secure-communication-with-tls-and-the-mosquitto-broker>

<https://dzone.com/articles/mqtt-security-securing-a-mosquitto-server>

 brew install mosquitto
 
 mosquitto has been installed with a default configuration file.
 You can make changes to the configuration by editing:
    /usr/local/etc/mosquitto/mosquitto.conf

To have launchd start mosquitto now and restart at login:
  brew services start mosquitto

Or, if you don't want/need a background service you can just run:
  mosquitto -v -c /usr/local/etc/mosquitto/mosquitto.conf   

openssl s_client -connect localhost:8883  

mosquitto_pub

## Stack Overflow

openssl s_client -showcerts -connect iot.eclipse.org:8883

<https://stackoverflow.com/questions/39435311/ca-certificate-to-connect-to-mqtt-server-over-tls-iot-eclipse-org>

## 2-ways auth
<https://tls.mbed.org/discussions/generic/get-the-private-key>

<https://tls.mbed.org/discussions/generic/ssl-handshake-failed-due-to-mbedtls_err_x509_cert_verify_failed>

<https://tls.mbed.org/discussions/crypto-and-ssl/reading-public-private-key-from-certificate>

<https://tls.mbed.org/discussions/crypto-and-ssl/how-to-send-self-signed-ca-certificate-to-server-from-mbedtls-client>

cat deviceCert.crt sampleCACertificate.pem > deviceCertAndCACert.crt
And then set it as the device certificate using mbedtls_ssl_conf_own_cert()

<https://github.com/ARMmbed/mbedtls>

<https://docs.mbed.com/docs/mbed-os-api-ref/en/latest/APIs/security/tls/>

<https://github.com/ARMmbed/mbedtls/blob/development/programs/ssl/ssl_client2.c>

<https://cloud.mbed.com/docs/v1.2/quick-start/qs-compiling.html>

<https://tls.mbed.org/high-level-design>

<https://tls.mbed.org/dev-corner>

<https://os.mbed.com/docs/v5.8/reference/security.html>

<https://tls.mbed.org>

<https://tls.mbed.org/kb>


## Wikipedia

<https://en.wikipedia.org/wiki/Public_key_certificate>

<https://en.wikipedia.org/wiki/Certificate_authority>

<https://en.wikipedia.org/wiki/Public_key_infrastructure>

<https://en.wikipedia.org/wiki/Transport_Layer_Security>

## MBED 

<https://phodal.github.io/awesome-iot/>

<https://os.mbed.com/docs/v5.8>  mbed OS 5.8 documentation

<https://www.mbed.com/en/platform/>  Mbed IoT

<https://www.youtube.com/watch?v=bY2QN-5BTCg>

<https://www.youtube.com/watch?v=LQn5-2caSZY> .  mbed OS overview

<http://infocenter.arm.com/help/index.jsp>

<https://nodered.org/blog/2018/03/13/project-updates>    Node-Red

<https://cloud.mbed.com/>

<http://eprints.gla.ac.uk/157277/1/157277.pdf>

<https://github.com/ARMmbed/easy-connect>

<https://www.hackster.io/search?i=projects&q=mbed>



<https://www.youtube.com/playlist?list=PLJEYfuHbcEIApuZR4L5tRiBCwTZCYeTNY> russian lectures

<https://libraries.io/search?q=mbed>   Github projects

## Integration platform
<https://thingsboard.io/>

<https://www.blynk.cc/>

<https://www.cumulocity.com/>

<https://www.losant.com/>

<https://thingspeak.com/>

<http://freeboard.io/>

<https://beebotte.com/>

<http://www.sitewhere.org/>

<http://www.thingstud.io/>

<https://opensensemap.org>

<https://io.adafruit.com/>

## Compilers
https://os.mbed.com/docs/latest/tools/index.html

## Mbed Simulator

<https://os.mbed.com/blog/entry/introducing-mbed-simulator/>

## Configuration
<https://os.mbed.com/docs/v5.8/reference/configuration.html>

<https://docs.mbed.com/docs/mbed-os-handbook/en/5.2/advanced/config_system/>

## Online compiler

<https://os.mbed.com/compiler>

<https://github.com/ARMmbed/Handbook/blob/new_engine/docs/tutorials/using_tools/oc_tut.md>

<https://github.com/ARMmbed/Handbook/blob/new_engine/docs/tutorials/quickstart/quick-start-compiler.md>

<https://www.youtube.com/watch?v=fnMwvUL-8KQ>


## GNU toolchain for ARM

<https://developer.arm.com/open-source/gnu-toolchain>

<https://www.linaro.org/downloads/>

Download GNU toolchain for ARM:

<https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads>

or  <https://github.com/ARMmbed/homebrew-formulae> 

    brew tap ArmMbed/homebrew-formulae
    brew install arm-none-eabi-gcc

 
or  <https://github.com/osx-cross/homebrew-arm>    GNU toolchain for ARM Cortex-M and Cortex-R

    brew tap osx-cross/arm
    brew install arm-gcc-bin

## MBED-CLI 

<https://docs.mbed.com/docs/mbed-os-handbook/en/latest/dev_tools/cli/>

 

Updating mbed OS

If you still have the mbed library (not mbed-os) in the online compiler, right click on 'mbed', and click 'Remove'. Then click on 'Add library' > 'From URL' and enter https://github.com/armmbed/mbed-os.

If you have mbed-os, right click on the library and select 'Upgrade'.

From mbed CLI:

    $ mbed remove mbed
    $ mbed add mbed-os

Or when you already have mbed-os:

    $ cd mbed-os
    $ git pull
    $ git checkout latest

 There is a difference between the online and CLI tools.  
 The CLI tools automatically pull in the latest mbed libraries 
 while the online tools will only pull newer libraries when you specifically update them.

 mbed import https://github.com/ARMmbed/mbed-os-example-blinky

 $ pwd      --> /Users/miclub01/NEW/mbed-os-example-blinky

    mbed config -G GCC_ARM_PATH "/Users/miclub01/gcc-arm-none-eabi-7-2017-q4-major/bin"

    mbed config --list

    GCC_ARM_PATH=/Users/miclub01/gcc-arm-none-eabi-7-2017-q4-major/bin 

    mbed compile -t GCC_ARM -m K64F
    
    mbed ls .     <--  dependency

Image: ./BUILD/K64F/GCC_ARM/mbed-os-example-blinky.bin
 
 
http://devblog.exmachina.fr/tutorial/2016/12/08/LPC1768-development-toolkit

<https://petewarden.com/2018/01/29/how-to-compile-for-arm-m-series-chips-from-the-command-line/>

<https://habr.com/company/efo/blog/277491/>  Overview of ARM devices

<https://github.com/ARMmbed/mbed-cli>  

<https://habr.com/post/307806/>   how to install cli

    pip install mbed-cli

<https://www.youtube.com/watch?v=PI1Kq9RSN_Y> . Quick start

<http://grbd.github.io/posts/2016/11/06/using-the-mbed-cli/>

<https://habr.com/company/efo/blog/308440/>  6 articles how to program for mbed

<https://www.youtube.com/watch?v=cM0dFoTuU14>


<https://stackoverflow.com/questions/44640547/mbed-cli-make-py-error-could-not-find-executable-for-arm>

    mbed config -G GCC_ARM_PATH "/Users/amod-mac/Desktop/gcc-arm-none-eabi-7-2017-q4-major/bin"
    mbed compile -m UBLOX_C027 -t ARM    <-- commercial compiler
    mbed compile -m UBLOX_C027 -t GCC_ARM   <-- GCC compiler


## MQTT
<https://github.com/hobbyquaker/awesome-mqtt>

<http://mqtt.org/documentation>

<https://www.hivemq.com/>

<https://www.hivemq.com/mqtt-toolbox>

<https://www.reddit.com/r/MQTT/>

<http://workswithweb.com/mqttbox.html>   load test

## Python


<http://www.steves-internet-guide.com/category/mqtt/>

<http://www.steves-internet-guide.com/python-mqtt-publish-subscribe/>

<https://github.com/eclipse/paho.mqtt-spy>   Java 
 
<http://test.mosquitto.org/>
 
<https://medium.com/@erinus/mosquitto-paho-mqtt-python-29cadb6f8f5c>   Python

<https://techtutorialsx.com/2017/04/23/python-subscribing-to-mqtt-topic/>


## MQTT Mbed

<https://github.com/ARMmbed/easy-connect>

<https://os.mbed.com/teams/mqtt/code/HelloMQTT/>

<https://os.mbed.com/search/repository?q=HelloMQTT>

<https://mcuoneclipse.com/2017/04/09/mqtt-with-lwip-and-nxp-frdm-k64f-board/>

<https://www.element14.com/community/blogs/JimFlynn/2018/04/24/an-updated-mqtt-client-solution-using-c-templates>


<https://os.mbed.com/blog/entry/Using-HTTP-HTTPS-MQTT-and-CoAP-from-mbed/>


<https://github.com/ARMmbed?utf8=%E2%9C%93&q=connector&type=&language=>

<https://os.mbed.com/search/?q=MQTT>



<http://www.eclipse.org/paho/clients/c/embedded/>   Paho MQTT

<https://www.youtube.com/watch?v=QAaXNt0oqSI>   Paho MQTT

http://www.eclipse.org/paho/clients/c/embedded/    Paho MQTT Paho MQQT

<https://www.hivemq.com/blog/mqtt-client-library-encyclopedia-paho-embedded>



<https://www.wolfssl.com/mqtt-with-wolfssl/>

<https://console.bluemix.net/docs/services/IoT/devices/libraries/mbedcpp.html#mbedcpp>

<https://blog.feabhas.com/2012/04/iot-mqtt-publish-and-subscriber-c-code/>



## Security: TTL SSL


<https://habr.com/post/346798/>   X509

<https://habr.com/post/352722/> .  how to create SSL cert

Первая и основная функция сертификатов X.509 — служить хранилищем открытого или публичного ключа PKI 
(public key infrastructure). 

Вторая функция сертификатов X.509 заключается в том, чтобы предъявитель сего был принят человеком, либо программой 
в качестве истинного владельца некоего цифрового актива: доменного имени, веб сайта и пр. 

RSA (буквенная аббревиатура от фамилий Rivest-Shamir-Adleman) – это криптографический алгоритм с открытым ключом. Это значит, что системой генерируется два разных ключа – открытый и секретный. 
Открытый ключ передается по открытому (незащищенному) каналу, и используется для зашифровки данных.
Секретный же ключ хранится только у владельца, и используется для расшифровки любых данных, зашифрованных открытым ключом.
Таким образом, мы можем передавать открытый ключ кому угодно, и получать зашифрованные этим ключом сообщения, расшифровать которые можем только мы (с использованием секретного ключа).

<https://os.mbed.com/search/repository?q=HelloMQTT> .  useful code


    security find-identity -v login.keychain

    openssl x509 -noout -startdate -in cert.pem // Feb 27 07:13:41 2016 GMT

    openssl x509 -noout -enddate -in cert.pem // Feb 26 07:13:41 2017 GMT

<https://medium.com/@yasithlokuge/mqtt-protocol-and-security-48cf2dcd2c4d> 

<https://medium.com/@erinus/mosquitto-paho-mqtt-python-29cadb6f8f5c>

<https://mcuoneclipse.com/2017/04/14/introduction-to-security-and-tls-transport-security-layer/>

<https://mcuoneclipse.com/2017/04/17/tutorial-secure-tls-communication-with-mqtt-using-mbedtls-on-top-of-lwip/>

<https://www.youtube.com/watch?v=1RPntz5gfcA> . Securing IoT Applications with Mbed TLS (Part I)

<https://www.youtube.com/watch?v=iH4v-aXQ2zQ>  Securing IoT Applications with Mbed TLS (Part II)

 
## AWS

https://iot.stackexchange.com/questions/2036/connect-webpage-to-aws-iot-to-publish-messages
https://medium.com/@jparreira/receiving-aws-iot-messages-in-your-browser-using-websockets-9b87f28c2357
<https://docs.mbed.com/docs/mbed-device-connector-web-interfaces/en/latest/cloud_amazon/>
 
<https://aws.amazon.com/blogs/iot/how-to-bridge-mosquitto-mqtt-broker-to-aws-iot/>   AWS Mosqitto IoT integration 

## IBM Watson Iot integration

<https://www.youtube.com/watch?v=xa5U5dipdMY>
 
<https://blog.mbed.com/post/arm-ibm-simplify-iot-data-analytics>   

<https://www.reddit.com/r/ECE/comments/6v2a1o/i_made_a_video_on_how_to_get_started_with_mqtt_on/>

<https://www.youtube.com/watch?v=lF4iuaMkSKQ>  ARM mbed IoT Starter Kit on IBM's Bluemix cloud platform 

## Docker

https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=0&q=mbed-cli&starCount=0

## IDE

<https://habr.com/post/358682/>    platformIO

В процессе установки platformIO разворачивает локальный репозиторий arm mbed (и не только его) 
по пути $HOME/.platformio/packages. 

<https://medium.com/@zlt1213/develop-stm32f4-discovery-cortex-m4-with-eclipse-on-mac-os-part-2-d803f69592f4>  Eclipse

<https://medium.com/jumperiot/nrf52-development-with-clion-2981e100a656>  CLion

<https://blog.jetbrains.com/clion/2017/12/clion-for-embedded-development-part-ii/>   CLion

<https://medium.com/jumperiot/debuggers-for-embedded-how-to-choose-the-right-debugger-a727b33b4061>  Debuggers

## Plotting 

<https://itnext.io/javascript-real-time-visualization-of-high-frequency-streams-d6533c774794>

<https://github.com/matbor/mqtt2highcharts>

https://bergie.iki.fi/blog/nasa-openmct-iot-dashboard/

<https://www.open-electronics.org/guest_projects/real-time-data-plotting-of-iot-sensor-using-python/>

<https://hackaday.com/2017/10/31/review-iot-data-logging-services-with-mqtt/>

<https://github.com/bboser/iot-plot>

<https://tinker.yeoman.com.au/2015/05/11/simple-browser-based-graphical-display-of-mqtt-data/>

<https://zoetrope.io/tech-blog/simple-mqtt-iot-logging/>

<https://thingsboard.io/>

## Unsorted

<https://vox.arm.com/>

<https://blog.benjamin-cabe.com/2017/12/08/cloud-native-iot-development-in-practice> 

<https://habr.com/post/189484/>   ARM for kids 1

<https://habr.com/post/191058/>  ARM for kids 3

<https://habr.com/post/194816/> ARM for kids 4

## Microsoft 

<https://habr.com/company/microsoft/blog/323200/>   Microsoft Azure IoT

<https://docs.microsoft.com/en-us/azure/iot-hub/iot-hub-mqtt-support>


Not all small IoT devices support IP but instead support protocols such as Bluetooth Low Energy (BLE) and LoRaWAN, which are cheap and energy-efficient but do not allow direct access to the internet.

CoAP protocol <http://coap.technology/> - The Constrained Application Protocol (CoAP) is a lightweight web protocol for IoT devices. It's similar to HTTP, but with a much lower footprint and additional features like multicast. mbed Device Connector, our device management solution, uses it as its transport layer - we therefore ship a CoAP library as part of mbed OS 5. We can use this library - which includes both a CoAP serializer and parser - to connect to any CoAP server.

https://os.mbed.com/blog/entry/Connecting-BLE-devices-to-the-cloud/ 

<https://os.mbed.com/blog/entry/streaming-data-cows-dsa2017/>

<https://medium.com/@teebr/iot-with-an-esp32-influxdb-and-grafana-54abc9575fb2>

<https://imc.signify.net/mysignify/Default.asp> . VPN


## Ethernet TCP/IP FRDM-K64F 

curl ipecho.net/plain ; echo

https://www.nxp.com/products/processors-and-microcontrollers/arm-based-processors-and-mcus/kinetis-cortex-m-mcus/k-seriesperformancem4/k2x-usb/freedom-development-platform-for-kinetis-k64-k63-and-k24-mcus:FRDM-K64F

<https://stackoverflow.com/questions/42158817/mbed-ethernet-interface-not-working>


    cp HelloMQTT_K64F.bin /Volumes/DAPLINK/
 
    minicom -D /dev/tty.usbmodem14412
 
TODO:  use NetworkInterface 
 
##      Code 

    #include "mbed.h"
    #define PRINT pc.printf

    Serial pc(USBTX, USBRX);
    pc.baud(115200);
    PRINT("Hello");




    #include "mbed.h"
    #include "EthernetInterface.h"
    Serial pc(USBTX, USBRX);      
    EthernetInterface eth;
    DigitalOut led1(LED1);
    // https://docs.mbed.com/docs/mbed-os-api-ref/en/latest/APIs/communication/ethernet/
    // https://github.com/ARMmbed/mbed-os-example-sockets/blob/master/main.cpp 

    // main() runs in its own thread in the OS
    int main() {
      int err1=0;
      int err2=0;
    
      //setup ethernet interface
      //err1 = eth.init(); //Use DHCP -- is it required???
      //NetworkInterface* network_interface = eth.connect(); // network_interface will be NULLPTR when connection fails
      err2 = eth.connect();
    
    //if (network_interface) {
       //err2 = eth.connect();
       const char *ip =   (err2 == 0) ? eth.get_ip_address()  : " ERROR1" ;
       const char *mac = (err2 == 0) ? eth.get_mac_address() : " ERROR2" ;
       //const char* ip = network_interface->get_ip_address();
 
    while (true) {
        led1 = !led1;
        wait(0.5);
        if ( err1==0 && err2 == 0){
           pc.printf("SUCCESS  \n\r");
           pc.printf("IP AGAIN address is: %s\n", ip ? ip : "No IP");
           pc.printf("MAC address is: %s\n", mac ? mac : "No MAC");    
           
        }   
        else
          pc.printf("ERRR  \n\r");
        
    }
    }
        
    }
    }

## DLMS

<https://www.dlms.com/documentation/index.html>

<https://docs.mbed.com/docs/mbed-os-api-ref/en/latest/APIs/communication/ethernet/>

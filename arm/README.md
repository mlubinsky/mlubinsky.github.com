<https://phodal.github.io/awesome-iot/>

<https://os.mbed.com/docs/v5.8>  mbed OS 5.8 documentation

<https://www.mbed.com/en/platform/>  Mbed IoT

<https://www.youtube.com/watch?v=bY2QN-5BTCg>

<https://www.youtube.com/watch?v=LQn5-2caSZY> .  mbed OS overview

<http://infocenter.arm.com/help/index.jsp>

<https://cloud.mbed.com/>

<http://eprints.gla.ac.uk/157277/1/157277.pdf>

<https://github.com/ARMmbed/easy-connect>

<https://www.hackster.io/search?i=projects&q=mbed>

<https://www.blynk.cc/>


## Compilers
https://os.mbed.com/docs/latest/tools/index.html

## Mbed Simulator

<https://os.mbed.com/blog/entry/introducing-mbed-simulator/>

## Online compiler

<https://os.mbed.com/compiler>

<https://github.com/ARMmbed/Handbook/blob/new_engine/docs/tutorials/using_tools/oc_tut.md>

<https://github.com/ARMmbed/Handbook/blob/new_engine/docs/tutorials/quickstart/quick-start-compiler.md>

<https://www.youtube.com/watch?v=fnMwvUL-8KQ>

## GNU toolchain for ARM

<https://developer.arm.com/open-source/gnu-toolchain>

Download GNU toolchain for ARM:

<https://developer.arm.com/open-source/gnu-toolchain/gnu-rm/downloads>

or  <https://github.com/ARMmbed/homebrew-formulae> 

    brew tap ArmMbed/homebrew-formulae
    brew install arm-none-eabi-gcc

 
or  <https://github.com/osx-cross/homebrew-arm>    GNU toolchain for ARM Cortex-M and Cortex-R

    brew tap osx-cross/arm
    brew install arm-gcc-bin

## MBED-CLI 
 There is a difference between the online and CLI tools.  
 The CLI tools automatically pull in the latest mbed libraries 
 while the online tools will only pull newer libraries when you specifically update them.

 mbed import https://github.com/ARMmbed/mbed-os-example-blinky

 pwd
  
  /Users/miclub01/NEW/mbed-os-example-blinky

 mbed config -G GCC_ARM_PATH "/Users/miclub01/gcc-arm-none-eabi-7-2017-q4-major/bin"
 
 mbed compile -t GCC_ARM -m K64F

Image: ./BUILD/K64F/GCC_ARM/mbed-os-example-blinky.bin
 
 cp HelloMQTT_K64F.bin /Volumes/DAPLINK/
 
 minicom -D /dev/tty.usbmodem14412
 
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

## Unsorted

<https://blog.benjamin-cabe.com/2017/12/08/cloud-native-iot-development-in-practice>



<https://tinker.yeoman.com.au/2015/05/11/simple-browser-based-graphical-display-of-mqtt-data/>

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




#include "mbed.h"
#include "EthernetInterface.h"

DigitalOut led1(LED1);

// main() runs in its own thread in the OS
int main() {
    int err1=0;
    int err2=0;
    
    //setup ethernet interface
    err1 = eth.init(); //Use DHCP
    if (err1 == 0)
       err2 = eth.connect();
    
    while (true) {
        led1 = !led1;
        wait(0.5);
        if ( err1 ==0  && err2 == 0)
           printf("IP Address is %s\n\r", eth.getIPAddress());
        else
          printf("err1=%d  err2=%d  \n\r", err1,err2);
        
    }
}

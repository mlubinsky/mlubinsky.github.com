<http://infocenter.arm.com/help/index.jsp>

<https://developer.arm.com/open-source/gnu-toolchain>

<https://cloud.mbed.com/>

<https://github.com/ARMmbed/easy-connect>

<https://www.hackster.io/search?i=projects&q=mbed>

<https://www.blynk.cc/>


## Compilers
https://os.mbed.com/docs/latest/tools/index.html

## Online compiler

<https://os.mbed.com/compiler>

<https://github.com/ARMmbed/Handbook/blob/new_engine/docs/tutorials/using_tools/oc_tut.md>

<https://github.com/ARMmbed/Handbook/blob/new_engine/docs/tutorials/quickstart/quick-start-compiler.md>

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
 
http://devblog.exmachina.fr/tutorial/2016/12/08/LPC1768-development-toolkit

<https://petewarden.com/2018/01/29/how-to-compile-for-arm-m-series-chips-from-the-command-line/>

<https://habr.com/company/efo/blog/277491/>  Overview of ARM devices

<https://github.com/ARMmbed/mbed-cli>  

<https://habr.com/post/307806/>   how to install cli

pip install mbed-cli

<http://grbd.github.io/posts/2016/11/06/using-the-mbed-cli/>

<https://habr.com/company/efo/blog/308440/>  6 articles how to program for mbed

<https://www.youtube.com/watch?v=cM0dFoTuU14>


<https://stackoverflow.com/questions/44640547/mbed-cli-make-py-error-could-not-find-executable-for-arm>

mbed config -G GCC_ARM_PATH "/Users/amod-mac/Desktop/gcc-arm-none-eabi-7-2017-q4-major/bin"

mbed compile -m UBLOX_C027 -t ARM    <-- commercial compiler
mbed compile -m UBLOX_C027 -t GCC_ARM   <-- GCC compiler


## MQTT

<https://os.mbed.com/blog/entry/Using-HTTP-HTTPS-MQTT-and-CoAP-from-mbed/>

<https://github.com/ARMmbed/connector-bridge-container-mqtt-getstarted>

<https://github.com/ARMmbed/connector-bridge-container-mqtt>

<https://github.com/ARMmbed/connector-bridge-container-awsiot>

<https://github.com/ARMmbed/connector-bridge-container-google>

<https://github.com/ARMmbed?utf8=%E2%9C%93&q=connector&type=&language=>

<https://os.mbed.com/search/?q=MQTT>

<https://os.mbed.com/teams/mqtt/code/HelloMQTT/>

http://www.eclipse.org/paho/clients/c/embedded/    Paho MQTT

<https://www.hivemq.com/blog/mqtt-client-library-encyclopedia-paho-embedded>

<https://www.wolfssl.com/mqtt-with-wolfssl/>

<https://console.bluemix.net/docs/services/IoT/devices/libraries/mbedcpp.html#mbedcpp>

<https://blog.feabhas.com/2012/04/iot-mqtt-publish-and-subscriber-c-code/>
 
## AWS

<https://docs.mbed.com/docs/mbed-device-connector-web-interfaces/en/latest/cloud_amazon/>
 
<https://aws.amazon.com/blogs/iot/how-to-bridge-mosquitto-mqtt-broker-to-aws-iot/>   AWS Mosqitto IoT integration 
 
<https://blog.mbed.com/post/arm-ibm-simplify-iot-data-analytics>   IBM Watson Iot integration

<https://www.reddit.com/r/ECE/comments/6v2a1o/i_made_a_video_on_how_to_get_started_with_mqtt_on/>

## Docker

https://hub.docker.com/search/?isAutomated=0&isOfficial=0&page=1&pullCount=0&q=mbed-cli&starCount=0

## IDE

<https://habr.com/post/358682/>    platformIO

В процессе установки platformIO разворачивает локальный репозиторий arm mbed (и не только его) 
по пути $HOME/.platformio/packages. 

<https://medium.com/@zlt1213/develop-stm32f4-discovery-cortex-m4-with-eclipse-on-mac-os-part-2-d803f69592f4>  Eclipse

<https://medium.com/jumperiot/nrf52-development-with-clion-2981e100a656>  CLion

https://blog.jetbrains.com/clion/2017/12/clion-for-embedded-development-part-ii/   CLion

<https://medium.com/jumperiot/debuggers-for-embedded-how-to-choose-the-right-debugger-a727b33b4061>  Debuggers

## Unsorted

<https://habr.com/post/189484/>   ARM for kids 1

<https://habr.com/post/191058/>  ARM for kids 3

<https://habr.com/post/194816/> ARM for kids 4

<https://habr.com/company/microsoft/blog/323200/>   Microsoft Azure IoT

Not all small IoT devices support IP but instead support protocols such as Bluetooth Low Energy (BLE) and LoRaWAN, which are cheap and energy-efficient but do not allow direct access to the internet.

CoAP protocol <http://coap.technology/> - The Constrained Application Protocol (CoAP) is a lightweight web protocol for IoT devices. It's similar to HTTP, but with a much lower footprint and additional features like multicast. mbed Device Connector, our device management solution, uses it as its transport layer - we therefore ship a CoAP library as part of mbed OS 5. We can use this library - which includes both a CoAP serializer and parser - to connect to any CoAP server.

https://os.mbed.com/blog/entry/Connecting-BLE-devices-to-the-cloud/ 

<https://os.mbed.com/blog/entry/streaming-data-cows-dsa2017/>

<https://medium.com/@teebr/iot-with-an-esp32-influxdb-and-grafana-54abc9575fb2>

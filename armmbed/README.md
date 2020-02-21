## Forum
<https://forums.mbed.com/>

<https://os.mbed.com/docs/mbed-os/v5.15/tools/index.html>

## Pelion Device Management

<https://www.pelion.com/docs/device-management/current/provisioning-process/provisioning-development-devices.html>

<https://www.pelion.com/docs/device-management/current/connecting/tutorial-pelion-mbedos.html>

<https://www.pelion.com/docs/device-management/current/welcome/index.html>

<https://www.pelion.com/docs/device-management/current/connecting/mbed-os.html>

<https://portal.mbedcloud.com/devices/list>

<https://os.mbed.com/teams/mbed-os-examples/code/mbed-os-example-pelion/> . (Feb 5 2020)

<https://www.pelion.com/docs/device-management/current/connecting/device-management-client-tutorials.html>

<https://github.com/ARMmbed/mbed-cloud-client>

<https://github.com/ARMmbed/mbed-cloud-client-example>

<https://www.pelion.com/docs/device-management/current/connecting/mbed-os.html>
 
To work with the Device Management Client example application, you need:

* A supported board with a network connection and an SD card attached.
* Serial connection to your device with open terminal connection (baud rate 115200, 8N1).
* Arm Mbed CLI installed. See installation instructions.
* Make sure that all the Python components are in par with the pip package requirements.txt list from Mbed OS.
* An API key (with Administrators group privilages) for your Device Management account.
* Updated DAPLink software (version 250 or later), if your board uses DAPLink.

<https://os.mbed.com/pelion-free-tier/>

### Bootloader
<https://github.com/ARMmbed/mbed-bootloader/>

<https://docs.mbed.com/docs/mbed-os-handbook/en/latest/advanced/bootloader/> Bootloader


### Pelion Certificates

<https://www.pelion.com/docs/device-management/current/provisioning-process/certificates-and-certificate-authorities.html>

#### Clone the embedded application's GitHub repository to your local computer and navigate to the new folder:

<https://github.com/ARMmbed/mbed-cloud-client-example>

```
mbed import https://github.com/ARMmbed/mbed-cloud-client-example
cd mbed-cloud-client-example
```
#### Configure Mbed CLI to use your Device Management account and board:
```
mbed config -G CLOUD_SDK_API_KEY <API_KEY>
mbed target <MCU>
mbed toolchain GCC_ARM
```
#### Use Mbed CLI to download a developer certificate and to create an update-related configuration for your device
mbed device-management init -d arm.com --model-name example-app --force -q

#### Compile

<https://www.pelion.com/docs/device-management/current/connecting/tutorial-pelion-mbedos.html>

<https://www.pelion.com/docs/device-management/current/connecting/device-management-client-tutorials.html>

<https://www.pelion.com/docs/device-management/current/release-notes/device-management-client.html>
 
 <https://www.pelion.com/docs/device-management/current/release-notes/device-management-client-lite.html>

## Send Data To Server

<https://os.mbed.com/blog/entry/Using-HTTP-HTTPS-MQTT-and-CoAP-from-mbed/>

<https://os.mbed.com/teams/sandbox/code/http-example/> . (15 Feb 2017)

<https://os.mbed.com/teams/sandbox/code/mbed-http/docs/tip/classHttpRequest.html>

*   WiFi  
*   Ethernet  
*  Bluetooth  

## TreasureData

<https://os.mbed.com/docs/mbed-os/v5.15/mbed-os-pelion/send-data-securely-to-arm-treasure-data.html>

https://github.com/ARMmbed/mbed-cli-osx-installer/

## Austin Blackstone 
<http://austinblackstoneengineering.com/how-to-send-data-from-mbed-os-to-treasure-data-pelion-data/>

<https://github.com/BlackstoneEngineering/aiot-workshop>

<https://os.mbed.com/platforms/ST-Nucleo-H743ZI2/> Pelion Device Ready  

<https://github.com/BlackstoneEngineering/aiot-workshop/blob/master/mbed_app.json>.  has this
```
"NUCLEO_H743ZI2": {
            "target.network-default-interface-type"     : "ETHERNET",
            "target.bootloader_img"                     : "tools/mbed-bootloader-nucleo_h743-internal-no-rot.bin",
```

```
Mbed Bootloader
No Update image
[DBG ] Active firmware up-to-date
booting...
Hello ...
Start Device Management Client
Using hardcoded Root of Trust, not suitable for production use.
Starting developer flow
Developer credentials already exist, continuing..
Application ready. Build at: Feb 21 2020 10:38:16
Mbed OS version 99.99.99
mcc_platform_interface_connect()
Connecting with interface: Ethernet
NSAPI_STATUS_CONNECTING
NSAPI_STATUS_GLOBAL_UP
IP: 192.168.1.5
Network initialized, registering...
Client registered
Endpoint Name: 01706912e912000000000001001b776d
Device Id: 01706912e912000000000001001b776d
temp:0.0000,humidity:0.0000,pressure:0.0000
temp:0.0000,humidity:480000000.0000,pressure:2.0000
temp:0.0000,humidity:480000000.0000,pressure:2.0000
temp:0.0000,humidity:480000000.0000,pressure:2.0000
```

Takuya Kitazawa (a.k.a. takuti) is an engineer working on machine learning, data science, and product development at Arm Treasure Data. 

<https://github.com/takuti/mbed-os-example-treasure-data>


<https://takuti.me/note/mbed-simulator-td/>

<https://support.treasuredata.com/hc/en-us/articles/360012567313-Data-Ingestion-from-Mbed-OS-HTTP-over-Wi-Fi->

<https://support.treasuredata.com/hc/en-us/articles/360034799633-Data-Ingestion-Using-the-Treasure-Data-MQTT-Broker-Experimental>

HTTPS library - Send data directly to the Treasure Data REST API.

Fluentd using fluent logger library - Send data to a hosted Fluentd instance that aggregates and forwards the data on to your treasure data account.

#### ST-Discovery-F413H

 
<https://os.mbed.com/platforms/ST-Discovery-F413H/>. Pelion Device Ready

<https://ide.mbed.com/compiler/#nav:/mbed-os-example-wifi-DISCO/main.cpp;>

<https://os.mbed.com/guides/connect-device-to-pelion/1/?board=ST-Discovery-F413H> .     Pelion

<https://ide.mbed.com/compiler/#nav:/pelion-example-common/mbed_app.json;>

```
"DISCO_F413ZH": {
      "target.network-default-interface-type"     : "WIFI", 
      "target.bootloader_img"                     : "bootloader/mbed-bootloader-DISCO_F413ZH.bin",

```

## Mbed Studio IDE

<https://os.mbed.com/studio/> michael.lybins@a Vanti..7!

## Mbed CLI

<https://os.mbed.com/docs/mbed-os/v5.15/tools/manual-installation.html>

<https://os.mbed.com/docs/mbed-os/v5.15/tools/working-with-mbed-cli.html>

<https://github.com/ARMmbed/mbed-cli-osx-installer/>
``
mbed new .  // will create file .med  and folder mbed-os
mbed add https://github.com/ARMmbed/mbed-cloud-client
```
## Mbed in Docker

<https://hub.docker.com/r/mbedos/mbed-os-env> official docker from ARM


### COM port apps

#### screen
```
 ls /dev/tty.usb* 
 screen /dev/tty.board_name 115200
``` 
#### CoolTerm

http://freeware.the-meiers.org/

https://learn.sparkfun.com/tutorials/terminal-basics/coolterm-windows-mac-linux

#### Cornflake
http://tomgerhardt.com/Cornflake/

#### minicom
```
 brew install minicom
 ls /dev/tty.usb*      # find the tty name
 minicom -D /dev/tty.usbmodem14412
``` 

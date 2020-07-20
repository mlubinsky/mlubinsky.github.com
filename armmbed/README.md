## MbedOS 6

<https://os.mbed.com/docs/mbed-os/v6.0/introduction/index.html>

<https://os.mbed.com/docs/mbed-os/v6.0/program-setup/serial-communication.html>


<https://embeddedartistry.com/blog/2018/04/26/embedded-rules-of-thumb/>

another way that I found out to reset the storage and erase the memory completely is:

create a empty file called 'erase.act' and drag it to the DAPLink drive. This should blow everything away.

### FRDM-K66F accelerometer
https://community.nxp.com/docs/DOC-101385


### LED

<https://os.mbed.com/questions/78630/Thread-called-only-once-when-thread-is-c/>

Available PinNames for FRDM-K64F platform.
```
LED (RGB)
LED_RED = PTB22
LED_GREEN = PTE26
LED_BLUE = PTB21

mbed original LED naming
LED1 = LED_RED
LED2 = LED_GREEN
LED3 = LED_BLUE
LED4 = LED_RED
```
 defined in pinnames.h

```
#include "mbed.h"
 
DigitalOut red  (LED_RED);
DigitalOut green(LED_GREEN);
DigitalOut blue (LED_BLUE);
 
int main() {
 
    while (1) {
        printf("red\n\r");        red = 0; green = 1; blue = 1; wait(5.0);  
        printf("green\n\r");      red = 1; green = 0; blue = 1; wait(5.0);  
        printf("blue\n\r");       red = 1; green = 1; blue = 0; wait(5.0);
        printf("red+green\n\r");  red = 0; green = 0; blue = 1; wait(5.0);
        printf("green+blue\n\r"); red = 1; green = 0; blue = 0; wait(5.0);
        printf("red+blue\n\r");   red = 0; green = 1; blue = 0; wait(5.0);
    }
}
```

## Embedded development 101

<https://habr.com/ru/post/503322/> 

### mbed update
```
https://github.com/ARMmbed/mbed-os/blob/master/platform/mbed_version.h

https://os.mbed.com/questions/82202/mbed-update-to-latest-release/

mbed update

printf("mbed-os-rev: %d.%d.%d  lib-rev: %d", 
MBED_MAJOR_VERSION, MBED_MINOR_VERSION, MBED_PATCH_VERSION, MBED_LIBRARY_VERSION);
```
 
## Pelion SDK
<https://www.pelion.com/docs/device-management/current/service-api-references/service-api-documentation.html>

<https://github.com/ARMmbed/mbed-cloud-sdk-python>


The Pelion SDKs are deprecated. So the options to manage devices are the device management console (aka portal), the command line tools, and the service APIs.
 
Here is some information.
https://www.pelion.com/docs/device-management/current/service-api-references/index.html
 
 
You can use Node.JS, Python or many other language stack with socket capabilities to interact with the service APIs.
See attached short presentation with a very simple tutorial using curl and a websocket library I put together.
 
Also we have other good internal tutorials on service APIs here.
https://confluence.arm.com/display/IoTBU/Pelion+Device+Management+Service+API+usage+examples

## MBed Version
```
pwd
[mbed-os-example-pelion](add-cy8cproto-capsense-slider)  
grep "define MBED_MINOR_VERSION"  mbed-os/platform/mbed_version.h
#define MBED_MINOR_VERSION 14

grep "define MBED_PATCH_VERSION" mbed-os/platform/mbed_version.h
#define MBED_PATCH_VERSION 1
 
grep "define MBED_MAJOR_VERSION"  mbed-os/platform/mbed_version.h
#define MBED_MAJOR_VERSION 5
```

## Mbed in Docker

<https://hub.docker.com/r/mbedos/mbed-os-env> official docker from ARM
```
docker run -it  -v /Users/miclub01/GIT/FORK/pelion-ml-demo:/mnt/host mbedos/mbed-os-env /bin/bash
```

## Manifest tool

<https://github.com/ARMmbed/manifest-tool>

## Embedding binary in C
<https://codeplea.com/embedding-files-in-c-programs>

<https://flak.tedunangst.com/post/embedding-binary-objects-in-c>

<https://news.ycombinator.com/item?id=22888318>


## CMSIS-NN

Because CMSIS-NN targets embedded devices, it focuses on fixed-point arithmetic. This means that a neural network cannot simply be reused. Instead, it needs to be converted to a fixed-point format that will run on a Cortex-M device.

<https://github.com/ARM-software/CMSIS_5/tree/develop/CMSIS/NN>

<https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/converting-a-neural-network-for-arm-cortex-m-with-cmsis-nn>

## TF micro on Mbed

<https://stackoverflow.com/questions/60764852/deploying-tflite-on-microcontrollers>

<https://github.com/ARMmbed/mbed-os/tree/master/targets>


<https://gitter.im/tensorflow/sig-micro>

<https://github.com/tensorflow/tensorflow/issues?q=mbed>

<https://petewarden.com/>

<https://github.com/tensorflow/tensorflow/issues?q=mbed>
 
<https://github.com/tensorflow/tensorflow/issues/34896>

<https://github.com/tensorflow/tensorflow/pull/38481>

```
mbed compile -m DISCO_F746NG -t GCC_ARM -D TF_LITE_STATIC_MEMORY
```

## WiFi extension
<https://habr.com/ru/post/155203/> 

## External Board in Mac is under /Volumes

ls /Volumes/NOD_H743ZI2/


### PDM-PCM microphone

2x PDM-PCM microphone

<https://en.wikipedia.org/wiki/Pulse-code_modulation>

<https://en.wikipedia.org/wiki/Pulse-density_modulation>

<https://www.youtube.com/watch?v=HlGJ6xxbz8s>

<https://www.youtube.com/watch?v=W2-FP7twy8s>

<https://www.youtube.com/watch?v=HqHIOA-Fcuw>

<https://www.youtube.com/watch?v=YJmUkNTBa8s>

pulse code modulation is a method used to convert an analog signal into a digital signal. So that it can be transmitted through a digital communication network, and then converted back into the original analog signal.

The PCM process includes three steps: Sampling, Quantization, and Coding.

In the sampling process, the magnitude of the analog signal is sampled regularly at uniform intervals. The obtained values are called samples.

For a 4 kHz voice channel, the sampling rate is 8000 Hz, which means the signal is sampled 8000 times per second.

The samples will then be converted to digital numbers as we will see in the quantization process.

Quantization is the process of converting the obtained samples into discrete digital values. The most basic type of quantization is called uniform quantization.

In an uniform quantization, the vertical axis, which represents the amplitude, is divided into equal sized steps. As shown in this figure, the range between 1 volt and -1 volt is divided into 16 steps, each step represents 0.125 volt.

All the samples whose amplitude falls within an step, take the same step value.

However, the quantization process introduces an error. This is because that the real amplitude of a sample is replaced by an approximate value. This error is called quantization noise or quantization distortion.

In uniform quantization, the quantization distortion presents a problem. For example, let's assume a quantization error of 0.05 volt, if this happens at a high level signal, such as 5 volt, the noise ratio is 0.05 volt divided by 5 volt, which is 1%, not too bad. But if the same quantization error happens at a low level signal, such as 0.5 volt, the noise ratio is 0.05 volt divided by 0.5 volt, which is 10%. 

Simply put, for uniform quantization, the signal to noise ratio is good at high level signals, but bad at low level signals. That is why non-uniform quantization was introduced.

In non-uniform quantization process, the steps are not of equal size. Small steps are used for small signal values and large steps for large values. The purpose of doing so is to achieve that the signal-to-noise ratio is nearly independent of the signal level.

This is done by favoring low-level voice over higher-level voice. In other words, more code groups are assigned to speech at low levels than at the higher levels, progressively more as the level reduces. This is shown in this figure.

There are two types of non-uniform quantization methods in popular use today. They are the A-law and the u-law. Let's first look at the A-law.

A law follows the logarithmic formula listed here, with A equals to 87.6.

We can see that the curve consists of linear piecewise segments, seven above and seven below the origin. The segment just above and the segment just below the origin consists of two linear segments. Counting the collinear elements by the origin, there are 16 segments. Each segment has 16 8-bit PCM codes assigned. These are the codewords that identify the voltage level of a sample at some moment in time.

Each codeword, often called a PCM "word", consists of 8 bits. The first bit tells the receiver if the sample is a positive or negative voltage. We can see that all PCM words above the origin start with a binary 1, and those below the origin start with a binary 0. 

The next 3 bits in sequence identify the segment. There are eight segments above the origin and eight below the origin. 

The last 4 bits, shown as XXXX, indicate exactly where in a particular segment that voltage line is located.

The second is called u-law. It follows the logarithmic formula listed here with u equals to 100.

The North American T1 system uses the u-law quantization and coding process. The process is similar to that of A-law.



## Cypress y8cproto_062_4343w
<https://blog.packetp.com/running-wifi-example-on-cy8cproto_062_4343w/> 

<https://www.cypress.com/documentation/development-kitsboards/psoc-6-wi-fi-bt-prototyping-kit-cy8cproto-062-4343w>

<https://os.mbed.com/platforms/CY8CPROTO-062-4343W/>

<https://www.embedded-computing.com/guest-blogs/for-the-professional-maker-get-started-with-psoc-6-using-the-cy8cproto-062-4343w-kit>

### Temperature code:
<https://iotexpert.com/2019/12/09/mouser-psoc-6-wifi-bt-mbed-l4-temperature-thread/>

<https://www.cypress.com/file/457891/download>

<https://www.cypress.com/file/421606/download>

<https://www.cypress.com/file/451811/download>

### MbedOS code
<https://github.com/ARMmbed/mbed-os/tree/master/targets/TARGET_Cypress/TARGET_PSOC6/TARGET_CY8CPROTO_062_4343W>



Not this:
<https://www.cypress.com/documentation/development-kitsboards/psoc-6-wifi-bt-pioneer-kit-cy8ckit-062-wifi-bt>

You can base the PSoC62 project off of this repo:
https://github.com/maclobdell/mbed-os-example-pelion

```
rm -rf mbed-os-example-pelion
mbed import https://github.com/maclobdell/mbed-os-example-pelion.git
cd mbed-os-example-pelion/
git checkout -B "add-cy8cproto-062-4343w-5.13.4" "origin/add-cy8cproto-062-4343w-5.13.4"
mbed status
mbed deploy
mbed device-management init -d arm.com --model-name example-app --force -q
mbed compile -m CY8CPROTO_062_4343W -t GCC_ARM

```


### Online compiler
<https://ide.mbed.com/compiler>

<https://github.com/mlubinsky-arm/sensor2cloud>

<https://github.com/ARMmbed/mbed-cli/issues/894>

## Code for the Grove-3-Axis-Digital-Accelerometer-MMA7660FC

<https://github.com/mrcoulter45/Grove-3-Axis-Digital-Accelerometer-MMA7660FC>

## Camera

<http://wiki.seeedstudio.com/Grove-Serial_Camera_Kit/>

<https://github.com/c1728p9/CameraOV528>

<https://github.com/sarahmarshy/mbed-timelapse>

<https://os.mbed.com/users/edodm85/notebook/ov7670-camera-module/>

<https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/image-recognition-on-arm-cortex-m-with-cmsis-nn>  real-time image recognition  Arm Cortex-M7 processor, using Arm’s CMSIS-NN 

<https://github.com/ARM-software/ML-examples>

## Forum
<https://forums.mbed.com/>

<https://os.mbed.com/docs/mbed-os/v5.15/tools/index.html>

<https://www.rlocman.ru/review/article.html?di=600377> Kalman filter

## Pelion Device Management

### SDK

<https://armmbed.github.io/mbed-cloud-sdk-documentation/#introduction>

<https://blog.pelion.com/en>. Pelion Blog

<https://www.pelion.com/docs/device-management/current/updating-firmware/integrating-the-client-in-your-application.html>

<https://www.pelion.com/docs/device-management/current/updating-firmware/setting-up.html> Device Update

<https://github.com/maclobdell/fota-runner/blob/master/fota-runner.py>

<https://armh.sharepoint.com/sites/Iot-partner-enablement-o365/SitePages/ISG-Training---October-2018.aspx?web=1>

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

<http://www.programmersought.com/article/605830579/>

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

Extension: Accelerometer, Gyroscope, Humidity, Magnetometer, Pressure, Temperature Sensor
<https://www.digikey.com/product-detail/en/stmicro/X-NUCLEO-IKS01A3/497-18505-ND/9950636>

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

<https://os.mbed.com/studio/> michael.lybins..@a Vanti..7!

## Mbed CLI
```

$ cd /Users/miclub01/python2_virtual_env
$ source  mbed//bin/activate

$ pip install mbed-cli

Download GCC_ARM for MAc
https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads
mbed config -G GCC_ARM_PATH "C:\Program Files (x86)\GNU Tools ARM Embedded\7 2018-q2-update\bin

$ mbed config -G CLOUD_SDK_API_KEY  xxxxxx

$ mbed config --list

[mbed] WARNING: Python 3 is not yet fully supported: Python errors may occur when compiling, testing and exporting
[mbed] Global config:
ARM_PATH=/Users/miclub01/Downloads/gcc-arm-none-eabi-9-2019-q4-major/bin/
GCC_ARM_PATH=/Users/miclub01/Downloads/gcc-arm-none-eabi-9-2019-q4-major/bin/
CLOUD_SDK_API_KEY=xxxxxxx



$ mbed dm init -d "company.com" --model-name "product-model" -q --force 
 
[mbed] Working path "/mnt/GIT/NUCLEO_H743ZI2" (program)
[mbed] Auto-installing missing Python modules (pyusb)...
[INFO] 2020-03-11 04:05:07 - __main__ - Found developer certificate named dev_cert_2020_02_13_12_35
[INFO] 2020-03-11 04:05:07 - __main__ - Writing developer certificate dev_cert_2020_02_13_12_35 into c file mbed_cloud_dev_credentials.c
[WARNING]: Certificates generated with this tool are self-signed and for testing only
[WARNING]: This certificate is valid for 90 days. For production,use certificates with at least 10 years validity.
[INFO] 2020-03-11 04:05:07 - manifesttool.init - Certificate written to .update-certificates/default.der
[INFO] 2020-03-11 04:05:07 - manifesttool.init - Private key written to .update-certificates/default.key.pem
[INFO] 2020-03-11 04:05:07 - manifesttool.init - Default settings written to .manifest_tool.json
[INFO] 2020-03-11 04:05:07 - manifesttool.init - Wrote default resource values to update_default_resources.c

$ git status

	modified:   mbed_cloud_dev_credentials.c
	modified:   update_default_resources.c

Untracked files:

	.manifest_tool.json
	.update-certificates/

cat .manifest_tool.json
{
    "classId": "d55bc4d2-da99-5898-b4e7-2fe11c5cf885",
    "default-certificates": [
        {
            "file": ".update-certificates/default.der"
        }
    ],
    "deviceURNs": [],
    "modelName": "mbed",
    "private-key": ".update-certificates/default.key.pem",
    "vendorDomain": "arm.com",
    "vendorId": "fa6b4a53-d5ad-5fdf-be9d-e663e4d41ffe"
}


$ mbed compile -m NUCLEO_H743ZI2 -t GCC_ARM -DRESET_STORAGE

$ mbed dm update device -D 0170a6e08345000000000001001a30be -m NUCLEO_H743ZI2 --no-cleanup -v
 
```

<https://os.mbed.com/docs/mbed-os/v5.15/tools/manual-installation.html>

<https://os.mbed.com/docs/mbed-os/v5.15/tools/working-with-mbed-cli.html>

<https://github.com/ARMmbed/mbed-cli-osx-installer/>
```
$ mbed new .  // will create file .med , mbed-os.lib mbed_app.json mbed_settings.py and folder mbed-os
$ mbed add https://github.com/ARMmbed/mbed-cloud-client

$ mbed compile
The Mbed OS tools in this program require the following Python modules: pyusb
       You can install all missing modules by running "pip install -r requirements.txt" in "/mnt/sensor2cloud/mbed-os"
       
$ mbed deploy
[mbed] Updating library "mbed-cloud-client" to rev #7b583acf30ca (tag: 4.3.0)
[mbed] Updating library "mbed-os" to rev #e642a7d8b360 (tags: latest, mbed-os-5.15.1)
[mbed] Auto-installing missing Python modules (pyusb)...
```



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

```

#cp ~/.ssh/id_rsa my_key
#cp ~/.ssh/id_rsa PelionML_Dashboard/my_key

```

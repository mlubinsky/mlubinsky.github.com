### IoT protocols

https://habr.com/ru/company/otus/blog/524140/


## DSP books:

<http://dsp-book.narod.ru/books.html>

<https://github.com/MattPD/cpplinks/blob/master/assembly.arm.md> ARM programming

hardware interrupt: <https://www.youtube.com/watch?v=DlEa8kd7n3Q>

## Serial port reading

Meta key

<https://osxdaily.com/2013/02/01/use-option-as-meta-key-in-mac-os-x-terminal/>


<https://www.cmrr.umn.edu/~strupp/serial.html#2_5_2>

C library for reading from Serial port:
<https://sigrok.org/wiki/Libserialport>

<https://sigrok.org/api/libserialport/unstable/index.html>



ML Processors
<https://www.electronicdesign.com/technologies/embedded-revolution/article/21131474/accelerating-machine-learning-means-new-hardware>


<https://opensource.googleblog.com/2020/03/pigweed-collection-of-embedded-libraries.html>

<https://gilberttanner.com/blog/convert-your-tensorflow-object-detection-model-to-tensorflow-lite> TF Lite

<https://www.embeddedrelated.com/showarticle/1324.php> .  So you want to be an embedded developer

Digi-key or Mouser- you can search MCUs by Architecture, peripherals, memory and so on

<https://www.rlocman.ru/review/article.html?di=600377> Kalman filter

<http://mymcu.ru/>




<https://www.artekit.eu/doc/guides/all-about-gpios/> GPIO

<https://interrupt.memfault.com/blog/i2c-in-a-nutshell>. I2C

<https://www.reddit.com/r/embedded/comments/f1b8f0/is_there_a_good_comprehensive_guide_checklist/>

<https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter> UART 

<https://habr.com/ru/post/109395/> UART

<https://habr.com/ru/post/488574/> UART

<https://www.edaboard.com/>

<https://www.microcontrollertips.com/>

<https://www.reddit.com/r/embedded/>

<https://www.reddit.com/r/microcontrollers/>

<https://habr.com/ru/hub/controllers/>

<http://easyelectronics.ru/category/arm-uchebnyj-kurs>

<https://platformio.org/>

<https://habr.com/ru/company/skyeng/blog/456094/> Читаем даташиты 2

<https://habr.com/ru/company/skyeng/blog/449624/> Читаем даташиты 1

<https://habr.com/ru/post/453262/>

<https://electronics.stackexchange.com/>

```
Электричество
Vcc, Vdd – «плюс», питание
Vss, Vee – «минус», земля
current – ток
voltage – напряжение
to sink current – работать «землей» для внешней нагрузки
to source current – питать внешнюю нагрузку
high sink/source pin – пин с повышенной «терпимостью» к нагрузке


IO
H, High – на пине Vcc
L, Low – на пине Vss
High Impedance, Hi-Z, floating – на пине ничего нет, «высокое сопротивление», он фактически невидим внешнему миру.
weak pull up, weak pull down – встроенный подтягивающий/стягивающий резистор, примерный аналог 50 кОм (см. даташит). Используется, например, чтобы входной пин не болтался в воздухе, вызывая ложные срабатывания. Weak – потому что его легко «перебить».
push pull – выходной режим пина, в котором он переключается между High и Low – обычный OUTPUT с Arduino.
open drain – обозначение выходного режима, в котором пин может быть либо Low, либо High Impedance / Floating. При этом почти всегда это не «настоящий» открытый сток, есть защитные диоды, резисторы, еще что. Это просто обозначение режима земля/ничего.
true open drain – а вот это уже настоящий открытый сток: пин напрямую ведет в землю, если открыт, или пребывает в подвешенном состоянии, если закрыт. Это значит, что через него при необходимости можно пускать напряжение больше Vcc, но максимум все равно оговаривается в даташите в разделе Absolute Maximum Ratings / Voltage.


Интерфейсы
in series – подключенные последовательно
to chain – собирать чипы в цепочку последовательным подключением, увеличивая количество выходов.
shift – сдвиг, обычно обозначает сдвиг битов. Соответственно, to shift in и to shift out – принимать и передавать данные побитно.
latch – задвижка, прикрывающая буфер, пока через него сдвигаются биты. Когда передача закончена, задвижка открывается, биты начинают работать.
to clock in – выполнить побитную передачу, сдвинуть все биты на нужные места.
double buffer, shadow register, preload register – обозначения истории, когда регистр должен уметь принимать новые данные, но придерживать их до какого-то момента. Например, для корректной работы ШИМ его параметры (скважность, частота) не должны меняться, пока не закончится текущий цикл, но новые параметры уже могут быть переданы. Соответственно, текущие держатся в shadow register, а новые попадают в preload register, будучи записанными в соответствующий регистр чипа.


Всякое
prescaler – предделитель частоты
to set a bit – установить бит в 1
to clear/reset a bit – сбросить бит в 0 (reset – фишка даташитов STM)
to toggle a bit – поменять значение бита на противоположное (см. пример в начале статьи)
```

### Sound

<https://arxiv.org/pdf/1711.07128.pdf>

<https://www.edgeimpulse.com/blog/train-a-tiny-ml-model>

### Arduino programming 

<https://youtu.be/ztGQrlx4AKs>

<https://habr.com/ru/post/489722/>

<https://www.udemy.com/course/arduino-sbs-17gs/learn/lecture/6080362?start=0#overview>

<https://www.udemy.com/course/arduino-sbs-getting-serious/learn/lecture/6843784#overview>

## ESP8266

<https://habr.com/ru/company/coolrf/blog/235881/>

<https://habr.com/ru/post/362623/>

<https://esp8266.ru/>

<https://www.esp8266.com/>

## STM32

<https://habr.com/ru/post/490474/>

<https://stm32-base.org/>

<https://www.reddit.com/r/embedded/comments/f2psv9/how_to_start_with_stm32/>

<https://www.youtube.com/channel/UCjnmZw3h4XnpK3e5D2jvIGA> STM32

### STM32F4 Cortex-M4 programming

<https://www.udemy.com/course/deep-learning-from-ground-uptm-on-arm-processors/learn/lecture/17392440#overview>

<https://www.udemy.com/course/stm32f4-programming-course-for-beginners/learn/lecture/4910872#overview>

<https://www.udemy.com/course/stm32f4-programming-course-for-beginners/>

<https://electronics.stackexchange.com/questions/179345/how-to-begin-programming-with-stm32-discovery>

<http://stm32f4-discovery.net/2014/09/stm32f4-tutorials-one-place/>

<https://www.fmf.uni-lj.si/~ponikvar/STM32F407%20project/Ch3%20-%20Programming.pdf>

<https://www.st.com/content/ccc/resource/technical/document/programming_manual/6c/3a/cb/e7/e4/ea/44/9b/DM00046982.pdf/files/DM00046982.pdf/jcr:content/translations/en.DM00046982.pdf>


### Client

 
 
### Arduino Nano BTE

<https://www.youtube.com/watch?v=jCLgqaXS6Gg&feature=youtu.be>. Arduino Programming

<https://medium.com/tensorflow/how-to-get-started-with-machine-learning-on-arduino-7daf95b4157>

<https://arduino.github.io/ArduinoAI/BLESense-test-dashboard/>

Gyroscope (3 features) and acceleration data (3 features)

NaNo 33 BLE does not support Wi-Fi
The ARM® Cortex-M4 processor with floating-point unit (FPU) has a 32-bit instruction set 
(Thumb®-2 technology) that implements a superset of 16- and 32-bit instructions to maximize code density and
performance.

The nRF52840 contains 1 MB of flash and 256 kB of RAM that can be used for code and data storage.

<https://content.arduino.cc/assets/Nano_BLE_MCU-nRF52840_PS_v1.1.pdf>

<https://blog.arduino.cc/2019/07/31/why-we-chose-to-build-the-arduino-nano-33-ble-core-on-mbed-os/>

<https://www.hackster.io/news/new-arduino-nano-boards-run-arm-s-mbed-os-3777ccb89017>

## Mbed Studio
<https://os.mbed.com/studio/>
michael.lybins@a 
Vanti..7!

## Pelion Device Management
<https://os.mbed.com/pelion-free-tier/> 

## Mbed-cli Docker

<https://hub.docker.com/r/mbedos/mbed-os-env> official docker from ARM

<https://os.mbed.com/docs/mbed-os/v5.15/tools/working-with-mbed-cli.html>

```
docker run -v /Users/mlubinsky/LEG/psweb/ARM/MYPROG:/mnt/myprog -i -t mbedos/mbed-os-env
root@c762b32ba377:~# ls /mnt

cd   /mnt/myprog/
  mbed new mbed-os-program
  Working path "/mnt/myprog" (directory)
  Creating new program "mbed-os-program" (git)
  Adding library "mbed-os" from "https://github.com/ARMmbed/mbed-os" at branch/tag "latest"
```

<https://os.mbed.com/docs/mbed-os/v5.15/quick-start/compiling-the-code.html>

```
 mbed import https://github.com/ARMmbed/mbed-os-example-blinky
$ cd mbed-os-example-blinky
mbed compile --target K64F --toolchain ARM --flash
```

```
mbed --help
usage: mbed [-h] [--version]             ...

Command-line code management tool for ARM mbed OS - http://www.mbed.com
version 1.10.2

Use "mbed <command> -h|--help" for detailed help.
Online manual and guide available at https://github.com/ARMmbed/mbed-cli

optional arguments:
  -h, --help         show this help message and exit
  --version          print version number and exit

Commands:

    new              Create new mbed program or library
    import           Import program from URL
    add              Add library from URL
    remove           Remove library
    deploy           Find and add missing libraries
    publish          Publish program or library
    update           Update to branch, tag, revision or latest
    sync             Synchronize library references

    ls               View dependency tree
    releases         Show release tags
    status           Show version control status

    compile          Compile code using the mbed build tools
    test             Find, build and run tests
    device-management
                     device management subcommand
    export           Generate an IDE project
    detect           Detect connected Mbed targets/boards

    sterm            Open serial terminal to connected target.

    config           Tool configuration
    target           Set or get default target
    toolchain        Set or get default toolchain
    cache            Repository cache management
```



```
docker pull mbedos/mbed-os-env
docker run -i -t mbedos/mbed-os-env /bin/bash
---docker exec -it mbedos/mbed-os-en /bin/bash
which python3
/usr/bin/python3

which mbed
/usr/local/bin/mbed

which mbed-cli .   <---  the same as mbed !!!
/usr/local/bin/mbed-cli

/usr/local/bin# cat mbed
#!/usr/bin/python3

# -*- coding: utf-8 -*-
import re
import sys

from mbed.mbed import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
    
```
<https://os.mbed.com/questions/>

<https://github.com/ARMmbed/mbed-cli/>

<https://github.com/wxgithub/armnn/blob/master/Dockerfile>

<https://github.com/aschmidt75/docker-mbed-cli-gcc-arm>

<https://hub.docker.com/r/macrat/docker-mbed-cli/>

<https://hub.docker.com/r/productize/mbed-cli/>

```
git clone  https://github.com/nigelpoulton/psweb.git
cd psweb/
docker image build -t test:latest .
docker container run -d --name webl3 --publish 8084:8080 test:latest
In browser: http://localhost:8084/

docker container run -it ubuntu:latest /bin/bash    # you inside the container shell now!


```
<https://os.mbed.com/docs/mbed-os/v5.15/tools/manual-installation.html> 

<https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads>
<https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm>
<https://gist.github.com/joegoggins/7763637>

<https://developer.arm.com/docs/100748/latest/getting-started/installing-arm-compiler>

<https://blog.feabhas.com/2017/10/introduction-docker-embedded-developers-part-2-building-images/>

<https://blog.feabhas.com/2017/11/introduction-docker-embedded-developers-part-3-cross-compiling-cortex-m/>

<https://blog.feabhas.com/2017/12/introduction-docker-embedded-developers-part-4-reducing-docker-image-size/>

<https://github.com/aschmidt75/docker-mbed-cli-gcc-arm>

<https://github.com/ARMmbed/mbed-cli/issues/599>

<https://github.com/productize/docker-mbed-cli>

<https://gitlab.com/alelec/docker-mbed-gcc-arm>

<https://www.arm.com/company/news/2019/04/arm-and-docker-better-together>

<https://github.com/3mdeb/docker-mbed-cli>

<https://blog.3mdeb.com/2018/2018-09-27-optimize-performance-in-docker/>

<https://www.thingforward.io/fileadmin/user_upload/knowledge_center/09_GettingStartedWithPlatformIOandArmMbedOs.pdf>
```
What I am about to describe will be a massive pain to set up but would be a solution to your problem long term.

On the dev machines:
VS-Code + VS-Code Remote docker extension

The build server:
boot2docker or other docker “server” OS

Installed In a docker image:
arm-gnu-emdedded toolchain
mbed-cli
whatever other dependencies are needed to do an mbed-os build

A vs-code remote development config file can be created such that vs-code will automatically connect to the docker server, start a container, and then attach vs-code to the container. The remote docker extension will allow the dev machines to build, compile, debug, etc. just like if the toolchain and sources were located on the dev machine.

Im very much simplifying this description but It is something my team and I have done successfully.

```
 ### screen
 
 Type Control-A followed by Control-\   (or k) to exit your screen session
 
 screen basics:

control-a begins the command sequence in screen

Next character:

d - disconnect from session
k - terminate session
If you disconnect, you can reconnect using screen -r


That is if you hit Control-A followed by an “a”. If you want to kill that session, use Control-A then “k”.
```
script -a -t 0 out.txt screen /dev/ttyUSB0 115200

Details

script: A built-in application to "make a typescript of terminal session"
-a: Append to output file
-t 0: Time between writing to output file is 0 seconds, 

so out.txt is updated for every new character
out.txt: Is just the output file name
screen /dev/ttyUSB0 115200: Command from question for connecting to an external device
```

 <https://stackoverflow.com/questions/14208001/save-screen-program-output-to-a-file>
 
 <http://stackoverflow.com/questions/1039442/mac-os-x-terminal-apps-buffer-and-screen-command>
 
 If you want to use screen as an terminal, 
 but don't want it to go into the background when the window dies, you will need to turn off auto-detach.

To do this, edit ~/.screenrc (it probably won't exist) and add the following line:

autodetach off

The next time you start screen, if you kill the window you will kill the session.
 ``` 
  ls /dev/tt*
  screen /dev/tty.board_name 115200
  ```
 ### CoolTerm 
 
 <http://freeware.the-meiers.org/>
 
 <https://learn.sparkfun.com/tutorials/terminal-basics/coolterm-windows-mac-linux>
 
 ### Cornflake
 <http://tomgerhardt.com/Cornflake/>
 
 ### minicom
 ```   
  brew install minicom
  ls /dev/tty.usb*.       # find the tty name
  minicom -D /dev/tty.usbmodem14412
 ```  
  
Mbed requires source files to be structured in a certain way. The TensorFlow Lite for Microcontrollers Makefile knows how to do this for us and can generate a directory suitable for Mbed. To do so, run the following command:
```
make f tensorflow/lite/micro/tools/make/Makefile \ TARGET = mbed TAGS = "cmsis-nn disco_f746ng" generate_micro_speech_mbed_project 
```
This results in the creation of a new directory: 
```
tensorflow/lite/micro/tools/make/gen/mbed_cortex-m4/prj/ 
```
To inform Mbed that the current directory is the root of an Mbed project: 
``` 
 mbed config root . 
``` 
Next, instruct Mbed to download the dependencies and prepare to build: 
``` 
 mbed deploy 
``` 
 By default, Mbed builds the project using C++98. However, TensorFlow Lite requires C++11.
 Run the following Python snippet to modify the Mbed configuration files so that it uses C++11. 
 
``` 
 python c 'import fileinput, glob; for filename in glob . glob ( "mbed-os/tools/profiles/*.json" ): for line in fileinput . input ( filename , inplace = True ): print ( line . replace ( " \" std=gnu++98 \" " , " \" std=c++11 \" , \" fpermissive \" " )) ' 
``` 
 Finally, run the following command to compile: 
``` 
 mbed compile m DISCO_F746NG -t GCC_ARM
``` 
This should result in a binary at the following path: ./BUILD/DISCO_F746NG/GCC_ARM/mbed.bin 
Deploy to  STM32F746G board - copy the file to it. 
On macOS, you can do this by using the following command: 
```
cp ./BUILD/DISCO_F746NG/GCC_ARM/mbed.bin /Volumes/DIS_F746NG/ 

ls /dev/tty* It will look something like the following: /dev/tty.usbmodem1454203 
```
A TensorFlow model consists of two main things: The weights and biases resulting from training
A graph of operations that combine the model’s input with these weights and biases to produce the model’s output
At this juncture, our model’s operations are defined in the Python scripts, and its trained weights and biases are in the most recent checkpoint file. We need to unite the two into a single model file with a specific format, which we can use to run inference. The process of creating this model file is called freezing we’re creating a static representation of the graph with the weights frozen into it. To freeze our model, we run a script:
```
!python tensorflow/tensorflow/examples/speech_commands/freeze.py \ model_architecture = tiny_conv window_stride = 20 preprocess = micro \ wanted_words = ${ WANTED_WORDS } quantize = 1 \ output_file = /content/tiny_conv.pb \ start_checkpoint = /content/speech_commands_train/tiny_conv. \ ckpt-${ TOTAL_STEPS } 
```
##  Blackstone Engineering IoT Workshop and Pelion Device Management
<https://www.pelion.com/docs/device-management> Pelion device management

<https://www.pelion.com/docs/device-management/current/service-api-references/account-management.html>

<https://www.pelion.com/docs/device-management/current/user-account/api-keys.html>

<https://docs.mbed.com/docs/mbed-os-handbook/en/latest/advanced/bootloader/>  Bootloader


<https://cloud.mbed.com/docs/current/porting/building-r1-3-version-of-cloud-client-for-different-operating-systems.html>


configure mbed
<https://os.mbed.com/docs/mbed-os/v5.15/tools/manual-installation.html>

<https://github.com/BlackstoneEngineering/aiot-workshop>

<https://github.com/moon412/mbed-dsc-e2e> Yue Zhao code

## CMSIS-NN 
<https://community.arm.com/developer/ip-products/processors/b/processors-ip-blog/posts/deploying-convolutional-neural-network-on-cortex-m-with-cmsis-nn>

CMSIS-NN code: <https://github.com/ARM-software/ML-KWS-for-MCU/blob/master/Deployment/Source/NN/DNN/dnn.cpp>

## TF-lite - tensorflow lite
<https://www.tensorflow.org/lite/microcontrollers>

<https://fosdem.org/2020/schedule/event/iottensorflow/>

<https://gilberttanner.com/blog/convert-your-tensorflow-object-detection-model-to-tensorflow-lite>

<https://developer.arm.com/solutions/machine-learning-on-arm/developer-material/how-to-guides/build-arm-cortex-m-voice-assistant-with-google-tensorflow-lite/single-page>

<https://github.com/uTensor/tf_microspeech> . source code for the article above

<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/README.md>

the TensorFlow Lite Converter’s Python API to do this. It takes our Keras model and writes it to disk in the form of a FlatBuffer , which is a special file format designed to be space-efficient. 




Warden, Pete,Situnayake, Daniel. TinyML (Kindle Locations 1221-1222). O'Reilly Media. Kindle Edition. 

<https://www.edgeimpulse.com/blog/train-a-tiny-ml-model> Sound recognition 
<https://github.com/tensorflow/tensorflow/tree/master/tensorflow/lite/micro> code from book

 sinus example
<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/create_sine_model.ipynb>

Hello word example
<https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/micro/examples/hello_world/hello_world_test.cc>


To check the version of Make installed, enter make version at the command line. You need a version greater than 3.82. 
```
 brew install make:
 installed gmake
 gmake --version 4.3 
 make --version  3.81
```
<https://tinymlsummit.org/2019/>

<https://tinymlsummit.org/>

<https://colab.research.google.com/github/arduino/ArduinoTensorFlowLiteTutorials/blob/master/GestureToEmoji/arduino_tinyml_workshop.ipynb#scrollTo=kGNFa-lX24Qo>

<https://www.eetimes.com/tinyml-sees-big-hopes-for-small-ai/>

## ARM CPUs
https://habr.com/ru/news/t/453954/

<https://habr.com/ru/post/473424/> . ARM - графические решения Mali-G57 Valhall и Mali-D37, нейропроцессоры Ethos-N57 и N37

<https://arxiv.org/abs/1911.05289> . 
The Deep Learning Revolution and Its Implications for Computer Architecture and Chip Design

<https://www.arm.com/products/silicon-ip-cpu/machine-learning/arm-nn>

### hotchips
<https://www.youtube.com/user/hotchipsvideos/videos>

<https://youtu.be/gPFTkud6lr0>

<https://youtu.be/uNUHQKJvAgE>


<https://github.com/ARM-software/ML-examples>

<https://www.youtube.com/watch?v=_6sh097Dk5k>

<https://developer.arm.com/ip-products/processors/machine-learning/arm-ml-processor>

<https://habr.com/ru/post/445936/>

<https://habr.com/post/420435/>

<https://habr.com/ru/post/448288/>

<https://developer.arm.com/ip-products/processors/machine-learning/arm-ml-processor>

<https://armh.sharepoint.com/sites/Iot-partner-enablement-o365/SitePages/ISG-Training---October-2018.aspx?web=1>

<https://www.youtube.com/watch?v=IbisEjzoxTY>

<https://sysprogs.com/w/mbed-settings-extractor/>



## AI on embedded devices from Intel, NVidia, etc

<https://www.informationweek.com/big-data/ai-machine-learning/engineering-tiny-machine-learning-for-the-edge/a/d-id/1336972>

<https://habr.com/ru/post/473424/> . ARM - графические решения Mali-G57 Valhall и Mali-D37, нейропроцессоры Ethos-N57 и N37

<https://habr.com/ru/company/1cloud/blog/472230/>

<https://habr.com/ru/company/recognitor/blog/468421/>

<https://habr.com/ru/post/471074/> Synet 

<https://www.jameswhanlon.com/new-chips-for-machine-intelligence.html>

<https://news.ycombinator.com/item?id=21178609>

## AWS
### S3
<https://s3.console.aws.amazon.com/s3/buckets/mlubinsky/?region=us-east-2&tab=overview>
### EC2
<https://us-east-2.console.aws.amazon.com/ec2/v2/home?region=us-east-2#Instances:search=i-0a35c9f8a92a39f8c;sort=dnsName>

	
InstanceID: i-0a35c9f8a92a39f8c
Instance type: t2.small
Zone: us-east-2c
DNS:  ec2-18-223-44-124.us-east-2.compute.amazonaws.com
IP4: 18.223.44.124

chmod 400 aws_ec2_key_pair.pem
ssh -i "aws_ec2_key_pair.pem" ubuntu@ec2-18-223-44-124.us-east-2.compute.amazonaws.com

 

## ML and Tensorflow on ARM

<https://news.ycombinator.com/item?id=19327183>

<https://utensor.ai>

<https://community.arm.com/tools/b/blog/posts/arm-nn-linaro-machine-intelligence-initiative>

<https://towardsdatascience.com/why-machine-learning-on-the-edge-92fac32105e6>

<https://blog.hackster.io/simple-neural-network-on-mcus-a7cbd3dc108c>

<https://github.com/uTensor/uTensor>

## DS-5

<https://www.youtube.com/playlist?list=PL2F72C57B07FC982D>

<https://confluence.arm.com/pages/viewpage.action?pageId=212209815>

<https://developer.arm.com/products/software-development-tools/ds-5-development-studio>

<https://community.arm.com/tools/b/blog>

## Cross compilation for ARM

<https://ru.wikipedia.org/wiki/%D0%9A%D1%80%D0%BE%D1%81%D1%81-%D0%BA%D0%BE%D0%BC%D0%BF%D0%B8%D0%BB%D1%8F%D1%82%D0%BE%D1%80>

<https://habr.com/post/319736/>

В случае платформ типа raspberrypi с linux'ом на борту необходимо использовать

     aarch64-linux-gnueabi
     arm-linux-gnueabi
     arm-linux-gnueabihf 
      
в зависимости от того какое abi используется ОС, установленной на rpi.


Toolchain'ы делятся на несколько типов или триплетов. Триплет обычно состоит из трёх частей: целевой процессор, vendor и OS, vendor зачастую опускается.

    *-none-eabi — это toolchain для компиляции проекта работающего в bare metal.
    *eabi — это toolchain для компиляции проекта работающего в какой-либо ОС. В моём случае, это Linux.
    *eabihf — это почти то же самое, что и eabi, с разницей в реализации ABI вызова функций с плавающей точкой. hf — расшифровывается как hard float.
    
    dnf info gcc-c++-arm-linux-gnu


## ESP8266
<https://habr.com/ru/post/463107/>

## IoT
SVG + VUE + MQTT
<https://www.smashingmagazine.com/2019/05/svg-web-page-components-iot-part1/> 

<https://vas3k.ru/blog/homesillyhome/> . Smart Home

<https://www.pyimagesearch.com/2017/09/04/raspbian-stretch-install-opencv-3-python-on-your-raspberry-pi/>

<https://habr.com/company/itsumma/blog/415933/>

<https://habr.com/company/itsumma/blog/416291/>


<https://github.com/owntracks/tools/blob/master/TLS/generate-CA.sh>




<https://www.seeedstudio.com/Base-Shield-V2-p-1378.html>

<https://mcu-things.com/blog/k64-adc-temp-sensor/>

<https://www.element14.com/community/roadTestReviews/1984/l/freescale-freedom-frdm-k64f-development-platform-review>

FXOS8700CQ – accelerometer and magnetometer <https://www.nxp.com/docs/en/data-sheet/FXOS8700CQ.pdf>
<https://www.mathworks.com/help/supportpkg/freescalefrdmk64fboard/examples/read-temperature-from-an-i2c-based-sensor.html>


<https://os.mbed.com/platforms/FRDM-K64F/>  there is  section "Sensors"
<https://os.mbed.com/components/Grove-TempHumi-Sensor/>
<https://os.mbed.com/teams/NXP/code/frdm_Grove_Temp-Humidity_Example/wiki/Homepage>
<https://www.seeedstudio.com/Grove-Temperature-%26amp%3B-Humidity-Sensor-%EF%BC%88DHT11%EF%BC%89-p-745.html>

Temperature and Humidity Sensor: DHT22 sensor
Temp/Humidity sensor uses a shared single wire connection for TX/RX so it’s very simple to connect up, however you need to remember to add a pullup to the data line. My router isn’t close to my desk so I used a powerline adapter for the Ethernet, this worked flawlessly without any setup.

<https://os.mbed.com/components/mbed-Application-Shield/>  expansion board

<https://os.mbed.com/components/Avnet-ATT-WNC-14A2A-Cellular-IoT-Kit/>
<http://cloudconnectkits.org/>
 Shield that contains an ST221 Temperature and Humidty Sensor

<https://os.mbed.com/platforms/hexiwear/>

## Yocto

<https://zatoichi-engineer.github.io/2017/10/02/yocto-on-osx.html>

<http://eastrivervillage.com/Raspberry-Pi-dishes-from-Yocto-cuisine/>

<https://community.nxp.com/docs/DOC-94953> bitbake commands

<https://www.udemy.com/raspberry-pi-with-embedded-linux-made-by-yocto/>

<https://www.packtpub.com/virtualization-and-cloud/embedded-linux-development-using-yocto-projects-second-edition>

<https://hub.packtpub.com/building-our-first-poky-image-raspberry-pi/>

<http://www.instructables.com/id/Building-GNULinux-Distribution-for-Raspberry-Pi-Us/>

<https://medium.com/@shigmas/yocto-and-pi-ef8f1aa70231>

<http://git.yoctoproject.org/cgit/cgit.cgi/meta-raspberrypi>

<http://www.jumpnowtek.com/rpi/Raspberry-Pi-Systems-with-Yocto.html>

<https://himvis.com/bake-64-bit-raspberrypi3-images-with-yoctoopenembedded/>

<https://github.com/cosmo0920/rpi3-yocto-conf>


### find . -type f -print0 | xargs -0 grep mbed-cloud-client-rpi-machine

./raspberrypi-conf/local.conf.sample:MACHINE = "mbed-cloud-client-rpi-machine"

./rpi-build/conf/local.conf:MACHINE = "mbed-cloud-client-rpi-machine"


### cat ./meta-mbed-cloud-client/conf/machine/mbed-cloud-client-rpi-machine.conf

    #@TYPE: Machine
    #@NAME: mbed cloud client machine based on RPi 3
    #@DESCRIPTION: Machine configuration for the mbed cloud client device

    #Were building on RPi3, so for the convenience, set the machine variable and include its conf
    MACHINE = "raspberrypi3"
    include conf/machine/raspberrypi3.conf    ## see next file

    #Use our custom scard_image -class to overwrite the raspberrypi basic image
    IMAGE_CLASSES += " mbed_sdcard_image-rpi "
    IMAGE_FSTYPES += " mbed-sdimg "

    UBOOT_MACHINE = "rpi_3_32b_config"


### cat meta-raspberrypi/conf/machine/raspberrypi.conf

    #@TYPE: Machine
    #@NAME: RaspberryPi Development Board
    #@DESCRIPTION: Machine configuration for the RaspberryPi http://www.raspberrypi.org/ Board

    DEFAULTTUNE ?= "arm1176jzfshf"

    require conf/machine/include/tune-arm1176jzf-s.inc
    include conf/machine/include/rpi-base.inc

    SERIAL_CONSOLE ?= "115200 ttyAMA0"

    UBOOT_MACHINE = "rpi_config"
    VC4_CMA_SIZE_raspberrypi ?= "cma-64"


.rpi-build/conf/local.conf  has variable MACHINE.

The MACHINE variable is used to determine the target architecture and various compiler tuning flags.

See the conf files under meta-raspberrypi/conf/machine for details.

The choices for MACHINE are

    raspberrypi (BCM2835)
    raspberrypi0 (BCM2835)
    raspberrypi0-wifi (BCM2835)
    raspberrypi2 (BCM2836 or BCM2837 v1.2+)
    raspberrypi3 (BCM2837)
    raspberrypi-cm (BCM2835)
    raspberrypi-cm3 (BCM2837)
    
    
~/yocto/mbed-cloud-client-yocto-setup-restricted/rpi-build/conf/local.conf

    MACHINE = "mbed-cloud-client-rpi-machine"

## Raspberry user/password:  pi/raspberry

    sudo raspi-config
    sudo apt-get install -y raspberrypi-ui-mods  # add GUI to Raspbian Lite
    
<https://medium.com/@rosbots/ready-to-use-image-raspbian-stretch-ros-opencv-324d6f8dcd96>


<https://habr.com/post/330160/>    

<https://www.amazon.com/Coding-Bible-Manuscripts-Python-Raspberry/dp/1718943253>

<https://habr.com/company/unet/blog/407867/> MQTT on Rasb

<https://habr.com/company/unet/blog/373929/> Node Red

<https://etcher.io/>  SD card Writer

    bootcode.bin
    config.txt  
    start.elf

aarch64-none-elf  croos-compiler

Под Linux: https://habr.com/post/349248/

Загрузим и распакуем aarch64-none-elf-linux-x64.tar.gz. После этого переместим arch64-none-elf в /usr/local/bin:
wget https://web.stanford.edu/class/cs140e/files/aarch64-none-elf-linux-x64.tar.gz

    tar -xzvf aarch64-none-elf-linux-x64.tar.gz
    sudo mv aarch64-none-elf /usr/local/bin
    
Добавим /usr/local/bin/aarch64-none-elf/bin к переменной окружения PATH. Как именно — это зависит от вашего конкретного диструбутива Linux. В большинстве случаев следует добавить в ~/.profile следующее:

    PATH="/usr/local/bin/aarch64-none-elf/bin:$PATH"
Проверяем, всё ли нормально. В качетве вывода мы должны получить версию gcc и всё такое.

    aarch64-none-elf-gcc --version

Можно собрать самому из исходников, если такое желание возникнет. Подробнее вот тут.

<https://habr.com/post/357968/>    Pi 3 Model B+

<https://habr.com/post/320450/>


```
 which mbed-cli
/usr/local/bin/mbed-cli
russ@thing2:~$  mbed-cli --help
usage: mbed [-h] [--version]             ...

Command-line code management tool for ARM mbed OS - http://www.mbed.com
version 1.10.2

Use "mbed <command> -h|--help" for detailed help.
Online manual and guide available at https://github.com/ARMmbed/mbed-cli

optional arguments:
  -h, --help         show this help message and exit
  --version          print version number and exit

Commands:

    new              Create new mbed program or library
    import           Import program from URL
    add              Add library from URL
    remove           Remove library
    deploy           Find and add missing libraries
    publish          Publish program or library
    update           Update to branch, tag, revision or latest
    sync             Synchronize library references

    ls               View dependency tree
    releases         Show release tags
    status           Show version control status

    compile          Compile code using the mbed build tools
    test             Find, build and run tests
    device-management
                     device management subcommand
    export           Generate an IDE project
    detect           Detect connected Mbed targets/boards

    sterm            Open serial terminal to connected target.

    config           Tool configuration
    target           Set or get default target
    toolchain        Set or get default toolchain
    cache            Repository cache management
```    

## TLS MQTT 

<https://github.com/ArmMbedCloud/data-cloud-client-mqtt>

<https://os.mbed.com/users/vpcola/code/HelloMQTT/>   Vergil Cola

<https://os.mbed.com/users/coisme/code/HelloMQTT/> Osamu

<https://tls.mbed.org/kb/how-to/reduce-mbedtls-memory-and-storage-footprint>

## Cloud
https://cloud.mbed.com/docs/current/mbed-cloud-sdk-references/index.html .  JavaScript SDK

https://os.mbed.com/teams/mbed-os-examples/code/mbed-cloud-example/ .  

https://confluence.arm.com/display/IoTBU/Platforms+for+Cloud+Client+5-minute+guide

<https://os.mbed.com/search/?q=cloud>

<https://cloud.mbed.com/docs/current/cloud-requirements/tool-requirements.html>

<https://cloud.mbed.com/docs/current/service-api-references/mbed-cloud-connect.html>

<https://github.com/ARMmbed/mbed-cloud-client>

Lightweight Machine to Machine Technical Specification (LwM2M)
<http://openmobilealliance.org/release/LightweightM2M/V1_0-20170208-A/OMA-TS-LightweightM2M-V1_0-20170208-A.pdf>

<https://cloud.mbed.com/docs/current/connecting/qs-credentials.html>  get mbed_cloud_dev_credentials.c

<https://portal.mbedcloud.com/login>

<https://cloud.mbed.com/docs/current/account-management/users.html>

<https://cloud.mbed.com/docs/current/connecting/qs-compiling.html>

<https://cloud.mbed.com/docs/current/connecting/flashing-the-binary-to-the-device.html>

mbed compile -t GCC_ARM -m K64F --app-config configs/eth_v4.json

python tools/combine_bootloader_with_app.py -m K64F -a BUILD/K64F/GCC_ARM/mbed-cloud-client-example.bin -o combined.hex

https://connector.mbed.com/

<https://tedium.co/2018/06/07/acorn-arm-holdings-history/>  ARM history

## Cortex-A76
<https://www.anandtech.com/show/12785/arm-cortex-a76-cpu-unveiled-7nm-powerhouse>

<https://www.extremetech.com/computing/270550-are-arm-cpu-cores-finally-ready-to-fight-intel-for-the-laptop-market> 

## Trilllium
https://www.anandtech.com/show/12791/arm-details-project-trillium-mlp-architecture

## Rasberry
<https://www.macworld.co.uk/how-to/mac/how-to-set-up-raspberry-pi-3-with-mac-3637490/>

<https://dev.to/wiaio/set-up-a-raspberry-pi-without-an-external-monitor-or-keyboard--c88>

## Multithreading
https://os.mbed.com/docs/v5.8/reference/thread.html


## AWS IoT

<https://habr.com/ru/post/472216/>

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


## Wikipedia : private/public keys

<https://en.wikipedia.org/wiki/Public_key_certificate>

<https://en.wikipedia.org/wiki/Certificate_authority>

<https://en.wikipedia.org/wiki/Public_key_infrastructure>

<https://en.wikipedia.org/wiki/Transport_Layer_Security>

<https://habr.com/post/418857/> . check certs

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

## IoT Integration platform
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

## Mbed Online compiler

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

<https://habr.com/ru/company/advantech/blog/490346/>

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

## Embedded programming IDE

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
 


## DLMS

<https://www.dlms.com/documentation/index.html>

<https://docs.mbed.com/docs/mbed-os-api-ref/en/latest/APIs/communication/ethernet/>

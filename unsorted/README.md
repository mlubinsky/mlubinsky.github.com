<https://softwareengineering.stackexchange.com/questions/49550/which-hashing-algorithm-is-best-for-uniqueness-and-speed>

<http://www.cmsmagazine.ru/library/items/programming/80-problems-with-it-interviews/>

<https://news.ycombinator.com/item?id=17202615> some youtube channels

<https://habr.com/company/globalsign/blog/348988/> Mozilla IoT Things

## Yocto

<https://www.packtpub.com/virtualization-and-cloud/embedded-linux-development-using-yocto-projects-second-edition>

<https://hub.packtpub.com/building-our-first-poky-image-raspberry-pi/>

<http://www.instructables.com/id/Building-GNULinux-Distribution-for-Raspberry-Pi-Us/>

<https://medium.com/@shigmas/yocto-and-pi-ef8f1aa70231>

<http://git.yoctoproject.org/cgit/cgit.cgi/meta-raspberrypi>

<http://www.jumpnowtek.com/rpi/Raspberry-Pi-Systems-with-Yocto.html>

<https://himvis.com/bake-64-bit-raspberrypi3-images-with-yoctoopenembedded/>

local.conf . has variable MACHINE

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

## Raspberry . pi/raspberry

    sudo raspi-config
    
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

<https://www.youtube.com/watch?time_continue=1&v=wu3p7dxrhl8> Easter front animated 1941

## Architecture

<https://github.com/donnemartin/system-design-primer>

<https://engineering.videoblocks.com/web-architecture-101-a3224e126947>

<https://news.ycombinator.com/item?id=17522362>

<https://the-cloud-book.com/>

<https://www.goodreads.com/book/show/25686275-the-art-of-scalability>

<https://www.goodreads.com/book/show/18043011-clean-architecture>

## Jenkins

<https://www.automationqc.com/jenkins-pipeline-for-beginners/>

<https://godaddy.github.io/2018/06/05/cicd-best-practices/>

## RabbitMQ
<https://itnext.io/connecting-competing-microservices-using-rabbitmq-28e5269861b6>

## Vim

<https://curi0sity.de/en/2018/06/use-vim-as-a-simple-ide/>
 
<https://github.com/morhetz/gruvbox/wiki/Installation>   Color sheme gruvebox

## VisualStudio Code + Java
<https://flaviocopes.com/vscode/>

<https://code.visualstudio.com/docs/java/java-tutorial>

 VS Code can quickly show the diff between two files, with
 
 code --diff file1.js file2.js.

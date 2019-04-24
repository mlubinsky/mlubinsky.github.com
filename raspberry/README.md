diskutil list

If you're using a Mac with just one hard drive, then two appear: /dev/disk0 and /dev/disk1. 

If you have external hard drives, or more volumes, then there will be more drives.
```
 
/dev/disk0 (internal):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      GUID_partition_scheme                         500.3 GB   disk0
   1:                        EFI EFI                     314.6 MB   disk0s1
   2:                 Apple_APFS Container disk1         500.0 GB   disk0s2

/dev/disk1 (synthesized):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:      APFS Container Scheme -                      +500.0 GB   disk1
                                 Physical Store disk0s2
   1:                APFS Volume Macintosh HD            419.3 GB   disk1s1
   2:                APFS Volume Preboot                 58.5 MB    disk1s2
   3:                APFS Volume Recovery                1.5 GB     disk1s3
   4:                APFS Volume VM                      9.7 GB     disk1s4
```   

## SD card formatters

<https://www.balena.io/etcher/> .  Flash OS images to SD cards & USB drives, safely and easily.

<https://www.sdcard.org/downloads/formatter/>



<https://dev.to/wiaio/set-up-a-raspberry-pi-without-an-external-monitor-or-keyboard--c88>

<https://www.macworld.co.uk/how-to/mac/how-to-set-up-raspberry-pi-3-with-mac-3637490/>

<https://ronnyvdbr.github.io/RaspberryIPCamera> .  IP camera


<https://www.youtube.com/watch?v=L2XaFmt9xsA> . Remote   Desktop to Raspberry Pi from Apple Mac

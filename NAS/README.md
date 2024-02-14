### NetGear AX1800 WiFi 6 router 
Serial: 6MA62954A0529 unevenmoon759

###  NetGear ser manual
 
https://www.downloads.netgear.com/files/GDC/RAX10/RAX10_UM_EN.pdf

192.168.1.1 admin/V...7!

https://kb.netgear.com/980/How-do-I-log-in-to-my-NETGEAR-router

#### NetGear LEDs
https://kb.netgear.com/24244/What-do-the-LEDs-on-my-NETGEAR-router-mean
```
1. Power LED
2. Internet LED

3. WiFi LED

4. Ethernet LED
• Solid green. The router detected a 1 Gbps link with a device that is connected to
one of the router's Ethernet ports.
• Solid Amber. The router detected a 10/100 Mbps link with a device that is connected
to one of the router's Ethernet ports.
• Blinking green. One of the router's Ethernet ports is sending or receiving traffic at
1 Gbps.
• Blinking amber. One of the router's Ethernet ports is sending or receiving traffic
at 10/100 Mbps.
• Off. No device is connected to an Ethernet port.

5. WPS : Wi-fi Protected Setup
Pressing the WPS button on the back of the router lets your WPS-enabled device join
your router's WiFi network without typing the WiFi password. The WPS LED blinks
green during the WPS process and then lights solid green when the WPS-enabled
device connects to your router's WiFi network.

```

### ARRIS router: 10.0.0.1  admin/password1

### Synology Disk station DS-213+ station: 192.168.1.14

Finder -> Go -> Connect to Server:  smb://192.168.1.14

192.168.1.47

old: 10.0.0.83



old: smb://10.0.0.83 

admin/pereucet

http://10.0.0.83:5000/webman/index.cgi 

Dropdown list appears: select homes

https://kb.synology.com/en-in/DSM/tutorial/Quick_Start_External_Access

https://kb.synology.com/tr-tr/DSM/tutorial/Unable_to_Locate_NAS
```
You may find your Synology NAS via either of the following tools:

Web Assistant: Enter find.synology.com or synologynas:5000 (synologynas.local:5000 
for Mac computers) in the address bar of your web browser.

Synology Assistant: Open Synology Assistant desktop utility.  
```

https://nascompares.com/answer/can-i-connect-synology-diskstation-nas-directly-to-a-pc-or-mac/
```
Can I connect my Synology NAS directly to my computer?
If you want to connect your NAS directly, you can do it. 
Set up manual IP on your PC and NAS with a one in the same IP range. 
Than use Synology finder app or type IP in the address bar and it's done.
```

https://gizarena.com/connect-synology-nas-directly-to-pc-over-ethernet/

### Scan from HP printer to e-mail

https://www.youtube.com/watch?v=OM7PS-5D06A

https://h30434.www3.hp.com/t5/Scanning-Faxing-Copying/Scan-to-email-M283fdw/td-p/8318699



### NAS
 The DS220+ NAS has two LAN ports. 
 
 The LAN Port 2 is connected to the Router and
 
 the LAN Port 1 is connected to MacBook Pro via Ethernet port.

### Assign a static IP address in Mac or MacBook:
```
Go to System Preferences -> Network
Select the Ethernet port or External USB Ethernet Adapter
Change Configure IPv4 to Manually
Enter IP address as 192.167.1.201
Enter Subnet mask as 255.255.0.0
Select Apply
```

### Once you’re done with assigning static IP addresses to both PC and NAS: 

connect the Synology NAS to Mac or PC using the Ethernet Cable. Here, I connected Port 1 to Mac because the static IP address is configured to Port 1. You can use an ethernet port on the NAS that has a static IP address but, you should use the same IP range on the PC.
```
Open Synology Assistant
Click on Search
Your PC or Laptop will detect the Synology NAS connected over Ethernet
```

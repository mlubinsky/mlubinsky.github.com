### Useful embedded in MacOS   utils
https://ss64.com/mac/  
https://notes.billmill.org/computer_usage/mac_os/mac_os_command_line_programs.html  
https://terminaltrove.com/categories/macos/  
https://blog.xoria.org/macos-tips/  
https://saurabhs.org/macos-tips  
https://news.ycombinator.com/item?id=42057431  
https://news.ycombinator.com/item?id=36491704 

https://lobste.rs/s/qgfqw3/macos_tips

### Keeping Mac awake
https://ss64.com/mac/caffeinate.html

https://github.com/newmarcel/KeepingYouAwake  
https://apps.apple.com/us/app/amphetamine/id937984704  


caffeinate -disu

### choose-an-app-to-open-a-file-on-mac
https://support.apple.com/guide/mac-help/choose-an-app-to-open-a-file-on-mac-mh35597/mac

### keyboard shortcats

Chrome has tab search. In MacOS: Shift+Cmd+A

https://shortcat.app/

https://www.homerow.app/


$ sw_vers
```
ProductName:	Mac OS X
ProductVersion:	10.14.6
BuildVersion:	18G95
```

https://lobste.rs/s/d5qwzs/what_is_your_mac_os_setup

### See versions of brew-installed packages:

brew list --versions

### Far and mc (Midnight commander)  for Mac

brew install --cask far2l

https://github.com/spvkgn/far2l-portable/releases

https://github.com/elfmz/far2l

https://github.com/akruphi/far2l/wiki

https://github.com/akruphi/far2l/wiki/far2l-vs-mc
 
### Command-line utils in MacOS:

https://saurabhs.org/advanced-macos-commands

https://news.ycombinator.com/item?id=36491704

open -e opens the file in TextEdit, in plain-text mode by default.

sample PROCESS SECS spends SECS seconds watching the process (name or pid) PROCESS, then outputs a stack-based profile. You can do this from Activity Monitor, but I often find it faster to do from the CLI.

### Setup

https://blog.scriptmint.com/my-macbook-setup-for-development-2024-caefe65d8bfb

https://blog.scriptmint.com/the-5-macos-apps-that-improved-my-productivity-f5b687269222

https://habr.com/ru/post/672510/ from Linux to Mac

https://earthly.dev/blog/homebrew-on-m1/ Homebrew on Mac1

https://hackercodex.com/guide/python-development-environment-on-mac-osx/.  Python

https://hookrace.net/blog/macos-setup/

https://news.ycombinator.com/item?id=29742551

<https://lobste.rs/s/uzdehw/what_should_i_do_after_getting_my_first_own>


https://app.vnote.fun/en_us/



### Dosk space

https://pawelurbanek.com/macos-free-disk-space   

brew install --cask disk-inventory-x

brew install awk coreutils findutils gnu-tar gnu-sed gnu-which gnu-time
 
 
 
 ### “Permission denied @ apply2files” 

https://stackoverflow.com/questions/61899041/permission-denied-apply2files-usr-local-lib-node-modules-expo-cli-node-modu

Reset permissions to /user/local.  
```
sudo chown -R $(whoami):admin /usr/local/* \
&& sudo chmod -R g+rwx /usr/local/*
``` 
 
 ### Preview
 
https://www.fourth-wall.co.uk/post/10-tips-for-preview-the-default-mac-app-that-people-forget-about

https://news.ycombinator.com/item?id=31315110
 

https://kapeli.com/dash

https://thume.ca/2020/09/04/macos-tips/

https://github.com/orf/crontabula Parse crontab expression in Python

https://github.com/yukondude/Scripnix

### Mac shortcuts

<https://support.apple.com/en-us/HT201236>

<https://news.ycombinator.com/item?id=24091707>

Page Up:  Fn + Up Arrow 

### Finder - how to go to parent directory

Command+↑ (Command + Up Arrow) 

https://www.mediaatelier.com/CheatSheet/

https://habr.com/ru/company/jugru/blog/573936/

Cmd+Q ("command quit") — выход из приложения

Cmd+H ("command hide") — скрыть окно

Cmd+F ("command find") — поиск

Cmd+C ("command copy") — копирование

Cmd+↑ ("command up") — переход на уровень выше

Cmd+↓ ("command down") — переход на уровень ниже
 
Cmd+ ~ next window of same app

### From Linux to Mac
https://habr.com/ru/post/588380/  Linux -> Mac

https://habr.com/ru/company/vdsina/blog/507016/ Mac-> Linux

### Chrome extensions

Include at the end 
of your ~/.bashrc, ~/.bash_profile or ~/.aliases the following lines:

 Google Chrome Alias
```
google-chrome() {
    open -a "Google Chrome" "$1"
}
```

https://chrome.google.com/webstore/detail/json-formatter/cfaihfocdnniaholfnjcemnfhcjchohb/related?hl=en. JSON formatter

The great suspender

https://www.zdnet.com/article/google-kills-the-great-suspender-heres-what-you-should-do-next/

chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=The%20Great%20Suspender%20-%20Chrome%20Web%20Store&pos=0&uri=https://chrome.google.com/webstore/detail/the-great-suspender/klbibkeccnjlkjkiokjodocebajanakg/related

The session buddy

chrome-extension://klbibkeccnjlkjkiokjodocebajanakg/suspended.html#ttl=Session%20Buddy%20-%20Chrome%20Web%20Store&pos=0&uri=https://chrome.google.com/webstore/detail/session-buddy/edacconmaakjimmfgnblocblbcdcpbko/related

### Python setup

https://github.com/simonw/til/blob/main/python/macos-catalina-sort-of-ships-with-python3.md

on MacOS Catalina
```
  which python3
/usr/bin/python3
  python3 -V
Python 3.8.2
  python -V
Python 2.7.16
```

https://peter-whittaker.com/install-python-MacOS

<https://hackercodex.com/guide/python-development-environment-on-mac-osx/>

https://ruddra.com/fix-python-after-brew-upgrade/

<https://gist.github.com/chris-zen/9e61db6924bd37fbe414f648614ca4c5>


### brew  


brew list
```
apache-spark	jq		oniguruma	openjdk@11	pcre2		ripgrep
```

ls /opt/homebrew/Cellar
```
apache-spark jq           oniguruma    openjdk@11   pcre2        ripgrep
```

ls /opt/homebrew/bin
```
brew                 jq                   onig-config          pcre2test            run-example          spark-shell          sparkR
docker-image-tool.sh load-spark-env.sh    pcre2-config         pyspark              spark-beeline        spark-sql
find-spark-home      meld                 pcre2grep            rg
```

ls /opt/homebrew/opt/

### Pyspark issue

Anaconda's pyspark fails:

which pyspark
/Users/mlubinsky/opt/anaconda3/bin/pyspark

/Users/mlubinsky/opt/anaconda3/lib/python3.9/site-packages/pyspark/bin/spark-class: line 96: CMD: bad array subscript
head: illegal line count -- -1


But homebrew Pyspark works:

/opt/homebrew/bin/pyspark

###   Java on Mac

```
brew install java
For the system Java wrappers to find this JDK, symlink it with
  sudo ln -sfn /opt/homebrew/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

openjdk is keg-only, which means it was not symlinked into /opt/homebrew,
because macOS provides similar software and installing this software in
parallel can cause all kinds of trouble.

If you need to have openjdk first in your PATH, run:
  echo 'export PATH="/opt/homebrew/opt/openjdk/bin:$PATH"' >> ~/.zshrc

For compilers to find openjdk you may need to set:
  export CPPFLAGS="-I/opt/homebrew/opt/openjdk/include"

==> Summary
  /opt/homebrew/Cellar/openjdk/19.0.2:
  
  
ls  /opt/homebrew/opt/ | grep java
java
java11

ls  /opt/homebrew/opt/ | grep openjdk
openjdk
openjdk@11
openjdk@19  
  
```

  brew install jenv 
  
To activate jenv, add the following to your /Users/miclub01/.bash_profile:

  export PATH="$HOME/.jenv/bin:$PATH"
  eval "$(jenv init -)"
```
 echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.bash_profile
 echo 'eval "$(jenv init -)"' >> ~/.bash_profile
 
 brew tap AdoptOpenJDK/openjdk
 brew  install --cask adoptopenjdk8

ls /Library/Java/JavaVirtualMachines
adoptopenjdk-8.jdk 
jdk-15.0.1.jdk

jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home

jenv versions
* system (set by /Users/miclub01/.jenv/version)
  1.8
  1.8.0.282
  openjdk64-1.8.0.282
  
  jenv global openjdk64-1.8.0.282
  
```
<https://medium.com/@danielnenkov/multiple-jdk-versions-on-mac-os-x-with-jenv-5ea5522ddc9b>

<https://medium.com/@brunofrascino/working-with-multiple-java-versions-in-macos-9a9c4f15615a> 

https://dev.to/gabethere/installing-java-on-a-mac-using-homebrew-and-jevn-12m8

### Install Spark

https://medium.com/@le.oasis/setting-up-apache-spark-on-macos-a-comprehensive-guide-78af7642deb1

brew install apache-spark

/opt/homebrew/Cellar/apache-spark/3.5.0/bin
```
docker-image-tool.sh 
load-spark-env.sh    r
run-example          
spark-class          
spark-shell          
spark-submit
find-spark-home      
pyspark              
spark-beeline        
spark-connect-shell  
spark-sql            
sparkR
```

#### Scala and  Spark

https://notadatascientist.com/install-spark-on-macos/

brew tap eddies/spark-tap

brew install scala@2.11
```
scala@2.11 is keg-only, which means it was not symlinked into /usr/local,
because this is an alternate version of another formula.

If you need to have scala@2.11 first in your PATH, run:
  echo 'export PATH="/usr/local/opt/scala@2.11/bin:$PATH"' >> /Users/mlubinsky/.bash_profile
```

brew install apache-spark@2.4.6

```
brew install scala@2.12
 pwd
/usr/local/opt
[opt]$ ls -ltr | grep scala
lrwxrwxr-x  1 mlubinsky  admin  30 Aug 29  2021 scala@2.11 -> ../Cellar/scala@2.11/2.11.12_1
lrwxr-xr-x  1 mlubinsky  admin  28 Jul  7 15:07 scala@2.12 -> ../Cellar/scala@2.12/2.12.14
```


### CyberChef
https://gchq.github.io/CyberChef

https://github.com/gchq/CyberChef


### Useful Apps

https://app.vnote.fun/en_us/

https://tinyapps.org/macos.html

https://github.com/muesli/duf disk usage 

https://cyberduck.io/

https://devutils.app

https://apps.apple.com/us/app/boop/id1518425043?mt=12 Boop

http://ridiculousfish.com/hexfiend/

<https://news.ycombinator.com/item?id=24604291>

<https://thume.ca/2020/09/04/macos-tips/>

<https://wiki.nikitavoloboev.xyz/macos/macos-apps>

<https://twitter.com/craigmod/status/1268788533990289409>

<https://github.com/learn-anything/macos-apps>

### diff tools
https://github.com/dandavison/delta

<https://www.jefftk.com/icdiff>

<https://news.ycombinator.com/item?id=23744381>

## Rigrep
```
brew install rigrep
rg Logistic tensorflow
```
https://github.com/BurntSushi/ripgrep


https://wiki.nikitavoloboev.xyz/macos

https://github.com/iCHAIT/awesome-macOS

https://github.com/nikitavoloboev/knowledge

https://lobste.rs/s/aqwsn5/praise_autohotkey



###  NNN - terminal navigator

https://github.com/jarun/nnn



### Split screen verically

<https://support.apple.com/en-us/HT204948>

<https://youtu.be/cYGrlEtqaVw>


### Apps 
<https://github.com/ytdl-org/youtube-dl/> youtube downloader

<https://news.ycombinator.com/item?id=22849208>

<https://lukemil.es/blog/software-i-like>

### SSH
<https://stackoverflow.com/questions/24392657/adding-an-rsa-key-without-overwriting>

```
Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa_private_server
  IdentityFile ~/.ssh/id_rsa_github
  IdentityFile ~/.ssh/id_rsa_work_server
```

## Spaces - Virtual desktops

<https://www.howtogeek.com/180677/mission-control-101-how-to-use-multiple-desktops-on-a-mac/>

<https://support.apple.com/guide/mac-help/work-in-multiple-spaces-mh14112/mac>

<https://support.apple.com/guide/mac-help/open-windows-spaces-mission-control-mh35798/10.15/mac/10.15>

<https://appleinsider.com/articles/18/10/12/how-to-use-spaces-apples-mostly-ignored-macos-mojave-productivity-feature>

f you have a trackpad, swipe upwards with four fingers. This gets you the Mac's Expose feature where windows from every open application are shown to you in thumbnails. However, at the very top of the screen lies the Spaces feature. 

You can also get to this by holding the Control key and tapping the up arrow

 you can also switch between spaces with a keystroke: Control and 1 takes you to Desktop 1, Control and 2 to Desktop 2 and so on. You can move to any of your first 10 spaces this way: to get to 10 you press Control-0. If this isn't working for you, check System Preferences, Keyboard, Shortcuts. Select Mission Control and you will see that some or all Spaces shortcuts have been unchecked.

## Japan

<https://support.apple.com/guide/mac-help/international-fonts-display-correctly-mac-mchl14cc6599/mac>

## Windows managers for Mac

https://taoofmac.com/space/apps/window_managers

<https://www.sempliva.com/tiles/>

<https://magnet.crowdcafe.com/> Magnet not free

<https://rectangleapp.com/> 

<https://github.com/koekeishiya/yabai>

 

<https://ianyh.com/amethyst/> Amethyst

<https://setapp.com/apps/mosaic> Mosaic

<https://github.com/appalaszynski/mac-setup>
```
==> python
Python has been installed as
  /usr/local/bin/python3

Unversioned symlinks `python`, `python-config`, `pip` etc. pointing to
`python3`, `python3-config`, `pip3` etc., respectively, have been installed into
  /usr/local/opt/python/libexec/bin

If you need Homebrew's Python 2.7 run
  brew install python@2

You can install Python packages with
  pip3 install <package>
They will install into the site-package directory
  /usr/local/lib/python3.7/site-packages
```    
  <https://docs.brew.sh/Homebrew-and-Python>

### mysqlclient python macOS

<https://www.peterbe.com/plog/ld-library-not-found-for-lssl-mysqlclient-python-macos>


### brew

brew list
```
freetds		libtool		openjdk		pcre2		readline	unixodbc
kafka		mysql@5.7	openssl@1.1	postgresql@9.6	ripgrep		zookeeper
adoptopenjdk8
```
brew services
```
kafka          stopped
mysql@5.7      stopped
postgresql@9.6 stopped
zookeeper      stopped
```



<https://news.ycombinator.com/item?id=21253850>

<https://dbngin.com/> . Free All-in-One Database Version Management Tool




<https://github.com/serhii-londar/open-source-mac-os-apps>

<https://chrome.google.com/webstore/detail/web-sniffer/ndfgffclcpdbgghfgkmooklaendohaef?hl=en> Web Sniffer Chrome extension

<https://zenworkpro.com/2018/08/14/computer-ergonomics-useful-tips-for-working-in-macos>

<https://github.com/serhii-londar/open-source-mac-os-apps>    Open source Mac OS apps

<https://www.mediaatelier.com/CheatSheet/>

<https://github.com/RafalWilinski/s3-uploader>   Upload file to S3

https://github.com/720kb/ndm  UI for npm

https://github.com/vsaravind007/nodeScratchpad   Run JS code snippets

<https://github.com/wellsjo/JSON-Splora>  JSON manipulation


### File compare
<https://yousseb.github.io/meld/>

<https://www.kaleidoscopeapp.com/>

### FTP SFTP S3
<https://panic.com/transmit/> .  S3, FTP, etc

<https://cyberduck.io/> .  free



### Anaconda on Mac:

<https://stackoverflow.com/questions/45684618/having-default-mac-python-2-7-and-anaconda-python-3>

<https://towardsdatascience.com/how-to-successfully-install-anaconda-on-a-mac-and-actually-get-it-to-work-53ce18025f97>

```
bash ./Anaconda3-2019.07-MacOSX-x86_64.sh

Preparing transaction: done
Executing transaction: \ b''
| WARNING conda.core.envs_manager:register_env(46): Unable to register environment. Path not writable or missing.
  environment location: /Users/miclub01/anaconda3
  registry file: /Users/miclub01/.conda/environments.txt
done
installation finished.
Do you wish the installer to initialize Anaconda3
by running conda init? [yes|no]
[yes] >>> yes
no change     /Users/miclub01/anaconda3/condabin/conda
no change     /Users/miclub01/anaconda3/bin/conda
no change     /Users/miclub01/anaconda3/bin/conda-env
no change     /Users/miclub01/anaconda3/bin/activate
no change     /Users/miclub01/anaconda3/bin/deactivate
no change     /Users/miclub01/anaconda3/etc/profile.d/conda.sh
no change     /Users/miclub01/anaconda3/etc/fish/conf.d/conda.fish
no change     /Users/miclub01/anaconda3/shell/condabin/Conda.psm1
no change     /Users/miclub01/anaconda3/shell/condabin/conda-hook.ps1
no change     /Users/miclub01/anaconda3/lib/python3.7/site-packages/xontrib/conda.xsh
no change     /Users/miclub01/anaconda3/etc/profile.d/conda.csh
modified      /Users/miclub01/.bash_profile

==> For changes to take effect, close and re-open your current shell. <==

If you'd prefer that conda's base environment not be activated on startup,
   set the auto_activate_base parameter to false:

conda config --set auto_activate_base false

Thank you for installing Anaconda3!




python -V .    Python 3.7.3
conda create --name deepCognition python=3.7.3

#
# To activate this environment, use
#
#     $ conda activate deepCognition
#
# To deactivate an active environment, use
#
#     $ conda deactivate

(base) [arm-space-analytics](master)$ conda activate deepCognition
(deepCognition) [arm-space-analytics](master)$


conda activate deepCognition
pip -V
pip 19.1.1 from /Users/miclub01/anaconda3/envs/deepCognition/lib/python3.7/site-packages/pip (python 3.7)

```


### Color command line
<https://www.cyberciti.biz/faq/apple-mac-osx-terminal-color-ls-output-option/>
```
alias ls='ls -G'
alias ll='ls -lG'

ls -G
```
### ~/.bash_profile

    #### Tell ls to be colourful
    export CLICOLOR=1
    export LSCOLORS=Exfxcxdxbxegedabagacad
 
    #### Tell grep to highlight matches
    export GREP_OPTIONS='--color=auto'
    
    #### Show Git branch in color
    git_branch() {
       git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
    }
    
    export PS1="[\W]\[\033[00;32m\]\$(git_branch)\[\033[00m\]\$ "

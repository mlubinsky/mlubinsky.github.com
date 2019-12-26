
## Расширение Visual Studio Code: Remote — SSH 
<https://habr.com/ru/company/microsoft/blog/472274/>
 Remote — SSH позволяет подключаться к удаленной машине или виртуальной машине с использованием SSH, 
 и все изнутри VS Code.
 
 
Pexpect is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. Pexpect works like Don Libes’ Expect. 
Pexpect allows your script to spawn a child application and control it as if a human were typing commands. 
<https://pexpect.readthedocs.io/en/stable/> pexpect

<https://github.com/fgimian/paramiko-expect>

<https://www.booleanworld.com/set-ssh-keys-linux-unix-server/>

https://habr.com/post/435546/  


### SSH from Python

<https://janakiev.com/blog/python-shell-commands/>
```
import subprocess

ssh = subprocess.Popen(["ssh", "-i .ssh/id_rsa", "user@host"],
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        universal_newlines=True,
                        bufsize=0)
 
# Send ssh commands to stdin
ssh.stdin.write("uname -a\n")
ssh.stdin.write("uptime\n")
ssh.stdin.close()

# Fetch output
for line in ssh.stdout:
    print(line.strip())
    
```    

### TUNNELS
https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-ssh-config/  
  
https://hackertarget.com/ssh-examples-tunnels/

https://news.ycombinator.com/item?id=18775604  
  
https://solitum.net/an-illustrated-guide-to-ssh-tunnels/

https://www.everythingcli.org/ssh-tunnelling-for-fun-and-profit-autossh/  autossh

https://www.opoet.com/pyro/

```
ssh-keygen -t dsa
default folder /home/user/data/.ssh/id_dsa
~/.ssh/id_dsa  ~/.ssh/id_dsa.pub
```
copy public key on server:
```
ssh user@hostname 
"umask 077; cat >> .ssh/authorized_keys" < ~/.ssh/id_dsa.pub
```
To avoid yyping logins  in ~/.ssh/config, add:
```
Host host
User user
Hostname hostname
```

http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/

https://habrahabr.ru/post/122445/

https://habrahabr.ru/post/331348/

https://habrahabr.ru/post/39116/

https://habrahabr.ru/post/142717/

https://habrahabr.ru/post/150047/ ssh+python

http://mah.everybody.org/docs/ssh

https://blog.jetbrains.com/pycharm/2017/08/ssh-agent-simplify-ssh-keys/ PuTTY

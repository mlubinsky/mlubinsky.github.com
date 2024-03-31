### SSH-Туннели простыми словами

https://habr.com/ru/articles/804263/

### Executing remote command via SSH

https://news.ycombinator.com/item?id=27483077

https://plumbum.readthedocs.io/en/latest/remote.html

https://iapyeh.github.io/sshscript/index

### SSH tips and tricks

https://news.ycombinator.com/item?id=32486031

### SSL TLS explained

https://news.ycombinator.com/item?id=23096166

### OAuth 2
https://medium.com/dailyjs/what-every-software-engineer-should-know-about-oauth-2-0-10f0ef4998e5

#### How to manage ssh keys

https://www.paepper.com/blog/posts/how-to-properly-manage-ssh-keys-for-server-access/

### VSCode via SSH

https://jlelse.blog/dev/code-using-vps/

# cURL and SSH , detach from terminal

### Ctrl-Z bg fg jobs disown 

<https://superuser.com/questions/178587/how-do-i-detach-a-process-from-terminal-entirely>
If a process is already in execution, such as the logg running  tar,  
simply press ``Ctrl+Z`` to stop it then enter the command ``bg`` to continue with its execution in the background as a job.
``jobs` show all your background jobs. 
However, its stdin, stdout, stderr are still joined to the terminal.

also you may use &:
```
 tar -czf  my.tar.gz . &
 jobs
```

``disown`  is used after the a process has been launched and put in the background, it’s work is to remove a shell job from the shell’s active list jobs,
 when you close the controlling terminal, the job will not hang or send a SIGHUP to any child jobs.
 
 ```disown -h %1```
 You cannot apply ``nohup`` to running process.
  Unlike nohup, disown is used after the process has been launched and backgrounded.
```
my_command &
disown
```
 
### CURL

<https://nordicapis.com/understanding-the-hidden-powers-of-curl/>

### HTTP cURL httpie

<https://jvns.ca/blog/2019/08/27/curl-exercises/>

<https://catonmat.net/cookbooks/curl>

<https://linuxize.com/post/curl-command-examples/>

<https://nordicapis.com/understanding-the-hidden-powers-of-curl/>

<https://curl.haxx.se/book.html> Curl book

Curl to python request:
<https://curl.trillworks.com/>

<https://ryan.govost.es/http-translator/>

<https://github.com/spulec/uncurl>

<https://github.com/asciimoo/wuzz>

### curl alternatives

httpie  https://github.com/jakubroztocil/httpie  
insomnia
postmam


in my .bash_aliases
This will output the HTTP status code for a given URL.

     alias hstat="curl -o /dev/null --silent --head --write-out '%{http_code}\n'" $1 
     
### Example
```
#!/bin/bash
    set -e

    download_command () {
        if type wget >/dev/null 2>&1; then
            echo "wget -q -O-"
        elif type curl >/dev/null 2>&1; then
            echo "curl -sL"
        else
            echo "Error: curl or wget is required" >&2
            exit 1
        fi
    }

    download=$(download_command)
    public_v4=$($download http://whatismyip.akamai.com/)
    public_v6=$($download http://ipv6.whatismyip.akamai.com/)
```

## Расширение Visual Studio Code: Remote — SSH 
<https://habr.com/ru/company/microsoft/blog/472274/>
 Remote — SSH позволяет подключаться к удаленной машине или виртуальной машине с использованием SSH, 
 и все изнутри VS Code.
 
 
Pexpect is a pure Python module for spawning child applications; controlling them; and responding to expected patterns in their output. Pexpect works like Don Libes’ Expect. 
Pexpect allows your script to spawn a child application and control it as if a human were typing commands. 
<https://pexpect.readthedocs.io/en/stable/> pexpect

<https://github.com/fgimian/paramiko-expect>

## SSH 

https://www.reddit.com/r/Python/comments/jxxncp/sshcontroller_a_small_package_to_easily_run_ssh/ sshcontroller

https://gravitational.com/blog/ssh-config/ 

<https://smallstep.com/blog/ssh-tricks-and-tips/>

<https://news.ycombinator.com/item?id=23025756>

<https://gravitational.com/blog/how-to-ssh-properly/>

<https://www.wagner.pp.ru/fossil/advice/doc/trunk/ssh.md>

<https://www.booleanworld.com/set-ssh-keys-linux-unix-server/>

<https://habr.com/post/435546/>

https://habr.com/ru/company/skillbox/blog/529702/

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

https://news.ycombinator.com/item?id=26053323

https://unix.stackexchange.com/a/118650/289353

https://robotmoon.com/ssh-tunnels/

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

https://www.freecodecamp.org/news/how-to-manage-multiple-ssh-keys/

```
ssh-add -l    (show)
ssh-add -D (clear)
ssh-add my)id_rsa

cat ~/.ssh/config

Host gitlab.eng.roku.com
	   HostName gitlab.eng.roku.com
	   User git
	   IdentityFile ~/.ssh/original_id_rsa
	   IdentitiesOnly yes


```
http://nerderati.com/2011/03/17/simplify-your-life-with-an-ssh-config-file/

https://habrahabr.ru/post/122445/

https://habrahabr.ru/post/331348/

https://habrahabr.ru/post/39116/

https://habrahabr.ru/post/142717/

https://habrahabr.ru/post/150047/ ssh+python

http://mah.everybody.org/docs/ssh

https://blog.jetbrains.com/pycharm/2017/08/ssh-agent-simplify-ssh-keys/ PuTTY

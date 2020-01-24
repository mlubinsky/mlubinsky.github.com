.vimrc

.bash_profile

<https://www.bottomupcs.com/index.xhtml> how linux works

<https://news.ycombinator.com/item?id=21711761> . command-line utils

<https://www.shellcheck.net/>

<https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html>

<https://www.pixelstech.net/article/1326641280-Useful-Bash-Scripts>

<https://www.pixelstech.net/article/1377917732-Server-monitoring-shell-scripts>

<https://mywiki.wooledge.org/BashGuide>

<https://news.ycombinator.com/item?id=22027809> $@ . 
https://mywiki.wooledge.org/BashGuide
```
 A shebang is basically just a line (always the first line) in a file which tells the operating system what program to invoke to execute the script. There are different shells beyond just bash, so shellcheck wants to know which flavor the shell is written for and uses the shebang to figure it out.
 

Pick the user's bash from PATH environment:
    #!/usr/bin/env bash
Or specify a specific bash:
    #!/bin/bash
Or use whatever plain-shell is installed:
    #!/bin/sh
Or maybe it's a Python script:
    #!/usr/bin/env python3
Or it's a text file:
    #!/usr/bin/env vi
```

```
set -e . # exit on any non zero return code ( set -o errexit )
Unfortunately it means you can't check $? as bash will never get to the checking code if it isn't zero. 


set -x . # echo any command ( set -o xtrace )
set -u . exit on any attempts to use uninitialised variables
set -euf

!! – repeat last command

sudo !!  runs the previous command as root

!$ - repeats the last argument of the last command, example:

mkdir longDirectoryNameIDontWantToTypeAgain
cd !$

$?  - return code of last command
```

Given: text file and you need to remove all of its duplicate lines.
<https://opensource.com/article/19/10/remove-duplicate-lines-files-awk>

awk '!visited[$0]++' your_file > deduplicated_file

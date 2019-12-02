.vimrc

.bash_profile

<https://www.shellcheck.net/>

<https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html>

``
set -e . # exit on any non zero return code .  set -o errexit
set -x . # echo any command . set -o xtrace
set -u . exit on any attempts to use uninitialised variables
set -euf

!! – repeat last command

sudo !!  runs the previous command as root

!$ - repeats the last argument of the last command, example:

mkdir longDirectoryNameIDontWantToTypeAgain
cd !$

$?  - return code of last command
``

Given: text file and you need to remove all of its duplicate lines.
<https://opensource.com/article/19/10/remove-duplicate-lines-files-awk>

awk '!visited[$0]++' your_file > deduplicated_file

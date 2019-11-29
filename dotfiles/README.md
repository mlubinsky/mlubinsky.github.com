.vimrc

.bash_profile

<https://blog.flowblok.id.au/2013-02/shell-startup-scripts.html>

``
set -e . # exit on any non zero return code .  set -o errexit
set -x . # echo any command . set -o xtrace
set -u . exit on any attempts to use uninitialised variables
set -euf

!! – repeat last command
!$ - repeats the last argument of the last command

$?  - return code of last command
``

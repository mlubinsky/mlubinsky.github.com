<https://zaiste.net/posts/shell-commands-rust/> many command line tools in Rust (procs!, fd)

<http://cb.vu/unixtoolbox.xhtml>

<https://neilkakkar.com/unix.html>

<https://likegeeks.com/linux-process-management>

<https://news.ycombinator.com/item?id=24100002>

<https://natanyellin.com/posts/tracking-running-processes-on-linux/>

## GCC
```
Yes, it's  y possible  to have multiple versions of GCC installed on Ubuntu.  Here's how and why you might do it:

How to Install Multiple GCC Versions:

Using apt (for versions in the repositories):

sudo apt update  # Refresh package list
sudo apt install gcc-<version> g++-<version>
Replace <version> with the specific version you want (e.g., gcc-11, g++-11, gcc-12, g++-12). This will install the specified GCC and G++ compilers alongside your existing ones.

Using PPAs (for newer or specific versions):

Add the appropriate PPA (e.g., ubuntu-toolchain-r/test) and then use apt as described above.

sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt update

Be very careful with PPAs and understand the risks before using them.

Building from source (for maximum control):

This is more advanced but gives you the most control.  You download the GCC source code, configure it with a different installation prefix (e.g., /usr/local/gcc-13), compile, and install it. This keeps it entirely separate from the system's default GCC.

Switching Between GCC Versions:

The update-alternatives command is the standard way to manage multiple versions of commands like gcc and g++:

Check available alternatives:

sudo update-alternatives --config gcc
sudo update-alternatives --config g++
This will show you the available GCC and G++ versions and allow you to select the default one.

Setting the default:

The update-alternatives command will present a menu.  Choose the number corresponding to the GCC version you want to use as the default.

 
Environment variables:
You can use environment variables (like PATH) to control which GCC version is used in a specific terminal or script.
cc and c++ symlinks:
The cc and c++ commands are often symbolic links to the default GCC and G++ compilers. update-alternatives manages these links.
 The update-alternatives command provides a clean way to manage and switch between them.
```

## How pipe is implemented

https://news.ycombinator.com/item?id=22704774>

## incron vs inotify

https://www.linux-magazine.com/Issues/2014/158/Monitoring-with-incron

## strace
<https://habr.com/ru/company/badoo/blog/493856/>


## Make Makefile

https://makefiletutorial.com/

https://danyspin97.org/blog/makefiles-best-practices/

http://gabarro.org/ccn/makemath.html

https://tech.davis-hansson.com/p/make/

https://25thandclement.com/~william/cuda/Makefile.md.html

https://latedev.wordpress.com/2014/11/08/generic-makefiles-with-gcc-and-gnu-make/

https://labs.tomasino.org/makefiles-for-fun-and-profit/

https://antonz.org/makefile-automation/

https://ricardoanderegg.com/posts/makefile-python-project-tricks/

https://news.ycombinator.com/item?id=32303193

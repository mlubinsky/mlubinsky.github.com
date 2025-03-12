sudo ln -s /usr/bin/python3 /usr/bin/python

https://www.linux.org.ru/

<https://zaiste.net/posts/shell-commands-rust/> many command line tools in Rust (procs!, fd)

<http://cb.vu/unixtoolbox.xhtml>

<https://neilkakkar.com/unix.html>

<https://likegeeks.com/linux-process-management>

<https://news.ycombinator.com/item?id=24100002>

<https://natanyellin.com/posts/tracking-running-processes-on-linux/>


### No space left on device
```
 Check Disk Space Usage

df -h:

This command shows disk space usage in a human-readable format.
Look for the partition that's at 100% (or very close). This is the one you need to focus on.
2. Identify Space Hogs

du -sh *:

In the directory you suspect is full (often / or /home), this command shows the size of each file and directory.
The -s option summarizes the size of each directory, and -h makes the output human-readable.

du -a / | sort -rh | head -n 20
: This command will show the 20 largest files and directories on your entire system.

3. Common Culprits and How to Clean Them

Temporary Files:

sudo rm -rf /tmp/*
: Clears temporary files (use with caution, as some applications might be using them).   
sudo rm -rf ~/.cache/*
: Clears application caches in your home directory.

Log Files:

sudo truncate -s 0 /var/log/*
: Empties log files (useful for troubleshooting, but be aware you'll lose recent logs).

Package Cache:

sudo apt-get clean: Removes downloaded package files that are no longer needed.   
sudo apt-get autoclean: Removes old downloaded package files.   
Old Kernels:

dpkg -l | grep linux-image
: Lists installed kernels.
sudo apt-get remove linux-image-old-kernel-version
: Removes old kernels (make sure you're not removing the one you're currently using!).

Unused Applications:

sudo apt-get remove package-name: Removes unused applications.
Browser Cache:

Clear your browser's cache and download history.
Large Files:

Use the du command to find large files you no longer need and delete them.
Important Notes:

Be Careful: When deleting files, especially with sudo, double-check what you're removing.
System Files: Avoid deleting system files unless you know what you're doing.
find Command: The find command can be very powerful for locating specific types of files.
For example,

find . -name "*.log" will find all files ending in ".log"  

```

## GCC
```

Installing GCC 14 on Ubuntu can be done in a couple of ways, but the most common and generally recommended approach is building from source.  PPAs might have GCC 14 at some point, but building from source gives you the most control. Here's a comprehensive guide:

1. Prerequisites:

Essential build tools:
Bash

sudo apt update
sudo apt install build-essential
Required libraries (may vary slightly depending on your system):
Bash

sudo apt install libmpfr-dev libgmp-dev libmpc-dev
Download the GCC source code: Go to the official GNU GCC website (https://gcc.gnu.org/) and find the link to the GCC 14 source code (likely a .tar.gz or .tar.xz file). Download it. Let's assume you download it to your ~/Downloads directory.
2. Extract the Source Code:

Bash

cd ~/Downloads
tar -xf gcc-14.*.tar.gz  # Replace with the actual filename
cd gcc-14.*            # Go into the extracted directory
3. Create a Build Directory:

It's crucial to build GCC outside the source directory. This keeps things organized.

Bash

mkdir build-gcc-14
cd build-gcc-14
4. Configure GCC:

This is the most important step.  The --prefix option specifies where GCC will be installed.  Do not install it in a system directory like /usr or /usr/local directly unless you really know what you're doing.  It's best to keep it separate.

Bash

../gcc-14.*/configure --prefix=/usr/local/gcc-14 --enable-languages=c,c++ --disable-multilib
--prefix=/usr/local/gcc-14: This tells the build system to install GCC in /usr/local/gcc-14. You can choose any directory you want.
--enable-languages=c,c++: This enables support for C and C++. You can add other languages if needed (e.g., fortran, go).
--disable-multilib: This disables support for building 32-bit code on a 64-bit system. If you need multilib, omit this option. However, it can simplify the build process if you don't need it.
5. Build GCC:

This step takes a significant amount of time, depending on your system's resources.

Bash

make -j$(nproc)  # Use all available cores for faster compilation
6. Install GCC:

Bash

sudo make install
7. Add GCC to your PATH:

To use the newly installed GCC, you need to add its directory to your PATH environment variable.  Add the following lines to your ~/.bashrc file (or ~/.zshrc if you use Zsh):

Bash

export PATH=/usr/local/gcc-14/bin:$PATH
export LD_LIBRARY_PATH=/usr/local/gcc-14/lib:$LD_LIBRARY_PATH
Then, source the file to apply the changes:

Bash

source ~/.bashrc  # Or source ~/.zshrc for Zsh
8. Verify the Installation:

Bash

gcc --version
g++ --version
You should now see that GCC 14 is the active compiler.

Important Considerations:

Build time: Building GCC can take a long time (several hours).   
Disk space: The build process and installation will require a significant amount of disk space.   
Dependencies: Make sure you have all the necessary dependencies installed. The configuration step will usually tell you if anything is missing.
update-alternatives: If you want to switch between different GCC versions easily, you can use update-alternatives (as described in the previous response) after installing. This is a good idea, as it makes managing multiple GCC versions much cleaner.
This detailed guide should help you install GCC 14 successfully. Remember to carefully follow the instructions and adjust them as needed for your specific system. If you encounter errors, check the GCC documentation or online forums for solutions.


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
 

Switching Between GCC Versions:

The update-alternatives command is the standard way to manage multiple versions of commands like gcc and g++:

sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-13 13 --slave /usr/bin/g++ g++ /usr/bin/g++-13
 

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

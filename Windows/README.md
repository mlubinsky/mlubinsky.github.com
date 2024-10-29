 %* in batch file mean all command line arguments


## FOR LOOP
```
@echo off
echo START
FOR %%G IN (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)  ^
DO (
      echo %%G
)
```

### Run Windows program on another Windows box

1)	Use OpenSSH https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui
2)	Use PsExcec https://learn.microsoft.com/en-us/sysinternals/downloads/psexec
3)	Use PowerShell https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/running-remote-commands?view=powershell-7.4

### Extract substring
```
@echo off
set YYYYMM=202410
set DD=29

rem Extract year and month from YYYYMM
set YYYY=%YYYYMM:~0,4%
set MM=%YYYYMM:~4,2%

rem Combine with dash separators
set DATE_WITH_DASHES=%YYYY%-%MM%-%DD%

echo %DATE_WITH_DASHES%
```
 
### CMD
```
cmd.exe /?
Starts a new instance of the Windows command interpreter

CMD [/A | /U] [/Q] [/D] [/E:ON | /E:OFF] [/F:ON | /F:OFF] [/V:ON | /V:OFF]
    [[/S] [/C | /K] string]

/C      Carries out the command specified by string and then terminates
/K      Carries out the command specified by string but remains
/S      Modifies the treatment of string after /C or /K (see below)
/Q      Turns echo off
/D      Disable execution of AutoRun commands from registry (see below)
/A      Causes the output of internal commands to a pipe or file to be ANSI
/U      Causes the output of internal commands to a pipe or file to be
        Unicode
/T:fg   Sets the foreground/background colors (see COLOR /? for more info)
/E:ON   Enable command extensions (see below)
/E:OFF  Disable command extensions (see below)
/F:ON   Enable file and directory name completion characters (see below)
/F:OFF  Disable file and directory name completion characters (see below)
/V:ON   Enable delayed environment variable expansion using ! as the
        delimiter. For example, /V:ON would allow !var! to expand the
        variable var at execution time.  The var syntax expands variables
        at input time, which is quite a different thing when inside of a FOR
        loop.
/V:OFF  Disable delayed environment expansion.

Note that multiple commands separated by the command separator '&&'
are accepted for string if surrounded by quotes.  Also, for compatibility
reasons, /X is the same as /E:ON, /Y is the same as /E:OFF and /R is the
same as /C.  Any other switches are ignored.

```


### START
start "" /wait cmd.exe /c
start "" /wait cmd.exe /c runD_local.bat %*
```
start /?
Starts a separate window to run a specified program or command.

START ["title"] [/D path] [/I] [/MIN] [/MAX] [/SEPARATE | /SHARED]
      [/LOW | /NORMAL | /HIGH | /REALTIME | /ABOVENORMAL | /BELOWNORMAL]
      [/NODE <NUMA node>] [/AFFINITY <hex affinity mask>] [/WAIT] [/B]
      [command/program] [parameters]

    "title"     Title to display in window title bar.
    path        Starting directory.
    B           Start application without creating a new window. The
                application has ^C handling ignored. Unless the application
                enables ^C processing, ^Break is the only way to interrupt
                the application.
    I           The new environment will be the original environment passed
                to the cmd.exe and not the current environment.
    MIN         Start window minimized.
    MAX         Start window maximized.
    SEPARATE    Start 16-bit Windows program in separate memory space.
    SHARED      Start 16-bit Windows program in shared memory space.
    LOW         Start application in the IDLE priority class.
    NORMAL      Start application in the NORMAL priority class.
    HIGH        Start application in the HIGH priority class.
    REALTIME    Start application in the REALTIME priority class.
    ABOVENORMAL Start application in the ABOVENORMAL priority class.
    BELOWNORMAL Start application in the BELOWNORMAL priority class.
    NODE        Specifies the preferred Non-Uniform Memory Architecture (NUMA)
                node as a decimal integer.
    AFFINITY    Specifies the processor affinity mask as a hexadecimal number.
                The process is restricted to running on these processors.

                The affinity mask is interpreted differently when /AFFINITY and
                /NODE are combined.  Specify the affinity mask as if the NUMA
                node's processor mask is right shifted to begin at bit zero.
                The process is restricted to running on those processors in
                common between the specified affinity mask and the NUMA node.
                If no processors are in common, the process is restricted to
                running on the specified NUMA node.
    WAIT        Start application and wait for it to terminate.
    command/program
                If it is an internal cmd command or a batch file then
                the command processor is run with the /K switch to cmd.exe.
                This means that the window will remain after the command
                has been run.

                If it is not an internal cmd command or batch file then
                it is a program and will run as either a windowed application
                or a console application.
```



```
I have Windows batch file which calls several python scripts (1.py, 2,py, 3.py, 4.py, etc).
The batch file  checks the errorlevel - after calling every of these 3 python scripts.
In case when errorlevel != 0
after calling any of these python scripts the rest of the scripts
from the list above (1.py, 2,py, 3.py, 4.py, etc) should not be called;
in this case  batch_file  should call the python script update_status.py.

The final call in this Windows batch file  should be always the script named send_email.py
The send_email.py should be always called as the last call.

```
### Without checkrun
```
@echo off
REM Run scripts and check for errors

python 1.py
if %errorlevel% neq 0 goto error_handler

python 2.py
if %errorlevel% neq 0 goto error_handler

python 3.py
if %errorlevel% neq 0 goto error_handler

python 4.py
if %errorlevel% neq 0 goto error_handler

goto always_run

:error_handler
python update_status.py

:always_run
REM Always run send_email.py at the end
python send_email.py

:end
exit /b
```




GhatGPT:
```
@echo off
REM Run scripts and check for errors using a subroutine

python 1.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

python 2.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

python 3.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

python 4.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

goto always_run

:error_handler
python update_status.py

:always_run
REM Always run send_email.py at the end
python send_email.py

:end
exit /b

:checkrun
if %errorlevel% neq 0 exit /b 1
exit /b 0
```
Gemini:
```
Delayed Expansion: You're currently checking the %errorlevel% variable directly within the if statements.
This might not capture the actual error level after each script execution.
 To ensure accurate capture, consider using delayed expansion with exclamation marks (!errorlevel!).

Error Handling Consistency: Currently, the :checkrun subroutine exits with code 1 upon encountering an error. However, the if statements outside the subroutine check for neq 0. For consistency,
 you can either update the if statements to check for neq 1
or change the exit code in :checkrun to 0
and directly check for non-zero error levels in the if statements.

Here's the improved version with both options:

Option 1 (Delayed Expansion):

Code snippet
@echo off

:run_script
python %1
CALL :checkrun
if !errorlevel! neq 0 goto error_handler

GOTO :EOF

:checkrun
if %errorlevel% neq 0 exit /b 1
exit /b 0  

:error_handler
python update_status.py

:always_run
python send_email.py

:end
exit /b

:EOF
Use code with caution.

Option 2 (Consistent Error Code):

Code snippet
@echo off

python 1.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

python 2.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

python 3.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

python 4.py
CALL :checkrun
if %errorlevel% neq 0 goto error_handler

goto always_run

:error_handler
python update_status.py

:always_run
python send_email.py

:end
exit /b

:checkrun
if %errorlevel% neq 0 exit /b 0  **Exit with 0 on error**
exit /b  
Use code with caution.

Additional Improvements:

Consider renaming :end to a more descriptive label like :finish.
You can add comments within the script to explain specific sections.
Both options achieve the desired functionality of stopping after encountering an error and ensuring send_email.py is always called at the end. Choose the one that suits your preference and coding style.
```

### SET /P
```
The /P switch allows you to set the value of a variable to a line of input entered by the user.
Displays the specified promptString before reading the line of input. The promptString can be empty.

Usage case 1:

SET /P variable=
When batch file reaches this point (when left blank) it will halt and wait for user input.
Input then becomes variable.

Usage case 2:

SET /P variable=<%temp%\filename.txt
Will set variable to contents (the first line) of the txt file.
This method won't work unless the /P is included.
```

### Example of .bat file
with _not defined_ and _not exists_


```
@ECHO OFF

::: The below line assigns the Directory path your Program is in to the variable
::: for later use

Set Program_DIR=%~dp0

::: This creates the Directory for your User files

IF NOT EXIST "%Program_DIR%\Users" MD "%Program_DIR%\Users"

:login
cls
ECHO Welcome!
Set /p name=[Enter your Username to continue:]

IF not defined name GOTO login
IF Exist "%Program_DIR%\Users\%name%.bat" (
CALL "%Program_DIR%\Users\%name%.bat"
    ) else (
    GOTO New_User
)

:programMENU

::: Your program

:New_User

::: Save the users Name, and Assign the file to Variable to CALL when you wish to
::: store/Retrieve.

ECHO 0>"%Program_DIR%\Users\%name%.bat"
Set "LoadSave=%Program_DIR%\Users\%name%.bat"
```

### Power Toys
Color picker:

https://learn.microsoft.com/en-us/windows/powertoys/color-picker

activate Color Picker (Win+Shift+C) 

### Customize the background color of cmd.exe on Windows 10 programmatically
 
 

#### Using a Batch File
```
 The color command uses a two-digit hexadecimal code:
the first digit represents the background color,
and the second digit represents the text color.

Here's an example batch file to set the background to blue (1) and the text to white (F):

File: change_color.bat

@echo off
color 1F

Save this content to a file with a .bat extension, such as change_color.bat, and run it.
```
#### Using a Python Script

For a Python script, you can use the os module to call the color command. Here's how to do it:
``` 
import os

# Change the background color to blue (1) and text color to white (F)
os.system('color 1F')


This script executes the color command to change the cmd.exe background to blue and the text to white.

List of Color Codes
Here are some color codes you can use:

0 = Black
1 = Blue
2 = Green
3 = Aqua
4 = Red
5 = Purple
6 = Yellow
7 = White
8 = Gray
9 = Light Blue
A = Light Green
B = Light Aqua
C = Light Red
D = Light Purple
E = Light Yellow
F = Bright White
```

#### Example
```
If you want to set the background to red (4) and text to yellow (E), the code would be:

Batch File:

batch
Copy code
@echo off
color 4E
Python Script:

python
Copy code
import os

# Change the background color to red (4) and text color to yellow (E)


os.system('color 4E')
These methods will change the background color of the current cmd.exe session.
If you want to make permanent changes, you'll need to modify the registry,
which is more complex and not typically recommended for casual users.

```

### How to change the color of text programmatically?
``` 
To change the color of text programmatically in the Windows command prompt (cmd.exe),
you can use escape sequences with the color command within a batch file or from a Python script.
 The color command in cmd.exe changes both the background and text color,
but you can adjust it dynamically within a script to change only the text color when needed.

```

#### Change the color of text iusing a Batch File
```
You can change the color of text in a batch file using the color command followed by printing the text:
 
@echo off
:: Change background to black (0) and text to green (A)
color 0A
echo This text is green

:: Change background to black (0) and text to red (C)
color 0C
echo This text is red

:: Change background to black (0) and text to white (F)
color 0F
echo This text is white


Save the above content to a file with a .bat extension (e.g., change_text_color.bat) and run it.
```
#### Using a Python Script

In a Python script, you can use the os.system function to execute the color command and then print the text:

``` 
import os

# Change background to black (0) and text to green (A)
os.system('color 0A')
print("This text is green")

# Change background to black (0) and text to red (C)
os.system('color 0C')
print("This text is red")

# Change background to black (0) and text to white (F)
os.system('color 0F')
print("This text is white")

```
#### Example of Dynamic Text Color Change
```
If you need to dynamically change the text color within the same script, 
you can do it as shown in the examples above. 
However, if you need more control over text coloring 
(e.g., multiple colors in the same line or more complex text formatting), y
ou would need to use libraries such as colorama in Python, which allows more advanced text styling:

Using Colorama in Python
First, install the colorama library:

bash
Copy code
pip install colorama
Then, use the following script:
 
from colorama import init, Fore, Back, Style
# Initialize colorama
init()

print(Fore.GREEN + 'This text is green')
print(Fore.RED + 'This text is red')
print(Fore.WHITE + 'This text is white')

# Reset to default color
print(Style.RESET_ALL + 'This text is default color')


Explanation:

Batch File: The color command sets both background and text colors. T
he script changes the color and then prints the text.
Python Script (os.system):
Uses the os.system function to call the color command, changing the color and printing the text.
Python Script (colorama): The colorama library provides more advanced control over text colors and styles, allowing multiple colors in the same script.
These methods allow you to change text colors programmatically in cmd.exe on Windows.

```

### Terminal

https://github.com/microsoft/terminal

https://sysprogs.com/SmarTTY/  SSH client

### .bat file to invoke ruff
```
ruff check %* --ignore E501
```
### find

number of lines in file:

find /v /c “” C:\Users\Martin\Desktop\sample.txt

### if statement in bat file
```
@echo off
setlocal enabledelayedexpansion

:: Set the variable A with quotes
set A="G2"

:: Remove the leading and trailing double quotes from A
set A=%A:"=%

:: Check if the value of A is "G2"
if "%A%"=="G2" (
    echo Variable A is G2
    :: Place your code here that you want to execute when A is G2
) else (
    echo Variable A is not G2
)
```
Gemini solution:
```
Code snippet
@echo off

setlocal enabledelayedexpansion

if "!A!"=="G2" (
  echo A is equal to G2! Executing code...
  REM Your code here
  echo This line will only be executed if A is G2
) else (
  echo A is not equal to G2. Skipping code execution.
)

endlocal
pause
``` 

Gemini Explanation:
```
@echo off:
This line hides the commands from being echoed on the screen.

setlocal enabledelayedexpansion:
This line enables delayed variable expansion within a block scope.

This allows us to use the exclamation mark (!) for variable expansion even within quotes.
if "!A!"=="G2" ( ... ) else ( ... ):

This if-else statement remains the same, but we use !A! for variable expansion.
!: This exclamation mark allows delayed variable expansion within double quotes.

This ensures the actual value of A is compared, including any surrounding quotes.
```

### Removing quotes in bat file
CharGPT solution:
```
@echo off
setlocal enabledelayedexpansion

:: Set variables
set A=partA
set B="xyz"

:: Remove the leading and trailing double quotes from B
set B=%B:"=%

:: Concatenate A, -, and the modified B
set C=%A%-%B%

:: Display the result
echo %C%

endlocal
pause
```
Gemini solution:
```
Code snippet
@echo off

set "C=%A% - %B:~1,-1%"

echo The new variable C is: %C%

pause
```

Gemini Explanation:
```
@echo off: This line hides the commands from being echoed on the screen when the script runs.
set "C=%A% - %B:~1,-1%":
set: This command is used to define a new environment variable.
"C=: We set the name of the new variable to "C".
%A%: This expands the value of the existing variable "A" and adds it to the string.
-: This adds a literal hyphen (-) to the string.
%B:~1,-1%: This is a substring expansion of the "B" variable.
~: Tilde (~) is used for substring expansion.

1: This specifies the starting position of the substring (excluding the first character).
-1: This specifies the ending position of the substring (excluding the last character).
This removes the leading and trailing double quotes.
echo The new variable C is: %C%:
This line displays a message with the value of the newly created variable "C".
pause:
This line pauses the execution of the script and waits for any key to be pressed before closing the command prompt window.
```

###  Gemini my.bat

``` 
@echo off

rem Create RUNNING.txt with current timestamp
echo.%date% %time% > RUNNING.txt

rem Execute your Python scripts here
python script1.py
if %errorlevel% neq 0 goto :fail

python script2.py
if %errorlevel% neq 0 goto :fail

... (add more python scripts)

:success
rem Add current timestamp and rename to SUCCESS.txt
echo.%date% %time% >> RUNNING.txt
ren RUNNING.txt SUCCESS.txt
goto :eof

:fail
rem Rename to FAILED.txt
ren RUNNING.txt FAILED.txt
echo An error occurred during execution. Check FAILED.txt for details.
goto :eof
```

### ChatGPT my.bat
```
@echo off
setlocal enabledelayedexpansion

:: Create RUNNING.txt with the current timestamp
echo %date% %time% > RUNNING.txt

:: Call your Python scripts
call python script1.py
if errorlevel 1 goto failed

call python script2.py
if errorlevel 1 goto failed

call python script3.py
if errorlevel 1 goto failed

:: If all scripts succeed, add timestamp and rename to SUCCESS.txt
echo %date% %time% >> RUNNING.txt
rename RUNNING.txt SUCCESS.txt
goto end

:failed
:: If any script fails, rename RUNNING.txt to FAILED.txt
rename RUNNING.txt FAILED.txt

:end
```



### How to invoke program located on another Windows box on same network?


https://www.reddit.com/r/PowerShell/comments/q9e887/tldr_of_how_to_run_commands_on_a_remote_windows/

#### OpenSSH

https://learn.microsoft.com/ru-ru/windows/terminal/tutorials/ssh

https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui

https://medium.com/geekculture/setup-ssh-server-on-windows-10-11-34c7f096eaff

https://sysprogs.com/SmarTTY/

#### PowerShell
https://learn.microsoft.com/en-us/powershell/scripting/security/remoting/running-remote-commands?view=powershell-7.4

https://serverfault.com/questions/690852/use-powershell-to-start-a-gui-program-on-a-remote-machine

#### PSexec

https://www.youtube.com/watch?v=uis36XxFUfg

https://4sysops.com/archives/three-ways-to-run-remote-windows-commands/

https://learn.microsoft.com/en-us/sysinternals/downloads/psexec

psexec \\RemoteComputer cmd.exe

psexec \\computer_name -u username -p password ipconfig

#### The WMIC obsoleted !!!  is part of wbem win folder: C:\Windows\System32\wbem

winrs -r:PCNAME cmd

WMIC /node:ComputerName process call create “cmd.exe /c start.exe”


### .BAT file to traverse folder

```
@ECHO OFF
 
for %%f in (directory\path\*.txt) do (
  set /p val=<%%f
  echo "fullname: %%f"
  echo "name: %%~nf"
  echo "contents: !val!"
)
```
### Compare 2 folders PoweShell:
```
$folderA = "C:\A"
$folderB = "C:\B"

# Get the list of files from both folders
$filesA = Get-ChildItem -Path $folderA -File -Recurse
$filesB = Get-ChildItem -Path $folderB -File -Recurse

# Compare the files based on content
$differentFiles = @()

foreach ($fileA in $filesA) {
    $fileB = $filesB | Where-Object { $_.Name -eq $fileA.Name }

    if ($fileB -eq $null) {
        $differentFiles += $fileA.FullName
    } else {
        $hashA = Get-FileHash -Path $fileA.FullName -Algorithm MD5
        $hashB = Get-FileHash -Path $fileB.FullName -Algorithm MD5

        if ($hashA.Hash -ne $hashB.Hash) {
            $differentFiles += $fileA.FullName
        }
    }
}

# Display the list of different files
Write-Host "Different files:"
$differentFiles | ForEach-Object { Write-Host $_ }

# You can also save the list to a text file if you want
#$differentFiles | Out-File -FilePath "DifferentFilesList.txt"

```
### Compare folders using Python
```
import filecmp
import os

folder_a = r'C:\A'
folder_b = r'C:\B'

differing_files = []

for dirpath, dirnames, filenames in os.walk(folder_a):
    for filename in filenames:
        file_path_a = os.path.join(dirpath, filename)
        file_path_b = os.path.join(folder_b, os.path.relpath(file_path_a, folder_a))
        
        if os.path.exists(file_path_b):
            if not filecmp.cmp(file_path_a, file_path_b, shallow=False):
                differing_files.append(file_path_a)
        else:
            differing_files.append(file_path_a)

print("Different files:")
for file_path in differing_files:
    print(file_path)
```
### Compare folders using .bat 
```
@echo off
setlocal

set "folderA=C:\A"
set "folderB=C:\B"

setlocal enabledelayedexpansion
for /r "%folderA%" %%a in (*) do (
    set "relativePath=%%~pa"
    set "fileB=!folderB!\!relativePath:~1!\%%~nxa"
    if exist "!fileB!" (
        fc "%%a" "!fileB!" > nul
        if errorlevel 1 (
            echo Different: "%%a"
        )
    ) else (
        echo Missing in folder B: "%%a"
    )
)

endlocal
```




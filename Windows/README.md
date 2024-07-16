### Power Toys
Color picker:

https://learn.microsoft.com/en-us/windows/powertoys/color-picker

activate Color Picker (Win+Shift+C) 

### Terminal

https://github.com/microsoft/terminal

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
@echo off: This line hides the commands from being echoed on the screen.
setlocal enabledelayedexpansion: This line enables delayed variable expansion within a block scope.
This allows us to use the exclamation mark (!) for variable expansion even within quotes.
if "!A!"=="G2" ( ... ) else ( ... ): This if-else statement remains the same, but we use !A! for variable expansion.
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

@echo off: This line hides the commands from being echoed on the screen when the script runs.
set "C=%A% - %B:~1,-1%":
set: This command is used to define a new environment variable.
"C=: We set the name of the new variable to "C".
%A%: This expands the value of the existing variable "A" and adds it to the string.
-: This adds a literal hyphen (-) to the string.
%B:~1,-1%: This is a substring expansion of the "B" variable.
~: Tilde (~) is used for substring expansion.
1: This specifies the starting position of the substring (excluding the first character).
-1: This specifies the ending position of the substring (excluding the last character). This removes the leading and trailing double quotes.
echo The new variable C is: %C%: This line displays a message with the value of the newly created variable "C".
pause: This line pauses the execution of the script and waits for any key to be pressed before closing the command prompt window.
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

https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui

https://medium.com/geekculture/setup-ssh-server-on-windows-10-11-34c7f096eaff

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




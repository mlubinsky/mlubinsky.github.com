### Terminal

https://github.com/microsoft/terminal

### .bat file to invoke ruff
```
ruff check %* --ignore E501
```
### find

number of lines in file:

find /v /c “” C:\Users\Martin\Desktop\sample.txt


###  my.bat

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




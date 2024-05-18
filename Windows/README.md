### Terminal

https://github.com/microsoft/terminal

### .bat file to invoke ruff
```
ruff check %* --ignore E501
```
### find

number of lines in file:

find /v /c “” C:\Users\Martin\Desktop\sample.txt


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




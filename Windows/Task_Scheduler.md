### Multi-volume archive 7-zip
https://www.7-zip.org/
```
To check the integrity of a multi-volume compressed archive without uncompressing it, you can use 7-Zip. Here's how you can verify the archive on Windows:

Using the 7-Zip GUI:
Open 7-Zip File Manager:

Launch 7-Zip from the Start menu or by searching for it.
Locate Your Archive:

Navigate to the folder containing the multi-volume archive (e.g., a-001.zip, a-002.zip, etc.).
Verify the Archive:

Select the first file in the multi-volume archive (a-001.zip).
Click File > Test Archive or simply press Alt + T.
Check Results:

7-Zip will check the integrity of all volumes without extracting them. If everything is intact, it will show a message like "Everything is OK".
Using the Command Line (7z):
You can also use the command line for verification, which is especially useful if you want to automate the process.

Open Command Prompt:

Press Windows + R, type cmd, and press Enter.
Run the Test Command:

Navigate to the folder containing the archive:
 
 
cd C:\path\to\your\archive
Run the following command using 7z:
 
 
"C:\Program Files\7-Zip\7z.exe" t a-001.zip
This will test the integrity of the entire multi-volume archive.
Result:
If the archive is intact, the output will show "Everything is OK". If there are any issues with the files or their integrity, 7-Zip will display an error message.
```

### Get list of folders created by 7z
```
import subprocess
import os

def unpack_7z_archive(archive_path, destination_folder):
    # Step 1: Run the 7z command to unpack the archive
    result = subprocess.run(['7z', 'x', archive_path, f'-o{destination_folder}'], 
                            capture_output=True, text=True)

    if result.returncode != 0:
        raise Exception(f"7z extraction failed: {result.stderr}")
    
    # Step 2: List folders created after unpacking
    created_folders = [f for f in os.listdir(destination_folder) if os.path.isdir(os.path.join(destination_folder, f))]

    return created_folders

# Example usage
archive = 'example.7z'  # Replace with your archive path
destination = 'output_folder'  # Replace with your destination folder path
created_folders = unpack_7z_archive(archive, destination)

print("Created folders:", created_folders)

```




#### Check archive integrity from python
```
import subprocess

# Path to the first file of the multi-volume archive
archive_path = r'C:\path\to\your\archive\a-001.zip'

# Path to the 7z executable (adjust if 7-Zip is not in your PATH)
seven_zip_path = r'C:\Program Files\7-Zip\7z.exe'

def check_archive_integrity(archive_path):
    try:
        # Run the 7z test command to check archive integrity
        result = subprocess.run([seven_zip_path, 't', archive_path],
                                capture_output=True, text=True)
        
        # Output the result of the test
        if result.returncode == 0 and "Everything is OK" in result.stdout:
            print("Archive integrity check passed: Everything is OK")
        else:
            print("Archive integrity check failed.")
            print(result.stdout)
            print(result.stderr)
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to check the archive
check_archive_integrity(archive_path)

```

#### Move archived files and uncompress them
```
import os
import shutil
import subprocess
from datetime import datetime

# Path to 7z executable (adjust if not in your PATH)
seven_zip_path = r'C:\Program Files\7-Zip\7z.exe'

def get_creation_date(filepath):
    """ Get the creation date of the file """
    stat = os.stat(filepath)
    return datetime.fromtimestamp(stat.st_ctime)  # Creation time

def check_archive_integrity(archive_path):
    """ Check if the archive is valid using 7z test command """
    try:
        result = subprocess.run([seven_zip_path, 't', archive_path], capture_output=True, text=True)
        if result.returncode == 0 and "Everything is OK" in result.stdout:
            return True
        else:
            return False, result.stdout + result.stderr
    except Exception as e:
        return False, str(e)

def uncompress_archive(archive_path, destination_folder):
    """ Uncompress the archive to the destination folder using 7z """
    try:
        subprocess.run([seven_zip_path, 'x', archive_path, f'-o{destination_folder}', '-y'], check=True)
        print(f"Successfully uncompressed: {archive_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error while uncompressing {archive_path}: {e}")

def process_archives(input_folder, output_folder):
    """ Process all archives in the input folder and organize by creation date """
    # List all files in the input folder
    for file_name in os.listdir(input_folder):
        file_path = os.path.join(input_folder, file_name)
        
        # Check if the file is an archive (modify this based on your archive types)
        if file_name.endswith(('.zip', '.rar', '.7z')):
            try:
                # 1. Detect the creation date of the archive
                creation_date = get_creation_date(file_path)
                date_str = creation_date.strftime('%Y-%m-%d')
                
                # 2. Create the subfolder under the output folder
                destination_folder = os.path.join(output_folder, date_str)
                os.makedirs(destination_folder, exist_ok=True)
                
                # 3. Move the archive to the destination folder
                new_file_path = shutil.move(file_path, destination_folder)
                print(f"Moved {file_name} to {destination_folder}")
                
                # 4. Check the integrity of the archive
                is_valid = check_archive_integrity(new_file_path)
                if isinstance(is_valid, tuple) and not is_valid[0]:
                    print(f"Archive {file_name} is corrupted: {is_valid[1]}")
                else:
                    # Uncompress the archive
                    uncompress_archive(new_file_path, destination_folder)
                    
            except Exception as e:
                print(f"Error processing {file_name}: {e}")

# Example usage
input_folder = r'C:\path\to\input\folder'
output_folder = r'C:\path\to\output\folder'
process_archives(input_folder, output_folder)

```



### Start program automatically when computer restart
```
To automatically start a Python script (a.py) when your Windows computer reboots,
 you can use Task Scheduler.
```
#### 1. Open Task Scheduler:

Press Windows + R, type taskschd.msc, and hit Enter.

#### 2. Create a New Task:

In Task Scheduler, click on Action > Create Task.

#### 3. General Settings:
```
In the General tab, give your task a name (e.g., "Run Python Script").
Select Run whether user is logged on or not.
Check Run with highest privileges if needed.
```

#### 4. Trigger:
```
Go to the Triggers tab and click New.
Set the trigger to At startup.
Click OK.
```
#### 5. Action:
```
Go to the Actions tab and click New.
In the Action dropdown, select Start a program.
In the Program/script field, enter the path to the Python interpreter (e.g., C:\Python39\python.exe).
In the Add arguments field, enter the path to your a.py script (e.g., C:\path\to\a.py).
Click OK.
```
#### 6. Save the Task:
```
Click OK in the main task window.
Enter your password if prompted.
Now, your Python script will automatically start each time your computer reboots.
```


### Steps to Set Up an Hourly Task in Task Scheduler:  taskschd.msc
```
Steps to Set Up an Hourly Task in Task Scheduler:
Open Task Scheduler:

Press Windows + R, type taskschd.msc, and press Enter.
This will open the Task Scheduler.
Create a New Task:
```
### Generat Tab -> Create Task
```
In the Task Scheduler window, click on Action in the top menu and select Create Task.
Configure the General Tab:

In the General tab, give your task a name (e.g., "HourlyTask").
Choose Run whether user is logged on or not if you want the task to run even when you're not logged in.
Check Run with highest privileges if the task requires administrator rights.
Set the Trigger (Hourly Schedule):
```
### Trigger Tab
```
Go to the Triggers tab, and click on New to create a new trigger.
Under Begin the task, select On a schedule.
Set the schedule to Daily.
In the Advanced settings, check Repeat task every and set it to 1 hour.
Set the For a duration of option to Indefinitely (or set it to a specific time range).
Click OK.
Set the Action (What to Run):
```
### Actions Tab
```
Go to the Actions tab and click New.
In the Action dropdown, choose Start a program.
Click Browse and locate the program, script, or batch file you want to run every hour.
Add any necessary arguments in the Add arguments (optional) field.
Click OK.
```
### Contitions Tab
```
Optional Settings (Conditions and Settings):

In the Conditions tab, you can set conditions like running the task only
if the computer is idle or if it’s on AC power (optional).
```
### Settings tab
```
In the Settings tab, you can configure additional settings such as stopping the task
 if it runs too long or restarting it if it fails.
```
### Save the Task
Click OK to save the task.
If prompted, enter your user credentials.

### Testing the Task:
To test your task immediately, you can right-click the task in the Task Scheduler Library and select Run.


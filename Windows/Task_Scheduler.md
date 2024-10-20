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


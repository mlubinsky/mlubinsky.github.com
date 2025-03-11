
You can automate the reloading of your updated code without manually restarting the main program. Here are a few approaches to achieve this:

1. Use importlib.reload() to Reload Modules Dynamically
Instead of restarting the program, you can reload your updated modules dynamically inside the infinite loop.

Example:
 
import time
import importlib
import my_module  # This is the module that gets updated

while True:
    importlib.reload(my_module)  # Reload the module dynamically
    if my_module.check_for_input_file():  # Call the function from the updated module
        my_module.process_file()
    time.sleep(60)  # Sleep for 1 minute
Whenever my_module.py is modified, it will be reloaded dynamically before the next execution.

2. Use a File Watcher to Detect Code Changes
You can monitor changes in the source files and restart the script automatically when an update is detected.

Using watchdog:
 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import os
import sys
import time

class CodeChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"Detected code update in {event.src_path}, restarting...")
            os.execv(sys.executable, ['python'] + sys.argv)  # Restart the script

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    event_handler = CodeChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            # Your main logic here
            time.sleep(60)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
This will restart the program whenever a .py file in the current directory is modified.

3. Use supervisor or systemd for Automatic Restarts
If you're running this as a system service or script, you can use process managers like supervisor or systemd to monitor and restart the program when code changes.

Example: supervisor.conf
 
command=python /path/to/your_script.py
autorestart=true
directory=/path/to/
Run supervisorctl restart my_script whenever you update your code.

Best Approach?
If you need immediate updates without restarting, use importlib.reload().
If you can afford a restart when the code updates, watchdog + os.execv() is a solid approach.
If your script is managed as a service, supervisor or systemd is the best option.


### subprocess.run() what check=True means?
```
In Python's subprocess.run(), the parameter check=True is used to ensure that the program being called exits successfully.
 Here's what it does:

Without check=True: The subprocess.run() function will execute the command,
 and regardless of whether the command succeeds or fails (i.e., returns a non-zero exit code),
no exception will be raised.
You would need to manually check the return code (result.returncode) to detect failure.

With check=True: If the command returns a non-zero exit code (which indicates failure),
 Python will raise a subprocess.CalledProcessError exception.
 This allows you to handle failures more explicitly, for example, by adding try-except blocks.

Example:

import subprocess

# Without check=True
result = subprocess.run(['ls', 'non_existent_directory'], capture_output=True, text=True)
print("Without check=True:", result.returncode)  # Returns a non-zero code if 'ls' fails

# With check=True
try:
    subprocess.run(['ls', 'non_existent_directory'], check=True, capture_output=True, text=True)
except subprocess.CalledProcessError as e:
    print(f"With check=True: Command failed with error: {e}")

Key Points:
check=False (default): The command can fail without raising an exception.
 You need to check the returncode manually.

check=True: If the command fails, it raises a CalledProcessError, which you can catch to handle the failure.
 This is useful when you want to enforce that the command must succeed for the program to continue.
```



### Watchdog with multi volume support without classes
```
import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Timer

# Global dictionary to store pending multi-volume archives
pending_archives = {}

def on_created(event, folder_to_monitor, process_file_callback):
    if event.is_directory:
        return
    
    filepath = event.src_path
    if filepath.endswith(".zip"):
        # Extract the base filename and volume number
        basename = os.path.basename(filepath)
        base, ext = os.path.splitext(basename)
        # Detect multi-volume archives based on the suffix pattern (xx-001.zip, etc.)
        if '-' in base and base.split('-')[-1].isdigit():
            volume_id = int(base.split('-')[-1])
            archive_base = '-'.join(base.split('-')[:-1])
            handle_multivolume(archive_base, volume_id, filepath)
        else:
            # Single-volume archive, process immediately
            process_file_callback(filepath)

def handle_multivolume(archive_base, volume_id, filepath):
    global pending_archives
    
    # Add volume part to the pending archive set
    if archive_base not in pending_archives:
        pending_archives[archive_base] = {
            "files": {},
            "timer": Timer(1800, process_multivolume, [archive_base])
        }
        pending_archives[archive_base]["timer"].start()

    pending_archives[archive_base]["files"][volume_id] = filepath
    
    # Check if all parts are present (for this example, assume up to xx-003.zip)
    if len(pending_archives[archive_base]["files"]) == 3:  # Adjust as necessary for your use case
        pending_archives[archive_base]["timer"].cancel()
        process_multivolume(archive_base)

def process_multivolume(archive_base):
    global pending_archives
    
    # Get all volume parts and sort them
    volumes = sorted(pending_archives[archive_base]["files"].items())
    volume_paths = [v[1] for v in volumes]

    # Unzip all parts together using 7z
    unzip_files(volume_paths)

    # After unzipping, call external program to process unzipped files
    process_unzipped_files(volume_paths)

    # Clean up
    del pending_archives[archive_base]

def unzip_files(file_paths):
    try:
        # Unzip using subprocess and 7z
        subprocess.run(["7z", "x"] + file_paths, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error unzipping files: {e}")

def process_unzipped_files(file_paths):
    # Call external program to process unzipped files
    print(f"Processing unzipped files from: {file_paths}")
    # Replace with your external program call
    # subprocess.run([...])

def monitor_folder(folder_to_monitor):
    def process_file_callback(filepath):
        print(f"Processing single-volume file: {filepath}")
        # Unzip single-volume archive
        unzip_files([filepath])
        # Call external program to process unzipped files
        process_unzipped_files([filepath])

    def on_created_event(event):
        on_created(event, folder_to_monitor, process_file_callback)
    
    # Create watchdog observer
    event_handler = FileSystemEventHandler()
    event_handler.on_created = on_created_event
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=False)
    observer.start()
    print(f"Monitoring folder: {folder_to_monitor}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_monitor = "/path/to/monitored/folder"
    monitor_folder(folder_to_monitor)


```
### Watchdog with muli-volume archive support with class
```
import os
import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from threading import Timer

class ArchiveHandler(FileSystemEventHandler):
    def __init__(self, folder_to_monitor, process_file_callback):
        self.folder_to_monitor = folder_to_monitor
        self.process_file_callback = process_file_callback
        self.pending_archives = {}

    def on_created(self, event):
        if event.is_directory:
            return
        
        filepath = event.src_path
        if filepath.endswith(".zip"):
            # Extract the base filename and volume number
            basename = os.path.basename(filepath)
            base, ext = os.path.splitext(basename)
            # Detect multi-volume archives based on the suffix pattern (xx-001.zip, etc.)
            if '-' in base and base.split('-')[-1].isdigit():
                volume_id = int(base.split('-')[-1])
                archive_base = '-'.join(base.split('-')[:-1])
                self.handle_multivolume(archive_base, volume_id, filepath)
            else:
                # Single-volume archive, process immediately
                self.process_file_callback(filepath)

    def handle_multivolume(self, archive_base, volume_id, filepath):
        # Add volume part to the pending archive set
        if archive_base not in self.pending_archives:
            self.pending_archives[archive_base] = {
                "files": {},
                "timer": Timer(1800, self.process_multivolume, [archive_base])
            }
            self.pending_archives[archive_base]["timer"].start()

        self.pending_archives[archive_base]["files"][volume_id] = filepath
        
        # Check if all parts are present (for this example, assume up to xx-003.zip for simplicity)
        if len(self.pending_archives[archive_base]["files"]) == 3:  # Adjust as necessary for your use case
            self.pending_archives[archive_base]["timer"].cancel()
            self.process_multivolume(archive_base)

    def process_multivolume(self, archive_base):
        # Get all volume parts and sort them
        volumes = sorted(self.pending_archives[archive_base]["files"].items())
        volume_paths = [v[1] for v in volumes]

        # Unzip all parts together using 7z
        self.unzip_files(volume_paths)

        # After unzipping, call external program to process unzipped files
        # (implement this function to call your external program)
        self.process_unzipped_files(volume_paths)

        # Clean up
        del self.pending_archives[archive_base]

    def unzip_files(self, file_paths):
        try:
            # Unzip using subprocess and 7z
            subprocess.run(["7z", "x"] + file_paths, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error unzipping files: {e}")

    def process_unzipped_files(self, file_paths):
        # Call external program to process unzipped files
        print(f"Processing unzipped files from: {file_paths}")
        # Replace with your external program call
        # subprocess.run([...])

def monitor_folder(folder_to_monitor):
    event_handler = ArchiveHandler(folder_to_monitor, lambda f: print(f"Processing single-volume file: {f}"))
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=False)
    observer.start()
    print(f"Monitoring folder: {folder_to_monitor}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    folder_to_monitor = "/path/to/monitored/folder"
    monitor_folder(folder_to_monitor)


```


### ChatGPT  watchdog
pip install watchdog py7zr
```
Unfortunately, py7zr doesn't natively support extracting multi-volume 7z archives described (a-001.zip, a-002.zip, etc.).
This is because py7zr expects a single, valid 7z archive file.

Here are two approaches you can consider:

1. Using External Tools (Recommended):

This is the more robust and recommended approach. You can use a command-line tool like 7z (part of the p7zip package) or other tools like peazip to extract the multi-volume archive:

Bash
7z x a-001.zip a-002.zip  # Replace with your actual filenames
 
import time
import os
import py7zr
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ArchiveHandler(FileSystemEventHandler):
    def __init__(self, folder_to_watch):
        self.folder_to_watch = folder_to_watch
        self.processed_archives = set()  # Keep track of processed archives

    def on_created(self, event):
        if event.is_directory:
            return
        
        # Check if a new file is an archive part
        if event.src_path.endswith(".zip"):
            base_name = event.src_path[:-8]  # Strip "-XXX.zip" part
            self.handle_new_archive(base_name)

    def handle_new_archive(self, base_name):
        if base_name in self.processed_archives:
            return

        try:
            # Check if all parts of the multi-volume archive are present
            if self.check_all_parts_exist(base_name):
                print(f"Processing archive: {base_name}")
                self.extract_archive(base_name)
                self.processed_archives.add(base_name)
            else:
                print(f"Waiting for more parts of {base_name}...")
        except Exception as e:
            print(f"Error processing {base_name}: {e}")

    def check_all_parts_exist(self, base_name):
        part = 1
        while True:
            part_file = f"{base_name}-{part:03d}.zip"
            if os.path.exists(part_file):
                part += 1
            else:
                # If we reached the first missing part after at least one found, stop
                return part > 1

    def extract_archive(self, base_name):
        try:
            with py7zr.SevenZipFile(f"{base_name}-001.zip", mode='r') as archive:
                archive.extractall(path=self.folder_to_watch)
            print(f"Successfully extracted {base_name}")
        except Exception as e:
            print(f"Failed to extract {base_name}: {e}")


if __name__ == "__main__":
    folder_to_monitor = "C:/path/to/folder"  # Set the folder you want to monitor
    event_handler = ArchiveHandler(folder_to_monitor)
    observer = Observer()
    observer.schedule(event_handler, folder_to_monitor, recursive=False)

    print(f"Monitoring folder: {folder_to_monitor}")
    observer.start()

    try:
        while True:
            time.sleep(1)  # Keep the program running
    except KeyboardInterrupt:
        observer.stop()
    finally:
        observer.join()

```

### Gemini watchdog
```
import os
import zipfile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


def handle_new_file(event):
  """Handles new file events in the shared folder."""
  if not event.is_file:
    return

  # Check if filename follows multi-volume archive format (a-001.zip)
  filename = os.path.basename(event.src_path)
  if not filename.startswith("a-") or not filename.endswith(".zip"):
    return

  # Extract volume number from filename
  volume_number = int(filename.split("-")[1][:3])

  # Check if other volumes exist (search for next volume)
  next_volume = f"a-{volume_number+1:03}.zip"
  if not os.path.exists(os.path.join(event.src_path, next_volume)):
    print(f"Skipping incomplete archive: {filename}")
    return

  # Combine all volumes into a single archive
  combined_archive = f"combined.zip"
  try:
    with zipfile.ZipFile(combined_archive, 'w') as combined_zip:
      for i in range(1, volume_number + 1):
        volume_file = f"a-{i:03}.zip"
        with zipfile.ZipFile(os.path.join(event.src_path, volume_file), 'r') as volume_zip:
          for info in volume_zip.infolist():
            combined_zip.writestr(info, volume_zip.read(info))
    print(f"Successfully combined archives: {filename} (and following volumes)")
  except zipfile.BadZipFile:
    print(f"Error: Invalid archive found: {filename}")
  except Exception as e:
    print(f"Error uncompressing archives: {e}")
  finally:
    # Cleanup temporary combined archive
    if os.path.exists(combined_archive):
      os.remove(combined_archive)
    # Remove processed volumes (optional)
    # for i in range(1, volume_number + 1):
    #   volume_file = f"a-{i:03}.zip"
    #   os.remove(os.path.join(event.src_path, volume_file))


def monitor_folder(folder_path):
  """Monitors the specified folder for new files."""
  event_handler = FileSystemEventHandler()
  event_handler.on_created = handle_new_file
  observer = Observer()
  observer.schedule(event_handler, folder_path, recursive=False)
  observer.start()
  try:
    print(f"Monitoring folder: {folder_path}")
    while observer.is_alive():
           observer.join(1)
  except KeyboardInterrupt:
    observer.stop()

  observer.join()


# Replace with the actual path of your shared folder
shared_folder_path = r"\\server\shared\folder"
monitor_folder(shared_folder_path)
```

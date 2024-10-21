
### subprocess.run()  check=True
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


### ChatGPT
pip install watchdog py7zr

```
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
    observer.join()

```

### Gemini
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

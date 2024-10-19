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

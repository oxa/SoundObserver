import time
import re
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from playsound import playsound

class LogFileHandler(FileSystemEventHandler):
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, "r", encoding="utf-8")
        self.file.seek(0, 2)  # Go to the end of the file

    def on_modified(self, event):
        if event.src_path == self.file_path:
            self.parse_new_lines()

    def parse_new_lines(self):
        lines = self.file.readlines()
        for line in lines:
            # Example: Parse for a spell cast event
            if re.search("SPELL_CAST_SUCCESS", line):
                spell_name = re.search("SpellName\[(.*?)\]", line).group(1)
                print(f"Spell Cast: {spell_name}")
                # Update UI here based on the event

def start_monitoring(log_file_path):
    event_handler = LogFileHandler(log_file_path)
    observer = Observer()
    observer.schedule(event_handler, path=log_file_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

# Example usage
log_file_path = "/path/to/your/SWTOR/log/file.log"
start_monitoring(log_file_path)

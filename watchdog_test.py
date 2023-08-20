from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

templates_dir = Path("templates")


class TemplateChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        file_path = Path(event.src_path)
        file_name = file_path.relative_to(templates_dir)
        print(f"File modified: {file_name}")


def start_observer():
    event_handler = TemplateChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, str(templates_dir), recursive=True)
    observer.start()
    try:
        while True:
            pass  # Keep the observer running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    start_observer()

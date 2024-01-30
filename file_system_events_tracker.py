import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "test"


class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"Hey, {event.src_path} was created")

    def on_deleted(self, event):
        print(f"Oops, {event.src_path} was deleted")

    def on_modified(self, event):
        print(f"Hey, {event.src_path} was modified")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} was moved")


def main():
    observer = Observer()
    observer.schedule(FileEventHandler(), from_dir)
    observer.start()

    try:
        while True:
            time.sleep(2)
            print("running...")
    except KeyboardInterrupt:
        print("stopping...")
        observer.stop()


if __name__ == '__main__':
    main()

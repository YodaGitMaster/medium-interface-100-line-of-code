import os
from datetime import datetime

class ChatMemory:
    def __init__(self):
        self.log_folder = 'chats'

    def write_to_file(self, message):
        current_datetime = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.log_filename = f'{current_datetime}.log'
        self.log_filepath = os.path.join(self.log_folder, self.log_filename)

        if not os.path.exists(self.log_folder):
            os.makedirs(self.log_folder)

        with open(self.log_filepath, 'a') as file:
            file.write(f"{message}\n")

    def list_log_files(self):
        if not os.path.exists(self.log_folder):
            return []

        log_files = [file for file in os.listdir(self.log_folder) if file.endswith('.log')]
        return log_files

    def read_log_file(self, log_file):
        log_filepath = os.path.join(self.log_folder, log_file)

        if not os.path.exists(log_filepath):
            return f"Log file '{log_file}' not found."

        with open(log_filepath, 'r') as file:
            content = file.read()
            return content
        
        

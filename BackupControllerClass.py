import shutil
import os
from datetime import datetime

class BackupController:
    def __init__(self, backupFolder = "Backups", databaseName = "database.db"):
        self.backupFolder = backupFolder
        self.databaseName = databaseName
        os.makedirs(self.backupFolder, exist_ok=True)

    def create_backup(self):
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backupName = now + ".db"
        backupPath = os.path.join(self.backupFolder, backupName)
        shutil.copy2(self.databaseName, backupPath)
import shutil
import os
from datetime import datetime

class BackupController:
    def __init__(self, backupFolder="Backups", databaseName="database.db"):
        #Sets the backup folder
        self.backupFolder = backupFolder
        #Sets the name of the database to copy
        self.databaseName = databaseName
        #Makes backup folder if doesn't already exist
        os.makedirs(self.backupFolder, exist_ok=True)
    def create_backup(self):
        #Retrieves current time and sets it to backup path
        now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        backupName = now + ".db"
        backupPath = os.path.join(self.backupFolder, backupName)
        #Copies the database to new path
        shutil.copy2(self.databaseName, backupPath)

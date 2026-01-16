from LogClass import Log
from DatabaseWriterClass import DatabaseWriter

class LogController:
    def __init__(self):
        self.logObjects = []
        self.db = DatabaseWriter()

    def create_log(self, logId, action, date, time, updateDatabase=True):
        log = Log(logId, action, date, time)
        self.logObjects.append(log)

        if updateDatabase:
            self.db.create_log_db(logId, action, date, time)

    def get_log_objects(self):
        return self.logObjects


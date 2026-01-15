from DatabaseWriterClass import create_log_db

class LogController:
    def __init__(self):
        self.logObjects = []
    def create_log(self, logId, action, date, time, updateDatabase):
        log = Log(logId, action, date, time)
        self.logObjects.append(log)
        if updateDatabase:
            create_log_db(logId, action, date, time)

    def get_log_objects(self):
        return self.logObjects

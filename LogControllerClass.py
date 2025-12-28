from DatabaseWriterClass import create_log_db

class LogController:
    def __init__(self):
        pass
    def create_log(self, logId, action, date, time, updateDatabase, logObjects):
        log = Log(logId, action, date, time)
        logObjects.append(log)
        if updateDatabase:
            create_log_db(logId, action, date, time)
        return logObjects

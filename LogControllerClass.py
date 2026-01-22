from LogClass import Log
from DatabaseWriterClass import DatabaseWriter

class LogController:
    def __init__(self):
        #Creates empty list of log objects
        self.logObjects = []
        #Access to database
        self.db = DatabaseWriter()
    def create_log(self, logId, action, date, time, updateDatabase=True):
        #Creates log object
        log = Log(logId, action, date, time)
        #Adds to list of logs
        self.logObjects.append(log)

        #If necessary, update the database.
        if updateDatabase:
            self.db.create_log_db(logId, action, date, time)
    def get_log_objects(self):
        return self.logObjects

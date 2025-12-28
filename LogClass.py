class Log:
    def __init__(self, logId, action, date, time):
        self.logId = logId
        self.action = action
        self.date = date
        self.time = time
    def get_logId(self):
        return self.logId
    def get_action(self):
        return self.action
    def get_date(self):
        return self.date
    def get_time(self):
        return self.time
    def set_logId(self, logId):
        self.logId = logId
    def set_action(self, action):
        self.action = action
    def set_date(self, date):
        self.date = date
    def set_time(self, time):
        self.time = time

from StatusTypeEnum import StatusType

class Component:
    def __init__(self, componentId, componentName, quantity, minQuantity, status):
        self.componentId = componentId
        self.componentName = componentName
        self.quantity = quantity
        self.minQuantity = minQuantity
        self.status = StatusType[status]
    def get_componentId(self):
        return self.componentId
    def get_componentName(self):
        return self.componentName
    def get_quantity(self):
        return self.quantity
    def get_minQuantity(self):
        return self.minQuantity
    def get_status(self):
        return self.status.name
    def set_componentId(self, componentId):
        self.componentId = componentId
    def set_componentName(self, componentName):
        self.componentName = componentName
    def set_quantity(self, quantity):
        self.quantity = quantity
    def set_minQuantity(self, minQuantity):
        self.minQuantity = minQuantity
    def set_status(self, status):
        self.status = StatusType[status]

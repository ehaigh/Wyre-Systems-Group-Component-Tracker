from DatabaseWriterClass import create_component_db, edit_component_db, delete_component_db
from StatusTypeEnum import StatusType

class ComponentController:
    def __init__(self):
        self.componentObjects = []
    def create_component(self, componentId, componentName, quantity, minQuantity, status, updateDatabase):
        component = Component(componentId, componentName, quantity, minQuantity, status)
        self.componentObjects.append(component)
        if updateDatabase:
            create_component_db(componentId, componentName, quantity, minQuantity, status)
    def edit_component(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus):
        itemUpdated = False
        for component in self.componentObjects:
            componentUpdated = False
            if (oldcomponentId == component.get_componentId()):
                itemUpdated = True
                if (newcomponentId != "") and (newcomponentId != None):
                    component.set_componentId(newcomponentId)
                    componentUpdated = True
                if (newcomponentName != "") and (newcomponentName != None):
                    component.set_componentName(newcomponentName)
                    componentUpdated = True
                if (newquantity != "") and (newquantity != None):
                    component.set_quantity(newquantity)
                    componentUpdated = True
                if (newminQuantity != "") and (newminQuantity != None):
                    component.set_minQuantity(newminQuantity)
                    componentUpdated = True
                if (newstatus != "") and (newstatus != None):
                    component.set_status(newstatus)
                    componentUpdated = True
            if componentUpdated:
                edit_component_db(oldcomponentId, component.get_componentId(), component.get_componentName(), component.get_quantity(), component.get_minQuantity(), component.get_status().name)
        return itemUpdated
    def delete_component(self, componentId):
        itemDeleted = False
        for component in self.componentObjects:
            if (componentId == component.get_componentId()):
                itemDeleted = True
                delete_component_db(componentId)
                self.componentObjects.remove(component)
        return itemDeleted

    def get_component_objects(self):
        return self.componentObjects


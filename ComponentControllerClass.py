from ComponentClass import Component
from DatabaseWriterClass import DatabaseWriter

class ComponentController:
    def __init__(self):
        self.componentObjects = []
        self.db = DatabaseWriter()

    def create_component(self, componentId, componentName, quantity, minQuantity, status, updateDatabase=True):
        component = Component(componentId, componentName, quantity, minQuantity, status)
        self.componentObjects.append(component)

        if updateDatabase:
            self.db.create_component_db(componentId, componentName, quantity, minQuantity, status)

    def edit_component(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus):
        for component in self.componentObjects:
            if component.get_componentId() == oldcomponentId:
                if newcomponentId:
                    component.set_componentId(newcomponentId)
                if newcomponentName:
                    component.set_componentName(newcomponentName)
                if newquantity is not None:
                    component.set_quantity(newquantity)
                if newminQuantity is not None:
                    component.set_minQuantity(newminQuantity)
                if newstatus:
                    component.set_status(newstatus)

                self.db.edit_component_db(
                    oldcomponentId,
                    component.get_componentId(),
                    component.get_componentName(),
                    component.get_quantity(),
                    component.get_minQuantity(),
                    component.get_status()
                )
                return True
        return False

    def delete_component(self, componentId):
        for component in self.componentObjects:
            if component.get_componentId() == componentId:
                self.componentObjects.remove(component)
                self.db.delete_component_db(componentId)
                return True
        return False

    def get_component_objects(self):
        return self.componentObjects



from ComponentClass import Component
from DatabaseWriterClass import DatabaseWriter

class ComponentController:
    def __init__(self):
        #Creates empty list of component objects
        self.componentObjects = []
        #Access to database
        self.db = DatabaseWriter()
    def create_component(self, componentId, componentName, quantity, minQuantity, status, updateDatabase=True):
        #Creates component object
        component = Component(componentId, componentName, quantity, minQuantity, status)
        #Adds to list of components
        self.componentObjects.append(component)

        #If necessary, update the database.
        if updateDatabase:
            self.db.create_component_db(componentId, componentName, quantity, minQuantity, status)
    def edit_component(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus):
        #Check if componentId matches
        for component in self.componentObjects:
            if component.get_componentId() == oldcomponentId:
                #If matches, set new attributes
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
                #Edit component in database
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
        #Check if componentId matches
        for component in self.componentObjects:
            if component.get_componentId() == componentId:
                #If matches, delete component object and from database
                self.componentObjects.remove(component)
                self.db.delete_component_db(componentId)
                return True
        return False
    def get_component_objects(self):
        return self.componentObjects




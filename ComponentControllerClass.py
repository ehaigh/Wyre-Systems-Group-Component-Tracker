#source create_component_db, edit_component_db, delete_component_db
#source status enumeration

class ComponentController:
    def __init__(self):
        pass
    def create_component(self, componentId, componentName, quantity, minQuantity, status, updateDatabase, componentObjects):
        component = Component(componentId, componentName, quantity, minQuantity, status)
        componentObjects.append(component)
        if updateDatabase:
            create_component_db(componentId, componentName, quantity, minQuantity, status)
        return componentObjects
    def edit_component(self, oldcomponentId, newcomponentId, newcomponentName, newquantity, newminQuantity, newstatus, componentObjects):
        itemUpdated = False
        for component in componentObjects:
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
                edit_component_db(oldcomponentId, component.get_componentId(), component.get_componentName(), component.get_quantity(), component.get_minQuantity(), component.get_status())
        return componentObjects, itemUpdated
    def delete_component(self, componentId, componentObjects):
        itemDeleted = False
        for component in componentObjects:
            if (componentId == component.get_componentId()):
                itemDeleted = True
                delete_component_db(componentId)
                componentObjects.remove(component)
        return componentObjects, itemDeleted
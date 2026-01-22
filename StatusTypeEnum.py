from enum import Enum

class StatusType(Enum):
    #Contains the 5 types which status can be stored as
    outOfStock = 1
    available = 2
    inUse = 3
    faulty = 4
    maintenance = 5

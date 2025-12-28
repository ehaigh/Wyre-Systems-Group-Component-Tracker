from enum import Enum

class StatusType(Enum):
    outOfStock = 1
    available = 2
    inUse = 3
    faulty = 4
    maintenance = 5
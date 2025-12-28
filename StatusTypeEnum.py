from enum import Enum

class StatusType(Enum):
    outOfStock = "outOfStock"
    available = "available"
    inUse = "inUse"
    faulty = "faulty"
    maintenance = "maintenance"

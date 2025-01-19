from abc import ABC, abstractmethod
from enum import Enum

# Interface
class ITransport(ABC):
    @abstractmethod
    def deliver(self):
        pass

class Truck(ITransport):
    def deliver(self):
        return "Delivering using Truck"

class Ship(ITransport):
    def deliver(self):
        return "Delivering using Ship"

class Flight(ITransport):
    def deliver(self):
        return "Delivering using Airplane"

# Abstract Logistics Class
class Logistics(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def planDelivery(self):
        pass

    @abstractmethod
    def createTransport(self):
        pass

# Concrete Logistics Classes
class RoadLogistics(Logistics):
    def planDelivery(self):
        return f"Planning road delivery for {self.name}"

    def createTransport(self):
        return Truck().deliver()

class SeaLogistics(Logistics):
    def planDelivery(self):
        return f"Planning sea delivery for {self.name}"

    def createTransport(self):
        return Ship().deliver()

class AirLogistics(Logistics):
    def planDelivery(self):
        return f"Planning air delivery for {self.name}"

    def createTransport(self):
        return Flight().deliver()


# Factory Enums
class TransportType(Enum):
    TRUCK = 1
    SHIP = 2
    FLIGHT = 3

class LogisticsType(Enum):
    ROAD = 1
    AIR = 2
    SEA = 3

# Factory Classes
class LogisticsFactory:
    @staticmethod
    def select_logistics(logistics_type):
        if logistics_type == LogisticsType.AIR:
            return AirLogistics("Air Logistics")
        elif logistics_type == LogisticsType.ROAD:
            return RoadLogistics("Road Logistics")
        elif logistics_type == LogisticsType.SEA:
            return SeaLogistics("Sea Logistics")
        return None

class TransportFactory:
    @staticmethod
    def select_transport(transport_type):
        if transport_type == TransportType.TRUCK:
            return Truck()
        elif transport_type == TransportType.SHIP:
            return Ship()
        elif transport_type == TransportType.FLIGHT:
            return Flight()
        return None

# Main Function
def main():
    log_factory = LogisticsFactory()
    logistics = log_factory.select_logistics(LogisticsType.ROAD)
    print(logistics.planDelivery())
    print(logistics.createTransport())

    logistics = log_factory.select_logistics(LogisticsType.SEA)
    print(logistics.planDelivery())
    print(logistics.createTransport())

    logistics = log_factory.select_logistics(LogisticsType.AIR)
    print(logistics.planDelivery())
    print(logistics.createTransport())

if __name__ == "__main__":
    main()

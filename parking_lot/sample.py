"""
Parking Lot
1. The parking lot should have multiple levels, each level with a certain number of parking spots.
2. The parking lot should support different types of vehicles, such as cars, motorcycles, and trucks.
3. Each parking spot should be able to accommodate a specific type of vehicle.
4. The system should assign a parking spot to a vehicle upon entry and release it when the vehicle exits.
5. The system should track the availability of parking spots and provide real-time information to customers.
6. The system should handle multiple entry and exit points and support concurrent access.

ParkingLot
- levels
+ parkVehicle
+ unparkVehicle
+ displayAvailability

Level
- Parking Spot
- floor

Parking Spot
- spotNumber
- Car
- Parking Spot
- isAvailable

Car
- car type
"""

from enum import Enum
from abc import ABC

class VehicleType(Enum):
    CAR = 1
    TRUCK = 2
    MOTORCYCLE = 3

class Vehicle(ABC):
    def __init__(self,license_plate:str,vehicle_type: VehicleType):
        self.lecense_plate = license_plate
        self.vehicle_type = vehicle_type
    
    def get_type(self):
        return self.vehicle_type

class Car(Vehicle):
    def __init__(self, license_plate, vehicle_type):
        super().__init__(license_plate, VehicleType.CAR)
    
class Motorcycle(Vehicle):
    def __init__(self, license_plate, vehicle_type):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

class Truck(Vehicle):
    def __init__(self, license_plate, vehicle_type):
        super().__init__(license_plate, VehicleType.TRUCK)

class ParkingSpot:
    def __init__(self, spot_number):
        self.spot_number = spot_number
        self.spot_type = Ve
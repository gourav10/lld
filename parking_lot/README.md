# Parking Lot Design

## Scenario
Design a parking lot system that handles:
1. Entry and exit of vehicles.
2. Parking space allocation.
3. Payment for parking based on time.
4. Differentiation between vehicle types (e.g., car, bike, truck).
5. Support for multiple parking floors.
6. Real-time display of available parking spots.

---

## Requirements Gathering
1. Large Parking Lot with a capacity of 10,000–30,000 vehicles.
2. **Entrances and Exits**:
   - 4 entrances and 4 exits.
   - Ticket and spot allocation to occur at the entrance.
3. **Parking Spot Allocation**:
   - Allocate the nearest available parking spot to the entrance.
4. **Parking Spot Types**:
   - Handicapped Parking.
   - Compact Car.
   - Large Vehicles.
   - Motorcycles.
5. **Payment System**:
   - Hourly parking rates.
   - Accept both cash and credit cards.
6. Monitoring System for real-time updates.

---

## Design Patterns
1. **Creational Design Patterns**:
   - Focus on object instantiation.
2. **Structural Design Patterns**:
   - Combine objects and classes to form a larger structure.
3. **Behavioral Design Patterns**:
   - Handle responsibilities and interactions among objects.

---

## Design Approach
1. **Top-Down Design**:
   - Start with high-level objects and identify sub-components.
2. **Bottom-Up Design**:
   - Begin with the smallest components, building up to the complete system.
   - Aligns with object-oriented design principles.

---

## Objects and Actors in the System
1. **Parking Lot**:
   - Attributes: capacity, floors.
2. **Entry and Exit Terminals**:
   - Components: printers, payment processors.
3. **Parking Spot**:
   - Types:
     - Handicapped.
     - Compact.
     - Large vehicles.
     - Motorcycle.
4. **Ticket**:
   - Tracks vehicle details, parking spot, and issue time.
5. **Database**:
   - Stores all data related to vehicles, parking spots, and transactions.
6. **Monitoring System**:
   - Provides real-time updates on parking availability.

---

## Ideation

### 1. Parking Spots
- Use an enum-based approach for parking spot types:

   ```python
   from enum import Enum
   class ParkingSpotType(Enum):
       HANDICAPPED = 1
       COMPACT = 2
       LARGE_CAR = 3
       MOTORCYCLE = 4
Consideration:
While enums are straightforward, modifying them can violate the Open/Closed Principle of software design. This principle states:

Open for extension.
Closed for modification.

Using an enum requires changes in multiple parts of the code, which may lead to fragility and bugs. An alternative solution could involve creating a class hierarchy for parking spots.

### 2. Parking Lot
The Parking Lot class will be a singleton class and it will contain multiple smaller objects.

- Can take configurations

### Smaller objects
We will use  Abstract Factory and Factory Design pattern to instantiate smaller objects.

- Set of terminals will be instantiated
- Instantiate parking assignment strategy and pass configuration object
  - 

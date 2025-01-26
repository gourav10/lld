"""
Design Problem:
Design a Bag Locker System for Amazon where customers can securely store their bags at Amazon facilities while shopping 
or picking up orders.

Requirements:
Users should be able to use a code to open a locker and pick up a package
Delivery guy should be able to find an "optimal" locker for a package

Functional Requirements:
- Package
    - Package ID
    - Delivery Agent
    - Customer
    - LockerID

- Customer:
    - CustomerID
    - Name
    - Package Object

- Locker Class
    - package
    - Access Code
    - isAvailable
"""

from enum import Enum
from abc import ABC, abstractmethod

class LockerType(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE  = 3

class Observer(ABC):
    def __init__(self):
        self._observers = set()

    @abstractmethod
    def subscribe(self,customer):
        pass

    @abstractmethod
    def unsubscribe(self,customer):
        pass

    @abstractmethod
    def notify(self,package,agent):
        pass

class LockerManager(Observer):

    def __init__(self):
        self.lockers = {}
        self.agents = {}
        self.customers = {}

        for i in range(10):
            self.lockers[i] = False

    def addUser(self,customer):
        self.customers[customer.ID] = customer
    
    def addAgent(self,agent):

        self.agents[agent.ID] = agent

    def subscribe(self, customer,agent):
        for i in range(10):
            if self.lockers[i].isAvailable:
                self.lockers.agent = agent.id
                self.lockers.customer = customer.id
                self.lockers.isAvailable = False
                self.notify(locker, customer)
    
    def unsubscribe(self, customer):
        if (customer.order == "Delivered"):
            for locker in self.lockers:
                if customer.lockerID == locker.id:
                    locker.isAvailable = True

    def notify(self, customer):
        for observer in self._observers:
            if observer == package.customer:
                package.customer.update(f"{package.ID} assigned to Locker: {locker.id}")
    
class Subject(ABC):
    @abstractmethod
    def update(self,message):
        pass

class Customer(Subject):
    def __init__(self,name,id):
        self.name = name
        self.id = id
        self.order = None
        self.lockerId = None
        super().__init__()

class Locker(ABC):
    def __init__(self, lockerID, customerID, agentID):
        self.
        super().__init__()

    @abstractmethod
    def setPackage(self):
        pass

    @abstractmethod
    def update(self):
        pass

class SmallLocker(Locker):
    def __init__(self,agentID):
        super().__init__()

    
class Package:
    def __init__(self, packageID, customerID, agentID, lockerID):
        self.packageID = packageID
        self.customerID = customerID
        self.agentID = agentID
        self.lockerID = lockerID
    


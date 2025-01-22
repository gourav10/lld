from abc import ABC, abstractmethod

class Restaurant:
    def __init__(self, name, rating, location, menu):
        self.name = name
        self.rating = rating
        self.location = location
        self.menu = menu

    def getMenu(self):
        return self.menu

    def getlocation(self):
        return self.location

    def geRating(self):
        return self.rating

    def getName(self):
        return self.name

class User:
    def __init__(self,userName,userID,userLocation):
        self.userName = userName
        self.userID = userID
        self.userLocation = userLocation

    @abstractmethod
    def getUserID(self):
        return self.userName
    
    @abstractmethod
    def destinationLocation(self):
        pass

    @abstractmethod
    def getName(self):
        return self.userName

    
class Driver(User):
    def __init__(self, userName, userID, userLocation):
        super().__init__(userName, userID, userLocation)
        self.is_available = False

    def getUserID(self):
        return super().getUserID()
    
    def destinationLocation(self):
        return super().destinationLocation()
    
    def isAvailable(self):
        return self.is_available

    
class Order:
    def __init__(self, food, user,restaurant,driver):
        self.food = food
        self.user = user
        self.restaurant = restaurant
        self.driver = driver
    
    def generateOrder(self):
        if self.driver.isAvailable():
            return "Order Placed Successfully!"
        
class OrderManager:
    def __init__(self):
        self.users = []
        self.drivers = []
        pass

    def getFood(self,user, restaurant,foodItems):
        pass

    def getAvailableAgent(self):
        if len(self.drivers)>0:
            return self.drivers.pop()

    def placeOrder(self,food,restaurant,user,avail_driver):
        if food and avail_driver:
            print("Order Placed Successfully!")
        else:
            print("Failed to place order")
        return Order(food,user,restaurant,avail_driver)



class FoodApp:

    def __init__(self):
        self.order_id = 0
        self.restaurants = [
            Restaurant("Agas","4","1.01","A,B,C"),
            Restaurant("Wendys","3","2.01","G,H"),
            Restaurant("Hopdoddy","4.3","3","A,B")
        ]
        self.user = User("Abhi","1234","10.22")
        self.orderManager = OrderManager()
        self.orderManager.drivers = [Driver("SAM","qwert","ASDA")]
        pass
    
    def showRest(self):
        res = []
        for r in self.restaurants:
            res.append((r.getName(),r.geRating()))
        return res
    
    def search(self,text):
        res = []
        for rest in self.restaurants:
            if text in rest.getMenu():
                res.append(rest.getName())
        # return list of restaurants

        return res


    def order(self,restaurant,food_items):
        self.order_id+=1
        avail_driver = self.orderManager.getAvailableAgent()
        print(f"Available Driver: {avail_driver.userName}")
        return self.orderManager.placeOrder(restaurant,self.user,restaurant,avail_driver)

    def showStatus(self,order:Order):
        print(order.user.getName())
        print(order.driver.getName())
        for i in range(5,-1,-1):
            print(f"Distance Left: {order.user.userLocation}+{i}")


if __name__ == "__main__":
    app = FoodApp()

    print(app.showRest())
    
    print(f"Searched Item: A, Result: {app.search("A")}")
    order = app.order(app.restaurants[0],["A,B"])
    # print(app.order(app.restaurants[0],["A,B"]))
    print(app.showStatus(order))
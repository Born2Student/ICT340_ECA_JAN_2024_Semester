from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def registerObserver(self, observer):
        pass

    @abstractmethod
    def removeObserver(self, observer):
        pass

    @abstractmethod
    def notifyObservers(self):
        pass

class Observer(ABC):
    @abstractmethod
    def update(self):
        pass




class Customer(Observer):
    def __init__(self, name):
        self.customerName = name
        

    def update(self):
        print(f"{self.customerName} has been notified of a discount!")

class FoodItem(Subject):
    def __init__(self, name):
        self.itemName = name
        self.discount = 0
        self.observers = []

    def registerObserver(self, observer):
        self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()

    def setDiscount(self, discount):
        self.discount = discount
        self.notifyObservers()

class StallOwner:
    def giveDiscount(self, foodItem, discount):
        foodItem.setDiscount(discount)

# Example usage:

# Create instances
food_item = FoodItem("Pizza")

customer1 = Customer("Alice")
customer2 = Customer("Bob")
stall_owner = StallOwner()

# Register customers as observers
food_item.registerObserver(customer1)
food_item.registerObserver(customer2)

# Stall owner gives a discount
stall_owner.giveDiscount(food_item, 0.2)  # 20% discount

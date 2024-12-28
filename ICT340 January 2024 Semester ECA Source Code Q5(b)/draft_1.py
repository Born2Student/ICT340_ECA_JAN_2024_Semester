from abc import ABC, abstractmethod

### DONE
class Observer():
    def update(self, subject):
        pass

### DONE
class Subject:
    def __init__(self):
        self._observers = []
    
    def registerObserver(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def removeObserver(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notifyObservers(self, modifer = None):
        for observer in self._observers:
            if modifer != observer:
                observer.update(self)



class Feedback(Subject):
    def __init__(self, description):
        Subject.__init__(self)
        self._description = description
        self._ratings = 0
        
    @property
    def description(self):
        return self._description

    @property
    def ratings(self):
        return self._ratings

    @description.setter
    def description(self, description):
        self._description = description
        self.notifyObservers()

    @ratings.setter
    def ratings(self, ratings):
        self._ratings = ratings
        self.notifyObservers()
    
    # def registerObserver(self, observer):
    #     if observer not in self._observers:
    #         self._observers.append(observer)
    
    # def removeObserver(self, observer):
    #     try:
    #         self._observers.remove(observer)
    #     except ValueError:
    #         pass
    
    # def notifyObservers(self):
    #     for observer in self._observers:
    #         observer.update()
    

class Administrator(Observer):
    def __init__(self, name):
        self._adminName = name
        # self._adminName.registerObserver(self)
    
    def update(self, subject):
        print(f"Feedback: {subject.description}, {subject.ratings}. \n 
        The Administrator {self._adminName} has been notified of the feedback.")

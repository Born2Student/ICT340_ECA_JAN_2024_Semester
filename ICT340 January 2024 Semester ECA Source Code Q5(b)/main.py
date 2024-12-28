class Observer():
    def update(self, subject):
        pass


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
    
    def notifyObservers(self, modifier = None):
        for observer in self._observers:
            if modifier != observer:
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


    @ratings.setter
    def ratings(self, ratings):
        self._ratings = ratings
        self.notifyObservers()



class Administrator(Observer):
    def __init__(self, name):
        self._adminName = name
    
    def update(self, subject):
        print(f"Feedback: {subject.description}, Rating: {subject.ratings}. \n The Administrator {self._adminName} has been notified of the feedback. \n")


def main():
  # Create an administrator
  admin_1 = Administrator("Anson Goh")
  admin_2 = Administrator("Jason Wang")

  # Create some feedback
  feedback1 = Feedback("Great ride!")
  feedback2 = Feedback("Car was dirty")

  # Register the administrator to receive notifications from both feedbacks
  feedback1.registerObserver(admin_1)
  feedback2.registerObserver(admin_2)

  # Set the description and ratings for the feedbacks (This will trigger notification)
#   feedback1.description = "Excellent service by the driver"
  feedback1.ratings = 5
  feedback2.ratings = 3

if __name__ == "__main__":
  main()
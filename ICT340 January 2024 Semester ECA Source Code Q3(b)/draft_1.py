""" 
Question 3(b)

Implement the method in the following classes that is responsible for accepting a ride and assigning a driver:

Question 3(b)(i) (4 marks)

the orchestrating class """

class OrchestratingClass:
    def __init__(self):
        """ constructor that execute when an object is created """
        self.rideDict = {}

    def findRide(self, rideReference):
        return self.rideDict[rideReference]
    
    def findDriver(self, driverID):
        return self.rideDict[driverID]

    def acceptRide(self, driverID, rideReference):
            aRide = self.findRide(rideReference)    # is a self message
            aDriver = self.findDriver(driverID)     # is a self message
            updateRide = aRide.setDriver(aDriver)
            return updateRide

class aRide:
  def __init__(self, rideReference, driverID, rideStatus):
    self._rideReference = rideReference
    self._driverID = driverID
    self._rideStatus = rideStatus

  def setDriver(self, aDriver):
    self._driverID = aDriver.driverID
    self._rideStatus = "Driver Assigned"

  @property
  def rideStatus(self):
    return self._rideStatus

  @rideStatus.setter
  def rideStatus(self, newrideStatus):
    self._rideStatus = newrideStatus


class Driver:  # Simple Driver class for testing
  def __init__(self, driverID):
    self.driverID = driverID


def main():
  # Create Test Objects
    driver1 = Driver(123)
    ride1 = aRide("ABC123", None, "Open")

    # Orchestrating Object (assuming it's created elsewhere)
    orchestrator = OrchestratingClass()
    orchestrator.rideDict[ride1._rideReference] = ride1
    orchestrator.rideDict[driver1.driverID] = driver1

    # Test Accepting a Ride (assuming OrchestratingClass methods are available)
    accepted_ride = orchestrator.acceptRide(driver1.driverID, ride1._rideReference)   # Simulate calling through OrchestratingClass

    # Test Assertions
    assert accepted_ride.rideStatus == "Driver Assigned"
    assert ride1.rideStatus == "Driver Assigned"  # Verify ride object is updated
    assert accepted_ride._driverID == driver1.driverID  # Verify driver assigned


if __name__ == "__main__":
  main()
  print("Tests Passed!")

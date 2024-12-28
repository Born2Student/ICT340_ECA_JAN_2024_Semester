#### Correct ####
class OrchestratingClass:
    def __init__(self):
        self.rideDict = {}
        self.driverDict = {}

    def findRide(self, rideReference):
        return self.rideDict.get(rideReference)  # Use get() for potential non-existence

    def findDriver(self, driverID):
        return self.driverDict.get(driverID)

    def acceptRide(self, driverID, rideReference):
        aRide = self.findRide(rideReference)
        aDriver = self.findDriver(driverID)
        return aRide.setDriver(aDriver)

#### Additional ####
class Driver:
    def __init__(self, driverId):
        self._driverId = driverId

##############################

class Ride:
    def __init__(self, rideReference):
        self._rideReference = rideReference
        self._rideStatus = "Open"  # Initial status
        self._driver = None  # Initially unassigned

    @property
    def updateRideStatus(self):
        return self._rideStatus

    @updateRideStatus.setter
    def updateRideStatus(self, newrideStatus):
        return newrideStatus

    def setDriver(self, driver):
        self._driver = driver
        self._rideStatus = "Driver Assigned"
        # driver.acceptRide()
        return True
    


def main():
    # Create test objects
    driver1 = Driver(123)
    ride1 = Ride("ABC123")

    # Orchestrating object (assuming one instance)
    orchestrator = OrchestratingClass()

    # Add objects to dictionaries
    orchestrator.driverDict[driver1._driverId] = driver1
    orchestrator.rideDict[ride1._rideReference] = ride1

    # Simulate accepting the ride
    success = orchestrator.acceptRide(driver1._driverId, ride1._rideReference)

    if success:
        print(f"Ride details after assignment: \n Ride Reference: {ride1._rideReference} \n Driver Assigned: {driver1._driverId} \n Ride Status: {ride1._rideStatus}")
    else:
        print("Error: Ride or driver not found, or driver already assigned")

if __name__ == "__main__":
    main()
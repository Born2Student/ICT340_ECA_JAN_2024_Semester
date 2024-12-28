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
        self.driverId = driverId
        self._rideStatus = "Open"  # Initial status

    @property
    def updateRideStatus(self):
        return self._rideStatus

    @updateRideStatus.setter
    def updateRideStatus(self, newrideStatus):
        return newrideStatus

    def acceptRide(self):
        self._rideStatus = "Driver Assigned"

##############################

class Ride:
    def __init__(self, rideReference):
        self.rideReference = rideReference
        self.driver = None  # Initially unassigned

    def setDriver(self, driver):
            driver = self.driver
            # self._rideStatus = "Driver Assigned"
            # driver_acceptRide = aDriver.acceptRide(driverID)
            # return driver_acceptRide
            driver_accept = driver.acceptRide()
            return driver_accept

def main():
    # Create test objects
    driver1 = Driver(123)
    ride1 = Ride("ABC123")

    # Orchestrating object (assuming one instance)
    orchestrator = OrchestratingClass()

    # Add objects to dictionaries
    orchestrator.driverDict[driver1.driverId] = driver1
    orchestrator.rideDict[ride1.rideReference] = ride1

    # Simulate accepting the ride
    success = orchestrator.acceptRide(driver1.driverId, ride1.rideReference)

    if success:
        print(f"Ride details after assignment: \n Ride Reference: {ride1.rideReference} \n Driver Assigned: {driver1.driverId} \n Ride Status: {ride1._rideStatus}")
    else:
        print("Error: Ride or driver not found, or driver already assigned")

if __name__ == "__main__":
    main()
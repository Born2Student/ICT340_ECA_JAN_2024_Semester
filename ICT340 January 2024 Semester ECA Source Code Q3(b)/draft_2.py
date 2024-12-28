class Driver:
    def __init__(self, driverID):
        self.driverID = driverID

class OrchestratingClass:
    def __init__(self):
        """ constructor that executes when an object is created """
        self.rideDict = {}
        self.driverDict = {}

    def findRide(self, rideReference):
        return self.rideDict[rideReference]

    def findDriver(self, driverID):
        return self.driverDict[driverID]

    def acceptRide(self, driverID, rideReference):
        aRide = self.findRide(rideReference)
        aDriver = self.findDriver(driverID)
        return aRide.setDriver(aDriver)

class aRide:
    def __init__(self,  rideReference):
        self.rideReference = rideReference
        self.driver = None
        self._rideStatus = "Driver Unassigned"

    @property
    def rideStatus(self):
        return self._rideStatus

    @rideStatus.setter
    def rideStatus(self, newrideStatus):
        self._rideStatus = newrideStatus

    def setDriver(self, driver):
        self.driver = driver
        self._rideStatus = "Driver Assigned"
        return self

    


def main():
    orchestrator = OrchestratingClass()

    # Create ride and driver objects
    ride1 = aRide("ride123")
    driver1 = Driver("driver456")

    # Add ride and driver to the orchestrator's dictionary
    orchestrator.rideDict[ride1.rideReference] = ride1
    orchestrator.rideDict[driver1.driverID] = driver1

    # Call acceptRide to assign the driver to the ride
    assignedRide = orchestrator.acceptRide(driver1.driverID, ride1.rideReference)

    # Print the ride details after the driver is assigned
    print(f"Ride details after assignment: \n Ride Reference: {assignedRide.rideReference} \n Driver Assigned: {assignedRide.driver.driverID} \n Ride Status: {assignedRide._rideStatus}")


if __name__ == "__main__":
    main()

""" 
Question 3(b)

Implement the method in the following classes that is responsible for accepting a ride and assigning a driver:

Question 3(b)(i) (4 marks)

the orchestrating class """

### CORRECT
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


############ Additional     ############

class aDriver:
    def __init__(self, driverID):
        self.driverID = driverID

############################################

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

    def setDriver(self, driverID):
        self.driver = driverID
        self._rideStatus = "Driver Assigned"
        # aDriver.acceptRide(aRide)
        return self


def main():
    orchestrator = OrchestratingClass()

    # Create ride and driver objects
    ride1 = aRide("ride123")
    driver1 = aDriver("driver456")

    # Add ride and driver to the orchestrator's dictionary
    orchestrator.rideDict[ride1.rideReference] = ride1
    orchestrator.rideDict[driver1.driverID] = driver1

    # Call acceptRide to assign the driver to the ride
    assignedRide = orchestrator.acceptRide(driver1.driverID, ride1.rideReference)

    # Print the ride details after the driver is assigned
    print(f"Ride details after assignment: \n Ride Reference: {assignedRide.rideReference} \n Driver Assigned: {assignedRide.driver.driverID} \n Ride Status: {assignedRide._rideStatus}")


if __name__ == "__main__":
    main()

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


class Ride:
  def __init__(self, rideReference):
    self.rideReference = rideReference
    self.driver = None  # Initially, no driver is assigned
    self.status = "unassigned"  # Initial status is unassigned

  def setDriver(self, driver):
        """Assigns a driver to the ride and updates the ride status"""
        if driver:  # Check if a driver is assigned (not None)
            self.driver = driver
            self.status = "Driver Assigned"
            driver.acceptRide(self)  # Call driver's acceptRide method only if driver exists
        else:
            print("No driver assigned to the ride yet.")
        return self


class Driver:
  def __init__(self, driverID):
    self.ID = driverID  # Assuming Driver has an ID attribute

  def acceptRide(self, ride):
    """Confirms if the driver accepts the ride (replace with your logic)"""
    print(f"Driver {self.ID} received ride request for {ride.rideReference}.")
    # Simulate driver accepting the ride
    ride.status = "Driver Accepted"  # Update ride status in Ride object (assuming permission)
    print(f"Driver {self.ID} accepted ride {ride.rideReference}.")



def main():
    # Create some test objects
    ride1 = Ride("ride_123")
    driver1 = Driver("driver_456")

    # Create an orchestrating class object
    orchestrator = OrchestratingClass()

    # Add ride and driver to the orchestrator's dictionary
    orchestrator.rideDict[ride1.rideReference] = ride1
    orchestrator.rideDict[driver1.ID] = driver1

    # Accept the ride
    acceptedRide = orchestrator.acceptRide(driver1.ID, ride1.rideReference)

    # Print the ride details
    print(f"Ride details after accepting: \n  Reference: {acceptedRide.rideReference} \n  Status: {acceptedRide.status} \n  Driver: {acceptedRide.driver.ID}")


if __name__ == "__main__":
    main()
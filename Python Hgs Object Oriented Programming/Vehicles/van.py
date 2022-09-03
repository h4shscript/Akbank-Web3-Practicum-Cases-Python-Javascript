from vehicle import Vehicle, VehicleClasses
from Management.passthroug_vehicles import PassthroughVehicles


class Van(Vehicle, PassthroughVehicles):
    vehicle_classes = VehicleClasses.van

    def passthrough_vehicle_counter(self):
        if Van.passthrough_vehicles == []:
            print('No vehicle passed.')
        else:
            print(Van.passthrough_vehicles)

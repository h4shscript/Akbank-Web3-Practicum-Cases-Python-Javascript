from vehicle import Vehicle, VehicleClasses
from Management.passthroug_vehicles import PassthroughVehicles


class Car(Vehicle, PassthroughVehicles):
    vehicle_classes = VehicleClasses.car

    def passthrough_vehicle_counter(self):
        if Car.passthrough_vehicles == []:
            print('No vehicle passed.')
        else:
            print(Car.passthrough_vehicles)

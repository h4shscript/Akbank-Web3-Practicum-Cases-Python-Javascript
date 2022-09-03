from vehicle import Vehicle, VehicleClasses
from Management.passthroug_vehicles import PassthroughVehicles


class Bus(Vehicle, PassthroughVehicles):
    vehicle_classes = VehicleClasses.bus

    def passthrough_vehicle_counter(self):
        if Bus.passthrough_vehicles == []:
            print('No vehicle passed.')
        else:
            print(Bus.passthrough_vehicles)

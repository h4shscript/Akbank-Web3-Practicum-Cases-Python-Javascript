from datetime import *

from Counter.counter import Counter
from Management.fees import Fees
from Vehicles.vehicle import VehicleClasses
from Vehicles.car import Car
from Vehicles.van import Van
from Vehicles.bus import Bus


class HGSSystem:
    today = datetime.date.today()

    def hgs_control(self, vehicle):
        Counter.passing_vehicles.append(vehicle)
        passing_date = str(vehicle.date())
        if passing_date == HGSSystem.today:
            if VehicleClasses == 'car':
                Car.passthrough_vehicles.append(vehicle.hgsnumber)
                vehicle.balance -= Fees.car_fee
                Fees.total_fee += Fees.car_fee
            elif VehicleClasses == 'van':
                Van.passthrough_vehicles.append(vehicle.hgsNumber)
                vehicle.balance -= Fees.van_fee
                Fees.total_fee += Fees.van_fee
            else:
                Bus.passthrough_vehicles.append(vehicle.hgsnumber)
                vehicle.balance -= Fees.bus_fee
                Fees.total_fee += Fees.bus_fee
        else:
            return 'No vehicles passed today.'

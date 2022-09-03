from Vehicles.car import Car
from Vehicles.van import Van
from Vehicles.bus import Bus


class Counter(Car, Van, Bus):
    passing_vehicles = []

    def passing_vehicles_count(self):
        print(Counter.passing_vehicles)

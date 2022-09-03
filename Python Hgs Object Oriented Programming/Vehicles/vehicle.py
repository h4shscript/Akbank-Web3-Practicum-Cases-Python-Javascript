from enum import Enum


class Vehicle:

    def __init__(self, name, surname, hgsnumber, date, time, balance):
        self.name = name
        self.surname = surname
        self.hgsNumber = hgsnumber
        self.date = date
        self.time = time
        self.balance = balance


class VehicleClasses(Enum):
    car = 'car'
    van = 'van'
    bus = 'bus'

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, regnum, make, model, color):
        self.regnum = regnum
        self.make = make
        self.model = model
        self.color = color
        self.is_ev = False

    @abstractmethod
    def get_type(self):
        pass


# ---------- Regular vehicles ----------

class Car(Vehicle):
    def get_type(self):
        return "Car"


class Motorcycle(Vehicle):
    def get_type(self):
        return "Motorcycle"


# ---------- EV behavior via composition ----------

class ElectricMixin:
    def __init__(self):
        self.charge = 0
        self.is_ev = True

    def set_charge(self, value):
        self.charge = value

    def get_charge(self):
        return self.charge


class ElectricCar(Car, ElectricMixin):
    def __init__(self, *args):
        Car.__init__(self, *args)
        ElectricMixin.__init__(self)


class ElectricBike(Motorcycle, ElectricMixin):
    def __init__(self, *args):
        Motorcycle.__init__(self, *args)
        ElectricMixin.__init__(self)

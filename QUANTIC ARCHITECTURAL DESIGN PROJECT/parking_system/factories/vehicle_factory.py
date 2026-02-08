from domain.vehicle import Car, Motorcycle, ElectricCar, ElectricBike


class VehicleFactory:

    @staticmethod
    def create(is_electric, is_motorcycle, reg, make, model, color):
        if is_electric and is_motorcycle:
            return ElectricBike(reg, make, model, color)
        if is_electric:
            return ElectricCar(reg, make, model, color)
        if is_motorcycle:
            return Motorcycle(reg, make, model, color)
        return Car(reg, make, model, color)

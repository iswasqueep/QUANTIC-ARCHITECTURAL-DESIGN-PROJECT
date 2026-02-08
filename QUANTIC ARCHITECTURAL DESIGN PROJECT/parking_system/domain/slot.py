class Slot:
    def __init__(self):
        self.vehicle = None

    def is_free(self):
        return self.vehicle is None

    def park(self, vehicle):
        self.vehicle = vehicle

    def remove(self):
        self.vehicle = None

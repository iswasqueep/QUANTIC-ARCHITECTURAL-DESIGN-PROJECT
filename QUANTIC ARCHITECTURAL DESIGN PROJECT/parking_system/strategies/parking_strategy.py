from abc import ABC, abstractmethod


class ParkingStrategy(ABC):
    @abstractmethod
    def find_slot(self, slots):
        pass

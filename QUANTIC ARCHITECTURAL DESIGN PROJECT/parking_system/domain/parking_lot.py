from domain.slot import Slot
class ParkingLot:

    def __init__(self, regular_capacity, ev_capacity, strategy=None):
        self.regular_free = regular_capacity
        self.ev_free = ev_capacity
        self.slots = {}
        self.next_slot = 1


    def park_vehicle(self, vehicle):

        if vehicle.is_ev:
            if self.ev_free <= 0:
                return -1
            self.ev_free -= 1
        else:
            if self.regular_free <= 0:
                return -1
            self.regular_free -= 1

        slot_id = self.next_slot
        self.slots[slot_id] = vehicle
        self.next_slot += 1

        return slot_id


    def remove_vehicle(self, slot_id):

        if slot_id not in self.slots:
            return False

        vehicle = self.slots[slot_id]
        del self.slots[slot_id]

        if vehicle.is_ev:
            self.ev_free += 1
        else:
            self.regular_free += 1

        return True
    
    def get_by_registration(self, regnum):
        for slot_id, vehicle in self.slots.items():
            if vehicle.regnum == regnum:
                return slot_id, vehicle
        return None


    def status(self):
        return f"Regular free: {self.regular_free} | EV free: {self.ev_free}"
    
 
   
    
  

        

    

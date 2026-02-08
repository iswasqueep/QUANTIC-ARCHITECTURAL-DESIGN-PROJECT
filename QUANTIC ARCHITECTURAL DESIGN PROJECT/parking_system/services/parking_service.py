# class ParkingService:

#     def __init__(self, parking_lot):
#         self.lot = parking_lot

#     # ----------------
#     # core operations
#     # ----------------

#     def park_vehicle(self, vehicle):
#         return self.lot.park(vehicle)

#     def remove_vehicle(self, slot_id):
#         self.lot.leave(slot_id)

#     # ----------------
#     # status / reports
#     # ----------------

#     def status(self):
#         return self.lot.status()

#     def charge_status(self):
#         return self.lot.charge_status()

#     # ----------------
#     # search helpers
#     # ----------------

#     def slot_by_reg(self, reg):
#         return self.lot.get_slot_by_reg(reg)

#     def slot_by_color(self, color):
#         return self.lot.get_slots_by_color(color)

#     def reg_by_color(self, color):
#         return self.lot.get_regs_by_color(color)

class ParkingService:

    def __init__(self, strategy):
        self.strategy = strategy
        self.lot = None   # created later dynamically

    # ------------------------
    # create lot dynamically
    # ------------------------

    # def create_lot(self, capacity):
    #     from domain.parking_lot import ParkingLot
    #     self.lot = ParkingLot(capacity, self.strategy)
    def create_lot(self, regular, ev):
        from domain.parking_lot import ParkingLot
        self.lot = ParkingLot(regular, ev, self.strategy)

    # ------------------------
    # parking operations
    # ------------------------

    def park_vehicle(self, vehicle):
        return self.lot.park(vehicle)

    def remove_vehicle(self, slot_id, is_ev):
        self.lot.leave(slot_id, is_ev)

    def status(self):
        return self.lot.status()

    def charge_status(self):
        return self.lot.charge_status()

    def slot_by_reg(self, reg):
        return self.lot.get_slot_by_reg(reg)

    def slot_by_color(self, color):
        return self.lot.get_slots_by_color(color)

    def reg_by_color(self, color):
        return self.lot.get_regs_by_color(color)
    
    def get_by_registration(self, reg):
        return self.lot.get_by_registration(reg)

class RegularParkingStrategy:
    def find_slot(self, slots):
        for slot in slots:
            if slot.is_free():
                return slot
        return None

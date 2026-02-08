import tkinter as tk
from factories.vehicle_factory import VehicleFactory
from strategies.regular_parking_strategy import RegularParkingStrategy
from domain.parking_lot import ParkingLot


class TkinterAdapter:

    def __init__(self, parking_lot):

        self.parking_lot = parking_lot
        # self.service = parking_lot
        self.service = None
    

        self.root = tk.Tk()
        self.root.geometry("650x850")
        self.root.resizable(0, 0)
        self.root.title("Parking Lot Manager")
        


        # =========================
        # Variables Declaration
        # =========================
        self.num_value = tk.StringVar()
        self.ev_value = tk.StringVar()
        self.level_value = tk.StringVar(value="1")

        self.make_value = tk.StringVar()
        self.model_value = tk.StringVar()
        self.color_value = tk.StringVar()
        self.reg_value = tk.StringVar()

        self.slot_value = tk.StringVar()
        self.search_reg_value = tk.StringVar()

        self.ev_car_value = tk.IntVar()
        self.motor_value = tk.IntVar()
        

        # Output
        self.tfield = tk.Text(self.root, width=70, height=15)

        self.build_ui()

    # ======================================
    # BUILDING GUI 
    # ======================================

    def build_ui(self):

        tk.Label(self.root, text='Parking Lot Manager', font='Arial 14 bold').grid(row=0, columnspan=4)

        tk.Label(self.root, text='Lot Creation', font='Arial 12 bold').grid(row=1, columnspan=4)

        tk.Label(self.root, text='Number of Regular Spaces').grid(row=2, column=0)
        tk.Entry(self.root, textvariable=self.num_value, width=6).grid(row=2, column=1)

        tk.Label(self.root, text='Number of EV Spaces').grid(row=2, column=2)
        tk.Entry(self.root, textvariable=self.ev_value, width=6).grid(row=2, column=3)

        tk.Label(self.root, text='Floor Level').grid(row=3, column=0)
        tk.Entry(self.root, textvariable=self.level_value, width=6).grid(row=3, column=1)

        tk.Button(self.root, text="Create Parking Lot",
                  command=self.create_lot).grid(row=4, column=0)
        tk.Button(self.root, text="Remove Car", command=self.remove_car).grid(row=11, column=0)

        tk.Label(self.root, text='Search / Allocation Pane', font='Arial 12 bold')\
    .grid(row=12, columnspan=4, pady=(15, 5))
        
        
        

       
        


        
       


        # =================
        # Car Management
        # =================

        tk.Label(self.root, text='Car Management', font='Arial 12 bold').grid(row=5, columnspan=4)

        tk.Label(self.root, text='Make').grid(row=6, column=0)
        tk.Entry(self.root, textvariable=self.make_value).grid(row=6, column=1)

        tk.Label(self.root, text='Model').grid(row=6, column=2)
        tk.Entry(self.root, textvariable=self.model_value).grid(row=6, column=3)

        tk.Label(self.root, text='Color').grid(row=7, column=0)
        tk.Entry(self.root, textvariable=self.color_value).grid(row=7, column=1)

        tk.Label(self.root, text='Registration #').grid(row=7, column=2)
        tk.Entry(self.root, textvariable=self.reg_value).grid(row=7, column=3)

        tk.Checkbutton(self.root, text='Electric Car', variable=self.ev_car_value).grid(row=8, column=0)
        tk.Checkbutton(self.root, text='Regular Car', variable=self.motor_value).grid(row=8, column=1)

        tk.Button(self.root, text="Park Car", command=self.park_car).grid(row=9, column=0)

        tk.Label(self.root, text='Slot #').grid(row=10, column=0)
        tk.Entry(self.root, textvariable=self.slot_value).grid(row=10, column=1)

        tk.Button(self.root, text="Remove Car", command=self.remove_car).grid(row=11, column=0)

        

        self.tfield.grid(row=16, columnspan=4)

        tk.Label(self.root, text="Search by Registration").grid(row=17, column=0, sticky="w")

        tk.Entry(
    self.root,
    textvariable=self.search_reg_value,
    width=20
).grid(row=17, column=1, padx=5)

        tk.Button(
    self.root,
    text="Search",
    command=self.search_by_registration
).grid(row=17, column=2)

        

    # ======================================
    # BUTTON LOGIC (NEW ARCHITECTURE)
    # ======================================

    
    # def create_lot(self):
    #     capacity = int(self.num_value.get())
    #     self.service.create_lot(capacity)  
    #     self.output(f"Created parking lot with {capacity} slots\n")

    def create_lot(self):
        if self.service is not None:
            self.output("Parking lot already created\n")
            return
        
        regular_txt = self.num_value.get().strip()
        ev_txt = self.ev_value.get().strip()
        if not regular_txt or not ev_txt:
            self.output("Please enter both Regular and EV spaces\n")
            return
        
        if not regular_txt.isdigit() or not ev_txt.isdigit():
            self.output("Spaces must be numbers only\n")
            return
        
        regular = int(regular_txt)
        ev = int(ev_txt)
        strategy = RegularParkingStrategy()
        self.service = ParkingLot(regular, ev, strategy)
        self.output(f"Lot created: Regular={regular}, EV={ev}\n")
        self.output(self.service.status() + "\n")
        # regular_txt = self.num_value.get().strip()
        # ev_txt = self.ev_value.get().strip()

        # if not regular_txt or not ev_txt:
        #     self.output("Please enter both Regular and EV spaces\n")
        #     return

        # if not regular_txt.isdigit() or not ev_txt.isdigit():
        #     self.output("Spaces must be numbers only\n")
        #     return

        # regular = int(regular_txt)
        # ev = int(ev_txt)

        # strategy = RegularParkingStrategy()
        # self.service = ParkingLot(regular, ev, strategy)

        # self.output(f"Lot created: Regular={regular}, EV={ev}\n")
        # self.output(self.service.status() + "\n")

    def park_car(self):
        if not self.service:
            self.output("Create parking lot first\n")
            return

        vehicle = VehicleFactory.create(
            self.ev_car_value.get(),
            self.motor_value.get(),
            self.reg_value.get(),
            self.make_value.get(),
            self.model_value.get(),
            self.color_value.get()
        )

        

        slot = self.service.park_vehicle(vehicle)

        if slot == -1:
            self.output("Parking Full\n")
        else:
            self.output(f"Allocated slot number: {slot}\n")
        self.output(self.service.status() + "\n")

    # def remove_car(self):
    #     is_ev = self.ev_car_value.get()
    #     self.service.remove_vehicle(
    #     int(self.slot_value.get()),
    #     is_ev
    # )

    # def remove_car(self):
    #     slot_id = int(self.slot_value.get())
    #     is_ev = self.ev_car_value.get()   # checkbox
    #     self.service.remove_vehicle(slot_id, is_ev)
    #     self.output(f"Slot {slot_id} is now free\n")


        # self.service.remove_vehicle(int(self.slot_value.get()))
        # self.output(f"Slot {self.slot_value.get()} is free\n")


    def remove_car(self):

        if not self.service:
            self.output("Create parking lot first\n")
            return

        value = self.slot_value.get().strip()

        if not value:
            self.output("Please enter a slot number first\n")
            return

        if not value.isdigit():
            self.output("Slot number must be numeric\n")
            return

        slot_id = int(value)

        removed = self.service.remove_vehicle(slot_id)

        if not removed:
            self.output("Invalid slot number\n")
        else:
         self.output(f"Slot {slot_id} freed\n")

        self.output(self.service.status() + "\n")


    def search_model(self):
        model = self.model_value.get()

        vehicles = self.service.get_by_model(model)

        for slot, v in vehicles:
            self.output(
            f"{slot}\t{v.reg_no}\t{v.color}\t{v.make}\t{v.model}\n"
        )
    
    def search_by_registration(self):
        if not self.service:
            self.output("Create parking lot first\n")
            return
        reg = self.search_reg_value.get().strip()
        if not reg:
            self.output("Please enter a registration number\n")
            return
        
        result = self.service.get_by_registration(reg)
        if not result:
            self.output(f"No car found with registration {reg}\n")
            return
        
        slot, v = result
        self.output(
            f"""
SEARCH RESULT
-------------
Slot ID : {slot}
Reg No  : {v.regnum}
Make    : {v.make}
Model   : {v.model}
Color   : {v.color}
Type    : {"EV" if v.is_ev else "Regular"}
-------------
"""
    )


    # OUTPUT
    def output(self, text):
        self.tfield.insert(tk.END, text)

    def run(self):
        self.root.mainloop()

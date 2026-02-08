from strategies.regular_parking_strategy import RegularParkingStrategy
from domain.parking_lot import ParkingLot
from services.parking_service import ParkingService
from ui.tkinter_adapter import TkinterAdapter


def main():
    strategy = RegularParkingStrategy()

    parking_lot = ParkingLot(
        regular_capacity=20,
        ev_capacity=5,
        strategy=strategy
    )

    ui = TkinterAdapter(parking_lot)
    ui.run()

if __name__ == "__main__":
    main()
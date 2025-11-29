# File: run_carpark.py
from smartpark.CarparkManager import CarparkManager
import time

def main():
    manager = CarparkManager()

    print(f"Carpark {manager.location} has {manager.available_spaces} spaces available.")

    # simulate a few cars
    manager.incoming_car("ABC123")
    manager.incoming_car("XYZ789")

    print(f"Spaces after 2 cars entered: {manager.available_spaces}")

    manager.outgoing_car("ABC123")

    print(f"Spaces after 1 car left: {manager.available_spaces}")

    manager.temperature_reading(22.5)
    print(f"Current temperature: {manager.temperature}°C")

if __name__ == "__main__":
    main()

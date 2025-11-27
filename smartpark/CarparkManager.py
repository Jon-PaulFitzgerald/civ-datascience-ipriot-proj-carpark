# File: smartpark/CarparkManager.py
import time
from config_parser import parse_config
from interfaces import CarparkSensorListener, CarparkDataProvider

class Car:
    def __init__(self, plate):
        self.license_plate = plate
        self.entry_time = None
        self.exit_time = None

class CarparkManager(CarparkSensorListener, CarparkDataProvider):
    CONFIG_FILE = "samples_and_snippets/config.json"

    def __init__(self):
        self.config = parse_config(self.CONFIG_FILE)
        # normalize keys for test compatibility
        self.total_spaces = self.config.get("total-spaces", 0)
        self.location = self.config.get("location", "Unknown")
        self.cars = {}  # license_plate -> Car
        self._temperature = None
        self.log_file = "carpark.log"

    # ---------- DataProvider properties ----------
    @property
    def available_spaces(self):
        return self.total_spaces - len(self.cars)

    @property
    def temperature(self):
        return self._temperature

    @property
    def current_time(self):
        return time.localtime()

    # ---------- SensorListener methods ----------
    def incoming_car(self, license_plate):
        car = Car(license_plate)
        car.entry_time = time.time()
        self.cars[license_plate] = car
        self._log(f"Car entered: {license_plate}")

    def outgoing_car(self, license_plate):
        car = self.cars.pop(license_plate, None)
        if car:
            car.exit_time = time.time()
            self._log(f"Car exited: {license_plate}")

    def temperature_reading(self, reading):
        self._temperature = reading
        self._log(f"Temperature reading: {reading}")

    # ---------- Logging ----------
    def _log(self, message):
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        with open(self.log_file, "a") as f:
            f.write(f"[{ts}] {message}\n")

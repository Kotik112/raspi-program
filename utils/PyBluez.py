# Inte fått denna python klass att fungera. Får errors när jag försöker köra den.

import bluetooth

class BluetoothScanner:
    def init(self, target_mac_address):
        self.target_mac_address = target_mac_address

    def scan_for_devices(self):
        nearby_devices = bluetooth.discover_devices()
        for bdaddr in nearby_devices:
            if bdaddr == self.target_mac_address:
                print("Target device found!")
                # do something
            else:
                print("Target device not found.")
                # do something else

if __name__ == "__main__":
    scanner = BluetoothScanner("88:29:9C:36:73:54")
    scanner.scan_for_devices()
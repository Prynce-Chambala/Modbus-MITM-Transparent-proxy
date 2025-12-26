class PLC:
    def __init__(self):
        self.IP_address = "192.168.254.5"
        self.Modbus = None
        self.Connected = False
        self.Client = None

    def Connect(self):
        self.Client = ModbusTcpClient(self.IP_address)
        self.Connected = self.Client.connect() #Connect to REAL PLC
        if self.Connected:
            self.Display()

    def Display(self):
        print("[*] CONNECTED TO PLC...")
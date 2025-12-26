class TransparentModbusProxy:
    def __init__(self):
        self.PLC = None #Instance PLC
        self.Manipu = None
        self.server: ModbusTcpServer = None
        self.context = None
        self.framer = None
        self.identity = None
        self.address = None
        self.request_tracer = None
        self.response_manipulator = None
        self.fc_counter = 0
        self.update_Temp = 0
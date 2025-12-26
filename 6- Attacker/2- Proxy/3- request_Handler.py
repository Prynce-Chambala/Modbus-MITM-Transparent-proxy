        # ------------------------  ONLY READ REQUESTS --------------------------------#     
    def server_request_tracer(self,request,*_addr): # *_addr = All Server Requests pass this filter no matter the network before being handled
        self.last_request = request
        print(f"---> Forwarding REQUEST to PLC: {self.last_request}")
        if request.function_code == 3: # 0x03 -> Read holding registers | mapping request.function_code from ModbusTcpServer
            self.plc_response = self.PLC.Client.read_holding_registers(            
                request.address,    # -> Start address | mapping request.address from ModbusTcpServer
                request.count,        # -> Quantity | mapping requegetattr(request, "unit_id", 1)st.count from ModbusTcpServer
                getattr(request,"unit_id", 1)
            )
            return self.plc_response
   def server_response_manipulator(self,response): # Manipulate responses. All server responses passes this filter before being sent
        ## The filter returns: - response, either original or modified; - skip_encoding, signals whether or not to encode the response
        # ------------------------  READ RESPONSE --------------------------------#    
        if response.function_code == 3: # 0x03 -> Read holding registers | mapping request.function_code from ModbusTcpServer
            last_response = response.registers             # All register value
            self.update_Temp = last_response[1] # ONLY current temperature value
            print(f"[*]=> Current temperature: {self.update_Temp}")
        return response, False # --> False: Pymodbus encode itself

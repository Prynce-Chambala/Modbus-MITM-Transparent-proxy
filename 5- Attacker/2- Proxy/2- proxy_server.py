    async def server_configuration(self):
              """Prepare server."""
              pymodbus_apply_logging_config(logging.DEBUG)              
              store = ModbusSlaveContext(
                  hr=ModbusSequentialDataBlock(0x00,[0]*100) # Holding Registers
              )
              self.context= ModbusServerContext(slaves=store, single=True)             
              self.server = ModbusTcpServer( # Instantiate the Modbus TCP server
                context=self.context, # Modbus context
                framer=Framer.SOCKET, # TCP socket framer
                identity=None, # Server identity (unused)
                address=("0.0.0.0",502), # Bind address and port -> Listening on ALL PORT
                request_tracer=self.server_request_tracer, # Request hook
                response_manipulator=self.server_response_manipulator, # Response hook
                )

    async def run(self):
                """Attach Run server."""
                await self.server.serve_forever()
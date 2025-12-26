🔷 Overview :

This project demonstrates a Transparent Modbus TCP Man-in-the-Middle (MITM) proxy designed for industrial Cybersecurity research and training purposes.

The objective is to show how a transparent proxy positioned between a SCADA system and a PLC can Observe, Forward, and optionally manipulate Modbus responses, without disrupting the normal control process.

⚠️ This project focuses on visibility and architectural understanding, not on providing weaponized attack tooling.

🔷 Industrial Context: PLC ↔ SCADA Communication

In industrial environments:

  - PLCs interact directly with sensors and actuators via field I/O
  - SCADA systems supervise the process by:
	* Reading process values (temperature, pressure, level…)
	* Writing control values (setpoints, commands, modes)
        * Communication between SCADA and PLC commonly relies on Modbus TCP, especially in legacy or mixed OT environments.

🔷 Modbus TCP – Protocol Overview :

Modbus TCP is a request/response protocol operating over TCP/IP (port 502).

Common function codes include:

Function Code   	Description

FC 1 / 2	        Read Coils / Discrete Inputs

FC 3	                Read Holding Registers

FC 4	                Read Input Registers

FC 5 / 6	        Write Single Coil / Register

FC 15 / 16	        Write Multiple Coils / Registers


In typical SCADA operation:

  - Reads are continuous (monitoring)
  - Writes are occasional (operator actions, automation logic)

🔷 Normal PLC–SCADA Communication Flow :

          SCADA  ── (Modbus TCP) ──>  PLC
          SCADA  <─ (Modbus TCP) ───  PLC

The SCADA:

  - Sends read/write requests
  - Receives real-time process values from the PLC

The PLC:

  - Executes control logic
  - Responds with raw register values

🔷 Threat Model: MITM on Modbus TCP

Because Modbus TCP:

  - Has no authentication 
  - Has no encryption
  - Has no integrity checks

An attacker with network access can position themselves as a Man-in-the-Middle.


This project simulates that scenario using:

  - Network-level redirection (DNAT)
  - An application-level Modbus proxy

🔷 Transparent Proxy Architecture

          SCADA ──> [ DNAT ] ──> Modbus Proxy ──> PLC
          SCADA <── [ DNAT ] <── Modbus Proxy <── PLC


Key properties:

  - The proxy is transparent to both SCADA and PLC
  - Original requests are forwarded unchanged

Responses can be:

  - Observed
  - Logged
  - Optionally modified before reaching the SCADA


The proxy is implemented using Pymodbus, acting as an intermediary Modbus TCP server/client.

🔷 Attack Principle (High-Level)

This project demonstrates response-level manipulation, where:

  - The PLC continues to operate normally
  - The SCADA receives altered process values
  - The physical process remains unaffected

This highlights a critical OT risk:

  - Loss of operator visibility without impacting the control logic

⚠️ The detailed alteration logic is intentionally omitted.



🔷 Project Scope & Limitations:

  - This project is a lab-scale simulation
  - It does not attempt to bypass detection systems
  - It does not include persistence mechanisms
  - It does not exploit PLC firmware or logic

The focus is on:

  - Protocol behavior
  - Architectural weaknesses
  - Defensive awareness
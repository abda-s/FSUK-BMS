<!-- Converted from TCAN1462-Q1 Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](TCAN1462-Q1%20Datasheet_files/img_001.png)

INSTRUMENTS

## TCAN1462-Q1 Automotive Fault-Protected CAN FD Transceiver with Signal Improvement Capability (SIC) and Standby Mode

## 1 Features

- AEC Q100 (Grade 1): Qualified for automotive applications
- [Functional Safety-Capable](https://www.ti.com/technologies/functional-safety/overview.html#commitment)
- [Documentation available to aid functional safety system design](https://www.ti.com/product/TCAN1462-Q1#tech-docs)
- Meets the requirements of ISO 11898-2:2016 and CiA 601-4 standards
- Classical CAN and CAN FD up to 8Mbps
- Actively improves the bus signal by reducing ringing effects in complex topologies
- Backward compatible for use in classic CAN networks
- VIO level shifting supports: 1.7V to 5.5V
- Operating Modes
- Normal mode
- Low-power standby mode supporting remote wake-up request
- Passive behavior when unpowered
- Bus and logic terminals are high impedance (no load to operating bus or application)
- Hot plug capable: power up or down glitch free operation on bus and RXD output
- Defined device behavior with floating logic pins and in undervoltage supply conditions
- Protection features
- IEC ESD protection on bus pins
- ±58 V CAN bus fault tolerant
- Undervoltage protection on VCC and VIO (V variants only) supply terminals
- TXD dominant state timeout (TXD DTO)
- Thermal shutdown protection (TSD)
- Available in SOIC (8), small footprint SOT-23 (8) and leadless 3mm x 3mm VSON (8) package with wettable flanks for improved automated optical inspection (AOI) capability

## 2 Applications

- [Automotive gateway](http://www.ti.com/solution/automotive-gateway)
- [Advanced driver assistance system (ADAS)](http://www.ti.com/applications/automotive/adas/overview.html)
- [Body electronics and lighting](http://www.ti.com/applications/automotive/body-lighting/overview.html)
- [Hybrid, electric &amp; powertrain systems](http://www.ti.com/applications/automotive/hev-ev-powertrain/overview.html)
- [Automotive infotainment &amp; cluster](http://www.ti.com/applications/automotive/infotainment-cluster/overview.html)

## 3 Description

The TCAN1462-Q1 is a high speed Controller Area Network (CAN) transceiver that meet the physical layer requirements of the ISO 11898-2:2016 high speed CAN specification and the CiA 601-4 Signal Improvement Capability (SIC) specification. The devices reduce signal ringing at dominant-torecessive edge and enable higher throughput in complex network topologies. Signal improvement capability allows the applications to extract real benefit of CAN FD (flexible data rate) by operating at 2Mbps, or operating at 5Mbps or higher in large networks with multiple unterminated stubs.

The device meets the timing specifications mandated by CiA 601-4; thus, have much tighter bit timing symmetry compared to a regular CAN FD transceivers. This provides larger timing window to sample the correct bit and enables error-free communication in large complex star networks where ringing and bit distortion are inherent.

These devices are pin-compatible to 8-pin CAN FD transceivers, such as TCAN1044A-Q1 or TCAN1042Q1.

The TCAN1462-Q1 with suffix 'V' includes internal logic level translation via the VIO logic supply terminal to allow for interfacing directly to 1.8V, 2.5V, or 3.3V controllers. The transceivers support low power standby mode which allows remote wake-up via CAN bus compliant with ISO 11898-2:2016 defined wakeup pattern (WUP). The device family also includes many protection features such as undervoltage detection, thermal shutdown (TSD), driver dominant timeout (TXD DTO), and ±58V bus fault protection.

## Package Information

| PART NUMBER | PACKAGE (1) | PACKAGE SIZE (2) |
| - | - | - |
| TCAN1462-Q1 | SOT-23 (DDF) | 2.9mm x 2.8mm |
| TCAN1462-Q1 | VSON (DRB) | 3mm x 3 mm |
| TCAN1462-Q1 | SOIC (D) | 4.9mm x 6mm |

- (1) For all available packages, see Section 12.
- (2) The package size (length × width) is a nominal value and includes pins, where applicable.

![Image](TCAN1462-Q1%20Datasheet_files/img_002.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_003.png)

Simplified Block Diagram

![Image](TCAN1462-Q1%20Datasheet_files/img_004.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_005.png)

[www.ti.com](https://www.ti.com/)

## Table of Contents

| 1 Features............................................................................1 | 1 Features............................................................................1 | 8.2 Functional Block Diagram.........................................18 | 8.2 Functional Block Diagram.........................................18 |
| - | - | - | - |
| 2 Applications.....................................................................1 | 2 Applications.....................................................................1 | 8.3 Feature Description...................................................19 | 8.3 Feature Description...................................................19 |
| 3 Description.......................................................................1 | 3 Description.......................................................................1 | 8.4 Device Functional Modes..........................................23 | 8.4 Device Functional Modes..........................................23 |
| 4 Device Comparison Table...............................................3 | 4 Device Comparison Table...............................................3 | 9 Application and Implementation..................................25 | 9 Application and Implementation..................................25 |
| 5 Pin Configurations and Functions.................................4 | 5 Pin Configurations and Functions.................................4 | 9.1 Application Information............................................. 25 | 9.1 Application Information............................................. 25 |
| 6 Specifications.................................................................. 5 | 6 Specifications.................................................................. 5 | 9.2 Typical Application.................................................... 25 | 9.2 Typical Application.................................................... 25 |
| 6.1 Absolute Maximum Ratings........................................ 5 | 6.1 Absolute Maximum Ratings........................................ 5 | 9.3 System Examples..................................................... 28 | 9.3 System Examples..................................................... 28 |
| 6.2 ESD Ratings .............................................................. 5 | 6.2 ESD Ratings .............................................................. 5 | 9.4 Power Supply Recommendations.............................28 | 9.4 Power Supply Recommendations.............................28 |
| 6.3 ESD Ratings, IEC Transients......................................5 | 6.3 ESD Ratings, IEC Transients......................................5 | 9.5 Layout....................................................................... 29 | 9.5 Layout....................................................................... 29 |
| 6.4 Recommended Operating Conditions.........................6 | 6.4 Recommended Operating Conditions.........................6 | 10 Device and Documentation Support..........................30 | 10 Device and Documentation Support..........................30 |
| 6.5 Thermal Characteristics..............................................6 | 6.5 Thermal Characteristics..............................................6 | 10.1 Receiving Notification of Documentation Updates..30 | 10.1 Receiving Notification of Documentation Updates..30 |
| 6.6 Supply Characteristics................................................ 6 | 6.6 Supply Characteristics................................................ 6 | 10.2 Support Resources................................................. 30 | 10.2 Support Resources................................................. 30 |
| 6.7 Dissipation Ratings..................................................... 7 | 6.7 Dissipation Ratings..................................................... 7 | 10.3 Trademarks.............................................................30 | 10.3 Trademarks.............................................................30 |
| 6.8 Electrical Characteristics.............................................7 | 6.8 Electrical Characteristics.............................................7 | 10.4 Electrostatic Discharge Caution..............................30 | 10.4 Electrostatic Discharge Caution..............................30 |
| 6.9 Switching Characteristics............................................9 | 6.9 Switching Characteristics............................................9 | 10.5 Glossary..................................................................30 | 10.5 Glossary..................................................................30 |
| 6.10 Typical Characteristics............................................12 | 6.10 Typical Characteristics............................................12 | 11 Revision History.......................................................... 30 | 11 Revision History.......................................................... 30 |
| 7 Parameter Measurement Information..........................13 | 7 Parameter Measurement Information..........................13 | 12 Mechanical, Packaging, and Orderable | 12 Mechanical, Packaging, and Orderable |
| 8 Detailed Description......................................................16 | 8 Detailed Description......................................................16 | Information.................................................................... 30 | Information.................................................................... 30 |
| 8.1 Overview...................................................................16 4 Device Comparison Table | 8.1 Overview...................................................................16 4 Device Comparison Table | 8.1 Overview...................................................................16 4 Device Comparison Table | 8.1 Overview...................................................................16 4 Device Comparison Table |
| Device Number | Bus Fault Protection | Low voltage I/O Logic Support on Pin 5 | Pin 8 Mode Selection |
| TCAN1462-Q1 | ± 58 V | No | Low Power Standby Mode with Remote Wake |
| TCAN1462V-Q1 | ± 58 V | Yes |  |

![Image](TCAN1462-Q1%20Datasheet_files/img_006.png)

## 5 Pin Configurations and Functions

Figure 5-1. SOIC (D) and SOT-23 (DDF) Package, 8 Pin (Top View)

![Image](TCAN1462-Q1%20Datasheet_files/img_007.png)

Figure 5-2. VSON (DRB) Package, 8 Pin (Top View)

![Image](TCAN1462-Q1%20Datasheet_files/img_008.png)

Table 5-1. Pin Functions

| PINS - NAME | PINS - NO. | TYPE | DESCRIPTION |
| - | - | - | - |
| TXD | 1 | Digital Input | CAN transmit data input, integrated pull-up |
| GND | 2 | GND | Ground connection |
| VCC | 3 | Supply | 5 V supply voltage |
| RXD | 4 | Digital Output | CAN receive data output, tristate when powered off |
| VIO | 5 | Supply | Logic supply voltage |
| NC | 5 | -- | No Connect (not internally connected); Devices without VIO |
| CANL | 6 | Bus IO | Low-level CAN bus input/output line |
| CANH | 7 | Bus IO | High-level CAN bus input/output line |
| STB | 8 | Digital Input | Standby mode control input, integrated pull-up |
| Thermal Pad (VSON only) |  | - | Electrically connected to GND, connect the thermal pad to the printed circuit board (PCB) ground plane for thermal relief |

![Image](TCAN1462-Q1%20Datasheet_files/img_009.png)

[www.ti.com](https://www.ti.com/)

## 6 Specifications

## 6.1 Absolute Maximum Ratings

(1) (2)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| VCC | Supply voltage | -0.3 | 6 | V |
| VIO | Supply voltage IO level shifter (Devices with the "V" suffix) | -0.3 | 6 | V |
| VBUS | CAN bus IO voltage range on CANH and CANL | -58 | 58 | V |
| VDIFF | Max differential voltage between CANH and CANL VDIFF = (CANH - CANL) | -45 | 45 | V |
| VLogic_Input | Logic pin input voltage (TXD, STB) | -0.3 | 6 | V |
| VRXD | Logic output voltage range (RXD) | -0.3 | 6 | V |
| IO(RXD) | RXD output current | -8 | 8 | mA |
| TJ | Junction temperature | -40 | 165 | °C |
| TSTG | Storage temperature | -65 | 165 | °C |

(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.

- (2) All voltage values, except differential I/O bus voltages, are with respect to ground terminal.

## 6.2 ESD Ratings

|  |  |  |  | VALUE | UNIT |
| - | - | - | - | - | - |
| VESD |  | Human-body model (HBM), per AEC Q100-002 (1) | HBM classification level 3A for all pins | ±4000 | V |
| VESD | Electrostatic discharge |  | HBM classification level 3B for global pins CANH and CANL with respect to GND | ±10000 | V |
| VESD |  | Charged-device model (CDM), per AEC Q100-011 CDM classification level C5 for all pins |  | ±750 | V |

(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.

## 6.3 ESD Ratings, IEC Transients

|  |  |  |  | VALUE | UNIT |
| - | - | - | - | - | - |
| VESD | System level electrostatic discharge | CAN bus terminals (CANH, CANL) to GND | SAE J2962-2 per ISO 10605 Powered contact discharge | ±8000 | V |
| VESD | System level electrostatic discharge | CAN bus terminals (CANH, CANL) to GND | SAE J2962-2 per ISO 10605 Powered air discharge | ±15000 | V |
| VESD | System level electrostatic discharge | CAN bus terminals (CANH, CANL) to GND | IEC 62228-3 per ISO 10605 | ±8000 | V |
| VTran | ISO 7637-2 Transient immunity (1) | CAN bus terminals (CANH, CANL) to GND | Pulse 1 | -100 | V |
| VTran | ISO 7637-2 Transient immunity (1) | CAN bus terminals (CANH, CANL) to GND | Pulse 2a | 75 | V |
| VTran | ISO 7637-2 Transient immunity (1) | CAN bus terminals (CANH, CANL) to GND | Pulse 3a | -150 | V |
| VTran | ISO 7637-2 Transient immunity (1) | CAN bus terminals (CANH, CANL) to GND | Pulse 3b | 100 | V |
| VTran | Direct capacitor coupling, SAE J2962-2 per ISO 7637-3 (2) | CAN bus terminals (CANH, CANL) to GND | DCC slow transient pulse | ±30 | V |

- (1) Tested according to IEC 62228-3:2019 CAN Transceivers, Section 6.3; standard pulses parameters defined in ISO 7637-2 (2011)

(2) Tested according to SAE J2962-2

![Image](TCAN1462-Q1%20Datasheet_files/img_003.png)

## 6.4 Recommended Operating Conditions

|  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - |
| VCC | Supply voltage | 4.5 | 5 | 5.5 | V |
| VIO | Supply voltage for IO level shifter (Devices with VIO ) | 1.7 |  | 5.5 | V |
| IOH(RXD) | RXD terminal high-level output current | -1.5 |  |  | mA |
| IOL(RXD) | RXD terminal low-level output current |  |  | 1.5 | mA |
| TJ | Junction temperature | -40 |  | 150 | °C |

## 6.5 Thermal Characteristics

|  | (1) - THERMAL METRIC | TCAN1462(V)-Q1 - D (SOIC) | TCAN1462(V)-Q1 - DDF (SOT) | TCAN1462(V)-Q1 - DRB (VSON) | UNIT |
| - | - | - | - | - | - |
| RΘJA | Junction-to-ambient thermal resistance | 120 | 115.3 | 52.8 | ℃/W |
| RΘJC(top) | Junction-to-case (top) thermal resistance | 57.8 | 56.2 | 58.9 | ℃/W |
| RΘJB | Junction-to-board thermal resistance | 64.2 | 38 | 25.2 | ℃/W |
| ΨJT | Junction-to-top characterization parameter | 13.1 | 1.8 | 1.8 | ℃/W |
| ΨJB | Junction-to-board characterization parameter | 63.3 | 37.7 | 25.2 | ℃/W |
| RΘJC(bot) | Junction-to-case (bottom) thermal resistance | - | - | 9.3 | ℃/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

## 6.6 Supply Characteristics

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V (for devices with VIO), Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER |  | TEST CONDITIONS | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - | - |
| ICC | Supply current normal mode | Dominant | TXD = 0 V, STB = 0 V RL = 60 Ω, CL = open See Figure 7-1 |  | 45 | 70 | mA |
| ICC |  | Dominant | TXD = 0 V, STB = 0 V RL = 50 Ω, CL = open See Figure 7-1 |  | 49 | 80 | mA |
| ICC |  | Recessive | TXD = VIO, STB = 0 V RL = 50 Ω, CL = open See Figure 7-1 |  | 4.5 | 8 | mA |
| ICC |  | Dominant with bus fault | TXD = 0 V, STB = 0 V CANH = CANL = ±25 V RL = open, CL = open See Figure 7-1 |  |  | 130 | mA |
| ICC |  |  | TXD = STB = VIO , RL = 50 Ω, CL = open, Tj <= 85 °C, See Figure 7-1 |  |  | 0.6 | µA |
| ICC | Supply current standby mode (devices with VIO ) | Supply current standby mode (devices with VIO ) | TXD = STB = VIO , RL = 50 Ω, CL = open, Tj <= 125 °C, See Figure 7-1 | 0.2 |  | 2 | µA |
| ICC |  |  | TXD = STB = VIO , RL = 50 Ω, CL = open, Tj <= 150 °C, See Figure 7-1 |  |  | 5 | µA |
| ICC |  |  | TXD = STB = VCC , RL = 50 Ω, CL = open, Tj <= 85 °C, See Figure 7-1 |  |  | 14 |  |
| ICC | Supply current standby mode (devices without VIO ) | Supply current standby mode (devices without VIO ) | TXD = STB = VCC , RL = 50 Ω, CL = open, Tj <= 125 °C, See Figure 7-1 |  |  | 16 | µA |
| ICC |  |  | TXD = STB = VCC , RL = 50 Ω, CL = open, Tj <= 150 °C, See Figure 7-1 |  |  | 21 | µA |

![Image](TCAN1462-Q1%20Datasheet_files/img_010.png)

## 6.6 Supply Characteristics (continued)

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V (for devices with VIO), Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER | PARAMETER | TEST CONDITIONS | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - | - |
| IIO Devices with VIO IO supply mode |  | current normal Dominant | TXD = 0 V, STB = 0 V RL = 60 Ω, CL = open RXD floating |  | 125 | 300 | µA |
| IIO Devices with VIO IO supply mode |  | Recessive | TXD = VIO, STB = 0 V RL = 60 Ω, CL = open RXD floating |  | 25 | 48 | µA |
|  |  |  | TXD = VIO, STB = VIO RL = 60 Ω, CL = open RXD floating, Tj <= 85 °C |  |  | 13.5 | µA |
|  | IO supply current standby mode | IO supply current standby mode | TXD = VIO, STB = VIO RL = 60 Ω, CL = open RXD floating, Tj <= 125 °C |  | 8.5 | 15 | µA |
|  |  |  | TXD = VIO, STB = VIO RL = 60 Ω, CL = open RXD floating, Tj <= 150 °C |  |  | 16 | µA |
| UVCC(R) | Undervoltage detection VCC rising | Undervoltage detection VCC rising | Ramp up |  | 4.2 | 4.4 | V |
| UVCC(F) | Undervoltage detection on VCC falling | Undervoltage detection on VCC falling | Ramp down | 3.5 | 4 |  | V |
| UVIO(R) | Undervoltage detection VIO rising (Devices with VIO) | Undervoltage detection VIO rising (Devices with VIO) | Ramp up |  | 1.6 | 1.65 | V |
| UVIO(F) | Undervoltage detection on VIO falling (Devices with VIO) | Undervoltage detection on VIO falling (Devices with VIO) | Ramp down | 1.4 | 1.5 |  | V |

## 6.7 Dissipation Ratings

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN TYP | MAX | UNIT |
| - | - | - | - | - | - |
| PD | Average power dissipation Normal mode | VCC = 5 V, VIO = 3.3 V, TJ = 27°C, RL = 60Ω, CL_RXD = 15 pF TXD input = 250 kHz 50% duty cycle square wave | 60 |  | mW |
| PD | Average power dissipation Normal mode | VCC = 5.5 V, VIO = 5.5 V, TJ = 150°C, RL = 50Ω, CL_RXD = 15 pF TXD input = 2.5 MHz 50% duty cycle square wave | 120 |  | mW |
| TTSD | Thermal shutdown temperature |  | 192 |  | °C |
| TTSD_HYS | Thermal shutdown hysteresis |  | 10 |  | °C |

## 6.8 Electrical Characteristics

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V, Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER | PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - | - |
| Driver Electrical Characteristics | Driver Electrical Characteristics | Driver Electrical Characteristics | Driver Electrical Characteristics | Driver Electrical Characteristics | Driver Electrical Characteristics | Driver Electrical Characteristics | Driver Electrical Characteristics |
| VO(DOM) | Dominant output voltage normal mode | CANH | TXD = 0 V, STB = 0 V 50 Ω ≤ RL ≤ 65 Ω, CL = open, See Figure 7-2 and Figure 8-5 | 2.75 |  | 4.5 | V |
| VO(DOM) | Dominant output voltage normal mode | CANL | TXD = 0 V, STB = 0 V 50 Ω ≤ RL ≤ 65 Ω, CL = open, See Figure 7-2 and Figure 8-5 | 0.5 |  | 2.25 | V |
| VO(REC) | Recessive output voltage normal mode | CANH and CANL | TXD = VIO, STB = 0 V RL = open (no load), CL = open, See Figure 7-2 and Figure 8-5 | 2 | 0.5 VCC | 3 | V |
| VSYM | Driver symmetry (VO(CANH) + VO(CANL))/VCC |  | TXD = 250 kHz, 1 MHz, 2.5 MHz, STB = 0 V RL = 60, CSPLIT = 4.7 nF, CL = open, See Figure 7-2 and Figure 9-2 | 0.9 |  | 1.1 | V/V |
| VSYM_DC | DC output symmetry (VCC - VO(CANH) - VO(CANL)) |  | STB = 0 V RL = 60 Ω, CL = open, See Figure 7-2 and Figure 8-5 | -400 |  | 400 | mV |
| RID(DOM) | Differential input resistance in dominant phase | Differential input resistance in dominant phase | TXD= 0 V, STB = 0 V, See Figure 8-2 | 40 | 40 | 40 | Ω |

![Image](TCAN1462-Q1%20Datasheet_files/img_003.png)

## 6.8 Electrical Characteristics (continued)

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V, Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER |  |  | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - | - |
| RID(ACTIVE_RE C) | Differential input resistance in active recessive drive phase |  | Duration from TXD low-to-high edge to elapse of active recessive drive period (tSIC_TX_base), See Figure 8-2 |  | 100 |  | Ω |
| VOD(DOM) | Differential output voltage normal mode Dominant | CANH - CANL | TXD = 0 V, STB = 0 V 50 Ω ≤ RL ≤ 65 Ω, CL = open, See Figure 7-2 and Figure 8-5 | 1.5 |  | 3 | V |
|  |  |  | TXD = 0 V, STB = 0 V 45 Ω ≤ RL ≤ 70 Ω, CL = open, See Figure 7-2 and Figure 8-5 | 1.4 |  | 3.3 | V |
|  |  |  | TXD = 0 V, STB = 0 V RL = 2240 Ω, CL = open, See Figure 7-2 and Figure 8-5 | 1.5 |  | 5 | V |
| VOD(REC) | Differential output voltage normal mode Recessive | CANH - CANL | TXD = VIO, STB = 0 V RL = 60 Ω, CL = open, See Figure 7-2 and Figure 8-5 | -120 |  | 12 | mV |
|  |  |  | TXD = VIO, STB = 0 V RL = open, CL = open, See Figure 7-2 and Figure 8-5 | -50 |  | 50 | mV |
| VO(STB) | Bus output voltage standby mode | CANH | TXD = STB = VIO | -0.1 |  | 0.1 | V |
|  |  | CANL | RL = open , CL = open, See Figure 7-2 and Figure 8-5 | -0.1 |  | 0.1 | V |
|  |  | CANH - CANL |  | -0.2 |  | 0.2 | V |
| IOS | Short-circuit bus output current, TXD is dominant or recessive or toggling, |  | V(CANH) = -15 V to 40 V, CANL = open, TXD = 0 V or VIO or 250 kHz, 2.5 MHz square wave, See Figure 7-7 and Figure 8-5 | -115 |  | 115 | mA |
|  |  | normal mode | V(CAN_L) = -15 V to 40 V, CANH = open, TXD = 0 V or VIO or 250 kHz, 2.5 MHz square wave, See Figure 7-7 and Figure 8-5 | -115 |  | 115 | mA |
| Receiver Electrical Characteristics |  |  |  |  |  |  |  |
| VIT Input threshold voltage | normal | mode | -12 V ≤ VCM ≤ 12 V, STB= 0 V, See Figure 7-3 and Table 8-6 | 500 |  | 900 | mV |
| VIT(STB) | Input threshold standby mode |  | -12 V ≤ VCM ≤ 12 V, STB= VIO , See Figure 7-3 and Table 8-6 | 400 |  | 1150 | mV |
| VDOM | Normal mode dominant state differential input voltage range |  | -12 V ≤ VCM ≤ 12 V, STB= 0 V, See Figure 7-3 and Table 8-6 | 0.9 |  | 9 | V |
| VREC | Normal mode recessive state differential input voltage range |  | -12 V ≤ VCM ≤ 12 V , STB= 0 V, See Figure 7-3 and Table 8-6 | -4 |  | 0.5 | V |
| VDOM(STB) | Standby mode dominant state differential input voltage range |  | STB = VIO, -12 V ≤ VCM ≤ 12 V, See Figure 7-3 and Table 8-6 | 1.15 |  | 9 | V |
| VREC(STB) | Standby mode recessive state differential input voltage range |  | STB = VIO, -12 V ≤ VCM ≤ 12 V, See Figure 7-3 and Table 8-6 | -4 |  | 0.4 | V |
| VHYS | Hysteresis voltage for input threshold normal mode |  | -12 V ≤ VCM ≤ 12 V, STB= 0 V, See Figure 7-3 and Table 8-6 |  | 100 |  | mV |
| VCM | Common mode range normal and standby modes |  | See Figure 7-3 and Table 8-6 | -12 |  | 12 | V |
| ILKG(IOFF) | Unpowered bus input leakage current |  | CANH = CANL = 5 V, VCC = VIO = GND |  |  | 5 | µA |
| CI | Input capacitance to ground (CANH or CANL) |  |  |  |  | 40 | pF |
| CID | Differential input capacitance |  | TXD = VIO |  |  | 20 | pF |
| RID | Differential input resistance |  | TXD = VIO, STB = 0 V -12 V ≤ VCM ≤ 12 V, | 40 |  | 90 | kΩ |
| RIN | Single ended input resistance (CANH or CANL) |  | Delta V/Delta I | 20 |  | 45 | kΩ |
| RIN(M) | Input resistance matching [1 - (RIN(CANH) / RIN(CANL))] × 100 % |  | V(CAN_H) = V(CAN_L) = 5 V | -1 |  | 1 | % |
| TXD Terminal (CAN Transmit Data Input) |  |  |  |  |  |  |  |
| VIH | High-level input voltage |  | Devices without VIO | 0.7 VCC |  |  | V |
| VIH | High-level input voltage |  | Devices with VIO | 0.7 VIO |  |  | V |

![Image](TCAN1462-Q1%20Datasheet_files/img_011.png)

## 6.8 Electrical Characteristics (continued)

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V, Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| VIL | Low-level input voltage | Devices without VIO |  |  | 0.3 VCC | V |
| VIL | Low-level input voltage | Devices with VIO |  |  | 0.3 VIO | V |
| IIH | High-level input leakage current | TXD = VCC = VIO = 5.5 V | -2.5 | 0 | 1 | µA |
| IIL | Low-level input leakage current | TXD = 0 V, VCC = VIO = 5.5 V | -200 | -100 | -20 | µA |
| ILKG(OFF) | Unpowered leakage current | TXD = 5.5 V, VCC = VIO = 0 V | -1 | 0 | 1 | µA |
| CI | Input capacitance | VIN = 0.4×sin(2×π×2×10 6 ×t)+2.5 V |  | 5 |  | pF |
| RXD Terminal (CAN Receive Data Output) | RXD Terminal (CAN Receive Data Output) | RXD Terminal (CAN Receive Data Output) | RXD Terminal (CAN Receive Data Output) | RXD Terminal (CAN Receive Data Output) | RXD Terminal (CAN Receive Data Output) | RXD Terminal (CAN Receive Data Output) |
| VOH | High-level output voltage | Devices without VIO IO = -1.5 mA, See Figure 7-3 | 0.8 VCC |  |  | V |
| VOH | High-level output voltage | IO = -1.5 mA, Devices with VIO See Figure 7-3 | 0.8 VIO |  |  | V |
| VOL | Low-level output voltage | Devices without VIO IO = 1.5 mA, See Figure 7-3 |  |  | 0.2 VCC | V |
| VOL | Low-level output voltage | Devices with VIO IO = 1.5 mA, Devices with VIO See Figure 7-3 |  |  | 0.2 VIO | V |
| ILKG(OFF) | Unpowered leakage current | RXD = 5.5 V, VCC = VIO = 0 V | -1 | 0 | 1 | µA |
| STB Terminal (Standby Mode Input) | STB Terminal (Standby Mode Input) | STB Terminal (Standby Mode Input) | STB Terminal (Standby Mode Input) | STB Terminal (Standby Mode Input) | STB Terminal (Standby Mode Input) | STB Terminal (Standby Mode Input) |
| VIH | High-level input voltage | Devices without VIO | 0.7 VCC |  |  | V |
| VIH | High-level input voltage | Devices with VIO | 0.7 VIO |  |  | V |
| VIL | Low-level input voltage | Devices without VIO |  |  | 0.3 VCC | V |
| VIL | Low-level input voltage | Devices with VIO |  |  | 0.3 VIO | V |
| IIH | High-level input leakage current | VCC = VIO = STB = 5.5 V | -2 |  | 2 | µA |
| IIL | Low-level input leakage current | VCC = VIO = 5.5 V, STB = 0 V | -20 |  | -2 | µA |
| ILKG(OFF) | Unpowered leakage current | STB = 5.5V, VCC= VIO = 0 V | -1 | 0 | 1 | µA |

## 6.9 Switching Characteristics

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V, Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| Device Switching Characteristics | Device Switching Characteristics |  |  |  |  |  |
| tPROP(LOOP1) | Total loop delay, driver input (TXD) to receiver output (RXD), recessive to dominant | See Figure 7-4 , normal mode, VIO = 4.5 V to 5.5 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 95 | 145 | ns |  |
| tPROP(LOOP1) | Total loop delay, driver input (TXD) to receiver output (RXD), recessive to dominant | See Figure 7-4 , normal mode, VIO = 3 V to 3.6 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 100 | 155 |  | ns |
| tPROP(LOOP1) | Total loop delay, driver input (TXD) to receiver output (RXD), recessive to dominant | See Figure 7-4 , normal mode, VIO = 2.25 V to 2.75 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 105 |  | 170 | ns |
| tPROP(LOOP1) | Total loop delay, driver input (TXD) to receiver output (RXD), recessive to dominant | See Figure 7-4 , normal mode, VIO = 1.71 V to 1.89 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 120 |  | 190 | ns |

![Image](TCAN1462-Q1%20Datasheet_files/img_003.png)

## 6.9 Switching Characteristics (continued)

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V, Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| tPROP(LOOP2) | Total loop delay, driver input (TXD) to receiver output (RXD), dominant to recessive | See Figure 7-4 , normal mode, VIO = 4.5 V to 5.5 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF |  | 110 | 150 | ns |
| tPROP(LOOP2) |  | See Figure 7-4 , normal mode, VIO = 3 V to 3.6 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF |  | 115 | 160 | ns |
| tPROP(LOOP2) |  | See Figure 7-4 , normal mode, VIO = 2.25 V to 2.75 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF |  | 120 | 175 | ns |
| tPROP(LOOP2) |  | See Figure 7-4 , normal mode, VIO = 1.71 V to 1.89 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF |  | 135 | 190 | ns |
| tMODE | Mode change time, from normal to standby or from standby to normal | See Figure 7-5 |  |  | 30 | µs |
| tWK_FILTER | Filter time for a valid wake-up pattern | See Figure 8-7 | 0.5 |  | 1.8 | µs |
| tWK_TIMEOUT | Bus wake-up timeout value | See Figure 8-7 | 0.8 |  | 6 | ms |
| Tstartup | Time duration after VCC or VIO hass cleared rising undervoltage threshold, and device can resume normal operation |  |  |  | 1.5 | ms |
| Tfilter(STB) | Filter on STB pin to filter out any glitches |  | 0.5 | 1 | 2 | µs |
| Driver Switching Characteristics | Driver Switching Characteristics | Driver Switching Characteristics | Driver Switching Characteristics | Driver Switching Characteristics | Driver Switching Characteristics | Driver Switching Characteristics |
| tprop(TxD-busrec) | Propagation delay time, low-to-high TXD edge to driver recessive (dominant to recessive) | See Figure 7-2 , STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 4.5 V to 5.5 V |  | 50 | 70 | ns |
| tprop(TxD-busrec) | Propagation delay time, low-to-high TXD edge to driver recessive (dominant to recessive) | See Figure 7-2 STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 3 V to 3.6 V |  | 50 | 70 | ns |
| tprop(TxD-busrec) | Propagation delay time, low-to-high TXD edge to driver recessive (dominant to recessive) | See Figure 7-2 STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 2.25 V to 2.75 V |  | 55 | 75 | ns |
| tprop(TxD-busrec) |  | See Figure 7-2 STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 1.71 V to 1.89 V |  | 55 | 80 | ns |
| tprop(TxD-busdom) | Propagation delay time, high-to-low TXD edge to driver dominant (recessive to dominant) | See Figure 7-2 , STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 4.5 V to 5.5 V |  | 45 | 75 | ns |
| tprop(TxD-busdom) | Propagation delay time, high-to-low TXD edge to driver dominant (recessive to dominant) | See Figure 7-2 STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 3 V to 3.6 V |  | 50 | 75 | ns |
| tprop(TxD-busdom) | Propagation delay time, high-to-low TXD edge to driver dominant (recessive to dominant) | See Figure 7-2 STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 2.25 V to 2.75 V |  | 50 | 80 | ns |
| tprop(TxD-busdom) |  | See Figure 7-2 STB = 0 V, RL = 60 Ω, CL = 100 pF, VIO = 1.71 V to 1.89 V |  | 55 | 80 | ns |
| tsk(p) | Pulse skew (&#124;tprop(TxD-busrec) - tprop(TxD-busdom)&#124;) | STB = 0 V, RL = 60 Ω, CL = 100 pF, See Figure 7-2 |  | 3.5 | 10 | ns |
| tR | Differential output signal rise time | See Figure 7-2 , STB = 0 V, RL = 60 Ω, CL = 100 pF |  | 20 | 30 | ns |
| tF | Differential output signal fall time | See Figure 7-2 , STB = 0 V, RL = 60 Ω, CL = 100 pF |  | 30 | 40 | ns |
| tTXD_DTO | Dominant timeout | See Figure 7-6 , RL = 60 Ω, CL = 100 pF, STB = 0 V | 1.2 |  | 4.0 | ms |
| Receiver Switching Characteristics | Receiver Switching Characteristics | Receiver Switching Characteristics | Receiver Switching Characteristics | Receiver Switching Characteristics | Receiver Switching Characteristics | Receiver Switching Characteristics |
| tprop(busrec-RXD) | Propagation delay time, bus recessive input to RXD high output (dominant to recessive) | See Figure 7-3 , STB = 0 V, CL(RXD) = 15 pF, VIO = 4.5 V to 5.5 V |  | 60 | 85 | ns |
|  |  | See Figure 7-3 STB = 0 V, CL(RXD) = 15 pF, VIO = 3 V to 3.6 V |  | 65 | 95 | ns |
|  |  | See Figure 7-3 STB = 0 V, CL(RXD) = 15 pF, VIO = 2.25 V to 2.75 V |  | 70 | 105 | ns |
|  |  | See Figure 7-3 STB = 0 V, CL(RXD) = 15 pF, VIO = 1.71 V to 1.89 V |  | 80 | 110 | ns |

![Image](TCAN1462-Q1%20Datasheet_files/img_011.png)

## 6.9 Switching Characteristics (continued)

parameters valid over recommended operating conditions with -40℃ ≤ TJ ≤ 150℃ (Typical values are at VCC = 5 V, VIO = 3.3 V, Device ambient maintained at 27℃ ) unless otherwise noted

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| tprop(busdom-RXD) | Propagation delay time, bus dominant input to RXD low output (recessive to dominant) | See Figure 7-3 , STB = 0 V, CL(RXD) = 15 pF, VIO = 4.5 V to 5.5 V |  | 50 | 75 | ns |
| tprop(busdom-RXD) |  | See Figure 7-3 STB = 0 V, CL(RXD) = 15 pF, VIO = 3 V to 3.6 V |  | 50 | 80 | ns |
| tprop(busdom-RXD) |  | See Figure 7-3 STB = 0 V, CL(RXD) = 15 pF, VIO = 2.25 V to 2.75 V |  | 55 | 90 | ns |
| tprop(busdom-RXD) |  | See Figure 7-3 STB = 0 V, CL(RXD) = 15 pF, VIO = 1.71 V to 1.89 V |  | 65 | 110 | ns |
| tR | RXD output signal rise time | See Figure 7-3 , STB = 0 V, CL(RXD) = 15 pF |  | 8 | 20 | ns |
| tF | RXD output signal fall time | See Figure 7-3 , STB = 0 V, CL(RXD) = 15 pF |  | 7 | 25 | ns |
| Signal Improvement Timing Characteristics | Signal Improvement Timing Characteristics | Signal Improvement Timing Characteristics | Signal Improvement Timing Characteristics | Signal Improvement Timing Characteristics | Signal Improvement Timing Characteristics | Signal Improvement Timing Characteristics |
| tSIC_TX_base | Signal improvement time TX-based | Time from rising edge of the TXD signal to the end of the signal improvement phase | 230 | 340 | 530 | ns |
| ΔtBit(Bus) | Transmitted bit width variation | TXD <= 5Mbps square wave, ΔtBit(Bus) = tBit(Bus) - tBit(TxD) STB = 0 V, RL = 60 Ω, CL = 100 pF, See Figure 7-4 | -10 |  | 10 | ns |
| ΔtBIT(RxD) | Received bit width variation | TXD <= 5Mbps square wave, ΔtBit(RxD) = tBit(RxD) - tBit(TxD) STB = 0 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF, See Figure 7-4 | -30 |  | 20 | ns |
| ΔtREC | Receiver timing symmetry | TXD <= 5Mbps square wave, ΔtREC = tBit(RxD) - tBit(Bus) STB = 0 V, CL(RXD) = 15 pF, See Figure 7-4 | -20 |  | 15 | ns |
| FD Timing Characteristics | FD Timing Characteristics | FD Timing Characteristics | FD Timing Characteristics | FD Timing Characteristics | FD Timing Characteristics | FD Timing Characteristics |
| tBIT(BUS) | Bit time on CAN bus output pins with tBIT(TXD) = 500 ns | See Figure 7-4 , STB = 0 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 490 |  | 510 | ns |
| tBIT(BUS) | Bit time on CAN bus output pins with tBIT(TXD) = 200 ns | See Figure 7-4 , STB = 0 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 190 |  | 210 | ns |
| tBIT(BUS) | Bit time on CAN bus output pins with tBIT(TXD) = 125 ns (1) | See Figure 7-4 , STB = 0 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 115 |  | 135 | ns |
| tBIT(RXD) | Bit time on RXD output pins with tBIT(TXD) = 500 ns | See Figure 7-4 , STB = 0 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 470 |  | 520 | ns |
| tBIT(RXD) | Bit time on RXD output pins with tBIT(TXD) = 200 ns | See Figure 7-4 , STB = 0 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 170 |  | 220 | ns |
| tBIT(RXD) | Bit time on RXD output pins with tBIT(TXD) = 125 ns (1) | See Figure 7-4 , STB = 0 V, RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF | 95 |  | 145 | ns |
| ΔtREC | Receiver timing symmetry with tBIT(TXD) = 500 ns | See Figure 7-4 , RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF ΔtREC = tBIT(RXD) - tBIT(BUS) | -20 |  | 15 | ns |
|  | Receiver timing symmetry with tBIT(TXD) = 200 ns | See Figure 7-4 , RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF ΔtREC = tBIT(RXD) - tBIT(BUS) | -20 |  | 15 | ns |
|  | Receiver timing symmetry with tBIT(TXD) = 125 ns (1) | See Figure 7-4 , RL = 60 Ω, CL = 100 pF, CL(RXD) = 15 pF ΔtREC = tBIT(RXD) - tBIT(BUS) | -20 |  | 15 | ns |

(1) Measured during characterization and not an ISO 11898-2:2016 parameter

![Image](TCAN1462-Q1%20Datasheet_files/img_003.png)

## 6.10 Typical Characteristics

![Image](TCAN1462-Q1%20Datasheet_files/img_012.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_013.png)

## 7 Parameter Measurement Information

Figure 7-1. ICC Test Circuit

![Image](TCAN1462-Q1%20Datasheet_files/img_014.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_015.png)

Figure 7-2. Driver Test Circuit and Measurement

![Image](TCAN1462-Q1%20Datasheet_files/img_016.png)

Figure 7-3. Receiver Test Circuit and Measurement

![Image](TCAN1462-Q1%20Datasheet_files/img_017.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_018.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_019.png)

n = 1 to 5; TXD rise/fall time &lt; 10 ns

Figure 7-4. Transmitter and Receiver Timing Behavior Test Circuit and Measurement

![Image](TCAN1462-Q1%20Datasheet_files/img_020.png)

迎

![Image](TCAN1462-Q1%20Datasheet_files/img_021.png)

STB

RXD

Figure 7-5. tMODE Test Circuit and Measurement

![Image](TCAN1462-Q1%20Datasheet_files/img_022.png)

Figure 7-6. TXD Dominant Timeout Test Circuit and Measurement

![Image](TCAN1462-Q1%20Datasheet_files/img_023.png)

Figure 7-7. Driver Short-Circuit Current Test and Measurement

tMODE

50%

50%

VIH

0 V

VOH

VOL

![Image](TCAN1462-Q1%20Datasheet_files/img_024.png)

## 8 Detailed Description

## 8.1 Overview

The devices meet or exceed the specifications of the ISO 11898-2:2016 high speed CAN (Controller Area Network) physical layer standard and CiA 601-4 Signal Improvement capability (SIC) specification. The devices are data rate agnostic making them backward compatible for supporting classical CAN applications while also supporting CAN FD networks up to 8Mbps. These devices have standby mode support which puts the transceiver in ultra-low current consumption mode. Upon receiving a valid wake-up pattern (WUP) on the CAN bus, the device signals to the microcontroller through the RXD pin. The MCU can then put the device into normal mode using the STB pin.

The TCAN1462V-Q1 has two separate supply rails, VCC bus-side supply and VIO logic supply for logic-level translation for interfacing directly to 1.8V, 2.5V, 3.3V, or 5V controllers.

## 8.1.1 Signal Improvement

Signal improvement is an additional capability added to CAN FD transceiver that enhances the maximum data rate achievable in complex star topologies by minimizing signal ringing. Signal ringing is the result of reflections caused by impedance mismatch at various points in a CAN network due to the nodes that act as stubs.

An example of a complex network is shown in Figure 8-1.

Figure 8-1. CAN Network: Star topology

![Image](TCAN1462-Q1%20Datasheet_files/img_025.png)

Recessive-to-dominant signal edge is usually clean as it is strongly driven by the transmitter. Transmitter output impedance of CAN transceiver is ~50 Ω and matches to the network characteristic impedance. For a regular CAN FD transceiver, dominant-to-recessive edge is when the driver output impedance goes to ~60 kΩ and signal reflected back experiences impedance mismatch which causes ringing. TCAN1462-Q1 resolves this issue by TX-based Signal improvement capability (SIC). The device continues to drive the bus recessive until tSIC\_TX\_base so that reflections die down and recessive bit is clean at sampling point. In the active recessive phase, transmitter output impedance is low (~100 Ω). After this phase is over and device goes to passive recessive phase, driver output impedance goes to high-Z. This phenomenon is explained with Figure 8-2.

For more information on TI's signal improvement technology, and how it compares with similar devices in market, please refer to the white paper How Signal Improvement Capability Unlocks the Real Potential of CAN-FD Transceivers.

![Image](TCAN1462-Q1%20Datasheet_files/img_020.png)

Figure 8-2. TX based SIC

![Image](TCAN1462-Q1%20Datasheet_files/img_026.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_024.png)

## 8.2 Functional Block Diagram

Figure 8-3. Block Diagram

![Image](TCAN1462-Q1%20Datasheet_files/img_027.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_028.png)

[www.ti.com](https://www.ti.com/)

## 8.3 Feature Description

## 8.3.1 Pin Description

## 8.3.1.1 TXD

The TXD input is a logic-level signal from a CAN controller to the transceiver. It is referenced to VCC for TCAN1462-Q1 or to VIO for TCAN1462V-Q1 devices.

## 8.3.1.2 GND

GND is the ground pin of the transceiver, it must be connected to the PCB ground.

## 8.3.1.3 VCC

VCC provides the 5-V power supply to the CAN transceiver.

## 8.3.1.4 RXD

The RXD output is a logic-level signal from the CAN transceiver to the CAN controller. It is referenced to VCC for TCAN1462-Q1 and VIO for TCAN1462V-Q1 devices. For TCAN1462V-Q1, RXD is only driven once VIO is present.

When a wake event takes place, RXD is driven low.

## 8.3.1.5 VIO (only for TCAN1462V-Q1)

The VIO pin provides the digital I/O voltage to match the CAN controller voltage thus avoiding the requirement for a level shifter. It supports wide range of controller interface voltage levels from 1.7 V to 5.5 V.

## 8.3.1.6 CANH and CANL

These are the CAN high and CAN low differential bus pins. These pins are connected to the CAN transceiver and the low-voltage WUP CAN receiver.

## 8.3.1.7 STB (Standby)

The STB pin is an input pin used for mode control of the transceiver. The STB pin can be supplied from either the system processor or from a static system voltage source. If normal mode is the only intended mode of operation, then the STB pin can be tied directly to GND.

## 8.3.2 CAN Bus States

The CAN bus has two logical states during operation: recessive and dominant. See Figure 8-4 and Figure 8-5.

A dominant bus state occurs when the bus is driven differentially and corresponds to a logic low on the TXD and RXD pins. A recessive bus state occurs when the bus is biased to VCC/2 via the high-resistance internal input resistors RIN) of the receiver and corresponds to a logic high on the TXD and RXD pins.

A dominant state overwrites the recessive state during arbitration. Multiple CAN nodes may be transmitting a dominant bit at the same time during arbitration, and in this case the differential voltage of the bus is greater than the differential voltage of a single driver.

The TCAN1462-Q1 transceiver implements a low-power standby (STB) mode which enables a third bus state where the bus pins are weakly biased to ground via the high resistance internal resistors of the receiver. See Figure 8-4 and Figure 8-5.

迎

![Image](TCAN1462-Q1%20Datasheet_files/img_029.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_030.png)

Figure 8-4. Bus States

W-WW

- A. Normal Mode
- B. Standby Mode

Figure 8-5. Simplified Recessive Common Mode Bias Unit and Receiver

## 8.3.3 TXD Dominant Timeout (DTO)

During normal mode, the only mode where the CAN driver is active, the TXD DTO circuit prevents the local node from blocking network communication in the event of a hardware or software failure where TXD is held dominant longer than the timeout period tTXD\_DTO. The TXD DTO circuit is triggered by a falling edge on TXD. If no rising edge is seen before the timeout period of the circuit, tTXD\_DTO, the CAN driver is disabled. This frees the bus for communication between other nodes on the network. The CAN driver is reactivated when a recessive signal is seen on the TXD pin, thus clearing the dominant time out. The receiver remains active and biased to VCC/2 and the RXD output reflects the activity on the CAN bus during the TXD DTO fault.

The minimum dominant TXD time allowed by the TXD DTO circuit limits the minimum possible transmitted data rate of the device. The CAN protocol allows a maximum of eleven successive dominant bits (on TXD) for the worst case, where five successive dominant bits are followed immediately by an error frame. The minimum transmitted data rate may be calculated using Equation 1.

<!-- formula-not-decoded -->

CANH

CANL

Bias

Unit

W

2.5V A

B

GND

WWW

RXD

![Image](TCAN1462-Q1%20Datasheet_files/img_020.png)

Figure 8-6. Example Timing Diagram for TXD Dominant Timeout

![Image](TCAN1462-Q1%20Datasheet_files/img_031.png)

## 8.3.4 CAN Bus Short-circuit Current Limiting

The TCAN1462-Q1 has several protection features that limit the short-circuit current when a CAN bus line is shorted. These include CAN driver current limiting in the dominant and recessive states and TXD dominant state timeout which prevents permanently having the higher short-circuit current of a dominant state in case of a system fault. During CAN communication the bus switches between the dominant and recessive states; thus, the short-circuit current may be viewed as either the current during each bus state or as a DC average current. When selecting termination resistors or a common mode choke for the CAN design the average power rating, IOS(AVG), should be used. The percentage dominant is limited by the TXD DTO and the CAN protocol which has forced state changes and recessive bits due to bit stuffing, control fields, and inter frame space. These make sure there is a minimum amount of recessive time on the bus even if the data field contains a high percentage of dominant bits.

The average short-circuit current of the bus depends on the ratio of recessive to dominant bits and their respective short-circuit currents. The average short-circuit current may be calculated using Equation 2.

IOS(AVG) = % Transmit x [(% REC\_Bits x IOS(SS)\_REC) + (% DOM\_Bits x IOS(SS)\_DOM)] + [% Receive x IOS(SS)\_REC] (2)

## Where:

- IOS(AVG) is the average short-circuit current
- % Transmit is the percentage the node is transmitting CAN messages
- % Receive is the percentage the node is receiving CAN messages
- % REC\_Bits is the percentage of recessive bits in the transmitted CAN messages
- % DOM\_Bits is the percentage of dominant bits in the transmitted CAN messages
- IOS(SS)\_REC is the recessive steady state short-circuit current
- IOS(SS)\_DOM is the dominant steady state short-circuit current

This short-circuit current and the possible fault cases of the network should be taken into consideration when sizing the power supply used to generate the transceivers VCC supply.

![Image](TCAN1462-Q1%20Datasheet_files/img_003.png)

## 8.3.5 Thermal Shutdown (TSD)

If the junction temperature of the TCAN1462-Q1 exceeds the thermal shutdown threshold, TTSD, the device turns off the CAN driver circuitry and blocks the TXD to bus transmission path. The shutdown condition is cleared when the junction temperature of the device drops below TTSD. The CAN bus pins are biased to VCC/2 during a TSD fault and the receiver to RXD path remains operational. The TCAN1462-Q1 TSD circuit includes hysteresis which prevents the CAN driver output from oscillating during a TSD fault.

## 8.3.6 Undervoltage Lockout

The supply pins, VCC and VIO, have undervoltage detection that places the device into a protected state. This protects the bus during an undervoltage event on either supply pin.

Table 8-1. Undervoltage Lockout - TCAN1462-Q1

| VCC | DEVICE STATE | BUS | RXD PIN |
| - | - | - | - |
| > UVVCC | Normal | Per TXD | Mirrors bus |
| < UVVCC | Protected | High impedance | High impedance |

Table 8-2. Undervoltage Lockout - TCAN1462V-Q1

| VCC | VIO | DEVICE STATE | BUS | RXD PIN |
| - | - | - | - | - |
| > UVVCC | > UVVIO | Normal | Per TXD | Mirrors bus |
| < UVVCC | > UVVIO | STB = VIO: standby mode | High impedance | VIO: Remote wake request (1) |
| < UVVCC | > UVVIO | STB = GND: Protected | High impedance | Recessive |
| > UVVCC | < UVVIO | Protected | High impedance | High impedance |
| < UVVCC | < UVVIO | Protected | High impedance | High impedance |

(1) See Remote Wake Request via Wake-Up Pattern (WUP) in Standby Mode

Once the undervoltage condition is cleared and tMODE has expired, the TCAN1462-Q1 transitions to normal mode and the host controller can send and receive CAN traffic again.

## 8.3.7 Unpowered Device

The TCAN1462-Q1 is designed to be an ideal passive or no load to the CAN bus if the device is unpowered. The bus pins were designed to have low leakage currents when the device is unpowered, so they do not load the bus. This is critical if some nodes of the network are unpowered while the rest of the of network remains operational.

The logic pins also have low leakage currents when the device is unpowered, so they do not load other circuits which may remain powered.

## 8.3.8 Floating pins

The TCAN1462-Q1 has internal pull-ups on critical pins which place the device into known states if the pin floats. This internal bias should not be relied upon by design though, especially in noisy environments, but instead should be considered a failsafe protection feature.

When a CAN controller supporting open-drain outputs is used, an adequate external pull-up resistor must be chosen. This make sures the TXD output of the CAN controller maintains acceptable bit time to the input of the CAN transceiver. See Table 8-3 for details on pin bias conditions.

Table 8-3. Pin Bias

| Pin | Pull-up or Pull-down | Comment |
| - | - | - |
| TXD | Pull-up | Weakly biases TXD towards recessive to prevent bus blockage or TXD DTO triggering |
| STB | Pull-up | Weakly biases STB towards low-power standby mode to prevent excessive system power |

![Image](TCAN1462-Q1%20Datasheet_files/img_013.png)

## 8.4 Device Functional Modes

## 8.4.1 Operating Modes

The TCAN1462-Q1 has two main operating modes; normal mode and standby mode. Operating mode selection is made by applying a high or low level to the STB pin on the TCAN1462-Q1.

Table 8-4. Operating Modes

| STB | Device Mode | Driver | Receiver | RXD Pin |
| - | - | - | - | - |
| High | Low current standby mode with bus wake-up | Disabled | Low-power receiver and bus monitor enable | High (recessive) until valid WUP is received See (1) |
| Low | Normal Mode | Enabled | Enabled | Mirrors bus state |

(1) See Remote Wake Request via Wake-Up Pattern (WUP) in Standby Mode

## 8.4.2 Normal Mode

This is the normal operating mode of the TCAN1462-Q1. The CAN driver and receiver are fully operational and CAN communication is bi-directional. The driver is translating a digital input on the TXD input to a differential output on the CANH and CANL bus pins. The receiver is translating the differential signal from CANH and CANL to a digital output on the RXD output.

## 8.4.3 Standby Mode

This is the low-power mode of the TCAN1462-Q1. The CAN driver and main receiver are switched off and bi-directional CAN communication is not possible. The low-power receiver and bus monitor circuits are enabled to allow for RXD wake-up requests via the CAN bus. A wake-up request is output to RXD as shown in Figure 8-7. The local CAN protocol controller should monitor RXD for transitions (high-to-low) and reactivate the device to normal mode by pulling the STB pin low. The CAN bus pins are weakly pulled to GND in this mode; see Figure 8-4 and Figure 8-5.

In standby mode, only the VIO supply is required therefore the VCC may be switched off for additional system level current savings.

## 8.4.3.1 Remote Wake Request via Wake-Up Pattern (WUP) in Standby Mode

The TCAN1462-Q1 supports a remote wake-up request that is used to indicate to the host controller that the bus is active and the node should return to normal operation.

The device uses the multiple filtered dominant wake-up pattern (WUP) from the ISO 11898-2:2016 standard to qualify bus activity. Once a valid WUP has been received, the wake request is indicated to the controller by a falling edge and low period corresponding to a filtered dominant on the RXD output of the TCAN1462-Q1.

The WUP consists of a filtered dominant pulse, followed by a filtered recessive pulse, and finally by a second filtered dominant pulse. The first filtered dominant initiates the WUP, and the bus monitor then waits on a filtered recessive; other bus traffic does not reset the bus monitor. Once a filtered recessive is received the bus monitor is waiting for a filtered dominant and again, other bus traffic does not reset the bus monitor. Immediately upon reception of the second filtered dominant the bus monitor recognizes the WUP and drives the RXD output low every time an additional filtered dominant signal is received from the bus.

For a dominant or recessive to be considered filtered, the bus must be in that state for more than the tWK\_FILTER time. Due to variability in tWK\_FILTER the following scenarios are applicable. Bus state times less than tWK\_FILTER(MIN) are never detected as part of a WUP and thus no wake request is generated. Bus state times between tWK\_FILTER(MIN) and tWK\_FILTER(MAX) may be detected as part of a WUP and a wake-up request may be generated. Bus state times greater than tWK\_FILTER(MAX) are always detected as part of a WUP, and thus a wake request is always generated. See Figure 8-7 for the timing diagram of the wake-up pattern.

The pattern and tWK\_FILTER time used for the WUP prevents noise and bus stuck dominant faults from causing false wake-up requests while allowing any valid message to initiate a wake-up request.

![Image](TCAN1462-Q1%20Datasheet_files/img_032.png)

The ISO 11898-2:2016 standard has defined times for a short and long wake-up filter time. The tWK\_FILTER timing for the device has been picked to be within the minimum and maximum values of both filter ranges. This timing has been chosen such that a single bit time at 500 kbps, or two back-to-back bit times at 1 Mbps triggers the filter in either bus state. Any CAN frame at 500 kbps or less would contain a valid WUP.

For an additional layer of robustness and to prevent false wake-ups, the device implements a wake-up timeout feature. For a remote wake-up event to successfully occur, the entire WUP must be received within the timeout value t ≤ tWK\_TIMEOUT. If not, the internal logic is reset and the transceiver remains in its current state without waking up. The full pattern must then be transmitted again, conforming to the constraints mentioned in this section. See Figure 8-7 for the timing diagram of the wake-up pattern with wake timeout feature.

Figure 8-7. Wake-Up Pattern (WUP) with tWK\_TIMEOUT

![Image](TCAN1462-Q1%20Datasheet_files/img_033.png)

## 8.4.4 Driver and Receiver Function

The digital logic input and output levels for the TCAN1462-Q1 are CMOS levels with respect to VCC. For TCAN1462V-Q1, these are referred to VIO for compatibility with MCUs having 1.8 V, 2.5 V, 3.3 V, or 5 V supply.

Table 8-5. Driver Function Table

| Device Mode | (1) - TXD Input | Bus Outputs - CANH | Bus Outputs - CANL | Driven Bus State (2) |
| - | - | - | - | - |
| Normal | Low | High | Low | Dominant |
| Normal | High or open | High impedance | High impedance | Biased recessive |
| Standby | X | High impedance | High impedance | Biased to ground |

(1) X = irrelevant

(2) For bus state and bias see Figure 8-4 and Figure 8-5

## Table 8-6. Receiver Function Table Normal and Standby Mode

| Device Mode | CAN Differential Inputs VID = VCANH - VCANL | Bus State | RXD Pin |
| - | - | - | - |
| Normal | VID ≥ 0.9 V | Dominant | Low |
| Normal | 0.5 V < VID < 0.9 V | Undefined | Undefined |
| Normal | VID ≤ 0.5 V | Recessive | High |
| Standby | VID ≥ 1.15 V | Dominant | High Low if a remote wake event occurred See Figure 8-7 |
| Standby | 0.4 V < VID < 1.15 V | Undefined | High Low if a remote wake event occurred See Figure 8-7 |
| Standby | VID ≤ 0.4 V | Recessive | High Low if a remote wake event occurred See Figure 8-7 |
| Any | Open (VID ≈ 0 V) | Open | High |

![Image](TCAN1462-Q1%20Datasheet_files/img_013.png)

## 9 Application and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 9.1 Application Information

## 9.2 Typical Application

The TCAN1462-Q1 transceiver can be used in applications with a host controller or FPGA that includes the link layer portion of the CAN protocol. Figure 9-1 shows a typical configuration for 5 V controller applications. The bus termination is shown for illustrative purposes.

Figure 9-1. Transceiver Application Using 5 V I/O Connections

![Image](TCAN1462-Q1%20Datasheet_files/img_034.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_024.png)

## 9.2.1 Design Requirements

## 9.2.1.1 CAN Termination

Termination may be a single 120-Ω resistor at each end of the bus, either on the cable or in a terminating node. If filtering and stabilization of the common-mode voltage of the bus is desired then split termination may be used, see Figure 9-2. Split termination improves the electromagnetic emissions behavior of the network by filtering higher-frequency common-mode noise that may be present on the differential signal lines.

Figure 9-2. CAN Bus Termination Concepts

![Image](TCAN1462-Q1%20Datasheet_files/img_035.png)

## 9.2.2 Detailed Design Procedures

## 9.2.2.1 Bus Loading, Length and Number of Nodes

A typical CAN application may have a maximum bus length of 40 meters and maximum stub length of 0.3 m. However, with careful design, users can have longer cables, longer stub lengths, and many more nodes to a bus. A high number of nodes requires a transceiver with high input impedance such as the TCAN1462-Q1. Additionally, since TCAN1462(V)-Q1 has SIC, in a given network size, higher data rate can be achieved because signal ringing is attenuated.

Many CAN organizations and standards have scaled the use of CAN for applications outside the original ISO 11898-2 standard. They made system level trade off decisions for data rate, cable length, and parasitic loading of the bus. Examples of these CAN systems level specifications are ARINC 825, CANopen, DeviceNet, SAE J2284, SAE J1939, and NMEA 2000.

A CAN network system design is a series of tradeoffs. In the ISO 11898-2:2016 specification, the driver differential output is specified with a bus load that can range from 50 Ω to 65 Ω where the differential output must be greater than 1.5 V. The TCAN1462-Q1 family is specified to meet the 1.5-V requirement down to 50 Ω and is specified to meet 1.4-V differential output at 45Ω bus load. The differential input resistance of the TCAN1462-Q1 is a minimum of 40 kΩ. If 100 TCAN1462-Q1 transceivers are in parallel on a bus, this is equivalent to a 400-Ω differential load in parallel with the nominal 60 Ω bus termination which gives a total bus load of approximately 52 Ω. Therefore, the TCAN1462-Q1 family theoretically supports over 100 transceivers on a single bus segment. However, for a CAN network design margin must be given for signal loss across the system and cabling, parasitic loadings, timing, network imbalances, ground offsets and signal integrity thus a practical maximum number of nodes is often lower. Bus length may also be extended beyond 40 meters by careful system design and data rate tradeoffs. For example, CANopen network design guidelines allow the network to be up to 1 km with changes in the termination resistance, cabling, less than 64 nodes and significantly lowered data rate.

This flexibility in CAN network design is one of the key strengths of the various extensions and additional standards that have been built on the original ISO 11898-2 CAN standard. However, when using this flexibility the CAN network system, the designer must take the responsibility of good network design for a robust network operation.

![Image](TCAN1462-Q1%20Datasheet_files/img_020.png)

[www.ti.com](https://www.ti.com/)

Figure 9-3. Typical CAN Bus

![Image](TCAN1462-Q1%20Datasheet_files/img_036.png)

## 9.2.3 Application Curves

![Image](TCAN1462-Q1%20Datasheet_files/img_037.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_006.png)

## 9.3 System Examples

The TCAN1462V-Q1 CAN transceiver is typically used in applications with a host controller or FPGA that includes the link layer portion of the CAN protocol. A 1.8 V, 2.5 V, or 3.3 V application is shown in Figure 9-6. The bus termination is shown for illustrative purposes.

Figure 9-6. Typical Transceiver Application Using 1.8 V, 2.5 V, 3.3 V IO Connections

![Image](TCAN1462-Q1%20Datasheet_files/img_038.png)

## 9.4 Power Supply Recommendations

The TCAN1462-Q1 transceiver is designed to operate with a main VCC input voltage supply range between 4.5V and 5.5V. The TCAN1462V-Q1 implements an I/O level shifting supply input, VIO, designed for a range between 1.8V and 5.5V. Both supply inputs must be well regulated. A decoupling capacitance, typically 100nF, should be placed near the CAN transceiver main VCC supply pin in addition to bypass capacitors. A decoupling capacitor, typically 100nF, should be placed near the CAN transceiver VIO supply pin in addition to bypass capacitors.

![Image](TCAN1462-Q1%20Datasheet_files/img_020.png)

## 9.5 Layout

## 9.5.1 Layout Guidelines

- Place the protection and filtering circuitry close to the bus connector, J1, to prevent transients, ESD, and noise from propagating onto the board. This layout example shows an optional transient voltage suppression (TVS) diode, D1, which may be implemented if the system-level requirements exceed the specified rating of the transceiver. This example also shows optional bus filter capacitors C4 and C5.
- Design the bus protection components in the direction of the signal path. Do not force the transient current to divert from the signal path to reach the protection device.
- Decoupling capacitors should be placed as close as possible to the supply pins VCC and VIO of transceiver.
- Use at least two vias for supply and ground connections of bypass capacitors and protection devices to minimize trace and via inductance.

## Note

High frequency current follows the path of least impedance and not the path of least resistance.

- This layout example shows how split termination could be implemented on the CAN node. The termination is split into two resistors, R4 and R5, with the center or split tap of the termination connected to ground via capacitor C3. Split termination provides common mode filtering for the bus. See CAN Termination, and CAN Bus Short Circuit Current Limiting for information on termination concepts and power ratings needed for the termination resistor(s).

## 9.5.2 Layout Example

Figure 9-7. Layout Example

![Image](TCAN1462-Q1%20Datasheet_files/img_039.png)

![Image](TCAN1462-Q1%20Datasheet_files/img_040.png)

## 10 Device and Documentation Support

## 10.1 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. In the upper right corner, click on Alert me to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 10.2 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 10.3 Trademarks

TI E2E™ is a trademark of Texas Instruments.

All trademarks are the property of their respective owners.

## 10.4 Electrostatic Discharge Caution

![Image](TCAN1462-Q1%20Datasheet_files/img_041.png)

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 10.5 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

## 11 Revision History

| Changes from Revision A (June 2022) to Revision B (October 2024) | Page |
| - | - |
| · Deleted part number TCAN1462V-Q1 from the data sheet title and header information................................... | 1 |
| Changes from Revision * (February 2022) to Revision A (June 2022) | Page |
| · Changed the data sheet from Advanced information to Production data...........................................................1 |  |

## 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](TCAN1462-Q1%20Datasheet_files/img_042.png)

ÍNSTRUMENTS

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| TCAN1462DRBRQ1 | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1462 |
| TCAN1462DRBRQ1.A | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1462 |
| TCAN1462DRQ1 | Active | Production | SOIC (D) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 1462 |
| TCAN1462DRQ1.A | Active | Production | SOIC (D) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 1462 |
| TCAN1462VDRBRQ1 | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1462V |
| TCAN1462VDRBRQ1.A | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1462V |
| TCAN1462VDRQ1 | Active | Production | SOIC (D) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 1462V |
| TCAN1462VDRQ1.A | Active | Production | SOIC (D) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 1462V |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

![Image](TCAN1462-Q1%20Datasheet_files/img_043.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

8-Nov-2025

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

![Image](TCAN1462-Q1%20Datasheet_files/img_044.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

24-Jul-2025

## TAPE AND REEL INFORMATION

![Image](TCAN1462-Q1%20Datasheet_files/img_045.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](TCAN1462-Q1%20Datasheet_files/img_046.png)

## *All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| TCAN1462DRBRQ1 | SON | DRB | 8 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q1 |
| TCAN1462DRQ1 | SOIC | D | 8 | 3000 | 330.0 | 12.4 | 6.4 | 5.2 | 2.1 | 8.0 | 12.0 | Q1 |
| TCAN1462VDRBRQ1 | SON | DRB | 8 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q1 |
| TCAN1462VDRQ1 | SOIC | D | 8 | 3000 | 330.0 | 12.4 | 6.4 | 5.2 | 2.1 | 8.0 | 12.0 | Q1 |

![Image](TCAN1462-Q1%20Datasheet_files/img_044.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

24-Jul-2025

![Image](TCAN1462-Q1%20Datasheet_files/img_047.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| TCAN1462DRBRQ1 | SON | DRB | 8 | 3000 | 367.0 | 367.0 | 35.0 |
| TCAN1462DRQ1 | SOIC | D | 8 | 3000 | 353.0 | 353.0 | 32.0 |
| TCAN1462VDRBRQ1 | SON | DRB | 8 | 3000 | 367.0 | 367.0 | 35.0 |
| TCAN1462VDRQ1 | SOIC | D | 8 | 3000 | 353.0 | 353.0 | 32.0 |

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TCAN1462-Q1%20Datasheet_files/img_048.png)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

![Image](TCAN1462-Q1%20Datasheet_files/img_049.png)

INSTRUMENTS

4203482/L

## PLASTIC QUAD FLAT PACK- NO LEAD

![Image](TCAN1462-Q1%20Datasheet_files/img_050.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for optimal thermal and mechanical performance.

![Image](TCAN1462-Q1%20Datasheet_files/img_051.png)

## PLASTIC QUAD FLAT PACK- NO LEAD

![Image](TCAN1462-Q1%20Datasheet_files/img_052.png)

NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown on this view. It is recommended that vias under paste be filled, plugged or tented.

![Image](TCAN1462-Q1%20Datasheet_files/img_053.png)

NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

![Image](TCAN1462-Q1%20Datasheet_files/img_054.png)

## PLASTIC QUAD FLAT PACK- NO LEAD

![Image](TCAN1462-Q1%20Datasheet_files/img_055.png)

## SOLDER PASTE EXAMPLE

BASED ON 0.125 mm THICK STENCIL

EXPOSED PAD 81% PRINTED COVERAGE BY AREA SCALE: 20X

4225036/A 06/2019

![Image](TCAN1462-Q1%20Datasheet_files/img_056.png)

m

SCALE 2.800

## PACKAGE OUTLINE

## SOIC - 1.75 mm max height

SMALL OUTLINE INTEGRATED CIRCUIT

![Image](TCAN1462-Q1%20Datasheet_files/img_057.png)

## NOTES:

1. Linear dimensions are in inches [millimeters]. Dimensions in parenthesis are for reference only. Controlling dimensions are in inches. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed .006 [0.15] per side.
4. This dimension does not include interlead flash.
5. Reference JEDEC registration MS-012, variation AA.

![Image](TCAN1462-Q1%20Datasheet_files/img_058.png)

SMALL OUTLINE INTEGRATED CIRCUIT

![Image](TCAN1462-Q1%20Datasheet_files/img_059.png)

NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

![Image](TCAN1462-Q1%20Datasheet_files/img_060.png)

## SOIC - 1.75 mm max height

SMALL OUTLINE INTEGRATED CIRCUIT

![Image](TCAN1462-Q1%20Datasheet_files/img_061.png)

## SOLDER PASTE EXAMPLE

BASED ON .005 INCH [0.125 MM] THICK STENCIL SCALE:8X

4214825/C 02/2019

NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
9. Board assembly site may have different recommendations for stencil design.

![Image](TCAN1462-Q1%20Datasheet_files/img_062.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2025, Texas Instruments Incorporated Last updated 10/2025
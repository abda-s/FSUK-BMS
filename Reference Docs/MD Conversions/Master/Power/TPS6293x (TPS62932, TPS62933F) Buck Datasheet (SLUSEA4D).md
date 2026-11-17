<!-- Converted from TPS6293x (TPS62932, TPS62933F) Buck Datasheet (SLUSEA4D).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_001.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_002.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_003.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_004.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_005.png)

## TPS62933, TPS62932, TPS62933F, TPS62933P, TPS62933O

SLUSEA4D - JUNE 2021 - REVISED AUGUST 2022

## TPS6293x 3.8-V to 30-V, 2-A, 3-A Synchronous Buck Converters in a SOT583 Package

## 1 Features

- Configured for a wide range of applications
- 3.8-V to 30-V input voltage range
- 0.8-V to 22-V output voltage range
- Ultra-low quiescent current: 12 μA (TPS62932, TPS62933, and TPS62933P)
- Integrated 76-mΩ and 32-mΩ MOSFETs
- 0.8 V ± 1% reference voltage (25°C)
- Maximum 98% duty cycle operation
- Precision EN threshold
- 2-A (TPS62932) and 3-A (TPS62933 and TPS62933x) continuous output current
- -40°C to 150°C operating junction temperature
- Numerous pin-compatible options
- TPS62932, TPS62933, and TPS62933F with the SS pin for adjustable soft-start time
- TPS62933P and TPS62933O with the PG pin for a power-good indicator
- TPS62932, TPS62933, and TPS62933P with pulse frequency modulation (PFM) for high light-load efficiency
- TPS62933F with forced continuous current modulation (FCCM)
- TPS62933O with out-of-audio (OOA) feature
- Ease of use and small solution size
- Peak current control mode with internal compensation
- 200-kHz to 2.2-MHz selectable frequency
- EMI friendly with frequency spread spectrum (TPS62932, TPS62933, TPS62933P and TPS62933O)
- Supports start-up with prebiased output
- Cycle-by-cycle OC limit for both high-side and low-side MOSFETs
- Non-latched protections for OTP, OCP, OVP, UVP, and UVLO
- 1.6-mm × 2.1-mm SOT583 package
- Create a custom design with the TPS6293x using the WEBENCH® Power Designer

## 2 Applications

- Building automation, appliances, industrial PC
- Multifunction printers, enterprise projectors
- Portable electronics, connected peripherals
- Smart speakers, monitors
- [Distributed power systems with 5-V, 12-V, 19-V, and 24-V input](https://www.ti.com/applications/industrial/overview.html)

## 3 Description

The TPS6293x is a high-efficiency, easy-to-use synchronous buck converter with a wide input voltage range of 3.8 V to 30 V, and supports up to 2-A (TPS62932) and 3-A (TPS62933 and TPS62933x) continuous output current and 0.8-V to 22-V output voltage.

The device employs fixed-frequency peak current control mode for fast transient response and good line and load regulation. The optimized internal loop compensation eliminates external compensation components.

The TPS62932, TPS62933, and TPS62933P operate in pulse frequency modulation for high light load efficiency. The TPS62933F operates in forced continuous current modulation which maintains lower output ripple during all load conditions. The TPS62933O operates in out of audio mode to avoid audible noise.

## Device Information

| Part Number | Package (1) | Body Size (NOM) |
| - | - | - |
| TPS6293x | SOT583 (8) | 1.60 mm × 2.10 mm |

- (1) For all available packages, see the orderable addendum at the end of the data sheet.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_006.png)

## Simplified Schematic

TPS62933 Efficiency, VIN = 24 V, fSW = 500 kHz

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_007.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_008.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_009.png)

## Table of Contents

| 1 Features............................................................................1 |  | 9.4 Device Functional Modes..........................................26 |
| - | - | - |
| 2 Applications.....................................................................1 | 10 Application and Implementation................................28 |  |
| 3 Description.......................................................................1 | 10.1 Application Information........................................... | 28 |
| 4 Revision History.............................................................. 2 | 10.2 Typical Application.................................................. | 28 |
| 5 Description (continued).................................................. 3 | 10.3 What to Do and What Not to Do............................. | 38 |
| 6 Device Comparison Table...............................................3 | 11 Power Supply Recommendations..............................39 |  |
| 7 Pin Configuration and Functions...................................3 | 12 Layout...........................................................................40 |  |
| 8 Specifications.................................................................. 5 | 12.1 Layout Guidelines .................................................. | 40 |
| 8.1 Absolute Maximum Ratings........................................ 5 | 12.2 Layout Example...................................................... | 41 |
| 8.2 ESD Ratings............................................................... 5 | 13 Device and Documentation Support..........................42 |  |
| 8.3 Recommended Operating Conditions.........................5 | 13.1 Device Support....................................................... | 42 |
| 8.4 Thermal Information....................................................6 | 13.2 Receiving Notification of Documentation Updates..42 |  |
| 8.5 Electrical Characteristics.............................................6 | 13.3 Support Resources................................................. | 42 |
| 8.6 Typical Characteristics................................................9 | 13.4 Trademarks.............................................................42 |  |
| 9 Detailed Description......................................................16 | 13.5 Electrostatic Discharge Caution..............................42 |  |
| 9.1 Overview...................................................................16 | 13.6 Glossary..................................................................42 |  |
| 9.2 Functional Block Diagram.........................................17 | 14 Mechanical, Packaging, and Orderable |  |
| 9.3 Feature Description...................................................18 | Information.................................................................... | 43 |
| 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. | 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. | 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. |
| Changes from Revision C (July 2022) to Revision D (August 2022) · | Changes from Revision C (July 2022) to Revision D (August 2022) · | Page |
| Added the TPS62933O.......................................................................................................................................1 | Added the TPS62933O.......................................................................................................................................1 | Added the TPS62933O.......................................................................................................................................1 |
| · Changed link of WEBENCH® Power Designer for TPS6293x........................................................................... Changes from Revision B (February 2022) to Revision C (July 2022) | · Changed link of WEBENCH® Power Designer for TPS6293x........................................................................... Changes from Revision B (February 2022) to Revision C (July 2022) | 1 Page |
| · Added the TPS62933F....................................................................................................................................... · Added the | TPS62933P.......................................................................................................................................1 | 1 |

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_010.png)

## 5 Description (continued)

The ULQ (ultra-low quiescent) feature is beneficial for long battery lifetime. The switching frequency can be set by the configuration of the RT pin in the range of 200 kHz to 2.2 MHz, which can optimize system efficiency, solution size, and bandwidth. The soft-start time of the TPS62932, TPS62933, and TPS62933F can be adjusted by the external capacitor at the SS pin. The TPS62932, TPS62933, TPS62933P and TPS62933O are featured with frequency spread spectrum, which helps with lowering down EMI noise.

The TPS6293x is in a small SOT583 (1.6 mm × 2.1 mm) package with 0.5-mm pin pitch, and has an optimized pinout for easy PCB layout and promotes good EMI performance.

## 6 Device Comparison Table

| Part Number | Output Current | PFM or FCCM or OOA | SS or PG Pin |
| - | - | - | - |
| TPS62932 | 2 A | PFM | SS |
| TPS62933 | 3 A | PFM | SS |
| TPS62933F | 3 A | FCCM | SS |
| TPS62933P | 3 A | PFM | PG |
| TPS62933O | 3 A | OOA | PG |

## 7 Pin Configuration and Functions

- [ ] 1 RT

- [x] 2 EN

- [x] 3 VIN

- [x] 4 GND

- [x] 8 FB

- [x] SS 7

- [x] 6 BST

- [x] 5 SW

o

- [ ] 1 RT

- [x] 2 EN

- [x] 3 VIN

- [x] 4 GND

- [x] 8 FB

- [ ] PG 7

- [x] 6 BST

- [x] 5 SW

o

Figure 7-1. TPS62932, TPS62933, and TPS62933F 8-Pin SOT583 DRL Package (Top View)

Figure 7-2. TPS62933P and TPS62933O 8-Pin SOT583 DRL Package (Top View)

## Table 7-1. Pin Functions

| Pin - Name | Pin - NO. | Type (1) | Description |
| - | - | - | - |
| RT | 1 | A | Frequency programming input. Float for 500 kHz, tie to GND for 1.2 MHz, or connect to an RT timing resistor. See Section 9.3.5 for details. |
| EN | 2 | A | Enable input to the converter. Driving EN high or leaving this pin floating enables the converter. An external resistor divider can be used to implement an adjustable VIN UVLO function. |
| VIN | 3 | P | Supply input pin to internal LDO and high-side FET. Input bypass capacitors must be directly connected to this pin and GND. |
| GND | 4 | G | Ground pin. Connected to the source of the low-side FET as well as the ground pin for the controller circuit. Connect to system ground and the ground side of CIN and COUT. The path to CIN must be as short as possible. |
| SW | 5 | P | Switching output of the convertor. Internally connected to the source of the high-side FET and drain of the low-side FET. Connect to the power inductor. |
| BST | 6 | P | Bootstrap capacitor connection for high-side FET driver. Connect a high-quality, 100-nF ceramic capacitor from this pin to the SW pin. |

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_011.png)

## Table 7-1. Pin Functions (continued)

| Pin - Name | Pin - NO. | Type (1) | Description |
| - | - | - | - |
| SS/PG | 7 | A | TPS62932, TPS62933, and TPS62933F soft-start control pin. An external capacitor connected to this pin sets the internal voltage reference rising time. See Section 9.3.7 for details. A minimum 6.8-nF ceramic capacitor must be connected at this pin, which sets the minimum soft-start time to approximately 1 ms. Do not float. |
| SS/PG | 7 | A | TPS62933P and TPS62933O open-drain power good indicator, which is asserted low if output voltage is out of PG threshold, overvoltage, or if the device is under thermal shutdown, EN shutdown, or during soft start. |
| FB | 8 | A | Output feedback input. Connect FB to the tap of an external resistor divider from the output to GND to set output voltage. |

(1) A = Analog, P = Power, G = Ground

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_012.png)

## 8 Specifications

## 8.1 Absolute Maximum Ratings

Over the recommended operating junction temperature range of -40°C to +150°C , unless otherwise noted (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Input voltage | VIN | -0.3 | 32 | V |
| Input voltage | EN | -0.3 | 6 | V |
| Input voltage | FB | -0.3 | 6 | V |
| Output voltage | SW, DC | -0.3 | 32 | V |
| Output voltage | SW, transient < 10 ns | -3 | 33 | V |
| Output voltage | BST | -0.3 | SW + 6 | V |
| Output voltage | BST-SW | -0.3 | 6 | V |
| Output voltage | SS/PG | -0.3 | 6 | V |
| Output voltage | RT | -0.3 | 6 | V |
| TJ | Operating junction temperature (2) | -40 | 150 | °C |
| Tstg | Storage temperature | -65 | 150 | °C |

(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.

(2) Operating at junction temperatures greater than 150°C, although possible, degrades the lifetime of the device.

## 8.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| - | - | - | - | - |
| V(ESD) | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/JEDEC JS-001, all pins (1) Charged device model (CDM), per JS-002, all pins (2) | ±2000 | V |
| V(ESD) | Electrostatic discharge | ANSI/ESDA/JEDEC | ±500 | V |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.

(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 8.3 Recommended Operating Conditions

Over the recommended operating junction temperature range of -40°C to +150°C, unless otherwise noted (1)

|  |  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - | - |
| Input voltage | VIN | VIN | 3.8 |  | 30 | V |
| Input voltage | EN | EN | -0.1 |  | 5.5 | V |
| Input voltage | FB | FB | -0.1 |  | 5.5 | V |
| Input voltage | PG | PG | -0.1 |  | 5.5 | V |
| Output voltage | VOUT | VOUT | 0.8 |  | 22 | V |
| Output voltage | SW, DC | SW, DC | -0.1 |  | 30 | V |
| Output voltage | SW, transient < 10 ns | SW, transient < 10 ns | -3 |  | 32 | V |
| Output voltage | BST | BST | -0.1 |  | SW + 5.5 | V |
| Output voltage | BST-SW | BST-SW | -0.1 |  | 5.5 | V |
| Ouput current |  | TPS62933, TPS62933x | 0 |  | 3 | A |
| IOUT |  | TPS62932 | 0 |  | 2 | A |
| Temperature | Operating junction temperature, TJ | Operating junction temperature, TJ | -40 |  | 150 | °C |

(1) The Recommended Operating Conditions indicate conditions for which the device is intended to be functional, but do not guarantee specific performance limits. For compliant specifications, see the Electrical Characteristics.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_013.png)

## 8.4 Thermal Information

|  | THERMAL METRIC (1) | TPS6293x DRL (SOT583), 8 PINS - JEDEC (2) | TPS6293x DRL (SOT583), 8 PINS - EVM (3) | UNIT |
| - | - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 112.2 | N/A | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 29.1 | N/A | °C/W |
| RθJB | Junction-to-board thermal resistance | 19.3 | N/A | °C/W |
| ΨJT | Junction-to-top characterization parameter | 1.6 | N/A | °C/W |
| ΨJB | Junction-to-board characterization parameter | 19.2 | N/A | °C/W |
| RθJA_EVM | Junction-to-ambient thermal resistance on official EVM board | N/A | 60.2 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

(2) The value of RθJA given in this table is only valid for comparison with other packages and can not be used for design purposes. These values were simulated on a standard JEDEC board. They do not represent the performance obtained in an actual application.

(3) The real RθJA is tested on TI EVM (2 layer, 2-ounce copper thickness).

## 8.5 Electrical Characteristics

The electrical ratings specified in this section apply to all specifications in this document, unless otherwise noted. These specifications are interpreted as conditions that do not degrade the device parametric or functional specifications for the life of the product containing it. TJ = -40°C to +150°C, VIN = 3.8 V to 30 V, unless otherwise noted.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| POWER SUPPLY (VIN PIN) | POWER SUPPLY (VIN PIN) | POWER SUPPLY (VIN PIN) | POWER SUPPLY (VIN PIN) | POWER SUPPLY (VIN PIN) | POWER SUPPLY (VIN PIN) | POWER SUPPLY (VIN PIN) |
| VIN | Operation input voltage |  | 3.8 |  | 30 | V |
| IQ | Nonswitching quiescent current | EN = 5 V, VFB = 0.85 V, TPS62932, TPS62933, and TPS62933P |  | 12 |  | µA |
| IQ | Nonswitching quiescent current | EN = 5 V, VFB = 1 V, TPS62933F |  | 125 |  | µA |
| IQ | Nonswitching quiescent current | EN = 5 V, VFB = 1 V, TPS62933O |  | 45 |  | µA |
| ISHDN | Shutdown supply current | VEN = 0 V |  | 2 |  | µA |
| VIN_UVLO | Input undervoltage lockout thresholds | Rising threshold | 3.4 | 3.6 | 3.8 | V |
| VIN_UVLO | Input undervoltage lockout thresholds | Falling threshold | 3.1 | 3.3 | 3.5 | V |
| VIN_UVLO | Input undervoltage lockout thresholds | Hysteresis |  | 300 |  | mV |
| ENABLE (EN PIN) | ENABLE (EN PIN) | ENABLE (EN PIN) | ENABLE (EN PIN) | ENABLE (EN PIN) | ENABLE (EN PIN) | ENABLE (EN PIN) |
| VEN_RISE | Enable threshold | Rising enable threshold |  | 1.21 | 1.28 | V |
| VEN_FALL | Disable threshold | Falling disable threshold | 1.1 | 1.17 |  | V |
| Ip | EN pullup current | VEN = 1.0 V |  | 0.7 |  | µA |
| Ih | EN pullup hysteresis current | VEN = 1.5 V |  | 1.4 |  | µA |
| VOLTAGE REFERENCE (FB PIN) | VOLTAGE REFERENCE (FB PIN) | VOLTAGE REFERENCE (FB PIN) | VOLTAGE REFERENCE (FB PIN) | VOLTAGE REFERENCE (FB PIN) | VOLTAGE REFERENCE (FB PIN) | VOLTAGE REFERENCE (FB PIN) |
| VFB | FB voltage | TJ = 25°C | 792 | 800 | 808 | mV |
| VFB | FB voltage | TJ = 0°C to 85°C | 788 | 800 | 812 | mV |
| VFB | FB voltage | TJ = -40°C to 150°C | 784 | 800 | 816 | mV |
| IFB | Input leakage current | VFB = 0.8 V |  |  | 0.15 | μA |
| INTEGRATED POWER MOSFETS | INTEGRATED POWER MOSFETS | INTEGRATED POWER MOSFETS | INTEGRATED POWER MOSFETS | INTEGRATED POWER MOSFETS | INTEGRATED POWER MOSFETS | INTEGRATED POWER MOSFETS |
| RDSON_HS | High-side MOSFET on-resistance | TJ = 25°C, VBST - SW = 5 V |  | 76 |  | mΩ |
| RDSON_LS | Low-side MOSFET on-resistance | TJ = 25°C |  | 32 |  | mΩ |
| CURRENT LIMIT | CURRENT LIMIT | CURRENT LIMIT | CURRENT LIMIT | CURRENT LIMIT | CURRENT LIMIT | CURRENT LIMIT |
| IHS_LIMIT | High-side MOSFET current limit | TPS62933 and TPS62933x | 4.2 | 5 | 5.8 | A |
| IHS_LIMIT | High-side MOSFET current limit | TPS62932 | 2.8 | 3.4 | 4 | A |

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_010.png)

[www.ti.com](https://www.ti.com/)

## 8.5 Electrical Characteristics (continued)

The electrical ratings specified in this section apply to all specifications in this document, unless otherwise noted. These specifications are interpreted as conditions that do not degrade the device parametric or functional specifications for the life of the product containing it. TJ = -40°C to +150°C, VIN = 3.8 V to 30 V, unless otherwise noted.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| ILS_LIMIT | Low-side MOSFET current limit | TPS62933 and TPS62933x | 2.9 | 3.8 | 4.5 | A |
| ILS_NOC Reverse current limit | ILS_NOC Reverse current limit | TPS62932 TPS62933F | 2 | 2.5 2.4 | 3 | A |
| IPEAK_MIN | Minimum peak inductor current | TPS62933, TPS62933P, and TPS62933O | 1.2 |  | 3.6 |  |
|  |  | TPS62932 |  | 0.75 0.53 |  | A |
| SOFT START (SS PIN) | SOFT START (SS PIN) | SOFT START (SS PIN) | SOFT START (SS PIN) | SOFT START (SS PIN) | SOFT START (SS PIN) | SOFT START (SS PIN) |
| ISS | Soft-start charge current | TPS62932, TPS62933, and TPS62933F | 4.5 | 5.5 | 6.5 | μA |
| TSS | Fixed internal soft-start time | TPS62933P and TPS62933O |  | 2 |  | ms |
| POWER GOOD (PG PIN) | POWER GOOD (PG PIN) | POWER GOOD (PG PIN) | POWER GOOD (PG PIN) | POWER GOOD (PG PIN) | POWER GOOD (PG PIN) | POWER GOOD (PG PIN) |
|  |  | VFB falling, PG high to low |  | 85% |  |  |
|  |  | VFB rising, PG low to high |  | 90% |  |  |
| VPGTH PG threshold, VFB percentage | VPGTH PG threshold, VFB percentage | VFB falling, PG low to high |  | 110% |  |  |
|  |  | VFB rising, PG high to low |  | 115% |  |  |
| TPG_R | PG delay time | PG from low to high |  | 70 |  | μs |
| TPG_F | PG delay time | PG from high to low |  | 18 |  | μs |
| VIN_PG_VALID | Minimum VIN for valid PG output | Measured when PG < 0.5 V with 100-kΩ pullup to external 5 V |  | 2 | 2.5 | V |
| VPG_OL | PG output low-level voltage | IPG = 0.5 mA |  |  | 0.3 | V |
| IPG_LK | PG leakage current when open drain is high | VPG = 5.5 V | -1 |  | 1 | μA |
| OSCILLATOR FREQUENCY (RT PIN) | OSCILLATOR FREQUENCY (RT PIN) | OSCILLATOR FREQUENCY (RT PIN) | OSCILLATOR FREQUENCY (RT PIN) | OSCILLATOR FREQUENCY (RT PIN) | OSCILLATOR FREQUENCY (RT PIN) | OSCILLATOR FREQUENCY (RT PIN) |
|  |  | RT = floating | 450 | 500 | 550 | kHz |
|  |  | RT = GND | 1000 | 1200 | 1350 |  |
| fSW Switching center frequency | fSW Switching center frequency | RT = 71.5 kΩ |  | 310 |  |  |
|  |  | RT = 9.09 kΩ |  | 2100 |  |  |
| fSW_min | Minimum switching frequency | TPS62933O |  | 30 |  | kHz |
| tON_MIN (1) | Minimum ON pulse width |  |  | 70 |  | ns |
| tOFF_MIN (1) | Minimum OFF pulse width |  |  | 140 |  | ns |
| tON_MAX (1) | Maximum ON pulse width |  |  | 7 |  | μs |
| OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION | OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION | OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION | OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION | OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION | OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION | OUTPUT OVERVOLTAGE AND UNDERVOLTAGE PROTECTION |
| VOVP | Output OVP threshold | OVP detect (L→H) | 112% | 115% | 118% |  |
|  |  | Hysteresis |  | 5% |  |  |
| VUVP | Output UVP threshold | UVP detect (H→L) |  | 65% |  |  |
| thiccup_ON UV hiccup ON time before entering hiccup mode after soft start ends | thiccup_ON UV hiccup ON time before entering hiccup mode after soft start ends |  |  | 256 |  | μs |
| thiccup_OFF UV hiccup OFF time before restart | thiccup_OFF UV hiccup OFF time before restart |  |  | 10.5 × tSS |  | s |
| THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN |
| TSHDN (1) | Thermal shutdown threshold | Shutdown temperature |  | 165 |  | °C |
| THYS (1) | THYS (1) | Hysteresis |  | 30 |  | °C |
| SPREAD SPECTRUM FREQUENCY | SPREAD SPECTRUM FREQUENCY | SPREAD SPECTRUM FREQUENCY | SPREAD SPECTRUM FREQUENCY | SPREAD SPECTRUM FREQUENCY | SPREAD SPECTRUM FREQUENCY | SPREAD SPECTRUM FREQUENCY |
| fm | Modulation frequency |  | fSW | / 128 |  | kHz |

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_014.png)

## 8.5 Electrical Characteristics (continued)

The electrical ratings specified in this section apply to all specifications in this document, unless otherwise noted. These specifications are interpreted as conditions that do not degrade the device parametric or functional specifications for the life of the product containing it. TJ = -40°C to +150°C, VIN = 3.8 V to 30 V, unless otherwise noted.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| fspread | Internal spread oscillator frequency |  | ±6% |  |  |  |

(1) Not production tested, specified by design.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

## 8.6 Typical Characteristics

TJ = -40°C to 150°C, VIN = 12 V, unless otherwise noted.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_016.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_017.png)

## 8.6 Typical Characteristics (continued)

TJ = -40°C to 150°C, VIN = 12 V, unless otherwise noted.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_018.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

## 8.6 Typical Characteristics (continued)

TJ = -40°C to 150°C, VIN = 12 V, unless otherwise noted.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_019.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_017.png)

## 8.6 Typical Characteristics (continued)

TJ = -40°C to 150°C, VIN = 12 V, unless otherwise noted.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_020.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

## 8.6 Typical Characteristics (continued)

TJ = -40°C to 150°C, VIN = 12 V, unless otherwise noted.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_021.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_017.png)

## 8.6 Typical Characteristics (continued)

TJ = -40°C to 150°C, VIN = 12 V, unless otherwise noted.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_022.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

## 8.6 Typical Characteristics (continued)

TJ = -40°C to 150°C, VIN = 12 V, unless otherwise noted.

Figure 8-37. TPS62933 Switching Frequency vs VIN, VOUT = 3.3 V, IOUT = 3 A

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_023.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_024.png)

## 9 Detailed Description

## 9.1 Overview

The TPS62932 and TPS62933x are a 30-V, 2-A and 3-A, synchronous buck (step-down) converters with two integrated n-channel MOSFETs. They employ fixed-frequency peak current control mode for fast transient response and good line and load regulation. With the optimized internal loop compensation, the devices eliminate the external compensation components over a wide range of output voltage and switching frequency.

The integrated 76-mΩ and 32-mΩ MOSFETs allow for high-efficiency power supply designs with continuous output currents up to 2 A (TPS62932) or 3 A (TPS62933 and TPS62933x). The feedback reference voltage is designed at 0.8 V. The output voltage can be stepped down from 0.8 V to 22 V. The devices are ideally suited for systems powered from 5-V, 12-V, 19-V, and 24-V power-bus rails.

The TPS6293x has been designed for safe monotonic start-up into prebiased loads. The default start-up is at VIN equal to 3.8 V. After the device is enabled, the output rises smoothly from 0 V to its regulated voltage. The TPS6293x has low operating current when not switching under no load, especially the TPS62932, TPS62933, and TPS62933P whose operating current is 12 μA (typical). When the TPS6293x is disabled, the supply current is approximately 2 µA (typical). These features are extremely beneficial for long battery life time in low-power operation.

Pulse frequency modulation (PFM) mode allows the TPS62932, TPS62933, and TPS62933P to maximize the light-load efficiency. Continuous current mode allows the TPS62933F to have low output ripple in all load conditions. The TPS62933O operates in out of audio mode which can avoid the audible noise.

The EN pin has an internal pullup current that can be used to adjust the input voltage undervoltage lockout (UVLO) with two external resistors. In addition, the EN pin can be floating for the device to operate with the internal pullup current.

The switching frequency can be set by the configuration of the RT pin in the range of 200 kHz to 2.2 MHz, which allows for efficiency and solution size optimization when selecting the output filter components. The TPS62932, TPS62933, TPS62933P, and TPS62933O also have a frequency spread spectrum feature, which helps with lowering down EMI noise.

A small value capacitor or resistor divider is connected to the SS pin of the TPS62932, TPS62933, and TPS62933F for soft-start time setting or voltage tracking. The TPS62933P and TPS62933O indicate power good through PG pin.

The devices have the on-time extension function with a maximum on time of 7 μs (typical). During low dropout operation, the high-side MOSFET can turn on up to 7 μs, then the high-side MOSFET turns off and the low-side MOSFET turns on with a minimum off time of 140 ns (typical). The devices support the maximum 98% duty cycle.

The devices reduce the external component count by integrating the bootstrap circuit. The bias voltage for the integrated high-side MOSFET is supplied by a capacitor between the BST and SW pins. A UVLO circuit monitors the bootstrap capacitor voltage, VBST-SW. When it falls below a preset threshold of 2.5 V (typical), the SW pin is pulled low to recharge the bootstrap capacitor.

Cycle-by-cycle current limiting on the high-side MOSFET protects the device in overload situations and is enhanced by a low-side sourcing current limit, which prevents current runaway. The TPS6293x provides output undervoltage protection (UVP) when the regulated output voltage is lower than 65% of the nominal voltage due to overcurrent being triggered, approximately 256-μs (typical) deglitch time later, both the high-side and low-side MOSFET turn off, the device steps into hiccup mode.

The devices minimize excessive output overvoltage transient by taking advantage of the overvoltage comparator. When the regulated output voltage is greater than 115% of the nominal voltage, the overvoltage comparator is activated, and the high-side MOSFET is turned off and masked from turning on until the output voltage is lower than 110%.

Thermal shutdown disables the devices when the die temperature, TJ, exceeds 165°C and enables the devices again after TJ decreases below the hysteresis amount of 30°C.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

## 9.2 Functional Block Diagram

EN

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_025.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_026.png)

[www.ti.com](https://www.ti.com/)

## 9.3 Feature Description

## 9.3.1 Fixed Frequency Peak Current Mode

The following operation description of the TPS6293x refers to the functional block diagram and to the waveforms in Figure 9-1. The TPS6293x is a synchronous buck converter with integrated high-side (HS) and low-side (LS) MOSFETs (synchronous rectifier). The TPS6293x supplies a regulated output voltage by turning on the HS and LS NMOS switches with controlled duty cycle. During high-side switch on time, the SW pin voltage swings up to approximately VIN, and the inductor current, iL, increases with linear slope (VIN - VOUT) / L. When the HS switch is turned off by the control logic, the LS switch is turned on after an anti-shoot-through dead time. Inductor current discharges through the low-side switch with a slope of -VOUT / L. The control parameter of a buck converter is defined as Duty Cycle D = tON / tSW, where tON is the high-side switch on time and tSW is the switching period. The converter control loop maintains a constant output voltage by adjusting the duty cycle D. In an ideal buck converter where losses are ignored, D is proportional to the output voltage and inversely proportional to the input voltage: D = VOUT / VIN.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_027.png)

→

Figure 9-1. SW Node and Inductor Current Waveforms in Continuous Conduction Mode (CCM)

The TPS6293x employs the fixed-frequency peak current mode control. A voltage feedback loop is used to get accurate DC voltage regulation by adjusting the peak current command based on voltage offset. The peak inductor current is sensed from the HS switch and compared to the peak current threshold to control the on time of the HS switch. The voltage feedback loop is internally compensated, which allows for fewer external components, makes it easy to design, and provides stable operation with almost any combination of output capacitors.

## 9.3.2 Pulse Frequency Modulation

The TPS62932, TPS62933, and TPS62933P are designed to operate in pulse frequency modulation (PFM) mode at light load currents to boost light load efficiency.

When the load current is lower than half of the peak-to-peak inductor current in CCM, the devices operate in discontinuous conduction mode (DCM). In DCM operation, the low-side switch is turned off when the inductor current drops to ILS\_ZC to improve efficiency. Both switching losses and conduction losses are reduced in DCM, compared to forced CCM operation at light load.

At even lighter current load, pulse frequency modulation (PFM) mode is activated to maintain high-efficiency operation. When either the minimum high-side switch on time, tON\_MIN, or the minimum peak inductor current IPEAK\_MIN is reached, the switching frequency decreases to maintain regulation. In PFM mode, the switching frequency is decreased by the control loop to maintain output voltage regulation when load current reduces.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_028.png)

Switching loss is further reduced in PFM operation due to less frequent switching actions. Since the integrated current comparator catches the peak inductor current only, the average load current entering PFM mode varies with the applications and external output LC filters.

In PFM mode, the high-side MOSFET is turned on in a burst of one or more pulses to provide energy to the load. The duration of the burst depends on how long it takes the feedback voltage catches VREF. The periodicity of these bursts is adjusted to regulate the output, while zero current crossing detection turns off the low-side MOSFET to maximize efficiency. This mode provides high light-load efficiency by reducing the amount of input supply current required to regulate the output voltage at small loads. This trades off very good light-load efficiency for larger output voltage ripple and variable switching frequency.

## 9.3.3 Voltage Reference

The internal reference voltage, VREF, is designed at 0.8 V (typical). The negative feedback system of converter produces a precise ±2% feedback voltage, VFB, over full temperature by scaling the output of a temperaturestable internal band-gap circuit.

## 9.3.4 Output Voltage Setting

A precision 0.8-V reference voltage, VREF, is used to maintain a tightly regulated output voltage over the entire operating temperature range. The output voltage is set by a resistor divider from the output voltage to the FB pin. TI recommends using 1% tolerance resistors with a low temperature coefficient for the FB divider. Select the bottom-side resistor, RFBB, for the desired divider current and use Equation 1 to calculate the top-side resistor, RFBT. Lower RFBB increases the divider current and reduces efficiency at very light load. Larger RFBB makes the FB voltage more susceptible to noise, so larger RFBB values require a more carefully designed feedback path on the PCB. Setting RFBB = 10 kΩ and RFBT in the range of 10 kΩ to 300 kΩ is recommended for most applications.

The tolerance and temperature variation of the resistor dividers affect the output voltage regulation.

Figure 9-2. Output Voltage Setting

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_029.png)

<!-- formula-not-decoded -->

## where

- VREF is the 0.8 V (the internal reference voltage).
- RFBB is 10 kΩ (recommended).

## 9.3.5 Switching Frequency Selection

The switching frequency is set by the condition of the RT input. The condition of this input is detected when the device is first enabled. Once the converter is running, the switching frequency selection is fixed and cannot be changed until the next power-on cycle or EN toggle. Table 9-1 shows the selection programming. In adjustable frequency mode, the switching frequency can be set between 200 kHz and 2200 kHz by proper selection of RT resistor. See Equation 2.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_014.png)

fsw(kHz) = 17293 × RT(kΩ)−0.942

## where

- RT is the value of RT timing resistor in kΩ.
- fSW is the switching frequency in kHz.

## Table 9-1. RT Pin Resistor Settings

Figure 9-3 indicates the required resistor value for RT to set a desired switching frequency.

| RT Pin | Resistance | Switching Frequency |
| - | - | - |
| Floating | > 280 kΩ | 500 kHz |
| GND | < 1 kΩ | 1200 kHz |
| RT to GND | 8.9 kΩ to 111 kΩ | 200 kHz to 2200 kHz |

Figure 9-3. Switching Frequency vs RT

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_030.png)

There are four cases where the switching frequency does not conform to the condition set by the RT pin:

- Light load operation (PFM mode)
- Low dropout operation
- Minimum on-time operation
- Current limit tripped

Under all of these cases, the switching frequency folds back, meaning it is less than that programmed by the RT pin. During these conditions, the output voltage remains in regulation, except for current limit operation.

## 9.3.6 Enable and Adjusting Undervoltage Lockout

The EN pin provides electrical ON and OFF control of the device. When the EN pin voltage exceeds the enable threshold voltage, VEN\_RISE, the TPS6293x begins operation. If the EN pin voltage is pulled below the disable threshold voltage, VEN\_FALL, the converter stops switching and enters shutdown mode.

The EN pin has an internal pullup current source, which allows the user to float the EN pin to enable the device. If an application requires control of the EN pin, use an open-drain or open-collector or GPIO output logic to interface with the pin.

The TPS6293x implements internal undervoltage-lockout (UVLO) circuitry on the VIN pin. The device is disabled when the VIN pin voltage falls below the internal VIN\_UVLO threshold. The internal VIN\_UVLO threshold has a hysteresis of typical 300 mV. If an application requires a higher UVLO threshold on the VIN pin, the EN pin can

(2)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_031.png)

be configured as shown in Figure 9-4. When using the external UVLO function, setting the hysteresis at a value greater than 500 mV is recommended.

The EN pin has a small pullup current, Ip, which sets the default state of the EN pin to enable when no external components are connected. The pullup hysteresis current, Ih, is used to control the hysteresis voltage for the UVLO function when the EN pin voltage crosses the enable threshold. Use Equation 3 and Equation 4 to calculate the values of R1 and R2 for a specified UVLO threshold. Once R1 and R2 are settled down, VEN can be calculated by Equation 5, which must be lower than 5.5 V with the maximum VIN.

Figure 9-4. Adjustable VIN Undervoltage Lockout

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_032.png)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## where

- Ip is 0.7 µA.
- Ih is 1.4 µA.
- VEN\_FALL is 1.17 V.
- VEN\_RISE is 1.21 V.
- VSTART is the input voltage enabling the device.
- VSTOP is the input voltage disabling the device.

## 9.3.7 External Soft Start and Prebiased Soft Start

The SS pin of TPS62932, TPS62933, and TPS62933F are used to minimize inrush current when driving capacitive load. The devices use the lower voltage of the internal voltage reference, VREF, or the SS pin voltage as the reference voltage and regulates the output accordingly. A capacitor on the SS pin to ground implements a soft-start time. The device has an internal pullup current source that charges the external soft-start capacitor. Use Equation 6 to calculate the soft-start time (tSS, 0% to 100%) and soft-start capacitor (CSS).

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_033.png)

<!-- formula-not-decoded -->

## where

- VREF is 0.8 V (the internal reference voltage).
- ISS is 5.5 µA (typical), the internal pullup current.

If the output capacitor is prebiased at start-up, the devices initiate switching and start ramping up only after the internal reference voltage becomes greater than the feedback voltage, VFB. This scheme makes sure that the converters ramp up smoothly into regulation point.

A resistor divider connected to the SS pin can implement voltage tracking of the other power rail.

## 9.3.8 Power Good

The TPS62933P and TPS62933O have a built-in power good (PG) function to indicate whether the output voltage has reached its appropriate level or not. The PG signal can be used for start-up sequencing of multiple rails. The PG pin is an open-drain output that requires a pullup resistor to any voltage below 5.5 V. TI recommends a pullup resistor of 10 kΩ - 100 kΩ. The device can sink approximately 4 mA of current and maintain its specified logic low level. After the FB pin voltage is between 90% and 110% of the internal reference voltage (VREF) and after a deglitch time of 70 μs, the PG turns to high impedance status. The PG pin is pulled low after a deglitch time of 18 μs when FB pin voltage is lower than 85% of the internal reference voltage or greater than 115% of the internal reference voltage, or in events of thermal shutdown, EN shutdown, or UVLO conditions. VIN must remain present for the PG pin to stay low.

Table 9-2. PG Status

| Device State | Device State | PG Logic Status - High Impedance | PG Logic Status - Low |
| - | - | - | - |
| Enable (EN = High) | VFB does not trigger VPGTH | √ |  |
| Enable (EN = High) | VFB triggers VPGTH |  | √ |
| Shutdown (EN = Low) |  |  | √ |
| UVLO | 2.5 V < VIN < VUVLO |  | √ |
| Thermal shutdown | TJ > TSD |  | √ |
| Power supply removal | VIN < 2.5 V | √ |  |

## 9.3.9 Minimum On Time, Minimum Off Time, and Frequency Foldback

Minimum on time (tON\_MIN) is the smallest duration of time that the high-side switch can be on. tON\_MIN is typically 70 ns in the TPS6293x. Minimum off time (tOFF\_MIN) is the smallest duration that the high-side switch can be off. tOFF\_MIN is typically 140 ns. In CCM operation, tON\_MIN, and tOFF\_MIN, limit the voltage conversion range without switching frequency foldback.

The minimum duty cycle without frequency foldback allowed is:

<!-- formula-not-decoded -->

The maximum duty cycle without frequency foldback allowed is:

<!-- formula-not-decoded -->

Given a required output voltage, the maximum VIN without frequency foldback is:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

The minimum VIN without frequency foldback is:

<!-- formula-not-decoded -->

In TPS6293x, a frequency foldback scheme is employed once tON\_MIN or tOFF\_MIN is triggered, which can extend the maximum duty cycle or lower the minimum duty cycle.

The on time decreases while VIN voltage increases. Once the on time decreases to tON\_MIN, the switching frequency starts to decrease while VIN continues to go up, which lowers the duty cycle further to keep VOUT in regulation according to Equation 7.

The frequency foldback scheme also works once larger duty cycle is needed under low VIN condition. The frequency decreases once the device hits its tOFF\_MIN, which extends the maximum duty cycle according to Equation 8. A wide range of frequency foldback allows the TPS6293x output voltage to stay in regulation with a much lower supply voltage VIN, which allows a lower effective dropout.

With frequency foldback, VIN\_MAX is raised, and VIN\_MIN is lowered by decreased fSW.

Figure 9-5. Frequency Foldback at tON\_MIN, VOUT = 1.8 V, fSW = 1200 kHz

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_034.png)

Frequency (kHz)

Iout=1.5A

Iout=3A

4

5

6

7

8

9

10

11

12

Vin (V)

Figure 9-6. Frequency Foldback at tOFF\_MIN, VOUT = 5 V, fSW = 1200 kHz

## 9.3.10 Frequency Spread Spectrum

To reduce EMI, the TPS62932, TPS62933, TPS62933P, and TPS62933O introduce frequency spread spectrum. The jittering span is typically Δfc = ±6% of the switching frequency with the modulation frequency of fm = fSW / 128. The purpose of spread spectrum is to eliminate peak emissions at specific frequencies by spreading emissions across a wider range of frequencies than a part with fixed frequency operation. Figure 9-7 shows the frequency spread spectrum modulation. Figure 9-8 shows the energy is spread out at the center frequency, fc.

1500

1250

1000

750

500

250

0

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_014.png)

Figure 9-7. Frequency Spread Spectrum Diagram

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_035.png)

Figure 9-8. Energy vs Frequency

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_036.png)

## 9.3.11 Overvoltage Protection

The device incorporates an output overvoltage protection (OVP) circuit to minimize output voltage overshoot. The OVP feature minimizes the overshoot by comparing the FB pin voltage to the OVP threshold. If the FB pin voltage is greater than the OVP threshold of 115%, the high-side MOSFET is turned off, which prevents current from flowing to the output and minimizes output overshoot. When the FB pin voltage drops lower than the OVP threshold minus hysteresis, the high-side MOSFET is allowed to turn on at the next clock cycle. This function is non-latch operation.

## 9.3.12 Overcurrent and Undervoltage Protection

The TPS6293x incorporates both peak and valley inductor current limits to provide protection to the device from overloads and short circuits and limit the maximum output current. Valley current limit prevents inductor current run-away during short circuits on the output, while both peak and valley limits work together to limit the maximum output current of the converter. Hiccup mode is also incorporated for sustained short circuits.

The high-side switch current is sensed when it is turned on after a set blanking time (tON\_MIN), the peak current of high-side switch is limited by the peak current threshold, IHS\_LIMIT. The current going through low-side switch is also sensed and monitored. When the low-side switch turns on, the inductor current begins to ramp down.

As the device is overloaded, a point is reached where the valley of the inductor current cannot reach below ILS\_LIMIT before the next clock cycle, then the low-side switch is kept on until the inductor current ramps below

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

the valley current threshold, ILS\_LIMIT, then the low-side switch is turned off and the high-side switch is turned on after a dead time. When this occurs, the valley current limit control skips that cycle, causing the switching frequency to drop. Further overload causes the switching frequency to continue to drop, but the output voltage remains in regulation. As the overload is increased, both the inductor current ripple and peak current increase until the high-side current limit, IHS\_LIMIT, is reached. When this limit is tripped, the switch duty cycle is reduced and the output voltage falls out of regulation. This represents the maximum output current from the converter and is given approximately by Equation 11. The output voltage and switching frequency continue to drop as the device moves deeper into overload while the output current remains at approximately IOMAX. There is another situation, if the inductor ripple current is large, the high-side current limit can be tripped before the low-side limit is reached. In this case, Equation 12 gives the approximate maximum output current.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Furthermore, if a severe overload or short circuit causes the FB voltage to fall below the VUVP threshold, 65% of the VREF, and triggering current limit, and the condition occurs for more than the hiccup on time (typical 256 μs), the converter enters hiccup mode. In this mode, the device stops switching for hiccup off time, 10.5 × tSS, and then goes to a normal restart with soft-start time. If the overload or short-circuit condition remains, the device runs in current limit and then shuts down again. This cycle repeats as long as the overload or short-circuit condition persists. This mode of operation reduces the temperature rise of the device during a sustained overload or short circuit condition on the output. Once the output short is removed, the output voltage recovers normally to the regulated value.

For FCCM version, the inductor current is allowed to go negative. When this current exceed the LS negative current limit ILS\_NEG, the LS switch is turned off and HS switch is turned on immediately, which is used to protect the LS switch from excessive negative current.

## 9.3.13 Thermal Shutdown

The junction temperature (TJ) of the device is monitored by an internal temperature sensor. If TJ exceeds 165°C (typical), the device goes into thermal shutdown, both the high-side and low-side power FETs are turned off. When TJ decreases below the hysteresis amount of 30°C (typical), the converter resumes normal operation, beginning with a soft start.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_024.png)

## 9.4 Device Functional Modes

## 9.4.1 Modes Overview

The TPS6293x moves between CCM, DCM, PFM, OOA and FCCM mode as the load changes. Depending on the load current, the TPS6293x is in one of below modes:

- Continuous conduction mode (CCM) with fixed switching frequency when load current is above half of the peak-to-peak inductor current ripple
- Discontinuous conduction mode (DCM) with fixed switching frequency when load current is lower than half of the peak-to-peak inductor current ripple in CCM operation
- Pulse frequency modulation mode (PFM) when switching frequency is decreased at very light load
- Out of audio (OOA) mode when switching frequency is decreased but is always above 30 kHz at very light load
- Forced continuous conduction mode (FCCM) with fixed switching frequency even at light load

## 9.4.2 Heavy Load Operation

The TPS6293x operates in continuous conduction mode (CCM) when the load current is higher than half of the peak-to-peak inductor current. In CCM operation, the output voltage is regulated by switching at a constant frequency and modulating the duty cycle to control the power to the load. Regulating the output voltage provides excellent line and load regulation and minimum output voltage ripple, and the maximum continuous output current of 2 A or 3 A can be supplied by the TPS6293x.

## 9.4.3 Light Load Operation

The TPS62932, TPS62933, and TPS62933P are designed to operate in pulse frequency modulation (PFM) mode at light load currents to boost light load efficiency.

When the load current is lower than half of the peak-to-peak inductor current in CCM, the device operates in discontinuous conduction mode (DCM), also known as diode emulation mode (DEM). In DCM operation, the LS switch is turned off when the inductor current drops to ILS\_ZC to improve efficiency. Both switching losses and conduction losses are reduced in DCM, compared to forced CCM operation at light load.

At even lighter current load, pulse frequency modulation (PFM) mode is activated to maintain high efficiency operation. When either the minimum on time, tON\_MIN, or the minimum peak inductor current, IPEAK\_MIN (750 mA typical), is reached, the switching frequency decreases to maintain regulation. In PFM mode, switching frequency is decreased by the control loop to maintain output voltage regulation when load current reduces. Switching loss is further reduced in PFM operation due to less frequent switching actions. The output current for mode change depends on the input voltage, inductor value, and the programmed switching frequency. For applications where the switching frequency must be known for a given condition, the transition between PFM and CCM must be carefully tested before the design is finalized.

## 9.4.4 Out of Audio Operation

TPS62933O implements the out of audio (OOA) mode which is a unique control feature that keeps the switching frequency above audible frequency (20 Hz to 20 kHz) even at no load condition. When operates in OOA mode, the minimum switching frequency is clamped above 30 kHz which avoids the audible noise in the system. The loading to enter OOA mode depends on output LC filter.

## 9.4.5 Forced Continuous Conduction Operation

The TPS62933F is designed to operate in forced continuous conduction mode (FCCM) under light load conditions. During FCCM, the switching frequency is maintained at a constant level over the entire load range, which is suitable for applications requiring tight control of the switching frequency and output voltage ripple at the cost of lower efficiency under light load. For some audio applications, this mode can help avoid switching frequency drop into audible range that can introduce some noise.

## 9.4.6 Dropout Operation

The dropout performance of any buck converter is affected by the RDSON of the power MOSFETs, the DC resistance of the inductor, and the maximum duty cycle that the controller can achieve. As the input voltage level

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

approaches the output voltage, the off time of the high-side MOSFET starts to approach the minimum value. Beyond this point, the switching frequency becomes erratic and the output voltage can fall out of regulation. To avoid this problem, the TPS6293x automatically reduces the switching frequency (on-time extension function) to increase the effective duty cycle and maintain in regulation until the switching frequency reach to the lowest limit of about 140 kHz, the period is equal to tON\_MAX + tOFF\_MIN (7.14 μS typical). In this condition, the difference voltage between VIN and VOUT is defined as dropout voltage. The typical overall dropout characteristics can be found as Figure 9-9.

Figure 9-9. Overall Dropout Characteristic, VOUT = 5 V

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_037.png)

## 9.4.7 Minimum On-Time Operation

Every switching converter has a minimum controllable on time dictated by the inherent delays and blanking times associated with the control circuits, which imposes a minimum switch duty cycle and, therefore, a minimum conversion ratio. The constraint is encountered at high input voltages and low output voltages. To help extend the minimum controllable duty cycle, the TPS6293x automatically reduces the switching frequency when the minimum on-time limit is reached. This way, the converter can regulate the lowest programmable output voltage at the maximum input voltage. Use Equation 13 to find an estimate for the approximate input voltage for a given output voltage before frequency foldback occurs. The values of tON\_MIN and fSW can be found in Section 8.5.

<!-- formula-not-decoded -->

As the input voltage is increased, the switch on time (duty-cycle) reduces to regulate the output voltage. When the on time reaches the minimum on time, tON\_MIN, the switching frequency drops while the on time remains fixed.

## 9.4.8 Shutdown Mode

The EN pin provides electrical ON and OFF control for the device. When VEN is below typical 1.1 V, the TPS6293x is in shutdown mode. The device also employs VIN UVLO protection. If VIN voltage is below their respective UVLO level, the converter is turned off too.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_017.png)

## 10 Application and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 10.1 Application Information

The TPS62933 is a highly integrated, synchronous, step-down, DC-DC converter. This device is used to convert a higher DC input voltage to a lower DC output voltage, with a maximum output current of 3 A.

## 10.2 Typical Application

The application schematic of Figure 10-1 was developed to meet the requirements of the device. This circuit is available as the TPS62933EVM evaluation module. The design procedure is given in this section.

Figure 10-1. TPS62933 5-V Output, 3-A Reference Design

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_038.png)

## 10.2.1 Design Requirements

Table 10-1 shows the design parameters for this application.

Table 10-1. Design Parameters

| Parameter | Parameter | Conditions | MIN | TYP | MAX | Unit |
| - | - | - | - | - | - | - |
| VIN | Input voltage |  | 5.5 | 24 | 30 | V |
| VOUT | Output voltage |  |  | 5 |  | V |
| IOUT | Output current rating |  |  | 3 |  | A |
| ΔVOUT | Transient response | Load step from 0.5 A→2.5 A→0.5 A, 0.8-A/μS slew rate |  | ±5% × VOUT |  | V |
| VIN(ripple) | Input ripple voltage |  |  | 400 |  | mV |
| VOUT(ripple) | Output ripple voltage |  |  | 30 |  | mV |
| FSW | Switching frequency | RT = floating |  | 500 |  | kHz |
| tSS | Soft-start time | CSS = 33 nF |  | 5 |  | mS |
| VSTART | Start input voltage (Rising VIN) |  |  | 8 |  | V |
| VSTOP | Stop input voltage (Falling VIN) |  |  | 7 |  | V |
| TA | Ambient temperature |  |  | 25 |  | °C |

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

[www.ti.com](https://www.ti.com/)

## 10.2.2 Detailed Design Procedure

## 10.2.2.1 Custom Design With WEBENCH® Tools

Create a custom design with the TPS6293x using the WEBENCH® Power Designer.

1. Start by entering the input voltage (VIN), output voltage (VOUT), and output current (IOUT) requirements.
2. Optimize the design for key parameters such as efficiency, footprint, and cost using the optimizer dial.
3. Compare the generated design with other possible solutions from Texas Instruments.

The WEBENCH Power Designer provides a customized schematic along with a list of materials with real-time pricing and component availability.

In most cases, these actions are available:

- Run electrical simulations to see important waveforms and circuit performance
- Run thermal simulations to understand board thermal performance
- Export customized schematic and layout into popular CAD formats
- Print PDF reports for the design, and share the design with colleagues

Get more information about WEBENCH tools at www.ti.com/WEBENCH.

## 10.2.2.2 Output Voltage Resistors Selection

The output voltage is set with a resistor divider from the output node to the FB pin. TI recommends using 1% tolerance or better divider resistors. Referring to the application schematic of Figure 10-1, start with 10.2 kΩ for R7 and use Equation 14 to calculate R6 = 53.6 kΩ. To improve efficiency at light loads, consider using larger value resistors. If the values are too high, the converter is more susceptible to noise and voltage errors from the FB input leakage current are noticeable.

<!-- formula-not-decoded -->

Table 10-2 shows the recommended components value for common output voltages.

## 10.2.2.3 Choosing Switching Frequency

The choice of switching frequency is a compromise between conversion efficiency and overall solution size. Higher switching frequency allows the use of smaller inductors and output capacitors, and hence, a more compact design. However, lower switching frequency implies reduced switching losses and usually results in higher system efficiency, so the 500-kHz switching frequency was chosen for this example, remove the jumper on JP2 and leave RT pin floating.

Please note the switching frequency is also limited by the following as mentioned in Section 9.3.9:

- Minimum on time of the integrated power switch
- Input voltage
- Output voltage
- Frequency shift limitation

## 10.2.2.4 Soft-Start Capacitor Selection

The large CSS can reduce inrush current when driving large capacitive load. 33 nF is chosen for C4, which sets the soft-start time, tSS, to approximately 5 ms.

In addition, the SS pin cannot be floated, so a minimum 6.8-nF capacitor must be connected at this pin.

## 10.2.2.5 Bootstrap Capacitor Selection

A 0.1-µF ceramic capacitor must be connected between the BST to SW pins for proper operation. TI recommends to use a ceramic capacitor with X5R or better grade dielectric. The capacitor C5 must have a 16-V or higher voltage rating.

In addition, adding one BST resistor R4 to reduce the spike voltage on the SW node, TI recommends the resistance smaller than 10 Ω be used between BST to the bootstrap capacitor.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_033.png)

## 10.2.2.6 Undervoltage Lockout Setpoint

The undervoltage lockout (UVLO) can be adjusted using the external voltage divider network of R1 and R2. R1 is connected between VIN and the EN pin and R2 is connected between EN and GND. The UVLO has two thresholds: one for power up when the input voltage is rising and one for power down or brownouts when the input voltage is falling. For the example design, the supply turns on and starts switching when the input voltage increases above 8 V (VSTART). After the converter starts switching, it continues to do so until the input voltage falls below 7 V (VSTOP). Equation 3 and Equation 4 can be used to calculate the values for the upper and lower resistor values. For the stop voltages specified, the nearest standard resistor value for R1 is 511 kΩ and for R2 is 80.7 kΩ.

## 10.2.2.7 Output Inductor Selection

The most critical parameters for the inductor are the inductance, saturation current, and the RMS current. The inductance is based on the desired peak-to-peak ripple current, ΔiL, which can be calculated by Equation 15.

<!-- formula-not-decoded -->

Usually, define K coefficient represents the amount of inductor ripple current relative to the maximum output current of the device, a reasonable value of K is 20% to 60%. Experience shows that the best value of K is 40%. Since the ripple current increases with the input voltage, the maximum input voltage is always used to calculate the minimum inductance L. Use Equation 16 to calculate the minimum value of the output inductor.

<!-- formula-not-decoded -->

where

- K is the ripple ratio of the inductor current (ΔIL / IOUT\_MAX).

In general, it is preferable to choose lower inductance in switching power supplies, because it usually corresponds to faster transient response, smaller DCR, and reduced size for more compact designs. Too low of an inductance can generate too large of an inductor current ripple such that overcurrent protection at the full load can be falsely triggered. The device also generates more inductor core loss since the current ripple is larger. Larger inductor current ripple also implies larger output voltage ripple with the same output capacitors.

After inductance L is determined, the maximum inductor peak current and RMS current can be calculated by Equation 17 and Equation 18.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Ideally, the saturation current rating of the inductor is at least as large as the high-side switch current limit, IHS\_LIMIT (see Section 8.5). This ensures that the inductor does not saturate even during a short circuit on the output. When the inductor core material saturates, the inductance falls to a very low value, causing the inductor current to rise very rapidly. Although the valley current limit, ILS\_LIMIT, is designed to reduce the risk of current runaway, a saturated inductor can cause the current to rise to high values very rapidly, this can lead to component damage, so do not allow the inductor to saturate. In any case, the inductor saturation current must not be less than the maximum peak inductor current at full load.

For this design example, choose the following values:

- K = 0.4
- VIN\_MAX = 30 V

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_015.png)

## [www.ti.com](https://www.ti.com/)

- fSW = 500 kHz
- IOUT\_MAX = 3 A

The inductor value is calculated to be 6.94 μH. Choose the nearest standard value of 6.8 μH, which gives a new K value of 0.408. The maximum IHS\_LIMIT is 5.8 A, the calculated peak current is 3.61 A, and the calculated RMS current is 3.02 A. The chosen inductor is a Würth Elektronik, 74439346068, 6.8 μH, which has a saturation current rating of 10 A and a RMS current rating of 6.5 A.

The maximum inductance is limited by the minimum current ripple required for the peak current mode control to perform correctly. To avoid subharmonic oscillation, as a rule-of-thumb, the minimum inductor ripple current must be no less than approximately 10% of the device maximum rated current (3 A) under nominal conditions.

## 10.2.2.8 Output Capacitor Selection

The device is designed to be used with a wide variety of LC filters, so it is generally desired to use as little output capacitance as possible to keep cost and size down. Choose the output capacitance, COUT, with care since it directly affects the following specifications:

- Steady state output voltage ripple
- Loop stability
- Output voltage overshoot and undershoot during load current transient

The output voltage ripple is essentially composed of two parts. One is caused by the inductor current ripple going through the Equivalent Series Resistance (ESR) of the output capacitors:

<!-- formula-not-decoded -->

The other is caused by the inductor current ripple charging and discharging the output capacitors:

<!-- formula-not-decoded -->

## where

- K is the ripple ratio of the inductor current (ΔIL / IOUT\_MAX).

The two components in the voltage ripple are not in phase, so the actual peak-to-peak ripple is smaller than the sum of the two peaks.

Output capacitance is usually limited by the load transient requirements rather than the output voltage ripple if the system requires tight voltage regulation with presence of large current steps and fast slew rate. When a large load step happens, output capacitors provide the required charge before the inductor current can slew up to the appropriate level. The control loop of the converter usually needs eight or more clock cycles to regulate the inductor current equal to the new load level. The output capacitance must be large enough to supply the current difference for about eight clock cycles to maintain the output voltage within the specified range. Equation 21 shows the minimum output capacitance needed for specified VOUT overshoot and undershoot.

<!-- formula-not-decoded -->

## where

- D is VOUT / VIN, duty cycle of steady state.
- ΔVOUT is the output voltage change.
- ΔIOUT is the output current change.

For this design example, the target output ripple is 30 mV. Presuppose ΔVOUT\_ESR = ΔVOUT\_C = 30 mV and choose K = 0.4. Equation 19 yields ESR no larger than 25 mΩ and Equation 20 yields COUT no smaller than 10 μF. For the target overshoot and undershoot limitation of this design, ΔVOUT\_SHOOT &lt; 5% × VOUT = 250 mV for an output current step of ΔIOUT = 1.5 A. COUT is calculated to be no smaller than 25 μF

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_017.png)

by Equation 21. In summary, the most stringent criterion for the output capacitor is 25 μF. Considering the ceramic capacitor has DC bias de-rating, it can be achieved with a bank of 2 × 22-μF, 35-V, ceramic capacitor C3216X5R1V226M160AC in the 1206 case size.

More output capacitors can be used to improve the load transient response. Ceramic capacitors can easily meet the minimum ESR requirements. In some cases, an aluminum electrolytic capacitor can be placed in parallel with the ceramics to build up the required value of capacitance. When using a mixture of aluminum and ceramic capacitors, use the minimum recommended value of ceramics and add aluminum electrolytic capacitors as needed.

The recommendations given in Table 10-2 provide typical and minimum values of output capacitance for the given conditions. These values are the effective figures. If the minimum values are to be used, the design must be tested over all of the expected application conditions, including input voltage, output current, and ambient temperature. This testing must include both bode plot and load transient assessments. The maximum value of total output capacitance can be referred to COUT selection and CFF selection in the TPS62933 Thermal Performance with SOT583 Package Application Report. Large values of output capacitance can adversely affect the start-up behavior of the converter as well as the loop stability. If values larger than noted here must be used, then a careful study of start-up at full load and loop stability must be performed.

In practice, the output capacitor has the most influence on the transient response and loop phase margin. Load transient testing and bode plots are the best way to validate any given design and must always be completed before the application goes into production. In addition to the required output capacitance, a small ceramic placed on the output can reduce high frequency noise. Small case size ceramic capacitors in the range of 1 nF to 100 nF can help reduce spikes on the output caused by inductor and board parasitics.

Table 10-2 shows the recommended LC combination.

Table 10-2. Recommended LC Combination for TPS62933

| VOUT(V) | fSW (kHz) | RTOP(kΩ) | RDOWN(kΩ) | Typical Inductor L (μH) | Typical Effective COUT (μF) | Minimum Effective COUT (μF) |
| - | - | - | - | - | - | - |
| 3.3 | 500 | 31.3 | 10.0 | 4.7 | 40 | 15 |
| 3.3 | 1200 | 31.3 | 10.0 | 2.2 | 30 | 10 |
| 5 | 500 | 52.5 | 10.0 | 6.8 | 20 | 10 |
| 5 | 1200 | 52.5 | 10.0 | 3.3 | 20 | 10 |
| 12 | 500 | 140.0 | 10.0 | 12 | 15 | 10 |

## 10.2.2.9 Input Capacitor Selection

The TPS6293x device requires an input decoupling capacitor and, depending on the application, a bulk input capacitor. The typical recommended value for the decoupling capacitor is 10 μF, and an additional 0.1-µF capacitor from the VIN pin to ground is recommended to provide high frequency filtering.

The value of a ceramic capacitor varies significantly over temperature and the amount of DC bias applied to the capacitor. X5R and X7R ceramic dielectrics are recommended because they have a high capacitance-to-volume ratio and are fairly stable over temperature. The capacitor must also be selected with the DC bias taken into account. The effective capacitance value decreases as the DC bias increases.

The capacitor voltage rating needs to be greater than the maximum input voltage. The capacitor must also have a ripple current rating greater than the maximum input current ripple. The input ripple current can be calculated using Equation 22.

<!-- formula-not-decoded -->

For this example design, two TDK CGA5L1X7R1H106K160AC (10-μF, 50-V, 1206, X7R) capacitors have been selected. The effective capacitance under input voltage of 24 V for each one is 3.45 μF. The input capacitance value determines the input ripple voltage of the converter. The input voltage ripple can be calculated using

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_039.png)

[www.ti.com](https://www.ti.com/)

Equation 23. Using the design example values, IOUT\_MAX = 3 A, CIN\_EFF = 2 × 3.45 = 6.9 μF, and fSW = 500 kHz, yields an input voltage ripple of 222 mV and a RMS input ripple current of 1.22 A.

<!-- formula-not-decoded -->

where

- RESR\_MAX is the maximum series resistance of the input capacitor, which is approximately 1.5 mΩ of two capacitors in paralleled.

## 10.2.2.10 Feedforward Capacitor CFF Selection

In some cases, a feedforward capacitor can be used across RFBT to improve the load transient response or improve the loop phase margin. This is especially true when values of RFBT &gt; 100 kΩ are used. Large values of RFBT in combination with the parasitic capacitance at the FB pin can create a small signal pole that interferes with the loop stability. A CFF helps mitigate this effect. Use lower values to determine if any advantage is gained by the use of a CFF capacitor.

The Optimizing Transient Response of Internally Compensated DC-DC Converters with Feedforward Capacitor Application Report is helpful when experimenting with a feedforward capacitor.

For this example design, a 10-pF capacitor C9 can be mounted to boost load transient performance.

## 10.2.2.11 Maximum Ambient Temperature

As with any power conversion device, the TPS6293x dissipates internal power while operating. The effect of this power dissipation is to raise the internal temperature of the converter above ambient. The internal die temperature (TJ) is a function of the following:

- Ambient temperature
- Power loss
- Effective thermal resistance, RθJA, of the device
- PCB combination

The maximum internal die temperature must be limited to 150°C. This establishes a limit on the maximum device power dissipation and, therefore, the load current. Equation 24 shows the relationships between the important parameters. It is easy to see that larger ambient temperatures (TA) and larger values of RθJA reduce the maximum available output current. The converter efficiency can be estimated by using the curves provided in this data sheet. Note that these curves include the power loss in the inductor. If the desired operating conditions cannot be found in one of the curves, then interpolation can be used to estimate the efficiency. Alternatively, the EVM can be adjusted to match the desired application requirements and the efficiency can be measured directly. The correct value of RθJA is more difficult to estimate. As stated in the Semiconductor and IC Package Thermal Metrics Application Report, the value of RθJA given in the Thermal Information table is not valid for design purposes and must not be used to estimate the thermal performance of the application. The values reported in that table were measured under a specific set of conditions that are rarely obtained in an actual application. The data given for RθJC(bott) and ΨJT can be useful when determining thermal performance. See the Semiconductor and IC Package Thermal Metrics Application Report for more information and the resources given at the end of this section.

<!-- formula-not-decoded -->

where

- ŋ is efficiency.

The effective RθJA is a critical parameter and depends on many factors such as the following:

- Power dissipation

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_040.png)

- Air temperature and flow
- PCB area
- Copper heat-sink area
- Number of thermal vias under the package
- Adjacent component placement

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_031.png)

## 10.2.3 Application Curves

VIN = 24 V, VOUT = 5 V, L1= 6.8 µH, COUT = 44 µF, TA = 25°C (unless otherwise noted)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_041.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_013.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_042.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_031.png)

www.ti.com SLUSEA4D - JUNE 2021 - REVISED AUGUST 2022

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_043.png)

## TPS62933, TPS62932, TPS62933F, TPS62933P, TPS62933O

SLUSEA4D - JUNE 2021 - REVISED AUGUST 2022

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_033.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_044.png)

## 10.3 What to Do and What Not to Do

- Do not exceed the Absolute Maximum Ratings.
- Do not exceed the Recommended Operating Conditions.
- Do not exceed the ESD Ratings.
- Do not allow the SS pin floating.
- Do not allow the output voltage to exceed the input voltage, nor go below ground.
- Do not use the value of RθJA given in the Thermal Information table to design your application. See Section 10.2.2.11.
- Follow all the guidelines and suggestions found in this data sheet before committing the design to production. TI application engineers are ready to help critique your design and PCB layout to help make your project a success.
- Use a 100-nF capacitor connected directly to the VIN and GND pins of the device. See Section 10.2.2.9 for details.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_045.png)

[www.ti.com](https://www.ti.com/)

## 11 Power Supply Recommendations

The devices are designed to operate from an input voltage supply range between 3.8 V and 30 V. This input supply must be well regulated and compatible with the limits found in the specifications of this data sheet. In addition, the input supply must be capable of delivering the required input current to the loaded converter. The average input current can be estimated with Equation 25.

<!-- formula-not-decoded -->

## where

- ŋ is efficiency.

If the converter is connected to the input supply through long wires or PCB traces, special care is required to achieve good performance. The parasitic inductance and resistance of the input cables can have an adverse effect on the operation of the converter. The parasitic inductance, in combination with the low-ESR, ceramic input capacitors, can form an under-damped resonant circuit, resulting in overvoltage transients at the input to the converter. The parasitic resistance can cause the voltage at the VIN pin to dip whenever a load transient is applied to the output. If the application is operating close to the minimum input voltage, this dip can cause the converter to momentarily shutdown and reset. The best way to solve these kind of issues is to reduce the distance from the input supply to the converter and use an aluminum or tantalum input capacitor in parallel with the ceramics. The moderate ESR of these types of capacitors help damp the input resonant circuit and reduce any overshoots. A value in the range of 20 μF to 100 μF is usually sufficient to provide input damping and help hold the input voltage steady during large load transients.

TI recommends that the input supply must not be allowed to fall below the output voltage by more than 0.3 V. Under such conditions, the output capacitors discharges through the body diode of the high-side power MOSFET. The resulting current can cause unpredictable behavior, and in extreme cases, possible device damage. If the application allows for this possibility, then use a Schottky diode from VIN to VOUT to provide a path around the converter for this current.

In some cases, a transient voltage suppressor (TVS) is used on the input of converters. One class of this device has a snap-back characteristic (thyristor type). The use of a device with this type of characteristic is not recommended. When the TVS fires, the clamping voltage falls to a very low value. If this voltage is less than the output voltage of the converter, the output capacitors discharges through the device, as mentioned above.

Sometimes, for other system considerations, an input filter is used in front of the converter, which can lead to instability as well as some of the effects mentioned above, unless it is designed carefully. The AN-2162 Simple Success with Conducted EMI from DCDC Converters User's Guide provides helpful suggestions when designing an input filter for any switching converter.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_046.png)

## 12 Layout

## 12.1 Layout Guidelines

The PCB layout of any DC/DC converter is critical to the optimal performance of the design. Bad PCB layout can disrupt the operation of a good schematic design. Even if the converter regulates correctly, bad PCB layout can mean the difference between a robust design and one that cannot be mass produced. Furthermore, the EMI performance of the converter is dependent on the PCB layout to a great extent. In a buck converter, the most critical PCB feature is the loop formed by the input capacitors and power ground, as shown in Figure 12-1. This loop carries large transient currents that can cause large transient voltages when reacting with the trace inductance. These unwanted transient voltages disrupt the proper operation of the converter. Because of this, the traces in this loop must be wide and short, and the loop area as small as possible to reduce the parasitic inductance.

TI recommends a 2-layer board with 2-oz copper thickness of top and bottom layer, and proper layout provides low current conduction impedance, proper shielding, and lower thermal resistance. Figure 12-2 and Figure 12-3 show the recommended layouts for the critical components of the TPS62933.

- Place the inductor, input and output capacitors, and the IC on the same layer.
- Place the input and output capacitors as close as possible to the IC. The VIN and GND traces must be as wide as possible and provide sufficient vias on them to minimize trace impedance. The wide areas are also of advantage from the view point of heat dissipation.
- Place a 0.1-µF ceramic decoupling capacitor or capacitors as close as possible to VIN and GND pins, which is key to EMI reduction.
- Keep the SW trace as physically short and wide as practical to minimize radiated emissions.
- Place a BST capacitor and resistor close to the BST pin and SW node. A &gt; 10-mil width trace is recommended to reduce the parasitic inductance.
- Place the feedback divider as close as possible to the FB pin. A &gt; 10-mil width trace is recommended for heat dissipation. Connect a separate VOUT trace to the upper feedback resistor. Place the voltage feedback loop away from the high-voltage switching trace. The voltage feedback loop preferably has ground shield.
- Place the SS capacitor and RT resistor close to the IC and routed with minimal lengths of trace. A &gt; 10-mil width trace is recommended for heat dissipation.

Figure 12-1. Current Loop With Fast Edges

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_047.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_031.png)

## 12.2 Layout Example

Figure 12-2. TPS62933 Top Layout Example

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_048.png)

Figure 12-3. TPS62933 Bottom Layout Example

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_049.png)

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_050.png)

## 13 Device and Documentation Support

## 13.1 Device Support

## 13.1.1 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

## 13.1.2 Development Support

## 13.1.2.1 Custom Design With WEBENCH® Tools

Create a custom design with the TPS6293x using the WEBENCH® Power Designer.

1. Start by entering the input voltage (VIN), output voltage (VOUT), and output current (IOUT) requirements.
2. Optimize the design for key parameters such as efficiency, footprint, and cost using the optimizer dial.
3. Compare the generated design with other possible solutions from Texas Instruments.

The WEBENCH Power Designer provides a customized schematic along with a list of materials with real-time pricing and component availability.

In most cases, these actions are available:

- Run electrical simulations to see important waveforms and circuit performance
- Run thermal simulations to understand board thermal performance
- Export customized schematic and layout into popular CAD formats
- Print PDF reports for the design, and share the design with colleagues

Get more information about WEBENCH tools at www.ti.com/WEBENCH.

## 13.2 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 13.3 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 13.4 Trademarks

TI E2E™ is a trademark of Texas Instruments.

WEBENCH® is a registered trademark of Texas Instruments.

All trademarks are the property of their respective owners.

## 13.5 Electrostatic Discharge Caution

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_051.png)

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 13.6 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_028.png)

[www.ti.com](https://www.ti.com/)

## 14 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_052.png)

ÍNSTRUMENTS

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| TPS62932DRLR | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 2932 |
| TPS62932DRLR.A | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 2932 |
| TPS62933DRLR | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 2933 |
| TPS62933DRLR.A | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 2933 |
| TPS62933FDRLR | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 933F |
| TPS62933FDRLR.A | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 933F |
| TPS62933ODRLR | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 933O |
| TPS62933ODRLR.A | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 933O |
| TPS62933PDRLR | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 933P |
| TPS62933PDRLR.A | Active | Production | SOT-5X3 (DRL) &#124; 8 | 4000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 933P |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

- (4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative INSTRUMENTS

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_053.png)

www.ti.com

## PACKAGE OPTION ADDENDUM

31-Oct-2025

and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_054.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

26-Sep-2024

## TAPE AND REEL INFORMATION

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_055.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_056.png)

## *All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| TPS62932DRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933DRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933FDRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933ODRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |
| TPS62933PDRLR | SOT-5X3 | DRL | 8 | 4000 | 180.0 | 8.4 | 2.75 | 1.9 | 0.8 | 4.0 | 8.0 | Q3 |

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_057.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

26-Sep-2024

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_058.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| TPS62932DRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0 |
| TPS62933DRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0 |
| TPS62933FDRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0 |
| TPS62933ODRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0 |
| TPS62933PDRLR | SOT-5X3 | DRL | 8 | 4000 | 210.0 | 185.0 | 35.0 |

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_059.png)

SCALE 8.0 0

## PACKAGE OUTLINE

## SOT-5X3 - 0.6 mm max height

PLASTIC SMALL OUTLINE

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_060.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, interlead flash, protrusions, or gate burrs shall not exceed 0.15 mm per side.
4. 4.Reference JEDEC Registration MO-293, Variation UDAD

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_061.png)

PLASTIC SMALL OUTLINE

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_062.png)

NOTES: (continued)

5. Publication IPC-7351 may have alternate designs.
6. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
7. Land pattern design aligns to IPC-610, Bottom Termination Component (BTC) solder joint inspection criteria.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_063.png)

## SOT-5X3 - 0.6 mm max height

PLASTIC SMALL OUTLINE

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_064.png)

SOLDER PASTE EXAMPLE

BASED ON 0.1 mm THICK STENCIL

SCALE:30X

4224486/G 11/2024

NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
9. Board assembly site may have different recommendations for stencil design.

![Image](TPS6293x%20%28TPS62932,%20TPS62933F%29%20Buck%20Datasheet%20%28SLUSEA4D%29_files/img_063.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2025, Texas Instruments Incorporated Last updated 10/2025
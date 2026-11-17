<!-- Converted from LP5912-EP Datasheet (TI SNVSC57).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_001.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_002.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_003.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_004.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_005.png)

[LP5912-EP](https://www.ti.com/product/LP5912-EP)

SNVSC57 - SEPTEMBER 2022

## LP5912-EP Enhanced Product, 500-mA, Low-Noise, Low-IQ LDO

## 1 Features

- Input voltage range: 1.6 V to 6.5 V
- Output voltage range: 0.8 V to 5.5 V
- Output current: Up to 500 mA
- Low output-voltage noise: 12 μVRMS (typ)
- PSRR at 1 kHz: 75 dB (typ)
- Output voltage tolerance (VOUT ≥ 3.3 V): ±2%
- Low IQ (enabled, no load): 30 μA (typ)
- Low dropout (VOUT ≥ 3.3 V): 95 mV (typ) at 500-mA load
- Stable with 1-µF ceramic input and output capacitors
- Thermal-overload and short-circuit protection
- Reverse current protection
- No noise bypass capacitor required
- Output automatic discharge for fast turnoff
- Power-good output with 140-µs (typ) delay
- Internal soft-start to limit inrush current
- Operating junction temperature: -55°C to +125°C
- Supports defense, aerospace, and medical applications:
- Controlled baseline
- One assembly and test site
- One fabrication site
- Extended product life cycle
- Extended product-change notification
- Product traceability

## 2 Applications

- [Surveillance systems](https://www.ti.com/SOLUTION/SURVEILLANCE-SYSTEM)
- [Inertial navigation](https://www.ti.com/SOLUTION/INERTIAL-NAVIGATION-SYSTEM-INS)
- [Land mobile radios](https://www.ti.com/SOLUTION/LAND-MOBILE-RADIO)
- [Global positioning system receivers](https://www.ti.com/SOLUTION/GLOBAL-POSITIONING-SYSTEM-RECEIVER)
- [Data concentrator units](https://www.ti.com/SOLUTION/REMOTE-DATA-CONCENTRATOR-RDC)

Simplified Schematic

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_006.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_007.png)

## 3 Description

The LP5912-EP is a low-noise, low-dropout regulator (LDO) that can supply up to 500 mA of output current. Designed to meet the requirements of RF and analog circuits, the LP5912-EP provides low noise, high PSRR, low quiescent current, and low line and load transient response. The LP5912-EP offers classleading noise performance without a noise bypass capacitor and with the ability for remote output capacitance placement.

The device is designed to work with a 1-µF input and a 1-µF output ceramic capacitor (a separate noise bypass capacitor is not required).

This device is available with fixed output voltages from 0.8 V to 5.5 V in 25-mV steps. Contact the Texas Instruments Sales office for specific voltage option requirements.

## Package Information (1)

| PART NUMBER | PACKAGE | BODY SIZE (NOM) |
| - | - | - |
| LP5912-EP | WSON (6) | 2.00 mm × 2.00 mm |

- (1) For all available packages, see the orderable addendum at the end of the data sheet.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_008.png)

## Table of Contents

| 1 Features............................................................................1 | 7.3 Feature Description...................................................16 |
| - | - |
| 2 Applications.....................................................................1 | 7.4 Device Functional Modes..........................................18 |
| 3 Description.......................................................................1 | 8 Applications and Implementation................................19 |
| 4 Revision History.............................................................. 2 | 8.1 Application Information............................................. 19 |
| 5 Pin Configuration and Functions...................................3 | 8.2 Typical Application.................................................... 19 |
| 6 Specifications.................................................................. 4 | 8.3 Power Supply Recommendations.............................23 |
| 6.1 Absolute Maximum Ratings........................................ 4 | 8.4 Layout....................................................................... 23 |
| 6.2 ESD Ratings............................................................... 4 | 9 Device and Documentation Support............................24 |
| 6.3 Recommended Operating Conditions.........................4 | 9.1 Documentation Support............................................ 24 |
| 6.4 Thermal Information....................................................4 | 9.2 Receiving Notification of Documentation Updates....24 |
| 6.5 Electrical Characteristics.............................................5 | 9.3 Support Resources................................................... 24 |
| 6.6 Output and Input Capacitors.......................................6 | 9.4 Trademarks...............................................................24 |
| 6.7 Typical Characteristics................................................7 | 10 Electrostatic Discharge Caution................................ 24 |
| 7 Detailed Description......................................................16 | 11 Glossary....................................................................... 24 |
| 7.1 Overview...................................................................16 | 12 Mechanical, Packaging, and Orderable |
| 7.2 Functional Block Diagram.........................................16 | Information.................................................................... 24 |

## 4 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

DATE

REVISION

NOTES

September 2022

*

Initial Release

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_009.png)

## 5 Pin Configuration and Functions

Figure 5-1. DRV Package, 6-Pin WSON With Thermal Pad (Top View)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_010.png)

Table 5-1. Pin Functions

| PIN - NO. | PIN - NAME | TYPE | DESCRIPTION |
| - | - | - | - |
| 1 | OUT | O | Regulated output voltage. |
| 2 | NC | - | No internal connection. Leave open, or connect to ground. |
| 3 | PG | O | Power-good indicator. Requires an external pullup resistor. |
| 4 | EN | I | Enable input. Logic high = device is on, logic low = device is off, with an internal 3-MΩ pulldown resistor. |
| 5 | GND | G | Ground. |
| 6 | IN | I | Unregulated input voltage. |
| Thermal pad | Thermal pad | - | Connect this pad to the copper area under the package to improve thermal performance. Use thermal vias to transfer heat to inner layers of the printed circuit board (PCB). Connect the thermal pad to ground, or leave floating. Do not connect the thermal pad to any potential other than ground. |

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_011.png)

## 6 Specifications

## 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted) (1) (2)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| VIN | IN pin voltage | -0.3 | 7 | V |
| VOUT | OUT pin voltage | -0.3 | 7 | V |
| VEN | EN pin voltage | -0.3 | 7 | V |
| VPG | PG pin voltage | -0.3 | 7 | V |
| TJ | Junction temperature | -55 | 150 | °C |
| PDISS | Continuous power dissipation (3) | Internally Limited | Internally Limited | W |
| Tstg | Storage temperature | -65 | 150 | °C |

- (1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.
- (2) All voltages are with respect to the potential at the GND pin.
- (3) Internal thermal shutdown circuitry protects the device from permanent damage.

## 6.2 ESD Ratings

|  |  | VALUE | UNIT |
| - | - | - | - |
| V(ESD) | Electrostatic discharge Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) Charged-device model (CDM), per JEDEC specification | ±2000 ±1000 | V |
| V(ESD) | JESD22-C101 (2) |  | V |

- (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process
- (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - |
| VIN | Input voltage | 1.6 |  | 6.5 | V |
| VOUT | Output voltage | 0.8 |  | 5.5 | V |
| VEN | EN input voltage | 0 |  | VIN | V |
| VPG | PG pin off voltage | 0 |  | 6.5 | V |
| IOUT | Output current | 0 |  | 500 | mA |
| TJ-MAX-OP | Operating junction temperature | -55 |  | 125 | °C |

## 6.4 Thermal Information

| THERMAL METRIC (1) | THERMAL METRIC (1) | LP5912-EP DRV (WSON) 6 PINS | UNIT |
| - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 75.8 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 92.6 | °C/W |
| RθJB | Junction-to-board thermal resistance | 40.0 | °C/W |
| ψJT | Junction-to-top characterization parameter | 3.3 | °C/W |
| ψJB | Junction-to-board characterization parameter | 40.0 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | 15.4 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC package thermal metrics application report.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_009.png)

## 6.5 Electrical Characteristics

VIN = VOUT(NOM) + 0.5 V or 1.6 V, whichever is greater; VEN = 1.35 V, CIN = 1 μF, COUT = 1 μF, IOUT = 1 mA (unless otherwise stated). (1) (2) (3)

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| OUTPUT VOLTAGE AND REGULATION | OUTPUT VOLTAGE AND REGULATION | OUTPUT VOLTAGE AND REGULATION | OUTPUT VOLTAGE AND REGULATION | OUTPUT VOLTAGE AND REGULATION | OUTPUT VOLTAGE AND REGULATION | OUTPUT VOLTAGE AND REGULATION |
|  | Output voltage tolerance | For VOUT(NOM) ≥ 3.3 V, VOUT(NOM) + 0.5 V ≤ VIN ≤ 6.5 V, IOUT = 1 mA to 500 mA | -2 |  | 2 | % |
| ΔVOUT | Output voltage tolerance | For 1.1 V ≤ VOUT(NOM) < 3.3 V, VOUT(NOM) + 0.5 V ≤ VIN ≤ 6.5 V, IOUT = 1 mA to 500 mA For VOUT(NOM) < 1.1 V, 1.6 V ≤ VIN ≤ 6.5 V, IOUT = 1 mA to 500 mA | -3 |  | 3 | % |
|  | Line regulation | For VOUT(NOM) ≥ 1.1V, VOUT(NOM) + 0.5 V ≤ VIN ≤ 6.5 V For VOUT(NOM) < 1.1 V, |  | 0.8 |  | %/V |
|  | Load regulation | 1.6 V ≤ VIN ≤ 6.5 V For IOUT = 1mA to 500 mA |  | 0.0022 |  | %/mA |
| CURRENT LEVELS | CURRENT LEVELS | CURRENT LEVELS | CURRENT LEVELS | CURRENT LEVELS | CURRENT LEVELS | CURRENT LEVELS |
| ISC | Short-circuit current limit | TJ = 25°C, (4) | 700 | 900 | 1100 | mA |
| IRO | Reverse leakage current (5) | VIN < VOUT |  | 10 | 150 | µA |
| IQ | Quiescent current (6) | VEN = 1.35 V, IOUT = 0 mA |  | 30 | 55 | µA |
|  |  | VEN = 1.35 V, IOUT = 500 mA |  | 400 | 600 |  |
| IQ(SD) | Quiescent current shutdown mode (6) | VEN = 0 V, -55°C ≤ TJ ≤ 85°C |  | 0.2 | 1.5 | µA |
| IQ(SD) |  | VEN = 0 V |  | 0.2 | 5 |  |
| IG | Ground-current (7) | VEN = 1.35 V, IOUT = 0 mA |  | 35 |  | µA |
| VDO DROPOUT VOLTAGE | VDO DROPOUT VOLTAGE | VDO DROPOUT VOLTAGE | VDO DROPOUT VOLTAGE | VDO DROPOUT VOLTAGE | VDO DROPOUT VOLTAGE | VDO DROPOUT VOLTAGE |
| VDO | Dropout voltage (8) | IOUT = 500 mA, 1.6 V ≤ VOUT(NOM) < 3.3 V |  | 170 | 250 | mV |
|  |  | IOUT = 500 mA, 3.3 V ≤ VOUT(NOM) ≤ 5.5 V |  | 95 | 180 | mV |
| VIN to VOUT RIPPLE REJECTION | VIN to VOUT RIPPLE REJECTION | VIN to VOUT RIPPLE REJECTION | VIN to VOUT RIPPLE REJECTION | VIN to VOUT RIPPLE REJECTION | VIN to VOUT RIPPLE REJECTION | VIN to VOUT RIPPLE REJECTION |
| PSRR | Power-supply rejection ratio (9) | f = 100 Hz, VOUT ≥ 1.1 V, IOUT = 20 mA |  | 80 |  | dB |
| PSRR |  | f = 1 kHz, VOUT ≥ 1.1 V, IOUT = 20 mA |  | 75 |  | dB |
| PSRR |  | f = 10 kHz, VOUT ≥ 1.1 V, IOUT = 20 mA |  | 65 |  | dB |
| PSRR |  | f = 100 kHz, VOUT ≥ 1.1 V, IOUT = 20 mA |  | 40 |  | dB |
| PSRR |  | f = 100 Hz, 0.8V ≤ VOUT < 1.1 V, IOUT = 20 mA |  | 65 |  | dB |
| PSRR |  | f = 1 kHz, 0.8V ≤ VOUT < 1.1 V, IOUT = 20 mA |  | 65 |  | dB |
| PSRR |  | f = 10 kHz, 0.8V ≤ VOUT < 1.1 V, IOUT = 20 mA |  | 65 |  | dB |
| PSRR |  | f = 100 kHz, 0.8V ≤ VOUT < 1.1 V, IOUT = 20 mA |  | 40 |  | dB |
| OUTPUT NOISE VOLTAGE | OUTPUT NOISE VOLTAGE | OUTPUT NOISE VOLTAGE | OUTPUT NOISE VOLTAGE | OUTPUT NOISE VOLTAGE | OUTPUT NOISE VOLTAGE | OUTPUT NOISE VOLTAGE |
| eN | Noise voltage | IOUT = 1 mA, BW = 10 Hz to 100 kHz |  | 12 |  | μVRMS |
|  |  | IOUT = 500 mA, BW = 10 Hz to 100 kHz |  | 12 |  | μVRMS |
| THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN |
| TSD | Thermal shutdown temperature |  |  | 160 |  | °C |
| THYS | Thermal shutdown hysteresis |  |  | 15 |  | °C |
| LOGIC INPUT THRESHOLDS | LOGIC INPUT THRESHOLDS | LOGIC INPUT THRESHOLDS | LOGIC INPUT THRESHOLDS | LOGIC INPUT THRESHOLDS | LOGIC INPUT THRESHOLDS | LOGIC INPUT THRESHOLDS |
| VEN(OFF) | Off threshold |  |  |  | 0.25 | V |
| VEN(ON) | On threshold |  | 1.35 |  |  | V |
| IEN | Input current at EN | VIN = 6 V, VEN = 6 V |  | 3 |  | µA |
|  | terminal (10) | VIN = 3.3 V, VEN = 0 V |  | 0.001 |  | µA |
| PGHYS | PG threshold hysteresis (% of nominal VOUT) |  |  | 4 |  | % |

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_012.png)

## 6.5 Electrical Characteristics (continued)

VIN = VOUT(NOM) + 0.5 V or 1.6 V, whichever is greater; VEN = 1.35 V, CIN = 1 μF, COUT = 1 μF, IOUT = 1 mA (unless otherwise stated). (1) (2) (3)

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| PGLTH | PG low threshold (% of nominal VOUT) |  | 86 | 90 | 93 | % |
| VOL(PG) | PG pin low-level output voltage | VOUT < PGLTH, sink current = 1 mA |  |  | 400 | mV |
| ILKG(PG) | PG pin leakage current | VOUT < PGHTH, VPG = 6 V |  |  | 1 | µA |
| TRANSITION CHARACTERISTICS | TRANSITION CHARACTERISTICS | TRANSITION CHARACTERISTICS | TRANSITION CHARACTERISTICS | TRANSITION CHARACTERISTICS | TRANSITION CHARACTERISTICS | TRANSITION CHARACTERISTICS |
| ΔVOUT | Line transients (9) | For VIN ↑ and VOUT(NOM) ≥ 1.1 V, VIN = (VOUT(NOM) + 0.5 V) to (VOUT(NOM) + 1.1 V), VIN trise = 30 µs |  |  | 1 | mV |
| ΔVOUT | Line transients (9) | For VIN ↑ and VOUT(NOM) < 1.1 V, VIN = 1.6 V to 2.2 V, VIN trise = 30 µs |  |  | 1 | mV |
| ΔVOUT | Line transients (9) | For VIN ↓ and VOUT(NOM) ≥ 1.1 V, VIN = (VOUT(NOM) + 0.5 V) to (VOUT(NOM) + 1.1 V), VIN trise = 30 µs | -1 | -1 | 1 | mV |
| ΔVOUT | Line transients (9) | For VIN ↓ and VOUT(NOM) < 1.1 V, VIN = 1.6 V to 2.2 V, VIN trise = 30 µs |  |  | 1 | mV |
| ΔVOUT | Load transients (9) | IOUT = 5 mA to 500 mA, IOUT tRISE = 10 μs | -45 | -45 | 1 | mV |
| ΔVOUT | Load transients (9) | IOUT = 500 mA to 5 mA, IOUT tFALL = 10 μs |  |  | 45 | mV |
| ΔVOUT | Overshoot on start-up (9) |  |  |  | 5 | % |
| tON | Turnon time | From VEN > VEN(ON) to VOUT = 95% of VOUT(NOM) |  | 200 |  | µs |
| OUTPUT AUTO DISCHARGE RATE | OUTPUT AUTO DISCHARGE RATE | OUTPUT AUTO DISCHARGE RATE | OUTPUT AUTO DISCHARGE RATE | OUTPUT AUTO DISCHARGE RATE | OUTPUT AUTO DISCHARGE RATE | OUTPUT AUTO DISCHARGE RATE |
| RAD | Output discharge pulldown resistance | VEN = 0 V, VIN = 3.6 V |  | 100 |  | Ω |

- (1) All voltages are with respect to the device GND pin, unless otherwise stated.
- (2) Minimum and maximum limits are specified through test, design, or statistical correlation over the junction temperature (TJ ) range of -55°C to +125°C, unless otherwise stated. Typical values represent the most likely parametric norm at TA = 25°C, and are provided for reference purposes only.
- (3) In applications where high power dissipation and poor package thermal resistance is present, the maximum ambient temperature may have to be derated. Maximum ambient temperature (TA-MAX) is dependent on the maximum operating junction temperature (TJ-MAX-OP = 125°C), the maximum power dissipation of the device in the application (PD-MAX), and the junction-to-ambient thermal resistance of the part/package in the application (RθJA), as given by the following equation: TA-MAX = TJ-MAX-OP - (RθJA × PD-MAX).
- (4) Short-circuit current (ISC) is equivalent to current limit. To minimize thermal effects during testing, ISC is measured with VOUT pulled to 100 mV below its nominal voltage.
- (5) Reverse current (IRO) is measured at the IN pin.
- (6) Quiescent current is defined here as the difference in current between the input voltage source and the load at VOUT.
- (7) Ground current is defined here as the total current flowing to ground as a result of all input voltages applied to the device (IQ + IEN).
- (8) Dropout voltage (VDO) is the voltage difference between the input and the output at which the output voltage drops to 150 mV below its nominal value when VIN = VOUT + 0.5 V. Dropout voltage is not a valid condition for output voltages less than 1.6 V as compliance with the minimum operating voltage requirement cannot be assured.
- (9) This specification is specified by design.
- (10) There is a 3-MΩ pulldown resistor between the EN pin and GND pin on the device.

## 6.6 Output and Input Capacitors

over operating free-air temperature range (unless otherwise noted)

|  | PARAMETERS | TEST CONDITIONS | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - | - |
| CIN | Input capacitance (1) | Capacitance for stability | 0.7 | 1 |  | µF |
| COUT | Output capacitance (1) | Capacitance for stability | 0.7 | 1 | 10 | µF |
| COUT_ESR | Output capacitor ESR (1) |  | 5 |  | 500 | mΩ |

- (1) This specification is verified by design.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_009.png)

## 6.7 Typical Characteristics

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_013.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_014.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_011.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_015.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_016.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_011.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_017.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_015.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_018.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_011.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_019.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_015.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_020.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_011.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_021.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_015.png)

## 6.7 Typical Characteristics (continued)

VIN = VOUT + 0.5 V, VEN = VIN, IOUT = 1 mA, CIN = 1 µF, COUT = 1 µF, and TJ = 25°C (unless otherwise noted)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_022.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_023.png)

## 7 Detailed Description

## 7.1 Overview

The LP5912-EP is a low-noise, high PSRR, low-dropout regulator (LDO) capable of sourcing a 500-mA load. The LP5912-EP can operate down to a 1.6-V input voltage and a 0.8-V output voltage. With this combination of low noise, high PSRR, and low output voltage, the device is designed to power a multitude of loads from noise-sensitive communication components to battery-powered systems.

The LP5912-EP contains several features, as shown in the Functional Block Diagram:

- Internal output resistor divider feedback
- Small size and low-noise internal protection circuit current limit
- Reverse current protection
- Current limit and inrush current protection
- Thermal shutdown
- Output auto discharge for fast turnoff
- Power-good output, with a fixed 140-µs typical delay

## 7.2 Functional Block Diagram

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_024.png)

## 7.3 Feature Description

## 7.3.1 Enable (EN)

The LP5912-EP enable (EN) pin is internally held low by a 3-MΩ resistor to GND. The EN pin voltage must be higher than the VEN(ON) threshold to ensure that the device is fully enabled under all operating conditions. The EN pin voltage must be lower than the VEN(OFF) threshold to ensure that the device is fully disabled and the automatic output discharge is activated.

When the device is disabled the output stage is disabled, the PG output pin is low, and the output automatic discharge is on.

## 7.3.2 Output Automatic Discharge (RAD)

The LP5912-EP output employs an internal 100-Ω (typical) pulldown resistance to discharge the output when the EN pin is low. If the LP5912-EP EN pin is low (the device is off) and the OUT pin is held high by a secondary supply, current flows from the secondary supply through the automatic discharge pulldown resistor to ground.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_025.png)

[www.ti.com](https://www.ti.com/)

## 7.3.3 Reverse Current Protection (IRO)

The LP5912-EP input is protected against reverse current when the output voltage is higher than the input voltage. In the event that extra output capacitance is used at the output, a power-down transient at the input normally causes a large reverse current through a conventional regulator. The LP5912-EP includes a reverse voltage detector that trips when VIN drops below VOUT, shutting off the regulator and opening the p-channel metal-oxide-semiconductor field effect transistor (PMOS) body diode connection, preventing any reverse current from the OUT pin from flowing to the IN pin.

If the LP5912-EP EN pin is low (the LP5912-EP is off) and the OUT pin is held high by a secondary supply, current flows from the secondary supply through the automatic discharge pulldown resistor to ground. This scenario is not reverse current, but is instead automatic discharge pulldown current.

Reverse current (IRO) is measured at the IN pin.

## 7.3.4 Internal Current Limit (ISC)

The internal current limit circuit protects the LDO against high-load current faults or shorting events. The LDO is not designed to operate continuously at the ISC current limit. During a current-limit event, the LDO sources constant current. Therefore, the output voltage falls when load impedance decreases. If a current limit occurs and the resulting output voltage is low, excessive power may be dissipated across the LDO, resulting in a thermal shutdown of the output.

## 7.3.5 Thermal Overload Protection (TSD)

Thermal shutdown disables the output when the junction temperature rises to approximately 160°C, which allows the device to cool. When the junction temperature cools to approximately 145°C, the output circuitry enables. Based on power dissipation, thermal resistance, and ambient temperature, the thermal protection circuit may cycle on and off. This thermal cycling limits the dissipation of the regulator, thus protecting the regulator from damage as a result of overheating.

## 7.3.6 Power-Good Output (PG)

The LP5912-EP has a power-good function that works by toggling the state of the PG output pin. When the output voltage falls below the PG threshold voltage (PGLTH), the PG pin open-drain output engages (low impedance to GND). When the output voltage rises above the PG threshold voltage (PGVHTH), the PG pin becomes high impedance. By connecting a pullup resistor to an external supply, any downstream device can receive PG as a logic signal. Make sure that the external pullup supply voltage results in a valid logic signal for the receiving device or devices. Use a pullup resistor from 10 kΩ to 100 kΩ for best results.

The input supply, VIN, must be no less than the minimum operating voltage of 1.6 V to ensure that the PG pin output status is valid. The PG pin output status is undefined when VIN is less than 1.6 V.

In the power-good function, the PG output pin being pulled high is typically delayed 140 µs after the output voltage rises above the PGHTH threshold voltage. If the output voltage rises above the PGHTH threshold and then falls below the PGLTH threshold voltage, the PG pin falls immediately with no delay time.

If the PG function is not needed, the pullup resistor can be eliminated, and the PG pin can be either connected to ground or left floating.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_026.png)

## 7.4 Device Functional Modes

## 7.4.1 Enable (EN)

The LP5912-EP EN pin is internally held low by a 3-MΩ resistor to GND. The EN pin voltage must be higher than the VEN(ON) threshold to ensure that the device is fully enabled under all operating conditions. When the EN pin voltage is lower than the VEN(OFF) threshold, the output stage is disabled, the PG pin goes low, and the output automatic discharge circuit is activated. Any charge on the OUT pin is discharged to ground through the internal 100-Ω (typical) output auto discharge pulldown resistance.

## 7.4.2 Minimum Operating Input Voltage (VIN)

The LP5912-EP does not include a dedicated undervoltage lockout (UVLO) circuit. The device internal circuit is not fully functional until VIN is at least 1.6 V. The output voltage is not regulated until VIN has reached at least the greater of 1.6 V or (VOUT + VDO).

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_009.png)

## 8 Applications and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 8.1 Application Information

The LP5912-EP is designed to meet the requirements of RF and analog circuits by providing low noise, high PSRR, low quiescent current, and low line or load transient response. The device offers excellent noise performance without the need for a noise bypass capacitor and is stable with input and output capacitors with a value of 1 μF. The device delivers this performance in an industry standard WSON package, which for this device is specified with an operating junction temperature (TJ) of -55°C to +125°C.

## 8.2 Typical Application

Figure 8-1 shows a typical application circuit for the LP5912-EP. Input and output capacitances may need to be increased above the 1-μF minimum for some applications.

Figure 8-1. LP5912-EP Typical Application

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_027.png)

## 8.2.1 Design Requirements

Use the parameters listed in Table 8-1 for typical RF linear regulator applications.

Table 8-1. Design Parameters

| DESIGN PARAMETER | EXAMPLE VALUE |
| - | - |
| Input voltage | 1.6 V to 6.5 V |
| Output voltage | 0.8 V to 5.5 V |
| Output current | 500 mA |
| Output capacitor | 1 µF to 10 µF |
| Input and output capacitor ESR range | 5 mΩ to 500 mΩ |

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_028.png)

## 8.2.2 Detailed Design Procedure

## 8.2.2.1 External Capacitors

As with most low-dropout regulators, the LP5912-EP requires external capacitors for regulator stability. The device is specifically designed for portable applications requiring minimum board space and the smallest possible components. These capacitors must be correctly selected for good performance.

## 8.2.2.2 Input Capacitor

An input capacitor is required for stability. The input capacitor must be at least equal to, or greater than, the output capacitor for good load-transient performance. A capacitor of at least 1 µF must be connected between the LP5912-EP IN pin and ground for stable operation over full load-current range. Having more output than input capacitance is acceptable, as long as the input is at least 1 µF.

The input capacitor must be located no more than 1 cm from the input pin and returned to a clean analog ground. Any good-quality ceramic, tantalum, or film capacitor can be used at the input.

## Note

To ensure stable operation, good PCB practices must be employed to minimize ground impedance and keep input inductance low. If these conditions cannot be met, or if long leads connect the battery or other power source to the LP5912-EP, increase the value of the input capacitor to at least 10 µF. Also, tantalum capacitors can suffer catastrophic failures resulting from surge current when connected to a low-impedance source of power (such as a battery or a very large capacitor). If a tantalum capacitor is used at the input, the capacitor must be verified by the manufacturer to have a surge current rating sufficient for the application. There are no requirements for the equivalent series resistance (ESR) on the input capacitor, but tolerance and temperature coefficient must be considered when selecting the capacitor to ensure the capacitance remains at 1 μF ±30% over the entire operating temperature range.

## 8.2.2.3 Output Capacitor

The LP5912-EP is designed specifically to work with a very small ceramic output capacitor, typically 1 µF. Use a ceramic capacitor (dielectric types of X5R or X7R) in the 1-µF to 10-µF range, and with an ESR from 5 mΩ to 500 mΩ, in the LP5912-EP application circuit. For this device, the output capacitor must be connected between the OUT pin with a good connection back to the GND pin.

Tantalum or film capacitors can also be used at the device output, VOUT, but these components are not as attractive for reasons of size and cost (see the Capacitor Characteristics section).

The output capacitor must meet the requirement for the minimum value of capacitance and have an ESR value that is within the range of 5 mΩ to 500 mΩ for stability.

## 8.2.2.4 Capacitor Characteristics

The LP5912-EP is designed to work with ceramic capacitors on the input and output to take advantage of the benefits they offer. For capacitance values in the range of 1 µF to 10 µF, ceramic capacitors are the smallest, least expensive, and have the lowest ESR values, thus making them best for eliminating high-frequency noise. The ESR of a typical 1-µF ceramic capacitor is in the range of 20 mΩ to 40 mΩ, which easily meets the ESR stability requirement for the LP5912-EP.

The preferred choice for temperature coefficient in a ceramic capacitor is X7R. This type of capacitor is the most stable and holds the capacitance within ±15% over the temperature range. Tantalum capacitors are less desirable than ceramic for use as output capacitors because they are more expensive when comparing equivalent capacitance and voltage ratings in the 1-µF to 10-µF range.

Another important consideration is that tantalum capacitors have higher ESR values than equivalent size ceramics. Although a tantalum capacitor can possibly be found with an ESR value within the stable range, low ESR tantalum capacitors are offered with larger capacitance (which means bigger and more costly) than a www.ti.com ceramic capacitor with the same ESR value. Also, the ESR of a typical tantalum increases at approximately 2:1 as the temperature goes from 25°C down to -40°C, so some guard band must be allowed.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_029.png)

## 8.2.2.5 Remote Capacitor Operation

To ensure stability, the LP5912-EP requires at least a 1-μF capacitor at the OUT pin. There is no strict requirement for the location of the output capacitor in regards to the LDO OUT pin; the output capacitor can be located 5 cm to 10 cm away from the LDO. This flexibility means that there is no need to have a special capacitor close to the OUT pin if there are already respective capacitors in the system. This placement flexibility requires that the output capacitor be connected directly between the LP5912-EP OUT pin and GND pin with no vias. This remote capacitor feature can help designers minimize the number of capacitors in the system.

As a good design practice, keep the wiring parasitic inductance at a minimum. Thus, use traces that are as wide as possible from the LDO output to the capacitors, keeping the LDO output trace layer as close to ground layer as possible and avoiding vias on the path. If there is a need to use vias, implement as many vias as possible between the connection layers. Keep parasitic wiring inductance less than 35 nH. For applications with fast load transients, use an input capacitor equal to (or larger than) the sum of the capacitance at the output node for the best load-transient performance.

## 8.2.2.6 Power Dissipation

Knowing the device power dissipation and proper sizing of the thermal plane connected to the tab or pad is critical to ensuring reliable operation. Device power dissipation can be calculated with Equation 1, and depends on input voltage, output voltage, and load conditions of the design.

<!-- formula-not-decoded -->

Power dissipation can be minimized, and greater efficiency can be achieved, by using the lowest available voltage drop option that is greater than the dropout voltage (VDO). However, keep in mind that higher voltage drops result in better dynamic (that is, PSRR and transient) performance.

On the WSON (DRV) package, the primary conduction path for heat is through the exposed power pad into the PCB. To ensure the device does not overheat, connect the exposed pad (through thermal vias) to an internal ground plane with an appropriate amount of copper PCB area.

According to Equation 2 or Equation 3, power dissipation and junction temperature are most often related by the junction-to-ambient thermal resistance (RθJA) of the combined PCB and device package and the temperature of the ambient air (TA):

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Unfortunately, this RθJA is highly dependent on the heat-spreading capability of the particular PCB design, and therefore varies according to the total copper area, copper weight, and location of the planes. The RθJA recorded in the Thermal Information table is determined by the specific EIA/JEDEC JESD51-7 standard for PCB and copper-spreading area, and is to be used only as a relative measure of package thermal performance. For a well-designed thermal layout, RθJA is actually the sum of the package junction-to-case (bottom) thermal resistance (RθJCbot) plus the thermal resistance contribution by the PCB copper area acting as a heat sink.

## 8.2.2.7 Estimating Junction Temperature

The EIA/JEDEC standard recommends the use of psi (Ψ) thermal characteristics to estimate the junction temperatures of surface-mount devices on a typical PCB board application. These characteristics are not true thermal resistance values, but rather package-specific thermal characteristics that offer practical and relative means of estimating junction temperatures. These psi metrics are determined to be significantly independent of copper-spreading area. The key thermal characteristics (ΨJT and ΨJB) are used in accordance with Equation 4 or Equation 5 and are given in the Thermal Information table.

<!-- formula-not-decoded -->

## where:

- PD(MAX) is explained in Equation 3
- TTOP is the temperature measured at the center-top of the device package

<!-- formula-not-decoded -->

## where:

- PD(MAX) is explained in the Power Dissipation section
- TBOARD is the PCB surface temperature measured 1 mm from the device package and centered on the package edge

For more information about the thermal characteristics ΨJT and ΨJB, see the Semiconductor and IC Package Thermal Metrics application note; for more information about measuring TTOP and TBOARD, see the Using New Thermal Metrics application note; and for more information about the EIA/JEDEC JESD51 PCB used for validating RθJA, see the Thermal Characteristics of Linear and Logic Packages Using JEDEC PCB Designs application note. These application notes are available at www.ti.com.

## 8.2.3 Application Curves

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_030.png)

VIN = 2.3 V, IOUT = 500 mA (3.6 Ω), COUT = 1 µF

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_031.png)

Figure 8-3. LP5912-1.8 VOUT vs VEN (Off)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_032.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_009.png)

## 8.3 Power Supply Recommendations

This device is designed to operate from an input supply voltage range of 1.6 V to 6.5 V. The input supply must be well regulated and free of spurious noise. To ensure that the LP5912-EP output voltage is well regulated and dynamic performance is optimum, the input supply must be at least VOUT + 0.5 V. A minimum capacitor value of 1 µF is required to be within 1 cm of the IN pin.

## 8.4 Layout

## 8.4.1 Layout Guidelines

The dynamic performance of the LP5912-EP is dependent on the layout of the PCB. PCB layout practices that are adequate for typical LDOs can degrade the PSRR, noise, or transient performance of the LP5912-EP.

Best performance is achieved by placing CIN and COUT on the same side of the PCB as the LP5912-EP, and as close to the package as practical. The ground connections for CIN and COUT must route back to the LP5912-EP ground pin using as wide and as short of a copper trace as practical.

Connections using long trace lengths, narrow trace widths, or connections through vias must be avoided. Such connections add parasitic inductances and resistance that result in inferior performance, especially during transient conditions.

## 8.4.2 Layout Example

Figure 8-4. LP5912-EP Layout Example

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_033.png)

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_034.png)

## 9 Device and Documentation Support

## 9.1 Documentation Support

## 9.1.1 Related Documentation

For additional information, see the following:

- [Texas Instruments, AN1187 Leadless Leadframe Package (LLP) application note](https://www.ti.com/lit/pdf/SNOA401)
- [Texas Instruments, Semiconductor and IC Package Thermal Metrics application report](https://www.ti.com/lit/pdf/SPRA953)
- [Texas Instruments, Using New Thermal Metrics application report](https://www.ti.com/lit/pdf/SBVA025)
- Texas Instruments, Thermal Characteristics of Linear and Logic Packages Using JEDEC PCB Designs application report

## 9.2 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 9.3 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 9.4 Trademarks

TI E2E™ is a trademark of Texas Instruments.

All trademarks are the property of their respective owners.

## 10 Electrostatic Discharge Caution

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_035.png)

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 11 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

## 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_036.png)

www.ti.com

26-Feb-2026

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| LP591209MDRVREP | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 2VC5 |
| LP591212MDRVREP | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MB |
| LP591218MDRVREP | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MD |
| LP591225MDRVREP | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 2VD5 |
| LP591230MDRVREP | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MG |
| LP591233MDRVREP | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MF |
| LP591250MDRVREP | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 2VE5 |
| V62/22601-01XE | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | - | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 2VC5 |
| V62/22601-04XE | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MB |
| V62/22601-06XE | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MD |
| V62/22601-07XE | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 2VD5 |
| V62/22601-09XE | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MG |
| V62/22601-10XE | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 12MF |
| V62/22601-11XE | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -55 to 125 | 2VE5 |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_037.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

26-Feb-2026

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

## OTHER QUALIFIED VERSIONS OF LP5912-EP :

- Catalog : LP5912

- Automotive : LP5912-Q1

## NOTE: Qualified Version Definitions:

- Catalog - TI's standard catalog product

- Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_038.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

18-Nov-2022

## TAPE AND REEL INFORMATION

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_039.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_040.png)

## *All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| LP591209MDRVREP | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| LP591212MDRVREP | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| LP591218MDRVREP | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| LP591225MDRVREP | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| LP591230MDRVREP | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| LP591233MDRVREP | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| LP591250MDRVREP | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_038.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

18-Nov-2022

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_041.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| LP591209MDRVREP | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LP591212MDRVREP | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LP591218MDRVREP | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LP591225MDRVREP | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LP591230MDRVREP | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LP591233MDRVREP | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LP591250MDRVREP | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |

PLASTIC SMALL OUTLINE - NO LEAD

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_042.png)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_043.png)

INSTRUMENTS

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_044.png)

## WSON - 0.8 mm max height

SCALE 5.50

PLASTIC SMALL OUTLINE - NO LEAD

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_045.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
4. Minimum 0.1 mm solder wetting on pin side wall. Available for wettable flank version only.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_046.png)

PLASTIC SMALL OUTLINE - NO LEAD

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_047.png)

NOTES: (continued)

5. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
6. Vias are optional depending on application, refer to device data sheet. If some or all are implemented, recommended via locations are shown.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_048.png)

## WSON - 0.8 mm max height

PLASTIC SMALL OUTLINE - NO LEAD

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_049.png)

## SOLDER PASTE EXAMPLE

BASED ON 0.125 mm THICK STENCIL

EXPOSED PAD #7 88% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE SCALE:30X

4222173/C 11/2025

NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

![Image](LP5912-EP%20Datasheet%20%28TI%20SNVSC57%29_files/img_048.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2026, Texas Instruments Incorporated Last updated 10/2025
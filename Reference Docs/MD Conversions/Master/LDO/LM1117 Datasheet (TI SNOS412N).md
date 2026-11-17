<!-- Converted from LM1117 Datasheet (TI SNOS412N).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_001.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_002.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_003.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_004.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_005.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_006.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_007.png)

[LM1117](http://www.ti.com/product/lm1117?qgpn=lm1117)

SNOS412N -FEBRUARY 2000-REVISED JANUARY 2016

## LM1117 800-mA Low-Dropout Linear Regulator

## 1 Features

## 3 Description

- 1 · Available in 1.8 V, 2.5 V, 3.3 V, 5 V, and Adjustable Versions
- Space-Saving SOT-223 and WSON Packages
- Current Limiting and Thermal Protection
- Output Current 800 mA
- Line Regulation 0.2% (Maximum)
- Load Regulation 0.4% (Maximum)
- Temperature Range
- LM1117: 0°C to 125°C
- LM1117I: -40°C to 125°C

## 2 Applications

- Post Regulator for Switching DC-DC Converter
- High Efficiency Linear Regulators
- Battery Chargers
- Portable Instrumentation
- Active SCSI Termination Regulator

The LM1117 is a low dropout voltage regulator with a dropout of 1.2 V at 800 mA of load current.

The LM1117 is available in an adjustable version, which can set the output voltage from 1.25 to 13.8 V with only two external resistors. In addition, it is available in five fixed voltages, 1.8 V, 2.5 V, 3.3 V, and 5 V.

The LM1117 offers current limiting and thermal shutdown. Its circuit includes a Zener trimmed bandgap reference to assure output voltage accuracy to within ±1%.

A minimum of 10-µF tantalum capacitor is required at the output to improve the transient response and stability.

## Device Information (1)

| PART NUMBER | PACKAGE | BODY SIZE (NOM) |
| - | - | - |
| LM1117, LM1117I | SOT-223 (4) | 6.50 mm × 3.50 mm |
| LM1117, LM1117I | TO-220 (3) | 14.986 mm × 10.16 mm |
| LM1117, LM1117I | TO-252 (3) | 6.58 mm × 6.10 mm |
| LM1117, LM1117I | WSON (8) | 4.00 mm × 4.00 mm |
| LM1117, LM1117I | TO-263 (3) | 10.18 mm × 8.41 mm |

- (1) For all available packages, see the orderable addendum at the end of the data sheet.

## Adjustable Output Regulator

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_008.png)

*CAdj is optional, however it will improve ripple rejection.

1

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_009.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

ÎNSTRUMENTS

## Table of Contents

| 1 | Features .................................................................. 1 |  | 7.3 Feature Description................................................. | 11 |
| - | - | - | - | - |
| 2 | Applications ........................................................... 1 |  | 7.4 Device Functional Modes........................................ | 12 |
| 3 | Description ............................................................. 1 | 8 | Application and Implementation ........................ | 14 |
| 4 | Revision History..................................................... 2 |  | 8.1 Application Information............................................ | 14 |
| 5 | Pin Configuration and Functions ......................... 3 |  | 8.2 Typical Application .................................................. | 14 |
| 6 | Specifications......................................................... 4 |  | 8.3 System Examples ................................................... | 16 |
| 6.1 | Absolute Maximum Ratings ...................................... 4 | 9 | Power Supply Recommendations...................... | 17 |
| 6.2 | ESD Ratings.............................................................. 4 | 10 | Layout................................................................... | 17 |
| 6.3 | Recommended Operating Conditions....................... 4 |  | 10.1 Layout Guidelines ................................................. | 17 |
|  | Thermal Information.................................................. 4 |  | 10.2 Layout Example .................................................... | 21 |
| 6.4 6.5 | LM1117 Electrical Characteristics............................. 5 | 11 | Device and Documentation Support ................. | 22 |
| 6.6 | LM1117I Electrical Characteristics............................ 7 |  | 11.1 Community Resources.......................................... | 22 |
| 6.7 | Typical Characteristics.............................................. 9 |  | 11.2 Trademarks ........................................................... | 22 |
| 7 | Detailed Description ............................................ 11 |  | 11.3 Electrostatic Discharge Caution............................ | 22 |
| 7.1 | Overview ................................................................. 11 |  | 11.4 Glossary ................................................................ | 22 |
| 7.2 | Functional Block Diagram ....................................... 11 | 12 | Mechanical, Packaging, and Orderable Information ........................................................... | 22 |
| 4 Revision History | 4 Revision History | 4 Revision History | 4 Revision History | 4 Revision History |
| NOTE: Page Changes from | numbers for previous revisions may differ from Revision M (March 2013) to Revision N | numbers | in the current version. | Page |
| Added Pin Configuration and Functions section, ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information section .............................. Removed LM1117-N-2.85 option after part became inactive................................................................................................. | Added Pin Configuration and Functions section, ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information section .............................. Removed LM1117-N-2.85 option after part became inactive................................................................................................. | Added Pin Configuration and Functions section, ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information section .............................. Removed LM1117-N-2.85 option after part became inactive................................................................................................. | Added Pin Configuration and Functions section, ESD Ratings table, Feature Description section, Device Functional Modes, Application and Implementation section, Power Supply Recommendations section, Layout section, Device and Documentation Support section, and Mechanical, Packaging, and Orderable Information section .............................. Removed LM1117-N-2.85 option after part became inactive................................................................................................. | 1 1 3 |
| · Changes from Revision L (July 2012) to Revision M Changed | layout of National Data Sheet to TI format | · Changes from Revision L (July 2012) to Revision M Changed | ........................................................................................................... | Page 16 |
| Removed TO-263 Pinout Side View image ........................................................................................................................... | Removed TO-263 Pinout Side View image ........................................................................................................................... | Removed TO-263 Pinout Side View image ........................................................................................................................... | Removed TO-263 Pinout Side View image ........................................................................................................................... |  |

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

ÎNSTRUMENTS

## 5 Pin Configuration and Functions

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_012.png)

When using the WSON package

Pins 2, 3 and 4 must be connected together and

Pins 5, 6 and 7 must be connected together

## Pin Functions

| PIN | PIN | PIN | PIN | PIN | PIN | I/O |  |
| - | - | - | - | - | - | - | - |
| NAME | TO-252 | WSON | SOT-223 | TO-263 | TO-220 | I/O | DESCRIPTION |
| ADJ/GND | 1 | 1 | 1 | 1 | 1 | - | Adjust pin for adjustable output option. Ground pin for fixed output option. |
| VIN | 3 | 2, 3, 4 | 3 | 3 | 3 | I | Input voltage pin for the regulator |
| VOUT | 2 , TAB | 5, 6, 7, TAB | 2, 4 | 2, TAB | 2, TAB | O | Output voltage pin for the regulator |

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

ÎNSTRUMENTS

## 6 Specifications

## 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted) (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Maximum Input Voltage (VIN to GND) | Maximum Input Voltage (VIN to GND) |  | 20 | V |
| Power Dissipation (2) | Power Dissipation (2) | Internally Limited | Internally Limited |  |
| Junction Temperature (TJ) (2) | Junction Temperature (TJ) (2) |  | 150 | °C |
| Lead Temperature | TO-220 (T) Package, 10 s |  | 260 | °C |
| Lead Temperature | SOT-223 (MP) Package, 4 s |  | 260 | °C |
| Storage Temperature, Tstg | Storage Temperature, Tstg | -65 | 150 | °C |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

(2) The maximum power dissipation is a function of TJ(max) , RθJA, and TA. The maximum allowable power dissipation at any ambient temperature is PD = (TJ(max)-TA)/RθJA. All numbers apply for packages soldered directly into a PCB.

## 6.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| - | - | - | - | - |
| V(ESD) | Electrostatic discharge | Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) | ±2000 | V |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. Pins listed as ±2000 V may actually have higher performance.

## 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Input Voltage (VIN to GND) |  |  | 15 | V |
| Junction Temperature (TJ) (1) | LM1117 | 0 | 125 | °C |
| Junction Temperature (TJ) (1) | LM1117I | -40 | 125 | °C |

(1) The maximum power dissipation is a function of TJ(max) , RθJA, and TA. The maximum allowable power dissipation at any ambient temperature is PD = (TJ(max)-TA)/RθJA. All numbers apply for packages soldered directly into a PCB.

## 6.4 Thermal Information

|  |  | LM1117, LM1117I | LM1117, LM1117I | LM1117, LM1117I | LM1117, LM1117I | LM1117, LM1117I |  |
| - | - | - | - | - | - | - | - |
|  | THERMAL METRIC (1) | DCY (SOT-223) | NDE (TO-220) | NDP (TO-252) | NGN (WSON) | KTT (TO-263) | UNIT |
|  |  | 4 PINS | 3 PINS | 3 PINS | 8 PINS | 3 PINS |  |
| RθJA | Junction-to-ambient thermal resistance | 61.6 | 23.8 | 45.1 | 39.3 | 41.3 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 42.5 | 16.6 | 52.1 | 31.4 | 44.1 | °C/W |
| RθJB | Junction-to-board thermal resistance | 10.4 | 5.3 | 29.8 | 16.5 | 24.2 | °C/W |
| ψJT | Junction-to-top characterization parameter | 2.9 | 3.1 | 4.5 | 0.3 | 10.9 | °C/W |
| ψJB | Junction-to-board characterization parameter | 10.3 | 5.3 | 29.4 | 16.7 | 23.2 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | - | 1.5 | 1.3 | 5.6 | 1.3 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report, SPRA953.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

ÎNSTRUMENTS

## [www.ti.com](http://www.ti.com/)

## 6.5 LM1117 Electrical Characteristics

unless otherwise specified, TJ = 25°C.

|  | PARAMETER | TEST CONDITIONS | TEST CONDITIONS | MIN (1) | TYP (2) | MAX (1) | UNIT |
| - | - | - | - | - | - | - | - |
|  |  | LM1117-ADJ IOUT = 10 mA, VIN - VOUT = 2 V, TJ = 25°C | LM1117-ADJ IOUT = 10 mA, VIN - VOUT = 2 V, TJ = 25°C | 1.238 | 1.25 | 1.262 |  |
| VREF | Reference Voltage | LM1117-ADJ | TJ = 25°C |  | 1.25 |  | V |
|  |  | 10 mA ≤ IOUT ≤ 800 mA, 1.4 V ≤ VIN - VOUT ≤ 10 V | over the junction temperature range 0°C to 125°C | 1.225 |  | 1.27 |  |
|  |  | LM1117-1.8 IOUT = 10 mA, VIN = 3.8 V, TJ = 25°C | LM1117-1.8 IOUT = 10 mA, VIN = 3.8 V, TJ = 25°C | 1.782 | 1.8 | 1.818 |  |
|  |  | LM1117-1.8 | TJ = 25°C |  | 1.8 |  | V |
|  |  | 0 ≤ IOUT ≤ 800 mA, 3.2 V ≤ VIN ≤ 10 V | over the junction temperature range 0°C to 125°C | 1.746 |  | 1.854 |  |
|  |  | LM1117-2.5 IOUT = 10 mA, VIN = 4.5 V, TJ = 25°C | LM1117-2.5 IOUT = 10 mA, VIN = 4.5 V, TJ = 25°C | 2.475 | 2.5 | 2.525 |  |
|  |  | LM1117-2.5 | TJ = 25°C |  | 2.5 |  | V |
|  |  | 0 ≤ IOUT ≤ 800 mA, 3.9 V ≤ VIN ≤ 10 V | over the junction temperature range 0°C to 125°C | 2.45 |  | 2.55 |  |
| VOUT | Output Voltage | LM1117-3.3 IOUT = 10 mA, VIN = 5 V TJ = 25°C | LM1117-3.3 IOUT = 10 mA, VIN = 5 V TJ = 25°C | 3.267 | 3.3 | 3.333 |  |
|  |  |  | TJ = 25°C |  | 3.3 |  | V |
|  |  | LM1117-3.3 0 ≤ IOUT ≤ 800 mA, 4.75 V ≤ VIN ≤ 10 V | over the junction temperature range 0°C to 125°C | 3.235 |  | 3.365 |  |
|  |  | LM1117-5.0 IOUT = 10 mA, VIN = 7 V, TJ = 25°C | LM1117-5.0 IOUT = 10 mA, VIN = 7 V, TJ = 25°C | 4.95 | 5 | 5.05 |  |
|  |  |  | TJ = |  | 5 |  | V |
|  |  | LM1117-5.0 0 ≤ IOUT ≤ 800 mA, 6.5 V ≤ VIN ≤ 12 V | 25°C over the junction temperature range | 4.9 |  | 5.1 |  |
|  |  | LM1117-ADJ IOUT = 10mA, 1.5V ≤ VIN-VOUT ≤ | 0°C to 125°C TJ = 25°C |  | 0.035% |  |  |
|  |  | 13.75V | over the junction temperature range 0°C to 125°C |  |  | 0.2% |  |
|  |  |  | 25°C |  | 1 |  |  |
|  |  | LM1117-1.8 IOUT = 0 mA, 3.2 V ≤ VIN ≤ 10 V | TJ = over the junction temperature range 0°C to 125°C |  |  | 6 | mV |
|  |  |  | TJ = 25°C junction temperature |  | 1 | 6 | mV |
| ΔVOUT | Line Regulation (3) | LM1117-2.5 IOUT = 0 mA, 3.9 V ≤ VIN ≤ 10 V | over the range 0°C to 125°C |  |  |  |  |
|  |  | LM1117-3.3 | TJ = 25°C |  | 1 |  | mV |
|  |  | IOUT = 0 mA, 4.75 V ≤ VIN ≤ 15 V | over the junction temperature range 0°C to 125°C |  | 1 | 6 |  |
|  |  | LM1117-5.0 IOUT = 0 mA, 6.5 V ≤ VIN ≤ 15 V | TJ = 25°C over the junction temperature range |  |  | 10 | mV |
|  |  |  | 0°C to 125°C |  | 0.2% |  |  |
|  |  | LM1117-ADJ | TJ = 25°C range |  |  |  |  |
|  |  | VIN - VOUT = 3 V, 10 ≤ IOUT ≤ mA | 800 over the junction temperature 0°C to 125°C |  | 1 | 0.4% |  |
|  |  | LM1117-1.8 | TJ = 25°C |  |  |  |  |
|  |  | VIN = 3.2 V, 0 ≤ IOUT ≤ 800 mA | over the junction temperature range 0°C to 125°C |  |  | 10 | mV |
|  |  | LM1117-2.5 | TJ = 25°C |  | 1 |  | mV |
| ΔVOUT | Load Regulation (3) | VIN = 3.9 V, 0 ≤ IOUT ≤ 800 mA | over the junction temperature range 0°C to 125°C |  |  | 10 |  |
|  |  | LM1117-3.3 VIN = 4.75 V, 0 ≤ IOUT ≤ 800 mA | TJ = 25°C over the junction temperature range 0°C to 125°C |  | 1 | 10 | mV |
|  |  |  | TJ = 25°C |  | 1 |  |  |
|  |  | LM1117-5.0 VIN = 6.5 V, 0 ≤ IOUT ≤ 800 mA | over the junction temperature range 0°C to 125°C |  |  | 15 | mV |

(1) All limits are ensured by testing or statistical analysis.

(2) Typical Values represent the most likely parametric normal.

(3) Load and line regulation are measured at constant junction room temperature.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

ÎNSTRUMENTS

## LM1117 Electrical Characteristics (continued)

unless otherwise specified, TJ = 25°C.

|  | PARAMETER | TEST CONDITIONS | TEST CONDITIONS | MIN (1) | TYP (2) | MAX (1) | UNIT |
| - | - | - | - | - | - | - | - |
|  |  |  | TJ = 25°C |  | 1.1 |  |  |
|  |  | IOUT = 100 mA | over the junction temperature range 0°C to 125°C |  |  | 1.2 | V |
|  |  |  | TJ = 25°C |  | 1.15 |  |  |
| VIN - V OUT | Dropout Voltage (4) | IOUT = 500 mA | over the junction temperature range 0°C to 125°C |  |  | 1.25 | V |
|  |  |  | TJ = 25°C |  | 1.2 |  |  |
|  |  | IOUT = 800 mA | over the junction temperature range 0°C to 125°C |  |  | 1.3 | V |
| ILIMIT | Current Limit | VIN - VOUT = 5 V, TJ = 25°C | VIN - VOUT = 5 V, TJ = 25°C | 800 | 1200 | 1500 | mA |
|  |  |  | TJ = 25°C |  | 1.7 |  |  |
|  | Minimum Load Current (5) | LM1117-ADJ VIN = 15 V | over the junction temperature range 0°C to 125°C |  |  | 5 | mA |
|  |  |  | TJ = 25°C |  | 5 |  |  |
|  |  | LM1117-1.8 VIN ≤ 15 V | over the junction temperature range 0°C to 125°C |  |  | 10 | mA |
|  |  |  | TJ = 25°C |  | 5 |  |  |
|  |  | LM1117-2.5 VIN ≤ 15 V | over the junction temperature range 0°C to 125°C |  |  | 10 | mA |
|  | Quiescent Current |  | TJ = 25°C |  | 5 |  |  |
|  |  | LM1117-3.3 VIN ≤ 15 V | over the junction temperature range 0°C to 125°C |  |  | 10 | mA |
|  |  |  | TJ = 25°C |  | 5 |  |  |
|  |  | LM1117-5.0 VIN ≤ 15 V | over the junction temperature range 0°C to 125°C |  |  | 10 | mA |
|  | Thermal Regulation | TA = 25°C, 30-ms pulse | TA = 25°C, 30-ms pulse | 0.01 |  | 0.1 | %/W |
|  |  |  | TJ = 25°C |  | 75 |  |  |
|  | Ripple Regulation | fRIPPLE = 1 20 Hz, VIN - VOUT = 3 V VRIPPLE = 1 VPP | over the junction temperature range 0°C to 125°C | 60 |  |  | dB |
|  |  | = 25°C |  |  | 60 |  |  |
|  | Adjust Pin Current | TJ over the junction temperature range 0°C to 125°C | TJ over the junction temperature range 0°C to 125°C |  |  |  | μA |
|  |  |  |  |  |  | 120 |  |
|  | Adjust Pin Current | TJ = 25°C 10 ≤ IOUT ≤ 80 0mA, over the junction 1.4 V ≤ VIN - VOUT ≤ 10 V | TJ = 25°C 10 ≤ IOUT ≤ 80 0mA, over the junction 1.4 V ≤ VIN - VOUT ≤ 10 V |  | 0.2 |  | µA |
|  | Change | = 125°C, 1000 Hrs | temperature range 0°C to 125°C |  |  | 5 |  |
|  | Temperature Stability |  |  | 0.5% |  |  |  |
|  | Long Term Stability RMS Output Noise | TA (% of VOUT), 10 Hz ≤ f ≤ 10 kHz | TA (% of VOUT), 10 Hz ≤ f ≤ 10 kHz | 0.3% | 0.003% |  |  |

(4) The dropout voltage is the input/output differential at which the circuit ceases to regulate against further reduction in input voltage. It is measured when the output voltage has dropped 100 mV from the nominal value obtained at VIN = VOUT + 1.5 V.

(5) The minimum output current required to maintain regulation.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

INSTRUMENTS

## [www.ti.com](http://www.ti.com/)

## 6.6 LM1117I Electrical Characteristics

unless otherwise specified, TJ = 25°C.

| PARAMETER | PARAMETER | TEST CONDITIONS | TEST CONDITIONS | MIN (1) | TYP (2) | MAX (1) | UNIT |
| - | - | - | - | - | - | - | - |
| VREF | Reference Voltage | LM1117I-ADJ IOUT = 10 mA, VIN - VOUT = 2 V, TJ = 25°C | LM1117I-ADJ IOUT = 10 mA, VIN - VOUT = 2 V, TJ = 25°C | 1.238 | 1.25 | 1.262 | V |
| VREF | Reference Voltage | LM1117I-ADJ 10 mA ≤ IOUT ≤ 800 mA, 1.4 V ≤ VIN - VOUT ≤ 10 V | TJ = 25°C |  | 1.25 |  | V |
| VREF | Reference Voltage | LM1117I-ADJ 10 mA ≤ IOUT ≤ 800 mA, 1.4 V ≤ VIN - VOUT ≤ 10 V | over the junction temperature range -40°C to 125°C | 1.2 |  | 1.29 | V |
| VOUT |  | LM1117I-3.3 IOUT = 10 mA, VIN = 5 V, TJ = 25°C |  | 3.267 | 3.3 | 3.333 | V |
| VOUT |  | LM1117I-3.3 0 ≤ IOUT ≤ 800 mA, 4.75 V ≤ VIN ≤ 10 V | TJ = 25°C |  | 3.3 |  | V |
| VOUT |  | LM1117I-3.3 0 ≤ IOUT ≤ 800 mA, 4.75 V ≤ VIN ≤ 10 V | over the junction temperature range -40°C to 125°C | 3.168 |  | 3.432 | V |
| VOUT |  | Output Voltage LM1117I-5.0 IOUT = 10 mA, VIN = 7 V, TJ = 25°C |  | 4.95 | 5 | 5.05 | V |
| VOUT |  | LM1117I-5.0 0 ≤ IOUT ≤ 800 mA, 6.5 V ≤ VIN ≤ 12 V | TJ = 25°C |  | 5 |  | V |
| VOUT |  | LM1117I-5.0 0 ≤ IOUT ≤ 800 mA, 6.5 V ≤ VIN ≤ 12 V | over the junction temperature range -40°C to 125°C | 4.8 |  | 5.2 | V |
| ΔVOUT | Line Regulation (3) | LM1117I-ADJ IOUT = 10 mA, 1.5 V ≤ VIN - VOUT ≤ 13.75 V | TJ = 25°C |  | 0.035% |  |  |
| ΔVOUT | Line Regulation (3) | LM1117I-ADJ IOUT = 10 mA, 1.5 V ≤ VIN - VOUT ≤ 13.75 V | over the junction temperature range -40°C to 125°C |  |  | 0.3% |  |
| ΔVOUT | Line Regulation (3) | LM1117I-3.3 IOUT = 0 mA, 4.75 V ≤ VIN ≤ 15 V | TJ = 25°C |  | 1 |  | mV |
| ΔVOUT | Line Regulation (3) | LM1117I-3.3 IOUT = 0 mA, 4.75 V ≤ VIN ≤ 15 V | over the junction temperature range -40°C to 125°C |  |  | 10 | mV |
| ΔVOUT | Line Regulation (3) | LM1117I-5.0 IOUT = 0 mA, 6.5 V ≤ VIN ≤ 15 V | TJ = 25°C |  | 1 |  | mV |
| ΔVOUT | Line Regulation (3) | LM1117I-5.0 IOUT = 0 mA, 6.5 V ≤ VIN ≤ 15 V | over the junction temperature range -40°C to 125°C |  |  | 15 | mV |
| ΔVOUT | Load Regulation (3) | LM1117I-ADJ VIN - VOUT = 3 V, 10 ≤ IOUT ≤ 800 mA | TJ = 25°C |  | 0.2% |  | mV |
| ΔVOUT | Load Regulation (3) | LM1117I-ADJ VIN - VOUT = 3 V, 10 ≤ IOUT ≤ 800 mA | over the junction temperature range -40°C to 125°C |  |  | 0.5% | mV |
| ΔVOUT | Load Regulation (3) | LM1117I-3.3 VIN = 4.75 V, 0 ≤ IOUT ≤ 800 mA | TJ = 25°C |  | 1 |  |  |
| ΔVOUT | Load Regulation (3) | LM1117I-3.3 VIN = 4.75 V, 0 ≤ IOUT ≤ 800 mA | over the junction temperature range -40°C to 125°C |  |  | 15 |  |
| ΔVOUT | Load Regulation (3) | LM1117I-5.0 VIN = 6.5 V, 0 ≤ IOUT ≤ 800 mA | TJ = 25°C |  | 1 |  |  |
| ΔVOUT | Load Regulation (3) | LM1117I-5.0 VIN = 6.5 V, 0 ≤ IOUT ≤ 800 mA | over the junction temperature range -40°C to 125°C |  |  | 20 | mV |

(1) All limits are ensured by testing or statistical analysis.

(2) Typical Values represent the most likely parametric normal.

(3) Load and line regulation are measured at constant junction room temperature.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

ÎNSTRUMENTS

## LM1117I Electrical Characteristics (continued)

unless otherwise specified, TJ = 25°C.

| PARAMETER | TEST CONDITIONS | TEST CONDITIONS | MIN (1) TJ = | TYP (2) MAX (1) |  | UNIT |
| - | - | - | - | - | - | - |
|  |  |  | 25°C | 1.1 |  | V |
|  |  | IOUT = 100 mA | over the junction temperature range -40°C to 125°C |  | 1.3 | V |
|  |  |  | TJ = 25°C | 1.15 |  | V |
| VIN-V OUT | Dropout Voltage (4) | IOUT = 500 mA | over the junction temperature range -40°C to 125°C |  | 1.35 | V |
|  |  |  | TJ = 25°C | 1.2 |  | V |
|  |  | IOUT = 800 mA | over the junction temperature range -40°C to 125°C |  | 1.4 | V |
| ILIMIT | Current Limit | VIN - VOUT = 5 V, TJ = 25°C | 800 | 1200 | 1500 | mA |
|  | Minimum Load |  | TJ = 25°C over the junction | 1.7 |  | mA |
|  | Current (5) | LM1117I-ADJ VIN = 15 V | temperature range -40°C to 125°C TJ = 25°C |  | 5 | mA |
|  | Quiescent Current | LM1117I-3.3 ≤ 15 V |  | 5 |  | mA |
|  |  | VIN | over the junction temperature range -40°C to 125°C |  | 15 | mA |
|  |  | LM1117I-5.0 VIN ≤ 15 V | TJ = 25°C | 5 |  | mA |
|  |  |  | over the junction temperature range -40°C to 125°C |  | 15 | mA |
|  | Thermal Regulation | TA = 25°C, 30ms Pulse |  | 0.01 | 0.1 | %/W |
|  |  |  | TJ = 25°C | 75 |  | dB |
|  | Ripple Regulation | fRIPPLE = 120 Hz, VIN - VOUT = 3 V VRIPPLE = 1 VPP | over the junction temperature range 60 -40°C to 125°C |  |  |  |
|  |  | TJ = 25°C |  | 60 |  | μA |
|  | Adjust Pin Current | over the junction temperature range -40°C to 125°C | over the junction temperature range -40°C to 125°C |  | 120 | μA |
|  | Adjust Pin Current Change | ≤ IOUT ≤ 800 mA, | TJ = 25°C | 0.2 |  | µA |
|  |  | 10 1.4 V ≤ VIN - VOUT ≤ 10 V | over the junction temperature range -40°C to 125°C |  | 10 | µA |
|  | Temperature Stability |  |  | 0.5% |  |  |
|  | Long Term Stability | TA = 125°C, 1000 Hrs |  | 0.3% |  |  |
|  | RMS Output Noise | (% of VOUT), 10 Hz ≤ f ≤ 10 kHz |  | 0.003% |  |  |

(4) The dropout voltage is the input/output differential at which the circuit ceases to regulate against further reduction in input voltage. It is measured when the output voltage has dropped 100 mV from the nominal value obtained at VIN = VOUT + 1.5 V.

(5) The minimum output current required to maintain regulation.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

INSTRUMENTS

## [www.ti.com](http://www.ti.com/)

## 6.7 Typical Characteristics

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_013.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_014.png)

ÎNSTRUMENTS

## Typical Characteristics (continued)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_015.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

ÎNSTRUMENTS

## 7 Detailed Description

## 7.1 Overview

The LM1117 adjustable version develops a 1.25V reference voltage, VREF, between the output and the adjust terminal. As shown in Figure 10, this voltage is applied across resistor R1 to generate a constant current I1. The current IADJ from the adjust terminal could introduce error to the output. But since it is very small (60µA) compared with the I1 and very constant with line and load changes, the error can be ignored. The constant current I1 then flows through the output set resistor R2 and sets the output voltage to the desired level.

For fixed voltage devices, R1 and R2 are integrated inside the devices.

Figure 10. Basic Adjustable Regulator

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_016.png)

## 7.2 Functional Block Diagram

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_017.png)

## 7.3 Feature Description

## 7.3.1 Load Regulation

The LM1117 regulates the voltage that appears between its output and ground pins, or between its output and adjust pins. In some cases, line resistances can introduce errors to the voltage across the load. To obtain the best load regulation, a few precautions are needed.

- ADJ. (ADJUSTABLE OUTPUT)

OVIN

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

ÎNSTRUMENTS

## Feature Description (continued)

Figure 11, shows a typical application using a fixed output regulator. The Rt1 and Rt2 are the line resistances. It is obvious that the VLOAD is less than the VOUT by the sum of the voltage drops along the line resistances. In this case, the load regulation seen at the RLOAD would be degraded from the data sheet specification. To improve this, the load should be tied directly to the output terminal on the positive side and directly tied to the ground terminal on the negative side.

Figure 11. Typical Application Using Fixed Output Regulator

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_018.png)

When the adjustable regulator is used (Figure 12), the best performance is obtained with the positive side of the resistor R1 tied directly to the output terminal of the regulator rather than near the load. This eliminates line drops from appearing effectively in series with the reference and degrading regulation. For example, a 5V regulator with 0.05Ω resistance between the regulator and load will have a load regulation due to line resistance of 0.05Ω x IL. If R1 (=125Ω) is connected near the load, the effective line resistance will be 0.05Ω (1+R2/R1) or in this case, it is 4 times worse. In addition, the ground side of the resistor R2 can be returned near the ground of the load to provide remote ground sensing and improve load regulation.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_019.png)

VLOAD = VREF (R1 + R2)/R1 - L Rt1

Figure 12. Best Load Regulation Using Adjustable Output Regulator

## 7.4 Device Functional Modes

## 7.4.1 Protection Diodes

Under normal operation, the LM1117 regulators do not need any protection diode. With the adjustable device, the internal resistance between the adjust and output terminals limits the current. No diode is needed to divert the current around the regulator even with capacitor on the adjust terminal. The adjust pin can take a transient signal of ±25V with respect to the output voltage without damaging the device.

When a output capacitor is connected to a regulator and the input is shorted to ground, the output capacitor will discharge into the output of the regulator. The discharge current depends on the value of the capacitor, the output voltage of the regulator, and rate of decrease of VIN. In the LM1117 regulators, the internal diode between the output and input pins can withstand microsecond surge currents of 10A to 20A. With an extremely large output capacitor (≥1000 µF), and with input instantaneously shorted to ground, the regulator could be damaged.

In this case, an external diode is recommended between the output and input pins to protect the regulator, as shown in Figure 13.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

INSTRUMENTS

## [www.ti.com](http://www.ti.com/)

## Device Functional Modes (continued)

Figure 13. Regulator With Protection Diode

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_020.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

ÎNSTRUMENTS

## 8 Application and Implementation

## NOTE

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

## 8.1 Application Information

The LM1117 is a versatile and high performance linear regulator with a wide temperature range and tight line/load regulation operation. An output capacitor is required to further improve transient response and stability. For the adjustable option, the ADJ pin can also be bypassed to achieve very high ripple-rejection ratios. The LM1117 is versatile in its applications, including its uses as a post regulator for DC/DC converters, battery chargers, and microprocessor supplies.

## 8.2 Typical Application

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_021.png)

CAdj

Figure 14. 1.25-V to 10-V Adjustable Regulator With Improved Ripple Rejection

## 8.2.1 Design Requirements

The device component count is very minimal, employing two resistors as part of a voltage divider circuit and an output capacitor for load regulation. A 10-μF tantalum on the input is a suitable input capacitor for almost all applications. An optional bypass capacitor across R2 can also be used to improve PSRR. See Recommended Operating Conditions for more information.

## 8.2.2 Detailed Design Procedure

The output voltage is set based on the selection of the two resistors, R1 and R2, as shown in Figure 14. For details on capacitor selection, refer to External Capacitors.

## 8.2.2.1 External Capacitors

## 8.2.2.1.1 Input Bypass Capacitor

An input capacitor is recommended. A 10-µF tantalum on the input is a suitable input capacitor for almost all applications.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

INSTRUMENTS

## Typical Application (continued)

## 8.2.2.1.2 Adjust Terminal Bypass Capacitor

The adjust terminal can be bypassed to ground with a bypass capacitor (CADJ) to improve ripple rejection. This bypass capacitor prevents ripple from being amplified as the output voltage is increased. At any ripple frequency, the impedance of the CADJ should be less than R1 to prevent the ripple from being amplified:

<!-- formula-not-decoded -->

The R1 is the resistor between the output and the adjust pin. Its value is normally in the range of 100-200Ω. For example, with R1 = 124Ω and fRIPPLE = 120Hz, the CADJ should be &gt; 11µF.

## 8.2.2.1.3 Output Capacitor

The output capacitor is critical in maintaining regulator stability, and must meet the required conditions for both minimum amount of capacitance and equivalent series resistance (ESR). The minimum output capacitance required by the LM1117 is 10 µF, if a tantalum capacitor is used. Any increase of the output capacitance will merely improve the loop stability and transient response. The ESR of the output capacitor should range between 0.3 Ω to 22 Ω. In the case of the adjustable regulator, when the CADJ is used, a larger output capacitance (22-µF tantalum) is required.

## 8.2.3 Application Curve

As shown in Figure 15, the dropout voltage will vary with output current and temperature. Care should be taken during design to ensure the dropout voltage requirement is met across the entire operating temperature and output current range.

Figure 15. Dropout Voltage (VIN - VOUT)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_022.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

INSTRUMENTS

## 8.3 System Examples

Several circuits can be realized with the LM1117. The circuit diagrams in this section demonstrate multiple system examples that can be utilized in many applications.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_023.png)

* Required if the regulator is located far from the power supply filter.

Figure 16. Fixed Output Regulator

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_024.png)

Figure 18. Regulator With Reference

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_025.png)

Figure 17. Adjusting Output of Fixed Regulators

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_026.png)

Figure 19. 5-V Logic Regulator With Electronic Shutdown*

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_027.png)

Select for charge rate.

Figure 20. Battery Backed-Up Regulated Supply

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_028.png)

Figure 21. Low Dropout Negative Supply

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

INSTRUMENTS

[www.ti.com](http://www.ti.com/)

## 9 Power Supply Recommendations

The input supply to the LM1117 must be kept at a voltage level such that its maximum rating is not exceeded. The minimum dropout voltage must also be met with extra headroom when possible to keep the LM1117 in regulation. An input capacitor is recommended. For more information regarding capacitor selection, refer to External Capacitors.

## 10 Layout

## 10.1 Layout Guidelines

Some layout guidelines must be followed to ensure proper regulation of the output voltage with minimum noise. Traces carrying the load current must be wide to reduce the amount of parasitic trace inductance and the feedback loop from VOUT to ADJ must be kept as short as possible. To improve PSRR, a bypass capacitor can be placed at the ADJ pin and must be located as close as possible to the IC. In cases when VIN shorts to ground, an external diode must be placed from VOUT to VIN to divert the surge current from the output capacitor and protect the IC. The diode must be placed close to the corresponding IC pins to increase their effectiveness.

## 10.1.1 Heatsink Requirements

When an integrated circuit operates with an appreciable current, its junction temperature is elevated. It is important to quantify its thermal limits in order to achieve acceptable performance and reliability. This limit is determined by summing the individual parts consisting of a series of temperature rises from the semiconductor junction to the operating environment. A one-dimensional steady-state model of conduction heat transfer is demonstrated in Figure 22. The heat generated at the device junction flows through the die to the die attach pad, through the lead frame to the surrounding case material, to the printed circuit board, and eventually to the ambient environment. Below is a list of variables that may affect the thermal resistance and in turn the need for a heatsink.

Table 1. Component and Application Variables

| RθJC (COMPONENT VARIABLES) | RθJA (APPLICATION VARIABLES) |
| - | - |
| Leadframe Size and Material | Mounting Pad Size, Material, and Location |
| No. of Conduction Pins | Placement of Mounting Pad |
| Die Size | PCB Size and Material |
| Die Attach Material | Traces Length and Width |
| Molding Compound Size and Material | Adjacent Heat Sources |
|  | Volume of Air |
|  | Ambient Temperatue |
|  | Shape of Mounting Pad |

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_029.png)

Mounting Pad

The case temperature is measured at the point where the leads contact with the mounting pad surface

Figure 22. Cross-Sectional View of Integrated Circuit Mounted on a Printed Circuit Board

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

ÎNSTRUMENTS

The LM1117 regulators have internal thermal shutdown to protect the device from over-heating. Under all possible operating conditions, the junction temperature of the LM1117 must be within the range of 0°C to 125°C. A heatsink may be required depending on the maximum power dissipation and maximum ambient temperature of the application. To determine if a heatsink is needed, the power dissipated by the regulator, PD , must be calculated:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 23 shows the voltages and currents which are present in the circuit.

Figure 23. Power Dissipation Diagram

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_030.png)

The next parameter which must be calculated is the maximum allowable temperature rise, TR(max):

TR(max) = TJ(max)-TA(max)

## where

- TJ(max) is the maximum allowable junction temperature (125°C) which will be encountered in the application
- TA(max) is the maximum ambient temperature which will be encountered in the application (4)

Using the calculated values for TR(max) and PD, the maximum allowable value for the junction-to-ambient thermal resistance (RθJA) can be calculated:

<!-- formula-not-decoded -->

For the maximum allowable value for θJA, refer to the Thermal Information table.

As a design aid, Table 2 shows the value of the θJA of SOT-223 and TO-252 for different heatsink area. Figure 24 and Figure 25 reflects the same test results as what are in the Table 2

Figure 26 and Figure 27 shows the maximum allowable power dissipation vs. ambient temperature for the SOT223 and TO-252 device. Figure 28 and Figure 29 shows the maximum allowable power dissipation vs. copper area (in 2 ) for the SOT-223 and TO-252 devices. Please see AN1028 for power enhancement techniques to be used with SOT-223 and TO-252 packages.

Application Note AN-1187 (SNOA401) discusses improved thermal performance and power dissipation for the WSON.

Table 2. RθJA Different Heatsink Area

| LAYOUT | COPPER AREA - Top Side (in 2 ) (1) | COPPER AREA - Bottom Side (in 2 ) | THERMAL RESISTANCE - (θJA,°C/W) SOT-223 | THERMAL RESISTANCE - (θJA,°C/W) TO-252 |
| - | - | - | - | - |
| 1 | 0.0123 | 0 | 136 | 103 |
| 2 | 0.066 | 0 | 123 | 87 |
| 3 | 0.3 | 0 | 84 | 60 |
| 4 | 0.53 | 0 | 75 | 54 |
| 5 | 0.76 | 0 | 69 | 52 |
| 6 | 1 | 0 | 66 | 47 |
| 7 | 0 | 0.2 | 115 | 84 |
| 8 | 0 | 0.4 | 98 | 70 |
| 9 | 0 | 0.6 | 89 | 63 |
| 10 | 0 | 0.8 | 82 | 57 |

(1) Tab of device attached to topside copper

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

ÎNSTRUMENTS

## [www.ti.com](http://www.ti.com/)

## Table 2. RθJA Different Heatsink Area (continued)

| LAYOUT | COPPER AREA | COPPER AREA | THERMAL RESISTANCE | THERMAL RESISTANCE |
| - | - | - | - | - |
| 11 | 0 | 1 | 79 | 57 |
| 12 | 0.066 | 0.066 | 125 | 89 |
| 13 | 0.175 | 0.175 | 93 | 72 |
| 14 | 0.284 | 0.284 | 83 | 61 |
| 15 | 0.392 | 0.392 | 75 | 55 |
| 16 | 0.5 | 0.5 | 70 | 53 |

Figure 24. RθJA vs 1-oz Copper Area for SOT-223

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_031.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_032.png)

Figure 26. Maximum Allowable Power Dissipation vs Ambient Temperature for SOT-223

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_033.png)

Figure 25. RθJA vs 2-oz Copper Area for TO-252

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_034.png)

Figure 27. Maximum Allowable Power Dissipation vs Ambient Temperature for TO-252

1

Figure 28. Maximum Allowable Power Dissipation vs 1-oz Copper Area for SOT-223

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_035.png)

1

Figure 29. Maximum Allowable Power Dissipation vs 2-oz Copper Area for TO-252

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_036.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

INSTRUMENTS

Figure 30. Top View of the Thermal Test Pattern in Actual Scale

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_037.png)

Figure 31. Bottom View of the Thermal Test Pattern in Actual Scale

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_038.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_011.png)

ÎNSTRUMENTS

## [www.ti.com](http://www.ti.com/)

## 10.2 Layout Example

Figure 32. Layout Example (SOT-223)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_039.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_010.png)

ÎNSTRUMENTS

## 11 Device and Documentation Support

## 11.1 Community Resources

The following links connect to TI community resources. Linked contents are provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

TI E2E™ Online Community TI's Engineer-to-Engineer (E2E) Community. Created to foster collaboration among engineers. At e2e.ti.com, you can ask questions, share knowledge, explore ideas and help solve problems with fellow engineers.

Design Support TI's Design Support Quickly find helpful E2E forums along with design support tools and contact information for technical support.

## 11.2 Trademarks

E2E is a trademark of Texas Instruments.

All other trademarks are the property of their respective owners.

## 11.3 Electrostatic Discharge Caution

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_040.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_041.png)

These devices have limited built-in ESD protection. The leads should be shorted together or the device placed in conductive foam during storage or handling to prevent electrostatic damage to the MOS gates.

## 11.4 Glossary

SLYZ022 - TI Glossary.

This glossary lists and explains terms, acronyms, and definitions.

## 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_042.png)

## PACKAGE OPTION ADDENDUM

3-Feb-2016

## PACKAGING INFORMATION

| Orderable Device | Status (1) | Package Type | Package Drawing | Pins | Package Qty | Eco Plan (2) | Lead/Ball Finish (6) | MSL Peak Temp (3) | Op Temp (°C) | Device Marking (4/5) | Samples |
| - | - | - | - | - | - | - | - | - | - | - | - |
| LM1117DT-1.8/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-1.8 | Samples |
| LM1117DT-2.5/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-2.5 | Samples |
| LM1117DT-3.3/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-3.3 | Samples |
| LM1117DT-5.0/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-5.0 | Samples |
| LM1117DT-ADJ/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-ADJ | Samples |
| LM1117DTX-1.8/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-1.8 | Samples |
| LM1117DTX-2.5/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-2.5 | Samples |
| LM1117DTX-3.3/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-3.3 | Samples |
| LM1117DTX-5.0/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-5.0 | Samples |
| LM1117DTX-ADJ/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | 0 to 125 | LM1117 DT-ADJ | Samples |
| LM1117IDT-3.3/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | -40 to 125 | LM1117 IDT-3.3 | Samples |
| LM1117IDT-5.0/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | -40 to 125 | LM1117 IDT-5.0 | Samples |
| LM1117IDT-ADJ/NOPB | ACTIVE | TO-252 | NDP | 3 | 75 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | -40 to 125 | LM1117 IDT-ADJ | Samples |
| LM1117IDTX-3.3/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | -40 to 125 | LM1117 IDT-3.3 | Samples |
| LM1117IDTX-5.0/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | -40 to 125 | LM1117 IDT-5.0 | Samples |
| LM1117IDTX-ADJ/NOPB | ACTIVE | TO-252 | NDP | 3 | 2500 | Green (RoHS & no Sb/Br) | CU SN | Level-2-260C-1 YEAR | -40 to 125 | LM1117 IDT-ADJ | Samples |
| LM1117ILD-ADJ/NOPB | ACTIVE | WSON | NGN | 8 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-3-260C-168 HR | -40 to 125 | 1117IAD | Samples |

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_043.png)

www.ti.com INSTRUMENTS

## PACKAGE OPTION ADDENDUM

3-Feb-2016

| Orderable Device | Status (1) | Package Type | Package Drawing | Pins | Package Qty | Eco Plan (2) | Lead/Ball Finish (6) | MSL Peak Temp (3) | Op Temp (°C) | Device Marking (4/5) | Samples |
| - | - | - | - | - | - | - | - | - | - | - | - |
| LM1117IMP-3.3/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | -40 to 125 | N05B | Samples |
| LM1117IMP-5.0/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | -40 to 125 | N06B | Samples |
| LM1117IMP-ADJ/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | -40 to 125 | N03B | Samples |
| LM1117IMPX-3.3/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | -40 to 125 | N05B | Samples |
| LM1117IMPX-5.0/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | -40 to 125 | N06B | Samples |
| LM1117IMPX-ADJ/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | -40 to 125 | N03B | Samples |
| LM1117LD-1.8/NOPB | ACTIVE | WSON | NGN | 8 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-3-260C-168 HR | 0 to 125 | 1117-18 | Samples |
| LM1117LD-2.5/NOPB | ACTIVE | WSON | NGN | 8 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-3-260C-168 HR | 0 to 125 | 1117-25 | Samples |
| LM1117LD-3.3/NOPB | ACTIVE | WSON | NGN | 8 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-3-260C-168 HR | 0 to 125 | 1117-33 | Samples |
| LM1117LD-ADJ/NOPB | ACTIVE | WSON | NGN | 8 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-3-260C-168 HR | 0 to 125 | 1117ADJ | Samples |
| LM1117LDX-1.8 | NRND | WSON | NGN | 8 | 4500 | TBD | Call TI | Call TI | 0 to 125 | 1117-18 |  |
| LM1117LDX-1.8/NOPB | ACTIVE | WSON | NGN | 8 | 4500 | Green (RoHS & no Sb/Br) | CU SN | Level-3-260C-168 HR | 0 to 125 | 1117-18 | Samples |
| LM1117LDX-ADJ/NOPB | ACTIVE | WSON | NGN | 8 | 4500 | Green (RoHS & no Sb/Br) | CU SN | Level-3-260C-168 HR | 0 to 125 | 1117ADJ | Samples |
| LM1117MP-1.8/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N12A | Samples |
| LM1117MP-2.5/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N13A | Samples |
| LM1117MP-3.3/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N05A | Samples |
| LM1117MP-5.0/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N06A | Samples |
| LM1117MP-ADJ/NOPB | ACTIVE | SOT-223 | DCY | 4 | 1000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N03A | Samples |

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_044.png)

www.ti.com

## PACKAGE OPTION ADDENDUM

3-Feb-2016

| Orderable Device | Status (1) | Package Type | Package Drawing | Pins | Package Qty | Eco Plan (2) | Lead/Ball Finish (6) | MSL Peak Temp (3) | Op Temp (°C) | Device Marking (4/5) | Samples |
| - | - | - | - | - | - | - | - | - | - | - | - |
| LM1117MPX-1.8/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N12A | Samples |
| LM1117MPX-2.5/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N13A | Samples |
| LM1117MPX-3.3 | ACTIVE | SOT-223 | DCY | 4 | 2000 | TBD | Call TI | Call TI |  | N05A | Samples |
| LM1117MPX-3.3/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N05A | Samples |
| LM1117MPX-5.0/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N06A | Samples |
| LM1117MPX-ADJ/NOPB | ACTIVE | SOT-223 | DCY | 4 | 2000 | Green (RoHS & no Sb/Br) | CU SN | Level-1-260C-UNLIM | 0 to 125 | N03A | Samples |
| LM1117S-ADJ/NOPB | ACTIVE | DDPAK/ TO-263 | KTT | 3 | 45 | Pb-Free (RoHS Exempt) | CU SN | Level-3-245C-168 HR | 0 to 125 | LM1117S ADJ | Samples |
| LM1117SX-3.3/NOPB | ACTIVE | DDPAK/ TO-263 | KTT | 3 | 500 | Pb-Free (RoHS Exempt) | CU SN | Level-3-245C-168 HR | 0 to 125 | LM1117S 3.3 | Samples |
| LM1117SX-5.0/NOPB | ACTIVE | DDPAK/ TO-263 | KTT | 3 | 500 | Pb-Free (RoHS Exempt) | CU SN | Level-3-245C-168 HR | 0 to 125 | LM1117S 5.0 | Samples |
| LM1117SX-ADJ/NOPB | ACTIVE | DDPAK/ TO-263 | KTT | 3 | 500 | Pb-Free (RoHS Exempt) | CU SN | Level-3-245C-168 HR | 0 to 125 | LM1117S ADJ | Samples |
| LM1117T-2.5/NOPB | ACTIVE | TO-220 | NDE | 3 | 45 | Green (RoHS & no Sb/Br) | CU SN | Level-1-NA-UNLIM | 0 to 125 | LM1117T 2.5 | Samples |
| LM1117T-3.3/NOPB | ACTIVE | TO-220 | NDE | 3 | 45 | Green (RoHS & no Sb/Br) | CU SN | Level-1-NA-UNLIM | 0 to 125 | LM1117T 3.3 | Samples |
| LM1117T-5.0/NOPB | ACTIVE | TO-220 | NDE | 3 | 45 | Green (RoHS & no Sb/Br) | CU SN | Level-1-NA-UNLIM | 0 to 125 | LM1117T 5.0 | Samples |
| LM1117T-ADJ/NOPB | ACTIVE | TO-220 | NDE | 3 | 45 | Green (RoHS & no Sb/Br) | CU SN | Level-1-NA-UNLIM | 0 to 125 | LM1117T ADJ | Samples |

(1) The marketing status values are defined as follows:

ACTIVE: Product device recommended for new designs.

LIFEBUY: TI has announced that the device will be discontinued, and a lifetime-buy period is in effect.

NRND: Not recommended for new designs. Device is in production to support existing customers, but TI does not recommend using this part in a new design.

PREVIEW: Device has been announced but is not in production. Samples may or may not be available.

OBSOLETE: TI has discontinued the production of the device.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_045.png)

www.ti.com

## PACKAGE OPTION ADDENDUM

3-Feb-2016

(2) Eco Plan - The planned eco-friendly classification: Pb-Free (RoHS), Pb-Free (RoHS Exempt), or Green (RoHS &amp; no Sb/Br) - please check http://www.ti.com/productcontent for the latest availability information and additional product content details.

TBD: The Pb-Free/Green conversion plan has not been defined.

Pb-Free (RoHS): TI's terms "Lead-Free" or "Pb-Free" mean semiconductor products that are compatible with the current RoHS requirements for all 6 substances, including the requirement that lead not exceed 0.1% by weight in homogeneous materials. Where designed to be soldered at high temperatures, TI Pb-Free products are suitable for use in specified lead-free processes.

Pb-Free (RoHS Exempt): This component has a RoHS exemption for either 1) lead-based flip-chip solder bumps used between the die and package, or 2) lead-based die adhesive used between the die and leadframe. The component is otherwise considered Pb-Free (RoHS compatible) as defined above.

Green (RoHS &amp; no Sb/Br): TI defines "Green" to mean Pb-Free (RoHS compatible), and free of Bromine (Br) and Antimony (Sb) based flame retardants (Br or Sb do not exceed 0.1% by weight in homogeneous material)

(3) MSL, Peak Temp. - The Moisture Sensitivity Level rating according to the JEDEC industry standard classifications, and peak solder temperature.

(4) There may be additional marking, which relates to the logo, the lot trace code information, or the environmental category on the device.

- (5) Multiple Device Markings will be inside parentheses. Only one Device Marking contained in parentheses and separated by a "~" will appear on a device. If a line is indented then it is a continuation of the previous line and the two combined represent the entire Device Marking for that device.
- (6) Lead/Ball Finish - Orderable Devices may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead/Ball Finish values may wrap to two lines if the finish value exceeds the maximum column width.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_046.png)

www.ti.com

## PACKAGE MATERIALS INFORMATION

3-Feb-2016

## TAPE AND REEL INFORMATION

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_047.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_048.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_049.png)

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| LM1117DTX-1.8/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117DTX-2.5/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117DTX-3.3/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117DTX-5.0/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117DTX-ADJ/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117IDTX-3.3/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117IDTX-5.0/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117IDTX-ADJ/NOPB | TO-252 | NDP | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| LM1117ILD-ADJ/NOPB | WSON | NGN | 8 | 1000 | 178.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |
| LM1117IMP-3.3/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117IMP-5.0/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117IMP-ADJ/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117IMPX-3.3/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117IMPX-5.0/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117IMPX-ADJ/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117LD-1.8/NOPB | WSON | NGN | 8 | 1000 | 178.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |
| LM1117LD-2.5/NOPB | WSON | NGN | 8 | 1000 | 178.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |
| LM1117LD-3.3/NOPB | WSON | NGN | 8 | 1000 | 178.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |

## *All dimensions are nominal

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_046.png)

INSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

3-Feb-2016

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| LM1117LD-ADJ/NOPB | WSON | NGN | 8 | 1000 | 178.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |
| LM1117LDX-1.8 | WSON | NGN | 8 | 4500 | 330.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |
| LM1117LDX-1.8/NOPB | WSON | NGN | 8 | 4500 | 330.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |
| LM1117LDX-ADJ/NOPB | WSON | NGN | 8 | 4500 | 330.0 | 12.4 | 4.3 | 4.3 | 1.3 | 8.0 | 12.0 | Q1 |
| LM1117MP-1.8/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MP-2.5/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MP-3.3/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MP-5.0/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MP-ADJ/NOPB | SOT-223 | DCY | 4 | 1000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MPX-1.8/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MPX-2.5/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MPX-3.3 | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MPX-3.3/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MPX-5.0/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117MPX-ADJ/NOPB | SOT-223 | DCY | 4 | 2000 | 330.0 | 16.4 | 7.0 | 7.5 | 2.2 | 12.0 | 16.0 | Q3 |
| LM1117SX-3.3/NOPB | DDPAK/ TO-263 | KTT | 3 | 500 | 330.0 | 24.4 | 10.75 | 14.85 | 5.0 | 16.0 | 24.0 | Q2 |
| LM1117SX-5.0/NOPB | DDPAK/ TO-263 | KTT | 3 | 500 | 330.0 | 24.4 | 10.75 | 14.85 | 5.0 | 16.0 | 24.0 | Q2 |
| LM1117SX-ADJ/NOPB | DDPAK/ TO-263 | KTT | 3 | 500 | 330.0 | 24.4 | 10.75 | 14.85 | 5.0 | 16.0 | 24.0 | Q2 |

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_050.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_046.png)

www.ti.com

## PACKAGE MATERIALS INFORMATION

3-Feb-2016

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| LM1117DTX-1.8/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117DTX-2.5/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117DTX-3.3/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117DTX-5.0/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117DTX-ADJ/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117IDTX-3.3/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117IDTX-5.0/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117IDTX-ADJ/NOPB | TO-252 | NDP | 3 | 2500 | 367.0 | 367.0 | 38.0 |
| LM1117ILD-ADJ/NOPB | WSON | NGN | 8 | 1000 | 213.0 | 191.0 | 55.0 |
| LM1117IMP-3.3/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117IMP-5.0/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117IMP-ADJ/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117IMPX-3.3/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117IMPX-5.0/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117IMPX-ADJ/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117LD-1.8/NOPB | WSON | NGN | 8 | 1000 | 213.0 | 191.0 | 55.0 |
| LM1117LD-2.5/NOPB | WSON | NGN | 8 | 1000 | 213.0 | 191.0 | 55.0 |
| LM1117LD-3.3/NOPB | WSON | NGN | 8 | 1000 | 213.0 | 191.0 | 55.0 |
| LM1117LD-ADJ/NOPB | WSON | NGN | 8 | 1000 | 213.0 | 191.0 | 55.0 |
| LM1117LDX-1.8 | WSON | NGN | 8 | 4500 | 367.0 | 367.0 | 35.0 |
| LM1117LDX-1.8/NOPB | WSON | NGN | 8 | 4500 | 367.0 | 367.0 | 35.0 |
| LM1117LDX-ADJ/NOPB | WSON | NGN | 8 | 4500 | 367.0 | 367.0 | 35.0 |
| LM1117MP-1.8/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117MP-2.5/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117MP-3.3/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117MP-5.0/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117MP-ADJ/NOPB | SOT-223 | DCY | 4 | 1000 | 367.0 | 367.0 | 35.0 |
| LM1117MPX-1.8/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117MPX-2.5/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117MPX-3.3 | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117MPX-3.3/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117MPX-5.0/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117MPX-ADJ/NOPB | SOT-223 | DCY | 4 | 2000 | 367.0 | 367.0 | 35.0 |
| LM1117SX-3.3/NOPB | DDPAK/TO-263 | KTT | 3 | 500 | 367.0 | 367.0 | 45.0 |
| LM1117SX-5.0/NOPB | DDPAK/TO-263 | KTT | 3 | 500 | 367.0 | 367.0 | 45.0 |
| LM1117SX-ADJ/NOPB | DDPAK/TO-263 | KTT | 3 | 500 | 367.0 | 367.0 | 45.0 |

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_051.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_052.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_053.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_054.png)

## MPDS094A - APRIL 2001 - REVISED JUNE 2002

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_055.png)

- NOTES: A. All linear dimensions are in millimeters (inches).
- B. This drawing is subject to change without notice.
- C. Body dimensions do not include mold flash or protrusion.
- D. Falls within JEDEC TO-261 Variation AA.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_056.png)

## DCY (R-PDSO-G4)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_057.png)

## NOTES:

- A. All linear dimensions are in millimeters.
- B. This drawing is subject to change without notice.
- C. Publication IPC-7351 is recommended for alternate designs.
- D. Laser cutting apertures with trapezoidal walls and also rounding corners wil offer better paste release. Customers should contact their board assembly site for stencil recommendations. Refer to IPC 7525 for stencil design considerations.

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_058.png)

www.ti.com

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_059.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_052.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_060.png)

![Image](LM1117%20Datasheet%20%28TI%20SNOS412N%29_files/img_052.png)

## IMPORTANT NOTICE

Texas Instruments Incorporated and its subsidiaries (TI) reserve the right to make corrections, enhancements, improvements and other changes to its semiconductor products and services per JESD46, latest issue, and to discontinue any product or service per JESD48, latest issue. Buyers should obtain the latest relevant information before placing orders and should verify that such information is current and complete. All semiconductor products (also referred to herein as "components") are sold subject to TI's terms and conditions of sale supplied at the time of order acknowledgment.

TI warrants performance of its components to the specifications applicable at the time of sale, in accordance with the warranty in TI's terms and conditions of sale of semiconductor products. Testing and other quality control techniques are used to the extent TI deems necessary to support this warranty. Except where mandated by applicable law, testing of all parameters of each component is not necessarily performed.

TI assumes no liability for applications assistance or the design of Buyers' products. Buyers are responsible for their products and applications using TI components. To minimize the risks associated with Buyers' products and applications, Buyers should provide adequate design and operating safeguards.

TI does not warrant or represent that any license, either express or implied, is granted under any patent right, copyright, mask work right, or other intellectual property right relating to any combination, machine, or process in which TI components or services are used. Information published by TI regarding third-party products or services does not constitute a license to use such products or services or a warranty or endorsement thereof. Use of such information may require a license from a third party under the patents or other intellectual property of the third party, or a license from TI under the patents or other intellectual property of TI.

Reproduction of significant portions of TI information in TI data books or data sheets is permissible only if reproduction is without alteration and is accompanied by all associated warranties, conditions, limitations, and notices. TI is not responsible or liable for such altered documentation. Information of third parties may be subject to additional restrictions.

Resale of TI components or services with statements different from or beyond the parameters stated by TI for that component or service voids all express and any implied warranties for the associated TI component or service and is an unfair and deceptive business practice. TI is not responsible or liable for any such statements.

Buyer acknowledges and agrees that it is solely responsible for compliance with all legal, regulatory and safety-related requirements concerning its products, and any use of TI components in its applications, notwithstanding any applications-related information or support that may be provided by TI. Buyer represents and agrees that it has all the necessary expertise to create and implement safeguards which anticipate dangerous consequences of failures, monitor failures and their consequences, lessen the likelihood of failures that might cause harm and take appropriate remedial actions. Buyer will fully indemnify TI and its representatives against any damages arising out of the use of any TI components in safety-critical applications.

In some cases, TI components may be promoted specifically to facilitate safety-related applications. With such components, TI's goal is to help enable customers to design and create their own end-product solutions that meet applicable functional safety standards and requirements. Nonetheless, such components are subject to these terms.

No TI components are authorized for use in FDA Class III (or similar life-critical medical equipment) unless authorized officers of the parties have executed a special agreement specifically governing such use.

Only those TI components which TI has specifically designated as military grade or "enhanced plastic" are designed and intended for use in military/aerospace applications or environments. Buyer acknowledges and agrees that any military or aerospace use of TI components which have not been so designated is solely at the Buyer's risk, and that Buyer is solely responsible for compliance with all legal and regulatory requirements in connection with such use.

TI has specifically designated certain components as meeting ISO/TS16949 requirements, mainly for automotive use. In any case of use of non-designated products, TI will not be responsible for any failure to meet ISO/TS16949.

| Products |  | Applications |  |
| - | - | - | - |
| Audio | www.ti.com/audio | Automotive and Transportation | www.ti.com/automotive |
| Amplifiers | amplifier.ti.com | Communications and Telecom | www.ti.com/communications |
| Data Converters | dataconverter.ti.com | Computers and Peripherals | www.ti.com/computers |
| DLP® Products | www.dlp.com | Consumer Electronics | www.ti.com/consumer-apps |
| DSP | dsp.ti.com | Energy and Lighting | www.ti.com/energy |
| Clocks and Timers | www.ti.com/clocks | Industrial | www.ti.com/industrial |
| Interface | interface.ti.com | Medical | www.ti.com/medical |
| Logic | logic.ti.com | Security | www.ti.com/security |
| Power Mgmt | power.ti.com | Space, Avionics and Defense | www.ti.com/space-avionics-defense |
| Microcontrollers | microcontroller.ti.com | Video and Imaging | www.ti.com/video |
| RFID OMAP Applications Processors | www.ti-rfid.com www.ti.com/omap | TI E2E Community | e2e.ti.com |
| Wireless Connectivity | www.ti.com/wirelessconnectivity | www.ti.com/wirelessconnectivity |  |

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2016, Texas Instruments Incorporated
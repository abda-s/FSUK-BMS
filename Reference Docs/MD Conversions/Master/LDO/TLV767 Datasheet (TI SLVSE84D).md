<!-- Converted from TLV767 Datasheet (TI SLVSE84D).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_001.png)

INSTRUMENTS

## 1 Features

- VIN: 2.5 V to 16 V
- VOUT:
- 0.8 V to 14.6 V (adjustable)
- 0.8 V to 6.6 V (fixed, 50-mV steps)
- 1% output accuracy over load and temperature
- Low IQ: 50 µA (typical, ~1.5 µA in shutdown)
- Internal soft-start time: 500 µs (typical)
- Fold-back current limiting and thermal protection
- Stable with 1-µF ceramic capacitors
- High PSRR: 70 dB at 1 kHz, 46 dB at 1 MHz
- Temperature range: -40°C to +125°C
- Packages:
- 6-pin 2-mm × 2-mm WSON
- 8-pin 3-mm x 3-mm HVSSOP
- 5-pin 2.9-mm x 1.6-mm SOT-23

## 2 Applications

- [Appliances](http://www.ti.com/applications/industrial/appliances/overview.html)
- [TVs, monitors, and set top boxes](http://www.ti.com/applications/personal-electronics/tv/overview.html)
- [Motion detectors (PIR, uWave, and so forth)](http://www.ti.com/solution/motion-detector-pir-uwave)
- [Motor drives and control boards](http://www.ti.com/applications/industrial/motor-drives/overview.html)
- [Printers and PC peripherals](http://www.ti.com/applications/personal-electronics/connected-peripherals-printers/overview.html)
- [Wi-Fi access points and routers](http://www.ti.com/applications/communications-equipment/wired-networking/overview.html)

Reduced Inrush Current With 22 µF at COUT

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_002.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_003.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_004.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_005.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_006.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_007.png)

[TLV767](https://www.ti.com/product/TLV767)

## TLV767 1-A, 16-V Precision Linear Voltage Regulator

## 3 Description

The TLV767 is a wide input linear voltage regulator supporting an input voltage range from 2.5 V to 16 V and up to 1 A of load current. The output range is from 0.8 V to 6.6 V or up to 14.6 V in the adjustable version.

Additionally, the TLV767 has a 1% output accuracy that can meet the needs of low voltage microcontrollers (MCUs) and processors.

The TLV767 is designed to have a much lower IQ than traditional wide-VIN regulators, thus making the device well positioned to meet the needs of increasingly stringent standby power requirements. When disabled, the TLV767 draws only 1.5 µA of IQ.

The internal soft-start time and foldback current limit reduce inrush current during start up, thus minimizing input capacitance.

Wide bandwidth PSRR performance is greater than 70 dB at 1 kHz and 46 dB at 1 MHz, which helps attenuate the switching frequency of an upstream DC/DC converter and minimizes post regulator filtering. To allow for more flexibility, the TLV767 has both fixed and adjustable versions.

The TLV767 is available in a 6-pin, 2-mm × 2-mm WSON (DRV), an 8-pin 3-mm x 3-mm HVSSOP (DGN), and a 5-pin 2.9-mm x 1.6-mm SOT-23 (DBV) package.

## Device Information (1)

| PART NUMBER | PACKAGE | BODY SIZE (NOM) |
| - | - | - |
| TLV767 | WSON (6) | 2.00 mm × 2.00 mm |
| TLV767 | HVSSOP (8) | 3.00 mm x 3.00 mm |
| TLV767 | SOT-23 (5) | 2.90 mm x 1.60 mm |

- (1) For all available packages, see the orderable addendum at the end of the data sheet.

Typical Application Circuit

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_008.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_009.png)

## Table of Contents

| 1 Features............................................................................1 |  | 8.4 Device Functional Modes..........................................18 |
| - | - | - |
| 2 Applications.....................................................................1 | 9 Application and Implementation..................................19 |  |
| 3 Description.......................................................................1 | 9.1 Application Information............................................. | 19 |
| 4 Revision History.............................................................. 2 | 9.2 Typical Application.................................................... | 22 |
| 5 Pin Configuration and Functions...................................3 | 10 Power Supply Recommendations..............................23 |  |
| 6 Specifications.................................................................. 5 | 11 Layout...........................................................................24 |  |
| 6.1 Absolute Maximum Ratings ....................................... 5 | 11.1 Layout Guidelines................................................... | 24 |
| 6.2 ESD Ratings .............................................................. 5 | 11.2 Layout Examples.....................................................24 |  |
| 6.3 Recommended Operating Conditions ........................5 | 12 Device and Documentation Support..........................25 |  |
| 6.4 Thermal Information ...................................................6 | 12.1 Device Support....................................................... | 25 |
| 6.5 Electrical Characteristics ............................................6 | 12.2 Documentation Support.......................................... | 25 |
| 7 Typical Characteristics................................................... 8 | 12.3 Receiving Notification of Documentation Updates..25 |  |
| 8 Detailed Description......................................................14 | 12.4 Support Resources................................................. | 25 |
| 8.1 Overview...................................................................14 | 12.5 Trademarks.............................................................25 |  |
| 8.2 Functional Block Diagrams....................................... 14 | 12.6 Electrostatic Discharge Caution..............................25 |  |
| 8.3 Feature Description...................................................15 | 12.7 Glossary..................................................................25 |  |
| 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. | 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. | 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. |
| Changes from Revision C (June 2020) to Revision D (July 2021) · | Changes from Revision C (June 2020) to Revision D (July 2021) · | Page |
| Added DBV (SOT-23) package to document......................................................................................................1 Changed VOUT adjustable Features bullet from 0.8 V to 13.6 V (adjustable) to 0.8 V to 14.6 V (adjustable) | Added DBV (SOT-23) package to document......................................................................................................1 Changed VOUT adjustable Features bullet from 0.8 V to 13.6 V (adjustable) to 0.8 V to 14.6 V (adjustable) |  |
| · Changed maximum output range for adjustable version from 13.6 V to 14.6 V ................................................ · | · Changed maximum output range for adjustable version from 13.6 V to 14.6 V ................................................ · | ..1 1 24 |
| · · Added DBV pinout and pin information to Pin Configuration and Functions section..........................................3 | · · Added DBV pinout and pin information to Pin Configuration and Functions section..........................................3 |  |
| Added Layout Example for the Fixed DBV Version figure to the Layout Examples section............................. Changes from Revision B (April 2019) to Revision C | (June 2020) | Page |
| Added DGN (HVSSOP) package to document...................................................................................................1 | Added DGN (HVSSOP) package to document...................................................................................................1 |  |
| · · Changed Applications section............................................................................................................................ | · · Changed Applications section............................................................................................................................ | 1 |
| · Added DGN pinouts and pin information to Pin Configuration and Functions section........................................3 | · Added DGN pinouts and pin information to Pin Configuration and Functions section........................................3 |  |
| · Added HVSSOP thermal information .................................................................................................................6 Added Layout Example for the Fixed HVSSOP Version and Layout Example for the Adjustable HVSSOP | · Added HVSSOP thermal information .................................................................................................................6 Added Layout Example for the Fixed HVSSOP Version and Layout Example for the Adjustable HVSSOP |  |
| · Version figures to the Layout Examples section...............................................................................................24 | · Version figures to the Layout Examples section...............................................................................................24 |  |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_010.png)

## 5 Pin Configuration and Functions

Figure 5-1. DRV Package (Adjustable), 6-Pin WSON, Top View

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_011.png)

Figure 5-3. DGN Package (Adjustable), 8-Pin HVSSOP, Top View

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_012.png)

Figure 5-2. DRV Package (Fixed), 6-Pin WSON, Top View

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_013.png)

Figure 5-4. DGN Package (Fixed), 8-Pin HVSSOP, Top View

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_014.png)

Figure 5-5. DBV Package (Fixed), 5-Pin SOT-23, Top View

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_015.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_016.png)

Table 5-1. Pin Functions

| PIN - NAME | PIN - DRV (Adj) | PIN - DRV (Fixed) | PIN - DGN (Adj) | PIN - DGN (Fixed) | DBV (Fixed) | I/O | DESCRIPTION |
| - | - | - | - | - | - | - | - |
| EN | 4 | 4 | 5 | 5 | 3 | I | Enable pin. Driving the enable pin high enables the device. Driving this pin low disables the device. High and low thresholds are listed in the Electrical Characteristics table. This pin has an internal pullup and can be left floating to enable the device or the pin can be connected to the input pin. |
| FB | 2 | - | 2 | - | - | I | Feedback pin. Input to the control-loop error amplifier. This pin is used to set the output voltage of the device with the use of external resistors. Do not float this pin. For adjustable-voltage version devices only. |
| GND | 3, 5 | 3, 5 | 4, 6 | 4, 6 | 2 | - | Ground pin. All ground pins must be grounded. |
| DNC | - | - | - | - | 4 | - | Do not connect to a biased voltage. Tie this pin to ground or leave floating |
| IN | 6 | 6 | 8 | 8 | 1 | I | Input pin. Use the recommended capacitor value as listed in the Recommended Operating Conditions table. Place the input capacitor as close to the IN and GND pins of the device as possible. |
| OUT | 1 | 1 | 1 | 1 | 5 | O | Output pin. Use the recommended capacitor value as listed in the Recommended Operating Conditions table. Place the output capacitor as close to the OUT and GND pins of the device as possible. |
| SNS | - | 2 | - | 2 | - | I | Output sense pin. Connect the SNS pin to the OUT pin, or to remotely sense the output voltage at the load, connect the SNS pin to the load. Do not float this pin. For fixed- voltage version devices only. |
| Thermal pad | Pad | Pad | Pad | Pad | - | - | Exposed pad of the package. Connect this pad to ground or leave floating. Connect the thermal pad to a large-area ground plane for best thermal performance. |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_017.png)

[www.ti.com](https://www.ti.com/)

## 6 Specifications

## 6.1 Absolute Maximum Ratings

Over operating free-air temperature range (unless otherwise noted) (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Voltage (2) | VIN | -0.3 | 18 | V |
| Voltage (2) | VOUT (3) | -0.3 | VIN + 0.3 | V |
| Voltage (2) | VSNS (3) | -0.3 | VIN + 0.3 | V |
| Voltage (2) | VFB | -0.3 | 3 | V |
| Voltage (2) | VEN | -0.3 | 18 | V |
| Current | Maximum output current | Internally Limited | Internally Limited | A |
| Temperature | Operating junction (TJ) | -50 | 150 | °C |
| Temperature | Storage (TSTG) | -65 | 150 | °C |

(1) Stresses beyond those listed under Absolute Maximum Rating may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Condition. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

- (2) All voltages with respect to GND.
- (3) VIN + 0.3 V or 18 V (whichever is smaller)

## 6.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| - | - | - | - | - |
| V(ESD) | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/ JEDEC JS-001, all pins (1) | ±3000 | V |
| V(ESD) |  | Charged device model (CDM), per JEDEC specification JESD22-C101, all pins (2) | ±1000 | V |

- (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
- (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - |
| VIN | Input voltage | 2.5 |  | 16 | V |
| VEN | Enable voltage | 0 |  | 16 | V |
| VOUT | Output voltage | 0.8 |  | 14.6 | V |
| IOUT | Output current (2.5 V ≤ VIN < 3 V) | 0 |  | 0.8 | A |
| IOUT | Output current (VIN ≥ 3 V) | 0 |  | 1 | A |
| COUT | Output capacitor (1) | 1 | 2.2 | 220 | µF |
| COUT ESR | Output capacitor ESR | 2 |  | 500 | mΩ |
| CIN | Input capacitor |  | 1 |  | µF |
| CFF | Feed-forward capacitor (optional (2) , for adjustable device only) |  | 10 |  | pF |
| IFB_DIVIDER | Feedback divider current (2) (adjustable device only) | 5 |  |  | µA |
| TJ | Junction temperature | -40 |  | 125 | °C |

(1) Effective output capacitance of 0.5 µF minimum required for stability.

(2) CFF required for stability if the feedback divider current &lt; 5 µA. Feedback divider current = VOUT / (R1 + R2). See Feed-Forward Capacitor (CFF) section for details.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_016.png)

## 6.4 Thermal Information

| THERMAL METRIC (1) | THERMAL METRIC (1) | TLV767 - DBV (SOT23) - 5 PINS | TLV767 - DGN (HVSSOP) - 8 PINS | TLV767 - DRV (WSON) - 6 PINS | UNIT |
| - | - | - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 165.7 | 60.1 | 77.7 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 61.6 | 81.7 | 92.3 | °C/W |
| RθJB | Junction-to-board thermal resistance | 37.9 | 32.8 | 40.8 | °C/W |
| ΨJT | Junction-to-top characterization parameter | 11.6 | 6 | 4.3 | °C/W |
| ΨJB | Junction-to-board characterization parameter | 37.6 | 32.7 | 40.8 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | N/A | 15.5 | 18.9 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

## 6.5 Electrical Characteristics

Specified at TJ = -40°C to 125°C, VIN = VOUT(nom) + 1.5 V or VIN = 2.5 V (whichever is greater), FB/SNS tied to OUT, IOUT = 10 mA, VEN = 2 V, CIN = 1.0 µF, COUT = 1.0 µF (unless otherwise noted). Typical values are at TJ= 25ºC.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| VOUT | Nominal output accuracy | TJ = 25°C | -0.5 |  | 0.5 | % |
| VOUT | Output accuracy over temperature | VIN ≥ 3.0 V, 1 mA ≤ IOUT ≤ 1 A | -1 |  | 1 | % |
| VOUT | Output accuracy over temperature | 2.5 V ≤ VIN < 3.0 V, 1 mA ≤ IOUT ≤ 800 mA | -1 |  | 1 | % |
| VFB | Feedback voltage |  |  | 0.8 |  | V |
| VREF | Internal reference (adjustable device) | TJ = 25ºC | -0.5 |  | 0.5 | % |
| VREF | Internal reference (adjustable device) |  | -1 |  | 1 | % |
| IFB | Feedback pin current | VFB = 1 V |  | 10 | 50 | nA |
| ΔVOUT(ΔVIN) | Line regulation (1) | VOUT(NOM) +1.5 V ≤ VIN ≤ 16 V, IOUT = 10 mA |  |  | 0.02 | %/V |
| ΔVOUT(ΔIOUT) | Load regulation | 1 mA ≤ IOUT ≤ 1 A, VIN ≥ 3.0 V |  | 0.1 | 0.5 | %/A |
| ΔVOUT(ΔIOUT) | Load regulation | 1 mA ≤ IOUT ≤ 800 mA, 2.5 V ≤ VIN < 3.0 V |  | 0.1 | 0.5 | %/A |
| VDO | Dropout voltage (2) | VIN ≥ 3.0V, IOUT = 1 A, DGN package |  | 0.9 | 1.5 |  |
| VDO | Dropout voltage (2) | VIN ≥ 3.0V, IOUT = 1 A, DRV package |  | 0.9 | 1.4 | V |
| VDO | Dropout voltage (2) | 2.5 V ≤ VIN < 3.0 V, IOUT = 800 mA |  | 0.8 | 1.3 |  |
| ICL | Output current limit | VOUT = 0.9 x VOUT(NOM) , VIN ≥ 3.0V | 1.1 |  | 1.6 | A |
| ICL | Output current limit | VOUT = 0.9 x VOUT(NOM), 2.5 V ≤ VIN < 3.0 V | 0.81 |  | 1.6 | A |
| ISC | Short-circuit current limit | VOUT = 0 V, DGN package |  | 250 |  | mA |
| ISC | Short-circuit current limit | VOUT = 0 V, DRV package | 150 | 250 | 350 | mA |
| IQ | Quiescent current | IOUT = 0 mA |  | 50 | 80 | µA |
| IQ | Quiescent current | Fixed output devices, IOUT = 0 mA |  | 60 | 95 | µA |
| IGND | Ground current | IOUT = 1 A, VIN ≥ 3.0 V |  | 1.5 |  | mA |
| ISHUTDOWN | Shutdown current | VEN ≤ 0.4 V, VIN = 16 V |  | 1.5 | 3 | µA |
| VEN(HIGH) | Enable pin logic high | 2.5 V ≤ VIN ≤ 16 V | 1.2 |  |  | V |
| VEN(LOW) | Enable pin logic low | 2.5 V ≤ VIN ≤ 16 V |  |  | 0.4 | V |
| IEN | Enable pullup current | VEN = 0 V |  | 400 |  | nA |
| IPULLDOWN | Output pulldown current | VIN = 16 V, VOUT = 2.5 V, VEN=0V |  | 1.2 |  | mA |
| PSRR | Power-supply rejection ratio | VIN = 3.3 V, VOUT = 1.8 V, IOUT = 300 mA, f = 120 Hz |  | 70 |  | dB |
| Vn | Output noise voltage | BW = 10 Hz to 100 kHz, VIN = 3.3 V, VOUT = 0.8 V, IOUT = 100 mA |  | 60 |  | µVRMS |
| VUVLO+ | UVLO threshold rising | VIN rising |  | 2.2 | 2.4 | V |
| VUVLO(HYS) | UVLO hysteresis |  |  | 130 |  | mV |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_018.png)

## 6.5 Electrical Characteristics (continued)

Specified at TJ = -40°C to 125°C, VIN = VOUT(nom) + 1.5 V or VIN = 2.5 V (whichever is greater), FB/SNS tied to OUT, IOUT = 10 mA, VEN = 2 V, CIN = 1.0 µF, COUT = 1.0 µF (unless otherwise noted). Typical values are at TJ= 25ºC.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| VUVLO- | UVLO threshold falling | VIN falling | 1.9 |  |  | V |
| TSD(shutdown) | Thermal shutdown temperature | Temperature increasing | 180 |  |  | ºC |
| TSD(reset) | Thermal shutdown reset temperature | Temperature falling | 160 |  |  | ºC |

(1) Line regulation is measured with VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater)

(2) VDO is measured with VIN = 95% x VOUT(nom) for fixed output devices. VDO is not measured for fixed output devices when VOUT &lt; 2.5 V. For adjustable output device, VDO is measured with VFB = 95% x VFB(nom)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_019.png)

## 7 Typical Characteristics

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, VEN = 2.0 V, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_020.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_010.png)

## 7 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, VEN = 2.0 V, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_021.png)

## 7 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, VEN = 2.0 V, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_022.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_019.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_010.png)

## 7 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, VEN = 2.0 V, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_023.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_024.png)

## 7 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, VEN = 2.0 V, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_025.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_018.png)

## 7 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, VEN = 2.0 V, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_026.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_027.png)

## 8 Detailed Description

## 8.1 Overview

The TLV767 is a low quiescent current, high PSRR linear regulator capable of handling up to 1 A of load current. Unlike typical high current linear regulators, the TLV767 consumes significantly less quiescent current. This device is ideal for high current applications that require very sensitive power-supply rails.

This device features integrated foldback current limit, thermal shutdown, output enable, internal output pulldown and undervoltage lockout (UVLO). This device delivers excellent line and load transient performance. This device is low noise and exhibits a very good PSRR. The operating ambient temperature range of the device is -40°C to +125°C.

## 8.2 Functional Block Diagrams

Figure 8-1. Adjustable Version Block Diagram

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_028.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_010.png)

[www.ti.com](https://www.ti.com/)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_029.png)

Figure 8-2. Fixed Version Block Diagram

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_030.png)

## 8.3 Feature Description

## 8.3.1 Output Enable

The enable pin for the device is an active-high pin. The output voltage is enabled when the voltage of the enable pin is greater than the high-level input voltage of the EN pin and disabled with the enable pin voltage is less than the low-level input voltage of the EN pin. If independent control of the output voltage is not needed, connect the enable pin to the input of the device.

This device has an internal pullup current on the EN pin. The EN pin can be left floating to enable the device.

The device has an internal pulldown circuit that activates when the device is disabled to actively discharge the output voltage.

## 8.3.2 Dropout Voltage

Dropout voltage (VDO) is defined as the input voltage minus the output voltage (VIN - VOUT) at the rated output current (IRATED), where the pass transistor is fully on. IRATED is the maximum IOUT listed in the Recommended Operating Conditions table. The pass transistor is in the ohmic or triode region of operation, and acts as a switch. The dropout voltage indirectly specifies a minimum input voltage greater than the nominal programmed output voltage at which the output voltage is expected to stay in regulation. If the input voltage falls to less than the nominal output regulation, then the output voltage falls as well.

For a CMOS regulator, the dropout voltage is determined by the drain-source on-state resistance (RDS(ON)) of the pass transistor. Therefore, if the linear regulator operates at less than the rated current, the dropout voltage for that current scales accordingly. The following equation calculates the RDS(ON) of the device.

<!-- formula-not-decoded -->

## 8.3.3 Foldback Current Limit

The device has an internal current limit circuit that protects the regulator during transient high-load current faults or shorting events. The current limit is a hybrid brickwall-foldback scheme. The current limit transitions from a

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_031.png)

brickwall scheme to a foldback scheme at the foldback voltage (VFOLDBACK). In a high-load current fault with the output voltage above VFOLDBACK, the brickwall scheme limits the output current to the current limit (ICL). When the voltage drops below VFOLDBACK, a foldback current limit activates that scales back the current as the output voltage approaches GND. When the output is shorted, the device supplies a typical current called the short-circuit current limit (ISC). ICL and ISC are listed in the Electrical Characteristics table.

For this device, VFOLDBACK = 50% × VOUT(nom).

The output voltage is not regulated when the device is in current limit. When a current limit event occurs, the device begins to heat up because of the increase in power dissipation. When the device is in brickwall current limit, the pass transistor dissipates power [(VIN - VOUT) × ICL]. When the device output is shorted and the output is below VFOLDBACK, the pass transistor dissipates power [(VIN - VOUT) × ISC]. If thermal shutdown is triggered, the device turns off. After the device cools down, the internal thermal shutdown circuit turns the device back on. If the output current fault condition continues, the device cycles between current limit and thermal shutdown. For more information on current limits, see the Know Your Limits application report.

Figure 8-3 shows a diagram of the foldback current limit.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_032.png)

Figure 8-3. Foldback Current Limit

## 8.3.4 Undervoltage Lockout (UVLO)

The device has an independent undervoltage lockout (UVLO) circuit that monitors the input voltage, allowing a controlled and consistent turn on and off of the output voltage. To prevent the device from turning off if the input drops during turn on, the UVLO has hysteresis as specified in the Electrical Characteristics table.

## 8.3.5 Output Pulldown

The device has an output pulldown circuit. VOUT pulldown sink to ground capability is listed in the Electrical Characteristics table. The output pulldown activates under the following conditions:

- Device disabled
- 1.0 V &lt; VIN &lt; VUVLO

The output pulldown current for this device is 1.2 mA typical, as listed in the Electrical Characteristics table.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_018.png)

[www.ti.com](https://www.ti.com/)

Do not rely on the output pulldown circuit for discharging a large amount of output capacitance after the input supply has collapsed because reverse current can flow from the output to the input. This reverse current flow can cause damage to the device. See the Reverse Current section for more details.

## 8.3.6 Thermal Shutdown

The device contains a thermal shutdown protection circuit to disable the device when the junction temperature (TJ) of the pass transistor rises to TSD(shutdown) (typical). Thermal shutdown hysteresis assures that the device resets (turns on) when the temperature falls to TSD(reset) (typical).

The thermal time-constant of the semiconductor die is fairly short, thus the device may cycle on and off when thermal shutdown is reached until power dissipation is reduced. Power dissipation during start up can be high from large VIN - VOUT voltage drops across the device or from high inrush currents charging large output capacitors. Under some conditions, the thermal shutdown protection disables the device before start up completes.

For reliable operation, limit the junction temperature to the maximum listed in the Recommended Operating Conditions table. Operation above this maximum temperature causes the device to exceed its operational specifications. Although the internal protection circuitry of the device is designed to protect against thermal overall conditions, this circuitry is not intended to replace proper heat sinking. Continuously running the device into thermal shutdown or above the maximum recommended junction temperature reduces long-term reliability.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_019.png)

## 8.4 Device Functional Modes

## 8.4.1 Device Functional Mode Comparison

Table 8-1 shows the conditions that lead to the different modes of operation. See the Electrical Characteristics table for parameter values.

Table 8-1. Device Functional Mode Comparison

| OPERATING MODE | PARAMETER - VIN | PARAMETER - VEN | PARAMETER - IOUT | PARAMETER - TJ |
| - | - | - | - | - |
| Normal operation | VIN > VOUT(nom) + VDO and VIN > VIN(min) | VEN > VEN(HI) | IOUT < IOUT(max) | TJ < TSD(shutdown) |
| Dropout operation | VIN(min) < VIN < VOUT(nom) + VDO | VEN > VEN(HI) | IOUT < IOUT(max) | TJ < TSD(shutdown) |
| Disabled (any true condition disables the device) | VIN < VUVLO | VEN < VEN(LOW) | Not applicable | TJ > TSD(shutdown) |

## 8.4.2 Normal Operation

The device regulates to the nominal output voltage when the following conditions are met:

- The input voltage is greater than the nominal output voltage plus the dropout voltage (VOUT(nom) + VDO)
- The output current is less than the current limit (IOUT &lt; ICL)
- The device junction temperature is less than the thermal shutdown temperature (TJ &lt; TSD)
- The enable voltage has previously exceeded the enable rising threshold voltage and has not yet decreased to less than the enable falling threshold

## 8.4.3 Dropout Operation

If the input voltage is lower than the nominal output voltage plus the specified dropout voltage, but all other conditions are met for normal operation, the device operates in dropout mode. In this mode, the output voltage tracks the input voltage. During this mode, the transient performance of the device becomes significantly degraded because the pass transistor is in the ohmic or triode region, and acts as a switch. Line or load transients in dropout can result in large output-voltage deviations.

When the device is in a steady dropout state (defined as when the device is in dropout, VIN &lt; VOUT(NOM) + VDO, directly after being in a normal regulation state, but not during startup), the pass transistor is driven into the ohmic or triode region. When the input voltage returns to a value greater than or equal to the nominal output voltage plus the dropout voltage (VOUT(NOM) + VDO), the output voltage can overshoot for a short period of time while the device pulls the pass transistor back into the linear region.

## 8.4.4 Disabled

The output of the device can be shutdown by forcing the voltage of the enable pin to less than the maximum EN pin low-level input voltage (see the Electrical Characteristics table). When disabled, the pass transistor is turned off, internal circuits are shutdown, and the output voltage is actively discharged to ground by an internal discharge circuit from the output to ground.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_033.png)

[www.ti.com](https://www.ti.com/)

## 9 Application and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 9.1 Application Information

## 9.1.1 Adjustable Device Feedback Resistors

The adjustable-version device requires external feedback divider resistors to set the output voltage. VOUT is set using the feedback divider resistors, R1 and R2, according to the following equation:

<!-- formula-not-decoded -->

To ignore the FB pin current error term in the VOUT equation, set the feedback divider current to 100x the FB pin current listed in the Electrical Characteristics table. This setting provides the maximum feedback divider series resistance, as shown in the following equation:

<!-- formula-not-decoded -->

## 9.1.2 Recommended Capacitor Types

The device is designed to be stable using low equivalent series resistance (ESR) ceramic capacitors at the input and output. Multilayer ceramic capacitors have become the industry standard for these types of applications and are recommended, but must be used with good judgment. Ceramic capacitors that employ X7R-, X5R-, and C0G-rated dielectric materials provide relatively good capacitive stability across temperature, whereas the use of Y5V-rated capacitors is discouraged because of large variations in capacitance.

Regardless of the ceramic capacitor type selected, the effective capacitance varies with operating voltage and temperature. As a rule of thumb, expect the effective capacitance to decrease by as much as 50%. The input and output capacitors recommended in the Recommended Operating Conditions table account for an effective capacitance of approximately 50% of the nominal value.

## 9.1.3 Input and Output Capacitor Requirements

Although an input capacitor is not required for stability, good analog design practice is to connect a capacitor from IN to GND. This capacitor counteracts reactive input sources and improves transient response, input ripple, and PSRR. An input capacitor is recommended if the source impedance is more than 0.5 Ω. A higher value capacitor may be necessary if large, fast rise-time load or line transients are anticipated or if the device is located several inches from the input power source.

Dynamic performance of the device is improved with the use of an output capacitor. Use an output capacitor within the range specified in the Recommended Operating Conditions table for stability.

## 9.1.4 Reverse Current

Excessive reverse current can damage this device. Reverse current flows through the intrinsic body diode of the pass transistor instead of the normal conducting channel. At high magnitudes, this current flow degrades the long-term reliability of the device.

Conditions where reverse current can occur are outlined in this section, all of which can exceed the absolute maximum rating of VOUT ≤ VIN + 0.3 V.

- If the device has a large COUT and the input supply collapses with little or no load current
- The output is biased when the input supply is not established
- The output is biased above the input supply

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_027.png)

If reverse current flow is expected in the application, external protection is recommended to protect the device. Reverse current is not limited in the device, so external limiting is required if extended reverse voltage operation is anticipated.

Figure 9-1 shows one approach for protecting the device.

Figure 9-1. Example Circuit for Reverse Current Protection Using a Schottky Diode

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_034.png)

## 9.1.5 Feed-Forward Capacitor (CFF)

For the adjustable-voltage version device, a feed-forward capacitor (CFF) can be connected from the OUT pin to the FB pin. CFF improves transient, noise, and PSRR performance, but is not required for regulator stability. Recommended CFF values are listed in the Recommended Operating Conditions table. A higher capacitance CFF can be used; however, the start-up time increases. For a detailed description of CFF tradeoffs, see the Pros and Cons of Using a Feedforward Capacitor with a Low-Dropout Regulator application report.

CFF and R1 form a zero in the loop gain at frequency fZ, while CFF, R1, and R2 form a pole in the loop gain at frequency fP. CFF zero and pole frequencies can be calculated from the following equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

CFF ≥ 10 pF is required for stability if the feedback divider current is less than 5 µA. Equation 6 calculates the feedback divider current.

<!-- formula-not-decoded -->

To avoid start-up time increases from CFF, limit the product CFF × R1 &lt; 50 µs.

For an output voltage of 0.8 V with the FB pin tied to the OUT pin, no CFF is used.

## 9.1.6 Power Dissipation (PD)

Circuit reliability requires consideration of the device power dissipation, location of the circuit on the printed circuit board (PCB), and correct sizing of the thermal plane. The PCB area around the regulator must have few or no other heat-generating devices that cause added thermal stress.

To first-order approximation, power dissipation in the regulator depends on the input-to-output voltage difference and load conditions. The following equation calculates power dissipation (PD).

<!-- formula-not-decoded -->

Note

Power dissipation can be minimized, and therefore greater efficiency can be achieved, by correct selection of the system voltage rails. For the lowest power dissipation use the minimum input voltage required for correct output regulation.

For devices with a thermal pad, the primary heat conduction path for the device package is through the thermal pad to the PCB. Solder the thermal pad to a copper pad area under the device. This pad area must contain an array of plated vias that conduct heat to additional copper planes for increased heat dissipation.

The maximum power dissipation determines the maximum allowable ambient temperature (TA) for the device. According to the following equation, power dissipation and junction temperature are most often related by the

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_035.png)

junction-to-ambient thermal resistance (RθJA) of the combined PCB and device package and the temperature of the ambient air (TA).

<!-- formula-not-decoded -->

Thermal resistance (RθJA) is highly dependent on the heat-spreading capability built into the particular PCB design, and therefore varies according to the total copper area, copper weight, and location of the planes. The junction-to-ambient thermal resistance listed in the Thermal Information table is determined by the JEDEC standard PCB and copper-spreading area, and is used as a relative measure of package thermal performance.

## 9.1.7 Estimating Junction Temperature

The JEDEC standard now recommends the use of psi (Ψ) thermal metrics to estimate the junction temperatures of the linear regulator when in-circuit on a typical PCB board application. These metrics are not thermal resistance parameters and instead offer a practical and relative way to estimate junction temperature. These psi metrics are determined to be significantly independent of the copper area available for heat-spreading. The Thermal Information table lists the primary thermal metrics, which are the junction-to-top characterization parameter (ψJT) and junction-to-board characterization parameter (ψJB). These parameters provide two methods for calculating the junction temperature (TJ), as described in the following equations. Use the junction-to-top characterization parameter (ψJT) with the temperature at the center-top of device package (TT) to calculate the junction temperature. Use the junction-to-board characterization parameter (ψJB) with the PCB surface temperature 1 mm from the device package (TB) to calculate the junction temperature.

<!-- formula-not-decoded -->

## where:

- PD is the dissipated power
- TT is the temperature at the center-top of the device package

<!-- formula-not-decoded -->

## where

- TB is the PCB surface temperature measured 1 mm from the device package and centered on the package edge

For detailed information on the thermal metrics and how to use them, see the Semiconductor and IC Package Thermal Metrics application report.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_027.png)

## 9.2 Typical Application

This section discusses implementing this device for a typical application. Figure 9-2 shows the application circuit.

Figure 9-2. Typical Application Circuit

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_036.png)

## 9.2.1 Design Requirements

Table 9-1 summarizes the design requirements for this application.

Table 9-1. Design Parameters

| PARAMETER | DESIGN REQUIREMENT |
| - | - |
| Input voltage | 5 V |
| Output voltage | 3.3 V |
| Output current | 100 mA |

## 9.2.2 Detailed Design Procedure

## 9.2.2.1 Transient Response

As with any regulator, increasing the size of the output capacitor reduces overshoot and undershoot magnitude. If load transients are expected with ramp rates greater than 0.5 A/µs, use a 2.2-µF or larger output capacitor.

## 9.2.2.2 Choose Feedback Resistors

For this design example, VOUT is set to 3.3 V. Equation 11 and Equation 12 set the feedback divider resistors for the desired output voltage:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For improved output accuracy, use Equation 12 and IFB = 50 nA as listed in the Electrical Characteristics table to calculate the upper limit for series feedback resistance (R1 + R2 ≤ 660 kΩ).

The control-loop error amplifier drives the FB pin to the same voltage as the internal reference (VFB = 0.8 V, as listed in the Electrical Characteristics table). Use Equation 11 to determine the ratio of R1 / R2 = 3.125. Use this ratio and solve Equation 12 for R2. Now calculate the upper limit for R2 ≤ 160 kΩ. Select a standard value resistor for R2 = 160 kΩ.

Reference Equation 11 and solve for R1:

<!-- formula-not-decoded -->

From Equation 13, R1 = 500 kΩ can be determined. Select a standard value resistor for R1 = 499 kΩ. VOUT = 3.3 V (as determined by Equation 11).

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_010.png)

## 9.2.3 Application Curves

Figure 9-3. Load Transient Response, IOUT 0 mA to 100 mA

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_037.png)

## 10 Power Supply Recommendations

This device is designed to operate from an input supply voltage range of 2.5 V to 16 V. To ensure that the output voltage is well regulated and dynamic performance is optimum, the input supply must be at least VOUT(nom) + 1.5 V. For 1-A output current operation, the input supply must be 3 V or greater. Connect a low output impedance power supply directly to the input pin of the TLV767.

VIN = 5 V, VOUT = 3.3 V, COUT = 1 µF, CFF = 0 pF Figure 9-4. PSRR Performance

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_038.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_039.png)

## 11 Layout

## 11.1 Layout Guidelines

- Place input and output capacitors as close to the device as possible
- Use copper planes for device connections to IN, OUT, and GND pins to optimize thermal performance
- Place thermal vias around the device to distribute heat

## 11.2 Layout Examples

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_040.png)

- Represents via used for application-specific connections
- Represents via used for application-specific connections
- Represents via used for application-specific connections
- Represents via used for application-specific connections

Figure 11-1. Layout Example for the Adjustable WSON Version

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_041.png)

Figure 11-3. Layout Example for the Fixed HVSSOP Version

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_042.png)

Figure 11-2. Layout Example for the Fixed WSON Version

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_043.png)

Figure 11-4. Layout Example for the Adjustable HVSSOP Version

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_044.png)

Figure 11-5. Layout Example for the Fixed DBV Version

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_045.png)

[www.ti.com](https://www.ti.com/)

## 12 Device and Documentation Support

## 12.1 Device Support

## 12.1.1 Device Nomenclature

| PRODUCT | VOUT |
| - | - |
| TLV767xx(x)yyyz | xx(x) is nominal output voltage. For output voltages with a resolution of 100 mV, two digits are used in the ordering number; otherwise, three digits are used (for example, 33 = 3.3 V; 125 = 1.25 V). 01 indicates adjustable output version. yyy is package designator. z is package quantity. R is for large quantity reel, T is for small quantity reel. |

## Table 12-1. Available Options (1)

(1) For the most current package and ordering information, see the Package Option Addendum at the end of this document, or visit the device product folder at www.ti.com.

## 12.2 Documentation Support

## 12.2.1 Related Documentation

For related documentation see the following:

- [Texas Instruments, TLV767EVM-014 Evaluation module user's guide](https://www.ti.com/lit/pdf/SBVU049)
- Texas Instruments, Pros and cons of using a feedforward capacitor with a low-dropout regulator application report
- [Texas Instruments, Know your limits application report](https://www.ti.com/lit/pdf/snva736)
- Texas Instruments, Universal low-dropout (LDO) linear voltage regulator MultiPkgLDOEVM-823 evaluation module user's guide

## 12.3 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 12.4 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 12.5 Trademarks

TI E2E™ is a trademark of Texas Instruments.

All trademarks are the property of their respective owners.

## 12.6 Electrostatic Discharge Caution

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_046.png)

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 12.7 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

## Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_047.png)

INSTRUMENTS

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| TLV76701DGNR | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BKX |
| TLV76701DGNR.A | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BKX |
| TLV76701DRVR | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RMH |
| TLV76701DRVR.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RMH |
| TLV76701DRVT | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAU &#124; NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 1RMH |
| TLV76701DRVT.A | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RMH |
| TLV76701DRVTG4 | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RMH |
| TLV76701DRVTG4.A | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RMH |
| TLV76708DGNR | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BLX |
| TLV76708DGNR.A | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BLX |
| TLV76708DRVR | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1RNH |
| TLV76708DRVR.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1RNH |
| TLV76708DRVT | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1RNH |
| TLV76708DRVT.A | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1RNH |
| TLV76718DGNR | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BMX |
| TLV76718DGNR.A | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BMX |
| TLV76718DRVR | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1ROH |
| TLV76718DRVR.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1ROH |
| TLV76718DRVT | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1ROH |
| TLV76718DRVT.A | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1ROH |
| TLV76725DGNR | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2GT7 |
| TLV76725DGNR.A | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2GT7 |
| TLV76728DGNR | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BNX |
| TLV76728DGNR.A | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BNX |
| TLV76728DRVR | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1RPH |
| TLV76728DRVR.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1RPH |
| TLV76728DRVT | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1RPH |
| TLV76728DRVT.A | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1RPH |
| TLV76733DGNR | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BOX |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_048.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

25-Jul-2026

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| TLV76733DGNR.A | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BOX |
| TLV76733DRVR | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU &#124; NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 1RQH |
| TLV76733DRVR.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RQH |
| TLV76733DRVRG4 | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RQH |
| TLV76733DRVRG4.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RQH |
| TLV76733DRVT | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1RQH |
| TLV76733DRVT.A | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1RQH |
| TLV76750DGNR | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BPX |
| TLV76750DGNR.A | Active | Production | HVSSOP (DGN) &#124; 8 | 2500 &#124; LARGE T&R | Yes | NIPDAUAG | Level-2-260C-1 YEAR | -40 to 125 | 2BPX |
| TLV76750DRVR | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1RRH |
| TLV76750DRVR.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1RRH |
| TLV76750DRVRG4 | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RRH |
| TLV76750DRVRG4.A | Active | Production | WSON (DRV) &#124; 6 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | 1RRH |
| TLV76750DRVT | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | NIPDAUAG &#124; SN | Level-2-260C-1 YEAR | -40 to 125 | 1RRH |
| TLV76750DRVT.A | Active | Production | WSON (DRV) &#124; 6 | 250 &#124; SMALL T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 1RRH |
| TLV76780DBVR | Active | Production | SOT-23 (DBV) &#124; 5 | 3000 &#124; LARGE T&R | Yes | NIPDAU &#124; SN | Level-1-260C-UNLIM | -40 to 125 | 2D2T |
| TLV76780DBVR.A | Active | Production | SOT-23 (DBV) &#124; 5 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 2D2T |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_048.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

25-Jul-2026

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

## OTHER QUALIFIED VERSIONS OF TLV767 :

- Automotive : TLV767-Q1

NOTE: Qualified Version Definitions:

- Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_049.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

3-Sep-2026

## TAPE AND REEL INFORMATION

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_050.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_051.png)

## *All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| TLV76701DGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1 |
| TLV76701DRVR | WSON | DRV | 6 | 3000 | 178.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76701DRVT | WSON | DRV | 6 | 250 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76701DRVTG4 | WSON | DRV | 6 | 250 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76708DGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1 |
| TLV76708DRVR | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76708DRVT | WSON | DRV | 6 | 250 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76718DGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1 |
| TLV76718DRVR | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76718DRVR | WSON | DRV | 6 | 3000 | 178.0 | 8.4 | 2.25 | 2.25 | 1.0 | 4.0 | 8.0 | Q2 |
| TLV76718DRVT | WSON | DRV | 6 | 250 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76725DGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1 |
| TLV76728DGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1 |
| TLV76728DRVR | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76728DRVT | WSON | DRV | 6 | 250 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76733DGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1 |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_052.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

3-Sep-2026

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| TLV76733DRVR | WSON | DRV | 6 | 3000 | 178.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76733DRVRG4 | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76733DRVT | WSON | DRV | 6 | 250 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76750DGNR | HVSSOP | DGN | 8 | 2500 | 330.0 | 12.4 | 5.3 | 3.4 | 1.4 | 8.0 | 12.0 | Q1 |
| TLV76750DRVR | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76750DRVR | WSON | DRV | 6 | 3000 | 178.0 | 8.4 | 2.25 | 2.25 | 1.0 | 4.0 | 8.0 | Q2 |
| TLV76750DRVRG4 | WSON | DRV | 6 | 3000 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76750DRVT | WSON | DRV | 6 | 250 | 180.0 | 8.4 | 2.3 | 2.3 | 1.15 | 4.0 | 8.0 | Q2 |
| TLV76780DBVR | SOT-23 | DBV | 5 | 3000 | 178.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3 |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_053.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

3-Sep-2026

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_054.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| TLV76701DGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0 |
| TLV76701DRVR | WSON | DRV | 6 | 3000 | 208.0 | 191.0 | 35.0 |
| TLV76701DRVT | WSON | DRV | 6 | 250 | 210.0 | 185.0 | 35.0 |
| TLV76701DRVTG4 | WSON | DRV | 6 | 250 | 210.0 | 185.0 | 35.0 |
| TLV76708DGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0 |
| TLV76708DRVR | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| TLV76708DRVT | WSON | DRV | 6 | 250 | 210.0 | 185.0 | 35.0 |
| TLV76718DGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0 |
| TLV76718DRVR | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| TLV76718DRVR | WSON | DRV | 6 | 3000 | 205.0 | 200.0 | 33.0 |
| TLV76718DRVT | WSON | DRV | 6 | 250 | 210.0 | 185.0 | 35.0 |
| TLV76725DGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0 |
| TLV76728DGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0 |
| TLV76728DRVR | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| TLV76728DRVT | WSON | DRV | 6 | 250 | 210.0 | 185.0 | 35.0 |
| TLV76733DGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0 |
| TLV76733DRVR | WSON | DRV | 6 | 3000 | 208.0 | 191.0 | 35.0 |
| TLV76733DRVRG4 | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_052.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

3-Sep-2026

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| TLV76733DRVT | WSON | DRV | 6 | 250 | 210.0 | 185.0 | 35.0 |
| TLV76750DGNR | HVSSOP | DGN | 8 | 2500 | 366.0 | 364.0 | 50.0 |
| TLV76750DRVR | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| TLV76750DRVR | WSON | DRV | 6 | 3000 | 205.0 | 200.0 | 33.0 |
| TLV76750DRVRG4 | WSON | DRV | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| TLV76750DRVT | WSON | DRV | 6 | 250 | 210.0 | 185.0 | 35.0 |
| TLV76780DBVR | SOT-23 | DBV | 5 | 3000 | 208.0 | 191.0 | 35.0 |

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_055.png)

SCALE 4.0 0

## SOT-23 - 1.45 mm max height

SMALL OUTLINE TRANSISTOR

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_056.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Refernce JEDEC MO-178.
4. Body dimensions do not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.25 mm per side.
5. Support pin may differ or may not be present.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_057.png)

SMALL OUTLINE TRANSISTOR

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_058.png)

NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_059.png)

## EXAMPLE STENCIL DESIGN

## SOT-23 - 1.45 mm max height

SMALL OUTLINE TRANSISTOR

SOLDER PASTE EXAMPLE BASED ON 0.125 mm THICK STENCIL SCALE:15X

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_060.png)

4214839/K 08/2024

NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
9. Board assembly site may have different recommendations for stencil design.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_057.png)

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_061.png)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_062.png)

INSTRUMENTS

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_063.png)

## WSON - 0.8 mm max height

SCALE 5.50

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_064.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.
4. Minimum 0.1 mm solder wetting on pin side wall. Available for wettable flank version only.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_065.png)

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_066.png)

NOTES: (continued)

5. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
6. Vias are optional depending on application, refer to device data sheet. If some or all are implemented, recommended via locations are shown.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_057.png)

## WSON - 0.8 mm max height

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_067.png)

## SOLDER PASTE EXAMPLE

BASED ON 0.125 mm THICK STENCIL

EXPOSED PAD #7 88% PRINTED SOLDER COVERAGE BY AREA UNDER PACKAGE SCALE:30X

4222173/C 11/2025

NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_057.png)

DGN 8

GENERIC PACKAGE VIEW

TM

PowerPAD HVSSOP - 1.1 mm max height

3 x 3, 0.65 mm pitch SMALL OUTLINE PACKAGE

This image is a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_068.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_069.png)

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_070.png)

## PACKAGE OUTLINE

## PowerPAD HVSSOP - 1.1 mm max height TM

SCALE 4.0

SMALL OUTLINE PACKAGE

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_071.png)

## NOTES:

PowerPAD is a trademark of Texas Instruments.

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-187.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_072.png)

## PowerPAD HVSSOP - 1.1 mm max height TM

SMALL OUTLINE PACKAGE

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_073.png)

## NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.
8. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown on this view. It is recommended that vias under paste be filled, plugged or tented.
9. Size of metal pad may vary due to creepage requirement.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_072.png)

## PowerPAD HVSSOP - 1.1 mm max height TM

| STENCIL THICKNESS | SOLDER STENCIL OPENING |
| - | - |
| 0.1 | 1.76 X 2.11 |
| 0.125 | 1.57 X 1.89 (SHOWN) |
| 0.15 | 1.43 X 1.73 |
| 0.175 | 1.33 X 1.60 |

SMALL OUTLINE PACKAGE

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_074.png)

## NOTES: (continued)

10. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
11. Board assembly site may have different recommendations for stencil design.

![Image](TLV767%20Datasheet%20%28TI%20SLVSE84D%29_files/img_072.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2026, Texas Instruments Incorporated Last updated 10/2025
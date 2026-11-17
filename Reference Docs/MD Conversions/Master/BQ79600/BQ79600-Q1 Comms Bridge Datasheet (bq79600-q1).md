<!-- Converted from BQ79600-Q1 Comms Bridge Datasheet (bq79600-q1).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_001.png)

[BQ79600-Q1](http://www.ti.com/product/BQ79600-Q1)

SLUSDS1A - NOVEMBER 2019 - REVISED AUGUST 2020

## BQ79600-Q1 Automotive SPI/UART Communication Interface Functional-Safety Compliant With Automatic Host Wakeup

## 1 Features

- Qualified for automotive applications
- AEC-Q100 Qualified with the following results:
- Device temperature grade 1: -40°C to +125°C ambient operating temperature range
- Device HBM ESD classification level 2
- Device CDM ESD classification level C4B
- [Functional Safety-Compliant](http://www.ti.com/technologies/functional-safety/overview.html)
- Developed for functional safety applications
- Documentation available to aid ISO 26262 system design
- [Safety Manual](https://www.ti.com/lit/pdf/slua984)
- [Functional Safety Analysis Report](https://www.ti.com/lit/pdf/sluaa63)
- Systematic capability up to ASIL-D
- Hardware capability up to ASIL-D
- Automatic wake up of BMS/BMU system when fault is detected in ring architecture
- Support supply from 4.75-V to 40-V
- UART/SPI Host interface
- Compatible with 3.3-V/5-V logic
- Isolated differential daisy chain
- Support ring architecture with one device
- Support transformer/ capacitor isolation
- Designed for BCI/EMI/EMC robustness
- Supports BQ7961X-Q1 family, BQ7965X, BQ7963X and future products

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_002.png)

Optional: Ring Enables Fault and Reverse Wakeup Feature

## Simplified System Diagram

Product Folder Links: BQ79600-Q1

## 2 Applications

- [Battery management system (BMS)](http://www.ti.com/solution/battery-management-system-bms)
- [Other HEV/EV](http://www.ti.com/applications/automotive/hev-ev-powertrain/overview.html)
- Fuel cell
- Energy storage

## 3 Description

The BQ79600-Q1 is a communication (bridge) IC designed to interface between a microcontroller (MCU) and TI battery monitoring ICs, for example the BQ7961X-Q1. The information from the MCU is translated by the device to signals recognized by TI's battery management daisy chain protocol, and transmitted out. And signals from daisy chain are decoded to bit stream and then sent back to MCU.

When the MCU and PMIC are in SHUTDOWN/ SLEEP, the BQ79600-Q1 can wake them up if any unmasked fault is detected when using ring architecture.

## Device Information

| PART NUMBER (1) | PACKAGE | BODY SIZE (NOM) |
| - | - | - |
| BQ79600-Q1 | TSSOP (16-pin) | 6.6 mm × 5.1 mm |

- (1) For all available packages, see the orderable addendum at the end of the data sheet.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_003.png)

1

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_004.png)

## Table of Contents

| 1 Features............................................................................1 | 7.5 Register Maps...........................................................37 |
| - | - |
| 2 Applications.....................................................................1 | 8 Application and Implementation..................................55 |
| 3 Description.......................................................................1 | 8.1 Application Information............................................. 55 |
| 4 Revision History.............................................................. 2 | 8.2 Typical Applications.................................................. 55 |
| 5 Pin Configuration and Functions...................................3 | 9 Power Supply Recommendations................................59 |
| Pin Functions.................................................................... 3 | 10 Layout...........................................................................60 |
| 6 Specifications.................................................................. 4 | 10.1 Layout Guidelines................................................... 60 |
| 6.1 Absolute Maximum Ratings ....................................... 4 | 10.2 Layout Example...................................................... 60 |
| 6.2 ESD Ratings .............................................................. 4 | 11 Device and Documentation Support..........................63 |
| 6.3 Recommended Operating Conditions ........................4 | 11.1 Device Support........................................................63 |
| 6.4 Thermal Information ...................................................4 | 11.2 Third-Party Products Disclaimer............................. 63 |
| 6.5 Electrical Characteristics ............................................5 | 11.3 Receiving Notification of Documentation Updates.. 63 |
| 6.6 Timing Requirements .................................................6 | 11.4 Support Resources................................................. 63 |
| 6.7 Typical Characteristics................................................9 | 11.5 Trademarks............................................................. 63 |
| 7 Detailed Description......................................................10 | 11.6 Electrostatic Discharge Caution.............................. 63 |
| 7.1 Overview...................................................................10 | 11.7 Glossary..................................................................63 |
| 7.2 Functional Block Diagram.........................................10 7.3 Feature Description...................................................10 | 12 Mechanical, Packaging, and Orderable |
| 7.4 Device Functional Modes..........................................36 | Information.................................................................... 64 |
| 4 Revision History | 4 Revision History |
| Changes from Revision * (November 2019) to Revision A (June 2020) · Changed from Advance Information to Production | Page Data.................................................................................... 1 |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

## 5 Pin Configuration and Functions

Figure 5-1. PW Package 16-Pin TSSOP Top View

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_006.png)

## Pin Functions

| PIN - NAME | PIN - NO. | TYPE (1) | DESCRIPTION |
| - | - | - | - |
| VIO | 3 | P | Power supply input for UART/SPI input/output pins. Decouple with a 0.1μF capacitor to GND. VIO should be powered before SCLK, nCS, RX/MOSI, TX/MISO, NFAULT, nUART/SPI (SPI_RDY) is driven. |
| SCLK | 6 | DI | SPI clock input. If SPI interface is used, this pin is connected to SPI master controller. Connect to GND with a 10-100kohm pull-down resistor. If not used, connect to GND. |
| nCS | 7 | DI | Active low chip select pin for SPI interface. Connect to VIO with 10-100kohm pull-up resistor in SPI mode. Cannot hardwire to GND in SPI mode. Connect to GND in UART mode. |
| RX/MOSI | 4 | DI | UART receiver input or SPI master out slave in. Connect to VIO with a 10-100kohm pull-up resistor. Don't leave it unconnected. |
| TX/MISO | 5 | DO | UART transmitter output or SPI master in slave out. Pull up to VIO with a 10-100kohm pull-up resistor at MCU side. MISO pin drives high in SPI idle mode, cannot directly support SPI multidrop, if multidrop is needed, add a tri-state buffer between BQ79600-Q1 and MCU. |
| NFAULT | 2 | DO | Fault indication output. Open drain active low. Pull up to VIO with 100kohm resistor. Connect NFAULT to host MCU GPIO. If not used, connect to GND. |
| nUART/SPI (SPI_RDY) | 8 | DI/O | If used as UART mode, connect this pin to GND. If used as SPI mode, connect to VIO through 10-100kohm pull up resistor and connect this pin to MCU GPIO. This pin is used as an input pin to select SPI or UART interface before device finishes wakeup/reset initialization (SPI communication is ready). If SPI mode is selected, SPI_RDY has to be used by host to decide if read/write can be initiated or needing further wait. Refer to Section 7.3.2.1.2.2.1 details. |
| DVDD | 1 | P | 1.8V regulated output. DVDD supplies the internal digital circuits. Bypass DVDD with a 0.22μF (recommended) or a 0.47μF capacitor to GND. |
| GND | 9 | P | Ground. |
| CVDD | 14 | P | Dedicated 5V supply used for the daisy chain communications. Decouple with a 0.22μF (recommended) or a 0.47μF to GND. |
| COMHN | 12 | AC-I/O | This is an AC coupled bi-directional I/O pin for daisy chain (VIF) communication. Do not apply external DC voltage to this pin. Shall connect to COMLN/P of adjacent device through proper |
| COMHP | 13 | AC-I/O | isolation, see Section 7.3.2.1.1. Leave unconnected if (Ring Architecture) not used. |
| COMLN | 11 | AC-I/O | This is an AC coupled bi-directional I/O pin for daisy chain (VIF) communication. Do not apply external DC voltage to this pin. Shall connect to COMHN/P of adjacent device through proper |
| COMLP | 10 | AC-I/O | isolation, see Section 7.3.2.1.1. Leave unconnected if (Ring Architecture) not used. |
| INH | 16 | HV-O | Inhibit pin (PMOS open drain) to control system voltage regulators, connect 100kohm resistor to GND. If reverse wake up feature is not used, connect this pin to BAT pin. Don't leave this pin floating. |
| BAT | 15 | HV-P | Battery supply Input. Supply internal LDOs and wakeup circuit. Connect to external supply through 10ohm resistor. Bypass to GND with 0.1μF. |

- (1) DI = digital input, DO = digital output, HV = high voltage

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_007.png)

## 6 Specifications

## 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted) (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Input Voltage | BAT to GND | -0.3 | 40 | V |
| Input Voltage | INH to GND (INH is lower than BAT) | -0.3 | 40 | V |
| Input Voltage | VIO, CVDD to GND | -0.3 | 5.5 | V |
| Input Voltage | DVDD to GND | -0.3 | 1.98 | V |
| Input Voltage | MISO/TX, MOSI/RX, nCS, SCLK, NFAULT, nUART/SPI(SPI_RDY) to GND | -0.3 | VIO+0.3 | V |
| Input Voltage | COMHP, COMHN, COMLP, COMLN to GND | -10 | 10 | V |
| Input Voltage | COMHP to COMHN, COMLP to COMLN | -6.5 | 6.5 | V |
| INH current |  |  | 4 | mA |
| I/O current | MISO/TX current (100pF load, VIO=5V, 10ns transition-time) |  | 8 | mA |
| TA | Ambient temperature | -40 | 125 | °C |
| TJ | Junction temperature | -40 | 150 | °C |
| Tstg | Storage temperature | -65 | 150 | °C |

(1) Stresses beyond those listed under Absolute Maximum Rating may caµse permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Condition. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

## 6.2 ESD Ratings

|  |  |  |  | VALUE | UNIT |
| - | - | - | - | - | - |
| V(ESD) | Electrostatic discharge | Human body model (HBM), per AEC Q100-002 (1) | Human body model (HBM), per AEC Q100-002 (1) | ±2000 | V |
|  |  | Charged device model (CDM), per | Corner pins (1, 8, 9 and 16) | ±750 | V |
|  |  | AEC Q100-011 | Other pins | ±500 | V |

(1) AEC Q100-002 indicates that HBM stressing shall be in accordance with the ANSI/ESDA/JEDEC JS-001 specification.

## 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|  |  | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - |
| VBAT, INH | BAT, INH (INH is equal to or lower than BAT) (Powered by 12V Battery) | 5.5 |  | 24 | V |
| VVIO_RANGE | VIO input (applies to nCS, MOSI/RX, MISO/TX, SLCK, nUART/SPI (SPI_RDY), NFAULT) | 3.135 |  | 5.25 | V |
| IMISO/TX | MISO/TX current |  |  | 3 | mA |
| IINH | INH output current |  |  | 2 | mA |
| TA | Operation temperature | -40 |  | 125 | °C |

## 6.4 Thermal Information

| THERMAL METRIC (1) | THERMAL METRIC (1) | BQ79600-Q1 PW(TSSOP) 16 PINS | UNIT |
| - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 102 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 28.9 | °C/W |
| RθJB | Junction-to-board thermal resistance | 49 | °C/W |
| ΨJT | Junction-to-top characterization parameter | 14 | °C/W |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

[www.ti.com](http://www.ti.com/)

| THERMAL METRIC (1) | BQ79600-Q1 PW(TSSOP) 16 PINS | UNIT |
| - | - | - |
| ΨJB Junction-to-board characterization parameter | 48.2 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

## 6.5 Electrical Characteristics

VIO = 3.3V, over operating free-air temperature range (unless otherwise noted)

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| OPERATION VOLTAGE | OPERATION VOLTAGE | OPERATION VOLTAGE | OPERATION VOLTAGE | OPERATION VOLTAGE | OPERATION VOLTAGE | OPERATION VOLTAGE |
| VBAT |  | When reverse wakeup feature is used, BAT pin is powered by "12V battery" | 5.5 |  | 24 | V |
| VBAT |  | When reverse wakeup feature is not used, BAT/CVDD are powered by regulated 5V | 4.75 |  | 5.25 | V |
| THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN | THERMAL SHUTDOWN |
| TSHUT_R | Thermal shutdown (rising direction) | DieTemp sensor | 126 | 138 | 150 | °C |
| TSHUT_F | Thermal shutdown (falling direction) | DieTemp sensor | 116 |  | 141 | °C |
| SUPPLY CURRENTS | SUPPLY CURRENTS | SUPPLY CURRENTS | SUPPLY CURRENTS | SUPPLY CURRENTS | SUPPLY CURRENTS | SUPPLY CURRENTS |
| ISHDN_1 | Supply current in SHUTDOWN mode device powered by regulated 5V supply | VBAT shorted to CVDD, both equal to 5V, measured through GND pin |  |  | 7 | µA |
| ISHDN_2 | Supply current in SHUTDOWN mode powered by "12V" battery directly | VBAT= 17V, CVDD self powered, measured through GND pin |  |  | 9 | µA |
| IVALIDATE | Supply current in VALIDATE mode | Current on BAT pin |  |  | 168 | µA |
| ISLP(IDLE) | Baseline supply current in SLEEP mode | Current on BAT pin, no fault, COMH and COML RX disabled, no HB TX |  |  | 110 | µA |
| ISLP_RX_O N | Additional supply current to SLEEP mode base line | When COML OR COMH RX is on |  | 35 |  | µA |
| ISLP_TX_O N | Additional supply current to SLEEP mode base line | When COML or COMH tone transmiter is on (HB tone) |  |  | 8 | µA |
| IACT(IDLE) | Baseline supply current in ACTIVE mode | Current on BAT pin, no fault, no communication, Tone RX/TX is off |  | 3 | 4 | mA |
| ICOMT | Additional average current for one of BQ79600 daisy chain transmitters is on | Average current into VBAT when BQ79600 transmits 14 bytes of data (brdcast write 8 bytes of 0x00 into address 0X1B) |  | 10 |  | mA |
| Supplies (AVAO_REF, always on internal supply) | Supplies (AVAO_REF, always on internal supply) | Supplies (AVAO_REF, always on internal supply) | Supplies (AVAO_REF, always on internal supply) | Supplies (AVAO_REF, always on internal supply) | Supplies (AVAO_REF, always on internal supply) | Supplies (AVAO_REF, always on internal supply) |
| VAVAORE G | AVAOREG voltage | VBAT > min VBAT |  | 2.45 |  | V |
| VAVDDREF _OV | AVDDREF OV threshold | VBAT > min VBAT, hys = 130mV | 2.8 |  | 3.1 | V |
| Supplies (CVDD) | Supplies (CVDD) | Supplies (CVDD) | Supplies (CVDD) | Supplies (CVDD) | Supplies (CVDD) | Supplies (CVDD) |
| VCVDD | CVDD output voltage | No external load, CSUPPLIES = 0.22µF, ACTIVE mode | 4.9 | 5 | 5.1 | V |
| VCVDD_O V | CVDD OV rising threshold | Hys = 140mV | 5.3 | 5.5 | 5.65 | V |
| VCVDD_U V_F | CVDD UV falling threshold |  | 4.35 | 4.5 | 4.65 | V |
| VCVDD_U V_R | CVDD UV rising threshold |  | 4.45 | 4.6 | 4.75 | V |
| VCVDD_ILI MIT | CVDD current limit |  | 53 |  | 81 | mA |
| CCVDD | Capacitance range on CVDD pin | Not capacitor value | 0.1 |  | 0.8 | µF |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_008.png)

VIO = 3.3V, over operating free-air temperature range (unless otherwise noted)

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| Supplies (DVDD) | Supplies (DVDD) | Supplies (DVDD) | Supplies (DVDD) | Supplies (DVDD) | Supplies (DVDD) | Supplies (DVDD) |
| VDVDD | DVDD output voltage | No external load, CSUPPLIES = 0.22µF, ACTIVE mode | 1.75 | 1.8 | 1.85 | V |
| VDVDD_O V | DVDD OV rising threshold | Hys = 65mV | 1.9 |  | 2.1 | V |
| VDVDD_U V_F | DVDD UV falling threshold |  | 1.63 |  | 1.69 | V |
| VDVDD_U V_R | DVDD UV rising threshold |  | 1.68 |  | 1.75 | V |
| VDVDD_ILI MIT | DVDD current limit |  | 20 |  | 57 | mA |
| DDVDD | Load capacitance on DVDD pin | Not capacitor value | 0.1 |  | 0.8 | µF |
| SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR |
| VVAL_THR _P | Sniffer detector threshold, rising swing on COMHP has to be larger than value | Sniffer is enabled, and device is in SHUTDOWN mode | 3.2 |  | 3.6 | V |
| INH Driver | INH Driver | INH Driver | INH Driver | INH Driver | INH Driver | INH Driver |
| VDROP_IN H | When INH is pulled up, voltage drop from BAT to INH | IINH = -0.5mA |  | 0.5 | 1 | V |
| VINH_DET | Threshold to set [INH_STAT] to '1' |  | 2.2 |  |  | V |
| Reference Voltages | Reference Voltages | Reference Voltages | Reference Voltages | Reference Voltages | Reference Voltages | Reference Voltages |
| Digital I/Os (TX, RX, NFAULT) | Digital I/Os (TX, RX, NFAULT) | Digital I/Os (TX, RX, NFAULT) | Digital I/Os (TX, RX, NFAULT) | Digital I/Os (TX, RX, NFAULT) | Digital I/Os (TX, RX, NFAULT) | Digital I/Os (TX, RX, NFAULT) |
| VVIO_UV_ R | VIO UV rising | Hys = 200mV | 2.5 |  | 3.1 | V |
| VOH | Output as logic level high (TX) | FET pull up, Iout=1mA, VIO = 3.3V or 5V | VVIO-0.1 |  |  | V |
| VOL | Output as logic level low (TX) | FET pull down, Iout=1mA, VIO = 3.3V or 5V |  |  | 0.1 | V |
| VIH | Input as logic level high (RX), requirement for user | VIO = 3.3V or 5V | 0.75 x VVIO |  |  | V |
| VIL | Input as logic level low (RX), requirement for user | VIO = 3.3V or 5V |  |  | 0.25 x VVIO | V |
| RNFAULT | NFAULT pull down impedance | Use 100kohm external pull up |  |  | 1000 | Ω |
| Daisy-chain Communication Bus | Daisy-chain Communication Bus | Daisy-chain Communication Bus | Daisy-chain Communication Bus | Daisy-chain Communication Bus | Daisy-chain Communication Bus | Daisy-chain Communication Bus |
| VDCCM_1 | Common mode voltage (COML and COMH) | ACTIVE mode |  | 2.2 |  | V |
| VDCCM_2 | Common mode voltage (COML and COMH) | SLEEP or VALIDATE mode |  | 1 |  | V |
| VCOMM_D ATA | COMM port data receiver threshold range (VCOMP-VCOMN) |  | 1.04 |  | 1.75 | V |
| VCOMM_T ONE | COMM port HB/FAULT tone receiver threshold range (VCOMP-VCOMN) |  | 1.13 |  | 1.94 | V |

## 6.6 Timing Requirements

over operating free-air temperature range (unless otherwise noted)

| PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - |
| POWER STATE TIMING |  |  |  |  |  |
| tPOR2COM M | From VBAT (rising) > VPOR to device ready to receive WAKE ping, ramp up VBAT and VIO in 10µs |  |  | 1 | ms |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

## [www.ti.com](http://www.ti.com/)

## over operating free-air temperature range (unless otherwise noted)

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| tSU(WAKE_ SHUT) | Startup from SHUTDOWN/VALIDATE to ACTIVE mode | From receiving WAKE ping (RX ping going low-to-high) to device in ACTIVE mode (ready to do µART /SPI communication) (CVDD= 0.22µF capacitor DVDD = 0.22µF capacitor) |  | 2 | 3.5 | ms |
| tSU(SLP2A CT) | Startup from SLEEP to ACTIVE mode (with Sleep2active ping) | From receiving SLP2ACT ping (RX ping going low-to-high) to device in ACTIVE mode (ready to do UART / SPIcommunication) |  |  | 260 | µs |
| tSU(WAKE_ SLP) | Startup from SLEEP to ACTIVE mode (with WAKE ping) | From receiving WAKE ping (RX ping going low-to-high) to device in ACTIVE mode (ready to do UART / SPIcommunication) |  |  | 600 | µs |
| tRST | Reset time from ACTIVE mode to ACTIVE mode | From receiving WAKE ping (RX ping going low-to-high) or CONTROL1[SOFT_RESET]=1 to device in ACTIVE mode (ready to do UART /SPI communication) |  |  | 600 | µs |
| tSLP | From ACTIVE to SLEEP mode | From receiving SLEEP entry condition to enter in SLEEP mode |  |  | 100 | µs |
| tSHTDN | From ACTIVE/SLEEP/VALIDATE to SHUTDOWN mode | From receiving SHUTDOWN entry condition to enter in SHUTDOWN mode (CVDD<1.2V) |  |  | 5 | ms |
| tVALID_EN TRY | From SHUTDOWN to VALIDATE | From fault tone toggling on COM port to DVDD hit above 1.75V |  |  | 10 | ms |
| tVALID_TIM EOUT | time to validate fault tone before transition to SHUTDOWN state | Start from DVDD out of reset |  | 150 |  | ms |
| INH Driver TIMING | INH Driver TIMING | INH Driver TIMING | INH Driver TIMING | INH Driver TIMING | INH Driver TIMING | INH Driver TIMING |
| tINH_DLY | After device enters VALIDATE, from first couplet of fault tone to INH pulled high |  |  | 720 |  | µs |
| PING SIGNAL TIMING | PING SIGNAL TIMING | PING SIGNAL TIMING | PING SIGNAL TIMING | PING SIGNAL TIMING | PING SIGNAL TIMING | PING SIGNAL TIMING |
| tHLD_WAK E | From user perspective, WAKE ping low time on MOSI/RX pin | VBAT > VPOR, RX pin (low-pulse width) VIO = 3.3 or 5V | 2.5 |  | 3 | ms |
| tHLD_SD | From user perspective, SHUTDOWN ping low time on MOSI/RX pin | VBAT > VPOR, RX pin (low-pulse width) VIO = 3.3 or 5V | 12.5 |  |  | ms |
| tStA | From user perspective, SLEEPtoACTIVE ping low time on MOSI/RX pin | VBAT > VPOR | 250 |  | 300 | µs |
| Daisy-chain Communication Bus TIMING | Daisy-chain Communication Bus TIMING | Daisy-chain Communication Bus TIMING | Daisy-chain Communication Bus TIMING | Daisy-chain Communication Bus TIMING | Daisy-chain Communication Bus TIMING | Daisy-chain Communication Bus TIMING |
| tPW_DC | COMM data Pulse width of data (half bit time) for communiction |  | 230 | 250 | 270 | ns |
| tCOMTONE | Time between pulses within a comm tone (HFO based). | Transmit. From the beginning of a pulse until the beginning of the next pulse. | 10.67 | 11 | 11.33 | µs |
| tCOMTONE _PLS | Comm tone pulse width(HFO based) | Transmit | 0.97 | 1 | 1.03 | µs |
| tFLTTONE | Time between pulses within a fault tone (LFO based). | Only transmit HB tone, not FAULT tone. From the beginning of a pulse until the beginning of the next pulse. | 10.3 | 11.5 | 12.7 | µs |
| tFLTTONE_ PLS | Fault tone or HB tone pulse width (analog delay based) |  |  | 1 |  | µs |
| nHBDET | HEARTBEAT: Number of pulses to detect as a valid tone (dig counter) | Detect |  | 16 |  | pulses |
| nFTONEDE T | FAULT TONE: Number of pulses to detect as a valid tone (dig counter) | Detect |  | 64 |  | pulses |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_009.png)

## over operating free-air temperature range (unless otherwise noted)

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| tHB_PERIO D | HEARTBEAT: Period between HEARTBEAT Burst (from the beginning of a HEARTBEAT to the beginning of the next HEARTBEAT) |  | 360 | 400 | 440 | ms |
| tHB_TIMEO UT | HEARTBEAT: Timeout to considered as not receving HEARTBEAT |  | 0.9 | 1 | 1.1 | s |
| tHB_FAST | HEARTBEAT: If HEARTBEAT is received within this time, it is considered receving HEARTBEAT too fast |  |  | 200 |  | ms |
| tFTONE_PE RIOD | Defined by BQ7961X, FAULT TONE: Period between FAULT TONE Burst | From the beginning of a FAULT TONE to the beginning of the next FAULT TONE |  | 50 |  | ms |
| tFT_LATEN CY | Fault Tone latency in Base Device | From the time device receives the tone to the time asserts NFAULT |  | 24 |  | µs |
| I/O TIMING (TX, RX, NFAULT) | I/O TIMING (TX, RX, NFAULT) | I/O TIMING (TX, RX, NFAULT) | I/O TIMING (TX, RX, NFAULT) | I/O TIMING (TX, RX, NFAULT) | I/O TIMING (TX, RX, NFAULT) | I/O TIMING (TX, RX, NFAULT) |
| tRISE_TX | Rise Time | CLOAD = 100pF, VIO=3.3V or 5V |  | 15 |  | ns |
| tFALL_TX | Fall Time | CLOAD = 100pF, VIO=3.3V or 5V |  | 15 |  | ns |
| tFALL/ RISE_RX | RX pin rise/fall time |  |  |  | 100 | ns |
| UART TIMING | UART TIMING | UART TIMING | UART TIMING | UART TIMING | UART TIMING | UART TIMING |
| UARTER R_BAUD | UART TX/RX baud rate (either 250K or 1Mbps) error |  | -1.5 |  | 1.5 | % |
| tUART(CLR ) | UART Comm Clear low time |  | 15 |  | 20 | bit period |
| tUART(RX_ HIGH) | UART high time after Comm Clear, before sending Clear or Reset |  | 1 |  |  | bit period |
| SPI TIMING | SPI TIMING | SPI TIMING | SPI TIMING | SPI TIMING | SPI TIMING | SPI TIMING |
| SCLK | SPI clock freq |  | 2 |  | 6 | MHz |
| nSPI(CLR) | SPI Comm Clear low time |  |  | 8 |  | bit |
| tSPI_R | SPI clock rising edge | 25% to 75% |  |  | 10 | ns |
| tSPI_F | SPI clock falling edge | 25% to 75% |  |  | 10 | ns |
| tSPI_CLKH | SPI clock high time SPI clock low time |  | 70 70 |  |  | ns ns |
| tSPI_CLKL t8 | Max SPI_RDY service interval. This time doesn't apply if total response bytes (payload + overhead) is less than 256 | Read SCLK = 6MHz, with 30% SPI BUS idle time |  | 1 |  | ms |
| t9 | bytes From nCS (25%) to SCLK rising (75%) |  | 500 |  |  | ns |
| t10 | From SCLK falling (25%) to nCS (75%) |  | 500 |  |  | ns |
| t11 | From nCS rising(75%) to nCS falling(25%) | Don't drop nCS while SPI_RDY is low | 1 |  |  | µs |
| t12 | From nCS falling (25%) to stable MISO(L:20% H:80%) | Timing is defined at device pins, exclude propergation delay of PCB traces (from device perspective) |  |  | 42 | ns |
| t13 | From SCLK falling (25%) to stable MISO(L:20% H:80%) | Timing is defined at device pins, exclude propergation delay of PCB traces (from device perspective) |  |  | 42 | ns |
| t14 | From nCS rising (75%) to MISO drive to '1' (80%) | Timing is defined at device pins, exclude propergation delay of PCB traces (from device perspective) |  |  | 42 | ns |
| tSU tH | Setup time, refer to 75% of SCLK rising Hold time, refer to 75% of SCLK rising |  | 20 20 |  |  | ns ns |
| SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR | SNIFF DETECTOR |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

over operating free-air temperature range (unless otherwise noted)

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| nVALIDATE | Number of pulses needed (digital counter) to transition to validate mode | Sniffer is enabled, and device is in SHUTDOWN mode |  | 64 |  | pulses |
| tSNIFFIDLE | Timer length. Once timer expired, it resets the 64 counter | Sniffer is enabled, and device is in SHUTDOWN mode | 20 |  | 52 | µs |
| OSCILLATOR | OSCILLATOR | OSCILLATOR | OSCILLATOR | OSCILLATOR | OSCILLATOR | OSCILLATOR |
| fHFO | HFO frequency |  | 31.52 | 32 | 32.48 | MHz |
| tHFOWDG | HFO watchdog time | Reset digital if HFO is stuck or period is > than the watchdog timer |  |  | 35 | µs |
| fLFO | LFO frequency |  | 235.8 | 262 | 288.2 | kHz |
| tLFOWDG | LFO watchdog time | Reset digital if LFO is stuck or period is > than the watchdog timer |  |  | 35 | µs |

## 6.7 Typical Characteristics

Figure 6-1. Typical COMHN and COMHP characteristic

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_011.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_012.png)

## 7 Detailed Description

## 7.1 Overview

The BQ79600-Q1 is a bridge IC designed to interface between microcontroller (MCU) and TI battery monitoring ICs (BQ7961X-Q1 family). It translates between daisy chain interface and SPI/UART interface. It is fully compatible with BQ7961X-Q1 family. When working with BQ7961X-Q1 family, BQ79600-Q1 supports automatic host wakeup through INH pin when unmask fault is detected in high voltage battery pack. Details can be found in Section 7.3.5 and Section 7.3.4. For convenience of traceability, each device is marked by DIE IDs and PARTID which could be found in Section 7.5 Register Summary Table.

## 7.2 Functional Block Diagram

Figure 7-1. Functional Block Diagram

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_013.png)

## 7.3 Feature Description

## 7.3.1 Functional Modes and Power Supply

## 7.3.1.1 Power Mode

The device has four power modes plus an Complete Off state. The functions supported under each power modes are summarized in Table 7-1 and the power state diagram is shown in Figure 7-2.

- COMPLETE OFF: The voltage at the BAT pin is less than VBAT min, and all circuits are powered off.
- SHUTDOWN: The lowest power mode. Without VIO, device can only transition to VALIDATE. (If Sniffer used)
- SLEEP: A low power mode. Transition to ACTIVE is much faster compared to SHUTDOWN.
- ACTIVE: Full power mode. Device can communicate between MCU and daisy chain.
- VALIDATE: This state is to validate if there is real fault tone from stack devices. If fault tone is validated, drive INH pin towards VBAT (INH pin is latched until cleared by user). Device goes back to SHUTDOWN if tVALID\_TIMEOUT or sleep timer expires. (tVALID\_TIMEOUT timer is reset if fault tone is detected, detecting Heartbeat tone doesn't reset timer.) This state is bypassed if Section 7.3.5 is disabled (by default). Once entered this state, a status bit [VALIDATE\_DET] is set in next ACTIVE such that host knows what happened. Without VIO, device can only transition to SHUTDOWN. NFAULT pin is low in this mode.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## Table 7-1. Functions Summary

| FUNCTIONAL BLOCK (1) | SHUTDOWN | VALIDATE (3) | SLEEP | ACTIVE |
| - | - | - | - | - |
| Data Communication RX/TX |  |  |  | If VIO_UV_R = 1 |
| Time out |  | Sleep Timeout | Sleep Timeout | Comm Timeout |
| Tone RX (HB/Fault) |  | √ | Depends on [DIR_SEL] and [TONE_RX_EN] | Depends on [DIR_SEL] and [TONE_RX_EN] |
| Tone TX (WAKE/ SLP2ACT/ SHUTDOWN/ HWRST) (5) |  |  |  | √ |
| Tone TX (HB) |  |  | Depends on [DIR_SEL] and [HB_TX_EN] |  |
| COM embedded fault |  |  |  | [FCOMM_EN] =1 |
| Sniff detector on COM* | If host enables this feature (2) |  |  |  |
| Wake/Shutdown Ping | If VIO_UV_R = 1 | If VIO_UV_R = 1 | If VIO_UV_R = 1 | If VIO_UV_R = 1 |
| SLP2ACT Ping |  |  | √ |  |
| NFAULT Driver |  | √ | √ | √ |
| LFO |  | √ | √ | √ |
| HFO |  |  |  | √ |
| INH Driver | Holds State | √ | INH_DIS[1:0] != 2'b11 | INH_DIS[1:0] != 2'b11 (4) |
| CVDD/DVDD |  | √ | √ | √ |
| Thermal Shutdown |  | √ | √ | √ |

- (1) Once device in SLEEP/ACTIVE, losing VIO doesn't directly cause change of state, it causes loss of data communication to MCU.
- (2) If host writes [SNIFDET\_EN] =1 &amp; [SNIFDET\_DIS] = 0 in ACTIVE mode, even device shuts down, enable signal is still valid. Sniff detector is enabled or disabled by a latch powered by always on power supply.
- (3) This mode is bypassed if sniff detector is not enabled, see register DEV\_CONF1.
- (4) INH can only be triggered by [INH\_SET\_GO] bit in ACTIVE.
- (5) Device does not recognize WAKE/ SLP2ACT/ SHUTDOWN/ HWRST tone sent by stack devices.

Figure 7-2. Power State Diagram

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_014.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_007.png)

## 7.3.1.2 Pings

A "ping" is a specific signal pattern to change power mode of BQ79600-Q1. There are total of 3 different pings:

Figure 7-3. Communication Pings

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_015.png)

- In SPI mode, ping can be sent without SCLK toggling or host can treat sending a ping like sending a series of logic '0' (drive nCS and SCLK properly, refer to SPI physical layer requirement, Section 7.3.2.1.2.2).
- Device does not transmit any tones to stack devices due to the receiving of pings.
- After sending in SHUTDOWN ping, host has to wait tSHTDN before sending another ping.
- If nCS = '1', all of the pings above are ignored by the device.

## Note

If device is shut down through SHUTDOWN ping (COMH RX and COML RX are disabled at next wake up), host needs to send 1 st WAKE ping, wait tSU(WAKE\_SHUT), and then send 2 nd WAKE ping.

Table 7-2. Device Behavior when SLP2ACT Ping is Sent

|  | UART | SPI WITH SCLK TOGGLING | SPI WITHOUT SCLK TOGGLING |
| - | - | - | - |
| ACTIVE | [COMMCLR_DET]=1, [STOP_DET] =1 | [COMCLR_ERR]=1, [COMMCLR_DET]=0 | [FMT_ERR]=1, [COMCLR_ERR]=0, [COMMCLR_DET]=0 |
| SLEEP | [COMMCLR_DET]=1, [STOP_DET] =0, transitions to active mode | [COMCLR_ERR]=0, [COMMCLR_DET]=0, transitions to active mode | [FMT_ERR]=0, [COMCLR_ERR]=0, [COMMCLR_DET]=0, transitions to active mode |

## 7.3.1.3 SPI/UART Selection

The SPI or UART interface is selected through hardware: connect pin nUART/SPI to VIO through resistor for SPI or connect to GND for UART. Device determines UART or SPI mode every time it transitions from SHUTDOWN to ACTIVE mode. Before transitioning to ACTIVE, the mode selected is locked in. VIO has to be above VVIO\_UV\_R. nUART/SPI pin is used as output indication of SPI\_RDY once in ACTIVE mode. See Section 7.3.2.1.2.2.1 for more information.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_016.png)

[www.ti.com](http://www.ti.com/)

## 7.3.1.4 Digital Reset

Digital reset is when digital core of the device in reset mode. It is not a power mode. Once device comes out of digital reset, [DRST] bit is set to '1', registers that are not included in NVM are set to RESET VALUE, registers included in NVM would be NVM program value. There are several conditions in which the device will go through a digital reset:

- A WAKE ping is received.
- The CONTROL1 [SOFT\_RESET] = 1 command is sent in ACTIVE mode.
- Power supply faults. DVDD UV or CVDD UV is detected.
- A HFO or LFO watchdog fault will reset the digital.

## 7.3.1.5 Power Mode in BMS System

It is recommended to follow the power state combinations below to save system level power.

Table 7-3. Power Mode Combination Summary

| STACK MONITORING IC | BQ79600-Q1 | COMMENT |
| - | - | - |
| ACTIVE | ACTIVE | Recommended |
| SLEEP | SLEEP | Recommended |
| SLEEP | SHUTDOWN | Recommended |
| SHUTDOWN | SHUTDOWN | Recommended |
| Other combinations |  | Not recommended |

## 7.3.1.6 Power Supply

This section provides an overview of each supplies for both user cases: without using Reverse Wakeup and with using Reverse Wakeup. See the Section 7.3.6 for diagnostic control and fault detection on the power supplies block.

Table 7-4. Power Supply Summary

| NAME | W/O REVERSE WAKEUP USER CASE | W/ REVERSE WAKEUP USER CASE |
| - | - | - |
| VIO | This supply is powered by regulated 3.3V or 5V from SBC (PMIC), it powers UART/SPI interface pins. | This supply is powered by regulated 3.3V or 5V from SBC (PMIC), it powers UART/SPI interface pins. |
| BAT | This supply is powered by regulated 5V from SBC (PMIC). | This supply is powered by unregulated 12V battery. |
| AVAOREF | This supply is generated from VBAT. It is always on if VBAT exists. It powers REFSYS and Power mode control block. | This supply is generated from VBAT. It is always on if VBAT exists. It powers REFSYS and Power mode control block. |
| AVDDREF | This supply is derived from AVAOREF. AVDDREF and AVAOREF are connected by a switch, the switch is open in SHUTDOWN mode. | This supply is derived from AVAOREF. AVDDREF and AVAOREF are connected by a switch, the switch is open in SHUTDOWN mode. |
| DVDD | This supply is generated by the internal DVDD LDO. It is the supply for the digital circuits. It takes the input voltage from CVDD and generates a nominal 1.8V. It will not be used to power any external circuit. | This supply is generated by the internal DVDD LDO. It is the supply for the digital circuits. It takes the input voltage from CVDD and generates a nominal 1.8V. It will not be used to power any external circuit. |
| CVDD | This supply is powered by regulated 5V from SBC(PMIC). It is the supply for daisy chain interface. | This supply is generated by the internal CVDD LDO. It is the supply for the daisy chain interface (or vertical interface, VIF). It takes the input voltage from VBAT and generates a nominal 5V. It will not be used to power any external circuit. |

## 7.3.1.7 Shutdown

Power Mode Transition Example

迎

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

Figure 7-4. Shutdown -&gt; Active -&gt; Sleep -&gt; Active

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_018.png)

Figure 7-5. Shutdown -&gt; Validate -&gt; Active

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_019.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.3.2 Communication

This device is used as a bridge (base) device in daisy chain configuration, as showed in figure below. It communicates with MCU through UART or SPI and communicates with stack devices through daisy chain (proprietary interface). MCU always initiates communication with a Command frame. In the system, BQ devices would never send data back to MCU before MCU requests. And MCU needs to wait all expected response frames before sending next command frame. Thus, communication scenarios can be put into 2 categories:

- MCU sends Write Command frames to BQ devices. Write Command frames don't incur Response frame.
- MCU sends one Read Command frame to BQ devices and waits till all Response frames are received.

Figure 7-6. System Communication Diagram

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_020.png)

Rest of the section talks about how data and tone are communicated among host, bridge, and stack devices: Section 7.3.2.1 (Section 7.3.2.1.1 and Section 7.3.2.1.2 protocol), Section 7.3.2.2. It also talks about Section 7.3.2.3 and Section 7.3.2.4.

## 7.3.2.1 Data Communication Protocol

## 7.3.2.1.1 Frame Layer

The communication frame is defined in figure below. It is made up of 5 types of information: initialization character (INIT), device address characters, register address character, data character(s) and CRC characters. Each character is transmitted at UART/ SPI/ Daisy Chain physical level, whose format is defined in following Section 7.3.2.1.2 section. There are 3 types of transaction frames: Read Command Frames, Write Command Frames and Response Frames. They follow the structure in the figure below.

| INIT [7:0] | DEV ADR [7:0] REG ADR [15:0] DATA byte(s) CRC [15:0] |
| - | - |

Figure 7-7. Command/Response Frame Structure

| Frames | Frames | INIT | DEV ADR | REG ADR | DATA | CRC |
| - | - | - | - | - | - | - |
| Read Command Frame | Single Device Read | Always 0x80 | Y | Y | # of byte requested (max value 127, meaning 128) | Y |
| Read Command Frame | Stack Read | Always 0xA0 | N | Y | # of byte requested (max value 127, meaning 128) | Y |
| Read Command Frame | Broadcast Read | Always 0xC0 | N | Y | # of byte requested (max value 127, meaning 128) | Y |
| Write Frame | Single Device Write | Y | Y | Y | Actual payload (1-8 bytes) | Y |
| Command | Stack Write | Y | N | Y | Actual payload (1-8 bytes) | Y |
| Command | Broadcast Write | Y | N | Y | Actual payload (1-8 bytes) | Y |
| Command | Broadcast Write Reverse (5) | Y (5) | N | Y (5) | Y (5) | Y |
| Response Frame | Response Frame | Y | Y | Y | Actual payload (1-128 bytes) | Y |

## Notes:

- When BQ79600-Q1 is used as bridge device, to read BQ devices information, host SHALL NOT use Broadcast Read command but only Single Device Read or Stack Read. The reason is BQ79600-Q1 register address does not overlap with stack devices, it would only return 0x00 to Broadcast Read command.
- For Stack Read command, the response is broken into individual response frames from each device addressed. Each device (address N) in the stack waits until the device above it (address N+1) responds before device N sends its own data back.
- After a read command frame is transmitted, the host must wait for all expected responses to return (or timeout: tWAIT\_READ\_MAX ) before initiating a new command frame.
- A response frame is not mandatary. A response frame is only received after a read command frame.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_007.png)

- Broadcast Write Reverse command frame should only be used to config [DIR\_SEL] bit, not for any other purposes. INIT byte is 0xE0, Reg address byte is 0x309 (BQ7961X-Q1), data byte is 0x80.
- Bytes received on COMH/COML are NOT propagated up to the stack; while bytes received on the SPI/UART are propagated to COMH or COML depending on [DIR\_SEL].
- Even if there is a byte error, data is still forwarded from VIF to SPI (buffer)/UART; if there is a byte error, data doesn't forward from SPI/UART to VIF.

|  | Bit | Command Frame - Bit Name | Description | Bit Name | Response Frame - Description |
| - | - | - | - | - | - |
| 7 | FRAME_TYPE | 1 = Command | Frame FRAME_TYPE |  | 0 = Response Frame |
| 6 | REQ_TYPE | 000 = Single Device 001 = Single Device 010 = Stack Read 011 = Stack Write 100 = Broadcast Read 101 = Broadcast Write 110 = Broadcast Write 111 = RSVD (1) | Read Write Reverse This bit is ignored | RESPONSE_BYTE | Number of the data bytes 0x00 = 1 byte 0x01 = 2 bytes : 0x7F = 128 bytes |
| 5 | REQ_TYPE | 000 = Single Device 001 = Single Device 010 = Stack Read 011 = Stack Write 100 = Broadcast Read 101 = Broadcast Write 110 = Broadcast Write 111 = RSVD (1) | Read Write Reverse This bit is ignored | RESPONSE_BYTE | Number of the data bytes 0x00 = 1 byte 0x01 = 2 bytes : 0x7F = 128 bytes |
| 4 | REQ_TYPE | 000 = Single Device 001 = Single Device 010 = Stack Read 011 = Stack Write 100 = Broadcast Read 101 = Broadcast Write 110 = Broadcast Write 111 = RSVD (1) | Read Write Reverse This bit is ignored | RESPONSE_BYTE | Number of the data bytes 0x00 = 1 byte 0x01 = 2 bytes : 0x7F = 128 bytes |
| INIT 3 | RSVD | RSVD. | Read Write Reverse This bit is ignored | RESPONSE_BYTE | Number of the data bytes 0x00 = 1 byte 0x01 = 2 bytes : 0x7F = 128 bytes |
| 2 | DATA_SIZE | Number of data bytes, excluding device address, register address or CRC 000 = 1 byte 001 = 2 bytes : 111 = 8 bytes | Read Write Reverse This bit is ignored | RESPONSE_BYTE | Number of the data bytes 0x00 = 1 byte 0x01 = 2 bytes : 0x7F = 128 bytes |
| 1 | DATA_SIZE | Number of data bytes, excluding device address, register address or CRC 000 = 1 byte 001 = 2 bytes : 111 = 8 bytes | Read Write Reverse This bit is ignored | RESPONSE_BYTE | Number of the data bytes 0x00 = 1 byte 0x01 = 2 bytes : 0x7F = 128 bytes |
| 0 | DATA_SIZE | Number of data bytes, excluding device address, register address or CRC 000 = 1 byte 001 = 2 bytes : 111 = 8 bytes | Read Write Reverse This bit is ignored | RESPONSE_BYTE | Number of the data bytes 0x00 = 1 byte 0x01 = 2 bytes : 0x7F = 128 bytes |

|  | Bit | Bit Name | Command/Response Frame - Description |
| - | - | - | - |
| DEV ADR | 7 | RSVD | 6KRXOG DOZD\V ZULWH ‡�· |
| DEV ADR | 6 | RSVD | 6KRXOG DOZD\V ZULWH ‡�· |
| DEV ADR | 5:0 | Device Address | Set the device address range from 0x00 to 0x3F |

|  | Bit | Bit Name | Command/Response Frame - Description |
| - | - | - | - |
| REG_ ADR | 7:0 | Register Address (MSB) | Target or beginning of the register address |
| REG_ ADR | 7:0 | Register Address (LSB) | Target or beginning of the register address |

|  | Bit | Bit Name | Description |
| - | - | - | - |
|  | 7:0 | Data Byte[0] | Data Byte[0] |
| DATA | « | «« | «« |
|  | 7:0 | Data Byte [n] | Data Byte[n] |

Figure 7-8. Frame Byte Definition

| Bit | Bit Name | Command/Response Frame - Description |
| - | - | - |
| CRC 7:0 7:0 | CRC (MSB) | CRC-16-IBM polynomial (x16 + x15 + x2 + 1 or 11000000000000101) with 0xFFFF initialization |
|  | CRC (LSB) | CRC-16-IBM polynomial (x16 + x15 + x2 + 1 or 11000000000000101) with 0xFFFF initialization |

## Notes:

- INIT character: (1) No function to this selection, but this selection sets the [RC\_IERR] error flag.
- Device Address character: Bit 6 and 7 are reserved; 0x4F to 0xFF is decoded as 0x3F by device.
- Register Address characters: Register addresses are two bytes in length. They indicate the targeted register address on a single byte read/write, or the beginning of the register address on a multi-byte read/write. If an invalid register address is set on a write command, the command will be ignored. If an invalid register address is set on a read command, a 0x00 will be returned as response.
- Data characters can be:
- Single data byte, it represents number of registers requested in Read Command Frame. The BQ79600Q1 supports up to 128 byte reads. The valid data byte for read command frame is 0b0000000 - 0b1111111. The MSB of the data byte is ignored for read command frames. For example, 0b10011001 is read as 0b00011001 and returns data from 26 registers.
- Actual payload in Write Command Frame (max 8 byte) or Response Frame (max 128 byte).
- CRC characters:
- The CRC value is checked as the first step (assume no physical layer error, no [RC\_IERR], no [RC\_SOF], no [RC\_BYTE\_ERR]) after receiving the communication frame. If the CRC is incorrect, the entire frame is discarded and not processed. Any additional frame errors are not checked.
- The frame with CRC error is still transferred up/down the stack. Every device processing this frame will also detect a CRC error. Hence, it is possible to have multiple devices indicating CRC fault on the same communication frame. If a CRC error occurs in the response frame from address N+1, device N does NOT append its own message and an invalid CRC fault is generated. For example, if device 15 finds response frame from device 16 has invalid CRC, device 15 doesn't send its own response frame.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

- The device uses a CRC (cyclic redundancy check) to protect data integrity during transmission. The device uses the CRC-16-IBM polynomial (x 16 + x 15 + x 2 + 1 ) with 0xFFFF initialization.

## 7.3.2.1.1.1 Calculating Frame CRC Value

The CRC calculation by the transmitter is in bit-stream order across the entire transmission frame (except for the CRC). When determining bit-stream order for implementing the CRC algorithm, it is important to note that protocol bytes transmit serially, least-significant bit first. Figure 7-9 illustrates the bit-stream order concept.

Figure 7-9. Bit-Stream Order Explanation

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_021.png)

The CRC (0x0000) is appended to the end of the bit-stream. This bit-stream is then initialized by XOR'ing with 0xFFFF to catch any leading 0 errors. This new bit-stream is then divided by the polynomial (0xC002) until only the 2-byte CRC remains. During this process, the most significant 17 bits of the bit stream are XOR'd with the polynomial. The leading zeroes of the result are removed and that result is XOR'd with the polynomial once again. The process is repeated until only the 2-byte CRC remains. For example:

Example 1: CRC Calculation Using Polynomial Division

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_022.png)

## 7.3.2.1.1.2 Verifying Frame CRC

There are several methods for checking the CRC of a frame. One method is to simply calculate the CRC for the transmitted command except the last two bytes (CRC bytes) using the method described in the previous section, and then compare that result with the transmitted CRC bytes. A more simple option is to run the entire transmission through the CRC algorithm. If the CRC is correct, the result is 0000. In this case, the initial zero padding of the bit-stream with 16 zeroes is not necessary. Using the previous result and running through the algorithm produces the following results:

## Example 1: CRC Verification Using Polynomial Division:

Command Frame = 0x80 00 02 0F 0B (0b1000 0000 0000 0000 0000 0010 0000 1111 0000 1011)

Command Frame w/ CRC in bit stream order = 0x80 00 02 0F 0B C0 29 (0b1000 0000 0000 0000 0000 0010

## [BQ79600-Q1](http://www.ti.com/product/BQ79600-Q1)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_023.png)

```
0000 1111 0000 1011 0000 0011 1001 0100) After Initialization (XOR with 0xFFFF) = 0b0 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 0011 1001 0100 1111 1110 1111 1111 0100 0000 1111 0000 1101 0000 0000 0011 1001 010 #delete leading zeros from previous result 1100 0000 0000 0010 1 #XOR with polynomial 0011 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0011 1001 0100 11 1110 1111 1101 1100 0000 1111 0000 1101 0000 0000 0011 1001 0100 #delete leading zeros from previous result 11 0000 0000 0000 101 #XOR with polynomial 00 1110 1111 1101 0110 0000 1111 0000 1101 0000 0000 0011 1001 0100 …… …… …… 1100 0110 0000 0010 1001 0100 1100 0000 0000 0010 1 #XOR with polynomial 0000 0110 0000 0000 0001 0100 1 1000 0000 0000 0101 00 1 1000 0000 0000 0101 #XOR with polynomial 0 0000 0000 0000 0000 00 0x0000 #verfiy that CRC checks out valid
```

## Note

The result of '0b0000 0000 0000 0000' for the CRC indicates a successful check.

## 7.3.2.1.2 Physical Layer

## 7.3.2.1.2.1 UART

Communication between host and BQ79600-Q1 can be configured to UART mode, refer to Section 7.3.1.3. The UART interface baud rate is default to 1Mbps at power up or digital reset. The UART interface follows the standard serial protocol of 8-N-1 (see Figure 7-10), where it sends information as a START bit, followed by eight data bits, and then one STOP bit. The STOP bit indicates the end of the byte. The protocol also supports two STOP bits. When the device is configured as 2 stop bits ([TWO\_STOP\_EN] = 1, stack devices should also be set as two stop bits), the UART response frame from the device to MCU will always return with 2 stop bits.

The UART sends data on the TX pin and receives data on the RX pin. When idle, the TX and RX are high. TX is always pulled to VIO internally while in ACTIVE or SLEEP mode, whether enabled or disabled.

The UART interface is strictly a half-duplex interface. While transmitting, any attempted communication on RX is ignored. The only exception is Section 7.3.2.1.2.1.2.

Figure 7-10. UART Character Definition

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_024.png)

Note: User can change baud rate using register bit [UART\_VIF\_BAUD] for debug purpose.

## 7.3.2.1.2.1.1 TX HOLD OFF

UART transmitter is configurable to wait a specified number of bit periods after the last bit reception of Single Device read command frame from host before starting transmitting Response Frame using the TX\_HOLD\_OFF register, as showed in Figure 7-11. This provides time for the host to switch the bus direction at the end of its transmission.

## Note

Host does not need to configure register TX\_HOLD\_OFF in BQ79600-Q1 if Stack Read command is used. Host shall not use Broadcast Read Command.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_025.png)

Figure 7-11. TX HOLD OFF Timing Diagram

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_026.png)

## 7.3.2.1.2.1.2 UART COMM CLEAR

## Note

Comm Clear concept only applies to bridge device not stack device.

Comm Clear command is used to clear the receiver and instruct it to look for a new start of frame. (Resync up with host) The next byte following the Comm Clear is considered a "start of frame" byte. The digital receiver continuously monitors the RX line for Comm Clear condition which is RX pin is held low for tUART (CLR) bit periods, showed in Figure 7-12.

When Comm Clear is detected, FAULT\_COMM1 [COMMCLR\_DET] and FAULT\_COMM1 [STOP\_DET] are set. [STOP\_DET] flag is set because the Comm Clear timing violates the typical byte timing and the STOP bit is seen as '0'. The only exception to this is when a COMM CLEAR is sent while BQ79600-Q1 is in sleep. If this is the case, there is no STOP error flag.

Figure 7-12. Comm Clear Timing

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_027.png)

## 7.3.2.1.2.2 SPI

## Note

To facilitate the communication between daisy chain (asynchronous protocol) and SPI (synchronous protocol), BQ79600-Q1 requires the use of Section 7.3.2.1.2.2.1.

Communication between host and BQ79600-Q1 can be configured to SPI mode, refer to Section 7.3.1.3. The host is always a SPI master while BQ79600-Q1 is always a slave. At physical layer, SPI is a five pin interface including 4 common pins (nCS, SCLK, MOSI, MISO) plus SPI\_RDY. At SPI interface, each bit is captured on low to high clock transitions and propagated on high to low clock transition and byte includes 8 bits as shown in Figure 7-13. Please note, MISO is driven high in idle mode. If MCU talks to multiple slaves, please add a tri-state buffer between BQ79600 MISO and MCU.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

Figure 7-13. SPI Timing and Byte Definition

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_028.png)

## Note

Although SPI interface is full duplex at physical layer, at frame layer, it is effectively half duplex because daisy chain only supports half duplex. It means, at the given time, only a command frame OR a response frame is transmitted between MCU and the device.

- When command is being sent from MCU to the device, BQ79600 TX FIFO (2 buffers) should be empty, 0xFF is sent to MCU (except in FIFO diagnostic mode)
- When response is being sent from device to MCU, MCU shall clock in 0xFF
- Host shall provide SPI clock in the range between 2MHz and 6MHz. This range is set by the predefined size of FIFO. Even SPI can run at 6MHz, it does not increase the throughput of total system as daisy chain speed still limit the throughput.
- To avoid collisions on the daisy chain interface, the MCU must wait until all expected response frames are received (or waiting timer expires) before sending another command frame to bq79600. Refer to flow chart in Figure 7-16.
- Master shall always drive MOSI to '1' when not sending command frame into device.
- Host Read mode: from host perspective, read mode is between first byte of a valid read command and last expected number of byte received.
- Device Read mode: start from first byte of a valid read command, device exists read mode when TX FIFO times out and FIFO is empty. Device read mode is subset of host read mode. (concept used for understanding of communication fault registers 0x2301, 0x2302)
- Other than Comm Clear, device rejects any data from MOSI before exiting Device Read mode.
- SPI module rejects any data from daisy chain (stack device) or from itself after TX FIFO timeout List item. until it enters Device Read mode again.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

## [www.ti.com](http://www.ti.com/)

- For command frame, device uses falling edge of nCS as indication of start of frame, and rising edge as end of frame. MCU needs to toggle and keep nCS low for the entire frame (up to 14 characters), toggle nCS back high at the end of this frame. It is legitimate to freeze SCLK while nCS is low. Pulsing nCS in the middle of a command frame is not supported.
- For response frame, nCS is not required to remain low throughout, although it can just like sending command frame. Host can toggle nCS high, stop SPI reading in the middle of the frame (at byte boundary).

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_029.png)

Only Supported in response frame

Figure 7-14. nCS Behavior when Sending Frames

## 7.3.2.1.2.2.1 SPI\_RDY and SPI FIFOs

SPI\_RDY is a output signal indicating to host that data is ready to communicate. SPI FIFOs Figure 7-15 are buffers in the device for temporary storage of incoming/outgoing data. They are required for the following reasons:

- Daisy chain baud rate is approximately 1Mbps by default, once host requests large amount of data, e.g. 400 bytes, device daisy chain receiver would try to send it back to host, but since device does not own the SCLK, it cannot control when the data would be read out. Thus when host is not reading, device need to store the incoming data in the TX FIFO. And even when host is reading, FIFOs are still needed to handle the baud rate difference between SPI and daisy chain.
- SPI\_RDY is required because there is limited depth of TX FIFOs. If host requests more than 256 bytes, and host does not service (read data out) device in time, data overflow would happen. SPI\_RDY indicates to host that certain amount of data is ready to be read or written, e.g. If host request 129 bytes, first time SPI\_RDY flags 128 bytes is ready, second time SPI\_RDY flags 1byte is ready. For details refer to Table 7-5

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_030.png)

Figure 7-15. SPI FIFO Simplified Diagram

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_031.png)

TX FIFO consists of two 128 bytes buffers (working together as Ping-Pong buffer).

1. When Ping buffer is filled up, Pong buffer should be empty, to store incoming data.
2. While Pong buffer is being filled, Ping buffer is being read. Each byte in buffer is reset to 0xFF once being read. Ping buffer shall be empty (read out) before Pong buffer is full.
3. After Pong buffer is filled up, Ping buffer catches up.
4. Device goes through this loop (step 1 to 3) till all response data are received.
5. Host has to read TX FIFO fast enough such that Ping (Pong) buffer is read out and ready to store data from daisy chain before Pong (Ping) buffer is full.

Table 7-5. SPI\_RDY Behavior Summary

|  | CASE # | HI->LOW WHEN - a | LO->HI WHEN - b |
| - | - | - | - |
| Host Writes | 1 | In 2μs when RX FIFO has >= 16 bytes. | After event a1, in 2μs when RX FIFO has < 8 bytes. |
| Host Reads | 2 | In 5μs after device receives 1st byte of read command frame. | In 1us after ping (pong) buffer is full. |
| Host Reads | 3 | TX buffer being read becomes empty (before transmitting out last bit of last byte in the buffer) Note: once going low, SPI_RDY remains low for 2μs no matter what. | TX FIFO time out happened Note: TX FIFO timeout could happen while SPY_RDY is high (while host is reading TX FIFO), in this case, after event a3, SPI_RDY goes how for approximately 2μs, then come back high. |

## Notes:

- SPI\_RDY sets flag only, doesn't gate data flow into or out of device.
- Once devices enters Device Read mode, device rejects any data from host other than COMM CLEAR. a1, b1 doesn't apply anymore.
- TX FIFO Timeout: after SPI module receives one byte of data from either daisy chain or BQ79600-Q1 local, a timer starts; this timer expires if there is no data received for 30μs.

## 7.3.2.1.2.2.2 Flow to Read/Write BQ79600-Q1

User shall follow flow chart Figure 7-16 to do read from device and Figure 7-17 to do write to device activities.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_025.png)

Figure 7-16. Flow Chart to Read from Device

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_032.png)

## Note

MCU shall check SPI\_RDY pin at least every t8 (max service interval). t8 = 1ms at SCLK = 6MHz / 890μs at SCLK = 4MHz /550μs at SCLK = 2MHz assuming host starts to read TX FIFO right after detecting SPI\_RDY = '1 and SPI bus has 30% idle time in the process of reading 128 bytes.

- For response frame, nCS has to be toggled high after reading the last byte of data in the current buffer.
- tWAIT\_READ\_MAX
- stack read/single device read from stack devices, with n stack devices, request m bytes in total (payload + overheads, from all stack devices), wait time: (n-1)*3μs*2 + m*10μs + 100μs.
- single device read from BQ79600-Q1, request m bytes , wait time: 100μs + m*10μs.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_033.png)

## Notes:

- Since write command frame doesn't incur response frames, host shall discard data from MISO pin.
- If host sends partial data, the device would keep waiting the rest of command data till communication time out happens. Refer to Section 7.3.2.4 for details.

## 7.3.2.1.2.2.3 SPI COMM CLEAR

## Note

SPI Comm Clear, applied only to bridge device, is used to clear the FIFOs and reset SPI module.

It stops BQ79600-Q1 sending response; it cannot stop stack devices sending response data back to BQ79600Q1. If host still couldn't communicate to device, host can ultimately use SHUTDOWN ping followed by WAKE ping to reboot device. Device only responses to Comm Clear in ACTIVE. Use the SPI Comm Clear command when:

- SPI\_RDY being low exceeds expected time, either tSPI\_RD\_WAIT\_MAX in READ mode in Figure 7-16 or when 220μs while sending write command frame into device. Don't send Comm Clear before this wait time has elapsed.
- Data read back by host has CRC error.
- Host cannot communicate to the device.

Figure 7-18. SPI Comm Clear

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_034.png)

Figure 7-17. Flow Chart to Send Write Command Frame to Device

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_035.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

SPI Comm Clear is strictly defined as nCS toggling low, 8 bits of '0', nCS toggling high like shown in Figure 7-18. nCS must remain low while sending the Comm Clear. If additional data is detected on MOSI pin before nCS going high, [COMCLR\_ERR] bit is set, device ignores malformed Comm Clear. A correctly formed Comm Clear will only trigger [COMMCLR\_DET]. If Comm Clear is used, it can trigger DEBUG\_SPI\_FRAME [TR\_SOF] (while transmitting local data), [RC\_SOF](receiving partial data) and [TS\_WAIT] (while transmitting daisy chain data).

## 7.3.2.1.2.3 Daisy Chain

Daisy chain is the interface (COMH/COML) communicating to stack devices. It is bi-directional and half duplex, and, therefore, has a transmitter (TX) and receiver (RX) on both COMH and COML interfaces, Figure 7-1. Signal going in and out of daisy chain port is taken care by the device. To use the device, host does not need to know daisy chain physical layer protocol (bit definition, byte definition and byte transferring). Host just needs to control SPI or UART port properly. Still, for user's information, daisy chain physical layer protocol is described below.

Daisy chain bit is transmitted between COM*P and COM*N in fully differential fashion, see Figure 7-19.

Daisy chain byte uses an asynchronous 13-bit byte-transfer protocol. The definition of each bit in the byte is defined in Table 7-6. Byte to byte transmission is captured in Figure 7-20.

Figure 7-19. Daisy Chain Bit Definition

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_036.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_037.png)

Daisy Chain Byte Transfer

Figure 7-20. Daisy Chain Byte/ Byte Transfer Definition

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

## Table 7-6. Daisy Chain Byte Definition

| BIT NAME | DESCRIPTION |
| - | - |
| Preamble (half-bit) | Indicates a start of byte transaction, signaling the receiver to start sampling. This half-bit and the following 2 SYNC bits are used for extra timing information. |
| SYNC[1:0] | Always 0b00. The SYNC bits are used for the digital to assess the timing and noise level on the byte, improving the detection of a '1' and '0' in a noisy environment. |
| Start-Of-Frame (1-bit) | The Start-Of-Frame (SOF) bit defines the byte as the INIT byte (initialization byte) in the frame, refer to Figure 7-8. Stack device needs this information in order to process the communication. |
| Data[7:0] | The actual 8-bit payload. |
| Byte Error BERR (1-bit) | For BQ79600-Q1, BERR is always '0' in command frames sent to stack device. While in received response frames, if it is '1', it indicates last device DEBUG_COM*_PHY[PERR] = 1. |
| Postamble (half-bit) | Indicates the end of byte transaction. |

## 7.3.2.2 Tone Communication Protocol

Other than data, certain information is transmitted using tone: signals to change power state of stack device (SLP2ACT tone, WAKE tone, SHUTDOWN tone, HWRST tone), signals related to faults (FAULT tone and HEARTBEAT tone). The definition of each tone is defined in Figure 7-22 and Figure 7-21.

Device can transmit and receive tones in summary below:

Table 7-7. Available Tones to BQ79600-Q1

| DIRECTION | NAME |
| - | - |
| Receive | FAULT tone and HEARTBEAT tone |
| Transmit | SLP2ACT tone, WAKE tone, SHUTDOWN tone, HWRST tone, HEARTBEAT tone |

## Note:

- Device does not transmit Fault Tone as it uses Section 7.3.3.2.1 to signal fault if enabled.
- SLP2ACT/WAKE/SHUTDOWN/HWRST tone transmitting is on demand when corresponding bit in register CONTROL1 and CONTROL2 is set.
- When bridge device in SHUTDOWN, wakeup bridge device doesn't change power mode of stack devices.
- Receiving threshold value is defined as nHBDET, nFTONEDET in section 6.6.
- Transmitting number is predefined by device in Table 7-8.

Table 7-8. Transmitting Tones Summary Table

|  | SLP2ACT | WAKE | SHUTDOWN | HWRST | HEARTBEAT (SLEEP only) |
| - | - | - | - | - | - |
| N of Couplets Transmitted in Single Burst | 30 | 90 | 270 | 810 | 30 |
| Burst Period | NA | NA | NA | NA | 400ms |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

www.ti.com SHUTDOWN, HEARTBEAT, HWRST Tone WAKE, SLP2ACT Tone

Figure 7-21. FAULT Tone and HEARTBEAT Tone Definition

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_038.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_039.png)

Figure 7-22. SHUTDOWN, HEARTBEAT, HWRST, SLP2ACT Tone Definition

## 7.3.2.3 Device Auto Addressing / Ring Communication

Note

The host starts communication at least 100µs after changing the [DIR\_SEL] setting to ensure the device finishes the COMH/COML reconfiguration.

## 7.3.2.3.1 Auto-Addressing

To properly communicate to every device in daisy chain, host has to assign a unique device address to every device. This process is called Auto-addressing. This step is required every time devices come out of SHUTDOWN or digital reset. Table 7-9 describes a procedure to bring up a system of 1 bridge device and 3 stack devices from SHUTDOWN to a state ready to do read/write communication.

- All device addresses must be sequential

Table 7-9. Auto-Addressing with Figure 7-22(a), assume all devices are in SHUTDOWN

| STEP | WORK WITH BQ7961X-Q1 |
| - | - |
| 1 | send WAKE ping on RX (wakeup BQ79600-Q1) |
| 2 | single device write to BQ79600-Q1 CONTROL1 [SEND_WAKE] = 1 (wake up stack devices) |
| 3 | dummy stack write data 0x00 to register 0x343 to 0x34A (sync up internal DLL). These are 8 separate write commands. |
| 4 | brdcast write 0x01 to address 0x309 (enable auto addressing) |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_007.png)

## Table 7-9. Auto-Addressing with Figure 7-22(a), assume all devices are in SHUTDOWN (continued)

| STEP | WORK WITH BQ7961X-Q1 |
| - | - |
| 5 | brdcast write consecutively to 0x306 = 0,1,2,3 (address 1-3 assigned to BQ7961X-Q1, 0 assigned to BQ79600-Q1) |
| 6 | brdcast write 0x02 to address 0x308 (set BQ7961X-Q1 as stack device ) |
| 7 | single device write to device 3: data 0x03 to address 0x308 (set 3rd BQ7961X-Q1 as top of stack, BQ79600-Q1 is default to base) |
| 8 | dummy stack read registers 0x343 to 0x34A (sync up internal DLL). These are 8 separate read commands. |
| 9 | stack read address 0x306 (read back to verify address are correct for stack devices) |
| 10 | single device read to BQ79600-Q1, verify 0x2001 = 0x14 |
| 11 | finish initialization |

## 7.3.2.3.2 Ring Communication (optional)

A ring communication (optional) allows the system to establish communication from either direction. This allows the system to continue communicating to all stack devices even if one piece of daisy chain cable is broken.

Table 7-10 describes a procedure auto address Figure 7-23(b): to bring up a system of 1 bridge device and 3 stack devices from SHUTDOWN to a state ready to do read/write communication in reverse direction.

To change communication direction from Figure 7-23(a) to Figure 7-23(b), follow the steps 2, 4-14. (Assuming all devices in (a) are already in ACTIVE and auto addressed as described in Table 7-9)

Figure 7-23. Example to Change Communication Direction in Daisy Chain

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_040.png)

Table 7-10. Auto-Addressing Figure 7-22(b), assume all devices are in SHUTDOWN

| STEP | WORK WITH BQ7961X-Q1 |
| - | - |
| 1 | send WAKE ping on RX (wakeup BQ79600-Q1) |
| 2 | single device write to BQ79600-Q1 control 1 [DIR_SEL] = 1 (change BQ79600-Q1 direction) |
| 3 | single device write to BQ79600-Q1 CONTROL1 [SEND_WAKE] = 1 (wake up stack devices) |
| 4 | dummy stack write data 0x00 to registers 0x343 to 0x34A (sync up internal DLL). These are 8 separate write commands. |
| 5 | brdcast write reverse 0x80 to address 0x309 (change stack devices direction DIR_SEL =1) |
| 6 | brdcast Write 0x02 to address 0x308 (1) |
| 7 | brdcast Write 0x81 to address 0x309 (enable BQ7961X-Q1 auto addressing) |
| 8 | brdcast Write consecutively to address 0x307 = 0,1,2,3 (address 1-3 assigned to BQ7961X-Q1, 0 assigned to BQ79600-Q1) |
| 9 | brdcast write 0x02 to address 0x308 (set BQ7961X-Q1 as stack device ) |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

## Table 7-10. Auto-Addressing Figure 7-22(b), assume all devices are in SHUTDOWN (continued)

| STEP | WORK WITH BQ7961X-Q1 |
| - | - |
| 10 | single device write to device 3: data 0x03 to address 0x308 (set 3rd BQ7961X-Q1 as top of stack, BQ79600-Q1 is default to base) |
| 11 | dummy stack read registers 0x343 to 0x34A (sync up internal DLL). These are 8 separate read commands. |
| 12 | stack read address 0x307 (read back to verify address are correct for stack device) |
| 13 | single device read to BQ79600-Q1, verify 0x2001 = 0x14 |
| 14 | finish initialization |

- (1) Clear the previous TOP\_STACK flag after communication direction is changed because top of stack device cannot be reached if one cable is broken

## 7.3.2.4 Communication Timeout

In ACTIVE, there are two programmable communication timeout timers, comm timeout short (once expires, flag fault) and comm timeout long (once expired, transition to SLEEP or SHUTDOWN). They monitor the absence of a valid frame from either UART/SPI or daisy chain communications. A valid frame is defined as any frame (response or command) that does NOT contain any errors that prevent the frame from being processed.

In SHUTDOWN, the timers are disabled and reset. In SLEEP, the last timer values are held frozen. The timer is reset every time a valid response or command frame is received.

How to set the timer, timer expiration action are described in COMM\_TIMEOUT. In order to avoid entering SHUTDOWN mode before a communications timeout fault, ensure the COMM\_TIMEOUT [CTS\_TIME] is shorter than the COMM\_TIMEOUT [CTL\_TIME].

## 7.3.2.5 Communication Debug Mode

The device provides a communication debug mode to ease the initial development phase. Enter/exit debug is controlled by setting of register DEBUG\_CTRL\_UNLOCK. Once device is in debug mode, user is able to control the UART/daisy chain baud rate and on/off of COMH/COML RX/TX. Please refer to register DEBUG\_COMM\_CTRL. User can always read DEBUG\_COMM\_STAT register for comm status disregard the setting/mode of device.

In addition to that, device provides communication low level faults (physical and frame layer)to facilitate debug. Refer to registers from address 0x2301 - 0x2307.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_030.png)

## 7.3.3 Fault Handling

## 7.3.3.1 Fault Status Hierarchy/Reset/Mask

## 7.3.3.1.1 Fault Status Hierarchy

BQ79600-Q1 reports faults in hierarchy, as shown in Figure 7-24:

- Level 1 is FAULT\_SUMMARY register in which each bit represents an OR function of all the bits in its own hierarchy captured in level 2.
- Level 2 bit is the OR function of level 3 bits in its own hierarchy.
- Level 3 contains debug register bits meant to inform host frame and physical layer fault. Level 3 fault is useful in firmware development.
- Any bit triggered in lower level would trigger higher level bit in its hierarchy, e.g. if [TXFIFO\_OV] is set, [SPI\_PHY], [FAULT\_COMM] would also be set.

## Note

Host system can periodically poll the FAULT\_SUMMARY to check the fault status and only read the lower level fault registers if needed.

## 7.3.3.1.2 Fault Reset and Mask

Once fault is detected, the fault status bit is latched until cleared using the reset bit.

When a specific fault reset bit is set, the same color coded bits in level 1 to level 3 are cleared if the fault condition is gone. If the fault condition persists and the reset bit is written, the fault status bit is not reset. For example, if [TXFIFO\_OV], [DVDD\_OV] bits are set, [SPI\_PHY], [FAULT\_COMM] and [FAULT\_PWR] are set, if fault conditions are eliminated and write '1' to [RST\_UART\_SPI] and [RST\_PWR], 5 faults bits would be '0'.

When a specific fault mask bit is set, the same color coded bits would be masked, meaning the fault bits will still be set, but the faults will not be reflected in level 1, FAULT\_SUMMARY register. For example, if [MSK\_UART\_SPI] = 1, any bits being set marked green in level 2 and 3 won't set [FAULT\_COMM] bit.

When fault is masked, it will also prevent the device from asserting the NFAULT pin when the masked faults occur. See Section 7.3.3.2 for details.

MASK/RST

Figure 7-24. Fault Status Hierarchy, Mask and Reset

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_041.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

## 7.3.3.2 Fault Interface

Host can acquire the fault status with the following two methods:

- Host ignores NFAULT pin, constantly polls the FAULT\_SUMMARY register of each device. If FAULT\_SUMMARY is non-zero, read the low level fault status registers to obtain more information.
- Host monitors NFAULT pin status. Enable fault status to pass down the daisy chain to bridge device. Enable bridge device's NFAULT pin to be asserted when the FAULT\_SUMMARY is non-zero. When NFAULT is triggered, host polls fault information to diagnose further.

## 7.3.3.2.1 NFAULT

Device integrates an NMOS open-drain output (NFAULT) to signal the MCU that a fault has occurred in the system (either fault from BQ79600-Q1 or from monitoring IC). The NFAULT driver is enabled when [NFAULT\_EN] = 1. When BQ79600-Q1 detects an unmasked fault, NFAULT asserts low. When NFAULT is disabled, the device will set the corresponding flag in FAULT\_SUMMARY register but will not assert NFAULT.

If the fault information of stack devices are not transmitted to bridge device through Section 7.3.3.2.2, NFAULT output only indicates faults in BQ79600-Q1.

## 7.3.3.2.2 Daisy Chain (COMH and COML)

When using BQ79600-Q1 NFAULT pin to signal the host under a fault detection, the stack devices have to transfer their fault status information to the base device. The information is transmitted through COMH/L interface through the same communication cables:

- In ACTIVE, BQ79600-Q1 detects embedded fault info in response frame from stack device.
- In SLEEP, stack device sends Heartbeat and Fault tone to BQ79600-Q1.
- In SHUTDOWN, use Sniff Detector of BQ79600-Q1 monitors stack device Fault tone.

## 7.3.3.2.2.1 Fault Transmitting when BQ79600-Q1 in ACTIVE

In ACTIVE mode, stack devices can embed their fault status in their response frames (refer to Figure 7-7) that are sent to BQ79600-Q1. The BQ79600-Q1 can detect their embedded fault info and sets [FTONE\_DET] bit once criteria in Figure 7-25 is met. Please refer to BQ7961X-Q1 on how to use embeded fault feature.

To pass on the fault status of the stack devices, the host sends a stack read which will result with response frame pass through every device in the daisy chain, giving each device an opportunity to embed their fault status to response frame.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_042.png)

Figure 7-25. Embed Fault Detection in Response Frame

|  | SOF bit of DEV ADR | SOF bit of REG ADR[15:8] | SOF bit of REG ADR[7:0] | Fault Status |
| - | - | - | - | - |
| [FCOMM_EN] = '1' | 1 | 1 | x | [FCOMM_DET] = '1' |
| [FCOMM_EN] = '1' | 1 | x | 1 | [FCOMM_DET] = '1' |
| [FCOMM_EN] = '1' | x | 1 | 1 | [FCOMM_DET] = '1' |
| [FCOMM_EN] = '1' | 0 | 0 | x | [FCOMM_DET] = '0' |
| [FCOMM_EN] = '1' | 0 | x | 0 | [FCOMM_DET] = '0' |
| [FCOMM_EN] = '1' | x | 0 | 0 | [FCOMM_DET] = '0' |
| [FCOMM_EN] = '0' | x | x | x | [FCOMM_DET] = '0' |

## 7.3.3.2.2.2 Fault Transmitting when BQ79600-Q1 in SLEEP

Because data communication is not available in SLEEP mode, the device provides following options to transmitting fault information:

- Transmit the Heartbeat tone (enabled by [HB\_TX\_EN], used to check integrity of cable between bridge and first stack device). Device does not transmitted fault tone as it has NFAULT.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_043.png)

- Detect Heartbeat and Fault tone, enabled, by [TONE\_RX\_EN].

These tones are transmitted in the same direction as a communication command frame, which is based on the CONTROL1[DIR\_SEL] setting. For the tone signal to return back to BQ79600-Q1 (so NFAULT can be triggered if needed), a Ring architecture must be used to support transmitting fault status in SLEEP mode.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_044.png)

IHN

IHN

Figure 7-26. Heartbeat and Fault Tone Examples

Both the Heartbeat and Fault Tone are a type of tone similar to the communication. One main difference is a communication tone only transmits with a single burst of couplets, while Heartbeat and Fault Tones are sent with a burst of couplets periodically. See Figure 7-21 for details.

7.3.3.2.2.3 Fault Transmitting (Automatic Host Wakeup/Reverse Wakeup) when BQ79600-Q1 in SHUTDOWN

## Note

This feature (Auto Host Wakeup/Reverse Wakeup) is only available if Section 7.3.5 is enabled.

The purpose of this user case is to keep BQ79600-Q1 in lowest power mode while still being able to detect fault information from stack devices. In this case, fault information transmittion is similar to that of SLEEP: top of stack device sends HB or Fault tone to BQ79600-Q1. The difference lies in the detection of those tones in BQ79600Q1. In SHUTDOWN, TONE RX is off, only low power Section 7.3.5 is available. Once sniffer detects FAULT tone, it puts device into VALIDATE mode in which full power TONE RX is available, device would validate if true Fault tone exists or not. If yes, it triggers INH. See Figure 7-27 for different case.

Figure 7-27. Reverse Wakeup User Case

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_045.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_046.png)

## 7.3.4 INH/ Reverse Wakeup

## Note

INH pin is used if Reverse Wakeup feature is used. If this feature is not used, connect this pin to BAT pin, refer to schematic in Figure 8-1.

Reverse wakeup feature is a mechanism where BQ79600-Q1 can wakeup the host, through INH pin, on faulty status from either BQ79600-Q1 or stack devices like BQ7961X-Q1. MCU and its supply (PMIC/SBC) are in SHUTDOWN for power saving on low voltage battery side.

The INH pin is a high voltage output pin that provides voltage from the BAT minus VDROP\_INH to enable an external high voltage regulators (SBC, PMIC). These regulators are usually used to support the microprocessor and VIO pin. When INH PMOS pullup is not activated, INH pin goes to a high Z state, it relies on external circuit to define the pin voltage (in application circuit, 100kohm resistor to GND is used.)

INH PMOS pullup can be triggered:

- In SLEEP mode or VALIDATE mode if following faults are detected regardless of setting of register FAULT\_MSK: [FTONE\_DET], [HB\_FAIL], [HB\_FAST], [AVAO\_SW\_FAIL], [FACT\_CRC], [CONF\_MON\_ERR].
- In ACTIVE, INH can only be triggered by setting [INH\_SET\_GO] =1.

Once INH triggered, it remains latched in all modes as long as VBAT is not removed.

INH function described above can be disabled by configuring INH\_DIS[1:0] = 2'b11.

Every time INH PMOS is activated, fault bit [INH] is set. To clear the fault, set INH\_DIS[1:0] = 2'b11 (disarm INH driver), then write [RST\_SYS] = 1. After this, to use INH feature, set INH\_DIS[1:0] = 2'b00.

As part of safety diagnostic (SM202 in Safety Manual), host can trigger INH in ACTIVE and check if pin voltage is set properly: If INH pin voltage is higher than VINH\_DET, [INH\_STAT] = 1.

## Note

INH pin should be considered a "high voltage logic" terminal, thus should be used to drive the EN terminal of the system's power management device. It should be not used as a switch for power management supply itself. This terminal is not reverse battery protected and thus should not be connected outside of the system module.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

## 7.3.5 Sniff Detector

## Note

Sniff detector is only used if reverse wakeup feature is used.

Sniff detector, powered by AVAOREF, is used to detect fault tone from stack device on COMH* or COML*. This detector would trigger if it detects/counts no less than nVALIDATE of continuous couplets (either "-" or "+") with amplitude larger than VVAL\_THR. If any couplet timing interval is larger than tSNIFFIDLE, detector/counter is reset.

This sniff detector rejects HB tone since nVALIDATE is more than 30, both HB/Fault tone are "-" tone; detector doesn't expect "+" tone.

## Note

The usage assumption of this detector is when system is in idle mode, BQ79600-Q1 in SHUTDOWN.

Sniff detector is only effective in SHUTDOWN. Once detector is triggered, device transitions from SHUTDOWN to VALIDATE. The sniff detector is by default disabled when first transition from COMPLETE OFF to SHUTDOWN. To enable the feature, host has to keep [SNIFDET\_EN] = '1' &amp; [SNIFDET\_DIS] = '0' before transitioning to SHUTDOWN. After enabling the detector, if device doesn't transition to COMPLETE OFF, the only way to disable the detector is to keep [SNIFDET\_DIS] = '1'. (Disable bit has higher priority so don't care about the setting of [SNIFDET\_EN]) before transitioning to SHUTDOWN.)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_046.png)

## 7.3.6 Device Diagnostic

The product is developed as a safety element out of context (SEooC), with a target safety goal of ASIL-D for communication. The following sub-sections describe the diagnostic control and fault status that can be used as part of the safety mechanisms.

The Safety Manual and FMEDA for BQ79600-Q1 are available separately from Texas Instruments. Contact TI Sales Associate or Applications Engineer for further information.

## 7.3.6.1 Power Supplies Check

## 7.3.6.1.1 Power Supply Diagnostic Check

The internal power supply circuits have overvoltage, undervoltage, and/or current limit checks. The table below summarizes the diagnostics that apply for each power supply and the corresponding action when failure is detected.

Table 7-11. Power Supply Diagnostic Summary

| SUPPLY | OV CHECK | UV CHECK | CURRENT LIMIT |
| - | - | - | - |
| DVDD | If fails, set [DVDD_OV] | If fails, digital reset | Limit current to EC table current limit specification |
| CVDD | If fails, set [CVDD_OV] | If fails, digital reset, set [CVDD_UV_DRST] | Limit current to EC table current limit specification |
| AVAOREF | If fails, set [AVDDREF_OV] (AVAOREF supplies AVDDREF) | If fails, device shuts down |  |
| AVDDREF | If fails, set [AVDDREF_OV] | If fails, set [AVAO_SW_FAIL] or digital reset |  |
| VIO |  | If fails, device losses data communication and Ping function |  |

## 7.3.6.1.2 Power Supply BIST

The device implemented a power supply BIST (Built-In Self-Test) function to test CVDD, DVDD, AVDDREF OV detection comparator integrity. It is a command base function initiated by host. Steps below explains how it works, and further details can be found in Safety Manual (SM017).

1. Host shall read the register FAULT\_PWR to verify [CVDD\_OV], [DVDD\_OV], [AVDDREF\_OV] are low.
2. Host shall write [PWR\_DIAG\_GO] = 1.
3. After 1.7ms, host shall read if [PWR\_DIAG\_RDY] = 1, else shall, keep waiting, reread.
4. If yes, host shall read FAULT\_PWR register, [CVDD\_OV], [DVDD\_OV], [AVDDREF\_OV] to verify the bits are asserted.
5. Host shall reset faults above.

## 7.3.6.2 Thermal Shutdown

Thermal shutdown (TSHUT) event occurs when the Thermal Shutdown sensor value exceeds the thermal shutdown temperature threshold. The sensor operates without interaction and is separated from the ADC measured die sensor. The thermal shutdown function has a register-status indicator flag (FAULT\_SYS[TSHUT]) that is saved during the shutdown event and can be read after the device is waken back up. When a TSHUT fault occurs, the device immediately enters the SHUTDOWN mode. Any pending transactions on UART or daisy chain are discarded. There is no fault signaling when a thermal shutdown event occurs, as the device immediately shuts down.

To awaken the device, host shall ensure the ambient temperature is below TSD\_FALL and sends a WAKE ping to the base device. Host shall not attempt to wake the device if the ambient temperature is still above TSD\_FALL.

Upon waking up, the FAULT\_SYS[TSHUT] bit is set. The FAULT\_SYS[SHUTDOWN\_REC] = 1 indicating the prior shutdown was caused by abnormal event. See Section 7.5.17 for more details. If the system faults are unmasked, FAULT\_MSK1[MSK\_SYS] = 0, the thermal shutdown will be reflected as FAULT and will be indicated in the FAULT\_SUMMARY register and the assertion of the NFAULT pin.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

## 7.3.6.3 Oscillators Watchdog

The oscillators are monitored by watchdog circuits. There are two oscillators in the device, the HFO and the LFO. If these oscillators are not functioning, the device does not operate. If the HFO or LFO does not transition within the expected time, the watchdog circuits trigger Digital Reset.

When such unexpected reset occurs, it is recommended for the host to send a SHUTDOWN ping/tone to the problem device and follow up a WAKE ping to reset the daisy chain. If the oscillators are truly damaged, the device will not restart and must be replaced.

In addition to the watchdog, the LFO frequency is monitored to ensure it stays within acceptable limits. If the LFO frequency falls outside of the expected range, the FAULT\_SYS\_FAULT[LFO] bit is set.

## 7.3.6.4 Register Bit Flip Monitor

This bit flip checker monitors 2 configuration registers: DEV\_CONF1, FAULT\_MSK. It is always running when device is out of SHUTDOWN. Whenever user changes those 2 register settings or any of the register bit flips, fault bit [CONF\_MON\_ERR] is set.

Once user changes the setting, user shall write [CONF\_MON\_GO]=1 (resample 2 register values), write [RST\_REG] =1 to clear the [CONF\_MON\_ERR] fault, after this point, if any bit flips among those 2 registers, [CONF\_MON\_ERR] is set. After device resets (receive WAKE ping or [SOFT\_RESET] = 1), [CONF\_MON\_ERR] = 0.

This device does not have customer register CRC check and the register bit flip monitor provides the protection for the above mentioned customer registers.

## 7.3.6.5 SPI FIFO Diagnostic

The FIFO diagnostic mode provides a method for host to exercise the RX/TX FIFOs. Please refer to safety manual for detailed FIFO diagnostic safety mechanism implementation (SM132).

## 7.4 Device Functional Modes

See Section 7.3.1

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_046.png)

## 7.5 Register Maps

Figure 7-28. Register Summary

|  | Addr R/W Type Reset Value Data - Hex | Addr R/W Type Reset Value Data | Addr R/W Type Reset Value Data - Bit7 | Addr R/W Type Reset Value Data - Bit6 | Addr R/W Type Reset Value Data - Bit5 | Addr R/W Type Reset Value Data - Bit4 | Addr R/W Type Reset Value Data - Bit3 Bit2 | Addr R/W Type Reset Value Data - Bit1 | Addr R/W Type Reset Value Data - Bit0 |
| - | - | - | - | - | - | - | - | - | - |
| DIR0_ADDR | 306 R/W | "0000 0000" | RSVD | RSVD | ADDRESS[5] | ADDRESS[4] | ADDRESS[3] ADDRESS[2] | ADDRESS[1] | ADDRESS[0] |
| DIR1_ADDR | 307 R/W | "0000 0000" | RSVD | RSVD | ADDRESS[5] | ADDRESS[4] | ADDRESS[3] ADDRESS[2] | ADDRESS[1] | ADDRESS[0] |
| CONTROL1 | 309 R/W-AC | "0000 0000" | DIR_SEL | SEND_SHUTDOWN | SEND_WAKE | SEND_SLPTOACT | GOTO_SHUTDOWN GOTO_SLEEP | SOFT_RESET | ADDR_WR |
| CONTROL2 | 30A R/W-AC | "0000 0000" | RSVD | RSVD | RSVD | RSVD | RSVD RSVD | SEND_HW_RESET | RSVD |
| DIAG_CTRL | 2000 R/W-AC | "0000 0000" | RSVD | RSVD | CONF_MON_GO | PWR_DIAG_GO | SPI_FIFO_DIAG_GO FLIP_FACT_CRC | FLIP_TR_CRC | INH_SET_GO |
| DEV_CONF1 | 2001 R/W | "0001 0100" | SNIFDET_EN | SNIFDET_DIS | TONE_RX_EN | FCOMM_EN | TWO_STOP_EN NFAULT_EN | RESERVED | HB_TX_EN |
| DEV_CONF2 | 2002 R/W | "0000 0000" | RSVD | RSVD | RSVD | RSVD | RSVD RSVD | INH_DIS[1] | INH_DIS[0] |
| TX_HOLD_OFF | 2003 R/W | "0000 0000" | DLY[7] | DLY[6] | DLY[5] | DLY[4] DLY[3] | DLY[2] | DLY[1] | DLY[0] |
| SLP_TIMEOUT | 2004 R/W | "0000 0011" | RSVD | RSVD | RSVD | RSVD | RSVD SLP_TIME[2] | SLP_TIME[1] | SLP_TIME[0] |
| COMM_TIMEOUT | 2005 R/W | "0011 0100" | RSVD | CTS_TIME[2] | CTS_TIME[1] | CTS_TIME[0] | CTL_ACT CTL_TIME[2] | CTL_TIME[1] | CTL_TIME[0] |
| SPI_FIFO_UNLOCK | 2010 R/W | "0000 0000" | RSVD | RSVD | RSVD | RSVD | CODE[3] CODE[2] | CODE[1] | CODE[0] |
| FAULT_MSK | 2020 R/W | "0000 0000" | MSK_COML_H | MSK_UART_SPI | MSK_FCOMM_DET | MSK_FTONE_DET | MSK_HB MSK_REG | MSK_SYS | MSK_PWR |
| FAULT_RST | 2030 R/W-AC | "0000 0000" | RST_COML_H | RST_UART_SPI | RST_FCOMM_DET | RST_FTONE_DET | RST_HB RST_REG | RST_SYS | RST_PWR |
| FAULT_SUMMARY | 2100 R | "0000 0000" | RSVD | RSVD | RSVD | RSVD | FAULT_COMM FAULT_REG | FAULT_SYS | FAULT_PWR |
| FAULT_REG | 2101 R | "0000 0000" | RSVD | RSVD | RSVD | RSVD | RSVD CONF_MON_ERR | FACTLDERR | FACT_CRC |
| FAULT_SYS | 2102 R | "0000 0000" | VALIDATE_DET | LFO | SHUTDOWN_REC | DRST | CTL CTS | TSHUT | INH |
| FAULT_PWR | 2103 R | "0000 0000" | RSVD | RSVD | RSVD | CVDD_UV_DRST | CVDD_OV DVDD_OV | AVDDREF_OV | AVAO_SW_FAIL |
| FAULT_COMM1 | 2104 R | "0000 0000" | RSVD | FCOMM_DET | FTONE_DET | HB_FAIL | HB_FAST UART_FRAME | COMMCLR_DET | STOP_DET |
| FAULT_COMM2 | 2105 R | "0000 0000" | RSVD | RSVD | SPI_FRAME | SPI_PHY | COML_FRAME COML_PHY | COMH_FRAME | COMH_PHY |
| DEV_DIAG_STAT | 2110 R | "0000 0000" | RSVD | RSVD | RSVD | RSVD | RSVD RSVD | PWR_DIAG_RDY | INH_STAT |
| PARTID | 2120 R | "0000 0000" | REV[7] | REV[6] | REV[5] | REV[4] | REV[3] REV[2] | REV[1] | REV[0] |
| DIE_ID1 | 2121 R | "0000 0000" | ID[7] | ID[6] | ID[5] | ID[4] | ID[3] ID[2] | ID[1] | ID[0] |
| DIE_ID2 |  | "0000 0000" |  |  | ID[5] | ID[4] | ID[2] | ID[1] | ID[0] |
| DIE_ID3 | 2122 R 2123 R | "0000 0000" | ID[7] ID[7] | ID[6] ID[6] | ID[5] | ID[4] ID[3] | ID[3] ID[2] | ID[1] | ID[0] |
| DIE_ID4 | 2124 R | "0000 0000" | ID[7] | ID[6] | ID[5] | ID[4] | ID[3] ID[2] | ID[1] | ID[0] |
| DIE_ID5 | 2125 R | "0000 0000" ID[7] |  | ID[6] | ID[5] | ID[4] | ID[3] ID[2] | ID[1] | ID[0] |
| DIE_ID6 | 2126 R | "0000 0000" ID[7] |  | ID[6] | ID[5] | ID[4] ID[3] | ID[2] | ID[1] | ID[0] |
| DIE_ID7 | 2127 R | "0000 0000" ID[7] |  | ID[6] | ID[5] | ID[4] | ID[3] ID[2] | ID[1] | ID[0] |
| DIE_ID8 | 2128 R | "0000 0000" ID[7] |  | ID[6] | ID[5] | ID[4] ID[3] | ID[2] | ID[1] | ID[0] |
| DIE_ID9 | 2129 R | "0000 0000" ID[7] |  | ID[6] | ID[5] | ID[4] ID[3] | ID[2] | ID[1] | ID[0] |
| DEBUG_CTRL_UNLOCK2200 | R/W | "0000 0000" | CODE[7] | CODE[6] | CODE[5] | CODE[4] | CODE[3] CODE[2] | CODE[1] | CODE[0] |
| DEBUG_COMM_CTRL | 2201 R/W | "0111 1000" | RSVD | COML_TX_EN | COML_RX_EN | COMH_TX_EN | COMH_RX_EN UART_VIF_BAUD | USER_UART_EN | USER_DAISY_EN |
| DEBUG_COMM_STAT | 2300 R | "0001 0011" | RSVD | RSVD | RSVD | HW_DAISY_DRV | COML_TX_ON COML_RX_ON | COMH_TX_ON | COMH_RX_ON |
| DEBUG_SPI_PHY | 2301 R | "0000 0000" | RSVD | FMT_ERR | COMCLR_ERR | TXDATA_UNEXP | RXDATA_UNEXP TXFIFO_OF | TXFIFO_UF | RXFIFO_OF |
| DEBUG_SPI_FRAME | 2302 R | "0000 0000" | RSVD | RSVD | TR_SOF | TR_WAIT TR_WAIT | RC_IERR RC_SOF | RC_BYTE_ERR | RC_CRC |
| DEBUG_UART_FRAME | 2303 R | "0000 0000" | RSVD | RSVD | TR_SOF |  | RC_IERR RC_SOF | RC_BYTE_ERR | RC_CRC |
| DEBUG_COMH_PHY | 2304 R | "0000 0000" | RSVD |  |  | RR_IERR | RR_SOF | SYNC1 |  |
|  |  |  |  | RSVD | RSVD | PERR | BERR_TAG SYNC2 |  | BIT |
| DEBUG_COMH_FRAME | 2305 R | "0000 0000" | RSVD | RSVD | RSVD |  | RR_BYTE_ERR | RR_UNEXP | RR_CRC |
| DEBUG_COML_PHY DEBUG_COML_FRAME | 2306 R 2307 R | "0000 0000" "0000 0000" | RSVD RSVD | RSVD RSVD | RSVD RSVD | PERR RR_IERR | BERR_TAG SYNC2 RR_SOF RR_BYTE_ERR | SYNC1 RR_UNEXP | BIT RR_CRC |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_007.png)

## 7.5.1 Register Summary Table

| ADDRESS | REGISTER | DESCRIPTION | R/W MODE | RESET VALUE | NVM VALUES | INCLUDED IN NVM? |
| - | - | - | - | - | - | - |
| 0x306 | DIR0_ADDR | Device Address North Direction | R/W | 0x00 | n/a | no |
| 0x307 | DIR1_ADDR | Device Address South Direction | R/W | 0x00 | n/a | no |
| 0x309 | CONTROL1 | Control1 | R/W | 0x00 | n/a | no |
| 0x30A | CONTROL2 | Control2 | R/W | 0x00 | n/a | no |
| 0x2000 | DIAG_CTRL | Diagnostic Control | R/W | 0x00 | n/a | no |
| 0x2001 | DEV_CONF1 | Device Configure1 | R/W | 0x14 | n/a | no |
| 0x2002 | DEV_CONF2 | Device Configure2 | R/W | 0x00 | n/a | no |
| 0x2003 | TX_HOLD_OFF | Transmitter Hold off Control | R/W | 0x00 | n/a | no |
| 0x2004 | SLP_TIMEOUT | Sleep Timer | R/W | 0x03 | n/a | no |
| 0x2005 | COMM_TIMEOUT | Communication Timeout Control | R/W | 0x34 | n/a | no |
| 0x2010 | SPI_FIFO_UNLOCK | FIFO Diagnostic Unlock | R/W | 0x00 | n/a | no |
| 0x2020 | FAULT_MSK | Fault Mask | R/W | 0x00 | n/a | no |
| 0x2030 | FAULT_RST | Fault Reset | R/W | 0x00 | n/a | no |
| 0x2100 | FAULT_SUMMARY | Fault Summary | R | 0x00 | n/a | no |
| 0x2101 | FAULT_REG | Register Fault | R | 0x00 | n/a | no |
| 0x2102 | FAULT_SYS | System Fault | R | 0x00 | n/a | no |
| 0x2103 | FAULT_PWR | Power Fault | R | 0x00 | n/a | no |
| 0x2104 | FAULT_COMM1 | Communication Fault1 | R | 0x00 | n/a | no |
| 0x2105 | FAULT_COMM2 | Communication Fault2 | R | 0x00 | n/a | no |
| 0x2110 | DEV_DIAG_STAT | Diagnostic Status | R | 0x00 | n/a | no |
| 0x2120 | PARTID | Part ID | R | 0x00 | various | yes |
| 0x2121 | DIE_ID1 | Die ID1 | R | 0x00 | various | yes |
| 0x2122 | DIE_ID2 | Die ID2 | R | 0x00 | various | yes |
| 0x2123 | DIE_ID3 | Die ID3 | R | 0x00 | various | yes |
| 0x2124 | DIE_ID4 | Die ID4 | R | 0x00 | various | yes |
| 0x2125 | DIE_ID5 | Die ID5 | R | 0x00 | various | yes |
| 0x2126 | DIE_ID6 | Die ID6 | R | 0x00 | various | yes |
| 0x2127 | DIE_ID7 | Die ID7 | R | 0x00 | various | yes |
| 0x2128 | DIE_ID8 | Die ID8 | R | 0x00 | various | yes |
| 0x2129 | DIE_ID9 | Die ID9 | R | 0x00 | various | yes |
| 0x2200 | DEBUG_CTRL_UNLOCK | Debug Control Unlock | R/W | 0x00 | n/a | no |
| 0x2201 | DEBUG_COMM_CTRL | Debug Communication Control | R/W | 0x78 | n/a | no |
| 0x2300 | DEBUG_COMM_STAT | Debug Communication Status | R | 0x13 | n/a | no |
| 0x2301 | DEBUG_SPI_PHY | SPI Physical Layer Error | R | 0x00 | n/a | no |
| 0x2302 | DEBUG_SPI_FRAME | SPI Frame Layer Error | R | 0x00 | n/a | no |
| 0x2303 | DEBUG_UART_FRAME | UART Frame Layer Error | R | 0x00 | n/a | no |
| 0x2304 | DEBUG_COMH_PHY | COMH Physical Layer Error | R | 0x00 | n/a | no |
| 0x2305 | DEBUG_COMH_FRAME | COMH Frame Layer Error | R | 0x00 | n/a | no |
| 0x2306 | DEBUG_COML_PHY | COML Physical Layer Error | R | 0x00 | n/a | no |
| 0x2307 | DEBUG_COML_FRAME | COML Frame Layer Error | R | 0x00 | n/a | no |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.5.2 Register: DIR0\_ADDR

| Address: 0x306 - B7 - RSVD | Address: 0x306 - B6 - RSVD | Address: 0x306 - B5 - ADDRESS[5:0] | Address: 0x306 - B4 - ADDRESS[5:0] | Address: 0x306 - B3 - ADDRESS[5:0] | Address: 0x306 - B2 - ADDRESS[5:0] | Address: 0x306 - B1 - ADDRESS[5:0] | Address: 0x306 - B0 - ADDRESS[5:0] |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |

ADDRESS [5:0] Follow steps in section "Device Addressing" to config this register. Always shows the current Device Address used by the device when [DIR\_SEL] = 0.

Default to 0x00 when digital core out of digital reset. MCU can re-address the device by writing a different device address to this register, and the device will take on the new address immediately.

## 7.5.3 Register: DIR1\_ADDR

| Address: 0x307 - B7 - RSVD | Address: 0x307 - B6 - RSVD | Address: 0x307 - B5 - ADDRESS[5:0] | Address: 0x307 - B4 - ADDRESS[5:0] | Address: 0x307 - B3 - ADDRESS[5:0] | Address: 0x307 - B2 - ADDRESS[5:0] | Address: 0x307 - B1 - ADDRESS[5:0] | Address: 0x307 - B0 - ADDRESS[5:0] |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |

ADDRESS [5:0] Follow steps in section "Device Addressing" to config this register. Always shows the current Device Address used by the device when [DIR\_SEL] = 1.

Default to 0x00 when digital core out of digital reset. MCU can re-address the device by writing a different device address to this register, and the device will take on the new address immediately.

## 7.5.4 Register: CONTROL1

| Address: 0x0309 - B7 | Address: 0x0309 - B6 | Address: 0x0309 - B5 | Address: 0x0309 - B4 | Address: 0x0309 - B3 | Address: 0x0309 - B2 | Address: 0x0309 - B1 | Address: 0x0309 - B0 |
| - | - | - | - | - | - | - | - |
| DIR_SEL | SEND_SHUTDO WN | SEND_WAKE | SEND_SLPTOAC T | GOTO_SHUTDO WN | GOTO_SLEEP | SOFT_RESET | ADDR_WR |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |

DIR\_SEL

Select daisy chain comm direction. Not self-clear bit.

SEND\_SHUTDO

WN

0: In a device, command frame travels from MCU to COMH

1: In a device, command frame travels from MCU to COML

Sends SHUTDOWN tone to next device up the stack. The device receiving this bit is unaffected. Self-clear bit.

0: Ready

- 1: Send SHUTDWON tone up the stack

SEND\_WAKE Send WAKE tone up the stack. Self-clear bit.

0: Ready

- 1: Send WAKE tone up the stack, then reset its own

Send SLEEPtoWAKE tone up the stack. Self-clear bit.

0: Ready

- 1: Send SLEEPtoWAKE tone up the stack

Transition device to SHUTDOWN mode. Self-clear bit.

0: Ready

SEND\_SLPTOAC

T

GOTO\_SHUTDO

WN

- 1: Enter SHUTDOWN mode

GOTO\_SLEEP Transition device to SLEEP mode. Self-clear bit.

0: Ready

- 1: Enter SLEEP mode

SOFT\_RESET Reset the digital to OTP default. Self-clear bit.

0: Ready

- 1: Reset device

ADDR\_WR

Enable device to start auto-addressing. See auto-addressing chapter for detail. Self cleared.

- 0: Not performing auto-address. Device forwards communication transaction as normal
- 1: Device is being auto-addressed; the 1st communication transaction it received will not be forwarded.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_009.png)

## 7.5.5 Register: CONTROL2

| Address: 0x30A - B7 | Address: 0x30A - B6 | Address: 0x30A - B5 | Address: 0x30A - B4 | Address: 0x30A - B3 | Address: 0x30A - B2 | Address: 0x30A - B1 | Address: 0x30A - B0 |
| - | - | - | - | - | - | - | - |
|  | RSVD | RSVD | RSVD | RSVD | RSVD | SEND_HW_RESE T | SPARE |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| SEND_HW_RESE T | Send HW_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW_RESET tone to next stack device up | Send HW_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW_RESET tone to next stack device up | Send HW_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW_RESET tone to next stack device up | Send HW_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW_RESET tone to next stack device up | Send HW_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW_RESET tone to next stack device up | Send HW_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW_RESET tone to next stack device up | Send HW_RESET tone up the stack. Self-clear bit. 0: Ready 1: Send HW_RESET tone to next stack device up |

## 7.5.6 Register: DIAG\_CTRL

| Address: 0x2000 - B7 | Address: 0x2000 - B6 | Address: 0x2000 - B5 | Address: 0x2000 - B4 | Address: 0x2000 - B3 | Address: 0x2000 - B2 | Address: 0x2000 - B1 | Address: 0x2000 - B0 |
| - | - | - | - | - | - | - | - |
| RSVD | RSVD | CONF_MON_GO | PWR_DIAG_GO | SPI_FIFO_DIAG_ GO | FLIP_FACT_CRC | FLIP_TR_CRC | INH_SET_GO |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| CONF_MON_GO | Resample the 2 registers (DEV_CONF1, FAULT_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting | Resample the 2 registers (DEV_CONF1, FAULT_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting | Resample the 2 registers (DEV_CONF1, FAULT_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting | Resample the 2 registers (DEV_CONF1, FAULT_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting | Resample the 2 registers (DEV_CONF1, FAULT_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting | Resample the 2 registers (DEV_CONF1, FAULT_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting | Resample the 2 registers (DEV_CONF1, FAULT_MSK) setting that bit flip monitor checks against. self-clear bit. For usage, refer to paragraph: Register Bit Flip Monitor 0: No action 1: Resample 2 registers setting |
| PWR_DIAG_GO | Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic | Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic | Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic | Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic | Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic | Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic | Indicates a power supply BIST diagnostic is initiated, self-clear bit. 0: No action 1: Initiate power BIST diagnostic |
| SPI_FIFO_DIAG_ GO | Write the unlock code 0x0A to SPI_FIFO_UNLOCK and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. 0: No action | Write the unlock code 0x0A to SPI_FIFO_UNLOCK and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. 0: No action | Write the unlock code 0x0A to SPI_FIFO_UNLOCK and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. 0: No action | Write the unlock code 0x0A to SPI_FIFO_UNLOCK and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. 0: No action | Write the unlock code 0x0A to SPI_FIFO_UNLOCK and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. 0: No action | Write the unlock code 0x0A to SPI_FIFO_UNLOCK and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. 0: No action | Write the unlock code 0x0A to SPI_FIFO_UNLOCK and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. This bit is self-cleared. 0: No action |
| FLIP_FACT_CRC | Initiate SPI An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. 0: No action 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT_REG[FACT_CRC] | diagnostic | Initiate SPI An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. 0: No action 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT_REG[FACT_CRC] | Initiate SPI An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. 0: No action 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT_REG[FACT_CRC] | Initiate SPI An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. 0: No action 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT_REG[FACT_CRC] | Initiate SPI An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. 0: No action 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT_REG[FACT_CRC] | Initiate SPI An enable bit to flip the factory CRC expected value. This is for factory CRC diagnostic. 0: No action 1: flip the CRC expected value. This will cause a factory CRC fault, FAULT_REG[FACT_CRC] |
| FLIP_TR_CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC | Sends a purposely incorrect communication (during transmitting response) CRC by inverting all of the calculated CRC bits 0: Send CRC as calculated 1: Send inverted CRC |
| INH_SET_GO | This bits intentionally activates INH PMOS pull up, sets [INH] and [INH_STAT] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up | This bits intentionally activates INH PMOS pull up, sets [INH] and [INH_STAT] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up | This bits intentionally activates INH PMOS pull up, sets [INH] and [INH_STAT] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up | This bits intentionally activates INH PMOS pull up, sets [INH] and [INH_STAT] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up | This bits intentionally activates INH PMOS pull up, sets [INH] and [INH_STAT] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up | This bits intentionally activates INH PMOS pull up, sets [INH] and [INH_STAT] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up | This bits intentionally activates INH PMOS pull up, sets [INH] and [INH_STAT] to 1. (self-cleared) 0: mission mode 1: Trigger INH PMOS pull up |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.5.7 Register: DEV\_CONF1

## Address: 0x2001

| B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| - | - | - | - | - | - | - | - |
| SNIFDET_EN | SNIFDET_DIS | TONE_RX_EN | FCOMM_EN | TWO_STOP_EN | NFAULT_EN | RESERVED | HB_TX_EN |
| 0 | 0 | 0 | 1 | 0 | 1 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |

SNIFDET\_EN Enable the Sniff detector on COM* port, this bit is latched into AVAOREF domain, once latched in, this bit is still effective in SHUTDOWN 0: no effect

- 1: SNIF DET is enabled in SHUTDOWN

SNIFDET\_DIS Enable the Sniff detector on COM* port, this bit is latched into AVAOREF domain, once latched in, this bit is still effective in SHUTDOWN 0: no effect

- 1: SNIF DET is disabled in SHUTDOWN, if both SNIFDET\_EN and SNIFDET\_DIS are '1', SNIFDET\_DIS takes priority.

TONE\_RX\_EN Enable the Tone receiver, depends on [DIR\_SEL], one of the COML/COMH tone recover is enabled. COMH/COML tone receivers are enabled in VALIDATE disregarding setting of this bit.

- 0: Disable
- 1: Enable

FCOMM\_EN

Enable the fault state detection through communication in ACTIVE mode

- 0: Disable
- 1: Enable

TWO\_STOP\_EN Enables two stop bits for the UART in case of severe oscillator error in both the host and device

- 0: One STOP bit
- 1: Two STOP bit

NFAULT\_EN

Enables the NFAULT function

RESERVED

- 0: NFAULT driver is disabled
- 1: NFAULT pulls low to indicate an unmasked fault is detected

Reserved. Default value is 0. Please don't alter.

HB\_TX\_EN

Enable HEARTBEAT transmitter when device is in SLEEP mode

- 0: Disable
- 1: Enable

## 7.5.8 Register: DEV\_CONF2

| Address: 0x2002 - B7 - RSVD | Address: 0x2002 - B6 - RSVD | Address: 0x2002 - B5 - RSVD | Address: 0x2002 - B4 - RSVD | Address: 0x2002 - B3 - RSVD | Address: 0x2002 - B2 - RSVD | Address: 0x2002 - B1 - INH_DIS[1:0] | Address: 0x2002 - B0 - INH_DIS[1:0] |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |

INH\_DIS[1:0]

Disable INH driver (PMOS pull up). In all modes, this bit overwrites [INH\_SET\_GO] and fault tone detection event

00: INH function is enabled

- 01: INH function is enabled
- 10: INH function is enabled
- 11: INH function is DISABLED

## 7.5.9 Register: TX\_HOLD\_OFF

| Address: 0x2003 - B7 | Address: 0x2003 - B6 | Address: 0x2003 - B5 | Address: 0x2003 - B4 | Address: 0x2003 - B3 | Address: 0x2003 - B2 | Address: 0x2003 - B1 | Address: 0x2003 - B0 |
| - | - | - | - | - | - | - | - |
| DLY[7:0] | DLY[7:0] | DLY[7:0] | DLY[7:0] | DLY[7:0] | DLY[7:0] | DLY[7:0] | DLY[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| DLY[7:0] | Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame | Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame | Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame | Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame | Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame | Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame | Set the number of bit period delay from 0 to 255, after receiving the STOP bit of a command frame and before transmitting the 1st bit of response frame |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_012.png)

## 7.5.10 Register: SLP\_TIMEOUT

| Address: 0x2004 - B7 | Address: 0x2004 - B6 | Address: 0x2004 - B5 | Address: 0x2004 - B4 | Address: 0x2004 - B3 | Address: 0x2004 - B2 | Address: 0x2004 - B1 | Address: 0x2004 - B0 |
| - | - | - | - | - | - | - | - |
| RSVD | RSVD | RSVD | RSVD | RSVD | SLP_TME[2:0] | SLP_TME[2:0] | SLP_TME[2:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| SLP_TME[2:0] | This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 2hours | This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 2hours | This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 2hours | This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 2hours | This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 2hours | This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 2hours | This timer starts counting when device enters SLEEP or VALIDATE. When the timer expires, the device enters SHUTDOWN. The timer reset if device wakes up to ACTIVE. 000: no timeout. Device remains in SLEEP 001: 5s 010: 10s 011: 1min 100: 10mins 101: 30mins 110: 1hour 2hours |

## 7.5.11 Register: COMM\_TIMEOUT

| Address: 0x2005 - B7 | Address: 0x2005 - B6 | Address: 0x2005 - B5 | Address: 0x2005 - B4 | Address: 0x2005 - B3 | Address: 0x2005 - B2 | Address: 0x2005 - B1 | Address: 0x2005 - B0 |
| - | - | - | - | - | - | - | - |
| RSVD | CTS_TIME[2:0] | CTS_TIME[2:0] | CTS_TIME[2:0] | CTL_ACT | CTL_TIME[2:0] | CTL_TIME[2:0] | CTL_TIME[2:0] |
| 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| CTS_TIME[2:0] | Set the short communication timeout. When this timer expires, the device set the FAULT_SYS [CTS] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min | Set the short communication timeout. When this timer expires, the device set the FAULT_SYS [CTS] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min | Set the short communication timeout. When this timer expires, the device set the FAULT_SYS [CTS] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min | Set the short communication timeout. When this timer expires, the device set the FAULT_SYS [CTS] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min | Set the short communication timeout. When this timer expires, the device set the FAULT_SYS [CTS] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min | Set the short communication timeout. When this timer expires, the device set the FAULT_SYS [CTS] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min | Set the short communication timeout. When this timer expires, the device set the FAULT_SYS [CTS] bit. This can be used as an alert to the system to prevent a long communication timeout. 000: disable short communication timeout 001: 100ms 010: 2s 011: 10s (default) 100: 1min 101: 10mins 110: 30min |
| CTL_ACT | 1hour Configure the device action when long communication timeout timer expires 0: set FAULT_SYS[CTL] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT_SYS[CTL] bit will not be set | 1hour Configure the device action when long communication timeout timer expires 0: set FAULT_SYS[CTL] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT_SYS[CTL] bit will not be set | 1hour Configure the device action when long communication timeout timer expires 0: set FAULT_SYS[CTL] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT_SYS[CTL] bit will not be set | 1hour Configure the device action when long communication timeout timer expires 0: set FAULT_SYS[CTL] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT_SYS[CTL] bit will not be set | 1hour Configure the device action when long communication timeout timer expires 0: set FAULT_SYS[CTL] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT_SYS[CTL] bit will not be set | 1hour Configure the device action when long communication timeout timer expires 0: set FAULT_SYS[CTL] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT_SYS[CTL] bit will not be set | 1hour Configure the device action when long communication timeout timer expires 0: set FAULT_SYS[CTL] and send device to SLEEP mode (default at reset) 1: Send the device to SHUTDOWN. FAULT_SYS[CTL] bit will not be set |
| CTL_TIME[2:0] | Set the long communication timeout. When this timer expires, the device takes the action configured by the [CTL_ACT] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour | Set the long communication timeout. When this timer expires, the device takes the action configured by the [CTL_ACT] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour | Set the long communication timeout. When this timer expires, the device takes the action configured by the [CTL_ACT] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour | Set the long communication timeout. When this timer expires, the device takes the action configured by the [CTL_ACT] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour | Set the long communication timeout. When this timer expires, the device takes the action configured by the [CTL_ACT] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour | Set the long communication timeout. When this timer expires, the device takes the action configured by the [CTL_ACT] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour | Set the long communication timeout. When this timer expires, the device takes the action configured by the [CTL_ACT] bit. 000: disable long communication timeout 001: 100ms 010: 2s 011: 10s 100: 1min (default) 101: 10mins 110: 30min 111: 1hour |

## 7.5.12 Register: SPI\_FIFO\_UNLOCK

| Address: 0x2010 - B7 - RSVD | Address: 0x2010 - B6 - RSVD | Address: 0x2010 - B5 - RSVD | Address: 0x2010 - B4 - RSVD | Address: 0x2010 - B3 - CODE[3:0] | Address: 0x2010 - B2 - CODE[3:0] | Address: 0x2010 - B1 - CODE[3:0] | Address: 0x2010 - B0 - CODE[3:0] |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| CODE[3:0] | In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI_FIFO_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them. | In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI_FIFO_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them. | In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI_FIFO_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them. | In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI_FIFO_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them. | In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI_FIFO_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them. | In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI_FIFO_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them. | In UART mode - write has no impact and read always returns 0 In SPI mode - Write the unlock code 0x0A to SPI_FIFO_UNLOCK (MSB 4 bits are don't care, e.g. 0x2A would also unlock) and followed by writing [SPI_FIFO_DIAG_GO] = 1 to do FIFO diagnostic. For detailed steps of FIFO diagnostic, refer to safety manual. After these bits are written, read cmd doesn't affect them while any write cmd clears them. |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.5.13 Register: FAULT\_MSK

| Address: 0x2020 - B7 | Address: 0x2020 - B6 | Address: 0x2020 - B5 | Address: 0x2020 - B4 | Address: 0x2020 - B3 | Address: 0x2020 - B2 | Address: 0x2020 - B1 | Address: 0x2020 - B0 |
| - | - | - | - | - | - | - | - |
| MSK_COML_H | MSK_UART_SPI | MSK_FCOMM_D ET | MSK_FTONE_DE T | MSK_HB | MSK_REG | MSK_SYS | MSK_PWR |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| MSK_COML_H | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to bits: [COML_FRAME], [COMH_FRAME], [COML_PHY], [COMH_PHY] and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to bits: [COML_FRAME], [COMH_FRAME], [COML_PHY], [COMH_PHY] and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to bits: [COML_FRAME], [COMH_FRAME], [COML_PHY], [COMH_PHY] and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to bits: [COML_FRAME], [COMH_FRAME], [COML_PHY], [COMH_PHY] and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to bits: [COML_FRAME], [COMH_FRAME], [COML_PHY], [COMH_PHY] and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to bits: [COML_FRAME], [COMH_FRAME], [COML_PHY], [COMH_PHY] and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to bits: [COML_FRAME], [COMH_FRAME], [COML_PHY], [COMH_PHY] and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above |
| MSK_UART_SPI | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [STOP_DET], [COMMCLR_DET], [UART_FRAME], [SPI_FRAME], [SPI_PHY] bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [STOP_DET], [COMMCLR_DET], [UART_FRAME], [SPI_FRAME], [SPI_PHY] bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [STOP_DET], [COMMCLR_DET], [UART_FRAME], [SPI_FRAME], [SPI_PHY] bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [STOP_DET], [COMMCLR_DET], [UART_FRAME], [SPI_FRAME], [SPI_PHY] bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [STOP_DET], [COMMCLR_DET], [UART_FRAME], [SPI_FRAME], [SPI_PHY] bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [STOP_DET], [COMMCLR_DET], [UART_FRAME], [SPI_FRAME], [SPI_PHY] bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [STOP_DET], [COMMCLR_DET], [UART_FRAME], [SPI_FRAME], [SPI_PHY] bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above |
| MSK_FCOMM_D ET | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FCOMM_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FCOMM_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FCOMM_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FCOMM_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FCOMM_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FCOMM_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FCOMM_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above |
| MSK_FTONE_DE T | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FTONE_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FTONE_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FTONE_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FTONE_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FTONE_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FTONE_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [FTONE_DET] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected 1: No NFAULT action, [FAULT_COMM] not set due to faults above |
| MSK_HB | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [HB_FAIL] and [HB_FAST] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [HB_FAIL] and [HB_FAST] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [HB_FAIL] and [HB_FAST] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [HB_FAIL] and [HB_FAST] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [HB_FAIL] and [HB_FAST] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [HB_FAIL] and [HB_FAST] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected | If this bit is set, [FAULT_COMM] bit in FAULT_SUMMARY register is not set (NFAULT won't toggle) due to [HB_FAIL] and [HB_FAST] 0: Assert NFAULT and set [FAULT_COMM] if fault above is detected |
| MSK_REG | 1: No NFAULT action, If this bit is set, [FAULT_REG] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to OTP fault. It doesn't affect FAULT_REG register. 0: Mask disabled 1: Mask enabled to prevent fault signaling | [FAULT_COMM] | not set due to faults | above | 1: No NFAULT action, If this bit is set, [FAULT_REG] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to OTP fault. It doesn't affect FAULT_REG register. 0: Mask disabled 1: Mask enabled to prevent fault signaling | 1: No NFAULT action, If this bit is set, [FAULT_REG] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to OTP fault. It doesn't affect FAULT_REG register. 0: Mask disabled 1: Mask enabled to prevent fault signaling | 1: No NFAULT action, If this bit is set, [FAULT_REG] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to OTP fault. It doesn't affect FAULT_REG register. 0: Mask disabled 1: Mask enabled to prevent fault signaling |
| MSK_SYS | If this bit is set, [FAULT_SYS] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT_SYS register. 0: Assert NFAULT if any bit from FAULT_SYS is set to '1' | If this bit is set, [FAULT_SYS] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT_SYS register. 0: Assert NFAULT if any bit from FAULT_SYS is set to '1' | If this bit is set, [FAULT_SYS] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT_SYS register. 0: Assert NFAULT if any bit from FAULT_SYS is set to '1' | If this bit is set, [FAULT_SYS] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT_SYS register. 0: Assert NFAULT if any bit from FAULT_SYS is set to '1' | If this bit is set, [FAULT_SYS] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT_SYS register. 0: Assert NFAULT if any bit from FAULT_SYS is set to '1' | If this bit is set, [FAULT_SYS] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT_SYS register. 0: Assert NFAULT if any bit from FAULT_SYS is set to '1' | If this bit is set, [FAULT_SYS] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to SYS fault. It doesn't affect FAULT_SYS register. 0: Assert NFAULT if any bit from FAULT_SYS is set to '1' |
| MSK_PWR | 1: No NFAULT action If this bit is set, [FAULT_PWR] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to PWR fault. It doesn't affect FAULT_PWR register. 0: Mask disabled 1: Mask enabled to prevent fault signaling | regardless of | FAULT_SYS status | 1: No NFAULT action If this bit is set, [FAULT_PWR] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to PWR fault. It doesn't affect FAULT_PWR register. 0: Mask disabled 1: Mask enabled to prevent fault signaling | 1: No NFAULT action If this bit is set, [FAULT_PWR] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to PWR fault. It doesn't affect FAULT_PWR register. 0: Mask disabled 1: Mask enabled to prevent fault signaling | 1: No NFAULT action If this bit is set, [FAULT_PWR] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to PWR fault. It doesn't affect FAULT_PWR register. 0: Mask disabled 1: Mask enabled to prevent fault signaling | 1: No NFAULT action If this bit is set, [FAULT_PWR] bit in FAULT_SUMMARY register is not set and NFAULT won't toggle due to PWR fault. It doesn't affect FAULT_PWR register. 0: Mask disabled 1: Mask enabled to prevent fault signaling |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

## 7.5.14 Register: FAULT\_RST

| Address: 0x2030 - B7 | Address: 0x2030 - B6 | Address: 0x2030 - B5 | Address: 0x2030 - B4 | Address: 0x2030 - B3 | Address: 0x2030 - B2 | Address: 0x2030 - B1 | Address: 0x2030 - B0 |
| - | - | - | - | - | - | - | - |
| RST_COML_H | RST_UART_SPI | RST_FCOMM_DE T | RST_FTONE_DE T | RST_HB | RST_REG | RST_SYS | RST_PWR |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| RST_COML_H | Reset bits: COML_FRAME, COMH_FRAME, COML_PHY, COMH_PHY and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset bits: COML_FRAME, COMH_FRAME, COML_PHY, COMH_PHY and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset bits: COML_FRAME, COMH_FRAME, COML_PHY, COMH_PHY and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset bits: COML_FRAME, COMH_FRAME, COML_PHY, COMH_PHY and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset bits: COML_FRAME, COMH_FRAME, COML_PHY, COMH_PHY and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset bits: COML_FRAME, COMH_FRAME, COML_PHY, COMH_PHY and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset bits: COML_FRAME, COMH_FRAME, COML_PHY, COMH_PHY and registers: DEBUG_COMH_PHY, DEBUG_COMH_FRAME, DEBUG_COML_PHY, DEBUG_COML_FRAME. self-cleared bit. 0: Do not reset 1: Reset to 0x00 |
| RST_UART_SPI | Reset STOP_DET, COMMCLR_DET, UART_FRAME, SPI_FRAME, SPI_PHY bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset STOP_DET, COMMCLR_DET, UART_FRAME, SPI_FRAME, SPI_PHY bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset STOP_DET, COMMCLR_DET, UART_FRAME, SPI_FRAME, SPI_PHY bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset STOP_DET, COMMCLR_DET, UART_FRAME, SPI_FRAME, SPI_PHY bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset STOP_DET, COMMCLR_DET, UART_FRAME, SPI_FRAME, SPI_PHY bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset STOP_DET, COMMCLR_DET, UART_FRAME, SPI_FRAME, SPI_PHY bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00 | Reset STOP_DET, COMMCLR_DET, UART_FRAME, SPI_FRAME, SPI_PHY bits and DEBUG_UART_FRAME, DEBUG_SPI_PHY, DEBUG_SPI_FRAME registers. self-cleared bit. 0: Do not reset 1: Reset to 0x00 |
| RST_FCOMM_DE T | Reset FCOMM_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FCOMM_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FCOMM_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FCOMM_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FCOMM_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FCOMM_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FCOMM_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' |
| RST_FTONE_DE T | Reset FTONE_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FTONE_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FTONE_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FTONE_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FTONE_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FTONE_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset FTONE_DET bit, self-cleared bit. 0: Do not reset 1: Reset to '0' |
| RST_HB | Reset HB_FAIL and HB_FAST bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset HB_FAIL and HB_FAST bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset HB_FAIL and HB_FAST bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset HB_FAIL and HB_FAST bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset HB_FAIL and HB_FAST bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset HB_FAIL and HB_FAST bit, self-cleared bit. 0: Do not reset 1: Reset to '0' | Reset HB_FAIL and HB_FAST bit, self-cleared bit. 0: Do not reset 1: Reset to '0' |
| RST_REG | Resets FAULT_SUMMARY [FAULT_REG] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0' | Resets FAULT_SUMMARY [FAULT_REG] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0' | Resets FAULT_SUMMARY [FAULT_REG] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0' | Resets FAULT_SUMMARY [FAULT_REG] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0' | Resets FAULT_SUMMARY [FAULT_REG] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0' | Resets FAULT_SUMMARY [FAULT_REG] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0' | Resets FAULT_SUMMARY [FAULT_REG] to '0', self-cleared bit. 0: Do not reset 1: Reset to '0' |
| RST_SYS | This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT_SYS and [FAULT_SYS] to 0x00 and '0' | This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT_SYS and [FAULT_SYS] to 0x00 and '0' | This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT_SYS and [FAULT_SYS] to 0x00 and '0' | This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT_SYS and [FAULT_SYS] to 0x00 and '0' | This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT_SYS and [FAULT_SYS] to 0x00 and '0' | This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT_SYS and [FAULT_SYS] to 0x00 and '0' | This bit is self-clear to 0 after writing to 1. 0: Do not reset 1: Reset register FAULT_SYS and [FAULT_SYS] to 0x00 and '0' |
| RST_PWR | Resets FAULT_SUMMARY [FAULT_PWR] to '0' and register FAULT_PWR, self-cleared bit. 0: Do not reset 1: Reset | Resets FAULT_SUMMARY [FAULT_PWR] to '0' and register FAULT_PWR, self-cleared bit. 0: Do not reset 1: Reset | Resets FAULT_SUMMARY [FAULT_PWR] to '0' and register FAULT_PWR, self-cleared bit. 0: Do not reset 1: Reset | Resets FAULT_SUMMARY [FAULT_PWR] to '0' and register FAULT_PWR, self-cleared bit. 0: Do not reset 1: Reset | Resets FAULT_SUMMARY [FAULT_PWR] to '0' and register FAULT_PWR, self-cleared bit. 0: Do not reset 1: Reset | Resets FAULT_SUMMARY [FAULT_PWR] to '0' and register FAULT_PWR, self-cleared bit. 0: Do not reset 1: Reset | Resets FAULT_SUMMARY [FAULT_PWR] to '0' and register FAULT_PWR, self-cleared bit. 0: Do not reset 1: Reset |

## 7.5.15 Register: FAULT\_SUMMARY

| Address: 0x2100 - B7 - RSVD | Address: 0x2100 - B6 - RSVD | Address: 0x2100 - B5 - RSVD | Address: 0x2100 - B4 - RSVD | Address: 0x2100 - B3 - FAULT_COMM | Address: 0x2100 - B2 - FAULT_REG | Address: 0x2100 - B1 - FAULT_SYS | Address: 0x2100 - B0 - FAULT_PWR |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| FAULT_COMM | Indicate communication related fault is detected (any bits in register FAULT_COMM1, FAULT_COMM2 is set) 0: No fault 1: Fault | Indicate communication related fault is detected (any bits in register FAULT_COMM1, FAULT_COMM2 is set) 0: No fault 1: Fault | Indicate communication related fault is detected (any bits in register FAULT_COMM1, FAULT_COMM2 is set) 0: No fault 1: Fault | Indicate communication related fault is detected (any bits in register FAULT_COMM1, FAULT_COMM2 is set) 0: No fault 1: Fault | Indicate communication related fault is detected (any bits in register FAULT_COMM1, FAULT_COMM2 is set) 0: No fault 1: Fault | Indicate communication related fault is detected (any bits in register FAULT_COMM1, FAULT_COMM2 is set) 0: No fault 1: Fault | Indicate communication related fault is detected (any bits in register FAULT_COMM1, FAULT_COMM2 is set) 0: No fault 1: Fault |
| FAULT_REG | Indicate registers related fault is detected 0: No fault 1: Fault | Indicate registers related fault is detected 0: No fault 1: Fault | Indicate registers related fault is detected 0: No fault 1: Fault | Indicate registers related fault is detected 0: No fault 1: Fault | Indicate registers related fault is detected 0: No fault 1: Fault | Indicate registers related fault is detected 0: No fault 1: Fault | Indicate registers related fault is detected 0: No fault 1: Fault |
| FAULT_SYS | Indicates system fault is detected (any bits in register FAULT_SYS). 0: No fault 1: Fault | Indicates system fault is detected (any bits in register FAULT_SYS). 0: No fault 1: Fault | Indicates system fault is detected (any bits in register FAULT_SYS). 0: No fault 1: Fault | Indicates system fault is detected (any bits in register FAULT_SYS). 0: No fault 1: Fault | Indicates system fault is detected (any bits in register FAULT_SYS). 0: No fault 1: Fault | Indicates system fault is detected (any bits in register FAULT_SYS). 0: No fault 1: Fault | Indicates system fault is detected (any bits in register FAULT_SYS). 0: No fault 1: Fault |
| FAULT_PWR | Indicates a power supply fault is detected (any bits in register FAULT_PWR) 0: No fault 1: Fault | Indicates a power supply fault is detected (any bits in register FAULT_PWR) 0: No fault 1: Fault | Indicates a power supply fault is detected (any bits in register FAULT_PWR) 0: No fault 1: Fault | Indicates a power supply fault is detected (any bits in register FAULT_PWR) 0: No fault 1: Fault | Indicates a power supply fault is detected (any bits in register FAULT_PWR) 0: No fault 1: Fault | Indicates a power supply fault is detected (any bits in register FAULT_PWR) 0: No fault 1: Fault | Indicates a power supply fault is detected (any bits in register FAULT_PWR) 0: No fault 1: Fault |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.5.16 Register: FAULT\_REG

| Address: 0x2101 - B7 | Address: 0x2101 - B6 | Address: 0x2101 - B5 - RSVD | Address: 0x2101 - B4 | Address: 0x2101 - B3 | Address: 0x2101 - B2 - CONF_MON_ERR | Address: 0x2101 - B1 - FACTLDERR | Address: 0x2101 - B0 - FACT_CRC |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

CONF\_MON\_ER

R

FACTLDERR

Indicates monitored 2 registers (DEV\_CONF1, FAULT\_MSK) have at least one bit flip. For usage, refer to paragraph: Register Bit Flip Monitor.

- 0: No fault
- 1: Fault

Indicates the factory NVM registers could not be loaded from OTP.

FACT\_CRC

- 0: No fault
- 1: Fault

Indicates a CRC error has occurred in the factory register space.

- 0: No fault
- 1: Fault

## 7.5.17 Register: FAULT\_SYS

| Address: 0x2102 - B7 | Address: 0x2102 - B6 | Address: 0x2102 - B5 | Address: 0x2102 - B4 | Address: 0x2102 - B3 | Address: 0x2102 - B2 | Address: 0x2102 - B1 | Address: 0x2102 - B0 |
| - | - | - | - | - | - | - | - |
| VALIDATE_DET | LFO | SHUTDOWN_REC | DRST | CTL | CTS | TSHUT | INH |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

VALIDATE\_DET Indicates device transitioned to VALIDATE mode

- 0: no transitioned to VALIDATE MODE
- 1: transitioned to VALIDATE MODE

LFO

Indicated LFO frequency is off by +/-25%

## SHUTDOWN\_RE C

- 0: no fault
- 1: fault

Indicates the device was shut down using SHUTDOWN ping. If this bit is set, the COML and COMH RX are both disabled at wake up as a way to isolate itself from the stack. Send another wake ping or [SOFT\_RESET] to re-enable COMH/L RX.

DRST

- 0: The previous SHUTDOWN was normal
- 1: The previous SHUTDOWN was caused by ping, which is not a usual SHUTDOWN method, indicating potential communication issue with the device

Indicates a digital reset has occurred.

CTL

CTS

TSHUT

- 0: no digital reset
- 1: digital reset has occurred

Indicates a long communication timeout occurred. Device action is configured by [CTL\_ACT]. This bit is not observable if the action is set to device shutdown.

- 0: No fault
- 1: long communication timeout occurs. Observable if long timeout action is set to SLEEP

Indicates a short communication timeout occurred. No action from the device. This can be served as an alert to system before reaching long communication timeout.

- 0: No fault
- 1: short communication timeout occurs

Indicates the previous shutdown was due to thermal shutdown

INH

- 0: die temp is &lt; thermal shutdown threshold
- 1: the previous shutdown was to due thermal shutdown

Indicates INH PMOS is enabled

- 0: INH driver is off
- 1: INH driver enabled, pulls pin up to BAT

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_023.png)

## 7.5.18 Register: FAULT\_PWR

| Address: 0x2103 - B7 | Address: 0x2103 - B6 | Address: 0x2103 - B5 | Address: 0x2103 - B4 | Address: 0x2103 - B3 | Address: 0x2103 - B2 | Address: 0x2103 - B1 | Address: 0x2103 - B0 |
| - | - | - | - | - | - | - | - |
| RSVD | RSVD | RSVD | CVDD_UV_DRST | CVDD_OV | DVDD_OV | AVDDREF_OV | AVAO_SW_FAIL |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| CVDD_UV_DRST | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. 0: no fault 1: fault | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. 0: no fault 1: fault | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. 0: no fault 1: fault | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. 0: no fault 1: fault | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. 0: no fault 1: fault | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. 0: no fault 1: fault | Indicates CVDDUV fault caused DRST. Shutdown/power up event shall not trigger this fault. 0: no fault 1: fault |
| CVDD_OV | Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the CVDD pin 0: no fault 1: fault |
| DVDD_OV | Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault | Indicates an over voltage fault on the DVDD pin 0: no fault 1: fault |
| AVDDREF_OV | Indicates an over voltage fault on the AVDD_REF internal supply 0: no fault 1: fault | Indicates an over voltage fault on the AVDD_REF internal supply 0: no fault 1: fault | Indicates an over voltage fault on the AVDD_REF internal supply 0: no fault 1: fault | Indicates an over voltage fault on the AVDD_REF internal supply 0: no fault 1: fault | Indicates an over voltage fault on the AVDD_REF internal supply 0: no fault 1: fault | Indicates an over voltage fault on the AVDD_REF internal supply 0: no fault 1: fault | Indicates an over voltage fault on the AVDD_REF internal supply 0: no fault 1: fault |
| AVAO_SW_FAIL | Indicates a fault is detected on the AVAO_REF switch. 0: no fault 1: fault | Indicates a fault is detected on the AVAO_REF switch. 0: no fault 1: fault | Indicates a fault is detected on the AVAO_REF switch. 0: no fault 1: fault | Indicates a fault is detected on the AVAO_REF switch. 0: no fault 1: fault | Indicates a fault is detected on the AVAO_REF switch. 0: no fault 1: fault | Indicates a fault is detected on the AVAO_REF switch. 0: no fault 1: fault | Indicates a fault is detected on the AVAO_REF switch. 0: no fault 1: fault |

## 7.5.19 Register: FAULT\_COMM1

| Address: 0x2104 - B7 | Address: 0x2104 - B6 | Address: 0x2104 - B5 | Address: 0x2104 - B4 | Address: 0x2104 - B3 | Address: 0x2104 - B2 | Address: 0x2104 - B1 | Address: 0x2104 - B0 |
| - | - | - | - | - | - | - | - |
| RSVD | FCOMM_DET | FTONE_DET | HB_FAIL | HB_FAST | UART_FRAME | COMMCLR_DET | STOP_DET |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| FCOMM_DET | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 family 0: no fault 1: fault | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 family 0: no fault 1: fault | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 family 0: no fault 1: fault | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 family 0: no fault 1: fault | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 family 0: no fault 1: fault | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 family 0: no fault 1: fault | Indicates the fault status bit in comm frame is set by stack devices. At least a fault in stack devices happened. Only apply to non-bq79606 family 0: no fault 1: fault |
| FTONE_DET | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault 1: fault | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault 1: fault | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault 1: fault | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault 1: fault | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault 1: fault | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault 1: fault | Indicates the fault tone is detected, COM Port in sleep mode if work with non-bq79606 (Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault 1: fault |
| HB_FAIL | Indicates HB tone is NOT detected within tHB_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault | Indicates HB tone is NOT detected within tHB_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault | Indicates HB tone is NOT detected within tHB_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault | Indicates HB tone is NOT detected within tHB_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault | Indicates HB tone is NOT detected within tHB_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault | Indicates HB tone is NOT detected within tHB_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault | Indicates HB tone is NOT detected within tHB_PERIOD, not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) 0: no fault, HB tone detected as expected 1: fault |
| HB_FAST | Indicates HB tone is detected within tHB_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) This bit could also be set when [FTONE_DET]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault | Indicates HB tone is detected within tHB_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) This bit could also be set when [FTONE_DET]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault | Indicates HB tone is detected within tHB_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) This bit could also be set when [FTONE_DET]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault | Indicates HB tone is detected within tHB_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) This bit could also be set when [FTONE_DET]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault | Indicates HB tone is detected within tHB_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) This bit could also be set when [FTONE_DET]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault | Indicates HB tone is detected within tHB_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) This bit could also be set when [FTONE_DET]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault | Indicates HB tone is detected within tHB_FAST (too frequent), not supported with BQ79606A-Q1 ( Detection is monitoring the COML side if [DIR_SEL] = 0 and vice versa.) This bit could also be set when [FTONE_DET]=1 depends on how soon the Fault Tone is detected from previous Heartbeat tone. 0: no fault |
| UART_FRAME | fault Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG_UART_FRAME register 0: no fault | fault Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG_UART_FRAME register 0: no fault | fault Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG_UART_FRAME register 0: no fault | fault Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG_UART_FRAME register 0: no fault | fault Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG_UART_FRAME register 0: no fault | fault Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG_UART_FRAME register 0: no fault | fault Indicates a UART FAULT detected when receiving command or transmitting response frames Further detail of the fault information is available in the DEBUG_UART_FRAME register 0: no fault |
| COMMCLR_DET | fault A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear | fault A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear | fault A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear | fault A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear | fault A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear | fault A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear | fault A UART/SPI communication clear signal is detected. This bit is set when Sleep2active ping is sent in UART mode. While in SPI mode, it is not set when sleep2active ping is sent. 0: no UART/SPI Comm Clear |
| STOP_DET | UART/SPI Comm Indicates and unexpected STOP condition is received. Apply to UART mode. This bit is set when Sleep2active ping is sent in ACTIVE. 0: no fault 1: fault | Clear detected | UART/SPI Comm Indicates and unexpected STOP condition is received. Apply to UART mode. This bit is set when Sleep2active ping is sent in ACTIVE. 0: no fault 1: fault | UART/SPI Comm Indicates and unexpected STOP condition is received. Apply to UART mode. This bit is set when Sleep2active ping is sent in ACTIVE. 0: no fault 1: fault | UART/SPI Comm Indicates and unexpected STOP condition is received. Apply to UART mode. This bit is set when Sleep2active ping is sent in ACTIVE. 0: no fault 1: fault | UART/SPI Comm Indicates and unexpected STOP condition is received. Apply to UART mode. This bit is set when Sleep2active ping is sent in ACTIVE. 0: no fault 1: fault | UART/SPI Comm Indicates and unexpected STOP condition is received. Apply to UART mode. This bit is set when Sleep2active ping is sent in ACTIVE. 0: no fault 1: fault |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.5.20 Register: FAULT\_COMM2

## Address: 0x2105

| B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| - | - | - | - | - | - | - | - |
| RSVD | RSVD | SPI_FRAME | SPI_PHY | COML_FRAME | COML_PHY | COMH_FRAME | COMH_PHY |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

SPI\_FRAME

SPI\_PHY

Indicates a SPI frame level FAULT detected when receiving command or transmitting response frames. Further detail of the fault information is available in the DEBUG\_SPI\_FRAME register

- 0: no fault
- 1: fault

Indicates a SPI bit level FAULT detected when receiving command or transmitting response frames. Further detail of the fault information is available in the DEBUG\_SPI\_PHY register

- 0: no fault
- 1: fault

COML\_FRAME Indicate a COML byte level fault detected when receiving response frames. Further details of the fault information is available in DEBUG\_COML\_FRAME

- 0: no fault
- 1: fault

Indicate a COML bit level fault detected, which would cause at least a byte level (RC\_RR) fault. Further details of the fault information are available in DEBUG\_COML\_PHY register.

- 0: no fault
- 1: fault

COMH\_FRAME Indicate a COMH byte level fault detected when receiving response frames. Further details of the fault information is available in DEBUG\_COMH\_FRAME

- 0: no fault
- 1: fault

Indicate a COMH bit level fault detected, which would cause at least a byte level (RC\_RR) fault. Further details of the fault information are available in DEBUG\_COMH\_PHY register.

- 0: no fault
- 1: fault

COMH\_PHY

## 7.5.21 Register: DEV\_DIAG\_STAT

| Address: 0x2110 - B7 - RSVD | Address: 0x2110 - B6 - RSVD | Address: 0x2110 - B5 - RSVD | Address: 0x2110 - B4 - RSVD | Address: 0x2110 - B3 - RSVD | Address: 0x2110 - B2 - RSVD | Address: 0x2110 - B1 - PWR_DIAG_RDY | Address: 0x2110 - B0 - INH_STAT |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

PWR\_DIAG\_RDY Indicates a power supply BIST test is done. It is cleared when [PWR\_DIAG\_GO] bit is set.

0: BIST is not done

1: BIST is done

INH\_STAT

Indicates INH Pin see VINH\_DET, this bit reflects real time value of pin INH

0: Voltage not detected

1: Voltage detected

## 7.5.22 Register: PARTID

| Address: 0x2120 - B7 | Address: 0x2120 - B6 | Address: 0x2120 - B5 | Address: 0x2120 - B4 | Address: 0x2120 - B3 | Address: 0x2120 - B2 | Address: 0x2120 - B1 | Address: 0x2120 - B0 |
| - | - | - | - | - | - | - | - |
| REV[7:0] | REV[7:0] | REV[7:0] | REV[7:0] | REV[7:0] | REV[7:0] | REV[7:0] | REV[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| REV[7:0] | Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. | Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. | Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. | Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. | Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. | Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. | Device revision 0x00 = A0, 0x01 = A1, 0x02 = A2, etc. |

COML\_PHY

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_012.png)

## 7.5.23 Register: DIE\_ID1

| Address: 0x2121 - B7 | Address: 0x2121 - B6 | Address: 0x2121 - B5 | Address: 0x2121 - B4 | Address: 0x2121 - B3 | Address: 0x2121 - B2 | Address: 0x2121 - B1 | Address: 0x2121 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.24 Register: DIE\_ID2

| Address: 0x2122 - B7 | Address: 0x2122 - B6 | Address: 0x2122 - B5 | Address: 0x2122 - B4 | Address: 0x2122 - B3 | Address: 0x2122 - B2 | Address: 0x2122 - B1 | Address: 0x2122 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.25 Register: DIE\_ID3

| Address: 0x2123 - B7 | Address: 0x2123 - B6 | Address: 0x2123 - B5 | Address: 0x2123 - B4 | Address: 0x2123 - B3 | Address: 0x2123 - B2 | Address: 0x2123 - B1 | Address: 0x2123 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.26 Register: DIE\_ID4

| Address: 0x2124 - B7 | Address: 0x2124 - B6 | Address: 0x2124 - B5 | Address: 0x2124 - B4 | Address: 0x2124 - B3 | Address: 0x2124 - B2 | Address: 0x2124 - B1 | Address: 0x2124 - B0 |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.27 Register: DIE\_ID5

| Address: 0x2125 - B7 | Address: 0x2125 - B6 | Address: 0x2125 - B5 | Address: 0x2125 - B4 | Address: 0x2125 - B3 | Address: 0x2125 - B2 | Address: 0x2125 - B1 | Address: 0x2125 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.28 Register: DIE\_ID6

| Address: 0x2126 - B7 | Address: 0x2126 - B6 | Address: 0x2126 - B5 | Address: 0x2126 - B4 | Address: 0x2126 - B3 | Address: 0x2126 - B2 | Address: 0x2126 - B1 | Address: 0x2126 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_046.png)

## 7.5.29 Register: DIE\_ID7

| Address: 0x2127 - B7 | Address: 0x2127 - B6 | Address: 0x2127 - B5 | Address: 0x2127 - B4 | Address: 0x2127 - B3 | Address: 0x2127 - B2 | Address: 0x2127 - B1 | Address: 0x2127 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.30 Register: DIE\_ID8

| Address: 0x2128 - B7 | Address: 0x2128 - B6 | Address: 0x2128 - B5 | Address: 0x2128 - B4 | Address: 0x2128 - B3 | Address: 0x2128 - B2 | Address: 0x2128 - B1 | Address: 0x2128 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.31 Register: DIE\_ID9

| Address: 0x2129 - B7 | Address: 0x2129 - B6 | Address: 0x2129 - B5 | Address: 0x2129 - B4 | Address: 0x2129 - B3 | Address: 0x2129 - B2 | Address: 0x2129 - B1 | Address: 0x2129 - B0 |
| - | - | - | - | - | - | - | - |
| ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] | ID[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| ID[7:0] | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. | Digital reset value 0x00, after factory NVM loaded successfully, it is value in the NVM. |

## 7.5.32 Register: DEBUG\_CTRL\_UNLOCK

| Address: 0x2200 - B7 | Address: 0x2200 - B6 | Address: 0x2200 - B5 | Address: 0x2200 - B4 | Address: 0x2200 - B3 | Address: 0x2200 - B2 | Address: 0x2200 - B1 | Address: 0x2200 - B0 |
| - | - | - | - | - | - | - | - |
| CODE[7:0] | CODE[7:0] | CODE[7:0] | CODE[7:0] | CODE[7:0] | CODE[7:0] | CODE[7:0] | CODE[7:0] |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| CODE[7:0] | Write the unlock code (0xA5) to this register to activate the setting in the DEBUG_COMM_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG_COMM_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG_COMM_STAT register. | Write the unlock code (0xA5) to this register to activate the setting in the DEBUG_COMM_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG_COMM_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG_COMM_STAT register. | Write the unlock code (0xA5) to this register to activate the setting in the DEBUG_COMM_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG_COMM_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG_COMM_STAT register. | Write the unlock code (0xA5) to this register to activate the setting in the DEBUG_COMM_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG_COMM_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG_COMM_STAT register. | Write the unlock code (0xA5) to this register to activate the setting in the DEBUG_COMM_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG_COMM_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG_COMM_STAT register. | Write the unlock code (0xA5) to this register to activate the setting in the DEBUG_COMM_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG_COMM_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG_COMM_STAT register. | Write the unlock code (0xA5) to this register to activate the setting in the DEBUG_COMM_CTRL register. Any other value than the unlock code will deactivate any effect in the DEBUG_COMM_CTRL setting and return to the device's normal setting. This register doesn't affect DEBUG_COMM_STAT register. |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_007.png)

## 7.5.33 Register: DEBUG\_COMM\_CTRL

| Address: 0x2201 B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| - | - | - | - | - | - | - | - |
| RSVD | COML_TX_EN | COML_RX_EN | COMH_TX_EN | COMH_RX_EN | UART_VIF_BAUD | USER_UART_E N | USER_DAISY_EN |
| 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 |
| RW | RW | RW | RW | RW | RW | RW | RW |
| COML_TX_EN | Enable COML transmitter 0: disable 1: enable | Enable COML transmitter 0: disable 1: enable | Enable COML transmitter 0: disable 1: enable | Enable COML transmitter 0: disable 1: enable | Enable COML transmitter 0: disable 1: enable | Enable COML transmitter 0: disable 1: enable | Enable COML transmitter 0: disable 1: enable |
| COML_RX_EN | Enable COML receiver 0: disable 1: enable | Enable COML receiver 0: disable 1: enable | Enable COML receiver 0: disable 1: enable | Enable COML receiver 0: disable 1: enable | Enable COML receiver 0: disable 1: enable | Enable COML receiver 0: disable 1: enable | Enable COML receiver 0: disable 1: enable |
| COMH_TX_EN | Enable COMH transmitter 0: disable 1: enable | Enable COMH transmitter 0: disable 1: enable | Enable COMH transmitter 0: disable 1: enable | Enable COMH transmitter 0: disable 1: enable | Enable COMH transmitter 0: disable 1: enable | Enable COMH transmitter 0: disable 1: enable | Enable COMH transmitter 0: disable 1: enable |
| COMH_RX_EN | Enable COMH receiver 0: disable 1: enable | Enable COMH receiver 0: disable 1: enable | Enable COMH receiver 0: disable 1: enable | Enable COMH receiver 0: disable 1: enable | Enable COMH receiver 0: disable 1: enable | Enable COMH receiver 0: disable 1: enable | Enable COMH receiver 0: disable 1: enable |
| UART_VIF_BAUD | This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps | This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps | This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps | This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps | This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps | This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps | This bit changes the baud rate of UART and Daisy Chain (Also called VIF) to 250kb/s. Useful on Daisy Chain debug. When system set all the daisy chain devices to the 250kb/s baud rate, it slows down the response byte through the Daisy Chain to increase the robustness of the Daisy Chain for debug purpose. 0: 1Mbps |
| USER_UART_EN | 1: 250kbps This bit enables [UART_VIF_BAUD] setting 0: disable 1: enable | 1: 250kbps This bit enables [UART_VIF_BAUD] setting 0: disable 1: enable | 1: 250kbps This bit enables [UART_VIF_BAUD] setting 0: disable 1: enable | 1: 250kbps This bit enables [UART_VIF_BAUD] setting 0: disable 1: enable | 1: 250kbps This bit enables [UART_VIF_BAUD] setting 0: disable 1: enable | 1: 250kbps This bit enables [UART_VIF_BAUD] setting 0: disable 1: enable | 1: 250kbps This bit enables [UART_VIF_BAUD] setting 0: disable 1: enable |
| USER_DAISY_E N | This bit enables the setting of bits [6:3] in this register 0: the setting of bits [6:3 ] of current register has no effect 1: the device will configure the COML and COMH per current register setting | This bit enables the setting of bits [6:3] in this register 0: the setting of bits [6:3 ] of current register has no effect 1: the device will configure the COML and COMH per current register setting | This bit enables the setting of bits [6:3] in this register 0: the setting of bits [6:3 ] of current register has no effect 1: the device will configure the COML and COMH per current register setting | This bit enables the setting of bits [6:3] in this register 0: the setting of bits [6:3 ] of current register has no effect 1: the device will configure the COML and COMH per current register setting | This bit enables the setting of bits [6:3] in this register 0: the setting of bits [6:3 ] of current register has no effect 1: the device will configure the COML and COMH per current register setting | This bit enables the setting of bits [6:3] in this register 0: the setting of bits [6:3 ] of current register has no effect 1: the device will configure the COML and COMH per current register setting | This bit enables the setting of bits [6:3] in this register 0: the setting of bits [6:3 ] of current register has no effect 1: the device will configure the COML and COMH per current register setting |

## 7.5.34 Register: DEBUG\_COMM\_STAT

| Address: 0x2300 - B7 | Address: 0x2300 - B6 | Address: 0x2300 - B5 | Address: 0x2300 - B4 | Address: 0x2300 - B3 | Address: 0x2300 - B2 | Address: 0x2300 - B1 | Address: 0x2300 - B0 |
| - | - | - | - | - | - | - | - |
| RSVD | RSVD | RSVD | HW_DAISY_DRV | COML_TX_ON | COML_RX_ON | COMH_TX_ON | COMH_RX_ON |
| 0 | 0 | 0 | 1 | 0 | 0 | 1 | 1 |
| R | R | R | R | R | R | R | R |
| HW_DAISY_DRV | Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG_COMM_CTRL [USER_DAISY_EN] = 1. COML and COMH are under manual control through DEBUG_COMM_CTRL register 1: COML and COMH are controlled by the device | Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG_COMM_CTRL [USER_DAISY_EN] = 1. COML and COMH are under manual control through DEBUG_COMM_CTRL register 1: COML and COMH are controlled by the device | Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG_COMM_CTRL [USER_DAISY_EN] = 1. COML and COMH are under manual control through DEBUG_COMM_CTRL register 1: COML and COMH are controlled by the device | Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG_COMM_CTRL [USER_DAISY_EN] = 1. COML and COMH are under manual control through DEBUG_COMM_CTRL register 1: COML and COMH are controlled by the device | Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG_COMM_CTRL [USER_DAISY_EN] = 1. COML and COMH are under manual control through DEBUG_COMM_CTRL register 1: COML and COMH are controlled by the device | Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG_COMM_CTRL [USER_DAISY_EN] = 1. COML and COMH are under manual control through DEBUG_COMM_CTRL register 1: COML and COMH are controlled by the device | Indicates the COML and COMH are controlled by the device itself or by MCU control 0: the DEBUG_COMM_CTRL [USER_DAISY_EN] = 1. COML and COMH are under manual control through DEBUG_COMM_CTRL register 1: COML and COMH are controlled by the device |
| COML_TX_ON | Show the current COML transmitter status 0: Disabled 1: Enabled | Show the current COML transmitter status 0: Disabled 1: Enabled | Show the current COML transmitter status 0: Disabled 1: Enabled | Show the current COML transmitter status 0: Disabled 1: Enabled | Show the current COML transmitter status 0: Disabled 1: Enabled | Show the current COML transmitter status 0: Disabled 1: Enabled | Show the current COML transmitter status 0: Disabled 1: Enabled |
| COML_RX_ON | Show the current COML receiver status 0: Disables 1: Enables | Show the current COML receiver status 0: Disables 1: Enables | Show the current COML receiver status 0: Disables 1: Enables | Show the current COML receiver status 0: Disables 1: Enables | Show the current COML receiver status 0: Disables 1: Enables | Show the current COML receiver status 0: Disables 1: Enables | Show the current COML receiver status 0: Disables 1: Enables |
| COMH_TX_ON | Show the current COMH transmitter status 0: Disabled 1: Enabled | Show the current COMH transmitter status 0: Disabled 1: Enabled | Show the current COMH transmitter status 0: Disabled 1: Enabled | Show the current COMH transmitter status 0: Disabled 1: Enabled | Show the current COMH transmitter status 0: Disabled 1: Enabled | Show the current COMH transmitter status 0: Disabled 1: Enabled | Show the current COMH transmitter status 0: Disabled 1: Enabled |
| COMH_RX_ON | Show the current COMH receiver status 0: Disabled 1: Enabled | Show the current COMH receiver status 0: Disabled 1: Enabled | Show the current COMH receiver status 0: Disabled 1: Enabled | Show the current COMH receiver status 0: Disabled 1: Enabled | Show the current COMH receiver status 0: Disabled 1: Enabled | Show the current COMH receiver status 0: Disabled 1: Enabled | Show the current COMH receiver status 0: Disabled 1: Enabled |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.5.35 Register: DEBUG\_SPI\_PHY

## Address: 0x2301

| B7 | B6 | B5 | B4 | B3 | B2 | B1 | B0 |
| - | - | - | - | - | - | - | - |
| RSVD | FMT_ERR | COMCLR_ERR | TXDATA_UNEXP | RXDATA_UNEXP | TXFIFO_OF | TXFIFO_UF | RXFIFO_OF |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

## FMT\_ERR

When not in Host Read mode (after sending a write cmd frame), indicates malformed cmd is received: 1. first byte of data after nCS falling edge is 0xFF 2. devices receives not multiple of 8bit . 3. In ACTIVE, nCS pulses low without SCLK toggling (send SLP2ACT ping) Comm clear doesn't trigger this fault. This fault doesn't lock down SPI interface.

0: No fault

- 1: Fault

COMCLR\_ERR More than 8 SCLK pulses are received during a comm clear. Once this fault is detected, device ignores the malformed comm clear. This fault doesn't affect SPI\_RDY nor data storing into RX/TX FIFO.

- 0: No fault

1: Fault

TXDATA\_UNEXP This fault occurs when: 1. device receives unexpected data from itself or daisy chain after a Comm clr OR 2. device receives unexpected data from daisy chain(or from bq79600) after a TX FIFO timeout. Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery.

0: No fault

1: Fault

RXDATA\_UNEXP Host sends data other than 0xFF during Device Read mode OR initiates SPI communication when SPI\_RDY = 0 (e.g. While FIFO2 is being filled up, host continues reading FIFO2 right after FIFO1 is read out. SPI\_DRY is low at this point) Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device would sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery.

- 0: No fault

1: Fault

If SPI module receives data (from itself or daisy chain) when current FIFO is full and 2nd FIFO is not empty (host hasn't complete reading the 2nd FIFO). Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery.

0: No fault

1: Fault

In Host Read mode, when both FIFOs are empty and the host continues to send clocks for more read data (send 0xFF through MOSI). SPI Slave sets this fault flag and continues to send 0xFF on MISO when host requests data. Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery. (FIFO 1 is read out, FIFO2 is still buffering, if reading happens, it is RXDATA\_UNEXP fault) Once FIFO is empty, device rejects any 0xFF until nCS going high.

- 0: No fault

1: Fault

RXFIFO\_OF While device is receiving command frame, more data is sent than device can accommodate in RX FIFO. Once this fault is detected, device doesn't store any new data into RX/TX FIFO. Device sends out 0xFF on MISO after current byte finished transmission(FIFO data mask happens at byte boundary). SPI\_RDY held low till Comm Clear detected. Comm Clear needed for recovery. Follow "Flow to send write cmd frame into bq79600" to avoid this fault.

- 0: No fault

1: Fault

## TXFIFO\_OF

## TXFIFO\_UF

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_047.png)

## 7.5.36 Register: DEBUG\_SPI\_FRAME

| Address: 0x2302 - B7 - RSVD | Address: 0x2302 - B6 - RSVD | Address: 0x2302 - B5 - TR_SOF | Address: 0x2302 - B4 - TR_WAIT | Address: 0x2302 - B3 - RC_IERR | Address: 0x2302 - B2 - RC_SOF | Address: 0x2302 - B1 - RC_BYTE_ERR | Address: 0x2302 - B0 - RC_CRC |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| TR_SOF | Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI_RDY is 0 or SPI_RDY = 1 and receiving new data from VIF.) If SPI_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI_RDY is 0 or SPI_RDY = 1 and receiving new data from VIF.) If SPI_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI_RDY is 0 or SPI_RDY = 1 and receiving new data from VIF.) If SPI_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI_RDY is 0 or SPI_RDY = 1 and receiving new data from VIF.) If SPI_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI_RDY is 0 or SPI_RDY = 1 and receiving new data from VIF.) If SPI_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI_RDY is 0 or SPI_RDY = 1 and receiving new data from VIF.) If SPI_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is data in output FIFO (SPI_RDY is 0 or SPI_RDY = 1 and receiving new data from VIF.) If SPI_RDY = 1 and not receiving new data from VIF while receiving COMM CLEAR, it doesn't assert this bit. 0: No fault 1: Fault |
| TR_WAIT | Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI_RDY. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI_RDY. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI_RDY. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI_RDY. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI_RDY. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI_RDY. 0: No fault 1: Fault | Indicates that a SPI COMM CLEAR is received while there is no data in output FIFO regardless of SPI_RDY. 0: No fault 1: Fault |
| RC_IERR | Detects initialization byte error in the received command frame. Example: · reserved command bits in the "INIT byte" is set, · expected to a cmd "INIT byte', but it is configured as response frame instead · extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · reserved command bits in the "INIT byte" is set, · expected to a cmd "INIT byte', but it is configured as response frame instead · extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · reserved command bits in the "INIT byte" is set, · expected to a cmd "INIT byte', but it is configured as response frame instead · extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · reserved command bits in the "INIT byte" is set, · expected to a cmd "INIT byte', but it is configured as response frame instead · extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · reserved command bits in the "INIT byte" is set, · expected to a cmd "INIT byte', but it is configured as response frame instead · extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · reserved command bits in the "INIT byte" is set, · expected to a cmd "INIT byte', but it is configured as response frame instead · extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · reserved command bits in the "INIT byte" is set, · expected to a cmd "INIT byte', but it is configured as response frame instead · extra data is sent other than one cmd frame during one nCS low All bytes that follow are discarded until a Comm Clear is received or a SOF due to a properly formed new command is received (nCS falling, etc). 0: No fault 1: Fault |
| RC_SOF | Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault | Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault | Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault | Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault | Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault | Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault | Detects a start-of-frame (SOF) error. Mostly, this is SPI COMM CLEAR is received on the SPI before the current frame is finished, e.g. partial cmd frame is sent 0: No fault |
| RC_BYTE_ERR | 1: Fault Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault | 1: Fault Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault | 1: Fault Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault | 1: Fault Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault | 1: Fault Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault | 1: Fault Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault | 1: Fault Device receives data from the VIF that needs to go out on SPI, while host send data into device through SPI. (TXDATA_UNEXP should also be set) CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault |
| RC_CRC | 1: Fault Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault | 1: Fault Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault | 1: Fault Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault | 1: Fault Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault | 1: Fault Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault | 1: Fault Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault | 1: Fault Detects CRC error in the received command frame from SPI. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected. 0: No fault |

## 7.5.37 Register: DEBUG\_UART\_FRAME

| Address: 0x2303 - B7 - RSVD | Address: 0x2303 - B6 - RSVD | Address: 0x2303 - B5 - TR_SOF | Address: 0x2303 - B4 - TR_WAIT | Address: 0x2303 - B3 - RC_IERR | Address: 0x2303 - B2 - RC_SOF | Address: 0x2303 - B1 - RC_BYTE_ERR | Address: 0x2303 - B0 - RC_CRC |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| TR_SOF | Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault | Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault | Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault | Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault | Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault | Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault | Indicates that a UART COMM CLEAR is received while the device is still transmitting data to host. 0: No fault 1: Fault |
| TR_WAIT | The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault | The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault | The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault | The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault | The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault | The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault | The device is waiting for its turn to transfer a response out but the action is terminated because: 1. the device receives a UART COMM CLEAR signal, or 2. the device receives a new command This bit is valid when broadcast or stack read command has been issued. 0: No fault 1: Fault |
| RC_IERR | Detects initialization byte error in the received command frame. Example: · a STOP error is detected, · reserved command bits in the "INIT byte" is set, · expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · a STOP error is detected, · reserved command bits in the "INIT byte" is set, · expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · a STOP error is detected, · reserved command bits in the "INIT byte" is set, · expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · a STOP error is detected, · reserved command bits in the "INIT byte" is set, · expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · a STOP error is detected, · reserved command bits in the "INIT byte" is set, · expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · a STOP error is detected, · reserved command bits in the "INIT byte" is set, · expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Detects initialization byte error in the received command frame. Example: · a STOP error is detected, · reserved command bits in the "INIT byte" is set, · expected a "INIT byte', but it is configured as response frame instead (e.g. 1st byte received after COMM CLEAR signal should but a "INIT byte") All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault |
| RC_SOF | Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault | Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault | Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault | Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault | Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault | Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault | Detects a start-of-frame (SOF) error. Mostly, this is UART COMM CLEAR is received on the UART before the current frame is finished. 0: No fault 1: Fault |
| RC_BYTE_ERR | Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault | Other than INIT byte, if STOP error is detected in rest of byte in the frame or TX receives data while RX is using. CRC is not calculated and doesn't forward communication in daisy chain. All bytes that follow are ignored until a communication CLEAR is received. 0: No fault 1: Fault |
| RC_CRC | Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault | Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault | Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault | Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault | Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault | Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault | Detects CRC error in the received command frame from UART. The frame will be considered as discarded frame. Frame CRC is calculated only if no physical level error, IERR, BERR, SOF error detected 0: No fault 1: Fault |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_010.png)

## 7.5.38 Register: DEBUG\_COMH\_PHY

| Address: 0x2304 - B7 | Address: 0x2304 - B6 | Address: 0x2304 - B5 | Address: 0x2304 - B4 | Address: 0x2304 - B3 | Address: 0x2304 - B2 | Address: 0x2304 - B1 | Address: 0x2304 - B0 |
| - | - | - | - | - | - | - | - |
|  | RSVD |  | PERR | BERR_TAG | SYNC2 | SYNC1 | BIT |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

PERR

BERR\_TAG

Pertain to received response frame from stack device only. PERR is a lump bit of all physical errors. Any error bit that is set in this register will also set the [PERR] bit. However, abnormality that isn't classified in the register can also trigger the [PERR] bit (e.g. detecting missing of data or wrong data order.)

- 0: no comm error detected
- 1: detected abnormality of the received comm frame. BERR is asserted to the forwarded communication.

Indicates BERR bit is set in at least one byte in received response frame from stack device

SYNC2

SYNC1

BIT

- 0: received response frame doesn't have BERR
- 1: received response frame has BERR

Timing information extracted from the demodulation of the preamble half-bit and the two full bits of synchronization is outside of the expected window, this bit is set and the byte is not processed.

- 0: No fault
- 1: Fault

If the demodulation of the preamble half-bit and the two full bits of synchronization data have errors and the timing is likely not correct, this bit is set and the byte is not processed.

- 0: No fault
- 1: Fault

The device has detected a data bit, however, the detection samples is not enough to guarantee a strong '1' or '0'.

- 0: No fault
- 1: Fault

## 7.5.39 Register: DEBUG\_COMH\_FRAME

| Address: 0x2305 - B7 | Address: 0x2305 - B6 | Address: 0x2305 - B5 | Address: 0x2305 - B4 | Address: 0x2305 - B3 | Address: 0x2305 - B2 | Address: 0x2305 - B1 | Address: 0x2305 - B0 |
| - | - | - | - | - | - | - | - |
|  | RSVD |  | RR_IERR | RR_SOF | RR_BYTE_ERR | RR_UNEXP | RR_CRC |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

## RR\_IERR

RR\_SOF

Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI).

- 0: No fault
- 1: Fault

Valid when [DIR\_SEL] = 0. Detects a start-of-frame (SOF) error on COMH. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected.

- 0: No fault
- 1: Fault

RR\_BYTE\_ERR Valid when [DIR\_SEL] = 0. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG\_COMH\_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI).

- 0: No fault
- 1: Fault

RR\_UNEXP

If [DIR\_SEL] = 1, but device received response frame from COMH which is an invalid condition and device will set this error bit.

RR\_CRC

- 0: No fault
- 1: Fault

Indicates one or more COMH response frames being discarded due to CRC error.

- 0: No fault
- 1: Fault

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_007.png)

## 7.5.40 Register: DEBUG\_COML\_PHY

| Address: 0x2306 - B7 | Address: 0x2306 - B6 | Address: 0x2306 - B5 | Address: 0x2306 - B4 | Address: 0x2306 - B3 | Address: 0x2306 - B2 | Address: 0x2306 - B1 | Address: 0x2306 - B0 |
| - | - | - | - | - | - | - | - |
|  | RSVD |  | PERR | BERR_TAG | SYNC2 | SYNC1 | BIT |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |

## PERR

BERR\_TAG

Pertain to received response frame from stack device only. PERR is a lump bit of all physical errors. Any error bit that is set in this register will also set the [PERR] bit. However, abnormality that isn't classified in the register can also trigger the [PERR] bit (e.g. detecting missing of data or wrong data order.)

0: no comm error detected

- 1: detected abnormality of the received comm frame. BERR is asserted to the forwarded communication.

Indicates BERR bit is set in at least one byte in received response frame from stack device

SYNC2

SYNC1

BIT

- 0: received response frame doesn't have BERR
- 1: received response frame has BERR

Timing information extracted from the demodulation of the preamble half-bit and the two full bits of synchronization is outside of the expected window, this bit is set and the byte is not processed.

- 0: No fault
- 1: Fault

If the demodulation of the preamble half-bit and the two full bits of synchronization data have errors and the timing is likely not correct, this bit is set and the byte is not processed.

- 0: No fault
- 1: Fault

The device has detected a data bit, however, the detection samples is not enough to guarantee a strong '1' or '0'.

- 0: No fault
- 1: Fault

## 7.5.41 Register: DEBUG\_COML\_FRAME

| Address: 0x2307 - B7 | Address: 0x2307 - B6 | Address: 0x2307 - B5 | Address: 0x2307 - B4 | Address: 0x2307 - B3 | Address: 0x2307 - B2 | Address: 0x2307 - B1 | Address: 0x2307 - B0 |
| - | - | - | - | - | - | - | - |
|  | RSVD |  | RR_IERR | RR_SOF | RR_BYTE_ERR | RR_UNEXP | RR_CRC |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| R | R | R | R | R | R | R | R |
| RR_IERR | Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault | Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault | Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault | Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault | Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault | Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault | Detects initialization byte error in the received response frame. This may due to improper formatting of a byte such as a frame initialization byte is expected, but start-of-frame (SOF) bit is not set, or an invalid frame type is selected. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault 1: Fault |
| RR_SOF | Valid when [DIR_SEL] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault | Valid when [DIR_SEL] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault | Valid when [DIR_SEL] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault | Valid when [DIR_SEL] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault | Valid when [DIR_SEL] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault | Valid when [DIR_SEL] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault | Valid when [DIR_SEL] = 1. Detects a start-of-frame (SOF) error on COML. The SOF bit shall only be set in the initialization frame but the SOF bit is set in the current frame that is not expected. 0: No fault |
| RR_BYTE_ERR | 1: Fault Valid when [DIR_SEL] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG_COML_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault | 1: Fault Valid when [DIR_SEL] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG_COML_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault | 1: Fault Valid when [DIR_SEL] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG_COML_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault | 1: Fault Valid when [DIR_SEL] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG_COML_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault | 1: Fault Valid when [DIR_SEL] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG_COML_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault | 1: Fault Valid when [DIR_SEL] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG_COML_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault | 1: Fault Valid when [DIR_SEL] = 1. Detected any byte errors, other than the error in the initialization byte, in the received response frame. If the byte err is on the last byte of the CRC, it would check CRC in addition to discarding the frame. This error can be triggered by one or more error bit set in the DEBUG_COML_PHY register. All bytes from VIF that follows are ignored until a SOF bit is received (BQ79600 still forwards data from VIF to UART/SPI). 0: No fault |
| RR_UNEXP | Fault If [DIR_SEL] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault | Fault If [DIR_SEL] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault | Fault If [DIR_SEL] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault | Fault If [DIR_SEL] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault | Fault If [DIR_SEL] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault | Fault If [DIR_SEL] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault | Fault If [DIR_SEL] = 0, but device received response frame from COML which is an invalid condition and device will set this error bit. 0: No fault |
| RR_CRC | Fault Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault | Fault Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault | Fault Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault | Fault Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault | Fault Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault | Fault Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault | Fault Indicates one or more COML response frames being discarded due to CRC error. 0: No fault 1: Fault |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_046.png)

## 8 Application and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes. Customers should validate and test their design implementation to confirm system functionality.

## 8.1 Application Information

This section is concerned with the external operation, what external components are required to add to the device to make it usable in a particular design, and how to calculate the values for those external components.

## 8.2 Typical Applications

## 8.2.1 Bridge With Reverse Wakeup in UART

The following application circuit is used when user chooses to use UART interface and any of those features: reverse wakeup, ring architecture, fault/heartbeat tone.

Figure 8-1. Typical Bridge with Reverse Wakeup in UART Applications Circuit

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_048.png)

## 8.2.1.1 Design Requirements

Table 8-1 describes the design parameters.

Table 8-1. Recommended Design Requirement

| PARAMETER | VALUE |
| - | - |
| UART speed | 1Mbps |

## 8.2.1.2 Detailed Design Procedure

## 8.2.1.2.1 MCU Interface (UART, NFAULT)

To select UART interface, connect nCS, nUART/SPI and SCLK pins to GND. UART interface includes RX/TX pins. They are pulled up through a 10-100kΩ resistor to VIO like figure above.

NFAULT pin, if not used, connect to GND. Otherwise, pull it up wtih 100kΩ to VIO.

## 8.2.1.2.2 Daisy Chain Interface

Given that galvanic isolation is expected between BQ79600-Q1 and stack BQ devices, transformer isolation is recommended. Section 8.2.1 shows the interface components values.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_012.png)

Contact TI for transformer recommendations.

## 8.2.1.2.3 INH Connection

INH pin is connected to the power management IC (PMIC) enable pin such that when reverse wakeup is triggered, INH would be pulled towards BAT and enable PMIC. INH pin should always be lower than BAT pin. The 100kΩ connected to INH in Section 8.2.1 is to make sure INH pin potential is defined when INH driver is off.

## 8.2.1.3 Application Performance Plot

Figure 8-2. Command and Response Frame for Read from 2 Stack Devices

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_049.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

迎

Figure 8-3. Zoomed View of Response Frame for 8 Registers Read from Stack Devices

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_050.png)

## 8.2.2 Bridge Without Reverse Wakeup in SPI

The following application circuit is used when user chooses to use SPI interface and none of those features: reverse wakeup, ring architecture, fault/heartbeat tone.

Figure 8-4. Typical Bridge without Reverse Wakeup in SPI Applications Circuit

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_051.png)

## 8.2.2.1 Design Requirements

Table 8-2 describes the design parameters.

Table 8-2. Key Requirements

| PARAMETER | VALUE |
| - | - |
| SPI speed | 2 - 6Mbps |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_012.png)

## 8.2.2.2 Detailed Design Procedure

## 8.2.2.2.1 MCU Interface (SPI, SPI\_RDY, NFAULT)

To select SPI interface, connect MOSI, MISO, SCLK, nCS, nUART/SPI as figure above shows. Connect SPI\_RDY to MCU GPIO port for SPI flow control use, Section 7.3.2.1.2.2.1.

NFAULT pin, if not used, connect to GND. Otherwise, pull it up wtih 100KΩ to VIO.

## 8.2.2.2.2 Daisy Chain Interface

Refer to Section 8.2.1.2.2.

## 8.2.2.3 Application Performance Plot

See Application Performance Plot for application performanace curve.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_016.png)

## 9 Power Supply Recommendations

The BQ79600-Q1 can be powered by either directly from 12-V battery (nominal 9 - 16V) or regulated 5-V supply. The design consideration for both options are described in the table below.

Table 9-1. Supply Design Considerations

|  | 12-V BATTERY (nominal 9 - 16 V) | REGULATED 5-V SUPPLY |
| - | - | - |
| VIO | 3.125 - 5.25V, decouple 0.1-µF capacitor to gnd | 3.125 - 5.25V, decouple 0.1-µF capacitor to gnd |
| BAT | Put RC between supply battery and BAT pin, R = 10Ω, C = 0.1-µF capacitor. Make sure BAT pin sees no less than 5.5V and no larger than 40V. | 4.75 - 5.25V, decouple 0.22-µF capacitor to gnd |
| CVDD | Decouple 0.22-µF capacitor to gnd | shorted to BAT |
| DVDD | Decouple 0.22-µF capacitor to gnd | Decouple 0.22-µF capacitor to gnd |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

## 10 Layout

The layout for this device must be designed carefully. Any design outside these guidelines can affect the communication robustness and EMI performance. Care must be taken in the layout of signals to and from the device to avoid coupling noise onto sensitive inputs. The layout of ground and power connections, as well as communication signals, should also be made carefully.

## 10.1 Layout Guidelines

## 10.1.1 Ground Planes

It is very important to establish a clean grounding scheme to ensure best performance of the device. There is one ground pin (GND) on the device. It is a good practice to use top and bottom PCB layers for signal routing, and use middle layers as ground planes. Even on a PCB layer that is mainly for signal routing, it is good practice to have a small island of ground pour if possible to provide a low-impedance ground, rather than simply a via through the ground trace to an lower ground plane. Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB layers.

There is a strong recommendation to have a minimum of 4 layers in the PCB, with one fully dedicated layer as an unbroken VSS plane (except thermal reliefs). Avoid placing tracks on this layer to maintain the unbroken integrity of the plane structure.

## 10.1.2 Bypass Capacitors for Power Supplies

The bypass capacitors of the following pins must be placed as close to the device pins as possible to ensure proper performance.

- BAT, VIO, CVDD, DVDD

## 10.1.3 UART/SPI communication

The UART/SPI interface (MISO/TX, MOSI/RX, SCLK, nCS, nUART/SPI\_RDY) between MCU and BQ79600-Q1 shall be kept as short and straight as possible for optimized EMC performance.

## 10.1.4 Daisy Chain Communication

It is important to have proper layout on the COMHP/N and COMLP/N circuits in order to have the best robust daisy chain communication.

- Keep differential traces as short as possible and as straight as possible. Minimize turns and avoid any looping on the traces.
- Keep the differential traces on the same layers. Run the trace in parallel with shielding and matching trace impedance.
- Place the isolation components close to the connectors.
- Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB layers.

## 10.2 Layout Example

This section presents the BQ79600-Q1 Evaluation Module (EVM) design as a layout example. Given the EVM doesn't have an MCU, the example of UART/SPI connection layout is not optimized.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_005.png)

Figure 10-1. Top Layer Layout

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_052.png)

Figure 10-2. Signal 1 Layer Layout

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_053.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_004.png)

Figure 10-3. Signal 2 Layer Layout

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_054.png)

Figure 10-4. Bottom Layer Layout

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_055.png)

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_046.png)

[www.ti.com](http://www.ti.com/)

## 11 Device and Documentation Support

## 11.1 Device Support

## 11.2 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

## 11.3 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 11.4 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 11.5 Trademarks

TI E2E™ is a trademark of Texas Instruments.

All other trademarks are the property of their respective owners.

## 11.6 Electrostatic Discharge Caution

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_056.png)

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 11.7 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_017.png)

## 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_057.png)

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| BQ79600PWRQ1 | Active | Production | TSSOP (PW) &#124; 16 | 2000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | BQ79600 |
| BQ79600PWRQ1.A | Active | Production | TSSOP (PW) &#124; 16 | 2000 &#124; LARGE T&R | Yes | NIPDAU | Level-2-260C-1 YEAR | -40 to 125 | BQ79600 |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

- (4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_058.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

24-Jul-2025

## TAPE AND REEL INFORMATION

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_059.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_060.png)

## *All dimensions are nominal

| Device | Package Type | Package Drawing Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - |
| BQ79600PWRQ1 | TSSOP | PW 16 | 2000 | 330.0 | 12.4 | 6.9 | 5.6 | 1.6 | 8.0 | 12.0 | Q1 |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_061.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

24-Jul-2025

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_062.png)

## *All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| BQ79600PWRQ1 | TSSOP | PW | 16 | 2000 | 353.0 | 353.0 | 32.0 |

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_063.png)

SCALE 2.50

## TSSOP - 1.2 mm max height

SMALL OUTLINE PACKAGE

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_064.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. This dimension does not include mold flash, protrusions, or gate burrs. Mold flash, protrusions, or gate burrs shall not exceed 0.15 mm per side.
4. This dimension does not include interlead flash. Interlead flash shall not exceed 0.25 mm per side.
5. Reference JEDEC registration MO-153.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_065.png)

SMALL OUTLINE PACKAGE

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_066.png)

## NOTES: (continued)

6. Publication IPC-7351 may have alternate designs.
7. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_067.png)

## TSSOP - 1.2 mm max height

SMALL OUTLINE PACKAGE

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_068.png)

## NOTES: (continued)

8. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
9. Board assembly site may have different recommendations for stencil design.

![Image](BQ79600-Q1%20Comms%20Bridge%20Datasheet%20%28bq79600-q1%29_files/img_069.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2025, Texas Instruments Incorporated Last updated 10/2025
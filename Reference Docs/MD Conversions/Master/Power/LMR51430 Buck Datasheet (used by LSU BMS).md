<!-- Converted from LMR51430 Buck Datasheet (used by LSU BMS).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_001.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_002.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_003.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_004.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_005.png)

[LMR51430](https://www.ti.com/product/LMR51430)

SLUSEF4A - JUNE 2022 - REVISED NOVEMBER 2022

## LMR51430 SIMPLE SWITCHER ® Power Converter 4.5-V to 36-V, 3-A, Synchronous Buck Converter in a SOT-23 Package

## 1 Features

- [Functional Safety-Capable](https://www.ti.com/technologies/functional-safety/overview.html)
- [Documentation available to aid functional safety system design](http://www.ti.com/lit/SFFS311)
- Configured for rugged industrial applications
- 4.5-V to 36-V input voltage range
- 3-A continuous output current
- 70-ns minimum switching on time
- 500-kHz and 1.1-MHz fixed switching frequency options
- -40°C to 150°C junction temperature range
- 98% maximum duty cycle
- Start-up with prebiased output
- Internal short circuit protection with hiccup mode
- ±1.5% tolerance voltage reference
- Precision enable
- Small solution size and ease of use
- Integrated synchronous rectification
- Internal compensation for ease of use
- SOT-23 package
- Pin-to-pin compatible with the TPS54202 and TPS54302
- PFM and forced PWM (FPWM) options available
- Create a custom design using the LMR51430 with the WEBENCH® Power Designer

## 2 Applications

- [Appliances](https://www.ti.com/applications/industrial/appliances/overview.html)
- [Building automation](https://www.ti.com/applications/industrial/building-automation/overview.html)
- [Motor drives](https://www.ti.com/applications/industrial/motor-drives/overview.html)
- [General purpose wide VIN power supplies](http://www.ti.com/power-management/wide-vin/overview.html)

Simplified Schematic

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_006.png)

## 3 Description

The LMR51430 is a wide-VIN, easy-to-use SIMPLE SWITCHER® power converter synchronous buck converter capable of driving up to 3-A load current. With a wide input range of 4.5 V to 36 V, the device is suitable for a wide range of industrial applications for power conditioning from an unregulated source.

The LMR51430 operates at 500-kHz and 1.1-MHz switching frequency to support use of relatively small inductors for an optimized solution size. The device has a PFM version to realize high efficiency at light load and FPWM version to achieve constant frequency, and small output voltage ripple over the full load range. Soft-start and compensation circuits are implemented internally, which allows the device to be used with minimum external components.

The device has built-in protection features, such as cycle-by-cycle current limit, hiccup mode short-circuit protection, and thermal shutdown in case of excessive power dissipation. The LMR51430 is available in a 6-pin SOT-23 package.

## Package Information

| PART NUMBER | PACKAGE (1) | BODY SIZE (NOM) |
| - | - | - |
| LMR51430 | DBV (SOT-23, 6) | 2.90 mm × 1.60 mm |

- (1) For all available packages, see the orderable addendum at the end of the data sheet.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_007.png)

D003\_SLUSEF4.grf

Efficiency vs Output Current, VOUT = 5 V, 500 kHz

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_008.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_009.png)

## Table of Contents

| 1 Features............................................................................1 |  | 8.3 Feature Description...................................................10 |
| - | - | - |
| 2 Applications.....................................................................1 | 8.4 Device Functional Modes..........................................15 |  |
| 3 Description.......................................................................1 | 9 Application and Implementation..................................16 |  |
| 4 Revision History.............................................................. 2 | 9.1 Application Information............................................. | 16 |
| 5 Device Comparison Table...............................................3 | 9.2 Typical Application.................................................... | 16 |
| 6 Pin Configuration and Functions...................................3 | 9.3 Power Supply Recommendations.............................21 |  |
| 7 Specifications.................................................................. 4 | 9.4 Layout....................................................................... | 21 |
| 7.1 Absolute Maximum Ratings........................................ 4 | 10 Device and Documentation Support..........................24 |  |
| 7.2 ESD Ratings............................................................... 4 | 10.1 Device Support....................................................... | 24 |
| 7.3 Recommended Operating Conditions.........................4 | 10.2 Documentation Support.......................................... | 24 |
| 7.4 Thermal Information ...................................................5 | 10.3 Receiving Notification of Documentation | Updates..24 |
| 7.5 Electrical Characteristics.............................................5 | 10.4 Support Resources................................................. | 24 |
| 7.6 System Characteristics............................................... 6 | 10.5 Trademarks.............................................................24 |  |
| 7.7 Typical Characteristics................................................7 | 10.6 Electrostatic Discharge Caution..............................24 |  |
| 8 Detailed Description........................................................9 | 10.7 Glossary..................................................................25 |  |
| 8.1 Overview.....................................................................9 | 11 Mechanical, Packaging, and Orderable |  |
| 8.2 Functional Block Diagram.........................................10 | Information.................................................................... | 25 |
| 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. | 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. | 4 Revision History NOTE: Page numbers for previous revisions may differ from page numbers in the current version. |
| Changes from Revision * (June 2022) to Revision A (November 2022) · · | Changes from Revision * (June 2022) to Revision A (November 2022) · · | Page |
| · Added "power converter" after the SIMPLE SWITCHER ® trademark................................................................ 1 · | · Added "power converter" after the SIMPLE SWITCHER ® trademark................................................................ 1 · | · Added "power converter" after the SIMPLE SWITCHER ® trademark................................................................ 1 · |
| Switched the "PFM" and "FPWM" curve label in "Efficiency vs Output current, VOUT = 5 V, 500 kHz".............. 1 | Switched the "PFM" and "FPWM" curve label in "Efficiency vs Output current, VOUT = 5 V, 500 kHz".............. 1 | Switched the "PFM" and "FPWM" curve label in "Efficiency vs Output current, VOUT = 5 V, 500 kHz".............. 1 |
| Switched the "PFM" and "FPWM" curve label in Figure7-1, Figure7-2, and Figure 7-3..................................... 7 | Switched the "PFM" and "FPWM" curve label in Figure7-1, Figure7-2, and Figure 7-3..................................... 7 | Switched the "PFM" and "FPWM" curve label in Figure7-1, Figure7-2, and Figure 7-3..................................... 7 |
| Changed the t_hiccup in Overcurrent and Short-Circuit Protection to 135 ms.................................................14 | Changed the t_hiccup in Overcurrent and Short-Circuit Protection to 135 ms.................................................14 | Changed the t_hiccup in Overcurrent and Short-Circuit Protection to 135 ms.................................................14 |
| · Added Table 9-2 ...............................................................................................................................................16 · Changed the quoted equation number in the design example as "Equation 12," "Equation 13," and "Equation 14".....................................................................................................................................................................18 | · Added Table 9-2 ...............................................................................................................................................16 · Changed the quoted equation number in the design example as "Equation 12," "Equation 13," and "Equation 14".....................................................................................................................................................................18 | · Added Table 9-2 ...............................................................................................................................................16 · Changed the quoted equation number in the design example as "Equation 12," "Equation 13," and "Equation 14".....................................................................................................................................................................18 |

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_010.png)

## 5 Device Comparison Table

| Orderable Part Number | Frequency | PFM OR FPWM | Output |
| - | - | - | - |
| LMR51430XDDCR | 500 kHz | PFM | Adjustable |
| LMR51430XFDDCR | 500 kHz | FPWM | Adjustable |
| LMR51430YDDCR | 1.1 MHz | PFM | Adjustable |
| LMR51430YFDDCR | 1.1 MHz | FPWM | Adjustable |

## 6 Pin Configuration and Functions

Figure 6-1. 6-Pin SOT-23 DBV Package (Top View)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_011.png)

Table 6-1. Pin Functions

| Pin - Name | Pin - NO. | Type (1) | Description |
| - | - | - | - |
| GND | 1 | G | Power ground terminals. This pin connects to the source of the low-side FET internally. Connect to system ground, and the ground side of CIN and COUT. The path to CIN must be as short as possible. |
| SW | 2 | P | Switching output of the converter. This pin connects to the source of the high-side FET and drain of the low-side FET. Connect this pin to the power inductor. |
| VIN | 3 | P | Supply input terminal to internal bias LDO and high-side FET. Connect this pin to the input supply and input bypass capacitors, CIN. Input bypass capacitors must be directly connected to this pin and GND. |
| FB | 4 | A | Feedback input to the converter. Connect a resistor divider to set the output voltage. Never short this pin to ground during operation. |
| EN | 5 | A | Precision enable input to the converter. Do not float. High = on, low = off. This pin can be tied to VIN. Precision enable input allows adjustable UVLO by an external resistor divider. If the EN pin is left floating, the device is disabled. |
| CB | 6 | P | Bootstrap capacitor connection for the high-side FET driver. Connect a high quality 100-nF capacitor from this pin to the SW pin. |

(1) A = Analog, P = Power, G = Ground

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_012.png)

## 7 Specifications

## 7.1 Absolute Maximum Ratings

Over operating junction temperature range (unless otherwise noted) (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Input voltage | VIN | -0.3 | 38 | V |
| Input voltage | EN | -0.3 | VIN + 0.3 | V |
| Input voltage | FB | -0.3 | 5.5 | V |
|  | SW, DC | -0.3 | 38 | V |
|  | Output voltage SW, transient < 20 ns | -3.0 | 38 | V |
|  | CB | -0.3 | 43.5 | V |
|  | CB to SW | -0.3 | 5.5 | V |
| Junction temperature, TJ | Junction temperature, TJ | -40 | 150 | °C |
| Storage temperature, Tstg | Storage temperature, Tstg | -65 | 150 | °C |

(1) Operation outside the Absolute Maximum Ratings may cause permanent device damage. Absolute Maximum Ratings do not imply functional operation of the device at these or any other conditions beyond those listed under Recommended Operating Conditions. If used outside the Recommended Operating Conditions but within the Absolute Maximum Ratings, the device may not be fully functional, and this may affect device reliability, functionality, performance, and shorten the device lifetime.

## 7.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| - | - | - | - | - |
| V(ESD) | Electrostatic | Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) | ±1000 | V |
| V(ESD) | discharge | Charged-device model (CDM), per ANSI/ESDA/JEDEC JS-002 (2) | ±500 | V |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.

(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 7.3 Recommended Operating Conditions

Over the recommended operating junction temperature range of -40°C to 150°C (unless otherwise noted) (1)

|  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - |
|  | VIN to GND | 4.5 |  | 36 |  |
| Input voltage | EN (2) | 0 |  | VIN | V |
|  | FB | 0 |  | 4.5 |  |
| Output voltage | VOUT (3) | 0.6 |  | 95% of VIN | V |
| Output current | Iout (4) |  | 3 |  | A |
| TJ | Operating junction temperature (5) | -40 |  | +150 | °C |

(1) Recommended operating conditions indicate conditions for which the device is intended to be functional, but do not ensure specific performance limits. For compliant specifications, see the Electrical Characteristics table.

(2) The voltage on this pin must not exceed the voltage on the VIN pin by more than 0.3 V.

(3) Under no conditions must the output voltage be allowed to fall below 0 V.

(4) Maximum continuous DC current can be derated when operating with high switching frequency, high ambient temperature, or both. See Application and Implementation section for details.

(5) High junction temperatures degrade operating lifetimes. Operating lifetime is de-rated for junction temperatures greater than 150℃.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_013.png)

## 7.4 Thermal Information

The value of RθJA given in this table is only valid for comparison with other packages and cannot be used for design purposes. These values were calculated in accordance with JESD 51-7, and simulated on a 4-layer JEDEC board. They do not represent the performance obtained in an actual application. For example, with a 2-layer PCB, a RθJA = 80℃/W can be achieved. For design information, see Maximum Output Current Versus Ambient Temperature.

| THERMAL METRIC (1) | THERMAL METRIC (1) | DDC (SOT-23-6) 6 PINS | UNIT |
| - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 107.8 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 52.4 | °C/W |
| RθJB | Junction-to-board thermal resistance | 23.3 | °C/W |
| ψJT | Junction-to-top characterization parameter | 9.3 | °C/W |
| ψJB | Junction-to-board characterization parameter | 23.0 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report.

## 7.5 Electrical Characteristics

Limits apply over operating junction temperature (TJ) range of -40°C to +150°C, unless otherwise stated. Minimum and maximum limits (1) are specified through test, design or statistical correlation. Typical values represent the most likely parametric norm at TJ = 25°C, and are provided for reference purposes only. Unless otherwise stated, the following conditions apply: VIN = 4.5 V to 36 V.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| SUPPLY | SUPPLY | SUPPLY | SUPPLY | SUPPLY | SUPPLY | SUPPLY |
| IQ(VIN) | VIN quiescent current (non-switching) (2) | VEN = 3 V, PFM variant only |  | 40 | 65 | µA |
| ISD(VIN) | VIN shutdown supply current | VEN = 0 V |  | 3 | 15 | µA |
| UVLO | UVLO | UVLO | UVLO | UVLO | UVLO | UVLO |
| VINUVLO(R) | VIN UVLO rising threshold | VIN rising |  | 3.89 | 4.5 | V |
| VINUVLO(F) | VIN UVLO falling threshold | VIN falling | 3.35 | 3.58 |  | V |
| VINUVLO(H) | VIN UVLO hysteresis |  |  | 0.3 |  | V |
| ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE | ENABLE |
| VEN(R) | EN voltage rising threshold | EN rising, enable switching | 1.1 | 1.227 | 1.36 | V |
| VEN(F) | EN voltage falling threshold | EN falling, disable switching | 0.95 | 1.08 | 1.22 | V |
| IEN(P2) | EN pin sourcing current post EN rising threshold | VEN = 3 V |  | 10 | 200 | nA |
| REFERENCE VOLTAGE | REFERENCE VOLTAGE | REFERENCE VOLTAGE | REFERENCE VOLTAGE | REFERENCE VOLTAGE | REFERENCE VOLTAGE | REFERENCE VOLTAGE |
| Vfb | Reference voltage |  | 0.591 | 0.6 | 0.609 | V |
| IFB(LKG) | FB input leakage current | VFB = 1.2 V |  | 0.8 | 50 | nA |
| SWITCHING FREQUENCY | SWITCHING FREQUENCY | SWITCHING FREQUENCY | SWITCHING FREQUENCY | SWITCHING FREQUENCY | SWITCHING FREQUENCY | SWITCHING FREQUENCY |
| fSW1(CCM) | Switching frequency, CCM operation | 500-kHz trim option | 450 | 500 | 560 | kHz |
| fSW2(CCM) | Switching frequency, CCM operation | 1.1-MHz trim option | 0.95 | 1.1 | 1.25 | MHz |
| STARTUP | STARTUP | STARTUP | STARTUP | STARTUP | STARTUP | STARTUP |
| tSS | Internal fixed soft-start time |  | 3.2 | 4.0 | 5.4 | ms |
| POWER STAGE | POWER STAGE | POWER STAGE | POWER STAGE | POWER STAGE | POWER STAGE | POWER STAGE |
| RDSON(HS) | High-side MOSFET on-resistance | TJ = 25℃ |  | 0.12 |  | Ω |
| RDSON(LS) | Low-side MOSFET on-resistance | TJ = 25℃ |  | 0.07 |  | Ω |
| tON(min) | Minimum ON pulse width | VIN = 12 V, IOUT = 3 A |  | 70 |  | ns |
| tON(max) | Maximum ON pulse width | VIN = 12 V, IOUT = 3 A |  | 6.76 |  | µs |
| tOFF(min) | Minimum OFF pulse width | VIN = 4.5 V |  | 150 |  | ns |
| OVERCURRENT PROTECTION | OVERCURRENT PROTECTION | OVERCURRENT PROTECTION | OVERCURRENT PROTECTION | OVERCURRENT PROTECTION | OVERCURRENT PROTECTION | OVERCURRENT PROTECTION |
| IHS_PK(OC) | High-side peak current limit (3) | LM51430 | 3.67 | 4.76 | 6.68 | A |

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_014.png)

## 7.5 Electrical Characteristics (continued)

Limits apply over operating junction temperature (TJ) range of -40°C to +150°C, unless otherwise stated. Minimum and maximum limits (1) are specified through test, design or statistical correlation. Typical values represent the most likely parametric norm at TJ = 25°C, and are provided for reference purposes only. Unless otherwise stated, the following conditions apply: VIN = 4.5 V to 36 V.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| ILS_V(OC) | Low-side valley current limit (3) | LM51430 | 2.75 | 3.5 | 4.2 | A |
| ILS(NOC) | Low-side negative current limit | LM51430 FPWM Only |  | -1.6 |  | A |
| IZC | Zero-cross detection current threshold |  |  | 0.02 |  | A |
| THERMAL SHUTDOWN | THERMAL SHUTDOWN |  |  |  |  |  |
| TJ(SD) | Thermal shutdown threshold (4) | Temperature rising |  | 163 |  | °C |
| TJ(HYS) | Thermal shutdown hysteresis (4) |  |  | 22 |  | °C |

(1) MIN and MAX limits are 100% production tested at 25℃. Limits over the operating temperature range verified through correlation using Statistical Quality Control (SQC) methods. Limits are used to calculate Average Outgoing Quality Level (AOQL).

(2) This is the current used by the device open loop. It does not represent the total input current of the system when in regulation.

(3) The current limit values in this table are tested, open loop, in production. They may differ from those found in a closed loop application

(4) Specified by design

## 7.6 System Characteristics

The following specifications apply to a typical application circuit with nominal component values. Specifications in the typical (TYP) column apply to TJ = 25°C only. Specifications in the minimum (MIN) and maximum (MAX) columns apply to the case of typical components over the temperature range of TJ = -40°C to 150°C. These specifications are not ensured by production testing.

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| VIN | Operating input voltage range |  | 4.5 |  | 36 | V |
| VOUT | Adjustable output voltage regulation (1) | PFM operation | -1.5% |  | 2.5% |  |
| ISUPPLY | VIN quiescent current (non-switching) | VIN =12 V, VOUT = 3.3 V, IOUT = 0 A, RFBT = 1 MΩ, PFM variant |  | 40 |  | µA |
| DMAX | Maximum switch duty cycle (2) |  |  | 98% |  |  |
| VHC | FB pin voltage required to trip short- circuit hiccup mode |  |  | 0.24 |  | V |
| tD | Switch voltage dead-time |  |  | 6.5 |  | ns |
| TSD | Thermal shutdown temperature | Shutdown temperature |  | 163 |  | °C |
| TSD | Thermal shutdown temperature | Recovery temperature |  | 141 |  | °C |

(1) Deviation in VOUT from nominal output voltage value at VIN = 24 V, IOUT = 0 A to full load

(2) In dropout, the switching frequency drops to increase the effective duty cycle. The lowest frequency is clamped at approximately: fMIN = 1 / (tON-MAX + tOFF-MIN). DMAX = tON-MAX / (tON-MAX + tOFF-MIN).

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_015.png)

## 7.7 Typical Characteristics

VIN = 12 V, fSW = 500 kHz ,TA = 25°C, unless otherwise specified.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_016.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_017.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_018.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_019.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_020.png)

[www.ti.com](https://www.ti.com/)

## 8 Detailed Description

## 8.1 Overview

The LMR51430 is an easy-to-use synchronous step-down DC-DC converter operating from a 4.5-V to 36-V supply voltage. The device is capable of delivering up to 3-A DC load current in a very small solution size. The family has multiple versions applicable to various applications. See Section 5 for detailed information.

The LMR51430 employs fixed-frequency peak-current mode control. The PFM version enters PFM mode at light load to achieve high efficiency. A FPWM version is provided to achieve low output voltage ripple, tight output voltage regulation, and constant switching frequency at light load. The device is internally compensated, which reduces design time and requires few external components.

Additional features such as precision enable and internal soft start provide a flexible and easy-to-use solution for a wide range of applications. Protection features include the following:

- Thermal shutdown
- VIN undervoltage lockout
- Cycle-by-cycle current limit
- Hiccup mode short-circuit protection

This family of devices requires very few external components and has a pinout designed for simple, optimal PCB layout.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_012.png)

## 8.2 Functional Block Diagram

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_021.png)

## 8.3 Feature Description

## 8.3.1 Fixed Frequency Peak Current Mode Control

The following operating description of the LMR51430 refers to Section 8.2 and to the waveforms in Figure 8-1. The LMR51430 is a step-down synchronous buck converter with integrated high-side (HS) and low-side (LS) switches (synchronous rectifier). The LMR51430 supplies a regulated output voltage by turning on the high-side and low-side NMOS switches with controlled duty cycle. During the high-side switch on time, the SW pin voltage swings up to approximately VIN, and the inductor current, iL, increases with a linear slope of (VIN - VOUT) / L. When the high-side switch is turned off by the control logic, the low-side switch is turned on after an anti-shootthrough dead time. Inductor current discharges through the low-side switch with a slope of -VOUT / L. The control parameter of a buck converter is defined as:

<!-- formula-not-decoded -->

## where

- tON is the high-side switch on time.
- tSW is the switching period.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_015.png)

The converter control loop maintains a constant output voltage by adjusting the duty cycle D. In an ideal buck converter where losses are ignored, and D is proportional to the output voltage and inversely proportional to the input voltage:

Figure 8-1. SW Node and Inductor Current Waveforms in Continuous Conduction Mode (CCM)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_022.png)

The LMR51430 employs fixed-frequency peak-current mode control. A voltage feedback loop is used to get accurate DC voltage regulation by adjusting the peak-current command based on voltage offset. The peak inductor current is sensed from the high-side switch and compared to the peak current threshold to control the on time of the high-side switch. The voltage feedback loop is internally compensated, which allows for fewer external components, making designing easy and providing stable operation when using a variety of output capacitors. The converter operates with fixed switching frequency at normal load conditions. During light-load condition, the LMR51430 operates in PFM mode to maintain high efficiency (PFM version) or in FPWM mode for low output voltage ripple, tight output voltage regulation, and constant switching frequency (FPWM version).

## 8.3.2 Adjustable Output Voltage

A precision 0.6-V reference voltage (VREF) is used to maintain a tightly regulated output voltage over the entire operating temperature range. The output voltage is set by a resistor divider from VOUT to the FB pin. TI recommends using 1% tolerance resistors with a low temperature coefficient for the FB divider. Select the bottom-side resistor, RFBB, for the desired divider current and use Equation 3 to calculate the top-side resistor, RFBT. The recommend range for RFBT is 10 kΩ to 100 kΩ. A lower RFBT value can be used if pre-loading is desired to reduce VOUT offset in PFM operation. Lower RFBT reduces efficiency at very light load. Less static current goes through a larger RFBT and can be more desirable when light-load efficiency is critical. However, TI does not recommend RFBT larger than 1 MΩ because it makes the feedback path more susceptible to noise. Larger RFBT values require a more carefully designed feedback path trace from the feedback resistors to the feedback pin of the device. The tolerance and temperature variation of the resistor divider network affect the output voltage regulation.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_023.png)

Figure 8-2. Output Voltage Setting

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_024.png)

<!-- formula-not-decoded -->

## 8.3.3 Enable

The voltage on the EN pin controls the ON and OFF operation of the LMR51430. A voltage of less than 0.95 V shuts down the device, while a voltage of greater than 1.36 V is required to start the converter. The EN pin is an input and cannot be left open or floating. The simplest way to enable the operation of the LMR51430 is to connect EN to VIN. This allows self-start-up of the LMR51430 when VIN is within the operating range.

Many applications benefit from the employment of an enable divider RENT and RENB (Figure 8-3) to establish a precision system UVLO level for the converter. System UVLO can be used for supplies operating from utility power as well as battery power. System UVLO can also be used for sequencing, ensuring reliable operation, or supplying protection, such as a battery discharge level. An external logic signal can also be used to drive EN input for system sequencing and protection.

## Note

The EN pin voltage must not to be greater than VIN + 0.3 V. Do not apply EN voltage when VIN is 0 V.

Figure 8-3. System UVLO by an Enable Divider

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_025.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_026.png)

## 8.3.4 Minimum On Time, Minimum Off Time, and Frequency Foldback

Minimum on time (tON\_MIN) is the shortest duration of time that the high-side switch can be turned on. tON\_MIN is typically 70 ns for the LMR51430. Minimum off time (tOFF\_MIN) is the shortest duration of time that the high-side switch can be off. tOFF\_MIN is typically 150 ns. In CCM operation, tON\_MIN and tOFF\_MIN limit the voltage conversion range without switching frequency foldback.

The minimum duty cycle without frequency foldback allowed is:

<!-- formula-not-decoded -->

The maximum duty cycle without frequency foldback allowed is:

<!-- formula-not-decoded -->

Given a required output voltage, the maximum VIN without frequency foldback can be found by:

<!-- formula-not-decoded -->

The minimum VIN without frequency foldback can be calculated by:

<!-- formula-not-decoded -->

In the LMR51430, a frequency foldback scheme is employed after tON\_MIN or tOFF\_MIN is triggered, which can extend the maximum duty cycle or lower the minimum duty cycle.

The on time decreases while VIN voltage increases. After the on time decreases to tON\_MIN, the switching frequency starts to decrease while VIN continues to increase, which lowers the duty cycle further to keep VOUT in regulation according to Equation 4.

The frequency foldback scheme also works after larger duty cycle is needed under low VIN condition. The frequency decreases after the device reaches tOFF\_MIN, which extends the maximum duty cycle according to Equation 5. In such condition, the frequency can be as low as approximately 133 kHz. A wide range of frequency foldback allows for the LMR51430 output voltage to stay in regulation with a much lower supply voltage VIN, which leads to a lower effective dropout.

With frequency foldback while maintaining a regulated output voltage, VIN\_MAX is raised, and VIN\_MIN is lowered by decreased fSW.

Figure 8-4. Frequency Foldback at tON\_MIN

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_027.png)

Figure 8-5. Frequency Foldback at tON\_MIN

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_028.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_014.png)

## 8.3.5 Bootstrap Voltage

The LMR51430 provides an integrated bootstrap voltage converter. A small capacitor between the CB and SW pins provides the gate drive voltage for the high-side MOSFET. The bootstrap capacitor is refreshed when the high-side MOSFET is off and the low-side switch is on. The recommended value of the bootstrap capacitor is 0.1 µF. TI recommends a ceramic capacitor with an X7R or X5R grade dielectric with a voltage rating of 16 V or higher for stable performance over temperature and voltage.

## 8.3.6 Overcurrent and Short-Circuit Protection

The LMR51430 incorporates both peak and valley inductor current limit to provide protection to the device from overloads and short circuits and limit the maximum output current. Valley current limit prevents inductor current runaway during short circuits on the output, while both peak and valley limits work together to limit the maximum output current of the converter. Cycle-by-cycle current limit is used for overloads, while hiccup mode is used for sustained short circuits.

High-side MOSFET overcurrent protection is implemented by the nature of the peak current mode control. The high-side switch current is sensed when the high-side is turned on after a set blanking time. The high-side switch current is compared to the output of the Error Amplifier (EA) minus slope compensation every switching cycle. See Functional Block Diagram for more details. The peak current of high-side switch is limited by a clamped maximum peak current threshold, Isc (see the Electrical Characteristics), which is constant.

The current going through the low-side MOSFET is also sensed and monitored. When the low-side switch turns on, the inductor current begins to ramp down. The low-side switch is not turned OFF at the end of a switching cycle if its current is above the low-side current limit, ILS\_LIMIT (see the Electrical Characteristics). The low-side switch is kept ON so that inductor current keeps ramping down until the inductor current ramps below ILS\_LIMIT. Then, the low-side switch is turned OFF and the high-side switch is turned on after a dead-time. After ILS\_LIMIT is achieved, peak and valley current limit controls the max current deliver and it can be calculated using Equation 8.

<!-- formula-not-decoded -->

If the feedback voltage is lower than 40% of VREF, the current of the low-side switch triggers ILS\_LIMIT for 256 consecutive cycles and hiccup current protection mode is activated. In hiccup mode, the converter shuts down and keeps off for a period of hiccup, tHICCUP (135-ms typical), before the LMR51430 tries to start again. If an overcurrent or short-circuit fault condition still exist, hiccup repeats until the fault condition is removed. Hiccup mode reduces power dissipation under severe overcurrent conditions, preventing overheating and potential damage to the device.

For FPWM version, the inductor current is allowed to go negative. When this current exceeds the low-side negative current limit, ILS\_NEG, the low-side switch is turned off and high-side switch is turned on immediately. This is used to protect the low-side switch from excessive negative current.

## 8.3.7 Soft Start

The integrated soft-start circuit prevents input inrush current impacting the LMR51430 and the input power supply. Soft start is achieved by slowly ramping up the internal reference voltage when the device is first enabled or powered up. The typical soft-start time is 4.0 ms.

The LMR51430 also employs overcurrent protection blanking time, tOCP\_BLK (33 ms typical), at the beginning of power up. Without this feature, in applications with a large amount of output capacitors and high VOUT, the inrush current is large enough to trigger the current-limit protection, which can cause a false start as the device enters into hiccup mode. This action results in a continuous recycling of soft start without raising up to the programmed output voltage. The LMR51430 is able to charge the output capacitor to the programmed VOUT by controlling the average inductor current during the start-up sequence in the blanking time, tOCP\_BLK.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_029.png)

[www.ti.com](https://www.ti.com/)

## 8.3.8 Thermal Shutdown

The LMR51430 provides an internal thermal shutdown to protect the device when the junction temperature exceeds 163°C. Both high-side and low-side FETs stop switching in thermal shutdown. After the die temperature falls below 141°C, the device reinitiates the power-up sequence controlled by the internal soft-start circuitry.

## 8.4 Device Functional Modes

## 8.4.1 Shutdown Mode

The EN pin provides electrical ON and OFF control for the LMR51430. When VEN is below 0.95 V, the device is in shutdown mode. The LMR51430 also employs VIN undervoltage lockout protection (UVLO). If VIN voltage is below its UVLO threshold of 3.58 V, the converter is turned off.

## 8.4.2 Active Mode

The LMR51430 is in active mode when both VEN and VIN are above their respective operating threshold. The simplest way to enable the LMR51430 is to connect the EN pin to VIN pin. This allows self-start-up when the input voltage is in the operating range of 4.5 V to 36 V. See Section 8.3.3 for details on setting these operating levels.

In active mode, depending on the load current, the LMR51430 is in one of four modes:

- Continuous conduction mode (CCM) with fixed switching frequency when load current is greater than half of the peak-to-peak inductor current ripple (for both PFM and FPWM versions)
- Discontinuous conduction mode (DCM) with fixed switching frequency when load current is less than half of the peak-to-peak inductor current ripple(only for PFM version)
- Pulse frequency modulation mode (PFM) when switching frequency is decreased at very light load (only for PFM version)
- Forced pulse width modulation mode (FPWM) with fixed switching frequency even at light load (only for FPWM version)

## 8.4.3 CCM Mode

Continuous conduction mode (CCM) operation is employed in the LMR51430 when the load current is greater than half of the peak-to-peak inductor current. In CCM operation, the frequency of operation is fixed, output voltage ripple is at a minimum in this mode and the maximum output current of 3 A can be supplied by the LMR51430.

## 8.4.4 Light-Load Operation (PFM Version)

For PFM version, when the load current is lower than half of the peak-to-peak inductor current in CCM, the LMR51430 operates in discontinuous conduction mode (DCM), also known as diode emulation mode (DEM). In DCM operation, the low-side switch is turned off when the inductor current drops to IZC (20 mA typical) to improve efficiency. Both switching losses and conduction losses are reduced in DCM, compared to forced PWM operation at light load.

During light-load operation, pulse frequency modulation (PFM) mode is activated to maintain high efficiency operation. When either the minimum high-side switch on time, tON\_MIN, or the minimum peak inductor current, IPEAK\_MIN (0.48 A typical), is reached, the switching frequency decreases to maintain regulation. In PFM mode, switching frequency is decreased by the control loop to maintain output voltage regulation when load current reduces. Switching loss is further reduced in PFM operation due to a significant drop in effective switching frequency.

## 8.4.5 Light-Load Operation (FPWM Version)

For FPWM version, the LMR51430 is locked in PWM mode at full load range. This operation is maintained, even in no-load condition, by allowing the inductor current to reverse its normal direction. This mode trades off reduced light load efficiency for low output voltage ripple, tight output voltage regulation, and constant switching frequency.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_030.png)

## 9 Application and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 9.1 Application Information

The LMR51430 is a step-down DC-to-DC converter. The device is typically used to convert a higher input voltage to a lower output DC voltage with a maximum output current of 3 A. The following design procedure can be used to select components for the LMR51430. Alternately, the WEBENCH ® software can be used to generate complete designs. When generating a design, the WEBENCH software uses iterative design procedure and accesses comprehensive databases of components. Go to ti.com for more details.

## 9.2 Typical Application

The LMR51430 only requires a few external components to convert from a wide voltage range supply to a fixed output voltage. Figure 9-1 shows a basic schematic.

Figure 9-1. Application Circuit

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_031.png)

The external components have to fulfill the needs of the application and the stability criteria of the control loop of the device. Table 9-1 can be used to simplify the output filter component selection.

Table 9-1. L and COUT Typical Values

| fSW (kHz) | VOUT (V) | L (µH) | COUT (µF) (1) | RFBT (kΩ) | RFBB (kΩ) |
| - | - | - | - | - | - |
| 500 | 3.3 | 5.6 | 2 × 22 µF / 25 V | 100 | 22.1 |
| 500 | 5 | 6.8 | 2 × 22 µF / 25 V | 100 | 13.7 |
| 500 | 12 | 12 | 3 × 22 µF / 25 V | 100 | 5.23 |

## Table 9-2. L and COUT Typical Values

| fSW (kHz) | VOUT (V) | L (µH) | COUT (µF) (1) | RFBT (kΩ) | RFBB (kΩ) |
| - | - | - | - | - | - |
| 1100 | 3.3 | 2.2 | 2 × 10 µF / 25 V | 100 | 22.1 |
| 1100 | 5 | 3.3 | 2 × 10 µF / 25 V | 100 | 13.7 |
| 1100 | 12 | 6.8 | 3 × 10 µF / 25 V | 100 | 5.23 |

- (1) A ceramic capacitor is used in this table.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_026.png)

## 9.2.1 Design Requirements

The detailed design procedure is described based on a design example. For this design example, use the parameters listed in Table 9-3 as the input parameters.

Table 9-3. Design Example Parameters

| Parameter | Value |
| - | - |
| Input voltage, VIN | 12 V typical, range from 6 V to 36 V |
| Output voltage, VOUT | 5 V ±3% |
| Maximum output current, IOUT_MAX | 3 A |
| Output overshoot and undershoot 0.5 A to 2 A | 5% |
| Output voltage ripple | 0.5% |
| Operating frequency | 500 kHz |

## 9.2.2 Detailed Design Procedure

## 9.2.2.1 Custom Design With WEBENCH® Tools

Click here to create a custom design using the LMR51430 device with the WEBENCH® Power Designer.

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

## 9.2.2.2 Output Voltage Set-Point

The output voltage of the LMR51430 device is externally adjustable using a resistor divider network. The divider network is comprised of a top feedback resistor RFBT and bottom feedback resistor RFBB. Equation 9 is used to determine the output voltage of the converter:

<!-- formula-not-decoded -->

Choose the value of RFBB to be 13.7 kΩ. With the desired output voltage set to 5 V and the VREF = 0.6 V, the RFBT value can then be calculated using Equation 9. The formula yields a value 100.4 kΩ. A standard value of 100 kΩ is selected.

## 9.2.2.3 Switching Frequency

The higher switching frequency allows for lower-value inductors and smaller output capacitors, which result in a smaller solution size and lower component cost. However, higher switching frequency brings more switching loss, making the solution less efficient and produce more heat. The switching frequency is also limited by the minimum on time of the following as mentioned in Section 8.3.4:

- Integrated power switch
- Input voltage
- Output voltage
- Frequency shift limitation

For this example, a switching frequency of 500 kHz is selected.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_032.png)

## 9.2.2.4 Inductor Selection

The most critical parameters for the inductor are the inductance, saturation current, and the RMS current. The inductance is based on the desired peak-to-peak ripple current, ΔiL. Because the ripple current increases with the input voltage, the maximum input voltage is always used to calculate the minimum inductance, LMIN. Use Equation 11 to calculate the minimum value of the output inductor. KIND is a coefficient that represents the amount of inductor ripple current relative to the maximum output current of the device. A reasonable value of KIND must be 20% to 60% of maximum IOUT supported by the converter. During an instantaneous overcurrent operation event, the RMS and peak inductor current can be high. The inductor saturation current must be higher than peak current limit level.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

In general, choose lower inductance in switching power supplies because it usually corresponds to faster transient response, smaller DCR, and reduced size for more compact designs. Too low of an inductance can generate too large of an inductor current ripple such that overcurrent protection at the full load can be falsely triggered and generates more inductor core loss because the current ripple is larger. Larger inductor current ripple also implies larger output voltage ripple with the same output capacitors. With peak current mode control, ensure there is an adequate amount of inductor ripple current. A larger inductor ripple current improves the comparator signal-to-noise ratio.

For this design example, choose KIND = 0.3. The minimum inductor value is calculated to be 6.48 µH. Choose the nearest standard 6.8-µH ferrite inductor with a capability of 4-A RMS current and 5-A saturation current.

## 9.2.2.5 Output Capacitor Selection

The device is designed to be used with a wide variety of LC filters. Minimize the output capacitance to keep cost and size down. The output capacitor or capacitors, COUT, must be chosen with care because it directly affects the steady state output voltage ripple, loop stability, and output voltage overshoot and undershoot during load current transient. The output voltage ripple is essentially composed of two parts. One part is caused by the inductor ripple current flowing through the Equivalent Series Resistance (ESR) of the output capacitors:

<!-- formula-not-decoded -->

The other part is caused by the inductor current ripple charging and discharging the output capacitors:

<!-- formula-not-decoded -->

The two components of the voltage ripple are not in-phase, therefore, the actual peak-to-peak ripple is less than the sum of the two peaks.

Output capacitance is usually limited by transient performance specifications if the system requires tight voltage regulation with presence of large current steps and fast slew rates. When a large load step occurs, output capacitors provide the required charge before the inductor current can slew to an appropriate level. The control loop of the converter usually requires eight or more clock cycles to regulate the inductor current equal to the new load level during this time. The output capacitance must be large enough to supply the current difference for eight clock cycles to maintain the output voltage within the specified range. Equation 14 shows the minimum output capacitance needed for a specified VOUT overshoot and undershoot.

<!-- formula-not-decoded -->

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_033.png)

## where

- KIND is the ripple ratio of the inductor current (ΔiL / IOUT).
- IOL is the low level output current during load transient.
- IOH is the high level output current during load transient.
- VOUT\_SHOOT is the target output voltage overshoot or undershoot.

For this design example, the target output ripple is 30 mV. Assuming ΔVOUT\_ESR = ΔVOUT\_C = 30 mV, choose KIND = 0.3. Equation 12 yields ESR no larger than 75 mΩ and Equation 13 yields COUT no smaller than 14 µF. For the target overshoot and undershoot limitation of this design, ΔVOUT\_SHOOT = 5% × VOUT = 250 mV. The COUT can be calculated to be no less than 48 µF by Equation 14. In summary, the most stringent criterion for the output capacitor is 48 µF. For this design, two 22-µF, 25-V, X7R ceramic capacitors with 5-mΩ ESR are used.

## 9.2.2.6 Input Capacitor Selection

The LMR51430 device requires a high frequency input decoupling capacitor or capacitor. The typical recommended value for the high frequency decoupling capacitor is 4.7 µF or higher. TI recommends a highquality ceramic type X5R or X7R with a sufficient voltage rating. The voltage rating must be greater than the maximum input voltage. To compensate the derating of ceramic capacitors, TI recommends a voltage rating of twice the maximum input voltage. For this design, two 4.7-µF, X7R dielectric capacitor rated for 50 V are used for the input decoupling capacitor. The equivalent series resistance (ESR) is approximately 10 mΩ and the current rating is 1 A. Include a capacitor with a value of 0.1 µF for high-frequency filtering and place it as close as possible to the device pins.

## 9.2.2.7 Bootstrap Capacitor

Every LMR51430 design requires a bootstrap capacitor, CBOOT. The recommended bootstrap capacitor is 0.1 µF and rated at 16 V or higher. The bootstrap capacitor is located between the SW pin and the CB pin. The bootstrap capacitor must be a high-quality ceramic type with X7R or X5R grade dielectric for temperature stability.

## 9.2.2.8 Undervoltage Lockout Set-Point

The system undervoltage lockout (UVLO) is adjusted using the external voltage divider network of RENT and RENB. The UVLO has two thresholds, one for power up when the input voltage is rising and one for power down or brownouts when the input voltage is falling. Equation 15 can be used to determine the VIN UVLO level.

<!-- formula-not-decoded -->

The EN rising threshold (VENH) for the LMR51430 is set to be 1.23 V (typical). Choose a value of 200 kΩ for RENB to minimize input current from the supply. If the desired VIN UVLO level is at 6.0 V, then the value of RENT can be calculated using Equation 16:

<!-- formula-not-decoded -->

The above equation yields a value of 775.6 kΩ, a standard value of 768 kΩ is selected. The resulting falling UVLO threshold, equals 5.3 V, can be calculated by Equation 17 where EN hysteresis voltage, VEN\_HYS, is 0.13 V (typical).

<!-- formula-not-decoded -->

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_032.png)

## 9.2.3 Application Curves

Unless otherwise specified the following conditions apply: VIN = 12 V, VOUT = 5 V, fSW = 500 kHz, L = 6.8 µH, COUT = 44 µF, T = 25°C.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_034.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_015.png)

[www.ti.com](https://www.ti.com/)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_035.png)

## 9.3 Power Supply Recommendations

The LMR51430 is designed to operate from an input voltage supply range between 4.5 V and 36 V. This input supply must be well-regulated and able to withstand maximum input current and maintain a stable voltage. The resistance of the input supply rail must be low enough that an input current transient does not cause a high enough drop at the LMR51430 supply voltage that can cause a false UVLO fault triggering and system reset. If the input supply is located more than a few inches from the LMR51430 additional bulk capacitance can be required in addition to the ceramic bypass capacitors. The amount of bulk capacitance is not critical, but a 10-µF or 22-µF electrolytic capacitor is a typical choice.

## 9.4 Layout

## 9.4.1 Layout Guidelines

Layout is a critical portion of good power supply design. The following guidelines help users design a PCB with the best power conversion performance, thermal performance, and minimized generation of unwanted EMI.

- The input bypass capacitor CIN must be placed as close as possible to the VIN and GND pins. Grounding for both the input and output capacitors must consist of localized top-side planes that connect to the GND pin.
- Minimize trace length to the FB pin net. Both feedback resistors, RFBT and RFBB, must be located close to the FB pin. If VOUT accuracy at the load is important, make sure VOUT sense is made at the load. Route VOUT sense path away from noisy nodes and preferably through a layer on the other side of a shielded layer.
- Use the ground plane in one of the middle layers as noise shielding and heat dissipation path if possible.
- Make VIN, VOUT, and ground bus connections as wide as possible, which reduces any voltage drops on the input or output paths of the converter and maximizes efficiency.
- Provide adequate device heat-sinking. GND, VIN, and SW pins provide the main heat dissipation path. Make the GND, VIN, and SW plane area as large as possible. Use an array of heat-sinking vias to connect the top side ground plane to the ground plane on the bottom PCB layer. If the PCB has multiple copper layers, these thermal vias can also be connected to inner layer heat-spreading ground planes. Ensure enough copper area is used for heat-sinking to keep the junction temperature below 125°C.

## 9.4.1.1 Compact Layout for EMI Reduction

Radiated EMI is generated by the high di/dt components in pulsing currents in switching converters. The larger area covered by the path of a pulsing current, the more EMI is generated. High frequency ceramic bypass capacitors at the input side provide a primary path for the high di/dt components of the pulsing current. Placing a ceramic bypass capacitor or capacitors as close as possible to the VIN and GND pins is the key to EMI reduction.

The SW pin connected to the inductor must be as short as possible, and just wide enough to carry the load current without excessive heating. Short, thick traces or copper pours (shapes) must be used for high current conduction path to minimize parasitic resistance. The output capacitors must be placed close to the VOUT end of the inductor and closely grounded to the GND pin.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_036.png)

## 9.4.1.2 Feedback Resistors

To reduce noise sensitivity of the output voltage feedback path, make sure to place the resistor divider close to the FB pin, rather than close to the load. The FB pin is the input to the error amplifier, so it is a high impedance node and very sensitive to noise. Placing the resistor divider closer to the FB pin reduces the trace length of FB signal and reduces noise coupling. The output node is a low impedance node, so the trace from VOUT to the resistor divider can be long if short path is not available.

If voltage accuracy at the load is important, make sure voltage sense is made at the load. Doing so corrects for voltage drops along the traces and provides the best output accuracy. The voltage sense trace from the load to the feedback resistor divider must be routed away from the SW node path and the inductor to avoid contaminating the feedback signal with switch noise, while also minimizing the trace length. This effect is most important when high value resistors are used to set the output voltage. TI recommends to route the voltage sense trace and place the resistor divider on a different layer than the inductor and SW node path, such that there is a ground plane in between the feedback trace and inductor and SW node polygon, which provides further shielding for the voltage feedback path from EMI noises.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_015.png)

## 9.4.2 Layout Example

Figure 9-10. Layout

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_037.png)

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_038.png)

## 10 Device and Documentation Support

## 10.1 Device Support

## 10.1.1 Third-Party Products Disclaimer

TI'S PUBLICATION OF INFORMATION REGARDING THIRD-PARTY PRODUCTS OR SERVICES DOES NOT CONSTITUTE AN ENDORSEMENT REGARDING THE SUITABILITY OF SUCH PRODUCTS OR SERVICES OR A WARRANTY, REPRESENTATION OR ENDORSEMENT OF SUCH PRODUCTS OR SERVICES, EITHER ALONE OR IN COMBINATION WITH ANY TI PRODUCT OR SERVICE.

## 10.1.2 Development Support

## 10.1.2.1 Custom Design With WEBENCH® Tools

Click here to create a custom design using the LMR51430 device with the WEBENCH® Power Designer.

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

## 10.2 Documentation Support

## 10.2.1 Related Documentation

For related documentation see the following:

[Texas Instruments, AN-1149 Layout Guidelines for Switching Power Supplies](https://www.ti.com/lit/pdf/SNVA021)

## 10.3 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 10.4 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 10.5 Trademarks

TI E2E™ is a trademark of Texas Instruments.

WEBENCH® and SIMPLE SWITCHER® are registered trademarks of Texas Instruments.

All trademarks are the property of their respective owners.

## 10.6 Electrostatic Discharge Caution

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_039.png)

金

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_040.png)

## 10.7 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

## 11 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_041.png)

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| LMR51430XDDCR | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 4BXP |
| LMR51430XDDCR.A | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 4BXP |
| LMR51430XFDDCR | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 4BXF |
| LMR51430XFDDCR.A | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 4BXF |
| LMR51430YDDCR | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 4BYP |
| LMR51430YDDCR.A | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 4BYP |
| LMR51430YFDDCR | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | Call TI &#124; Sn | Level-1-260C-UNLIM | -40 to 150 | 4BYF |
| LMR51430YFDDCR.A | Active | Production | SOT-23- THIN (DDC) &#124; 6 | 3000 &#124; LARGE T&R | Yes | SN | Level-1-260C-UNLIM | -40 to 150 | 4BYF |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

(4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_042.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

31-Oct-2025

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_043.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

5-Aug-2023

## TAPE AND REEL INFORMATION

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_044.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_045.png)

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| LMR51430XDDCR | SOT-23- THIN | DDC | 6 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3 |
| LMR51430XFDDCR | SOT-23- THIN | DDC | 6 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3 |
| LMR51430YDDCR | SOT-23- THIN | DDC | 6 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3 |
| LMR51430YFDDCR | SOT-23- THIN | DDC | 6 | 3000 | 180.0 | 8.4 | 3.2 | 3.2 | 1.4 | 4.0 | 8.0 | Q3 |

## *All dimensions are nominal

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_046.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

5-Aug-2023

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_047.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| LMR51430XDDCR | SOT-23-THIN | DDC | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LMR51430XFDDCR | SOT-23-THIN | DDC | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LMR51430YDDCR | SOT-23-THIN | DDC | 6 | 3000 | 210.0 | 185.0 | 35.0 |
| LMR51430YFDDCR | SOT-23-THIN | DDC | 6 | 3000 | 210.0 | 185.0 | 35.0 |

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_048.png)

SCALE 4.0 0

SMALL OUTLINE TRANSISTOR

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_049.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Reference JEDEC MO-193.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_050.png)

SMALL OUTLINE TRANSISTOR

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_051.png)

NOTES: (continued)

4. Publication IPC-7351 may have alternate designs.
5. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_052.png)

## EXAMPLE STENCIL DESIGN

## SOT-23 - 1.1 max height

SMALL OUTLINE TRANSISTOR

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_053.png)

SOLDER PASTE EXAMPLE BASED ON 0.125 THICK STENCIL SCALE:15X

4214841/E 08/2024

NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.
7. Board assembly site may have different recommendations for stencil design.

![Image](LMR51430%20Buck%20Datasheet%20%28used%20by%20LSU%20BMS%29_files/img_054.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2025, Texas Instruments Incorporated Last updated 10/2025
<!-- Converted from TPS3431 Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](TPS3431%20Datasheet_files/img_001.png)

![Image](TPS3431%20Datasheet_files/img_002.png)

![Image](TPS3431%20Datasheet_files/img_003.png)

![Image](TPS3431%20Datasheet_files/img_004.png)

![Image](TPS3431%20Datasheet_files/img_005.png)

[TPS3431](https://www.ti.com/product/TPS3431)

SNVSB66A - JULY 2018 - REVISED OCTOBER 2021

## TPS3431 Standard Programmable Watchdog Timer with Enable

## 1 Features

- Factory-programmed precision watchdog timers:
- ±2.5% Accurate watchdog timeout (WDT) typical at 25°C
- Watchdog disable feature
- User-programmable watchdog timeout
- Input voltage range: VDD = 1.8 V to 6.5 V
- Low quiescent current: IDD = 10 µA (typical)
- Active-low open-drain output
- Enable input (EN) and enable output (ENOUT)
- Available in a small 3-mm × 3-mm, 8-pin VSON package
- Junction operating temperature range: -40°C to +125°C

## 2 Applications

- [Cellular module asset tracker](https://www.ti.com/solution/cellular-module-asset-tracking)
- [Energy storage power conversion system (PCS)](https://www.ti.com/solution/energy-storage-power-conversion-system)
- [Electricity meter](https://www.ti.com/solution/electricity-meter)
- [Motion detector (PIR, uWave, etc.)](https://www.ti.com/solution/ip-network-camera)
- [IP network camera](https://www.ti.com/solution/ip-network-camera)
- [Surgical equipment](https://www.ti.com/solution/surgical-equipment)

![Image](TPS3431%20Datasheet_files/img_006.png)

Copyright © 2018, Texas Instruments Incorporated

- A. EN can also be left floating and is internally pulled-up to VDD
- B. ENOUT can also be left floating or tied to WDO

Standard Watchdog Timer Circuit

## 3 Description

The TPS3431 is a standard programmable watchdog timer with an enable feature for a wide variety of applications. The watchdog timeout features a 15% accuracy, high-precision timing (-40°C to +125°C) and 2.5% typical at 25°C. The watchdog timeout can be programmed either by an external capacitor, or by factory-programmed default delay settings. The watchdog can be disabled via the Enable pin or the SET logic pins to avoid undesired watchdog timeouts during the development process.

The TPS3431 is available in a small 3.00-mm × 3.00-mm, 8-pin VSON package.

## Device Information (1)

| PART NUMBER | PACKAGE | BODY SIZE (NOM) |
| - | - | - |
| TPS3431 | VSON (8) | 3.00 mm × 3.00 mm |

- (1) For all available packages, see the orderable addendum at the end of the data sheet.

Normalized Watchdog Timeout (tWD) Accuracy (SET1 = 1, CWD = NC)

![Image](TPS3431%20Datasheet_files/img_007.png)

![Image](TPS3431%20Datasheet_files/img_008.png)

![Image](TPS3431%20Datasheet_files/img_009.png)

## Table of Contents

| 1 Features............................................................................1 |  | 8 Application and Implementation..................................13 |
| - | - | - |
| 2 Applications.....................................................................1 |  | 8.1 Application Information............................................. 13 |
| 3 Description.......................................................................1 | 8.2 | Typical Application.................................................... 15 |
| 4 Revision History.............................................................. 2 | 8.3 | Programmable Application........................................17 |
| 5 Pin Configuration and Functions...................................3 | 9 | Power Supply Recommendations................................20 |
| 6 Specifications.................................................................. | 4 10 | Layout...........................................................................21 |
| 6.1 Absolute Maximum Ratings........................................ | 4 | 10.1 Layout Guidelines................................................... 21 |
| 6.2 ESD Ratings............................................................... | 4 10.2 | Layout Example...................................................... 21 |
| 6.3 Recommended Operating Conditions.........................4 | 11 Device | and Documentation Support..........................22 |
| 6.4 Thermal Information....................................................5 | 11.1 | Device Support........................................................22 |
| 6.5 Electrical Characteristics.............................................5 | 11.2 | Documentation Support.......................................... 22 |
| 6.6 Timing Requirements..................................................6 | 11.3 | Receiving Notification of Updates.. 22 |
| 6.7 Timing Diagrams ........................................................7 | 11.4 | Documentation Support Resources................................................. 22 |
| 6.8 Typical Characteristics................................................8 | 11.5 | Trademarks............................................................. 22 |
| 7 Detailed Description........................................................9 | 11.6 | Electrostatic Discharge Caution.............................. 22 |
| 7.1 Overview.....................................................................9 | 11.7 | Glossary..................................................................22 |
| 7.2 Functional Block Diagram...........................................9 | 12 | Mechanical, Packaging, and Orderable |
| 7.3 Feature Description.....................................................9 |  | Information.................................................................... 22 |
| 7.4 Device Functional Modes..........................................11 Changes from Revision * (July 2018) to Revision · Updated the Applications section with web · Removed "15% timing accuracy (-40°C to · Updated ESD · Updated ICWD min and max · Updated VCWD min and max · Added a footnote to for tINIT · Updated tWDU min and max boundry values from · Updated tWDU min and max values for all · Updated the equations 3 and 4 with tWD min and | A (June 2021) Ratings.........................................................................................................................................4 spec...................................................................................................................... ............................................................................................................................... 0.85 and 1.15 max boundry respectively.......................................................................................................................................................17 | Page links................................................................................................ 1 +125°C),"........................................................................................ 1 spec........................................................................................................................5 5 6 to 0.905 and 1.095 respectively...................14 capacitors........................................................................................14 values from 0.85 and 1.15 to 0.905 and 1.095 |
| 4 Revision History | 4 Revision History | 4 Revision History |
| · Removed "±15% Accurate Watchdog Timeout and Watchdog Reset Delays Over Temperature"..................... 1 | · Removed "±15% Accurate Watchdog Timeout and Watchdog Reset Delays Over Temperature"..................... 1 | · Removed "±15% Accurate Watchdog Timeout and Watchdog Reset Delays Over Temperature"..................... 1 |

![Image](TPS3431%20Datasheet_files/img_010.png)

## 5 Pin Configuration and Functions

![Image](TPS3431%20Datasheet_files/img_011.png)

- A. EN can also be left floating and is internally pulled-up to VDD
- B. ENOUT can also be left floating or tied to WDO

Figure 5-1. DRB Package: TPS3431 3-mm × 3-mm VSON-8

Top View

Table 5-1. Pin Functions

| PIN - NAME | PIN - NO. | I/O | DESCRIPTION |
| - | - | - | - |
| VDD | 1 | I | Supply voltage pin. For noisy systems, connecting a 0.1-μF bypass capacitor is recommended. |
| CWD | 2 | I | Programmable watchdog timeout input. The watchdog timeout is set by connecting a capacitor between this pin and ground. Connecting via a 10-kΩ resistor to VDD or leaving unconnected further enables the selection of the preset watchdog timeouts; see the CWD Functionality section. TheTPS3431 determines the watchdog timeout using Equation 1 |
| EN | 3 | I | Enable input pin. This pin is internally pulled up to VDD and must be logic high or left floating. When EN goes logic low, ENOUT goes logic low and WDI is ignored and WDO remains logic high. When EN goes logic high, ENOUT goes high (asserts) after the watchdog reset delay time (tRST). This pin can also be driven with an external push-button, transistor, or microcontroller. |
| GND | 4 | - | Ground pin |
| SET1 | 5 | I | Logic input. Grounding the SET1 pin disables the watchdog timer. SET1 and CWD select the watchdog timeouts; see the SET1 section. |
| WDI | 6 | I | Watchdog input. A falling edge must occur at WDI before the timeout (tWD) expires. When the watchdog is not in use, the SET1 pin can be used to disable the watchdog. WDI is ignored when WDO is low (asserted) and when the watchdog is disabled. If the watchdog is disabled, WDI cannot be left unconnected and must be driven to either VDD or GND. |
| WDO | 7 | O | Watchdog open-drain active-low output. Connect WDO with a 1-kΩ to 100-kΩ resistor to the correct pull-up voltage rail (VPU). WDO goes low (asserts) when a watchdog timeout occurs. When a watchdog timeout occurs, WDO goes low (asserts) for the watchdog reset delay time (tRST). When EN goes low, WDO is in a high-impedance state and will be pulled to logic high. |
| ENOUT | 8 | O | Enable open-drain active-high output. Connect ENOUT with a 1-kΩ to 100-kΩ resistor to the correct pull-up voltage rail (VPU). When EN goes logic high, ENOUT goes high impedance and pulls logic high (asserts) due to the external pull-up resistor after the watchdog reset delay time (tRST). When EN is forced logic low, ENOUT goes low after 200 ns and remains logic low as long as EN is logic low. |
| Thermal pad | Thermal pad | - | Connect the thermal pad to a large-area ground plane. The thermal pad is internally connected to GND. |

![Image](TPS3431%20Datasheet_files/img_012.png)

## 6 Specifications

## 6.1 Absolute Maximum Ratings

over operating free-air temperature range (unless otherwise noted) (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Supply voltage range | VDD | -0.3 | 7 | V |
| Output voltage range | ENOUT, WDO | -0.3 | 7 | V |
| Voltage ranges | SET1, WDI, EN | -0.3 | 7 | V |
| Voltage ranges | CWD | -0.3 | VDD + 0.3 (3) | V |
| Output pin current | ENOUT, WDO |  | ±20 | mA |
| Input current (all pins) | Input current (all pins) |  | ±20 | mA |
| Continuous total power dissipation | Continuous total power dissipation | See Section 6.4 | See Section 6.4 |  |
| Temperature | Operating junction, TJ (2) | -40 | 150 | °C |
| Temperature | Operating free-air temperature, TA (2) | -40 | 150 | °C |
| Temperature | Storage, Tstg | -65 | 150 | °C |

(1) Stresses beyond those listed under Absolute Maximum Ratings may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Conditions. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

(2) TJ = TA as a result of the low dissipated power in this device.

(3) The absolute maximum rating is VDD + 0.3 V or 7.0 V, whichever is smaller.

## 6.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| - | - | - | - | - |
| V(ESD) | Electrostatic discharge | Human-body model (HBM), per ANSI/ESDA/JEDEC JS-001 (1) Charged-device model (CDM), per JEDEC specification JESD22-C101 (2) | ±4000 ±1000 | V |

(1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process. Manufacturing with less than 500-V HBM is possible with the necessary precautions.

(2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process. Manufacturing with less than 250-V CDM is possible with the necessary precautions.

## 6.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - |
| VDD | Supply pin voltage | 1.8 |  | 6.5 | V |
| VSET1 | SET1 pin voltage | 0 |  | 6.5 | V |
| CCWD | Watchdog timing capacitor | 0.1 (1) |  | 1000 (1) | nF |
| CWD | Pullup resistor to VDD | 9 | 10 | 11 | kΩ |
| RPU | Pullup resistor, ENOUT and WDO | 1 | 10 | 100 | kΩ |
| IEN | EN pin current |  |  | 10 | mA |
| IWDO | Watchdog output current |  |  | 10 | mA |
| TJ | Junction Temperature | -40 |  | 125 | °C |

(1) Using a CCWD capacitor of 0.1 nF or 1000 nF gives a tWDU(typ) of 62.74 ms or 77.45 seconds, respectively.

![Image](TPS3431%20Datasheet_files/img_013.png)

## 6.4 Thermal Information

| THERMAL METRIC (1) | THERMAL METRIC (1) | TPS3431 DRB (VSON) 8 PINS | UNIT |
| - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 50.7 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 51.6 | °C/W |
| RθJB | Junction-to-board thermal resistance | 25.8 | °C/W |
| ψJT | Junction-to-top characterization parameter | 1.3 | °C/W |
| ψJB | Junction-to-board characterization parameter | 25.8 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | 7.1 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application report, SPRA953.

## 6.5 Electrical Characteristics

at 1.8 V ≤ VDD ≤ 6.5 V over the operating temperature range of -40°C ≤ TJ ≤ +125°C (unless otherwise noted); the open-drain pullup resistors are 10 kΩ; typical values are at TJ = 25°C

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| GENERAL CHARACTERISTICS | GENERAL CHARACTERISTICS | GENERAL CHARACTERISTICS | GENERAL CHARACTERISTICS | GENERAL CHARACTERISTICS | GENERAL CHARACTERISTICS | GENERAL CHARACTERISTICS |
| VDD (2) (3) | Supply voltage |  | 1.8 |  | 6.5 | V |
| IDD | Supply current |  |  | 10 | 19 | µA |
| VPOR (1) | Power-on reset voltage | VOL(MAX) = 0.25 V |  |  | 0.8 | V |
| WINDOW WATCHDOG FUNCTION | WINDOW WATCHDOG FUNCTION | WINDOW WATCHDOG FUNCTION | WINDOW WATCHDOG FUNCTION | WINDOW WATCHDOG FUNCTION | WINDOW WATCHDOG FUNCTION | WINDOW WATCHDOG FUNCTION |
| IEN | EN pin internal pullup current | VEN = 0V | 500 | 620 | 700 | nA |
| ICWD | CWD pin charge current | CWD = 0.5 V | 347 | 375 | 403 | nA |
| VCWD | CWD pin threshold voltage |  | 1.196 | 1.21 | 1.224 | V |
| VOL | ENOUT, WDO output low | VDD = 5 V, ISINK = 3 mA |  |  | 0.4 | V |
| ID | ENOUT, WDO output leakage current | VDD = 1.8 V, VWDO = 6.5 V |  |  | 1 | µA |
| VIL | Low-level input voltage (EN, SET1) |  |  |  | 0.25 | V |
| VIH | High-level input voltage (EN, SET1) |  | 0.8 |  |  | V |
| VIL(WDI) | Low-level input voltage (WDI) |  |  |  | 0.3 × VDD | V |
| VIH(WDI) | High-level input voltage (WDI) |  | 0.8 × VDD |  |  | V |

(1) When VDD falls below VPOR, WDI and ENOUT is undefined.

(2) When VDD falls below VDDMIN, WDI is ignored and ENOUT is driven low

(3) During power-on, VDD must be a minimum 1.8 V for at least 300 µs before WDI is active and ENOUT is high impedance.

![Image](TPS3431%20Datasheet_files/img_014.png)

## 6.6 Timing Requirements

|  |  | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - |
| GENERAL | GENERAL |  |  |  |  |
| tINIT | CWD pin evaluation period (1) |  | 381 |  | µs |
|  | EN, SET1 pin setup time |  | 1 |  | µs |
|  | Startup delay (2) |  | 300 |  | µs |
| DELAY FUNCTION | DELAY FUNCTION |  |  |  |  |
| tEN_ENOUT | EN to ENOUT | delay | 200 |  | ns |
| tRST | Watchdog reset | delay | 170 200 | 230 | ms |
| WINDOW WATCHDOG FUNCTION | WINDOW WATCHDOG FUNCTION |  |  |  |  |
| tWD | Watchdog timeout | CWD = NC, SET1 = 1 | 1360 1600 | 1840 | ms |
| tWD | Watchdog timeout | CWD = 10 kΩ to VDD, SET1 = 1 | 170 200 | 230 | ms |
| tWD | Watchdog timeout | CWD = NC, SET1 = 0 | Watchdog | disabled | Watchdog |
| tWD |  | CWD = 10 kΩ to VDD, SET1 = 0 | Watchdog | disabled |  |
| tWD-setup | Setup time required for device to respond to changes on WDI after being enabled | Setup time required for device to respond to changes on WDI after being enabled | 150 |  | µs |
|  | Minimum WDI pulse duration | Minimum WDI pulse duration | 50 |  | ns |
| tWD-del | WDI to WDO delay | WDI to WDO delay | 50 |  | ns |

(1) Refer to Section 8.1.1.2.

(2) During power-on, VDD must be a minimum 1.8 V for at least 300 µs before WDI is active and ENOUT is high impedance.

![Image](TPS3431%20Datasheet_files/img_015.png)

## 6.7 Timing Diagrams

Figure 6-1. Timing Diagram

![Image](TPS3431%20Datasheet_files/img_016.png)

- A. See Figure 6-2 for WDI timing requirements.

Figure 6-2. Watchdog Timing Diagram

![Image](TPS3431%20Datasheet_files/img_017.png)

![Image](TPS3431%20Datasheet_files/img_014.png)

## 6.8 Typical Characteristics

all typical characteristics curves are taken at 25°C with 1.8 V ≤ VDD ≤ 6.5 V (unless other wise noted)

![Image](TPS3431%20Datasheet_files/img_018.png)

![Image](TPS3431%20Datasheet_files/img_015.png)

## 7 Detailed Description

## 7.1 Overview

The TPS3431 is a standard programmable watchdog timer with enable/disable feature. This device includes a precision watchdog timer that achieves 15% timing accuracy over the specified temperature range of -40°C to +125°C.

## 7.2 Functional Block Diagram

![Image](TPS3431%20Datasheet_files/img_019.png)

## 7.3 Feature Description

## 7.3.1 Enable Input (EN) and Enable Output (ENOUT)

The Enable (EN) input allows a processor or other logic circuits to initiate a single cycle watchdog reset by momentarily bringing Enable low, or a permanent disable by keeping Enable low. After EN goes to a logic high and VDD is above VDD (min), ENOUT and WDO go logic high after the watchdog reset delay time (tRST). If EN is not controlled externally, then EN can either be connected to VDD or left floating because the EN pin is internally pulled up to VDD. When EN is forced logic low, ENOUT goes low after a propagation delay of 200 ns and WDO goes high impedance and pulls to logic high due to the external pull-up resistor. Because WDO and ENOUT are both open-drain outputs, these outputs can be tied together to create an OR logic function so that if either output pulls down to logic low, the other will also pull down logic low.

## 7.3.2 Watchdog Mode

This section provides information for the watchdog mode of operation.

![Image](TPS3431%20Datasheet_files/img_020.png)

## 7.3.2.1 CWD

The CWD pin provides the user the functionality of both high-precision, factory-programmed watchdog timing options and user-programmable watchdog timing. The TPS3431 features three options for setting the watchdog timer: connecting a capacitor to the CWD pin, connecting a pull-up resistor to VDD, and leaving the CWD pin unconnected. The configuration of the CWD pin is evaluated by the device every time VDD rises above VDD (min). The pin evaluation is controlled by an internal state machine that determines which option is connected to the CWD pin. The sequence of events typically takes 381 μs (tINIT) to determine if the CWD pin is left unconnected, pulled-up through a resistor, or connected to a capacitor. If the CWD pin is being pulled up to VDD, a 10-kΩ resistor is required.

## 7.3.2.2 Watchdog Input WDI

WDI is the watchdog timer input that controls the WDO output. The WDI input is triggered by the falling edge of the input signal. To ensure proper functionality of the watchdog timer, always issue the WDI pulse before tWD(min). If the pulse is issued in this region, then WDO remains unasserted. Otherwise, the device asserts WDO, putting the WDO pin into a low-impedance state therefore WDO will be logic low.

The watchdog input (WDI) is a digital pin. To ensure there is no increase in IDD, drive the WDI pin to either VDD or GND at all times. Putting the pin to an intermediate voltage can cause an increase in supply current (IDD) because of the architecture of the digital logic gates. When EN is logic low, the watchdog is disabled and all signals input to WDI are ignored. When EN is logic high, the device resumes normal operation and no longer ignores the signal on WDI. If the watchdog is disabled, drive the WDI pin to either VDD or GND. Figure 7-1 shows the valid region for a WDI pulse to be issued to prevent WDO from being triggered and pulled low.

Figure 7-1. Watchdog Timing Diagram

![Image](TPS3431%20Datasheet_files/img_021.png)

![Image](TPS3431%20Datasheet_files/img_010.png)

## 7.3.2.3 Watchdog Output WDO

The TPS3431 features an active-low open-drain watchdog output that asserts when a pulse on WDI fails to arrive within the watchdog timeout. When EN is logic high, the WDO signal maintains normal operation. When the EN pin is logic low, the WDO pin goes to a high-impedance state and pulls logic high due to the external pull-up resistor. Because WDO and ENOUT are both open-drain outputs, these outputs can be tied together to create an OR logic function so that if either output pulls down to logic low, the other will also pull down logic low.

## 7.3.2.4 SET1

The SET1 pin can enable and disable the watchdog timer and should be used when disabling the watchdog timer for longer than one watchdog reset cycle. If SET1 is set to GND, the watchdog timer is disabled and WDI is ignored. If the watchdog timer is disabled, drive the WDI pin to either GND or VDD to ensure that there is no increase in IDD. When SET1 is logic high, the watchdog operates normally. The SET1 pin can be changed dynamically; however, if the watchdog is going from disabled to enabled there is a 150 µs setup time where the watchdog does not respond to changes on WDI, as shown in Figure 7-2. Note: disabling using SET1 pin causes a delay defined by the fixed 150-us setup time when enabling again.

Figure 7-2. Enabling and Disabling the Watchdog

![Image](TPS3431%20Datasheet_files/img_022.png)

## 7.4 Device Functional Modes

Table 7-1 summarizes the functional modes of the TPS3431.

Table 7-1. Device Functional Modes

| VDD | EN | ENOUT | WDI | WDO |
| - | - | - | - | - |
| VDD < VPOR | --- | --- | --- | --- |
| VPOR ≤ VDD < VDD(min) | --- | Low | Ignored | High |
| VDD > VDD (min) (1) | High | High | tPULSE < tWD(min) (2) | High |
| VDD > VDD (min) (1) | High | High | tPULSE > tWD(min) (2) | Low |
| VDD > VDD (min) (1) | Low | Low | Ignored | High |

- (1) VDD must be above VDD (min)for longer than 300 µs.

(2) Where tpulse is the time between the falling edges on WDI.

## 7.4.1 VDD is Below VPOR ( VDD &lt; VPOR)

When VDD is less than VPOR, WDO is undefined and can be either high or low. The state of WDO largely depends on the load that the WDO pin is experiencing.

![Image](TPS3431%20Datasheet_files/img_023.png)

## 7.4.2 Above Power-On-Reset, But Less Than VDD(min) (VPOR ≤ VDD &lt; VDD(min))

When the voltage on VDD is less than VDD(min), and greater than or equal to VPOR, the WDO signal is asserted (logic low). When EN is logic low, the watchdog output WDO is in a high-impedance state and logic low regardless of the WDI signal that is input to the device.

## 7.4.3 Normal Operation (VDD ≥ VDD(min))

When VDD is greater than or equal to VDD(min) and EN is logic high, the WDO signal is determined by WDI. When WDI is within the watchdog timeout, the internal MOSFET turns off and WDO is pulled high through external pull-up resistor. When WDI is not within the watchdog timeout, the internal MOSFET turns on and WDO is pulled to logic low. When EN is logic low, ENOUT goes to logic low and WDO goes to a high-impedance state and pulls to logic high due to the external pull-up resistor.

![Image](TPS3431%20Datasheet_files/img_013.png)

## 8 Application and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 8.1 Application Information

The following sections describe in detail proper device implementation, depending on the final application requirements.

## 8.1.1 CWD Functionality

The TPS3431 features three options for setting the watchdog timeout: connecting a capacitor to the CWD pin, connecting a pull-up resistor to VDD, and leaving the CWD pin unconnected. Figure 8-1 shows a schematic drawing of all three options. If this pin is connected to VDD through a 10-kΩ pullup resistor or left unconnected (high impedance), then the factory-programmed watchdog timeouts are enabled; see the Section 8.1.1.1 section. Otherwise, the watchdog timeout can be adjusted by placing a capacitor from the CWD pin to ground.

Figure 8-1. CWD Charging Circuit

![Image](TPS3431%20Datasheet_files/img_024.png)

## 8.1.1.1 Factory-Programmed Timing Options

If using the factory-programmed timing options (listed in Table 8-1), the CWD pin must either be unconnected or pulled up to VDD through a 10-kΩ pull-up resistor. Using these options enables high-precision, 15% accurate watchdog timing.

Table 8-1. Factory Programmed Watchdog Timing

| INPUT - CWD | INPUT - SET1 | STANDARD WATCHDOG TIMEOUT WDT (tWD) - MIN | STANDARD WATCHDOG TIMEOUT WDT (tWD) - TYP | STANDARD WATCHDOG TIMEOUT WDT (tWD) - MAX | UNIT |
| - | - | - | - | - | - |
| NC | 0 | Watchdog disabled | Watchdog disabled | Watchdog disabled |  |
| NC | 1 | 1360 | 1600 | 1840 | ms |
| 10 kΩ to VDD | 0 | Watchdog disabled | Watchdog disabled | Watchdog disabled |  |
| 10 kΩ to VDD | 1 | 170 | 200 | 230 | ms |

![Image](TPS3431%20Datasheet_files/img_025.png)

## 8.1.1.2 CWD Adjustable Capacitor Watchdog Timeout

Adjustable capacitor timing is achievable by connecting a capacitor to the CWD pin. If a capacitor is connected to CWD, then a 375-nA, constant-current source charges CCWD until VCWD = 1.21 V. Table 8-2 shows how to calculate tWD using Equation 1 and the SET1 pin. The TPS3431 determines the watchdog timeout with the formulas given in Equation 1, where CCWD is in nanofarads and tWD is in milliseconds.

<!-- formula-not-decoded -->

The TPS3431 is designed and tested using CCWD capacitors between 100 pF and 1 µF. Note that Equation 1 is for ideal capacitors and capacitor tolerances vary the actual device timing. For the most accurate timing, use ceramic capacitors with COG dielectric material. If a CCWD capacitor is used, Equation 1 can be used to set tWD for the watchdog timeout. Table 8-3 shows the minimum and maximum calculated tWD values using an ideal capacitor.

Table 8-2. Programmable CWD Timing

| INPUT - CWD | INPUT - SET1 | WATCHDOG TIMEOUT WDT (tWD) (1) - MIN | WATCHDOG TIMEOUT WDT (tWD) (1) - TYP | WATCHDOG TIMEOUT WDT (tWD) (1) - MAX | UNIT |
| - | - | - | - | - | - |
| CCWD | 0 | Watchdog disabled | Watchdog disabled | Watchdog disabled | Watchdog disabled |
| CCWD | 1 | tWD × 0.905 | tWD Equation 1 | tWD × 1.095 | ms |

(1) Calculated from Equation 1 using an ideal capacitor.

Table 8-3. tWD Values for Common Ideal Capacitor Values

| CCWD | WATCHDOG TIMEOUT WDT (tWD) - MIN (1) | WATCHDOG TIMEOUT WDT (tWD) - TYP | WATCHDOG TIMEOUT WDT (tWD) - MAX (1) | UNIT |
| - | - | - | - | - |
| 100 pF | 56.77 | 62.74 | 68.7 | ms |
| 1 nF | 119.82 | 132.4 | 144.98 | ms |
| 10 nF | 750 | 829 | 908 | ms |
| 100 nF | 7054 | 7795 | 8536 | ms |
| 1 μF | 70096 | 77455 | 84814 | ms |

(1) The minimum and maximum values are calculated using an ideal capacitor.

![Image](TPS3431%20Datasheet_files/img_015.png)

## 8.2 Typical Application

![Image](TPS3431%20Datasheet_files/img_026.png)

Copyright © 2018, Texas Instruments Incorporated

- A. EN can also be left floating and is internally pulled-up to VDD
- B. ENOUT can also be left floating or tied to WDO

Figure 8-2. Monitoring a Microcontroller with Standard Watchdog Timer

## 8.2.1 Design 1 Requirements

| PARAMETER | DESIGN REQUIREMENT | DESIGN RESULT |
| - | - | - |
| Output logic voltage | 3.3V Open-Drain | 3.3V Open-Drain |
| Watchdog Timeout | Leave CWD disconnected: 1.6 seconds (typical) | tWD(min) = 1360 ms, tWD(TYP) = 1600 ms, tWD(max) = 1840 ms |
| Maximum device current consumption | 35 µA | 33 µA when WDO is asserted |

## 8.2.2 Detailed Design 1 Procedure

## 8.2.2.1 Calculating WDO Pullup Resistor Design 1

The TPS3431 uses an open-drain configuration for the WDO circuit, as shown in Figure 8-3. When the internal MOSFET is off, the external pull-up resistor pulls the drain of the transistor to VDD and when the MOSFET is turned on, the MOSFET attempts to pull the drain to ground, thus creating an effective resistor divider. The resistors in this divider must be chosen to ensure that VOL is below the maximum value.

To choose the proper pull-up resistor, there are three key specifications to keep in mind: the pull-up voltage (VPU), the recommended maximum WDO pin current (IWDO), and VOL.

The maximum VOL is 0.4 V, meaning that the effective resistor divider created must be able to bring the voltage on the reset pin below 0.4 V with IWDO kept below 10 mA. For this example, with a VPU of 3.3 V, a resistor must be chosen to keep IWDO below 35 μA because this value is the maximum consumption current allowed. To ensure this specification is met, a pull-up resistor value of 100 kΩ was selected, which sinks a maximum of 33 μA when WDO is asserted.

Figure 8-3. WDO Open-Drain Configuration

![Image](TPS3431%20Datasheet_files/img_027.png)

![Image](TPS3431%20Datasheet_files/img_028.png)

## 8.2.2.2 Setting the Watchdog Design 1

As illustrated in Figure 8-1 there are three options for setting the watchdog timer. The design specifications in this application allow for a factory-programmed timing option by leaving CWD floating. To ensure proper functionality, a falling edge must be issued before tWD(min) with is set for 1.36 seconds when CWD is not connected. Figure 8-8 illustrates that a WDI signal with a period of 1 second keeps WDO from asserting.

Figure 8-4 shows WDO asserting when the WDI signal has a period longer than tWD(max) which is 1.84 seconds when CWD is not connected. Figure 8-5 shows a watchdog fault caused by missing WDI pulse followed by correct timing WDI pulses to deactivate WDO.

## 8.2.3 Application Curves Design 1

Unless otherwise stated, application curves were taken at TA = 25°C.

Figure 8-4. WDO Fault Caused by WDI Pulse Arriving Too Late (After tWD(max))

![Image](TPS3431%20Datasheet_files/img_029.png)

Figure 8-5. WDO Fault Caused by missing WDI Pulses Followed by Correct Timing WDI Pulses

![Image](TPS3431%20Datasheet_files/img_030.png)

![Image](TPS3431%20Datasheet_files/img_015.png)

## 8.3 Programmable Application

![Image](TPS3431%20Datasheet_files/img_031.png)

Copyright © 2018, Texas Instruments Incorporated

Figure 8-6. Monitoring the Supply Voltage and Watchdog Supervision of a Microcontroller

## 8.3.1 Design 2 Requirements

| PARAMETER | DESIGN REQUIREMENT | DESIGN RESULT |
| - | - | - |
| Watchdog disable for initialization period | Watchdog must remain disabled for 5 seconds until logic enables the watchdog timer | 5.02 seconds (typ) |
| Programmable disable feature | Microcontroller controls SET1 on TPS3431 via a GPIO | The Microcontroller can disable TPS3431 via SET1 and thus disable the watchdog for any reason. |
| Output logic voltage | 1.8-V Open-Drain | 1.8V Open-Drain |
| Monitored rail (TPS3890) | 1.8 V with a 5% threshold and 1% accuracy | Worst-case VITN = 1.714 V - 4.7% |
| Watchdog timeout (TPS3431) | 265 ms typical | tWD(min) = 213 ms, tWD(TYP) = 264 ms, tWD(max) = 319 ms |
| Maximum device current consumption | 50 µA | 37 µA when WDO is asserted |

## 8.3.2 Detailed Design 2 Procedure

## 8.3.2.1 Calculating WDO Pullup Resistor Design 2

The TPS3431 uses an open-drain configuration for the WDO circuit. When the internal MOSFET is off, the external pull-up resistor pulls the drain of the transistor to VDD and when the MOSFET is turned on, the MOSFET attempts to pull the drain to ground, thus creating an effective resistor divider. The resistors in this divider must be chosen to ensure that VOL is below the maximum value. To choose the proper pull-up resistor, there are three key specifications to keep in mind: the pull-up voltage (VPU), the recommended maximum WDO pin current (IWDO), and VOL. The maximum VOL is 0.4 V, meaning that the effective resistor divider created must be able to bring the voltage on the reset pin below 0.4 V with IWDO kept below 10 mA. For this example, with a VPU of 1.8 V, a resistor must be chosen to keep IWDO below 50 μA because this value is the maximum consumption current allowed. To ensure this specification is met, a pull-up resistor value of 100 kΩ was selected, which sinks a maximum of 18 μA when WDO is asserted.

## 8.3.2.2 Setting the Watchdog Design 2

As illustrated in Figure 8-1 there are three options for setting the watchdog timer. The design specifications in this application require the programmable timing option (external capacitor connected to CWD). When a capacitor is connected to the CWD pin, the watchdog timer is governed by Equation 1. This equation estimation is only valid for ideal capacitors and any temperature or voltage derating must be accounted for separately.

<!-- formula-not-decoded -->

The nearest standard capacitor value is 2.7 nF. Selecting 2.7 nF for the CCWD capacitor gives the following minimum and maximum timing parameters:

![Image](TPS3431%20Datasheet_files/img_032.png)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Capacitor tolerance also influences tWD(MIN) and tWD(MAX). Select a ceramic COG dielectric capacitor for high accuracy. For 2.7 nF, COG capacitors are readily available with 5% tolerances. This selection results in a 5% decrease in tWD(MIN) and a 5% increase in tWD(MAX), giving 213.16 ms and 318.75 ms, respectively. To ensure proper functionality, a falling edge must be issued before tWD(min). Figure 8-8 illustrates that a WDI signal with a period of 260 ms keeps WDO from asserting.

## 8.3.2.3 Watchdog Disabled During Initialization Period Design 2

The watchdog is often needed to be disabled during startup to allow for an initialization period. When the initialization period is over, the watchdog timer is turned back on to allow the microcontroller to be monitored by the TPS3431. To achieve this setup, EN on TPS3431 is controlled by TPS3890 supervisor. In this application, the TPS3890 was chosen to monitor VDD as well, which means that the RESET on the TPS3890 stays low until VDD rises above VITN. When VDD comes up, the delay time can be adjusted through the CT capacitor on the TPS3890. With this approach, the RESET delay can be adjusted from a minimum of 25 μs to a maximum of 30 seconds. For this design, a typical delay of 5 seconds is needed before the watchdog timer is enabled. The CT capacitor calculation (see the TPS3890 data sheet) yields an ideal capacitance of 4.67 μF, giving a closest standard ceramic capacitor value of 4.7 μF. When connecting a 4.7 μF capacitor from CT to GND, the typical delay time is 5 seconds. Figure 8-7 shows that when the watchdog is disabled, the WDO output remains high. However when SET1 goes high and there is no WDI signal, WDO begins to assert. See the TPS3890 datasheet for detailed information on the TPS3890. The ENOUT pin on the TPS3431 reflects the status of the EN pin and can be connected to the microcontroller for monitoring or can be left floating if not being used. When the TPS3431 is disabled, ENOUT is logic low and WDO is logic high so the user can also tie ENOUT to WDO to force WDO to logic low when TPS3431 is disabled.

## 8.3.2.4 Programmable Disable Feature Design 2

The watchdog is often needed to be disabled during operation to prevent false watchdog faults. When the watchdog is disabled, all pulses or lack of pulses on WDI are ignored and WDO is high impedance as shown in Figure 8-9. When the watchdog is re-enabled, the watchdog timer is turned back on after a watchdog start-up delay of 150 µs to allow the microcontroller to be monitored by the TPS3431. To achieve this setup, SET1 on TPS3431 is controlled by a GPIO on the microcontroller and must be logic high to enable to watchdog. To disable the watchdog, the microcontroller sets the GPIO connected to SET1 to logic low. To re-enable the watchdog, the microcontroller sets the GPIO connected to SET1 back to logic high. This configuration is useful when another device or signal is already using the EN pin on TPS3431, and a programmable disable feature with minimal delay upon enable is still required. When the watchdog is disabled using SET1 instead of EN, ENOUT remains unaffected which is useful when needing to disable the watchdog but not causing another device connected to ENOUT to be disabled.

## 8.3.3 Application Curves Design 2

Unless otherwise stated, application curves were taken at TA = 25°C.

![Image](TPS3431%20Datasheet_files/img_033.png)

![Image](TPS3431%20Datasheet_files/img_034.png)

![Image](TPS3431%20Datasheet_files/img_015.png)

迎

INSTRUMENTS

[www.ti.com](https://www.ti.com/)

Figure 8-9. Watchdog Disabled With Missing WDI Pulse

![Image](TPS3431%20Datasheet_files/img_035.png)

![Image](TPS3431%20Datasheet_files/img_014.png)

## 9 Power Supply Recommendations

This device is designed to operate from an input supply with a voltage range between 1.8 V and 6.5 V. An input supply capacitor is not required for this device; however, if the input supply is noisy, then good analog practice is to place a 0.1-µF capacitor between the VDD pin and the GND pin.

![Image](TPS3431%20Datasheet_files/img_010.png)

## 10 Layout

## 10.1 Layout Guidelines

- Make sure that the connection to the VDD pin is low impedance. Good analog design practice is to place a 0.1-µF ceramic capacitor as near as possible to the VDD pin.
- If a CCWD capacitor or pull-up resistor is used, place these components as close as possible to the CWD pin. If the CWD pin is left unconnected, make sure to minimize the amount of parasitic capacitance on the pin.
- Place the pull-up resistor on WDO as close to the pin as possible.

## 10.2 Layout Example

![Image](TPS3431%20Datasheet_files/img_036.png)

C

Denotes a via

- A. EN can also be left floating and is internally pulled-up to VDD
- B. ENOUT can also be left floating or tied to WDO

Figure 10-1. TPS3431 Recommended Layout

![Image](TPS3431%20Datasheet_files/img_037.png)

## 11 Device and Documentation Support

## 11.1 Device Support

## 11.2 Documentation Support

## 11.2.1 Related Documentation

For related documentation see the following:

- [TPS3890 Low Quiescent Current, 1% Accurate Supervisor with Programmable Delay (SLVSD65)](https://www.ti.com/lit/pdf/SLVSD65)
- [TPS3431EVM-780 Evaluation Module (SBVU033)](https://www.ti.com/lit/pdf/SBVU033)

## 11.3 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Subscribe to updates to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 11.4 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 11.5 Trademarks

TI E2E™ is a trademark of Texas Instruments.

All trademarks are the property of their respective owners.

## 11.6 Electrostatic Discharge Caution

![Image](TPS3431%20Datasheet_files/img_038.png)

金

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 11.7 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

## 12 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](TPS3431%20Datasheet_files/img_039.png)

ÍNSTRUMENTS

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| TPS3431SDRBR | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 431DD |
| TPS3431SDRBR.A | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 431DD |
| TPS3431SDRBRG4 | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 431DD |
| TPS3431SDRBRG4.A | Active | Production | SON (DRB) &#124; 8 | 3000 &#124; LARGE T&R | Yes | NIPDAU | Level-1-260C-UNLIM | -40 to 125 | 431DD |

(1) Status: For more details on status, see our product life cycle.

(2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.

(3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.

- (4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.

(5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.

(6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

## OTHER QUALIFIED VERSIONS OF TPS3431 :

![Image](TPS3431%20Datasheet_files/img_039.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

9-Nov-2025

- Automotive : TPS3431-Q1

## NOTE: Qualified Version Definitions:

- Automotive - Q100 devices qualified for high-reliability automotive applications targeting zero defects

![Image](TPS3431%20Datasheet_files/img_040.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

27-Jun-2026

## TAPE AND REEL INFORMATION

![Image](TPS3431%20Datasheet_files/img_041.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](TPS3431%20Datasheet_files/img_042.png)

## *All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| TPS3431SDRBR | SON | DRB | 8 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |
| TPS3431SDRBRG4 | SON | DRB | 8 | 3000 | 330.0 | 12.4 | 3.3 | 3.3 | 1.1 | 8.0 | 12.0 | Q2 |

![Image](TPS3431%20Datasheet_files/img_043.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

27-Jun-2026

![Image](TPS3431%20Datasheet_files/img_044.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| TPS3431SDRBR | SON | DRB | 8 | 3000 | 356.0 | 356.0 | 36.0 |
| TPS3431SDRBRG4 | SON | DRB | 8 | 3000 | 367.0 | 367.0 | 35.0 |

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TPS3431%20Datasheet_files/img_045.png)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

![Image](TPS3431%20Datasheet_files/img_046.png)

INSTRUMENTS

4203482/L

![Image](TPS3431%20Datasheet_files/img_047.png)

SCALE 4.0 0

## PACKAGE OUTLINE

## VSON - 1 mm max height

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TPS3431%20Datasheet_files/img_048.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. The package thermal pad must be soldered to the printed circuit board for thermal and mechanical performance.

![Image](TPS3431%20Datasheet_files/img_049.png)

## VSON - 1 mm max height

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TPS3431%20Datasheet_files/img_050.png)

NOTES: (continued)

4. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature number SLUA271 (www.ti.com/lit/slua271).
5. Vias are optional depending on application, refer to device data sheet. If any vias are implemented, refer to their locations shown on this view. It is recommended that vias under paste be filled, plugged or tented.

![Image](TPS3431%20Datasheet_files/img_051.png)

## VSON - 1 mm max height

PLASTIC SMALL OUTLINE - NO LEAD

![Image](TPS3431%20Datasheet_files/img_052.png)

NOTES: (continued)

6. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

![Image](TPS3431%20Datasheet_files/img_051.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2026, Texas Instruments Incorporated Last updated 10/2025
<!-- Converted from TLV761 Datasheet (TI SBVS349D) - chosen.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_001.png)

INSTRUMENTS

## TLV761 18V, 1A, Fixed-Output Linear Voltage Regulator

## 3 Description

The TLV761 is a linear voltage regulator that improves the functionality of a traditional x1117 regulator (TLV1117 or LM1117) with tighter output accuracy and low quiescent current (IQ) to lower the standby power consumption. The TLV761 is pin-to-pin compatible with other fixed SOT-223, TO-252 regulators.

The TLV761 input voltage range is from 2.5V to 18V and provides an output voltage range from 0.8V to 13V to support a wide variety of applications.

The wide bandwidth PSRR performance of the TLV761 is typically greater than 60dB at 1kHz and 40dB at 1MHz, which helps attenuate the switching frequency of an upstream DC/DC converter and minimizes post regulator filtering.

Additionally, the TLV761 has an internal soft start feature to reduce inrush current during start-up, which can help save space and cost in a design by minimizing input capacitance. The TLV761 features a foldback current limit that limits the power dissipation of the device during high-load current faults or shorting events.

## Package Information

| PART NUMBER | PACKAGE (1) | PACKAGE SIZE (2) |
| - | - | - |
| TLV761 | DCY (SOT-223, 4) | 6.5mm × 7mm |
| TLV761 | KVU (TO-252, 3) | 6.6mm × 10.11mm |

- (1) For more information, see the Mechanical, Packaging, and Orderable Information.
- (2) The package size (length × width) is a nominal value and includes pins, where applicable.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_002.png)

## 1 Features

- Pin-compatible with industry-standard LM1117 and TLV1117 (x1117) devices in select packages
- Input voltage range VIN: 2.5V to 18V (abs max rating of 20V)
- Output voltage range VOUT:
- 0.8V to 13V (fixed, 100mV steps)
- Output current: Up to 1A
- Low quiescent current IQ:
- 60μA (typical, ~1.5μA in shutdown)
- ±1% output accuracy over line and load
- High PSRR: 60dB at 1kHz, 40dB at 1MHz
- Internal soft-start time: 500µs (typical)
- Foldback current limiting and thermal protection
- Stable with 1µF ceramic output capacitors
- Temperature range: -40°C to +125°C
- Packages:
- 4-pin, 6.5mm × 7mm SOT-223
- 3-pin, 6.6mm × 10.11mm TO-252

## 2 Applications

- [Appliances](http://www.ti.com/applications/industrial/appliances/overview.html)
- [Home theater and entertainment](http://www.ti.com/applications/personal-electronics/home-theater-entertainment/overview.html)
- [Motor drives](http://www.ti.com/applications/industrial/motor-drives/overview.html)
- [HVAC and building security systems](http://www.ti.com/applications/industrial/building-automation/overview.html)
- [Smart meters](https://www.ti.com/solution/electricity-meter)

Inrush Current With 22µF at COUT

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_003.png)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_004.png)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_005.png)

## Table of Contents

| 1 Features............................................................................1 | 7.1 Application Information............................................. 13 |
| - | - |
| 2 Applications.....................................................................1 | 7.2 Typical Application.................................................... 15 |
| 3 Description.......................................................................1 | 7.3 Best Design Practices...............................................17 |
| 4 Pin Configuration and Functions...................................3 | 7.4 Power Supply Recommendations.............................17 |
| 5 Specifications.................................................................. 4 | 7.5 Layout....................................................................... 18 |
| 5.1 Absolute Maximum Ratings........................................ 4 | 8 Device and Documentation Support............................19 |
| 5.2 ESD Ratings............................................................... 4 | 8.1 Device Support......................................................... 19 |
| 5.3 Recommended Operating Conditions.........................4 | 8.2 Documentation Support............................................ 19 |
| 5.4 Thermal Information....................................................5 | 8.3 Receiving Notification of Documentation Updates....19 |
| 5.5 Electrical Characteristics.............................................5 | 8.4 Support Resources................................................... 19 |
| 5.6 Typical Characteristics................................................6 | 8.5 Trademarks...............................................................19 |
| 6 Detailed Description......................................................10 | 8.6 Electrostatic Discharge Caution................................19 |
| 6.1 Overview...................................................................10 | 8.7 Glossary....................................................................19 |
| 6.2 Functional Block Diagram.........................................10 | 9 Revision History............................................................ 20 |
| 6.3 Feature Description...................................................10 | 10 Mechanical, Packaging, and Orderable |
| 6.4 Device Functional Modes..........................................12 | Information.................................................................... 20 |
| 7 Application and Implementation..................................13 |  |

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_006.png)

## 4 Pin Configuration and Functions

Figure 4-1. DCY Package, 4-Pin SOT-223 (Top View)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_007.png)

Figure 4-2. KVU Package, 3-Pin TO-252 (Top View)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_008.png)

## Table 4-1. Pin Functions

| PIN - NAME | PIN - DCY | PIN - KVU | PIN - FUNCTION | DESCRIPTION |
| - | - | - | - | - |
| GND | 1 | 1 | - | Ground pin |
| OUT | 2, Tab | 2, Tab | O | Output pin. Use the recommended capacitor value as listed in the Recommended Operating Conditions table. Place the output capacitor as close to the OUT and GND pins of the device as possible. |
| IN | 3 | 3 | I | Input pin. Use the recommended capacitor value as listed in the Recommended Operating Conditions table. Place the input capacitor as close to the IN and GND pins of the device as possible. |

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_009.png)

## 5 Specifications

## 5.1 Absolute Maximum Ratings

Over operating free-air temperature range (unless otherwise noted) (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Voltage (2) | VIN | -0.3 | 20 | V |
| Voltage (2) | VOUT (3) | -0.3 | VIN + 0.3 | V |
| Current | Maximum output current | Internally limited | Internally limited | A |
| Power | Power dissipation | Package limited (4) | Package limited (4) | W |
| Temperature | Operating junction (TJ) | -50 | 150 | °C |
| Temperature | Storage (TSTG) | -65 | 150 | °C |

(1) Stresses beyond those listed under Absolute Maximum Rating may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Condition. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

- (2) All voltages with respect to GND.
- (3) VIN + 0.3 V or 18 V (whichever is smaller).
- (4) See thermal information for further details.

## 5.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| - | - | - | - | - |
| V(ESD) | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/ JEDEC JS-001, all pins (1) | ±3000 | V |
| V(ESD) |  | Charged device model (CDM), per JEDEC specification JESD22-C101, all pins (2) | ±1000 | V |

- (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
- (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 5.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - |
| VIN | Input voltage | 2.5 |  | 18 | V |
| VOUT | Output voltage | 0.8 |  | 13.5 | V |
| IOUT | Output current (2.5 V ≤ VIN < 3 V) | 0 |  | 0.8 | A |
| IOUT | Output current (VIN ≥ 3 V) | 0 |  | 1 | A |
| COUT ESR | Output capacitor ESR | 2 |  | 500 | mΩ |
| COUT | Output capacitor (1) | 1 | 2.2 | 220 | µF |
| CIN | Input capacitor (2) |  | 1 |  | µF |
| TJ | Junction temperature | -40 |  | 125 | °C |

- (1) Effective output capacitance of 0.47 µF minimum required for stability.

(2) An input capacitor is not required for LDO stability. However, an input capacitor with an effective value of 0.47 μF minimum is recommended to counteract the effect of source resistance and inductance, which may in some cases cause symptoms of systemlevel instability such as ringing or oscillation, especially in the presence of load transients

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_010.png)

## 5.4 Thermal Information

| THERMAL METRIC (1) | THERMAL METRIC (1) | TLV761 - DCY (SOT-223) - 4 PINS | TLV761 - KVU (TO-252) - 4 PINS | UNIT |
| - | - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 95.4 | 67.2 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 55.6 | 71.8 | °C/W |
| RθJB | Junction-to-board thermal resistance | 33.7 | 45.5 | °C/W |
| ΨJT | Junction-to-top characterization parameter | 13.9 | 31.6 | °C/W |
| ΨJB | Junction-to-board characterization parameter | 33.4 | 45.4 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | N/A | 40.5 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application note.

## 5.5 Electrical Characteristics

specified at TJ = -40°C to 125°C, VIN = VOUT(nom) + 1.5V or VIN = 2.5V (whichever is greater), IOUT = 10mA, CIN = 1.0µF and COUT = 1.0µF (unless otherwise noted); typical values are at TJ= 25ºC

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| VOUT | Nominal output accuracy | TJ = 25°C | -1 |  | 1 | % |
| VOUT | Output accuracy over temperature | VIN ≥ 3.0V, VOUT(NOM) ≤ 9.0V, 1mA ≤ IOUT ≤ 1A | -1.75 |  | 1.75 | % |
| VOUT | Output accuracy over temperature | VOUT(NOM) > 9.0V, 1mA ≤ IOUT ≤ 1A | -1.5 |  | 1.5 | % |
| ΔVOUT(ΔVIN) | Line regulation (1) | VOUT(NOM) ≤ 9.0V, VOUT(NOM) + 1.5V ≤ VIN ≤ 18V, IOUT = 10mA |  |  | 0.02 | %/V |
| ΔVOUT(ΔVIN) | Line regulation (1) | VOUT(NOM) > 9.0V, VOUT(NOM) + 1.5V ≤ VIN ≤ 18V, IOUT = 10mA |  |  | 9.9 | mV |
| ΔVOUT(ΔIOUT) | Load regulation | 1mA ≤ IOUT ≤ 1A, VIN ≥ 3.0V |  | 0.1 | 0.75 | %/A |
| VDO | Dropout voltage (2) | VIN ≥ 3.0V, IOUT = 1A |  | 0.9 | 1.6 | V |
| ICL | Output current limit | VOUT = 0.9 x VOUT(NOM) , VIN ≥ 3.0V | 1.1 |  | 1.6 | A |
| ISC | Short-circuit current limit | VOUT = 0V | 150 | 250 | 350 | mA |
| IQ | Quiescent current | IOUT = 0mA |  | 65 | 100 | µA |
| IPULLDOWN | Output pulldown current (3) | VIN = 1.8V, VOUT = 2.5V | 0.7 |  | 1.1 | mA |
| PSRR | Power-supply rejection ratio | VIN = 3.3V, VOUT = 1.8V, IOUT = 300mA, f = 120Hz |  | 70 |  | dB |
| Vn | Output noise voltage | BW = 10Hz to 100kHz, VIN = 3.3V, VOUT = 0.8V, IOUT = 100mA |  | 60 |  | µVRMS |
| VUVLO+ | UVLO threshold rising | VIN rising |  | 2.2 | 2.4 | V |
| VUVLO(HYS) | UVLO hysteresis |  |  | 130 |  | mV |
| VUVLO- | UVLO threshold falling | VIN falling | 1.9 |  |  | V |
| TSD(shutdown) | Thermal shutdown temperature | Temperature increasing |  | 180 |  | ºC |
| TSD(reset) | Thermal shutdown reset temperature | Temperature falling |  | 160 |  | ºC |

(1) Line regulation is measured with VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater).

(2) VDO is measured with VIN = 95% x VOUT(nom) for fixed output devices. VDO is not measured for fixed output devices when VOUT &lt; 2.5 V.

(3) IPULLDOWN is measured with VIN = 1.8 V (lower than UVLO falling threshold, with LDO in disabled state) and 2.5 V applied on VOUT externally.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_011.png)

## 5.6 Typical Characteristics

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_012.png)

For VIN ≥ 3.0 V

Figure 5-1. VOUT Accuracy vs IOUT

0.2

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_013.png)

IOUT = 10 mA

Figure 5-2. VOUT Accuracy vs VIN

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_014.png)

IOUT = 0 mA

Figure 5-3. IQ vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_015.png)

IOUT = 0 mA

Figure 5-4. IQ Increase Below Minimum VIN

1

Figure 5-5. IGND vs IOUT

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_016.png)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_017.png)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.4 A/µs

Figure 5-6. IOUT Transient From 0 mA to 100 mA

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_006.png)

## 5.6 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_018.png)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.5 A/µs

Figure 5-7. IOUT Transient From 1 mA to 1 A

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_019.png)

Figure 5-8. IOUT Transient From 250 mA to 850 mA

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_020.png)

VIN = 5 V VOUT = 3.3 V, IOUT = 1 A, VIN ramp rate = 0.6 V/µs

Figure 5-9. VIN Transient in Dropout From 4 V to 13 V

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_021.png)

VOUT = 3.3 V, IOUT = 33 µA, VIN ramp rate = 1.6 V/µs

Figure 5-10. VIN Transient From 5 V to 16 V

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_022.png)

IOUT = 1.0 A

Figure 5-11. VDO vs VIN

1.4

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_023.png)

IOUT = 0.8 A

Figure 5-12. VDO vs VIN

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_009.png)

## 5.6 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

Figure 5-13. UVLO Thresholds vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_024.png)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_025.png)

For VIN ≥ 3.0 V

Figure 5-14. VDO vs IOUT

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_026.png)

For VIN ≥ 3.0 V

Figure 5-15. Foldback Current Limit vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_027.png)

Figure 5-16. Foldback Current Limit vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_028.png)

VOUT = 1.8 V, VIN = 3.3 V

Figure 5-17. PSRR vs IOUT

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_029.png)

VOUT = 1.8 V, IOUT = 0.55 A

Figure 5-18. PSRR vs VIN

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_006.png)

## 5.6 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

IOUT = 0.1 A, RMS noise BW = 10 Hz to 100 kHz

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_030.png)

Figure 5-19. Output Noise (Vn) vs VOUT

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_031.png)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_032.png)

## 6 Detailed Description

## 6.1 Overview

The TLV761 is a low quiescent current, high PSRR linear regulator capable of sourcing load current up to 1 A. This device is designed for high current applications such as appliances where there are increasingly stringent requirements for standby and active power consumption.

This device features integrated foldback current limit, thermal shutdown, internal output pulldown, and undervoltage lockout (UVLO). This device delivers excellent line and load transient performance. The TLV761 is low noise and exhibits very good PSRR. The operating ambient temperature range of the device is -40°C to +125°C.

## 6.2 Functional Block Diagram

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_033.png)

## 6.3 Feature Description

## 6.3.1 Dropout Voltage

Dropout voltage (VDO) is defined as the input voltage minus the output voltage (VIN - VOUT) at the rated output current (IRATED), where the pass transistor is fully on. IRATED is the maximum IOUT listed in the Recommended Operating Conditions table. The pass transistor is in the ohmic or triode region of operation, and acts as a switch. The dropout voltage indirectly specifies a minimum input voltage greater than the nominal programmed output voltage at which the output voltage is expected to stay in regulation. If the input voltage falls to less than the nominal output regulation, then the output voltage falls as well.

For a CMOS regulator, the dropout voltage is determined by the drain-source on-state resistance (RDS(ON)) of the pass transistor. Therefore, if the linear regulator operates at less than the rated current, the dropout voltage for that current scales accordingly. The following equation calculates the RDS(ON) of the device.

<!-- formula-not-decoded -->

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_006.png)

## 6.3.2 Foldback Current Limit

The device has an internal current limit circuit that protects the regulator during transient high-load current faults or shorting events. The current limit is a hybrid brick-wall-foldback scheme. The current limit transitions from a brick-wall scheme to a foldback scheme at the foldback voltage (VFOLDBACK). In a high-load current fault with the output voltage above VFOLDBACK, the brick-wall scheme limits the output current to the current limit (ICL). When the voltage drops below VFOLDBACK, a foldback current limit activates that scales back the current as the output voltage approaches GND. When the output is shorted, the device supplies a typical current called the short-circuit current limit (ISC). ICL and ISC are listed in the Electrical Characteristics table.

For this device, VFOLDBACK = 50% × VOUT(nom).

The output voltage is not regulated when the device is in current limit. When a current limit event occurs, the device begins to heat up because of the increase in power dissipation. When the device is in brick-wall current limit, the pass transistor dissipates power [(VIN - VOUT) × ICL]. When the device output is shorted and the output is below VFOLDBACK, the pass transistor dissipates power [(VIN - VOUT) × ISC]. If thermal shutdown is triggered, the device turns off. After the device cools down, the internal thermal shutdown circuit turns the device back on. If the output current fault condition continues, the device cycles between current limit and thermal shutdown. For more information on current limits, see the Know Your Limits application note.

Figure 6-1 shows a diagram of the foldback current limit.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_034.png)

Figure 6-1. Foldback Current Limit

## 6.3.3 Undervoltage Lockout (UVLO)

The device has an independent undervoltage lockout (UVLO) circuit that monitors the input voltage, allowing a controlled and consistent turn on and off of the output voltage. To prevent the device from turning off if the input drops during turn on, the UVLO has hysteresis as specified in the Electrical Characteristics table.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_009.png)

## 6.3.4 Thermal Shutdown

The device contains a thermal shutdown protection circuit to disable the device when the junction temperature (TJ) of the pass transistor rises to TSD(shutdown) (typical). Thermal shutdown hysteresis assures that the device resets (turns on) when the temperature falls to TSD(reset) (typical).

The thermal time-constant of the semiconductor die is fairly short, thus the device may cycle on and off when thermal shutdown is reached until power dissipation is reduced. Power dissipation during start-up can be high from large VIN - VOUT voltage drops across the device or from high inrush currents charging large output capacitors. Under some conditions, the thermal shutdown protection disables the device before start-up completes.

For reliable operation, limit the junction temperature to the maximum listed in the Recommended Operating Conditions table. Operation above this maximum temperature causes the device to exceed operational specifications. Although the internal protection circuitry of the device is designed to protect against thermal overall conditions, this circuitry is not intended to replace proper heat sinking. Continuously running the device into thermal shutdown or above the maximum recommended junction temperature reduces long-term reliability.

## 6.4 Device Functional Modes

## 6.4.1 Device Functional Mode Comparison

Table 6-1 shows the conditions that lead to the different modes of operation. See the Electrical Characteristics table for parameter values.

Table 6-1. Device Functional Mode Comparison

| OPERATING MODE | PARAMETER - VIN | PARAMETER - IOUT | PARAMETER - TJ |
| - | - | - | - |
| Normal operation | VIN > VOUT(nom) + VDO and VIN > VIN(min) | IOUT < IOUT(max) | TJ < TSD(shutdown) |
| Dropout operation | VIN(min) < VIN < VOUT(nom) + VDO | IOUT < IOUT(max) | TJ < TSD(shutdown) |
| Disabled (any true condition disables the device) | VIN < VUVLO | Not applicable | TJ > TSD(shutdown) |

## 6.4.2 Normal Operation

The device regulates to the nominal output voltage when the following conditions are met:

- The input voltage is greater than the nominal output voltage plus the dropout voltage (VOUT(nom) + VDO)
- The output current is less than the current limit (IOUT &lt; ICL)
- The device junction temperature is less than the thermal shutdown temperature (TJ &lt; TSD)

## 6.4.3 Dropout Operation

If the input voltage is lower than the nominal output voltage plus the specified dropout voltage, but all other conditions are met for normal operation, the device operates in dropout mode. In this mode, the output voltage tracks the input voltage. During this mode, the transient performance of the device becomes significantly degraded because the pass transistor is in the ohmic or triode region, and acts as a switch. Line or load transients in dropout can result in large output-voltage deviations.

When the device is in a steady dropout state (defined as when the device is in dropout, VIN &lt; VOUT(NOM) + VDO, directly after being in a normal regulation state, but not during start-up), the pass transistor is driven into the ohmic or triode region. When the input voltage returns to a value greater than or equal to the nominal output voltage plus the dropout voltage (VOUT(NOM) + VDO), the output voltage can overshoot for a short period of time while the device pulls the pass transistor back into the linear region.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_035.png)

[www.ti.com](https://www.ti.com/)

## 7 Application and Implementation

## Note

Information in the following applications sections is not part of the TI component specification, and TI does not warrant its accuracy or completeness. TI's customers are responsible for determining suitability of components for their purposes, as well as validating and testing their design implementation to confirm system functionality.

## 7.1 Application Information

## 7.1.1 Recommended Capacitor Types

The device is designed to be stable using low equivalent series resistance (ESR) ceramic capacitors at the input and output. Multilayer ceramic capacitors have become the industry standard for these types of applications and are recommended, but must be used with good judgment. Ceramic capacitors that employ X7R-, X5R-, and C0G-rated dielectric materials provide relatively good capacitive stability across temperature, whereas the use of Y5V-rated capacitors is discouraged because of large variations in capacitance.

Regardless of the ceramic capacitor type selected, the effective capacitance varies with operating voltage and temperature. Generally, expect the effective capacitance to decrease by as much as 50%. The input and output capacitors recommended in the Recommended Operating Conditions table account for an effective capacitance of approximately 50% of the nominal value.

## 7.1.2 Input and Output Capacitor Requirements

Although an input capacitor is not required for stability, good analog design practice is to connect a capacitor from IN to GND. This capacitor counteracts reactive input sources and improves transient response, input ripple, and PSRR. An input capacitor is recommended if the source impedance is more than 0.5 Ω. A higher value capacitor may be necessary if large, fast rise-time load or line transients are anticipated or if the device is located several inches from the input power source.

Dynamic performance of the device is improved with the use of an output capacitor. Use an output capacitor within the range specified in the Recommended Operating Conditions table for stability.

## 7.1.3 Reverse Current

Excessive reverse current can damage this device. Reverse current flows through the intrinsic body diode of the pass transistor instead of the normal conducting channel. At high magnitudes, this current flow degrades the long-term reliability of the device.

Conditions where reverse current can occur are outlined in this section, all of which can exceed the absolute maximum rating of VOUT ≤ VIN + 0.3 V.

- If the device has a large COUT and the input supply collapses with little or no load current
- The output is biased when the input supply is not established
- The output is biased above the input supply

If reverse current flow is expected in the application, external protection is recommended to protect the device. Reverse current is not limited in the device, so external limiting is required if extended reverse voltage operation is anticipated.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_011.png)

Figure 7-1 shows one approach for protecting the device.

Figure 7-1. Example Circuit for Reverse Current Protection Using a Schottky Diode

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_036.png)

## 7.1.4 Power Dissipation (PD)

Circuit reliability requires consideration of the device power dissipation, location of the circuit on the printed circuit board (PCB), and correct sizing of the thermal plane. The PCB area around the regulator must have few or no other heat-generating devices that cause added thermal stress.

To first-order approximation, power dissipation in the regulator depends on the input-to-output voltage difference and load conditions. The following equation calculates power dissipation (PD).

<!-- formula-not-decoded -->

Note

Power dissipation can be minimized, and therefore greater efficiency can be achieved, by correct selection of the system voltage rails. For the lowest power dissipation use the minimum input voltage required for correct output regulation.

For devices with a thermal pad, the primary heat conduction path for the device package is through the thermal pad to the PCB. Solder the thermal pad to a copper pad area under the device. This pad area must contain an array of plated vias that conduct heat to additional copper planes for increased heat dissipation.

The maximum power dissipation determines the maximum allowable ambient temperature (TA) for the device. According to the following equation, power dissipation and junction temperature are most often related by the junction-to-ambient thermal resistance (RθJA) of the combined PCB and device package and the temperature of the ambient air (TA).

<!-- formula-not-decoded -->

Thermal resistance (RθJA) is highly dependent on the heat-spreading capability built into the particular PCB design, and therefore varies according to the total copper area, copper weight, and location of the planes. The junction-to-ambient thermal resistance listed in the Thermal Information table is determined by the JEDEC standard PCB and copper-spreading area, and is used as a relative measure of package thermal performance.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_037.png)

## 7.1.5 Estimating Junction Temperature

The JEDEC standard now recommends the use of psi (Ψ) thermal metrics to estimate the junction temperatures of the linear regulator when in-circuit on a typical PCB board application. These metrics are not thermal resistance parameters and instead offer a practical and relative way to estimate junction temperature. These psi metrics are determined to be significantly independent of the copper area available for heat-spreading. The Thermal Information table lists the primary thermal metrics, which are the junction-to-top characterization parameter (ψJT) and junction-to-board characterization parameter (ψJB). These parameters provide two methods for calculating the junction temperature (TJ). As described in the following equations, use the junction-to-top characterization parameter (ψJT) with the temperature at the center-top of device package (TT) to calculate the junction temperature. Use the junction-to-board characterization parameter (ψJB) with the PCB surface temperature 1 mm from the device package (TB) to calculate the junction temperature.

<!-- formula-not-decoded -->

## where:

- PD is the dissipated power
- TT is the temperature at the center-top of the device package

<!-- formula-not-decoded -->

## where:

- TB is the PCB surface temperature measured 1 mm from the device package and centered on the package edge

For detailed information on the thermal metrics and how to use them, see the Semiconductor and IC Package Thermal Metrics application note.

## 7.2 Typical Application

The TLV761 is a low quiescent current linear regulator designed for high current applications. Unlike most typical high current linear regulators, the TLV761 consumes significantly less quiescent current. This device delivers excellent line and load transient performance. The device is low noise and exhibits a very good PSRR. As a result, the TLV761 is designed for high current applications that require very sensitive power-supply rails.

This regulator offers both current limit and thermal protection. The operating ambient temperature range of the device is -40°C to +125°C.

Figure 7-2 shows a typical application circuit for this device.

Figure 7-2. Typical Application Circuit

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_038.png)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_032.png)

## 7.2.1 Design Requirements

For this design example, use the parameters listed in Table 7-1 as the input parameters.

Table 7-1. Design Parameters

| PARAMETER | DESIGN REQUIREMENT |
| - | - |
| Input voltage | 12 V |
| Output voltage | 3.3 V |
| Output current | 50 mA |

## 7.2.2 Detailed Design Procedure

For this design example, the 3.3-V, fixed-version TLV76133 is selected and is powered by a standard 12-V input supply. The dropout voltage (VDO) is kept within the TLV761 dropout voltage specification for the 3.3-V output voltage option to keep the device in regulation under all load and temperature conditions for this design. A 1.0-µF output capacitor is recommended for excellent load transient response. The input capacitor is optional and is used to reduce the input impedance of the circuit and improve the transient response.

As with any regulator, increasing the size of the output capacitor reduces overshoot and undershoot magnitude.

## 7.2.3 Application Curves

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.4 A/µs

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_039.png)

Figure 7-3. IOUT Transient From 0 mA to 100 mA

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_040.png)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.5 A/µs

Figure 7-4. IOUT Transient From 1 mA to 1 A

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_041.png)

Figure 7-5. IOUT Transient From 250 mA to 850 mA

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_042.png)

VIN = 5 V VOUT = 3.3 V, IOUT = 1 A, VIN ramp rate = 0.6 V/µs

Figure 7-6. VIN Transient in Dropout From 4 V to 13 V

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_037.png)

迎

[www.ti.com](https://www.ti.com/)

VOUT = 3.3 V, IOUT = 33 µA, VIN ramp rate = 1.6 V/µs

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_043.png)

Figure 7-7. VIN Transient From 5 V to 16 V

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_044.png)

Figure 7-8. Inrush Current With 22 µF at COUT

## 7.3 Best Design Practices

Place input and output capacitors as close to the device as possible.

Use a ceramic output capacitor.

Do not exceed the device absolute maximum ratings.

## 7.4 Power Supply Recommendations

Connect a low output impedance power supply directly to the INPUT pin of the device . Inductive impedances between the input supply and the INPUT pin can create significant voltage excursions at the INPUT pin during start-up or load transient events.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_045.png)

## 7.5 Layout

## 7.5.1 Layout Guidelines

Place input and output capacitors as close to the device pins as possible. To improve characteristic AC performance such as PSRR, output noise, and transient response, design the board with separate ground planes for VIN and VOUT, with the ground plane connected only at the GND pin of the device. In addition, the ground connection for the output capacitor must be connected directly to the GND pin of the device. Higher value ESR capacitors can degrade PSRR performance.

## 7.5.2 Layout Examples

Figure 7-9. Layout Example for DCY (SOT-223) Package

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_046.png)

Figure 7-10. Layout Example for KVU (TO-252) Package

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_047.png)

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_048.png)

[www.ti.com](https://www.ti.com/)

## 8 Device and Documentation Support

## 8.1 Device Support

## 8.1.1 Device Nomenclature

| PRODUCT (1) (2) | DESCRIPTION |
| - | - |
| TLV761 abxxxy | ab is the nominal output voltage, hexadecimal coding is used. · a is used for the unit level of the output voltage. · b is used for the tenth level of the output voltage. For example, use 33 for 3.3V, A0 for 10.0V, C0 for 12.0V, and D0 for 13.0V. xxx is the package designator. y is the package quantity. |

## Table 8-1. Available Options

- (1) For the most current package and ordering information, see the Package Option Addendum at the end of this document, or visit the device product folder at www.ti.com.
- (2) The device is available in factory-programmable fixed output voltage increments of 50mV upon request.

## 8.2 Documentation Support

## 8.2.1 Related Documentation

For related documentation see the following:

- [Texas Instruments, TLV1117 Adjustable and Fixed Low-Dropout Voltage Regulator data sheet](https://www.ti.com/lit/pdf/SLVS561)
- [Texas Instruments, LM1117 800-mA Low-Dropout Linear Regulator data sheet](https://www.ti.com/lit/pdf/SNOS412)

## 8.3 Receiving Notification of Documentation Updates

To receive notification of documentation updates, navigate to the device product folder on ti.com. Click on Notifications to register and receive a weekly digest of any product information that has changed. For change details, review the revision history included in any revised document.

## 8.4 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 8.5 Trademarks

TI E2E™ is a trademark of Texas Instruments.

All trademarks are the property of their respective owners.

## 8.6 Electrostatic Discharge Caution

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_049.png)

This integrated circuit can be damaged by ESD. Texas Instruments recommends that all integrated circuits be handled with appropriate precautions. Failure to observe proper handling and installation procedures can cause damage.

ESD damage can range from subtle performance degradation to complete device failure. Precision integrated circuits may be more susceptible to damage because very small parametric changes could cause the device not to meet its published specifications.

## 8.7 Glossary

TI Glossary This glossary lists and explains terms, acronyms, and definitions.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_050.png)

## 9 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

| Changes from Revision C (April 2024) to Revision D (May 2025) | Page |
| - | - |
| · Changed KVU status from preview to Production Data .....................................................................................1 |  |
| · Changed maximum input voltage range (VIN) from 16V to 18V throughout document...................................... | 1 |
| · Changed output accuracy bullet in Features .....................................................................................................1 |  |
| · Added Application Curves section....................................................................................................................16 |  |
| · Changed Available Options table..................................................................................................................... | 19 |
| Changes from Revision B (February 2023) to Revision C (April 2024) | Page |
| · Added KVU (TO-252) package to document as Advance Information ..............................................................1 |  |
| · Added KVU package information to Pin Configuration and Functions section...................................................3 |  |
| · Increased absolute maximum ratings to 20V for Input pin................................................................................. | 4 |
| · Added thermal numbers for KVU (TO-252) package......................................................................................... | 5 |
| · Changed output voltage value from 5 V to 3.3 V in Design Parameters table................................................. | 16 |
| · Added Layout Example for KVU (TO-252) Package image to Layout Examples section................................ | 18 |

## 10 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_051.png)

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| PTLV76118DCYR | Obsolete | Preproduction | SOT-223 (DCY) &#124; 4 | - | - | Call TI | Call TI | -40 to 125 |  |
| TLV76112DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76112C |
| TLV76112DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76112C |
| TLV76118DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76118C |
| TLV76118DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76118C |
| TLV76125DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76125C |
| TLV76125DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76125C |
| TLV76130DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76130C |
| TLV76130DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76130C |
| TLV76133DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76133C |
| TLV76133DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76133C |
| TLV76133KVUR | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76133 |
| TLV76133KVUR.A | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76133 |
| TLV76136DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76136C |
| TLV76136DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76136C |
| TLV76150DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76150C |
| TLV76150DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76150C |
| TLV76150KVUR | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76150 |
| TLV76150KVUR.A | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76150 |
| TLV76180DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76180C |
| TLV76180DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76180C |
| TLV761C0DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 761C0C |
| TLV761C0DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 761C0C |
| TLV761C0KVUR | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV761C0 |
| TLV761C0KVUR.A | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV761C0 |

(1) Status: For more details on status, see our product life cycle.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_052.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

7-Nov-2025

- (2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.
- (3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.
- (4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.
- (5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.
- (6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_053.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

4-Oct-2024

## TAPE AND REEL INFORMATION

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_054.png)

Reel Width (W1)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_055.png)

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| TLV76112DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76118DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76125DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76130DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76133DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76133KVUR | TO-252 | KVU | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| TLV76136DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76150DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76150KVUR | TO-252 | KVU | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| TLV76180DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV761C0DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV761C0KVUR | TO-252 | KVU | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |

## *All dimensions are nominal

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_056.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

4-Oct-2024

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_057.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| TLV76112DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76118DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76125DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76130DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76133DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76133KVUR | TO-252 | KVU | 3 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76136DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76150DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76150KVUR | TO-252 | KVU | 3 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76180DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV761C0DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV761C0KVUR | TO-252 | KVU | 3 | 2500 | 340.0 | 340.0 | 38.0 |

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_058.png)

SCALE 2. 0

## SOT-223 - 1.8 mm max height

PLASTIC SMALL OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_059.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Reference JEDEC TO-261.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_060.png)

PLASTIC SMALL OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_061.png)

NOTES: (continued)

4. Publication IPC-7351 may have alternate designs.
5. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_062.png)

## SOT-223 - 1.8 mm max height

PLASTIC SMALL OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_063.png)

SOLDER PASTE EXAMPLE BASED ON 0.125 mm THICK STENCIL SCALE:8X

4214843/C 05/2026

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_062.png)

TRANSISTOR OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_064.png)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_065.png)

INSTRUMENTS

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_066.png)

4

## PACKAGE OUTLINE

## TO-252 - 2.52 mm max height

SCALE 1.50

TO-252

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_067.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Shape may vary per different assembly sites.
4. Reference JEDEC registration TO-252.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_068.png)

## TO-252 - 2.52 mm max height

TO-252

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_069.png)

NOTES: (continued)

5. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature numbers SLMA002(www.ti.com/lit/slm002) and SLMA004 (www.ti.com/lit/slma004).
6. Vias are optional depending on application, refer to device data sheet. It is recommended that vias under paste be filled, plugged or tented.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_062.png)

## TO-252 - 2.52 mm max height

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_070.png)

NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

8. Board assembly site may have different recommendations for stencil design.

![Image](TLV761%20Datasheet%20%28TI%20SBVS349D%29%20-%20chosen_files/img_068.png)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2026, Texas Instruments Incorporated Last updated 10/2025
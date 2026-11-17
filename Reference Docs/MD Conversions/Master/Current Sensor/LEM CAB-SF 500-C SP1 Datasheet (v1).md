<!-- Converted from LEM CAB-SF 500-C SP1 Datasheet (v1).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_001.png)

## AUTOMOTIVE CURRENT TRANSDUCER FLUXGATE TECHNOLOGY

## CAB-SF 500-C/SP1-000; CAB-SF 500-C/SP1-001; CAB-SF 500-C/SP1-002; CAB-SF 500-C/SP1-003

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_002.png)

## Introduction

The CAB-SF family is the best suited for battery monitoring application where functional safety is required by keeping a high accuracy and very low offset.

It offers galvanic insulation between the primary circuit (high voltage) and the secondary circuit (12 V system).

## Features

- Transducer using Fluxgate technology
- Unlimited over-current capability
- Unipolar +12 V battery power supply
- Output signal: High speed CAN (500 kbps)
- Plug&amp;Play with standard CAB family
- Mating connector type: Tyco AMP 1473672-1.

## Special features

- Metallic insert in the ear
- Special CAN frame.

## Advantages

- Offset below 10 mA
- Total error [-40 °C to 85 °C] 0.5 % typical total error at 1-sigma 0.8 % total error at 3-sigma
- Full galvanic separation.

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_003.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_004.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_005.png)

## Automotive applications

- Hybrid and electric vehicle battery pack
- Conventional lead-acid batteries
- Accurate current measurement for battery management applications (SOC, SOH, SOF, etc…).

## Principle of Fluxgate Transducers

A low-frequency fluxgate transducer is made of a wound core which saturates under low induction.

A current chopper switches the winding's current to saturate the magnetic core alternatively at ±B max with a fixed frequency.

Fluxgate transducers use the change of the saturation's point symmetry to measure the primary current.

Due to the principle of switching the current, all offsets (electric and magnetic) are cancelled.

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_006.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_001.png)

## Dimensions CAB SF 500-C/SP1-xxx series (in mm)

## CAB-SF 500-C/SP1-xxx

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_007.png)

## Mechanical characteristics

- Plastic case
- Mass

PBT GF 30

67 g

## Mounting recommendation

- Connector type
- Assembly

Mating with Tyco-AMP P/N: 1 473672-1

M4 screw with 2 N·m ±5 %

## Marking

- DESIGNATION
- DATE CODE

CAB-SF 500-C/SP1-xxx

P = Production center ID

- 2D MATRIX

YY = Last two digit of the year

DDD = Day number of the year

CC = Machine ID

HH = Hour

MM = Minute

SS = Second

J = Machine jig ID

PYYDDDCCHHMMSSJ90.D9.50.0X1.0.

- Example

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_008.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_009.png)

## Absolute ratings (not operating)

## CAB-SF 500-C/SP1-xxx

| Parameter | Symbol | Unit | Specification | Conditions |
| - | - | - | - | - |
| Over-voltage | U C | V | 24 | 1 minute |
| Reverse polarity | U C | V | -14 | 1 minute |
| Minimum supply voltage | U C min | V | 6 | continuous, not measuring |
| Maximum supply voltage | U C max | V | 18 | continuous, not measuring |
| Ambient storage temperature | T A st | °C | -40/ +105 |  |
| Creepage distance | d Cp | mm | 7.2 |  |
| Clearance | d CI | mm | 6.95 |  |
| RMS voltage for AC insulation test | U d | kV | 2.5 | 50 Hz,1 min |
| Insulation resistance | R INS | MΩ | 500 | 500 V -ISO 16750-2 |
| IP Level |  |  | IP42 |  |

## Characteristics in nominal range

| Parameter | Symbol | Unit | Specification - Min | Specification - Typical | Specification - Max | Conditions |
| - | - | - | - | - | - | - |
| Electrical Data | Electrical Data | Electrical Data | Electrical Data | Electrical Data | Electrical Data | Electrical Data |
| Supply voltage | U C | V | 8.5 | 13.5 1) | 16 |  |
| Current consumption @ I P = 0 A | I C | mA |  | 30 | 40 | @U C = 13.5 V, CAN acknowledge |
| Current consumption @ ±I P = 500 A | I C | mA |  | 150 | 200 | @U C = 13.5 V, CAN acknowledge |
| Ambient operating temperature | T A | °C | -40 |  | 85 |  |
| Performance Data | Performance Data | Performance Data | Performance Data | Performance Data | Performance Data | Performance Data |
| Primary nominal DC or rms current | I P N | A | -500 |  | 500 |  |
| Current clamping value |  | A | -530 |  | 530 | For I p between -530 A and minus over current value For I p between +530 A and plus over current value |
| Output frequency of CAN signal 2) |  | Hz |  | 100 |  | Depends on the filter implemented |
| Start-up time |  | ms |  | 150 |  |  |
| Analog measurement Channel | Analog measurement Channel | Analog measurement Channel | Analog measurement Channel | Analog measurement Channel | Analog measurement Channel | Analog measurement Channel |
| Linearity error | ε L | % |  | ±0.1 |  | At room temperature |
| Output noise |  | mA |  | ±10 |  | With Periodic CAN meassage @ 10 ms Peak to peak value. No averaging. |
| Digital measurement channel 3) | Digital measurement channel 3) | Digital measurement channel 3) | Digital measurement channel 3) | Digital measurement channel 3) | Digital measurement channel 3) | Digital measurement channel 3) |
| Total error | ε tot | % |  | ±5 |  |  |

Notes: 1) For the classical 12 V Lead-acid battery system, the mean value of battery voltage becomes to 13.5 V during charging

2) Output frequency depends on the emission period of the frame without digital filter

3) Digital measurement is only for internal safety function.

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_010.png)

## Total Error Graph

Performances are considered with average value over 10 CAN frames (100 ms)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_011.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_012.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_013.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_014.png)

| I P (A) | Total error @ 25 °C (A) | Total error @ -40 °C to 85 °C (A) |
| - | - | - |
| -500 | ±2 | ±4 |
| 0 | ±0.01 | ±0.01 |
| 500 | ±2 | ±4 |

## CAB-SF 500-C/SP1-xxx

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_010.png)

## Typical noise shape at primary current = 0 A

## CAB-SF 500-C/SP1-xxx

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_015.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_016.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_017.png)

## Can output specification

- CAN protocol 2.0B
- Bit order: big endian (Motorola)
- CAN oscillator tolerance: 0.27 %
- No sleep mode capability
- 120 ohm termination resistor to be added externally, internal CAN impedance = 4.8 kohm.

| Message description | Products | CAN ID | Name | Data length (Nb bytes) | Type of frame | Message launch type | Signal name | Start bit | Length |
| - | - | - | - | - | - | - | - | - | - |
| Return Current I P (mA) | CAB-SF 500-C/SP1-000 | 0x3C0 | IP_000 | 8 | Standard | Cyclic message every 10 ms | SEQUENCE_COUNTER 1) | 0 | 8 |
| Return Current I P (mA) | CAB-SF 500-C/SP1-001 | 0x3C1 | IP_001 | 8 | Standard | Cyclic message every 10 ms | IP_VALUE 2) | 24 | 24 |
| Return Current I P (mA) | CAB-SF 500-C/SP1-002 | 0x3C2 | IP_002 | 8 | Standard | Cyclic message every 10 ms | ERROR_INFO 4) | 32 | 7 |
| Return Current I P (mA) | CAB-SF 500-C/SP1-003 | 0x3C3 | IP_003 | 8 | Standard | Cyclic message every 10 ms | ERROR_INDICATION 3) | 39 | 1 |
| Return Current I P (mA) |  |  |  | 8 | Standard | Cyclic message every 10 ms | SF_COUNTER 6) | 40 | 7 |
| Return Current I P (mA) |  |  |  | 8 | Standard | Cyclic message every 10 ms | ISO_WARNING 5) | 47 | 1 |
| Return Current I P (mA) |  |  |  | 8 | Standard | Cyclic message every 10 ms | SOFT_MINOR_REV 7) | 48 | 4 |
| Return Current I P (mA) |  |  |  | 8 | Standard | Cyclic message every 10 ms | SOFT_MAJOR_REV 8) | 52 | 4 |
| Return Current I P (mA) |  |  |  | 8 | Standard | Cyclic message every 10 ms | CRC 9) | 56 | 8 |
| UDS | CAB-SF 500-C/SP1-000 | 0x7E0 | UDS_CLIENT_000 | 8 |  |  |  |  |  |
| UDS |  | 0x7E8 | UDS_SERVER_000 | 8 |  |  |  |  |  |
| UDS | CAB-SF 500-C/SP1-001 | 0x7E1 | UDS_CLIENT_001 | 8 |  |  |  |  |  |
| UDS |  | 0x7E9 | UDS_SERVER_001 | 8 |  |  |  |  |  |
| UDS | CAB-SF 500-C/SP1-002 | 0x7E2 | UDS_CLIENT_002 | 8 |  |  |  |  |  |
| UDS |  | 0x7EA | UDS_SERVER_002 | 8 |  |  |  |  |  |
| UDS | CAB-SF 500-C/SP1-003 | 0x7E3 | UDS_CLIENT_003 | 8 |  |  |  |  |  |
| UDS |  | 0x7EB | UDS_SERVER_003 | 8 |  |  |  |  |  |

## Notes: CAB-SF 500/SP1-xxx I P \_xxx message description

- 1) 'SEQUENCE\_COUNTER' signal
- Initialized with 0 and incremented by 1 for every subsequent send request
- When the counter reaches the value 255 (0xFF), the restart with 1 for the next send request
- 2) 'I P\_ Value' signal ( Analog measurement of the primary current )
- Notes: Same behavior for negative currents.
- 3) 'ERROR\_INDICATION' signal
- When set to '1', the 'ERROR\_INFO' signal indicates the error code.

- 0 ≤ I P ≤ 520 A 'I P Value' signal follows the primary current value
- 520 A ≤ I P ≤ 530 A 'I P Value' signal clamped to 520 A
- I P ≥ 530 A 'I P Value' signal = 0xFFFFFF 'ERROR\_INDICATION' signal is set to '1'

'ERROR\_INFO' signal is set to 'Overcurrent detection' (0x41)

## CAB-SF 500-C/SP1-xxx

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_018.png)

## 4) 'ERROR\_INFO' signal

## CAB-SF 500-C/SP1-xxx

- In case of more than one error at the same time, the error with the highest priority is sent out. Priotity '1' means the highest priority.

| Priority | Failure mode | ERROR_INFO | Filter (1) | I P _VALUE' signal |
| - | - | - | - | - |
| 1 | Overcurrent Detection | 0x41 | No | 0xFFFFFF |
| 2 | Memory Error | 0x40 | No | 0xFFFFFF |
| 3 | Safety goal violation | 0x4C | 2/4 | I P current value |
| 4 | New Data not available | 0x49 | No | 0xFFFFFF |
| 5 | Fluxgate has no oscillation for more than 20 ms | 0x42 | No | 0xFFFFFF |
| 6 | Supply voltage is out of range | 0x46 | 2/4 | I P current value |
| 7 | Hardware default: ADC channel | 0x47 | 0.1/0.05 | 0xFFFFFF |
| 8 | Hardware default: Reference voltage | 0x4B | 2/4 | I P current value |
| 9 | Hardware default: DAC Threshold | 0x4A | 0.1/0.05 | I P current value |
| 10 | Temperature error | 0x44 | 0.1/0.05 | I P current value |

(1) x/y : Error should be active for 'x' seconds to set the 'ERROR\_INFO' signal. 'y' seconds to clear the signal.

## 5) 'ISO\_WARNING' signal

- Indicates that the absolute difference between the analog and digital measurement is below / higher than 7 %
- Filtering: The Signal is set to be '1' when the difference is above 7 % for at least 2 seconds. The signal is reset when the difference is below 7 % for at least 4 seconds.

## 6) 'SF\_COUNTER' signal

- The 'Safety goal violation' error (ERROR\_INFO = 0x4C) indicates that the absolute difference between the analog and digital measurement is below / higher than 20 %
- Filtering: The Signal 'ERROR\_INFO ' is set to be 'Safety goal violation' error when the difference is above 20 % for at least 2 seconds. The error is reset when difference is below 20 % for at least 4 seconds. The 'SF\_COUNTER' signal shows the progression of the filtering. 'Safety goal violation' error is set when the 'SF\_COUNTER' signal reaches 100. The 'Safety goal violation' error is reset when 'SF\_COUNTER' signal goes below 50.
- 7) 'SOFT\_MAJOR\_REV' signal
- 8) 'SOFT\_MINOR\_REV' signal
- Information about software release
- 9) 'CRC' signal
- 8-bit SAE J1850 CRC calculation of the first seven bytes.

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_019.png)

## SAFETY GOALS for CAB-SF 500-C

CAB-SF 500-C/SP1-xxx

An hazard analysis was performed for the CAB-SF 500-C sensor. A list of hazard events have been identified and an ISO26262 rating has been made for each of them. The highest quotation for which the product meets is ASILB level.The electronic design followed the guidelines and development methods recommended by ISO26262.

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_018.png)

## Applicable standards

## CAB-SF 500-C/SP1-xxx

| Test | Standard | Procedure |
| - | - | - |
| Environmental test | Environmental test | Environmental test |
| Low Temperature Operating Endurance | ISO 16750-4 (04/2010) | 120 hrs, -40 °C, power on |
| High Temperature Operating Endurance | ISO 16750-4 (04/2010) | 85 °C, 120 hrs, power on |
| Powered Thermal Cycle Endurance | ISO16750-4 (04/2010) | -40 °C (20 min soak) / +85 °C (20 min soak), slope 4 °C/min, 540 cycles (936 h, 39 days), power supply 13.5 V |
| Thermal Shock | ISO 16750-4 (04/2010) | -40 °C (20 min soak) / +85 °C (20 min soak), 1000 cycles (667 h, 28 days); no power supply |
| High Temperature and Humidity Endurance | JESD 22-A101 (03/2009) | 85 °C, 85 % humidity, 1000 hrs |
| Random Vibration | ISO 16750-3 (12/2012) | Test IV, -40 °C / + 85 °C during 8 hours (Fig.1), RMS acceleration 27.1 m/s 2 , 20 h/axis, 3 axis+, power on and output monitoring |
| Mechanical Shocks | ISO 16750-3 (12/2012) | 500 m/s 2 , 10 each direction (60 total), Half sine pulse |
| Free Fall | ISO 16750-3 (12/2012) | 2 falls per DUT, 3 axis, total 6 falls, from 1 meter on concrete floor |
| Water Intrusion | DIN 40050-9 (1993-05) | IPx2, flow 3 (+0.5/0) mm/min, 10 mins, connector downward, parts inclined at 15° |
| Dust (and other solid intrusion) | DIN 40050-9 (1993-05) | IP4x, The rigid stem, 1 mm diameter, is pressed against the casing of the part with a 1N force Vertical flow chamber, Portland cement, 2 kg/m^3, 6 s ON/15 min OFF for 20 cycles, parts inclined at 15° |
| Mixed Flowing Gas | IEC60068-2-60 (12/1996) | Mehod4 in Table1, H2S, NO2, Cl2, SO2, 25 ±1 °C, RH 75 ±3 %, 21 days |
| Salt Fog | NISSAN M0158 (2009) / M0140 (2014) | NaCl 50 g/L, Cycle: salt spray 4 hrs, dry 2 hrs with 60 °C < 30 % RH, moistening 2 hrs with 50 °C 95 % RH, 110 cycles |
| EMC test | EMC test | EMC test |
| Conduted emission- Voltage method | CISPR 25 (03/2008) | 150 kHz-108 MHz Class 4 (LW,VHF (68-87 MHz),FM); Class 3 (MW,SW,CB); Class 2 (VF (30-54 MHz)) |
| Conducted emission- Current method | CISPR 25 (03/2008) | 150 kHz -245 MHz Class 4 ( only for LW, FM); Class 3 (Rest frequency) |
| Radio frequency radiated Emission electric field | CISPR 25 (04/2016) | Class 5 (FM); Class 4 (LW,VHF (68-87 MHz),GSM, EGSM/GSM 900); Class 2 (VHF (30-54 MHz),VHF (142-175 MHz)) ; Class 3 (Rest frequency) |
| IMMUNITY TO CURRENT INJECTION (BCI) | ISO 11452-4 (12/2011) | 1 MHz to 400 MHz Level 1 100 mA: Class A; Level 2 200 mA: Class C; Level 3 300 mA: Class C |
| Immunity to Radiated field- Anechoic chamber(ALSE with ground plane) | ISO 11452-2 | 200 MHz-3.2 GHz; 150 V/m Class A |
| RESISTANCE TO PULSES 1, 2A,2B (Transient Disturbance conducted along supply line) | ISO-7637-2 (03/2011) | pulse 1, pulse 2a 500 pulses; pulse 2b 10 pulses Class C |
| Resistance to pulses 3a & 3b (Transient Disturbance conducted along supply line) | ISO-7637-2 (03/2011) | pulse 3a, pulse 3b time duration = 1 hour Class A |

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_020.png)

## CAB-SF 500-C/SP1-xxx

| Resistance to pulses 4 (Starting profile) | ISO 16750-2 § 4.6.3 (11/2012) | pulse 4 10 pulses Test level I: Class A; Test level II: Class C; Test level III: Class C |
| - | - | - |
| Load Dump | ISO 16750-2 § 4.6.4.2.3 | U A = 14 V, U S * = 29 V, R I < 1 ohm t D = 400 ms 5 pulses Class C |
| Transient disturbance conducted along i/o or sensor lines | ISO-7637-3 (07/2007) | Fast pulse a: CCC Fast pulse b: CCC Slow pulse +: DCC Slow pulse -: DCC level IV Class A |
| RESISTANCE TO ELECTROSTATIC DISCHARGES, EQUIPMENT NOT CONNECTED (handling) | ISO 10605 IEC 61000-4-2 (2008) | UN-powered ±2 kV ±4 kV air: ±8 kV ±15 kV |
| ESD Operating | ISO 10605 IEC 61000-4-2 (2008) | Powered indirect contact discharge: ±4 kV air: ±8 kV |

## Electrical test

| Direct current supply voltage | ISO 16750-2 § 4.2 (11/2012) | Code B |
| - | - | - |
| Overvoltage | ISO 16750-2 § 4.3.1 (11/2012) | 18 V, 1 h, @ 65 °C ; 24 V, 1 min, @ 25 °C |
| Superimposed Alternating Voltage | ISO 16750-2 § 4.4 (11/2012) | -severity 2: Upp = 4 V -severity 4: Upp = 2 V |
| Resistance to slow decrease and increase of supply voltage | ISO 16750-2 § 4.5 (11/2012) | Umin = 8 V, 0.5 V/min, Run DUT 10 min |
| Momentary drop in supply voltage | ISO 16750-2 § 4.6.1 (11/2012) | Room temperature, US min to 4.5 V |
| Re-initialization test (Reset behaviour at voltage drop) | ISO 16750-2 § 4.6.2 (11/2012) | US min = 8 V |
| Reverse voltage | ISO 16750-2 § 4.7 (11/2012) | Case 2 |
| Ground reference and supply voltage | ISO 16750-2 § 4.8 (11/2012) | Offset voltage = 1.0 ±0.1 V |
| Open Circuit | ISO 16750-2 § 4.9 (11/2012) | Single line / Multiple line interruption |
| Short circuit protection | ISO 16750-2 § 4.10.2 (11/2012) | Signal circuits, US max = 16 V and GND, duration 60 s |
| RESISTANCE TO SHORT INTERRUPTION OF THE POWER SUPPLY | PSA B217110 E § 7.1.13 no reference | US = 14 V, t D = 2 μs,1 ms,5 ms |
| resistance to "volt control" voltage pulse | PSA B217110 E § 7.1.16 no reference | U 1 = 15.2 V; U 2 = 18.0 V; t r = 1 ms; t f = 300 ms 5 pulse with an interval of 1 min |
| resistance to supply voltage in the usual "volt control" range | PSA B217110 E § 7.1.2 no reference | Umin = 10.5 V; Umax = 16 V; t D = 5 s; R r = 10 V/s 5 pulse with an interval of 1 min |

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_018.png)

## Installation influence

## Overview

The CAB 500-C family uses a very accurate technology and offers the customers the current measurement needed to the application. In order to respect this accuracy, some conditions must be respected during the design of the environment of the sensor:

- Primary busbar centering
- Busbar shape
- Contactors position

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_021.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_022.png)

The busbar dimension for test: 20 mm(W)x3 mm(H). 20 mm (W) x 3 mm (H)

Environment: room temperature.

It can be reference during BDU design, but the performance validation of BDU is necessary.

## Return busbar type definition

Explanation: Recommended / Case of accuracy close to the limit / Not recommended

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_023.png)

## CAB-SF 500-C/SP1-xxx

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_024.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_025.png)

Due to the complexity of practical application, the examples cannot cover all the application conditions.

The sensor has different performance on different angles. For details or any further questions, please contact LEM Technical Customer Support.

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_026.png)

## U1-shape busbar recommendation

## CAB-SF 500-C/SP1-xxx

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_027.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_028.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_029.png)

## U2-shape busbar recommendation

60mm

b

B

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_030.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_031.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_032.png)

A

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_033.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_034.png)

## U3-shape busbar recommendation

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_035.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_036.png)

A

D

A

D

C

B

B

b(mm)

a(mm)

20

30

40

50

60

70

A B A B A B A B A B

C D C D C D C D C D

80

A B A B A B A B A B

C D C D C D C D C D

90

A B A B A B A B A B

C D C D C D C D C D

100

A B A B A B A B A B

C D C D C D C D C D

b(mm)

a(mm)

20

30

40

50

60

70

A

B

A

B

A

B

A

B

A

B

C D C D C D C D C D

80

A

B

A

B

A

B

A

B

A

B

C D C D C D C D C D

90

A

B

A

B

A

B

A

B

A

B

C D C D C D C D C D

100

A

B

A

B

A

B

A

B

A

B

C D C D C D C D C D

## U4-shape busbar recommendation

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_037.png)

A

D

B

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_038.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_039.png)

![Image](LEM%20CAB-SF%20500-C%20SP1%20Datasheet%20%28v1%29_files/img_040.png)

b(mm)

a(mm)

20

30

40

50

70

A B

A B

A B

A

B

C D C D C D C D

80

A B

A B

A B

A

B

C D C D C D C D

90

A B

A B

A B

A

B

C D C D C D C D

100

A B

A B

A B

A

B

C D C D C D C D

in order to improve them, without prior notice.
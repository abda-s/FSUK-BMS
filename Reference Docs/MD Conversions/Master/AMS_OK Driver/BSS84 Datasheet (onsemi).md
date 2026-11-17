<!-- Converted from BSS84 Datasheet (onsemi).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_001.png)

## onsemi.

## P-Channel Enhancement Mode Field-Effect Transistor

## BSS84

## General Description

This P-channel enhancement-mode field-effect transistor is produced using onsemi's proprietary, high cell density, DMOS technology. This very high density process minimizes on-state resistance and to provide rugged and reliable performance and fast switching. The BSS84 can be used, with a minimum of effort, in most applications requiring up to 0.13 A DC and can deliver current up to 0.52 A. This product is particularly suited to low-voltage applications requiring a low-current high-side switch.

## Features

- -0.13 A, -50 V, RDS(on) = 10 W at VGS = -5 V
- Voltage-Controlled P-Channel Small-Signal Switch
- High-Density Cell Design for Low RDS(on)
- High Saturation Current
- This Device is Pb-Free and Halogen Free

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_002.png)

SOT-23-3 CASE 318-08

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_003.png)

## MARKING DIAGRAM

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_004.png)

SP = Specific Device Code

M = Date Code*

- Γ = Pb-Free Package

(Note: Microdot may be in either location)

*Date Code orientation and/or position may vary depending upon manufacturing location.

## ORDERING INFORMATION

| Device | Package | Shipping † |
| - | - | - |
| BSS84, BSS84-G | SOT-23-3 (Pb-Free) | 3000 / Tape & Reel |

†For information on tape and reel specifications, including part orientation and tape sizes, please refer to our Tape and Reel Packaging Specification Brochure, BRD8011/D.

## BSS84

## ABSOLUTE MAXIMUM RATINGS TA = 25°C unless otherwise noted.

| Symbol | Parameter | Ratings | Unit |
| - | - | - | - |
| VDSS | Drain-Source Voltage | -50 | V |
| VGSS | Gate-Source Voltage | ±20 | V |
| ID | Drain Current - Continuous (Note 1) | -0.13 | A |
| ID | Drain Current - Pulsed (Note 1) | -0.52 | A |
| PD | Maximum Power Dissipation (Note 1) | 0.36 | W |
| PD | Derate Above 25°C | 2.9 | mW/°C |
| TJ, TSTG | Operating and Storage Junction Temperature Range | -55 to +150 | °C |
| TL | Maximum Lead Temperature for Soldering Purposes, 1/16" from Case for 10 s | 300 | °C |

Stresses exceeding those listed in the Maximum Ratings table may damage the device. If any of these limits are exceeded, device functionality should not be assumed, damage may occur and reliability may be affected.

## THERMAL CHARACTERISTICS TA = 25°C unless otherwise noted.

| Symbol | Parameter | Ratings | Unit |
| - | - | - | - |
| RqJA | Thermal Resistance, Junction-to-Ambient (Note 1) | 350 | °C/W |

## ELECTRICAL CHARACTERISTICS (Note 2) TA = 25°C unless otherwise noted.

| Symbol | Parameter | Test Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - |

## OFF CHARACTERISTICS

| BVDSS | Drain-Source Breakdown Voltage | VGS = 0 V, ID = -250 mA | -50 | - | - | V |
| - | - | - | - | - | - | - |
| DBV DSS DT J | Breakdown Voltage Temperature Coefficient | ID = -250 μA, Referenced to 25°C | - | -48 | - | mV/°C |
| IDSS | Zero Gate Voltage Drain Current | VDS = -50 V, VGS = 0 V | - | - | -15 | mA |
|  |  | VDS = -50 V, VGS = 0 V, TJ = 125°C | - | - | -60 |  |
| IGSS | Gate-Body Leakage | VGS = ±20 V, VDS = 0 V | - | - | ±10 | nA |

## ON CHARACTERISTICS (Note 2)

| VGS(th) | Gate Threshold Voltage | VDS = VGS, ID = -1 mA | -0.8 | -1.7 | -2 | V |
| - | - | - | - | - | - | - |
| DV GS(th) DT J | Gate Threshold Voltage Temperature Coefficient | ID = -1 mA, Referenced to 25°C | - | 3 | - | mV/°C |
| RDS(on) | Static Drain-Source On-Resistance | VGS = -5 V, ID = -0.10 A | - | 1.2 | 10 | W |
| RDS(on) |  | VGS = -5 V, ID = -0.10 A, TJ = 125°C | - | 1.9 | 17 |  |
| ID(on) | On-State Drain Current | VGS = -5 V, VDS = -10 V | -0.6 | - | - | A |
| gFS | Forward Transconductance | VDS = -25 V, ID = -0.10 A | 0.05 | 0.6 | - | S |

## DYNAMIC CHARACTERISTICS

| Ciss | Input Capacitance | VDS = -25 V, VGS = 0 V, f = 1.0 MHz | - | 73 | - | pF |
| - | - | - | - | - | - | - |
| Coss | Output Capacitance | VDS = -25 V, VGS = 0 V, f = 1.0 MHz | - | 10 | - | pF |
| Crss | Reverse Transfer Capacitance | VDS = -25 V, VGS = 0 V, f = 1.0 MHz | - | 5 | - | pF |
| RG | Gate Resistance | VGS = 15 mV, f = 1.0 MHz | - | 9 | - | W |

ELECTRICAL CHARACTERISTICS (Note 2) TA = 25°C unless otherwise noted. (continued)

| Symbol | Parameter | Test Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - |
| SWITCHING CHARACTERISTICS (Note 2) | SWITCHING CHARACTERISTICS (Note 2) | SWITCHING CHARACTERISTICS (Note 2) | SWITCHING CHARACTERISTICS (Note 2) | SWITCHING CHARACTERISTICS (Note 2) | SWITCHING CHARACTERISTICS (Note 2) | SWITCHING CHARACTERISTICS (Note 2) |
| td(on) | Turn-On Delay Time | VDD = -30 V, ID = -0.27 A, VGS = -10 V, RGEN = 6 W | - | 2.5 | 5.0 | ns |
| tr | Turn-On Rise Time | VDD = -30 V, ID = -0.27 A, VGS = -10 V, RGEN = 6 W | - | 6.3 | 13 | ns |
| td(off) | Turn-Off Delay Time | VDD = -30 V, ID = -0.27 A, VGS = -10 V, RGEN = 6 W | - | 10 | 20 | ns |
| tf | Turn-Off Fall Time | VDD = -30 V, ID = -0.27 A, VGS = -10 V, RGEN = 6 W | - | 4.8 | 9.6 | ns |
| Qg | Total Gate Charge | VDS = -25 V, ID = -0.10 A, VGS = -5 V | - | 0.9 | 1.3 | nC |
| Qgs | Gate-Source Charge | VDS = -25 V, ID = -0.10 A, VGS = -5 V | - | 0.2 | - | nC |
| Qgd | Gate-Drain Charge | VDS = -25 V, ID = -0.10 A, VGS = -5 V | - | 0.3 | - | nC |

## DRAIN-SOURCE DIODE CHARACTERISTICS AND MAXIMUM RATINGS

| IS | Maximum Continuous Drain-Source Diode Forward Current | Maximum Continuous Drain-Source Diode Forward Current | - | - | -0.13 | A |
| - | - | - | - | - | - | - |
| VSD | Drain-Source Diode Forward Voltage | VGS = 0 V, IS = -0.26 A (Note 2) | - | -0.8 | -1.2 | V |
| trr | Diode Reverse Recovery Time | IF = -0.1 A, dif/dt = 100 A/ms (Note 2) | - | 10 | - | ns |
| Qrr | Diode Reverse Recovery Charge | IF = -0.1 A, dif/dt = 100 A/ms (Note 2) | - | 3 | - | nC |

Product parametric performance is indicated in the Electrical Characteristics for the listed test conditions, unless otherwise noted. Product performance may not be indicated by the Electrical Characteristics if operated under different conditions.

1. RqJA is the sum of the junction-to-case and case-to-ambient thermal resistance where the case thermal reference is defined as the solder mounting surface of the drain pins. RqJA is guaranteed by design while RqJA is determined by the user's board design.

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_005.png)

a) 350°C/W when mounted on a minimum pad.

2. Pulse Test: Pulse Width ≤ 300 ms, Duty Cycle ≤ 2.0%

## TYPICAL CHARACTERISTICS

Figure 1. On-Region Characteristics

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_006.png)

Figure 2. On-Resistance Variation with Drain Current and Gate Voltage

1

BSS84

## TYPICAL CHARACTERISTICS (continued)

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_007.png)

## BSS84

## TYPICAL CHARACTERISTICS (continued)

Figure 9. Maximum Safe Operating Area

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_008.png)

Figure 10. Single Pulse Maximum Power Dissipation

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_009.png)

Figure 11. Transient Thermal Response Curve

Thermal characterization performed using the conditions described in Note 1a. Transient thermal response will change depending on the circuit board design.

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_010.png)

| DIM | MILLIMETERS - MIN | MILLIMETERS - NOM | MILLIMETERS - MAX | INCHES - MIN | INCHES - NOM | INCHES - MAX |
| - | - | - | - | - | - | - |
| A | 0.89 | 1.00 | 1.11 | 0.035 | 0.039 | 0.044 |
| A1 | 0.01 | 0.06 | 0.10 | 0.000 | 0.002 | 0.004 |
| b | 0.37 | 0.44 | 0.50 | 0.015 | 0.017 | 0.020 |
| c | 0.08 | 0.14 | 0.20 | 0.003 | 0.006 | 0.008 |
| D | 2.80 | 2.90 | 3.04 | 0.110 | 0.114 | 0.120 |
| E | 1.20 | 1.30 | 1.40 | 0.047 | 0.051 | 0.055 |
| e | 1.78 | 1.90 | 2.04 | 0.070 | 0.075 | 0.080 |
| L | 0.30 | 0.43 | 0.55 | 0.012 | 0.017 | 0.022 |
| L1 | 0.35 | 0.54 | 0.69 | 0.014 | 0.021 | 0.027 |
| HE | 2.10 | 2.40 | 2.64 | 0.083 | 0.094 | 0.104 |
| T | 0 ° | --- | 10 ° | 0 ° | --- | 10 ° |

| DOCUMENT NUMBER: | 98ASB42226B | Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped "CONTROLLED COPY" in red. | Electronic versions are uncontrolled except when accessed directly from the Document Repository. Printed versions are uncontrolled except when stamped "CONTROLLED COPY" in red. |
| - | - | - | - |
| DESCRIPTION: | SOT-23 (TO-236) |  | PAGE 1 OF 1 |

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_011.png)

![Image](BSS84%20Datasheet%20%28onsemi%29_files/img_012.png)

ON Semiconductor and are trademarks of Semiconductor Components Industries, LLC dba ON Semiconductor or its subsidiaries in the United States and/or other countries. ON Semiconductor reserves the right to make changes without further notice to any products herein. ON Semiconductor makes no warranty, representation or guarantee regarding the suitability of its products for any particular purpose, nor does ON Semiconductor assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation special, consequential or incidental damages. ON Semiconductor does not convey any license under its patent rights nor the rights of others.

onsemi, , and other names, marks, and brands are registered and/or common law trademarks of Semiconductor Components Industries, LLC dba "onsemi" or its affiliates and/or subsidiaries in the United States and/or other countries. onsemi owns the rights to a number of patents, trademarks, copyrights, trade secrets, and other intellectual property. A listing of onsemi's product/patent coverage may be accessed at www.onsemi.com/site/pdf/Patent-Marking.pdf. onsemi reserves the right to make changes at any time to any products or information herein, without notice. The information herein is provided "as-is" and onsemi makes no warranty, representation or guarantee regarding the accuracy of the information, product features, availability, functionality, or suitability of its products for any particular purpose, nor does onsemi assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any and all liability, including without limitation special, consequential or incidental damages. Buyer is responsible for its products and applications using onsemi products, including compliance with all laws, regulations and safety requirements or standards, regardless of any support or applications information provided by onsemi. "Typical" parameters which may be provided in onsemi data sheets and/or specifications can and do vary in different applications and actual performance may vary over time. All operating parameters, including "Typicals" must be validated for each customer application by customer's technical experts. onsemi does not convey any license under any of its intellectual property rights nor the rights of others. onsemi products are not designed, intended, or authorized for use as a critical component in life support systems or any FDA Class 3 medical devices or medical devices with a same or similar classification in a foreign jurisdiction or any devices intended for implantation in the human body. Should Buyer purchase or use onsemi products for any such unintended or unauthorized application, Buyer shall indemnify and hold onsemi and its officers, employees, subsidiaries, affiliates, and distributors harmless against all claims, costs, damages, and expenses, and reasonable attorney fees arising out of, directly or indirectly, any claim of personal injury or death associated with such unintended or unauthorized use, even if such claim alleges that onsemi was negligent regarding the design or manufacture of the part. onsemi is an Equal Opportunity/Affirmative Action Employer. This literature is subject to all applicable copyright laws and is not for resale in any manner.

## PUBLICATION ORDERING INFORMATION

LITERATURE FULFILLMENT:

Email Requests to: orderlit@onsemi.com TECHNICAL SUPPORT

North American Technical Support:

Voice Mail: 1 800-282-9855 Toll Free USA/Canada

Phone: 011 421 33 790 2910

Europe, Middle East and Africa Technical Support:

For additional information, please contact your local Sales Representative
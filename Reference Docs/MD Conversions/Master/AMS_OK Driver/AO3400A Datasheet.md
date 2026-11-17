<!-- Converted from AO3400A Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](AO3400A%20Datasheet_files/img_001.png)

## General Description

## AO3400A 30V N-Channel MOSFET

## Product Summary

The AO3400A combines advanced trench MOSFET technology with a low resistance package to provide extremely low RDS(ON). This device is suitable for use as a load switch or in PWM applications.

SOT23

Top View Bottom View

![Image](AO3400A%20Datasheet_files/img_002.png)

## Absolute Maximum Ratings TA=25°C unless otherwise noted

![Image](AO3400A%20Datasheet_files/img_003.png)

| Parameter | Parameter | Symbol | Maximum | Units |
| - | - | - | - | - |
| Drain-Source Voltage | Drain-Source Voltage | VDS | 30 | V |
| Gate-Source Voltage | Gate-Source Voltage | VGS | ±12 | V |
|  | TA=25°C Continuous Drain | ID | 5.7 | A |
|  | TA=70°C Current | ID | 4.7 | A |
| Pulsed Drain Current C | Pulsed Drain Current C | IDM | 30 | A |
|  | TA=25°C | PD | 1.4 | W |
|  | TA=70°C Power Dissipation B | PD | 0.9 | W |
| Junction and Storage Temperature | Range | TJ, TSTG | -55 to 150 | °C |

| Thermal Characteristics Parameter | Thermal Characteristics Parameter | Symbol | Typ | Max | Units |
| - | - | - | - | - | - |
| Maximum Junction-to-Ambient A | t ≤ 10s | RqJA | 70 | 90 | °C/W |
| Maximum Junction-to-Ambient A D | Steady-State | RqJA | 100 | 125 | °C/W |
| Maximum Junction-to-Lead | Steady-State | RqJL | 63 | 80 | °C/W |

VDS

ID (at VGS=10V)

30V

5.7A

RDS(ON) (at VGS=10V)

&lt; 26.5mW

RDS(ON) (at VGS = 4.5V)

&lt; 32mW

RDS(ON) (at VGS = 2.5V)

&lt; 48mW

![Image](AO3400A%20Datasheet_files/img_004.png)

![Image](AO3400A%20Datasheet_files/img_005.png)

## Electrical Characteristics (TJ=25°C unless otherwise noted)

| Symbol | Parameter | Conditions | Min | Typ | Max | Units |
| - | - | - | - | - | - | - |
| STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS |
| BVDSS | Drain-Source Breakdown Voltage | ID=250mA, VGS=0V | 30 |  |  | V |
| IDSS | Zero Gate Voltage Drain Current | VDS=30V, VGS=0V |  |  | 1 | mA |
|  |  | VDS=30V, VGS=0V | TJ=55°C |  | 5 |  |
| IGSS | Gate-Body leakage current | VDS=0V, VGS= ±12V |  |  | 100 | nA |
| VGS(th) | Gate Threshold Voltage | VDS=VGS ID=250mA | 0.65 | 1.05 | 1.45 | V |
| ID(ON) | On state drain current | VGS=4.5V, VDS=5V | 30 |  |  | A |
| RDS(ON) | Static Drain-Source On-Resistance | VGS=10V, ID=5.7A |  | 18 | 26.5 | mW |
|  | Static Drain-Source On-Resistance | VGS=10V, ID=5.7A | TJ=125°C | 28 | 38 | mW |
|  |  | VGS=4.5V, ID=5A |  | 19 | 32 | mW |
|  |  | VGS=2.5V, ID=3A |  | 24 | 48 | mW |
| gFS | Forward Transconductance | VDS=5V, ID=5.7A |  | 33 |  | S |
| VSD | Diode Forward Voltage | IS=1A,VGS=0V |  | 0.7 | 1 | V |
| IS | Maximum Body-Diode Continuous Current | Maximum Body-Diode Continuous Current |  |  | 2 | A |
| DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS |
| Ciss | Input Capacitance | VGS=0V, VDS=15V, f=1MHz |  | 630 |  | pF |
| Coss | Output Capacitance | VGS=0V, VDS=15V, f=1MHz |  | 75 |  | pF |
| Crss | Reverse Transfer Capacitance | VGS=0V, VDS=15V, f=1MHz |  | 50 |  | pF |
| Rg | Gate resistance | VGS=0V, VDS=0V, f=1MHz | 1.5 | 3 | 4.5 | W |
| SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS |
| Qg | Total Gate Charge | VGS=4.5V, VDS=15V, ID=5.7A |  | 6 | 7 | nC |
| Qgs | Gate Source Charge | VGS=4.5V, VDS=15V, ID=5.7A |  | 1.3 |  | nC |
| Qgd | Gate Drain Charge | VGS=4.5V, VDS=15V, ID=5.7A |  | 1.8 |  | nC |
| tD(on) | Turn-On DelayTime | VGS=10V, VDS=15V, RL=2.6W, RGEN=3W |  | 3 |  | ns |
| tr | Turn-On Rise Time | VGS=10V, VDS=15V, RL=2.6W, RGEN=3W |  | 2.5 |  | ns |
| tD(off) | Turn-Off DelayTime | VGS=10V, VDS=15V, RL=2.6W, RGEN=3W |  | 25 |  | ns |
| tf | Turn-Off Fall Time | VGS=10V, VDS=15V, RL=2.6W, RGEN=3W |  | 4 |  | ns |
| trr | Body Diode Reverse Recovery Time | IF=5.7A, dI/dt=100A/ms |  | 8.5 |  | ns |
| Qrr | Body Diode Reverse Recovery Charge | IF=5.7A, dI/dt=100A/ms |  | 2.6 |  | nC |

A. The value of RqJA is measured with the device mounted on 1in 2 FR-4 board with 2oz. Copper, in a still air environment with T A =25°C. The value in any given application depends on the user's specific board design.

- B. The power dissipation P D is based on T J(MAX) =150°C, using ≤10s junction-to-ambient thermal resistance.
- C. Repetitive rating, pulse width limited by junction temperature T J(MAX) =150°C. Ratings are based on low frequency and duty cycles to keep initialT J =25°C.
- D. The RqJA is the sum of the thermal impedence from junction to lead RqJL and lead to ambient.
- E. The static characteristics in Figures 1 to 6 are obtained using &lt;300ms pulses, duty cycle 0.5% max.
- F. These curves are based on the junction-to-ambient thermal impedence which is measured with the device mounted on 1in 2 FR-4 board with 2oz. Copper, assuming a maximum junction temperature of T J(MAX) =150°C. The SOA curve provides a single pulse rating.

APPLICATIONS OR USES AS CRITICAL COMPONENTS IN LIFE SUPPORT DEVICES OR SYSTEMS ARE NOT AUTHORIZED. AOS DOES NOT ASSUME ANY LIABILITY ARISING OUT OF SUCH APPLICATIONS OR USES OF ITS PRODUCTS. AOS RESERVES THE RIGHT TO MAKE CHANGES TO PRODUCT SPECIFICATIONS WITHOUT NOTICE. IT IS THE RESPONSIBILITY OF THE CUSTOMER TO EVALUATE SUITABILITY OF THE PRODUCT FOR THEIR INTENDED APPLICATION. CUSTOMER SHALL COMPLY WITH APPLICABLE LEGAL REQUIREMENTS, INCLUDING ALL APPLICABLE EXPORT CONTROL RULES, REGULATIONS AND LIMITATIONS.

AOS' products are provided subject to AOS' terms and conditions of sale which are set forth at: http://www.aosmd.com/terms\_and\_conditions\_of\_sale

![Image](AO3400A%20Datasheet_files/img_006.png)

## TYPICAL ELECTRICAL AND THERMAL CHARACTERISTICS

V DS (Volts) Fig 1: On-Region Characteristics (Note E)

![Image](AO3400A%20Datasheet_files/img_007.png)

![Image](AO3400A%20Datasheet_files/img_008.png)

I D (A)

Figure 3: On-Resistance vs. Drain Current and Gate Voltage (Note E)

![Image](AO3400A%20Datasheet_files/img_009.png)

V GS (Volts) Figure 2: Transfer Characteristics (Note E)

![Image](AO3400A%20Datasheet_files/img_010.png)

0 18 Temperature (°C) Figure 4: On-Resistance vs. Junction Temperature (Note E)

![Image](AO3400A%20Datasheet_files/img_011.png)

![Image](AO3400A%20Datasheet_files/img_012.png)

![Image](AO3400A%20Datasheet_files/img_006.png)

## TYPICAL ELECTRICAL AND THERMAL CHARACTERISTICS

Figure 11: Normalized Maximum Transient Thermal Impedance (Note F)

![Image](AO3400A%20Datasheet_files/img_013.png)

![Image](AO3400A%20Datasheet_files/img_014.png)

## Gate Charge Test Circuit &amp; Waveform

![Image](AO3400A%20Datasheet_files/img_015.png)

![Image](AO3400A%20Datasheet_files/img_016.png)

Resistive Switching Test Circuit &amp; Waveforms

![Image](AO3400A%20Datasheet_files/img_017.png)

![Image](AO3400A%20Datasheet_files/img_018.png)

![Image](AO3400A%20Datasheet_files/img_019.png)

Diode Recovery Test Circuit &amp; Waveforms

![Image](AO3400A%20Datasheet_files/img_020.png)
<!-- Converted from AO3401A Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](AO3401A%20Datasheet_files/img_001.png)

## General Description

## AO3401A 30V P-Channel MOSFET

## Product Summary

The AO3401A uses advanced trench technology to provide excellent RDS(ON) , low gate charge and operation gate voltages as low as 2.5V. This device is suitable for use as a load switch or other general applications.

SOT23 Top View Bottom View

![Image](AO3401A%20Datasheet_files/img_002.png)

## Absolute Maximum Ratings TA=25°C unless otherwise noted

![Image](AO3401A%20Datasheet_files/img_003.png)

| Parameter | Parameter | Symbol | Maximum | Units |
| - | - | - | - | - |
| Drain-Source Voltage | Drain-Source Voltage | VDS | -30 | V |
| Gate-Source Voltage | Gate-Source Voltage | VGS | ±12 | V |
| Continuous Drain Current | TA=25°C | ID | -4 | A |
| Continuous Drain Current | TA=70°C | ID | -3.2 | A |
| Pulsed Drain Current C | Pulsed Drain Current C | IDM | -27 | A |
|  | TA=25°C | PD | 1.4 | W |
|  | Power Dissipation B TA=70°C | PD | 0.9 | W |
| Junction and Storage Temperature Range | Junction and Storage Temperature Range | TJ, TSTG | -55 to 150 | °C |

| Thermal Characteristics - Parameter | Thermal Characteristics - Parameter | Thermal Characteristics - Symbol | Thermal Characteristics - Typ | Thermal Characteristics - Max | Thermal Characteristics - Units |
| - | - | - | - | - | - |
| Maximum Junction-to-Ambient A | t ≤ 10s | RqJA | 70 | 90 | °C/W |
| Maximum Junction-to-Ambient A D | Steady-State | RqJA | 100 | 125 | °C/W |
| Maximum Junction-to-Lead | Steady-State | RqJL | 63 | 80 | °C/W |

VDS

ID (at VGS=-10V)

- -30V
- -4.0A

RDS(ON) (at VGS=-10V)

- &lt; 50mW

RDS(ON) (at VGS =-4.5V)

- &lt; 60mW

RDS(ON) (at VGS=-2.5V)

- &lt; 85mW

![Image](AO3401A%20Datasheet_files/img_004.png)

![Image](AO3401A%20Datasheet_files/img_005.png)

## Electrical Characteristics (TJ=25°C unless otherwise noted)

| Symbol | Parameter | Conditions | Min | Typ | Max | Units |
| - | - | - | - | - | - | - |
| STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS | STATIC PARAMETERS |
| BVDSS | Drain-Source Breakdown Voltage | ID=-250mA, VGS=0V | -30 |  |  | V |
| IDSS | Zero Gate Voltage Drain Current | VDS=-30V, VGS=0V |  |  | -1 | mA |
|  |  |  | TJ=55°C |  | -5 |  |
| IGSS | Gate-Body leakage current | VDS=0V, VGS= ±12V |  |  | ±100 | nA |
| VGS(th) | Gate Threshold Voltage | VDS=VGS ID=-250mA | -0.5 | -0.9 | -1.3 | V |
| ID(ON) | On state drain current | VGS=-10V, VDS=-5V | -27 |  |  | A |
| RDS(ON) |  | VGS=-10V, ID=-4.0A |  | 41 | 50 |  |
|  |  |  | TJ=125°C | 62 | 75 | mW |
|  | Static Drain-Source On-Resistance | VGS=-4.5V, ID=-3.5A |  | 47 | 60 | mW |
|  |  | VGS=-2.5V, ID=-2.5A |  | 60 | 85 | mW |
| gFS | Forward Transconductance | VDS=-5V, ID=-4.0A |  | 17 |  | S |
| VSD | Diode Forward Voltage | IS=-1A,VGS=0V |  | -0.7 | -1 | V |
| IS | Maximum Body-Diode Continuous Current | Maximum Body-Diode Continuous Current |  |  | -2 | A |
| DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS | DYNAMIC PARAMETERS |
| Ciss | Input Capacitance | VGS=0V, VDS=-15V, f=1MHz |  | 645 |  | pF |
| Coss | Output Capacitance | VGS=0V, VDS=-15V, f=1MHz |  | 80 |  | pF |
| Crss | Reverse Transfer Capacitance | VGS=0V, VDS=-15V, f=1MHz |  | 55 |  | pF |
| Rg | Gate resistance | VGS=0V, VDS=0V, f=1MHz | 4 | 7.8 | 12 | W |
| SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS | SWITCHING PARAMETERS |
| Qg(10V) | Total Gate Charge | VGS=-10V, VDS=-15V, ID=-4.0A |  | 14 |  | nC |
| Qg(4.5V) | Total Gate Charge | VGS=-10V, VDS=-15V, ID=-4.0A |  | 7 |  | nC |
| Qgs | Gate Source Charge | VGS=-10V, VDS=-15V, ID=-4.0A |  | 1.5 |  | nC |
| Qgd | Gate Drain Charge |  |  | 2.5 |  | nC |
| tD(on) | Turn-On DelayTime | VGS=-10V, VDS=-15V, RL=3.75W, |  | 6.5 |  | ns |
| tr | Turn-On Rise Time | VGS=-10V, VDS=-15V, RL=3.75W, |  | 3.5 |  | ns |
| tD(off) | Turn-Off DelayTime | RGEN=3W |  | 41 |  | ns |
| tf | Turn-Off Fall Time | VGS=-10V, VDS=-15V, RL=3.75W, |  | 9 |  | ns |
| trr | Body Diode Reverse Recovery Time | IF=-4.0A, dI/dt=100A/ms |  | 11 |  | ns |
| Qrr | Body Diode Reverse Recovery Charge | IF=-4.0A, dI/dt=100A/ms |  | 3.5 |  | nC |

A. The value of RqJA is measured with the device mounted on 1in 2 FR-4 board with 2oz. Copper, in a still air environment with T A =25°C. The value in any given application depends on the user's specific board design.

- B. The power dissipation P D is based on T J(MAX) =150°C, using ≤10s junction-to-ambient thermal resistance.
- C. Repetitive rating, pulse width limited by junction temperature T J(MAX) =150°C. Ratings are based on low frequency and duty cycles to keep initialT J =25°C.
- D. The RqJA is the sum of the thermal impedence from junction to lead RqJL and lead to ambient.
- E. The static characteristics in Figures 1 to 6 are obtained using &lt;300ms pulses, duty cycle 0.5% max.
- F. These curves are based on the junction-to-ambient thermal impedence which is measured with the device mounted on 1in 2 FR-4 board with 2oz. Copper, assuming a maximum junction temperature of T J(MAX) =150°C. The SOA curve provides a single pulse rating.

APPLICATIONS OR USES AS CRITICAL COMPONENTS IN LIFE SUPPORT DEVICES OR SYSTEMS ARE NOT AUTHORIZED. AOS DOES NOT ASSUME ANY LIABILITY ARISING OUT OF SUCH APPLICATIONS OR USES OF ITS PRODUCTS. AOS RESERVES THE RIGHT TO MAKE CHANGES TO PRODUCT SPECIFICATIONS WITHOUT NOTICE. IT IS THE RESPONSIBILITY OF THE CUSTOMER TO EVALUATE SUITABILITY OF THE PRODUCT FOR THEIR INTENDED APPLICATION. CUSTOMER SHALL COMPLY WITH APPLICABLE LEGAL REQUIREMENTS, INCLUDING ALL APPLICABLE EXPORT CONTROL RULES, REGULATIONS AND LIMITATIONS.

AOS' products are provided subject to AOS' terms and conditions of sale which are set forth at:

http://www.aosmd.com/terms\_and\_conditions\_of\_sale

![Image](AO3401A%20Datasheet_files/img_006.png)

## TYPICAL ELECTRICAL AND THERMAL CHARACTERISTICS

-V DS (Volts) Fig 1: On-Region Characteristics (Note E)

![Image](AO3401A%20Datasheet_files/img_007.png)

![Image](AO3401A%20Datasheet_files/img_008.png)

-I D (A)

Figure 3: On-Resistance vs. Drain Current and Gate Voltage (Note E)

![Image](AO3401A%20Datasheet_files/img_009.png)

Figure 5: On-Resistance vs. Gate-Source Voltage (Note E)

![Image](AO3401A%20Datasheet_files/img_010.png)

-V GS (Volts)

Figure 2: Transfer Characteristics (Note E)

![Image](AO3401A%20Datasheet_files/img_011.png)

0 18 Temperature (°C) Figure 4: On-Resistance vs. Junction Temperature (Note E)

![Image](AO3401A%20Datasheet_files/img_012.png)

![Image](AO3401A%20Datasheet_files/img_013.png)

## TYPICAL ELECTRICAL AND THERMAL CHARACTERISTICS

10

8

-V GS (Volts)

-ID (Amps)

6

4

2

0

V DS =-15V

I D =-4A

0

5

10

15

100.0

10.0

1.0

0.1

0.0

Q g (nC) Figure 7: Gate-Charge Characteristics

10ms

RDS(ON)

limited

100ms

1ms

10ms

TJ(Max)=150°C

TA=25°C

10s

DC

0.01

0.1

1

10

100

-V DS (Volts) Figure 9: Maximum Forward Biased Safe

Operating Area (Note F)

C iss

C oss

C rss

0

5

10

15

20

25

30

10000

1000

100

10

1

-V DS (Volts)

Figure 8: Capacitance Characteristics

T A =25°C

0.00001

0.001

0.1

10

1000

Pulse Width (s) Figure 10: Single Pulse Power Rating Junction-toAmbient (Note F)

![Image](AO3401A%20Datasheet_files/img_014.png)

Pulse Width (s)

Figure 11: Normalized Maximum Transient Thermal Impedance (Note F)

1000

800

600

400

200

0

Capacitance (pF)

Power (W)

![Image](AO3401A%20Datasheet_files/img_015.png)

## Gate Charge Test Circuit &amp; Waveform

![Image](AO3401A%20Datasheet_files/img_016.png)

![Image](AO3401A%20Datasheet_files/img_017.png)

![Image](AO3401A%20Datasheet_files/img_018.png)

Resistive Switching Test Circuit &amp; Waveforms

![Image](AO3401A%20Datasheet_files/img_019.png)

Unclamped Inductive Switching (UIS) Test Circuit &amp; Waveforms

![Image](AO3401A%20Datasheet_files/img_020.png)

![Image](AO3401A%20Datasheet_files/img_021.png)

Diode Recovery Test Circuit &amp; Waveforms

![Image](AO3401A%20Datasheet_files/img_022.png)
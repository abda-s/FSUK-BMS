<!-- Converted from RP131x Datasheet (Ricoh).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_001.png)

NISSHINBO

## RP131x SERIES

## LOW ON RESISTANCE / LOW VOLTAGE 1A LDO

## OUTLINE

The RP131x Series are voltage-regulators with a built-in low ON-resistance transistor and output current is 1A capability. These ICs are capable of the low input voltage (Min.1.6V) and also the minimum output voltage can be set from 0.8V. (The output voltage is fixed in the IC.)

Each of these ICs consists of a voltage reference unit, an error amplifier, a resistor net for setting output voltage, a chip enable circuit, current limit circuits for over-current and short, and a thermal-shutdown circuit.

A standby mode with ultra low supply current can be realized with the chip enable function.

The packages for these ICs are DFN1616-6B and DFN(PL)1820-6 which are suitable for high density mounting of the ICs on boards. SOT-89-5, HSOP-6J and TO-252-5-P2 with high power dissipation are also available.

## FEATURES

| · Output Current | ............................................................ Min. 1A |
| - | - |
| · Supply Current | ............................................................. Typ. 65µA |
| · Standby Current | ......................................................... Typ. 0.15µA |
| · Input Voltage Range | ................................................... 1.6V to 6.5V |
| · Output Voltage Range | .................................................. 0.8V to 5.5V (1) (0.1V steps) |
| · Dropout Voltage............................................................ | Typ. 0.5V (VOUT=2.8V, IOUT=1A) |
| · Ripple Rejection | ........................................................... Typ. 70dB (f=1kHz, VOUT=2.8V) |
| · Output Voltage Accuracy | .............................................. ±1.0% |
| · Temperature-Drift Coefficient of Output Voltage | .......... Typ. ±100ppm/°C |
| · Line Regulation | ............................................................ Typ. 0.05%/V |
| · Load Regulation | ......................................................... Typ. 20mV at IOUT=300mA, Typ. 80mV at IOUT=1A |
| · Packages | .................................................................... DFN1616-6B, DFN(PL)1820-6, SOT-89-5, HSOP-6J, TO-252-5-P2 |
| · Built-in Inrush current limit circuit | ............................... Typ. 500mA |
| · Built-in Fold-Back Protection Circuit | ........................... Typ. 250mA (Current at short mode) |
| · Built-in Thermal Shutdown Circuit | .............................. Thermal Shutdown Temperature ; Typ. 165°C Released Temperature ; Typ. 135°C |
| · Built-in Auto Discharge Function | ................................ D version |
| · Ceramic capacitors are recommended to be used with this IC .... 2.2µF or more | (VOUT≤3.6V) |

4.7µF or more (VOUT&gt;3.6V)

NO.EA-174-231017

## APPLICATIONS

- Power source for battery-powered equipment.
- Power source for portable communication equipment.
- Power source for electrical appliances such as cameras, VCRs and camcorders.
- Power source for Notebook PC.
- Power source for home appliances.

(1) For other voltages, please refer to MARK INFORMATIONS.

## RP131x

## SELECTION GUIDE

The output voltage, auto discharge function, package for the ICs can be selected at the user's request.

| Product Name | Package | Quantity per Reel | Pb Free | Halogen Free |
| - | - | - | - | - |
| RP131Lxx1∗-TR | DFN1616-6B | 5,000 pcs | Yes | Yes |
| RP131Kxx1∗-TR | DFN(PL)1820-6 | 5,000 pcs | Yes | Yes |
| RP131Hxx1∗-T1-FE | SOT-89-5 | 1,000 pcs | Yes | Yes |
| RP131Sxx1∗-E2-FE | HSOP-6J | 1,000 pcs | Yes | Yes |
| RP131Jxx1∗-T1-FE | TO-252-5-P2 | 3,000 pcs | Yes | Yes |

- xx : The output voltage can be designated in the range from 0.8V(08) to 5.5V(55) in 0.1V steps. (For other voltages, please refer to MARK INFORMATIONS.)
- ∗ : The auto discharge function at off state are options as follows. (1)
- (B) without auto discharge function at off state
- (D) with auto discharge function at off state

## BLOCK DIAGRAMS

## RP131xxx1B

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_002.png)

(1) Auto-discharge function quickly lowers the output voltage to 0V, when the chip enable signal is switched from the active mode to the standby mode, by releasing the electrical charge accumulated in the external capacitor.

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_003.png)

NO.EA-174-231017

## RP131x

## PIN DESCRIPTIONS

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_004.png)

DFN1616-6B

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_005.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_006.png)

NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_007.png)

SOT-89-5

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_008.png)

HSOP-6J

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_009.png)

- ∗Tab is GND level. (They are connected to the reverse side of this IC.) The tab is better to be connected to the GND, but leaving it open is also acceptable.

## RP131L (DFN1616-6B) Pin Description

| Pin No. | Symbol | Pin Description |
| - | - | - |
| 1 | VOUT | Output Pin (1) |
| 2 | VOUT | Output Pin(1) |
| 3 | GND | Ground Pin |
| 4 | CE | Chip Enable Pin ("H" Active) |
| 5 | VDD | Input Pin(1) |
| 6 | VDD | Input Pin(1) |

(1) When you use this IC, please make sure be wired with 1pin with 2pin and 5pin with 6pin.

## RP131K (DFN(PL)1820-6) Pin Description

| Pin No. | Symbol | Pin Description |
| - | - | - |
| 1 | VOUT | Output Pin (1) |
| 2 | VOUT | Output Pin(1) |
| 3 | GND | Ground Pin |
| 4 | CE | Chip Enable Pin ("H" Active) |
| 5 | VDD | Input Pin(1) |
| 6 | VDD | Input Pin(1) |

1

## RP131H (SOT-89-5) Pin Description

| Pin No. | Symbol | Pin Description |
| - | - | - |
| 1 | NC | No Connection |
| 2 | GND | Ground Pin |
| 3 | CE | Chip Enable Pin ("H" Active) |
| 4 | VDD | Input Pin |
| 5 | VOUT | Output Pin |

## RP131S (HSOP-6J) Pin Description

| Pin No. | Symbol | Pin Description |
| - | - | - |
| 1 | VOUT | Output Pin |
| 2 | GND | Ground Pin (2) |
| 3 | NC | No Connection |
| 4 | CE | Chip Enable Pin ("H" Active) |
| 5 | GND | Ground Pin(2) |
| 6 | VDD | Input Pin |

## RP131J (TO-252-5-P2) Pin Description

| Pin No. | Symbol | Pin Description |
| - | - | - |
| 1 | VOUT | Output Pin |
| 2 | GND | Ground Pin (3) |
| 3 | GND | Ground Pin(3) |
| 4 | CE | Chip Enable Pin ("H" Active) |
| 5 | VDD | Input Pin |

(1) When you use this IC, please make sure be wired with 1pin with 2pin and 5pin with 6pin.

(2) When you use this IC, please make sure be wired with 2pin and 5pin.

(3) When you use this IC, please make sure be wired with 2pin and 3pin.

NO.EA-174-231017

## ABSOLUTE MAXIMUM RATINGS

| Symbol | Item | Rating | Unit |
| - | - | - | - |
| VIN | Input Voltage | 7.0 | V |
| VCE | Input Voltage (CE Pin) | -0.3 to 7.0 | V |
| VOUT | Output Voltage | -0.3 to VIN+0.3 | V |
| PD | Power Dissipation (1) DFN1616-6B | 2400 | mW |
| PD | DFN(PL)1820-6 | 2200 | mW |
| PD | SOT-89-5 | 2600 | mW |
| PD | HSOP-6J | 2700 | mW |
| PD | TO-252-5-P2 | 3800 | mW |
| Tj | Junction Temperature Range | -40 to 125 | °C |
| Tstg | Storage Temperature Range | -55 to 125 | °C |

## ABSOLUTE MAXIMUM RATINGS

Electronic and mechanical stress momentarily exceeded absolute maximum ratings may cause the permanent damages and may degrade the life time and safety for both device and system using the device in the field.

The functional operation at or over these absolute maximum ratings is not assured.

## RECOMMENDED OPERATING CONDITIONS

| Symbol | Item | Rating | Unit |
| - | - | - | - |
| VIN | Input Voltage | 1.6 to 6.5 | V |
| Ta | Operating Temperature Range | -40 to 85 | °C |

## RECOMMENDED OPERATING CONDITIONS

All of electronic equipment should be designed that the mounted semiconductor devices operate within the recommended operating conditions. The semiconductor devices cannot operate normally over the recommended operating conditions, even if when they are used over such ratings by momentary electronic noise or surge. And the semiconductor devices may receive serious damage when they continue to operate over the recommended operating conditions.

(1) Refer to POWER DISSIPATION for detailed information.

NO.EA-174-231017

## ELECTRICAL CHARACTERISTICS

VIN=Set VOUT+1V, IOUT=1mA

The specification in is checked and guaranteed by design engineering at -40°C≤Ta≤85°C, unless otherwise noted.

## RP131xxx1B/D

(Ta = 25°C)

| Symbol | Item | Conditions | Conditions | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - | - | - |
| VOUT | Output Voltage | Ta = 25°C | VOUT>1.5V | ×0.99 |  | ×1.01 | V |
| VOUT | Output Voltage | Ta = 25°C | VOUT≤1.5V | -15 |  | 15 | mV |
| VOUT | Output Voltage | -40°C ≤ Ta ≤ 85°C | VOUT>1.5V | ×0.974 |  | ×1.018 | V |
| VOUT | Output Voltage | -40°C ≤ Ta ≤ 85°C | VOUT≤1.5V | -40 |  | 27 | mV |
| ∆VOUT/ ∆IOUT | Load Regulation | 0.1mA ≤ IOUT ≤ 300mA | 0.1mA ≤ IOUT ≤ 300mA |  | 20 | 40 | mV |
| ∆VOUT/ ∆IOUT | Load Regulation | 0.1mA ≤ IOUT ≤ 1A | 0.1mA ≤ IOUT ≤ 1A |  | 80 | 120 | mV |
| VDIF | Dropout Voltage | Refer to the following table | Refer to the following table | Refer to the following table | Refer to the following table | Refer to the following table | Refer to the following table |
| ISS | Supply Current | IOUT=0mA (VIN=6.5V) | IOUT=0mA (VIN=6.5V) |  | 65 | 90 | µA |
| Istandby | Standby Current | VCE=0V, VIN=6.5V | VCE=0V, VIN=6.5V |  | 0.15 | 0.60 | µA |
| ∆VOUT/ ∆VIN | Line Regulation | Set VOUT+0.5V ≤ VIN ≤ 6.5V ∗However, VIN ≥ 1.6V | Set VOUT+0.5V ≤ VIN ≤ 6.5V ∗However, VIN ≥ 1.6V |  | 0.05 | 0.1 | %/V |
| RR | Ripple Rejection | f=1kHz Ripple 0.2Vp-p IOUT=100mA | VOUT≤3.3V |  | 70 |  | dB |
| RR | Ripple Rejection | f=1kHz Ripple 0.2Vp-p IOUT=100mA | VOUT>3.3V |  | 60 |  | dB |
| VIN | Input Voltage |  |  | 1.6 |  | 6.5 | V |
| ILIM | Output Current Limit |  |  | 1 |  |  | A |
| ∆VOUT/ ∆Ta | Output Voltage Temperature Coefficient | -40°C≤Ta≤85°C | -40°C≤Ta≤85°C |  | ±100 |  | ppm /°C |
| ISC | Short Current Limit | VOUT=0V | VOUT=0V |  | 250 |  | mA |
| IPD | CE Pull-down Current |  |  |  | 0.3 |  | µA |
| VCEH | CE Input Voltage "H" |  |  | 1.0 |  |  | V |
| VCEL | CE Input Voltage "L" |  |  |  |  | 0.4 | V |
| en | Output Noise | BW=10Hz to 100kHz, IOUT=1mA | BW=10Hz to 100kHz, IOUT=1mA |  | 45 |  | µVrms |
| TTSD | Thermal Shutdown Temperature | Junction Temperature | Junction Temperature |  | 165 |  | °C |
| TTSR | Thermal Shutdown Released Temperature | Junction Temperature | Junction Temperature |  | 135 |  | °C |
| RLOW | Low Output Nch Tr. ON Resistance (of D version) | VIN=4.0V, VCE=0V | VIN=4.0V, VCE=0V |  | 30 |  | Ω |

All test items listed under Electrical Characteristics are done under the pulse load condition (Tj≈Ta = 25°C) except for Output Noise, Ripple Rejection, Output Voltage Temperature Coefficient, Dropout Voltage at 1A Output Current and Thermal Shutdown items.

NO.EA-174-231017

## RP131x

NO.EA-174-231017

The specification in is checked and guaranteed by design engineering at -40°C ≤ Ta ≤ 85°C, unless otherwise noted.

| Dropout Voltage - Output Voltage VOUT (V) | Dropout Voltage | Condition Typ. | Max. | VDIF (V) Condition | Typ. | (Ta = 25°C) - Max. |
| - | - | - | - | - | - | - |
| 0.8 ≤ VOUT < 0.9 | IOUT=300mA | 0.600 | 0.780 | IOUT=1A | 1.100 | 1.650 |
| 0.9 ≤ VOUT < 1.0 | IOUT=300mA | 0.550 | 0.690 | IOUT=1A | 1.050 | 1.500 |
| 1.0 ≤ VOUT < 1.1 | IOUT=300mA | 0.450 | 0.610 | IOUT=1A | 1.000 | 1.450 |
| 1.1 ≤ VOUT < 1.2 | IOUT=300mA | 0.340 | 0.540 | IOUT=1A | 0.930 | 1.420 |
| 1.2 ≤ VOUT < 1.5 | IOUT=300mA | 0.290 | 0.500 | IOUT=1A | 0.900 | 1.380 |
| 1.5 ≤ VOUT < 2.6 | IOUT=300mA | 0.230 | 0.310 | IOUT=1A | 0.700 | 1.100 |
| 2.6 ≤ VOUT < 3.3 | IOUT=300mA | 0.150 | 0.180 | IOUT=1A | 0.500 | 0.750 |
| 3.3 ≤ VOUT ≤ 5.5 | IOUT=300mA | 0.140 | 0.170 | IOUT=1A | 0.450 | 0.650 |

## APPLICATION INFORMATION

## Typical Application Circuits

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_010.png)

## Recommendation value of the external capacitors

| VOUT | Capacitors | Capacitors | Capacitors |
| - | - | - | - |
| VOUT ≤ 3.6V | CIN | Kyocera 2.2µF (size:1005) | [CM05X5R225M06AB] |
| VOUT ≤ 3.6V | COUT | Kyocera 2.2µF (size:1608) | [CM105X5R225K06AB] |
| VOUT > 3.6V | CIN | Kyocera 2.2µF (size:1608) | [CM105X5R225K06AB] |
| VOUT > 3.6V | COUT | Kyocera 4.7µF (size:1608) | [CM105X5R475M06AB] |

## Technical Notes on the External Components

When using this IC, consider following points:

## Phase Compensation

In these ICs, phase compensation is made for securing stable operation even if the load current is varied. For this purpose, use a capacitor COUT with good frequency characteristics and ESR (Equivalent Series Resistance).

If a tantalum capacitor is used, and its ESR of COUT is large, the loop oscillation may result. Because of this, select COUT carefully considering its frequency characteristics.

## PCB Layout

Make VDD and GND lines sufficient. If their impedance is high, noise pickup or unstable operation may result. Connect a capacitor CIN between VDD and GND pin with a capacitance value as "Recommendation value of the external capacitors" above or more, and as close as possible to the pins.

Set external components, especially the output capacitor COUT, as close as possible to the ICs, and make wiring as short as possible.

NO.EA-174-231017

## RP131x

## TEST CIRCUITS

Basic Test Circuit

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_011.png)

Test Circuit for Supply Current

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_012.png)

Test Circuit for Ripple Rejection

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_013.png)

Test Circuit for Load Transient Response

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_014.png)

## NO.EA-174-231017

## TYPICAL CHARACTERISTICS

Typical Characteristics are intended to be used as reference data; they are not guaranteed.

## 1) Output Voltage vs. Output Current (Ta = 25°C)

## RP131x081x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_015.png)

RP131x331x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_016.png)

2) Output Voltage vs. Input Voltage (Ta=25°C) RP131x081x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_017.png)

NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_018.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_019.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_020.png)

RP131x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_021.png)

NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_022.png)

3) Supply Current vs. Input Voltage (Ta=25°C) RP131x081x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_023.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_024.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_025.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_026.png)

## 4) Output Voltage vs. Temperature

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_027.png)

NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_028.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_029.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_030.png)

## 5) Supply Current vs. Temperature

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_031.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_032.png)

RP131x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_033.png)

NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_034.png)

## 6) Dropout Voltage vs. Output Current

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_035.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_036.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_037.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_038.png)

## 7) Dropout Voltage vs. Set Output Voltage

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_039.png)

- 8) Ripple Rejection vs. Input Bias Voltage (CIN=none, COUT=Ceramic 1.0µF, Ripple=0.2Vp-p, Ta=25°C)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_040.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_041.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_042.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_043.png)

NO.EA-174-231017

Ripple Rejection RR (dB)

90

80

70

60

50

40

30

20

lout=10mA

f=0.2kHz

f=1kHz

10

0

4.5

5.0

RP131x501x

5.5

f=10kHz

f=100kHz

6.0

6.5

Input Voltage Vin (V)

## RP131x

NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_044.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_045.png)

9) Ripple Rejection vs. Frequency (CIN=none, COUT=Ceramic 4.7µF, Ta=25°C)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_046.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_047.png)

RP131x501x

VIN=6.0VDC+0.2Vp-p

100

90

80

70

60

50

40

30

lout=1mA

20

10

0

0.1

lout=30mA

lout=100mA

1

10

100

1000

Frequency f (kHz)

Ripple Rejection RR (dB)

10) Input Transient Response (IOUT=100mA, tr=tf=5µs, CIN=none, Ta=25°C) RP131x081x RP131x151x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_048.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_049.png)

RP131x331x RP131x501x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_050.png)

11) Load Transient Response (tr=tf=0.5µs, CIN=Ceramic 2.2µF, VIN=VOUT+1.0V, Ta=25°C)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_051.png)

RP131x081x NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_052.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_053.png)

RP131x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_054.png)

## NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_055.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_056.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_057.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_058.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_059.png)

RP131x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_060.png)

## NO.EA-174-231017

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_061.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_062.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_063.png)

## 12) Turn On Speed with CE pin (CIN=Ceramic 2.2µF, COUT=Ceramic 4.7µF, Ta=25°C)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_064.png)

RP131x081x RP131x501x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_065.png)

NO.EA-174-231017

13) Turn Off Speed with CE pin (D Version) (CIN=Ceramic 2.2µF, COUT=Ceramic 4.7µF, Ta=25°C) RP131x081D RP131x501D

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_066.png)

M

14) Inrush Current at turning on (CIN=Ceramic 2.2µF, COUT=Ceramic 4.7µF, Ta=25°C)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_067.png)

RP131x081x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_068.png)

## 15) Minimum Operating Voltage

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_069.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_070.png)

Hatched area is available for 0.8V output.

## ESR vs. Output Current

When using these ICs, consider the following points:

The relations between IOUT (Output Current) and ESR of an output capacitor are shown below.

The conditions when the white noise level is under 40µV (Avg.) are marked as the hatched area in the graph.

## Measurement conditions

Frequency Band : 10Hz to 3MHz

Temperature : -40°C to 85°C

CIN

: 2.2µF (Kyocera, CM05X5R225M04AD)

COUT

: 2.2µF (Kyocera, CM105X5R225K06AE)

4.7µF (Kyocera, CM105X5R475M06AB)

## RP131x081x

## RP131x151x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_071.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_072.png)

## RP131x331x

## RP131x501x

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_073.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_074.png)

NO.EA-174-231017

## RP131L SERIES MARK SPECIFICATION

## · DFN1616-6B

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_075.png)

c to f : Product Code (Refer to Part Number vs. Product Code)

g, h : Lot Number

## · Part Number vs. Product Code

## RP131Lxx1B Series

## RP131Lxx1D Series

| Product Code d e Part | f | Number | c | d | e f |  | Number | c | d | C C 2 6 | RP131L081B 0 | C | B | e | f - 1 | f - RP131L301B | f - C | f - B |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| 2 | 6 | RP131L081D | C | C | 0 | 1 | RP131L301D |  |  |  | RP131L091B | C | B | 0 | 2 | RP131L311B | C | B |
| 2 | 7 | RP131L091D | C | C | 0 | 2 | RP131L311D | C | C | 7 | RP131L101B | C | B | 0 | 3 | RP131L321B | C | B |
| 2 | 8 | RP131L101D | C | C | 0 | 3 | RP131L321D | C | C | 2 8 | RP131L111B | C | B | 0 | 4 | RP131L331B | C | B |
| 2 | 9 | RP131L111D | C | C | 0 | 4 | RP131L331D | C | C | 2 9 | RP131L121B | C | B | 0 | 5 | RP131L341B | C | B |
| 3 | 0 | RP131L121D | C | C | 0 | 5 | RP131L341D | C | C | 3 0 | RP131L131B | C | B | 0 | 7 | RP131L351B | C | B |
| 3 | 1 | RP131L131D | C | C | 0 | 7 | RP131L351D | C | C | 3 1 | RP131L141B | C | B | 0 | 8 | RP131L361B | C | B |
| 3 | 2 | RP131L141D | C | C | 0 | 8 | RP131L361D | C | C | 3 2 | RP131L151B | C | B | 0 | 9 | RP131L371B | C | B |
| 3 | 3 | RP131L151D | C | C | 0 | 9 | RP131L371D | C | C | 3 3 | RP131L161B | C | B | 1 | 0 | RP131L381B | C | B |
| 3 | 4 | RP131L161D | C | C | 1 | 0 | RP131L381D | C | C | 3 4 | RP131L171B | C | B | 1 | 1 | RP131L391B | C | B |
| 3 | 5 | RP131L171D | C | C | 1 | 1 | RP131L391D | C | C | 3 5 | RP131L181B | C | B | 1 | 2 | RP131L401B | C | B |
| 3 | 6 | RP131L181D | C | C | 1 | 2 | RP131L401D | C | C | 3 6 | RP131L191B | C | B | 1 | 4 | RP131L411B | C | B |
| 3 | 7 | RP131L191D | C | C | 1 | 4 | RP131L411D | C | C | 3 7 | RP131L201B | C | B | 1 | 5 | RP131L421B | C | B |
| 3 | 8 | RP131L201D | C | C | 1 | 5 | RP131L421D | C | C | 3 8 | RP131L211B | C | B | 1 | 6 | RP131L431B | C | B |
| 3 | 9 | RP131L211D | C | C | 1 | 6 | RP131L431D | C | C | 3 9 | RP131L221B | C | B | 1 | 7 | RP131L441B | C | B |
| 4 | 0 | RP131L221D | C | C | 1 | 7 | RP131L441D | C | C | 4 0 | RP131L231B | C | B | 1 | 8 | RP131L451B | C | B |
| 4 | 1 | RP131L231D | C | C | 1 | 8 | RP131L451D | C | C | 4 1 | RP131L241B | C | B | 1 | 9 | RP131L461B | C | B |
| 4 | 2 | RP131L241D | C | C | 1 | 9 | RP131L461D | C | C | 4 2 | RP131L251B | C | B | 2 | 0 | RP131L471B |  | B |
| 4 | 3 | RP131L251D | C | C | 2 | 0 C | RP131L471D |  | C | 4 3 | RP131L261B | C | B | 2 | C 1 | RP131L481B | C | B |
| 4 | 4 | RP131L261D | C | C | 2 | 1 | RP131L481D | C | C | 4 4 | RP131L271B | C | B | 2 | 2 | RP131L491B | C | B |
| 4 | 5 | RP131L271D | C | C | 2 | 2 | RP131L491D | C | C | 4 5 | RP131L281B | C | B | 2 | 3 | RP131L501B | C | B |
| 4 | 6 | RP131L281D | C | C | 2 | 3 | RP131L501D | C | C | 4 6 | RP131L291B | C | B | 2 | 5 | RP131L511B | C |  |
|  |  |  | C | C |  | 5 | RP131L511D |  | C | 4 8 |  |  |  |  |  |  | C | B 2 |
| 4 B 4 | 8 9 | RP131L291D |  |  |  | C C |  | C |  | 4 9 |  | RP131L521B |  | B | 5 |  | RP131L521D | C |
|  |  |  |  |  |  | C | 0 |  |  |  |  |  |  |  |  | RP131L531B C 0 | RP131L531D |  |
| 5 | 1 |  |  |  |  |  | 5 |  | RP131L541B |  |  |  |  | B | C |  | RP131L541D | C |
|  |  |  |  |  | C | 5 1 |  | RP131L551B |  |  |  |  |  |  | 2 | RP131L551D | C B 5 | C |
|  |  |  |  |  | C | 5 2 |  | C | B | 4 |  |  |  |  | 7 | RP131L101B5 C 4 | RP131L101D5 |  |
| B |  |  |  |  |  | C C | 7 |  | C | 0 6 |  |  |  | RP131L121B5 0 1 | C 6 | RP131L121D5 | RP131L181D5 | B |
| 2 | 4 |  |  |  | 3 | C C | RP131L281B5 C |  | B | 1 2 |  |  |  | RP131L181B5 | C 3 |  | RP131L281D5 | C |
|  |  |  |  |  | Part C | Product | 4 |  |  | Code e f 2 | Product Code Part Number c d |  | Part |  | Number c |  |  | Product Code |

## RP131K SERIES MARK SPECIFICATION

## · DFN(PL)1820-6

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_076.png)

c to f : Product Code (Refer to Part Number vs. Product Code)

g, h : Lot Number

## · Part Number vs. Product Code

## RP131Kxx1B Series

| Part Number | Product Code - c | Product Code - d | Product Code - e | Product Code - f | Part Number | Product - c | Product - d | Product - e | Code f Part Number | Product Code | Product Code - c | Product Code - d | Product Code - e | Product Code - f | Part Number | Product - c | Product - d | Product - e f | Product - e f | Product - e f |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| RP131K081B | A | M | 0 | 1 | RP131K301B | A | M | 2 | 6 | RP131K081D | A | N | 0 | 1 | RP131K301D | A | N | 2 6 | 2 6 | 2 6 |
| RP131K091B | A | M | 0 | 2 | RP131K311B | A | M | 2 | 7 | RP131K091D | A | N | 0 | 2 | RP131K311D | A | N | 2 7 | 2 7 | 2 7 |
| RP131K101B | A | M | 0 | 3 | RP131K321B | A | M | 2 | 8 | RP131K101D | A | N | 0 | 3 | RP131K321D | A | N | 2 8 | 2 8 | 2 8 |
| RP131K111B | A | M | 0 | 4 | RP131K331B | A | M | 2 | 9 | RP131K111D | A | N | 0 | 4 | RP131K331D | A | N | 2 9 | 2 9 | 2 9 |
| RP131K121B | A | M | 0 | 5 | RP131K341B | A | M | 3 | 0 | RP131K121D | A | N | 0 | 5 | RP131K341D | A | N | 3 0 | 3 0 | 3 0 |
| RP131K131B | A | M | 0 | 7 | RP131K351B | A | M | 3 | 1 | RP131K131D | A | N | 0 | 7 | RP131K351D | A | N | 3 1 | 3 1 | 3 1 |
| RP131K141B | A | M | 0 | 8 | RP131K361B | A | M | 3 | 2 RP131K141D |  | A | N | 0 | 8 | RP131K361D | A | N | 3 2 | 3 2 | 3 2 |
| RP131K151B | A | M | 0 | 9 | RP131K371B | A | M | 3 | 3 | RP131K151D | A | N | 0 | 9 | RP131K371D | A | N | 3 3 | 3 3 | 3 3 |
| RP131K161B | A | M | 1 | 0 | RP131K381B | A | M | 3 | 4 | RP131K161D | A | N | 1 | 0 | RP131K381D | A | N | 3 4 | 3 4 | 3 4 |
| RP131K171B | A | M | 1 | 1 | RP131K391B | A | M | 3 | 5 | RP131K171D | A | N | 1 | 1 | RP131K391D | A | N | 3 5 | 3 5 | 3 5 |
| RP131K181B | A | M | 1 | 2 | RP131K401B | A | M | 3 | 6 | RP131K181D | A | N | 1 | 2 | RP131K401D | A | N | 3 6 | 3 6 | 3 6 |
| RP131K191B | A | M | 1 | 4 | RP131K411B | A | M | 3 | 7 | RP131K191D | A | N | 1 | 4 | RP131K411D | A | N | 3 7 | 3 7 | 3 7 |
| RP131K201B | A | M | 1 | 5 | RP131K421B | A | M | 3 | 8 | RP131K201D | A | N | 1 | 5 | RP131K421D | A | N | 3 8 | 3 8 | 3 8 |
| RP131K211B | A | M | 1 | 6 | RP131K431B | A | M | 3 | 9 | RP131K211D | A | N | 1 | 6 | RP131K431D | A | N | 3 9 | 3 9 | 3 9 |
| RP131K221B | A | M | 1 | 7 | RP131K441B | A | M | 4 | 0 | RP131K221D | A | N | 1 | 7 | RP131K441D | A | N | 4 0 | 4 0 | 4 0 |
| RP131K231B | A | M | 1 | 8 | RP131K451B | A | M | 4 | 1 | RP131K231D | A | N | 1 | 8 | RP131K451D | A | N | 4 1 | 4 1 | 4 1 |
| RP131K241B | A | M | 1 | 9 | RP131K461B | A | M | 4 | 2 | RP131K241D | A | N | 1 | 9 | RP131K461D | A | N | 4 2 | 4 2 | 4 2 |
| RP131K251B | A | M | 2 | 0 | RP131K471B | A | M | 4 | 3 | RP131K251D | A | N | 2 | 0 | RP131K471D | A | N | 4 3 | 4 3 | 4 3 |
| RP131K261B | A | M | 2 | 1 | RP131K481B | A | M | 4 | 4 | RP131K261D | A | N | 2 | 1 | RP131K481D | A | N | 4 4 | 4 4 | 4 4 |
| RP131K271B | A | M | 2 | 2 | RP131K491B | A | M | 4 | 5 | RP131K271D | A | N | 2 | 2 | RP131K491D | A | N | 4 5 | 4 5 | 4 5 |
| RP131K281B | A | M | 2 | 3 | RP131K501B | A | M | 4 | 6 | RP131K281D | A | N | 2 | 3 | RP131K501D | A | N | 4 6 | 4 6 | 4 6 |
| RP131K291B | A | M | 2 | 5 | RP131K511B | A | M | 4 | 9 RP131K291D |  | A |  | N | 2 5 | RP131K511D | A | N | 4 9 | 4 9 | 4 9 |
|  |  |  |  |  | RP131K521B | A | M | 5 | 0 |  |  |  |  |  | RP131K521D | A | N | 5 0 | 5 0 | 5 0 |
|  |  |  |  |  | RP131K531B | A | M | 5 | 1 |  |  |  |  |  | RP131K531D |  | A | 5 1 | 5 1 | 5 1 |
|  |  |  |  |  |  |  |  | 5 |  |  |  |  |  |  |  |  | N |  |  |  |
|  |  |  |  |  | RP131K541B | A | M |  | 2 |  |  |  |  |  | RP131K541D | A | A | 5 2 | 5 2 | 5 2 |
|  |  |  |  |  | RP131K551B | A | M | 4 | 8 |  |  |  |  |  | RP131K551D |  |  | 4 | N | 8 |
|  |  |  |  |  | RP131K101B5 | A | M | 4 | 7 |  |  |  |  | RP131K101D5 | N | 7 | 7 | 7 | 7 | 7 |
|  |  |  |  |  | RP131K121B5 | A | M | 0 1 | 6 |  |  |  |  |  | RP131K121D5 RP131K181D5 |  | A | 0 3 | 0 3 | 6 |
|  |  |  |  |  | RP131K181B5 | A | M |  | 3 |  |  |  |  |  |  |  | A | 1 | 1 | 1 |
|  |  |  |  |  | RP131K281B5 | A | M | 2 | 4 |  |  |  |  |  | RP131K281D5 | A | N | 2 4 | 2 4 | 2 4 |

## RP131Kxx1D Series

## RP131H SERIES MARK SPECIFICATION

## · SOT-89-5

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_077.png)

c to f : Product Code (Refer to Part Number vs. Product Code)

g, h : Lot Number

## · Part Number vs. Product Code

## RP131Hxx1B Series

| Part Number | Product - c | Product - d | Product - e | Product - Code f | Product Part - Number | Product Part - c d | Product Part - e | Code f Part Number | Product | Product - c | Product - d | Product - Code e f | Product | Part Number | Product Code - c | Product Code - d e | Product Code - f |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| RP131H081B | U | 0 | 8 | B | RP131H401B | U 4 | 0 | B | RP131H081D | U | 0 | 8 | D | RP131H401D | U 4 | 0 | D |
| RP131H091B | U | 0 | 9 | B | RP131H411B | U 4 | 1 | B | RP131H091D | U | 0 | 9 | D | RP131H411D | U | 4 1 | D |
| RP131H101B | U | 1 | 0 | B | RP131H421B | U 4 | 2 | B | RP131H101D | U | 1 0 | D |  | RP131H421D | U | 4 | 2 D |
| RP131H111B | U | 1 | 1 | B | RP131H431B | U 4 | 3 | B | RP131H111D | U | 1 1 | D | RP131H431D |  | U | 4 | 3 D |
| RP131H121B | U | 1 | 2 | B | RP131H441B | U 4 | 4 | B | RP131H121D | U | 1 2 | D |  | RP131H441D | U | 4 | 4 D |
| RP131H131B | U | 1 | 3 | B | RP131H451B | U 4 | 5 | B | RP131H131D | U | 1 3 | D |  | RP131H451D | U | 4 | 5 D |
| RP131H141B | U | 1 | 4 | B | RP131H461B | U 4 | 6 | B | RP131H141D | U | 1 4 | D |  | RP131H461D | U | 4 | 6 D |
| RP131H151B | U | 1 | 5 | B | RP131H471B | U 4 | 7 | B | RP131H151D | U | 1 5 | D |  | RP131H471D | U | 4 7 | D |
| RP131H161B | U | 1 | 6 | B | RP131H481B | U 4 | 8 | B | RP131H161D | U | 1 6 | D |  | RP131H481D | U | 4 8 | D |
| RP131H171B | U | 1 | 7 | B | RP131H491B | U 4 | 9 | B | RP131H171D | U | 1 | 7 D | RP131H491D |  | U | 4 9 | D |
| RP131H181B | U | 1 | 8 | B | RP131H501B | U 5 | 0 | B | RP131H181D | U | 1 8 | D |  | RP131H501D | U | 5 0 | D |
| RP131H191B | U | 1 | 9 | B | RP131H511B | U 5 | 1 | B | RP131H191D | U | 1 9 | D |  | RP131H511D | U 5 | 1 | D |
| RP131H201B | U | 2 | 0 | B | RP131H521B U | 5 | 2 | B | RP131H201D | U | 2 0 | D |  | RP131H521D | U 5 | 2 | D |
| RP131H211B | U | 2 | 1 | B | RP131H531B | U 5 | 3 | B | RP131H211D | U | 2 1 | D |  | RP131H531D | U | 5 3 | D |
| RP131H221B | U | 2 2 | 2 3 | B | RP131H541B | U 5 U | 4 | B | RP131H221D RP131H231D | U U | 2 2 | D |  | RP131H541D | U U | 5 4 | D |
| RP131H231B | U |  |  | B | RP131H551B | 5 | 5 | B |  |  | 2 3 | D |  | RP131H551D |  | 5 | 5 D |
| RP131H241B | U | 2 | 4 | B | RP131H101B5 | U 0 | 4 | B | RP131H241D | U | 2 4 | D |  | RP131H101D5 | U | 0 | 4 D |
| RP131H251B | U | 2 | 5 | B | RP131H121B5 | U 0 | 1 | B | RP131H251D | U | 2 | 5 D |  | RP131H121D5 | U | 0 | 1 D |
| RP131H261B | U | 2 | 6 | B | RP131H181B5 | 0 | 2 | B | RP131H261D | U | 2 6 | D |  | RP131H181D5 | U | 0 | 2 D |
| RP131H271B | U | 2 | 7 | B | RP131H281B5 U | U 0 | 3 | B | RP131H271D | U | 2 7 | D |  | RP131H281D5 | U | 0 | 3 D |
| RP131H281B | U | 2 | 8 | B |  |  |  |  | RP131H281D | U | 2 8 | D |  |  |  |  |  |
| RP131H291B | U | 2 | 9 | B |  |  |  |  | RP131H291D | U |  | 9 D |  |  |  |  |  |
|  |  |  | 0 |  |  |  |  |  |  |  | 2 |  |  |  |  |  |  |
| RP131H301B | U | 3 |  | B |  |  |  |  | RP131H301D | U | 3 0 | D |  |  |  |  |  |
| RP131H311B | U | 3 | 1 2 | B |  |  |  |  | RP131H311D | U | 3 2 | 1 D |  |  |  |  |  |
| RP131H321B | U | 3 |  | B |  |  |  |  | RP131H321D | U | 3 | D |  |  |  |  |  |
| RP131H331B | U | 3 | 3 | B |  |  |  |  | RP131H331D | U | 3 3 | D |  |  |  |  |  |
| RP131H341B | U | 3 | 4 | B |  |  |  |  | RP131H341D | U | 3 4 | D |  |  |  |  |  |
| RP131H351B | U | 3 | 5 | B |  |  |  |  | RP131H351D | U | 3 5 | D |  |  |  |  |  |
| RP131H361B | U | 3 |  | B |  |  |  |  | RP131H361D | U | 3 6 | D |  |  |  |  |  |
| RP131H371B | U |  | 6 | B |  |  |  |  | RP131H371D | U | 3 7 | D 8 D |  |  |  |  |  |
| RP131H381B | U | 3 3 | 7 8 | B |  |  |  |  | RP131H381D | U | 3 | 9 |  |  |  |  |  |
| RP131H391B | U | 3 | 9 | B |  |  |  |  | RP131H391D | U | 3 | D |  |  |  |  |  |

## RP131Hxx1D Series

## RP131S SERIES MARK SPECIFICATION

## · HSOP-6J

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_078.png)

c to f : Product Code (Refer to Part Number vs. Product Code)

g, h : Lot Number

## · Part Number vs. Product Code

## RP131Sxx1B Series

| Part Number | Product - c | Product - d | Product - e | Product - Code f | Part Number | c d | e f | Product Code | Product - Part Number | Product - c | Product - d | Product - Code e | Product - f | Part Number | Product Code - c | Product Code - d e | Product Code - f |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| RP131S081B | G | 0 | 8 | B | RP131S401B | G 4 | 0 | B | RP131S081D | G | 0 | 8 | D | RP131S401D | G 4 | 0 | D |
| RP131S091B | G | 0 | 9 | B | RP131S411B | G 4 | 1 | B | RP131S091D | G | 0 | 9 | D | RP131S411D | G 4 | 1 | D |
| RP131S101B | G | 1 | 0 | B | RP131S421B | G 4 | 2 | B | RP131S101D | G | 1 | 0 | D | RP131S421D | G | 4 | 2 D |
| RP131S111B | G | 1 | 1 | B | RP131S431B | G 4 | 3 | B | RP131S111D | G | 1 | 1 D | RP131S431D |  | G | 4 3 | D |
| RP131S121B | G | 1 | 2 | B | RP131S441B | G 4 | 4 | B | RP131S121D | G | 1 | 2 D | RP131S441D |  | G | 4 4 | D |
| RP131S131B | G | 1 | 3 | B | RP131S451B | G 4 | 5 | B | RP131S131D | G | 1 | 3 | D | RP131S451D | G | 4 5 | D |
| RP131S141B | G | 1 | 4 | B | RP131S461B | G 4 | 6 | B | RP131S141D | G | 1 | 4 | D | RP131S461D | G | 4 6 | D |
| RP131S151B | G | 1 | 5 | B | RP131S471B | G 4 | 7 | B | RP131S151D | G | 1 | 5 | D | RP131S471D | G | 4 7 | D |
| RP131S161B | G | 1 | 6 | B | RP131S481B | G 4 | 8 | B | RP131S161D | G | 1 | 6 | D | RP131S481D | G | 4 8 | D |
| RP131S171B | G | 1 | 7 | B | RP131S491B | G 4 | 9 | B | RP131S171D | G | 1 7 | D |  | RP131S491D | G | 4 | 9 D |
| RP131S181B | G | 1 | 8 | B | RP131S501B | G 5 | 0 | B | RP131S181D | G | 1 | 8 | D | RP131S501D | G | 5 0 | D |
| RP131S191B | G | 1 | 9 | B | RP131S511B | G 5 | 1 | B | RP131S191D | G | 1 | 9 | D | RP131S511D G | 5 | 1 | D |
| RP131S201B | G | 2 | 0 | B | RP131S521B | G 5 | 2 | B | RP131S201D | G | 2 0 | D |  | RP131S521D | G 5 | 2 | D |
| RP131S211B | G | 2 | 1 | B | RP131S531B | G 5 | 3 | B | RP131S211D | G | 2 | 1 | D | RP131S531D | G 5 | 3 | D |
| RP131S221B | G | 2 | 2 | B | RP131S541B | G 5 | 4 | B | RP131S221D | G | 2 | 2 | D | RP131S541D G |  | 5 4 | D |
| RP131S231B | G | 2 | 3 | B | RP131S551B | G 5 | 5 | B | RP131S231D | G | 2 | 3 | D | RP131S551D | G | 5 | 5 D |
| RP131S241B | G | 2 | 4 | B | RP131S101B5 | G 0 | 4 | B | RP131S241D | G | 2 | 4 | D | RP131S101D5 G |  | 0 | 4 D |
| RP131S251B | G | 2 | 5 | B | RP131S121B5 | G 0 | 1 | B | RP131S251D | G | 2 | 5 | D | RP131S121D5 | G | 0 | 1 D |
| RP131S261B | G | 2 | 6 | B | RP131S181B5 | G 0 | 2 | B | RP131S261D | G | 2 | 6 | D | RP131S181D5 | G | 0 | 2 D |
| RP131S271B | G | 2 | 7 | B | RP131S281B5 | G 0 | 3 | B | RP131S271D | G |  | 7 | D | RP131S281D5 | G | 0 | 3 D |
| RP131S281B | G | 2 | 8 | B |  |  |  |  | RP131S281D | G | 2 2 | 8 D |  |  |  |  |  |
| RP131S291B | G | 2 | 9 | B |  |  |  |  | RP131S291D | G | 2 | 9 | D |  |  |  |  |
| RP131S301B | G | 3 | 0 | B |  |  |  |  | RP131S301D | G | 3 | 0 | D |  |  |  |  |
| RP131S311B | G | 3 | 1 | B |  |  |  |  | RP131S311D | G | 3 | 1 | D |  |  |  |  |
| RP131S321B | G | 3 | 2 | B |  |  |  |  | RP131S321D | G | 3 | 2 | D |  |  |  |  |
| RP131S331B | G | 3 | 3 | B |  |  |  |  |  | G | 3 | 4 | D |  |  |  |  |
|  | G | 3 | 4 |  |  |  |  |  | RP131S331D |  | 3 | 3 | D |  |  |  |  |
| RP131S341B RP131S351B | G | 3 | 5 | B B |  |  |  |  | RP131S341D RP131S351D | G G | 3 | 5 | D |  |  |  |  |
| RP131S361B | G | 3 | 6 |  |  |  |  |  | RP131S361D | G |  | 6 | D |  |  |  |  |
|  |  |  |  | B |  |  |  |  |  |  | 3 |  |  |  |  |  |  |
| RP131S371B RP131S381B RP131S391B | G G G | 3 3 3 | 7 8 9 | B B B |  |  |  |  | RP131S371D RP131S381D RP131S391D | G G G | 3 3 3 | 7 D 8 9 D | D |  |  |  |  |

## RP131Sxx1D Series

## RP131J SERIES MARK SPECIFICATION

## · TO-252-5-P2

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_079.png)

c to j : Product Code (Refer to Part Number vs. Product Code)

k, l : Lot Number

## · Part Number vs. Product Code

## RP131Jxx1B Series

| Part Number | Product Code - c | Product Code - d | Product Code - e | Product Code - f | Product Code - g | Product Code - h | Product Code - i | Product Code - j |
| - | - | - | - | - | - | - | - | - |
| RP131J081B | D | 1 | J | 0 | 8 | 1 | B |  |
| RP131J091B | D | 1 | J | 0 | 9 | 1 | B |  |
| RP131J101B | D | 1 | J | 1 | 0 | 1 | B |  |
| RP131J111B | D | 1 | J | 1 | 1 | 1 | B |  |
| RP131J121B | D | 1 | J | 1 | 2 | 1 | B |  |
| RP131J131B | D | 1 | J | 1 | 3 | 1 | B |  |
| RP131J141B | D | 1 | J | 1 | 4 | 1 | B |  |
| RP131J151B | D | 1 | J | 1 | 5 | 1 | B |  |
| RP131J161B | D | 1 | J | 1 | 6 | 1 | B |  |
| RP131J171B | D | 1 | J | 1 | 7 | 1 | B |  |
| RP131J181B | D | 1 | J | 1 | 8 | 1 | B |  |
| RP131J191B | D | 1 | J | 1 | 9 | 1 | B |  |
| RP131J201B | D | 1 | J | 2 | 0 | 1 | B |  |
| RP131J211B | D | 1 | J | 2 | 1 | 1 | B |  |
| RP131J221B | D | 1 | J | 2 | 2 | 1 | B |  |
| RP131J231B | D | 1 | J | 2 | 3 | 1 | B |  |
| RP131J241B | D | 1 | J | 2 | 4 | 1 | B |  |
| RP131J251B | D | 1 | J | 2 | 5 | 1 | B |  |
| RP131J261B | D | 1 | J | 2 | 6 | 1 | B |  |
| RP131J271B | D | 1 | J | 2 | 7 | 1 | B |  |
| RP131J281B | D | 1 | J | 2 | 8 | 1 | B |  |
| RP131J291B | D | 1 | J | 2 | 9 | 1 | B |  |
| RP131J301B | D | 1 | J | 3 | 0 | 1 | B |  |
| RP131J311B | D | 1 | J | 3 | 1 | 1 | B |  |
| RP131J321B | D | 1 | J | 3 | 2 | 1 | B |  |
| RP131J331B | D | 1 | J | 3 | 3 | 1 | B |  |
| RP131J341B | D | 1 | J | 3 | 4 | 1 | B |  |
| RP131J351B | D | 1 | J | 3 | 5 | 1 | B |  |
| RP131J361B | D | 1 | J | 3 | 6 | 1 | B |  |
| RP131J371B | D | 1 | J | 3 | 7 | 1 | B |  |
| RP131J381B | D | 1 | J | 3 | 8 | 1 | B |  |
| RP131J391B | D | 1 | J | 3 | 9 | 1 | B |  |
| RP131J401B | D | 1 | J | 4 | 0 | 1 | B |  |
| RP131J411B | D | 1 | J | 4 | 1 | 1 | B |  |
| RP131J421B | D | 1 | J | 4 | 2 | 1 | B |  |
| RP131J431B | D | 1 | J | 4 | 3 | 1 | B |  |
| RP131J441B | D | 1 | J | 4 | 4 | 1 | B |  |
| RP131J451B | D | 1 | J | 4 | 5 | 1 | B |  |
| RP131J461B | D | 1 | J | 4 | 6 | 1 | B |  |

Product Code

Part Number c d e f g h i j

RP131J301D D 1 J 3 0 1 D

RP131J311D D 1 J 3 1 1 D

RP131J321D D 1 J 3 2 1 D

RP131J331D D 1 J 3 3 1 D

RP131J341D D 1 J 3 4 1 D

RP131J351D D 1 J 3 5 1 D

RP131J361D D 1 J 3 6 1 D

RP131J371D D 1 J 3 7 1 D

RP131J381D D 1 J 3 8 1 D

RP131J391D D 1 J 3 9 1 D

RP131J401D D 1 J 4 0 1 D

RP131J411D D 1 J 4 1 1 D

RP131J421D D 1 J 4 2 1 D

RP131J431D D 1 J 4 3 1 D

RP131J441D D 1 J 4 4 1 D

RP131J451D D 1 J 4 5 1 D

RP131J461D D 1 J 4 6 1 D

RP131J471D D 1 J 4 7 1 D

RP131J481D D 1 J 4 8 1 D

RP131J491D D 1 J 4 9 1 D

RP131J501D D 1 J 5 0 1 D

RP131J511D D 1 J 5 1 1 D

RP131J521D D 1 J 5 2 1 D

RP131J531D D 1 J 5 3 1 D

RP131J541D D 1 J 5 4 1 D

RP131J551D D 1 J 5 5 1 D

RP131J101D5 D 1 J 1 0 1 D 5

RP131J121D5 D 1 J 1 2 1 D 5

RP131J181D5 D 1 J 1 8 1 D 5

RP131J281D5 D 1 J 2 8 1 D 5

Product Code

Part Number c d e f g h i j

RP131J471B D 1 J 4 7 1 B

RP131J481B D 1 J 4 8 1 B

RP131J491B D 1 J 4 9 1 B

RP131J501B D 1 J 5 0 1 B

RP131J511B D 1 J 5 1 1 B

RP131J521B D 1 J 5 2 1 B

RP131J531B D 1 J 5 3 1 B

RP131J541B D 1 J 5 4 1 B

RP131J551B D 1 J 5 5 1 B

RP131J101B5 D 1 J 1 0 1 B 5

RP131J121B5 D 1 J 1 2 1 B 5

RP131J181B5 D 1 J 1 8 1 B 5

RP131J281B5 D 1 J 2 8 1 B 5

## RP131Jxx1D Series

Product Code

Part Number c d e f g h i j

RP131J081D D 1 J 0 8 1 D

RP131J091D D 1 J 0 9 1 D

RP131J101D D 1 J 1 0 1 D

RP131J111D D 1 J 1 1 1 D

RP131J121D D 1 J 1 2 1 D

RP131J131D D 1 J 1 3 1 D

RP131J141D D 1 J 1 4 1 D

RP131J151D D 1 J 1 5 1 D

RP131J161D D 1 J 1 6 1 D

RP131J171D D 1 J 1 7 1 D

RP131J181D D 1 J 1 8 1 D

RP131J191D D 1 J 1 9 1 D

RP131J201D D 1 J 2 0 1 D

RP131J211D D 1 J 2 1 1 D

RP131J221D D 1 J 2 2 1 D

RP131J231D D 1 J 2 3 1 D

RP131J241D D 1 J 2 4 1 D

RP131J251D D 1 J 2 5 1 D

RP131J261D D 1 J 2 6 1 D

RP131J271D D 1 J 2 7 1 D

RP131J281D D 1 J 2 8 1 D

RP131J291D D 1 J 2 9 1 D

## POWER DISSIPATION

PD-DFN1616-6B-(85125150)-JE-B

The power dissipation of the package is dependent on PCB material, layout, and environmental conditions. The following measurement conditions are based on JEDEC STD. 51.

## Measurement Conditions

| Item | Measurement Conditions |
| - | - |
| Environment | Mounting on Board (Wind Velocity = 0 m/s) |
| Board Material | Glass Cloth Epoxy Plastic (Four-Layer Board) |
| Board Dimensions | 76.2 mm × 114.3 mm × 0.8 mm |
| Copper Ratio | Outer Layer (First Layer): Less than 95% of 50 mm Square Inner Layers (Second and Third Layers): Approx. 100% of 50 mm Square Outer Layer (Fourth Layer): Approx. 100% of 50 mm Square |
| Through-holes | φ 0.2 mm × 25 pcs |

## Measurement Result

(Ta = 25°C, Tjmax = 125°C)

| Item | Measurement Result |
| - | - |
| Power Dissipation | 2400 mW |
| Thermal Resistance (θja) | θja = 41°C/W |
| Thermal Characterization Parameter (ψjt) | ψjt = 11°C/W |

θja: Junction-to-Ambient Thermal Resistance

ψjt: Junction-to-Top Thermal Characterization Parameter

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_080.png)

76.2

Power Dissipation vs. Ambient Temperature Measurement Board Pattern

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_081.png)

The above graph shows the power dissipation of the package at Tjmax = 125°C and Tjmax = 150°C. Operating the device in the hatched range might have a negative influence on its lifetime. The total hours of use and the total years of use must be limited as follows:

| Total Hours of Use | Total Years of Use (4 hours/day) |
| - | - |
| 13,000 hours | 9 years |

*

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_082.png)

DFN1616-6B Package Dimensions (Unit: mm)

� The tab on the bottom of the package shown by blue circle is a substrate potential (GND). It is recommended that this tab be connected to the ground plane pin on the board but it is possible to leave the tab floating.

Ver. A

PD-DFN(PL)1820-6-(85125150)-JE-B

The power dissipation of the package is dependent on PCB material, layout, and environmental conditions. The following measurement conditions are based on JEDEC STD. 51.

## Measurement Conditions

| Item | Measurement Conditions |
| - | - |
| Environment | Mounting on Board (Wind Velocity = 0 m/s) |
| Board Material | Glass Cloth Epoxy Plastic (Four-Layer Board) |
| Board Dimensions | 76.2 mm × 114.3 mm × 0.8 mm |
| Copper Ratio | Outer Layer (First Layer): Less than 95% of 50 mm Square Inner Layers (Second and Third Layers): Approx. 100% of 50 mm Square Outer Layer (Fourth Layer): Approx. 100% of 50 mm Square |
| Through-holes | φ 0.2 mm × 36 pcs |

## Measurement Result

(Ta = 25°C, Tjmax = 125°C)

| Item | Measurement Result |
| - | - |
| Power Dissipation | 2200 mW |
| Thermal Resistance (θja) | θja = 45°C/W |
| Thermal Characterization Parameter (ψjt) | ψjt = 18°C/W |

θja: Junction-to-Ambient Thermal Resistance

ψjt: Junction-to-Top Thermal Characterization Parameter

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_083.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_084.png)

Power Dissipation vs. Ambient Temperature Measurement Board Pattern The above graph shows the power dissipation of the package at Tjmax = 125°C and Tjmax = 150°C. Operating the device in the hatched range might have a negative influence on its lifetime. The total hours of use and the total years of use must be limited as follows:

| Total Hours of Use | Total Years of Use (4 hours/day) |
| - | - |
| 13,000 hours | 9 years |

*

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_085.png)

DFN(PL)1820-6 Package Dimensions (Unit: mm)

� The tab on the bottom of the package is substrate level (GN'). It is recommended that the tab be connected to the ground plane on the board, or otherwise be left floating.

Ver. A

Ver. A

The power dissipation of the package is dependent on PCB material, layout, and environmental conditions. The following measurement conditions are based on JEDEC STD. 51-7.

## Measurement Conditions

| Item | Measurement Conditions |
| - | - |
| Environment | Mounting on Board (Wind Velocity = 0 m/s) |
| Board Material | Glass Cloth Epoxy Plastic (Four-Layer Board) |
| Board Dimensions | 76.2 mm × 114.3 mm × 0.8 mm |
| Copper Ratio | Outer Layer (First Layer): Less than 95% of 50 mm Square Inner Layers (Second and Third Layers): Approx. 100% of 50 mm Square Outer Layer (Fourth Layer): Approx. 100% of 50 mm Square |
| Through-holes | I0.3mm ×13pcs |

## Measurement Result

| Item | Measurement Result |
| - | - |
| Power Dissipation | 2600 mW |
| Thermal Resistance (Tja) | Tja = 38°C/W |
| Thermal Characterization Parameter (ȥjt) | ȥjt = 13°C/W |

Tja: Junction-to-Ambient Thermal Resistance

ȥjt: Junction-to-Top Thermal Characterization Parameter

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_086.png)

Power Dissipation vs. Ambient Temperature

(Ta = 25°C, Tjmax = 125°C)

76.2

Measurement Board Pattern

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_087.png)

The above graph shows the power dissipation of the package at Tjmax = 125°C and Tjmax = 150°C. Operating the device in the hatched range might have a negative influence on its lifetime. The total hours of use and the total years of use must be limited as follows:

| Total Hours of Use | Total Years of Use (4 hours/day) |
| - | - |
| 13,000 hours | 9 years |

Ver. A

627����� Package Dimensions

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_088.png)

Ver. A

The power dissipation of the package is dependent on PCB material, layout, and environmental conditions. The following measurement conditions are based on JEDEC STD. 51-7.

## Measurement Conditions

| Item | Measurement Conditions |
| - | - |
| Environment | Mounting on Board (Wind Velocity = 0 m/s) |
| Board Material | Glass Cloth Epoxy Plastic (Four-Layer Board) |
| Board Dimensions | 76.2 mm × 114.3 mm × 0.8 mm |
| Copper Ratio | Outer Layer (First Layer): Less than 95% of 50 mm Square Inner Layers (Second and Third Layers): Approx. 100% of 50 mm Square Outer Layer (Fourth Layer): Approx. 100% of 50 mm Square |
| Through-holes | I0.3mm ×28pcs |

## Measurement Result

| Item | Measurement Result |
| - | - |
| Power Dissipation | 2700 mW |
| Thermal Resistance (Tja) | Tja = 37°C/W |
| Thermal Characterization Parameter (ȥjt) | ȥjt = 7°C/W |

Tja: Junction-to-Ambient Thermal Resistance

ȥjt: Junction-to-Top Thermal Characterization Parameter

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_089.png)

Power Dissipation vs. Ambient Temperature

(Ta = 25°C, Tjmax = 125°C)

Measurement Board Pattern

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_090.png)

The above graph shows the power dissipation of the package at Tjmax = 125°C and Tjmax = 150°C. Operating the device in the hatched range might have a negative influence on its lifetime. The total hours of use and the total years of use must be limited as follows:

| Total Hours of Use | Total Years of Use (4 hours/day) |
| - | - |
| 13,000 hours | 9 years |

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_091.png)

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_092.png)

+623��- Package Dimensions

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_093.png)

UNIT: mm

Ver. A

Ver. A

The power dissipation of the package is dependent on PCB material, layout, and environmental conditions. The following measurement conditions are based on JEDEC STD. 51-7.

## Measurement Conditions

| Item | Measurement Conditions |
| - | - |
| Environment | Mounting on Board (Wind Velocity = 0 m/s) |
| Board Material | Glass Cloth Epoxy Plastic (Four-Layer Board) |
| Board Dimensions | 76.2 mm × 114.3 mm × 0.8 mm |
| Copper Ratio | Outer Layer (First Layer): Less than 95% of 50 mm Square Inner Layers (Second and Third Layers): Approx. 100% of 50 mm Square Outer Layer (Fourth Layer): Approx. 100% of 50 mm Square |
| Through-holes | I0.3mm ×21pcs |

## Measurement Result

| Item | Measurement Result |
| - | - |
| Power Dissipation | 3800 mW |
| Thermal Resistance (Tja) | Tja = 26°C/W |
| Thermal Characterization Parameter (ȥjt) | ȥjt = 7°C/W |

Tja: Junction-to-Ambient Thermal Resistance

ȥjt: Junction-to-Top Thermal Characterization Parameter

Power Dissipation vs. Ambient Temperature

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_094.png)

(Ta = 25°C, Tjmax = 125°C)

Measurement Board Pattern

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_095.png)

The above graph shows the power dissipation of the package at Tjmax = 125°C and Tjmax = 150°C. Operating the device in the hatched range might have a negative influence on its lifetime. The total hours of use and the total years of use must be limited as follows:

| Total Hours of Use | Total Years of Use (4 hours/day) |
| - | - |
| 13,000 hours | 9 years |

72�������3� Package Dimensions

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_096.png)

Ver. A

� The tab on the bottom of the package shown by blue circle is a substrate potential (GND). It is recommended that this tab be connected to the ground plane on the board but it is possible to leave the tab floating.

1. The products and the product specifications described in this document are subject to change or discontinuation of production without notice for reasons such as improvement. Therefore, before deciding to use the products, please refer to our sales representatives for the latest information thereon.
2. The materials in this document may not be copied or otherwise reproduced in whole or in part without the prior written consent of us.
3. This product and any technical information relating thereto are subject to complementary export controls (so-called KNOW controls) under the Foreign Exchange and Foreign Trade Law, and related politics ministerial ordinance of the law. (Note that the complementary export controls are inapplicable to any application-specific products, except rockets and pilotless aircraft, that are insusceptible to design or program changes.) Accordingly, when exporting or carrying abroad this product, follow the Foreign Exchange and Foreign Trade Control Law and its related regulations with respect to the complementary export controls.
4. The technical information described in this document shows typical characteristics and example application circuits for the products. The release of such information is not to be construed as a warranty of or a grant of license under our or any third party's intellectual property rights or any other rights.
5. The products listed in this document are intended and designed for use as general electronic components in standard applications (office equipment, telecommunication equipment, measuring instruments, consumer electronic products, amusement equipment etc.). Those customers intending to use a product in an application requiring extreme quality and reliability, for example, in a highly specific application where the failure or misoperation of the product could result in human injury or death should first contact us.
- Aerospace Equipment
- Equipment Used in the Deep Sea
- Power Generator Control Equipment (nuclear, steam, hydraulic, etc.)
- Life Maintenance Medical Equipment
- Fire Alarms / Intruder Detectors
- Vehicle Control Equipment (automotive, airplane, railroad, ship, etc.)
- Various Safety Devices
- Traffic control system
- Combustion equipment

In case your company desires to use this product for any applications other than general electronic equipment mentioned above, make sure to contact our company in advance. Note that the important requirements mentioned in this section are not applicable to cases where operation requirements such as application conditions are confirmed by our company in writing after consultation with your company.

6. We are making our continuous effort to improve the quality and reliability of our products, but semiconductor products are likely to fail with certain probability. In order to prevent any injury to persons or damages to property resulting from such failure, customers should be careful enough to incorporate safety measures in their design, such as redundancy feature, fire containment feature and fail-safe feature. We do not assume any liability or responsibility for any loss or damage arising from misuse or inappropriate use of the products.
7. The products have been designed and tested to function within controlled environmental conditions. Do not use products under conditions that deviate from methods or applications specified in this datasheet. Failure to employ the products in the proper applications can lead to deterioration, destruction or failure of the products. We shall not be responsible for any bodily injury, fires or accident, property damage or any consequential damages resulting from misuse or misapplication of the products.
8. Quality Warranty
4. 8-1. Quality Warranty Period

In the case of a product purchased through an authorized distributor or directly from us, the warranty period for this product shall be one (1) year after delivery to your company. For defective products that occurred during this period, we will take the quality warranty measures described in section 8-2. However, if there is an agreement on the warranty period in the basic transaction agreement, quality assurance agreement, delivery specifications, etc., it shall be followed.

- 8-2. Quality Warranty Remedies

When it has been proved defective due to manufacturing factors as a result of defect analysis by us, we will either deliver a substitute for the defective product or refund the purchase price of the defective product.

Note that such delivery or refund is sole and exclusive remedies to your company for the defective product.

8-3. Remedies after Quality Warranty Period With respect to any defect of this product found after the quality warranty period, the defect will be analyzed by us. On the basis of the defect analysis results, the scope and amounts of damage shall be determined by mutual agreement of both parties. Then we will deal with upper limit in Section 8-2. This provision is not intended to limit any legal rights of your company.

9. Anti-radiation design is not implemented in the products described in this document.
10. The X-ray exposure can influence functions and characteristics of the products. Confirm the product functions and characteristics in the evaluation stage.
11. WLCSP products should be used in light shielded environments. The light exposure can influence functions and characteristics of the products under operation or storage.
12. Warning for handling Gallium and Arsenic (GaAs) products (Applying to GaAs MMIC, Photo Reflector). These products use Gallium (Ga) and Arsenic (As) which are specified as poisonous chemicals by law. For the prevention of a hazard, do not burn, destroy, or process chemically to make them as gas or power. When the product is disposed of, please follow the related regulation and do not mix this with general industrial waste or household waste.
13. Please contact our sales representatives should you have any questions or comments concerning the products or the technical information.

![Image](RP131x%20Datasheet%20%28Ricoh%29_files/img_097.png)

Official website https://www.nisshinbo-microdevices.co.jp/en/ Purchase information

https://www.nisshinbo-microdevices.co.jp/en/buy/
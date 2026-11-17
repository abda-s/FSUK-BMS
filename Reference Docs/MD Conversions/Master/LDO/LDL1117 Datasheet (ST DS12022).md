<!-- Converted from LDL1117 Datasheet (ST DS12022).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_001.png)

S

## Datasheet

## 1.2 A high PSRR low-dropout linear voltage regulator

## Features

- Input voltage from 2.5 V to 18 V
- 20 V AMR
- Available on fixed output voltages: 1.2 V (1.185 V), 1.5 V, 1.8 V, 2.5 V, 3 V, 3.3 V, 5.0 V (other options are available on request)
- Guaranteed output current 1.2 A
- Typical dropout 350 mV @ 1.2 A
- Internal thermal, current and power limitation
- High PSRR 87 dB @ 120 Hz
- Operating temperature range: -40 °C to 125°C
- Package SOT223

## Applications

- Consumer
- Industrial
- SMPS
- Motherboard P.O.L.
- DC-DC post-regulation

## Description

The LDL1117 provides 1.2 A of maximum current with an input voltage range from 2.5 V to 18 V, and a typical dropout voltage of 350 mV @ 1.2 A.

The high power supply rejection ratio of 87 dB at 120 Hz, rolling down to more than 40 dB at 100 kHz, makes the LDL1117 suitable for direct regulations in SMPS and secondary linear regulations in DC-DC converters.

This device includes current limit, SOA and thermal protections.

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_002.png)

SOT223

Maturity status link

[LDL1117](https://www.st.com/en/product/LDL1117?ecmp=tt9470_gl_link_feb2019&rt=ds&id=DS12022)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_003.png)

## 1 Diagram

Figure 1. Block diagram

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_004.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_005.png)

## 2 Pin configuration

Figure 2. Pin connection (top view)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_006.png)

VIN

Table 1. Pin description

| Pin name | Pin number | Description |
| - | - | - |
| GND | 1 | Ground |
| VOUT | 2 | Output voltage |
| VIN | 3 | Input voltage |

Note: The tab is connected to VOUT.

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_003.png)

## 3

## Typical application

Figure 3. Typical application diagram

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_007.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_008.png)

G

## 4 Maximum ratings

Table 2. Absolute maximum ratings

| Symbol | Parameter | Value | Unit |
| - | - | - | - |
| VIN | Input supply voltage | -0.3 to 20 | V |
| VOUT | Output voltage | -0.3 to VIN + 0.3 | V |
| IOUT | Output current | Internally limited | A |
| PD | Power dissipation | Internally limited | W |
| TJ-OP | Operating junction temperature | - 40 to 125 | °C |
| TJ-MAX | Maximum junction temperature | 150 | °C |
| TSTG | Storage temperature | - 55 to 150 | °C |

Note: Absolute maximum ratings are those values beyond which damage to the device may occur. Functional operation under these conditions is not implied.

Table 3. Thermal data

| Symbol | Parameter | Value | Unit |
| - | - | - | - |
| θJ-C | Thermal resistance junction-to-case | 15 | °C/W |
| θJ-A | Thermal resistance junction-to-ambient | 120 | °C/W |

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_003.png)

G

## 5 Electrical characteristics

TJ = 25 °C, VIN = VOUT + 1 V or 2.6 V, whichever is greater; CIN = 1 μF; COUT = 4.7 μF; IOUT = 10 mA.

Table 4. Electrical characteristics

| Symbol | Parameter | Test conditions | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - | - |
| VIN | Operating input voltage |  | 2.6 |  | 18 | V |
| VUVLO | Turn-on threshold |  |  | 2.3 | 2.4 | V |
| VUVLO | Hysteresis |  |  | 200 |  | mV |
| VOUT | VOUT accuracy | IOUT = 10 mA, TJ = 25 °C | -2 |  | +2 | % |
| VOUT | VOUT accuracy | IOUT = 10 mA, -40 °C < TJ < 125°C | -3 |  | +3 | % |
| ∆VOUT | Line regulation | VOUT + 1 V (1) ≤ VIN ≤ 18 V, IOUT = 10 mA -40 °C < TJ< 125 °C |  | 0.002 | 0.02 | %/V |
| ∆VOUT | Load regulation | IOUT = 10 mA to 1.2 A, - 40 °C < TJ < 125 °C |  | 5 | 15 | mV |
| VDROP | Dropout voltage (2) | IOUT = 1.2 A, VOUT > 2.5 V - 40°C < TJ < 125 °C |  | 350 | 600 | mV |
| eN | Output noise voltage | 10 Hz to 100 kHz, IOUT = 100 mA |  | 60 |  | µVRMS/ VOUT |
| SVR | Supply voltage rejection | VIN = VOUT(NOM) +1 V ± VRIPPLE VRIPPLE = 0.5 V, f = 120 Hz |  | 87 |  | dB |
| SVR | Supply voltage rejection | VIN = VOUT(NOM) +1 V ± VRIPPLE VRIPPLE = 0.5 V, f = 1 kHz |  | 80 |  | dB |
| SVR | Supply voltage rejection | VIN= VOUT(NOM) +1 V ± VRIPPLE VRIPPLE = 0.5 V, f = 100 kHz |  | 65 |  | dB |
| IQ | Quiescent current | IOUT = 0 mA to 1.2 A, -40 °C < TJ < 125 °C |  | 250 | 500 | µA |
| ISC | Output current |  | 1.5 | 2 |  | A |
| TSHDN | Thermal shutdown |  |  | 175 |  | °C |
| TSHDN | Hysteresis |  |  | 25 |  | °C |

1. VIN = VOUT + 1 V or 2.6 V, whichever is greater.

2. Dropout voltage is the input-to-output voltage difference at which the output voltage is 100 mV below its nominal value; this specification does not apply for nominal output voltages below 2.5 V.

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_008.png)

G

## 6 Application information

## 6.1 Thermal and short-circuit protections

The LDL1117 is self-protected from short-circuit conditions and overtemperature. When the output load is higher than the one supported by the device, the output current rises until the limit of typically 2 A is reached. The current limit value is dependent of the dissipated power, thanks to an additional SOA protection, so that the maximum power is limited.

The peak current available for a defined drop voltage (VIN-VOUT) is shown in Section 7 .

The thermal protection occurs when the junction temperature reaches typically 175 °C. The IC enters the shutdown status. As soon as the junction temperature falls again below 150 °C (typ.) the device starts working again.

In order to calculate the maximum power that the device can dissipate, keeping the junction temperature below TJ-OP, the following formula is used: PDMAX = 125- TAMB / RTHJ -A (1) PDMAX should be also derated according to the maximum current allowed by the SOA protection.

## 6.2 Input and output capacitor selection

The LDL1117 requires external capacitors to assure the regulator control loop stability.

Any good quality ceramic capacitor can be used but, the X5R and the X7R are suggested since they guarantee a very stable combination of capacitance and ESR over the temperature range. The input/output capacitors should be placed as close as possible to the relative pins. The LDL1117 requires an input capacitor with a minimum value of 1 μF.

The device is also equipped with a differential thermal protection that avoid damage in case of fast thermal gradients inside the chip. When the differential thermal protection is activated both channel and the LDO are switched off. This protection works in auto-retry mode, the device restarts automatically when the thermal conditions go back into the normal operating region.

This capacitor must be placed as close as possible to the input pin of the device and returned to a clean analog ground. The control loop of the LDL1117 is designed to work with an output ceramic capacitor. Other type of capacitors may be used, as long as they meet the requirements of minimum capacitance and equivalent series resistance (ESR), as shown in Figure 20 and Figure 21.

To assure stability, the output capacitor must maintain its ESR and capacitance in the stable region, over the full operating temperature range.

The suggested combination of 1 μF input and 4.7 μF output capacitors offers a good compromise among the stability of the regulator, optimum transient response and total PCB area occupation.

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

G

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_010.png)

## 7 Typical characteristics

The following plots are referred to the typical application circuit and, unless otherwise noted, at TA = 25 °C.

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_011.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_012.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_013.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_014.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_015.png)

Figure 10. Load regulation vs. temperature (VIN = 6 V, VOUT = 5 V, IOUT = 10 to 1200 mA)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_016.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_017.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_018.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_019.png)

Figure 14. Quiescent current vs. temperature (600 mA)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_020.png)

Temperature [°C]

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_021.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_022.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_023.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_024.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

G

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_025.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_026.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_027.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_028.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_029.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_030.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

G

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_031.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_008.png)

G

## 8 Package information

In order to meet environmental requirements, ST offers these devices in different grades of ECOPACK packages, depending on their level of environmental compliance. ECOPACK specifications, grade definitions and product status are available at: www.st.com. ECOPACK is an ST trademark.

## 8.1 SOT223 package information

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_032.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_033.png)

Figure 28. SOT223 package outline

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_034.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_005.png)

Table 5. SOT223 mechanical data

| Dim. | mm - Min. | mm - Typ. | mm - Max. |
| - | - | - | - |
| A |  |  | 1.8 |
| A1 | 0.02 |  | 0.1 |
| B | 0.6 | 0.7 | 0.85 |
| B1 | 2.9 | 3 | 3.15 |
| c | 0.24 | 0.26 | 0.35 |
| D | 6.3 | 6.5 | 6.7 |
| e |  | 2.3 |  |
| e1 |  | 4.6 |  |
| E | 3.3 | 3.5 | 3.7 |
| H | 6.7 | 7.0 | 7.3 |
| V |  |  | 10º |

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

G

## 8.2 SOT223 packing information

Table 6. SOT223 tape and reel mechanical data

| Tape - Dim. | Tape - mm - Min. | Tape - mm - Typ. | Tape - mm - Max. | Reel - Dim. | Reel - mm - Min. | Reel - mm - Max. |
| - | - | - | - | - | - | - |
| A0 | 6.75 | 6.85 | 6.95 | A |  | 180 |
| B0 | 7.30 | 7.40 | 7.50 | N | 60 |  |
| K0 | 1.80 | 1.90 | 2.00 | W1 |  | 12.4 |
| F | 5.40 | 5.50 | 5.60 | W2 |  | 18.4 |
| E | 1.65 | 1.75 | 1.85 | W3 | 11.9 | 15.4 |
| W | 11.7 | 12 | 12.3 |  |  |  |
| P2 | 1.90 | 2 | 2.10 | Basequantity pcs | Basequantity pcs | 1000 |
| P0 | 3.90 | 4 | 4.10 | Bulk quantity pcs | Bulk quantity pcs | 1000 |
| P1 | 7.90 | 8 | 8.10 |  |  |  |
| T | 0.25 | 0.30 | 0.35 |  |  |  |
| D | 1.50 | 1.55 | 1.60 |  |  |  |
| D1 | 1.50 | 1.60 | 1.70 |  |  |  |

Figure 29. Tape for SOT223 (dimensions are in mm)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_035.png)

Figure 30. Reel for SOT223 (dimensions are in mm)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_005.png)

Figure 31. SOT223 reel oriented

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_036.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_037.png)

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_005.png)

## 9 Ordering information

Table 7. Order code

| Part number | Marking | Order code | Output voltage (V) |
| - | - | - | - |
| LDL1117 | LL12 | LDL1117S12R | 1.185 |
| LDL1117 | LL15 | LDL1117S15R | 1.5 |
| LDL1117 | LL18 | LDL1117S18R | 1.8 |
| LDL1117 | LL25 | LDL1117S25R | 2.5 |
| LDL1117 | LL30 | LDL1117S30R | 3.0 |
| LDL1117 | LL33 | LDL1117S33R | 3.3 |
| LDL1117 | LL50 | LDL1117S50R | 5.0 |

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

## Revision history

Table 8. Document revision history

| Date | Revision | Changes |
| - | - | - |
| 27-Feb-2017 | 1 | Initial release. |
| 30-Mar-2017 | 2 | Updated features in cover page and Section 9: "Ordering information". Minor text changes. |
| 04-Jul-2017 | 3 | In Table3: "Thermal data": - thermal data values changed. Minor textchanges. |
| 04-Mar-2020 | 4 | Updated Figure 28. SOT223 package outline. |
| 24-Mar-2020 | 5 | Updated Figure 12. |
| 03-Apr-2020 | 6 | Added Section 8.2 SOT223 packing information. |

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

## Contents

| 1 | Diagram...........................................................................2 | Diagram...........................................................................2 |  |
| - | - | - | - |
| 2 | Pin configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Pin configuration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . .3 |
| 3 | Typical application. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Typical application. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . .4 |
| 4 | Maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . .5 |
| 5 | Electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Electrical characteristics. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . .6 |
| 6 | Application information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Application information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . .7 |
|  | 6.1 | Thermal and short-circuit protections . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 |
|  | 6.2 | Input and output capacitor selection . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7 |
| 7 | Typical characteristics . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .8 |
| 8 | Package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Package information. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . .14 |
|  | 8.1 | SOT223 package information . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14 |
|  | 8.2 | SOT223 packing information . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 |
| 9 | Ordering information . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .18 |
| Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | Revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | .19 |

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

## List of tables

| Table 1. | Pin description. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3 |
| - | - | - |
| Table 2. | Absolute maximum ratings . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 |
| Table 3. | Thermal data. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5 |
| Table 4. | Electrical characteristics . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6 |
| Table 5. | SOT223 mechanical data . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15 |
| Table 6. | SOT223 tape and reel mechanical data . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16 |
| Table 7. | Order code . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18 |
| Table 8. | Document revision history . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19 |

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_009.png)

G

## List of figures

| Figure 1. | Block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . 2 |
| - | - | - |
| Figure 2. | Pin connection (top view) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . 3 |
| Figure 3. | Typical application diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . 4 |
| Figure 4. | Output voltage vs. temperature (VIN = 2.6 V, VOUT = 1.2 V, no load) . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . 8 |
| Figure 5. | Output voltage vs. temperature (VIN = 2.6 V, VOUT = 1.2 V, 1200 mA) . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . 8 |
| Figure 6. | Output voltage vs. temperature (VIN = 6 V, VOUT = 5 V, no load) . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . 8 |
| Figure 7. | Output voltage vs. temperature (VIN = 6 V, VOUT = 5 V, 1200 mA) . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . 8 |
| Figure 8. | Line regulation vs. temperature (VIN = 6 to 18 V, VOUT = 5 V, IOUT = 10 mA) . . . . . | . . . . . . . . . . . . . . . . . . . . . 9 |
| Figure 9. | Line regulation vs. temperature (VIN = 2.5 to 18 V, VOUT = 1.2 V, IOUT = 10 mA) . . | . . . . . . . . . . . . . . . . . . . . . 9 |
| Figure 10. | Load regulation vs. temperature (VIN = 6 V, VOUT = 5 V, IOUT = 10 to 1200 mA) . . | . . . . . . . . . . . . . . . . . . . . . 9 |
| Figure 11. | Load regulation vs. temperature (VIN = 2.6 V, VOUT = 1.2 V, IOUT = 10 to 1200 mA) | . . . . . . . . . . . . . . . . . . . . . 9 |
| Figure 12. | Dropout voltage vs. temperature . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 10 |
| Figure 13. | Quiescent current vs. temperature (no load) . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 10 |
| Figure 14. | Quiescent current vs. temperature (600 mA). . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 10 |
| Figure 15. | Quiescent current vs. temperature (1.2 A) . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 10 |
| Figure 16. | Short-circuit current vs. dropout voltage (VOUT = 5 V) . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 11 |
| Figure 17. | Short-circuit current vs. dropout voltage (VOUT = 1.2 V) . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 11 |
| Figure 18. | SVR vs. frequency . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 11 |
| Figure 19. | Output noise spectral density (VO = 1.2 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 11 |
| Figure 20. | Stability plan (VOUT = 5 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 12 |
| Figure 21. | Stability plan (VOUT = 1.2 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 12 |
| Figure 22. | Turn-on time (VOUT = 5 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 12 |
| Figure 23. | Turn-on time (VOUT = 1.2 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 12 |
| Figure 24. | Line transient (VOUT = 5 V). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 12 |
| Figure 25. | Line transient (VOUT = 1.2 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 12 |
| Figure 26. | Load transient (VOUT = 1.2 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 13 |
| Figure 27. | Load transient (VOUT = 5 V) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 13 |
| Figure 28. | SOT223 package outline . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 14 |
| Figure 29. | Tape for SOT223 (dimensions are in mm) . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 16 |
| Figure 30. | Reel for SOT223 (dimensions are in mm). . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 17 |
| Figure 31. | SOT223 reel oriented . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . 17 |

![Image](LDL1117%20Datasheet%20%28ST%20DS12022%29_files/img_005.png)

## IMPORTANT NOTICE - PLEASE READ CAREFULLY

STMicroelectronics NV and its subsidiaries ("ST") reserve the right to make changes, corrections, enhancements, modifications, and improvements to ST products and/or to this document at any time without notice. Purchasers should obtain the latest relevant information on ST products before placing orders. ST products are sold pursuant to ST's terms and conditions of sale in place at the time of order acknowledgement.

Purchasers are solely responsible for the choice, selection, and use of ST products and ST assumes no liability for application assistance or the design of Purchasers' products.

No license, express or implied, to any intellectual property right is granted by ST herein.

Resale of ST products with provisions different from the information set forth herein shall void any warranty granted by ST for such product.

ST and the ST logo are trademarks of ST. For additional information about ST trademarks, please refer to www.st.com/trademarks. All other product or service names are the property of their respective owners.

Information in this document supersedes and replaces information previously supplied in any prior versions of this document.

© 2020 STMicroelectronics - All rights reserved
<!-- Converted from SPX3819 Datasheet (MaxLinear).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_001.png)

May 2014

## GENERAL DESCRIPTION

The SPX3819 is a positive voltage regulator with a low dropout voltage and low noise output. In addition, this device offers a very low ground current of 800µA at 100mA output. The SPX3819 has an initial tolerance of less than 1% max and a logic compatible ON/OFF switched input. When disabled, power consumption drops to nearly zero. Other key features include reverse battery protection, current limit, and thermal shutdown. The SPX3819 includes a reference bypass pin for optimal low noise output performance. With its very low output temperature coefficient, this device also makes a superior low power voltage reference.

The SPX3819 is an excellent choice for use in battery-powered applications such as cordless telephones, radio control systems, and portable computers. It is available in several fixed output voltage options or with an adjustable output voltage.

This device is offered in 8 pin NSOIC, 8 pin DFN and 5-pin SOT-23 packages.

## TYPICAL APPLICATION DIAGRAM

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_002.png)

Fig. 1: SPX3819 Application Circuit

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

Rev. 2.0.2

## APPLICATIONS

- Portable Consumer Equipment
- Portable Instrumentation
- Industrial Equipment
- SMPS Post Regulators

## FEATURES

- Low Noise: 40µV Possible
- High Accuracy: 1%
- Reverse Battery Protection
- Low Dropout: 340mV at Full Load
- Low Quiescent Current: 90µA
- Zero Off-Mode Current

- Fixed &amp; Adjustable Output Voltages:
- 1.2V, 1.5V, 1.8V, 2.5V, 3.0V, 3.3V &amp; 5.0V Fixed Output Voltages
- ≥1.235V Adjustable Output Voltages
- Available in RoHS Compliant, Lead Free Packages:
- 5-pin SOT-23, 8-pin SOIC and 8-pin DFN

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

## ABSOLUTE MAXIMUM RATINGS

These are stress ratings only and functional operation of the device at these ratings or any other above those indicated in the operation sections of the specifications below is not implied. Exposure to absolute maximum rating conditions for extended periods of time may affect reliability.

| VIN, EN ..................................................... | -20V to +20V |
| - | - |
| Storage Temperature | .............................. -65°C to 150°C |
| Junction Temperature | .......................................... 150°C |
| Power Dissipation ................................ | Internally Limited |
| Lead Temperature (Soldering, | 5 sec) ..................... 260°C |
| ESD Rating (HBM - Human Body | Model) .................... 2kV |

## ELECTRICAL SPECIFICATIONS

Specifications with standard type are for an Operating Junction Temperature of TJ = 25°C only; limits applying over the full Operating Junction Temperature range are denoted by a "·". Minimum and Maximum limits are guaranteed through test, design, or statistical correlation. Typical values represent the most likely parametric norm at TJ = 25°C, and are provided for reference purposes only. Unless otherwise indicated, VIN = VOUT + 1V (VIN = VOUT + 1.2V for 1.2V option), IL = 100µA, CL = 1µF, VEN ≥ 2.5V, TA= TJ = 25°C.

| Parameter | Min. | Typ. | Max. | Units |  | Conditions |
| - | - | - | - | - | - | - |
| Output Voltage Tolerance | -1 |  | +1 | % |  |  |
| Output Voltage Tolerance | -2 |  | +2 | % | · |  |
| Output Voltage Temperature Coefficient |  | 57 |  | ppm/°C |  |  |
| Line Regulation |  | 0.04 | 0.1 | %/V |  | VIN = VOUT +1 to 16V and VEN ≤ 6V |
| Line Regulation |  |  | 0.2 | %/V | · | VIN = VEN = VOUT +1 ≤ 8V |
| Line Regulation |  |  | 0.2 | %/V |  | VIN = VEN = VOUT +1 ≤16V TA = 25°C to 85°C |
| Load Regulation |  | 0.05 | 0.4 | % |  | IL = 0.1mA to 500mA |
| Dropout Voltage (VIN-VOUT) 2 |  | 10 | 60 | mV | · | = 100µA |
| Dropout Voltage (VIN-VOUT) 2 |  |  | 80 | mV |  | IL |
| Dropout Voltage (VIN-VOUT) 2 |  | 125 | 175 | mV |  | IL = 50mA |
| Dropout Voltage (VIN-VOUT) 2 |  |  | 250 | mV | · |  |
| Dropout Voltage (VIN-VOUT) 2 |  | 180 | 350 | mV |  | IL = 150mA |
| Dropout Voltage (VIN-VOUT) 2 |  |  | 450 | mV | · |  |
| Dropout Voltage (VIN-VOUT) 2 |  | 340 | 550 |  |  | IL = 500mA |
| Dropout Voltage (VIN-VOUT) 2 |  |  | 700 |  | · |  |
| Quiescent Current (IGND) |  | 0.05 | 3 | µA |  | VENABLE ≤ 0.4V |
| Quiescent Current (IGND) |  |  | 8 |  | · | VENABLE = 0.25V |
| Ground Pin Current (IGND) |  | 90 | 150 | µA |  | IL = 100µA |
| Ground Pin Current (IGND) |  |  | 190 | µA | · | IL = 100µA |
| Ground Pin Current (IGND) |  | 250 | 650 | µA |  | IL = 50mA |
| Ground Pin Current (IGND) |  |  | 900 | µA | · | IL = 50mA |
| Ground Pin Current (IGND) |  | 1.0 | 2.0 | mA |  | IL = 150mA |
| Ground Pin Current (IGND) |  |  | 2.5 | mA | · | IL = 150mA |
| Ground Pin Current (IGND) |  | 6.5 | 25.0 |  |  | IL = 500mA |
| Ground Pin Current (IGND) |  |  | 30.0 |  | · | IL = 500mA |
| Ripple Rejection (PSRR) |  | 70 |  | dB |  |  |

## OPERATING RATINGS

| Input Voltage Range VIN ................................ 2.5V to | 16V |
| - | - |
| Enable Pin EN ............................................... | 0.0V to VIN |
| Junction Temperature Range ................. | -40°C to +125°C |
| Thermal Resistance 1 | ..................................................... |
| θJA (SOT23-5) | ...............................................191°C/W |
| θJA (NSOIC-8) ............................................ | 128.4°C/W |
| θJA (DFN-8) | ................................................... 59°C/W |

Note 1: The maximum allowable power dissipation is a function of maximum operating junction temperature, TJ(max) the junction to ambient thermal resistance, and the ambient θJA, and the ambient temperature TA. The maximum allowable power dissipation at any ambient temperature is given: PD(max) = (TJ(max)-TA)/θJA, exceeding the maximum allowable power limit will result in excessive die temperature; thus, the regulator will go into thermal shutdown

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

Note 2: Not applicable to output voltage 2V or less.

| Parameter | Min. | Typ. | Max. | Units |  | Conditions |
| - | - | - | - | - | - | - |
| Current Limit (ILIMIT) |  | 800 |  | mA | · | VOUT=0V |
|  |  |  | 950 | mA | · | VOUT=0V |
| Output Noise (eNO) |  | 300 |  | µVRMS |  | IL = 10mA, CL = 1.0µF, CIN = 1µF, (10Hz - 100kHz) |
| Output Noise (eNO) |  | 40 |  | µVRMS |  | IL = 10mA, CL = 1.0µF, CBYP = 1µF, CIN = 1µF, (10Hz - 100kHz) |
| Input Voltage Level Logic Low (VIL) |  |  | 0.4 | V |  | OFF |
| Input Voltage Level Logic High (VIH) | 2 |  |  | V |  | ON |
| ENABLE Input Current |  | 0.01 | 2 | µA |  | VIL ≤ 0.4V |
| ENABLE Input Current |  | 3 | 20 | µA |  | VIH ≥ 2.0V |

## PIN ASSIGNMENT

Fig. 2: SPX3819 Pin Assignment

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_004.png)

## PIN DESCRIPTION

| Name | Pin # nSOIC | Pin # DFN | Pin # SOT-23 | Description |
| - | - | - | - | - |
| VIN | 2 | 3 | 1 | Supply Input |
| GND | 5, 6, 7, 8 | 7 | 2 | Ground |
| VOUT | 3 | 5 | 5 | Regulator Output |
| EN | 1 | 1 | 3 | Enable(input). CMOS compatible control input. Logic high - enable; logic low or open = shutdown |
| ADJ/BYP | 4 | 8 | 4 | Adjust(input). Feedback input. Connect to resistive voltage-divider network |
| NC | - | 2, 4, 6 | - | No Connect |

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

## ORDERING INFORMATION

| Part Number | Temperature Range | Marking | Package | Packing Quantity | Note 1 | Note 2 |
| - | - | - | - | - | - | - |
| SPX3819M5-L | -40°C≤TJ≤+125°C |  | SOT-23-5 | Bulk | Halogen free |  |
| SPX3819M5-L/TR | -40°C≤TJ≤+125°C | G1WW | SOT-23-5 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819M5-L-1-2 | -40°C≤TJ≤+125°C | A4WW | SOT-23-5 | Bulk | Halogen free |  |
| SPX3819M5-L-1-2/TR | -40°C≤TJ≤+125°C | A4WW | SOT-23-5 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819M5-L-1-5 | -40°C≤TJ≤+125°C | W3WW | SOT-23-5 | Bulk | Halogen free |  |
| SPX3819M5-L-1-5/TR | -40°C≤TJ≤+125°C | W3WW | SOT-23-5 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819M5-L-1-8 | -40°C≤TJ≤+125°C | G3WW | SOT-23-5 | Bulk | Halogen free |  |
| SPX3819M5-L-1-8/TR | -40°C≤TJ≤+125°C | G3WW | SOT-23-5 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819M5-L-2-5 | -40°C≤TJ≤+125°C | H3WW | SOT-23-5 | Bulk | Halogen |  |
| SPX3819M5-L-2-5/TR | -40°C≤TJ≤+125°C | H3WW | SOT-23-5 | 2.5K/Tape & Reel | Halogen |  |
| SPX3819M5-L-3-0 |  | J3WW |  | Bulk | free |  |
| SPX3819M5-L-3-0/TR | -40°C≤TJ≤+125°C | J3WW | SOT-23-5 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819M5-L-3-3 | -40°C≤TJ≤+125°C | L3WW | SOT-23-5 | Bulk | Halogen free |  |
| SPX3819M5-L-3-3/TR | -40°C≤TJ≤+125°C | L3WW | SOT-23-5 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819M5-L-5-0 |  | M3WW | DFN-8 | Bulk |  |  |
| SPX3819M5-L-5-0/TR | -40°C≤TJ≤+125°C | M3WW | DFN-8 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819R2-L | -40°C≤TJ≤+125°C | L0L YWW |  | Bulk | Halogen free |  |
| SPX3819R2-L/TR | -40°C≤TJ≤+125°C | XX |  | 3.0K/Tape & Reel | Halogen free |  |
| SPX3819R2-L-1-2 | -40°C≤TJ≤+125°C | M0L YWW | DFN-8 | Bulk | Halogen free |  |
| SPX3819R2-L-1-2/TR | -40°C≤TJ≤+125°C | XX | DFN-8 | 3.0K/Tape & Reel | Halogen free |  |
| SPX3819R2-L-1-8 | -40°C≤TJ≤+125°C | N0L | DFN-8 | Bulk | Halogen free |  |
| SPX3819R2-L-1-8/TR | -40°C≤TJ≤+125°C | YWW XX | DFN-8 | 3.0K/Tape & Reel | Halogen free |  |
| SPX3819S-L | -40°C≤TJ≤+125°C | SPX3819 YYWWL | NSOIC-8 | Bulk |  |  |
| SPX3819S-L/TR | -40°C≤TJ≤+125°C | XXX | NSOIC-8 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819S-L-1-2 | -40°C≤TJ≤+125°C | SPX3819 12YYWWL | NSOIC-8 | Bulk | Halogen free |  |
| SPX3819S-L-1-2/TR | -40°C≤TJ≤+125°C | XXX | NSOIC-8 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819S-L-1-5 | -40°C≤TJ≤+125°C | SPX3819 15YYWWL | NSOIC-8 | Bulk |  |  |
| SPX3819S-L-1-5/TR | -40°C≤TJ≤+125°C | XXX | NSOIC-8 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819S-L-1-8 | -40°C≤TJ≤+125°C | SPX3819 18YYWWL | NSOIC-8 | Bulk | Halogen free |  |
| SPX3819S-L-1-8/TR | -40°C≤TJ≤+125°C | XXX | NSOIC-8 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819S-L-2-5 | -40°C≤TJ≤+125°C | SPX3819 25YYWWL XXX | NSOIC-8 | Bulk |  |  |
| SPX3819S-L-2-5/TR | -40°C≤TJ≤+125°C | SPX3819 25YYWWL XXX | NSOIC-8 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819S-L-3-3 | -40°C≤TJ≤+125°C | SPX3819 33YYWWL | NSOIC-8 | Bulk | Halogen free |  |
|  | -40°C≤TJ≤+125°C | SPX3819 33YYWWL | NSOIC-8 | 2.5K/Tape & Reel | Halogen free |  |
| SPX3819S-L-5-0 |  | SPX3819 50YYWWL | NSOIC-8 |  |  |  |
| SPX3819S-L-3-3/TR |  | SPX3819 50YYWWL | NSOIC-8 |  |  |  |
| SPX3819S-L-5-0/TR | -40°C≤TJ≤+125°C | XXX |  | Bulk 2.5K/Tape & | Halogen free Reel |  |

"YY" = Year - "WW" = Work Week - "X" = Lot Number; when applicable.

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_005.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

## TYPICAL PERFORMANCE CHARACTERISTICS

Fig. 3: Ground Current vs Load Current

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_006.png)

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_007.png)

Fig. 4: Ground Current vs Input Voltage

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_008.png)

Fig. 5 Ground Current vs Load Current in Dropout

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_009.png)

Fig. 7 Dropout Voltage vs Load Current

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_010.png)

Fig. 6 Output Voltage vs Input Voltage

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_011.png)

Fig. 8 Output Voltage vs Load Current

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

Fig. 9 Ground Current vs Temperature with 100µA Load

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_012.png)

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_013.png)

Fig. 11 Ground Current vs Temperature with 500mA Load

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_014.png)

Fig. 10 Ground Current vs Temperature with 50mA Load

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_015.png)

Fig. 12 Ground Current vs Temperature in Dropout

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_016.png)

VIN (V)

Fig. 13 ENABLE Voltage, ON threshold, vs Input Voltage

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_017.png)

Fig. 14 Output Voltage vs Temperature

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_001.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

Fig. 15 Output Noise vs Bypass Capacitor Value IL = 10mA, 10Hz - 100kHz

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_018.png)

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_019.png)

Fig. 17 Load Transient Response for 3.3V Device

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_020.png)

## APPLICATION INFORMATION

The SPX3819 requires an output capacitor for device stability. Its value depends upon the application circuit. In general, linear regulator stability decreases with higher output currents. In applications where the SPX3819 is sourcing less current, a lower output capacitance may be sufficient. For example, a regulator outputting only 10mA, requires approximately half the capacitance as the same regulator sourcing 150mA.

Bench testing is the best method for determining the proper type and value of the capacitor since the high frequency characteristics of electrolytic capacitors vary widely, depending on type and manufacturer. A high quality 2.2µF aluminum electrolytic capacitor works in most application circuits, but the same stability often can be obtained with a 1µF tantalum electrolytic.

Fig. 16 Line Transient Response for 3.3V Device

With the SPX3819 adjustable version, the minimum value of output capacitance is a function of the output voltage. The value decreases with higher output voltages, since closed loop gain is increased.

## TYPICAL APPLICATIONS CIRCUITS

A 10nF capacitor on the BYP pin will significantly reduce output noise, but it may be left unconnected if the output noise is not a major concern. The SPX3819 start-up speed is inversely proportional to the size of the BYP capacitor. Applications requiring a slow rampup of the output voltage should use a larger CBYP. However, if a rapid turn-on is necessary, the BYP capacitor can be omitted.

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_005.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

The SPX3819's internal reference is available through the BYP pin.

Figure 18 represents a SPX3819 standard application circuit. The EN (enable) pin is pulled high (&gt;2.0V) to enable the regulator. To disable the regulator, EN &lt; 0.4V.

Fig. 18: Standard Application Circuit

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_021.png)

The SPX3819 in Figure 19 illustrates a typical adjustable output voltage configuration. Two resistors (R1 and R2) set the output voltage.

The output voltage is calculated using the formula:

<!-- formula-not-decoded -->

R2 must be &gt;10kΩ and for best results, R2 should be between 22kΩ and 47kΩ.

Fig. 19: Typical Adjustable Output Voltage Configuration

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_022.png)

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

## PACKAGE SPECIFICATION

## 8-PIN SOICN

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_023.png)

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

## 8-PIN 2X3 DFN

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_024.png)

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

## 5-PIN SOT-23

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_025.png)

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_003.png)

## SPX3819

## 500mA Low-Noise LDO Voltage Regulator

## REVISION HISTORY

| Revision | Date | Description |
| - | - | - |
| 2.0.0 | 08/23/12 | Reformat of Datasheet Addition of SPX3819R2-L and SPX3819R2-L/TR part numbers |
| 2.0.1 | 12/02/13 | Added Storage Temperature Range and Junction Temperature in ABS MAX Ratings. |
| 2.0.2 | 05/20/14 | Updated package drawings and corrected DFN-8 package marking information [ECN 1423-03 6/3/14] |

## FOR FURTHER ASSISTANCE

Email:

Exar Technical Documentation:

customersupport@exar.com

powertechsupport@exar.com

http://www.exar.com/TechDoc/default.aspx?

## EXAR CORPORATION

## HEADQUARTERS AND SALES OFFICES

48720 Kato Road

Fremont, CA 94538 - USA

Tel.: +1 (510) 668-7000

Fax: +1 (510) 668-7030

www.exar.com

A New Direction in Mixed-Signal

![Image](SPX3819%20Datasheet%20%28MaxLinear%29_files/img_026.png)

## NOTICE

EXAR Corporation reserves the right to make changes to the products contained in this publication in order to improve design, performance or reliability. EXAR Corporation assumes no responsibility for the use of any circuits described herein, conveys no license under any patent or other right, and makes no representation that the circuits are free of patent infringement. Charts and schedules contained herein are only for illustration purposes and may vary depending upon a user's specific application. While the information in this publication has been carefully checked; no responsibility, however, is assumed for inaccuracies.

EXAR Corporation does not recommend the use of any of its products in life support applications where the failure or malfunction of the product can reasonably be expected to cause failure of the life support system or to significantly affect its safety or effectiveness. Products are not authorized for use in such applications unless EXAR Corporation receives, in writing, assurances to its satisfaction that: (a) the risk of injury or damage has been minimized; (b) the user assumes all such risks; (c) potential liability of EXAR Corporation is adequately protected under the circumstances.

Reproduction, in part or whole, without the prior written consent of EXAR Corporation is prohibited.
<!-- Converted from BQ79616-Q1 Daisy Chain Communications (slvaep4).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

www.ti.com Table of Contents

## Application Note

## BQ79616-Q1 Daisy Chain Communications

Taylor Vogt

## ABSTRACT

This application note is designed to demystify the bq7961X daisy chain communications interface when stacking multiple devices for high-voltage applications. The goal is to provide a deeper understanding of the protocol details when evaluating the device. Additionally, this report provides recommended isolation components and typical application practices for system designs to take full advantage of designing with this interface.

## Table of Contents

| 1 Introduction.............................................................................................................................................................................1 |
| - |
| 2 Receiver Topology and Common Mode Voltages................................................................................................................4 |
| 3 Signal Integrity Requirements...............................................................................................................................................5 |
| 3.1 Receiver Timing Requirements..........................................................................................................................................5 |
| 3.2 Receiver Threshold Requirements.....................................................................................................................................5 |
| 4 Debug Fault Registers............................................................................................................................................................7 |
| 5 Isolation Types........................................................................................................................................................................8 |
| 5.1 Transformer Isolation......................................................................................................................................................... 8 |
| 5.2 Capacitor Only Isolation.....................................................................................................................................................8 |
| 5.3 Capacitor and Choke Isolation...........................................................................................................................................9 |
| 6 Mixed Isolation Circuits using bq79600-Q1....................................................................................................................... 10 7 Ring Architecture..................................................................................................................................................................12 |
| 8 Noise Immunity and Emissions...........................................................................................................................................14 |
| 9 Daisy Chain Cable Selection............................................................................................................................................... 14 10 References.......................................................................................................................................................................... 14 |

## Trademarks

All trademarks are the property of their respective owners.

## 1 Introduction

The daisy chain communication interface on the bq7961X family of devices is a proprietary protocol developed by Texas Instruments. It is designed using differential signaling to minimize Electro-Magnetic Susceptibility (EMS) and strengthen Bulk Current Injection (BCI) immunity. The differential communication transmits complement data on the COM*P and COM*N pins, respectively. This interface is bi-directional and half duplex, and, therefore, has a transmitter (TX) and receiver (RX) on the COMH (high -side) and COML (low-side) interfaces.

The device supports the use of transformers or capacitors to electrically isolate the signals between devices in the stack. There are configurations where the devices are physically located on the same board or located in entirely separate packs connected with twisted pair wiring. For applications that have multiple devices on the same PCB, a single capacitor is connected between the COMH/L pins of the devices. For extremely noisy environments and stringent EMI/EMC requirements, additional filtering may be necessary. For devices that are separated by cabling, additional isolation components are used.

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_001.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_002.png)

Figure 1-2. Communication Tones

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_003.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_004.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_005.png)

Figure 1-3. Daisy Chain Bit Level Definition

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_006.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_007.png)

## 2 Receiver Topology and Common Mode Voltages

The daisy chain is bi-directional and half duplex, and, therefore, has a transmitter (TX) and receiver (RX) on the COMH and COML interfaces. The TX and RX functions are controlled automatically by the hardware based on the device's base/stack detection. When a WAKE ping/tone is received, the communication direction is set by CONTROL1[DIR\_SEL] and the COMM\_CTRL[TOP\_STACK] configurations. See Start Communication in the bq79616-Q1 data sheet for details. Additionally, a user overwrite to take over the complete control of the COMH and COML is available under communication debug mode using the DEBUG\_CTRL\_UNLOCK, DEBUG\_COMM\_CTRL1, and DEBUG\_COMM\_CTRL2 registers. See the Debug Control and Status section for more details in the bq79616-Q1 data sheet. Additionally, for a more detailed explanation of the basic timings and function of the protocol and plots below, visit section 9.5.1.2. of the bq79616-Q1 data sheet.

The RX topology of the bq7961X devices is similar to RS485 but with added design mechanisms to attenuate common mode voltages of up to ±20V due to noisy conditions. This common mode voltage limit for the differential signals is best explained by the chart in Figure 2-1. In an ambient test scenario, the common mode voltage of both the COM*P and COM*N holds at 2.5 V when there are no communications occurring. This is necessary because the attenuation of a negative signal would otherwise not bring the voltage between the receivers local ground and 5 V CVDD rail (internal LDO dedicated for communications). If communications occur, then the device will drive the COM pins with the CVDD rail between 0V (low) and 5V (high) and return to 2.5V between data packets (idle time) and after the communications have completed.

In the event of a common mode voltage swing due to noisy conditions such as EV inverter noise or Bulk Current Injection (BCI) testing - the common mode voltage seen at the COM pins may oscillate up to ±20 V depending on the isolation components and current injected. The device is designed to withstand this type noise level up to ±20 V because of the internal attenuation that allows the 5 V transceivers to handle the response and therefore the differential signal would still remain intact. Above this ±20 V level, there is risk of clamping the internal ESD structure or causing damage to the COM pins. This limit should be taken into consideration when determining BCI limits and testing.

Figure 2-1. Common Mode Voltage Diagram

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_008.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_009.png)

[www.ti.com](https://www.ti.com/)

## 3 Signal Integrity Requirements

Proper receiver waveform timing and thresholds are critical factors for the internal digital to correctly interpret tones and data communications. Note that these factors can be affected by isolation component choices and cabling.

## 3.1 Receiver Timing Requirements

As shown in Figure 3-3, the high and low timing differs between a tone signal (1us pulse width at 500 kHz) or data communications (approximately 250 ns pulse width at 2 MHz) waveform. However, both tones and data communications share similar rise/fall times and must both be rectangular waveforms with a maximum decay below 1 V. Note that the timing for the thigh/tlow refers to the time that the signal must be above or below the proper threshold value for the integration to succeed. If the signal is noisy during this thigh/tlow time and droops below the threshold value for some time - then there is risk of the signal being detected. We expect that roughly 1us ± 8% for tones and 250ns ± 20ns for data communications is the allowed timing variation for these signals to still be properly detected.

## 3.2 Receiver Threshold Requirements

The thresholds at which the internal digital is able to properly detect a high vs. low transition are shown in Figure 3-1. A good quality waveform will have a differential voltage above 1.8 V (and below -1.8 V on the negative side). It typically resembles a square wave with rounded edges.

The image below shows a poor quality or drooping waveform that still meets the criteria for a valid communication. The first diagram is showing a starting voltage (VSTART) of 1.7 V with an ending voltage (VEND) of 1.2V. The second diagram shows a second scenario where the starting voltage (VSTART) is only 1.6 V with an ending voltage (VEND) of 1.3V. If the starting amplitude is not at least 1.6 V, then the bit will not be detected, regardless of ending amplitude. These types of drooping waveforms most often are seen when there are two adjacent bits of opposite polarity, forming what can be referred to as a double-bit.

## Note

The color red indicates the region that the signal may or may not be detected (poor quality waveform zone) whereas orange indicating the area the area near the triggering threshold range. A good quality waveform would remain in the green region above 1.7 V for the duration of the positive pulse width.

Figure 3-1. Differential Signal Eye Diagram - 1.7 V VSTART

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_010.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_011.png)

Figure 3-2. Differential Signal Eye Diagram - 1.6 V VSTART

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_012.png)

Table 3-1 shows the specific timing and voltage requirements for valid daisy-chain communication.

Table 3-1. Timing Chart

|  | Parameter | Conditions | Min | Typ | Max |
| - | - | - | - | - | - |
| thigh | positive pulse width | COMP-COMN from +1.2V of rising edge to -1.2V of next falling edge | 220 ns | 250 ns | 280 ns |
| tlow | negative pulse width | COMP-COMN from -1.2V of rising edge to +1.2V of next falling edge | 220 ns | 250 ns | 280 ns |
| trise | Rising slew rate | COMP-COMN from -1.2V to +1.2V of rising edge |  |  | 60 ns |
| tfall | Falling slew rate | COMP-COMN from +1.2V to -1.2V of falling edge |  |  | 60 ns |
| Vstart | Starting amplitude | If ending amplitude is above 1.3V | 1.6 V |  |  |
| Vstart | Starting amplitude | If ending amplitude is between 1.2V and 1.3V | 1.7 V |  |  |
| tblank | Blanking time | After last bit | 4 us |  |  |
| Wake Tone (thigh/tlow) | Wake Tone pulse widths | COMP-COMN from +1.2V of rising edge to -1.2V of next falling edge during and vice versa for Wake tones | 1 us |  |  |

Figure 3-3 shows the threshold needed for interfacing with the BQ79600 device. The primary difference is the threshold and timing references are based on a 1.8 V threshold.

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_013.png)

[www.ti.com](https://www.ti.com/)

Figure 3-3. Differential Signal Eye Diagram - BQ79600

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_014.png)

## 4 Debug Fault Registers

The bq7961X devices come equipped with many fault registers that help the user determine the cause and effect of signal noise between devices. Most importantly, we recommend always checking the FAULT\_SUMMARY register to determine if an error occurs during communication. If the FAULT\_SUMMARY flags a FAULT\_COMM error then the next steps would be to read back the 3 FAULT\_COMM1/2/3 registers and DEBUG registers to identify the exact issue. Refer to the bq79616-Q1 data sheet section 9.6.4.14 to learn more about these registers and indicators.

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_011.png)

## 5 Isolation Types

With the bq7961X family of devices, TI offers several options for designing an isolation interface between stacked devices in a complete system. These include:

1. Transformer/Galvanic/Inductive
2. Capacitive + Choke
3. Capacitive Only

Note that individual component properties and characteristics can affect signal integrity, robustness, and EMC performance. In the following sections, we go into detail of each isolation type and recommended component choices.

## 5.1 Transformer Isolation

For longer daisy chain cable lengths or highly noisy applications, the system may require the use of transformer isolation to provide the most robust form of communications. This design choice allows the daisy chain communications to be galvanically isolated and withstand higher sources of noise compared to capacitive coupled communications. The recommendation is to use a certain set of parameters to meet automotive qualified temperature, voltage, and reliability ratings. The recommendation is to choose parts that remain in the 150 - 600uH inductance range for best performance. Table 5-1 is a list of recommended part numbers that were tested using the bq7961X devices. Choosing a part outside of this list or parameters would require thorough validation on the system designer side to ensure that the communication is robust over temperature, can withstand rapid communication transactions, and provides proper EMI filtering. Note that it is important and highly recommended to use the same transformer part number on both sides of a daisy chain interface (COML of top device and COMH of connected lower device).

Figure 5-1. Transformer Isolation Across PCBs

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_015.png)

Table 5-1. Recommended Transformer Part Numbers

| Part Number | Supplier | Inductance (OCL) uH | Height (mm) |
| - | - | - | - |
| HMU1228NL | Pulse | 150-370 | 6.85 |
| HM2147NL | Pulse | 580-1285 | 3.45 |
| SM91502AL | Bourns | 150-450 | 5.72 |

## 5.2 Capacitor Only Isolation

For low noise environments or devices mounted on the same pcb, typically the best practice is to choose capacitors only for isolation. We recommend these capacitors to be 2.2nF, high voltage rated (twice the voltage of the system's total pack voltage), and automotive qualified. Our reference schematic uses the 1206J2K00222KXR supplied by Knowles. Use of a capacitor of up to 5.6nF for this isolation is possible.

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_013.png)

www.ti.com Components Required for Cap Coupled Daisy Chain on different pcb Components Required for Cap Coupled Daisy Chain on the same PCB

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_016.png)

Figure 5-2. Capacitors Only Across PCBs

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_017.png)

Figure 5-3. Capacitor Only on Same PCB

## 5.3 Capacitor and Choke Isolation

If the system uses capacitive based isolation, then it can be required for longer daisy chain cable lengths or highly noisy applications to use an additional common-mode choke filter in series with the capacitors. For these applications, it is recommended use an automotive grade 100 μH common-mode filter minimum for proper operation. To achieve the best performance in noisy environments, use dual common-mode filters (100 μH and 470 μH). For single common-mode filter applications, the TDK 51 μH 2.8kΩ choke (ACT45B-510-2P-TL003) is recommended. For dual common-mode filter applications, the TDK 100 μH 5.8 kΩ choke (ACT45B-101-2PTL003) and Wurth 470 μH 2.2 kΩ (744242471) are recommended. Note that the common mode impedance specification is most critical to suppressing the higher noise sources. The same principle can be applied when determining choice of a ferrite bead.

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_018.png)

Components Required for cap-choke Daisy Chain with Cabling

Figure 5-4. Capacitor and Choke Across PCBs

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_002.png)

## 6 Mixed Isolation Circuits using bq79600-Q1

When using the bq79600-Q1 device as the communication bridge in combination with any variant of the bq79616-Q1 device as the stack device, it is important to validate the robustness of the isolation interface between the base and first stack device. This process is because the devices are designed to support a mixed isolation type on the COMH side of the base vs. the COML of the stack device. Typically this means that the bq79600-Q1 will have a transformer from the previous list, and then the user may select any of the three supported isolation types for the bq79616-Q1 stack device side (that is the same transformer part number on both sides if transformer isolation is desired). Every scenario with different transformer, cap, and choke part numbers mixed has not been tested so it is important for the user to ensure that the signal integrity is maintained after choosing their isolation components. Schematically, the key difference is that the decoupling capacitors on the bq79600-Q1 circuit are 100pF compared to 220pF for the bq79616-Q1 device.

- ξ BQ79600 is used as communication bridge, shown as B0

Figure 6-1. Example: BQ79600-Q1 Connected to BQ79616-Q1 Timing

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_019.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_020.png)

Figure 6-2. How a Stack Command is Sent

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_021.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_004.png)

[www.ti.com](https://www.ti.com/)

This is the tRECLK\_DC spec in DS:

3us typ, 5 µs max (will be using 3 µs for all

calculations in this ppt)

This is the tRECLK\_DC spec in DS: 3us typ, 5us max The timing analysis can be different depends on the definition of start and stop of time count For simplicity, the command frame timing analysis use the following

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_022.png)

- definition:ξ t\_start = MCU finishes sending the command
- ξ t\_stop = top device receives the full command

Figure 6-3. When Does Each Device Receive the Command?

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_023.png)

Figure 6-4. Sequence of Device Receiving or Sending Commands

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_011.png)

## 7 Ring Architecture

The bq7961X daisy chain interface offers the option to use ring architecture. In this architecture, a cable break between two devices does not prevent communication to all upstream devices as in a normal non-ring scheme. When the host detects a broken communication, the device allows the host to switch the communication direction to communicate with devices on both sides of the break. This allows for safe operation until the break in the lines is repaired. The CONTROL1[DIR\_SEL] controls the communication direction. The devices will reconfigure the COMH and COML ports depending on the [DIR\_SEL] and the [TOP\_STACK] settings. Auto-addressing procedure is needed to re-address the device address for the reverse communication direction. Example to change the communication direction to [DIR\_SEL] = 1 to the entire daisy chain:

1. Host sends Single Device Write to change the base device [DIR\_SEL] = 1. The base device will disable its COMH and enable its COML.
2. Host sends Broadcast Write Reverse Direction to clear the COMM\_CTRL register settings on all devices.
3. Host sends Broadcast Write Reverse Direction to change the rest of the devices' [DIR\_SEL] = 1. In this step, the entire daisy chain set up to transmitting communication in the [DIR\_SEL] = 1 direction (that is, each device set up to transmit command frames sent by host from its COMH to its COML).
4. Host performs auto-addressing procedure to set up device address in the DIR1\_ADDR register. Unless the devices have been reset, host can skip the dummy read/write steps to synchronize the DLL in the autoaddressing procedure.
5. Host sets up the new Top of Stack device and the new ToS device will disable its COML transmitter.

Once the device address in both communication directions is set up, the host can skip auto-address step when switching communication direction.

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_024.png)

Figure 7-1. Example to Change Communication Direction in Daisy Chain

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_025.png)

In a broken cable case, the host follows the same procedure to change the communication direction. To access all devices in the daisy chain, the host will have to communicate with [DIR\_SEL] = 0 on some devices and communicate with [DIR\_SEL] = 1 on other devices in the daisy chain. The chain will also have two ToS devices, one for each communication direction.

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_004.png)

[www.ti.com](https://www.ti.com/)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_026.png)

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_027.png)

(a) Use [DIR\_SEL] = 0 direction to communicate to S1

(a) Use [DIR\_SEL] = 1 direction to communicate to S3 and S2

Figure 7-2. Using Ring Architecture to Access All Devices in a Broken Cable Case

![Image](BQ79616-Q1%20Daisy%20Chain%20Communications%20%28slvaep4%29_files/img_028.png)

## 8 Noise Immunity and Emissions

To determine that the bq7961X daisy chain architecture can be considered in automotive or EV applications, we perform several EMI or EMC tests to showcase the robustness. However, these results will vary based on schematic or pcb layout design choices, external noise sources, distance from UART or MCU connections, and calibration equipment. Reach out to TI sales team or support team representative to receive more details on these specifications passed. Below is a list of common practices in order to replicate best case results.:

1. Layout Recommendations in the BQ7961x-Q1 Design Recommendations for High Voltage Automotive BMS application note.
2. Closely follow our reference EVM Schematic and Layout detailed in the BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules.
3. Common practices include isolating UART or MCU connections with ferrite, beads, filtering components.

## 9 Daisy Chain Cable Selection

Typically daisy chain testing is done with minimally short, symmetrical, matching impedance on-board pcb traces between devices or a 1 - 1.7m long twisted pair cabling between two separate pcbs or evaluation modules. However, depending on proper layout, isolation, and delay between commands - the communication protocol can support cabling up to 20-40m if needed but this would not be recommended for most robust solutions. The cabling material, twisting, and connectors can play a role in communication robustness but we do not provide strict requirements for these factors due to the flexibility provided to many different system architectures. However, testing has been completed with basic copper twisted pair wiring (no shielding) for many of our temperature and EMC testing. Although it may be best to use PP material rather than PVC material which changes the dielectric constant of the cable over time and temperature and thus has an impact on the transferred signals as opposed to more expensive, but better PP material. Typically for best practices is to support at least 1-2 twists per cable inch and start the twisting very close to the connectors. This will help reduce external effects of EMI interference.

## 10 References

- [Texas Instruments, BQ7961x-Q1 Family of 12S, 14S, 16S Precision Automotive Battery Monitor, Balancer and Integrated Hardware Protector with up to SafeTITM-26262 ASIL-D Compliance, data sheet.](https://www.ti.com/lit/pdf/SLUSB75)
- [Texas Instruments, BQ79600-Q1 Automotive SPI/UART Communication Interface Functional-Safety Compliant With Automatic Host Wakeup, data sheet.](https://www.ti.com/lit/pdf/SLUSDS1)
- [Texas Instruments, BQ79616-Q1, BQ75614-Q1, and BQ79656-Q1 Evaluation Modules, EVM user's guide.](https://www.ti.com/lit/pdf/SLUUC37)
- Texas Instruments, BQ7961x-Q1 Design Recommendations for High Voltage Automotive BMS, application note.

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2023, Texas Instruments Incorporated
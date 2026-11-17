<!-- Converted from BQ79600-Q1 Design Recommendations (sluaa16a).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

www.ti.com Table of Contents

## Application Note

## BQ79600-Q1 Design Recommendations

## ABSTRACT

BQ79600-Q1 is a communication bridge device used to interface between the host microcontroller and the battery monitor devices from the BQ7961X family. The device is capable of communicating through UART or through SPI interface to the host and translates the communication to a differential daisy chain protocol understood by BQ7961X family of devices.

The bidirectional daisy chain ports support transformer-based isolation. In ring architecture, this device supports automatic host wakeup or reverse wakeup which allows the host microcontroller and PMIC to be in low power mode (SHUTDOWN/SLEEP) while the BQ79600-Q1 monitors for faults coming from the stacked battery monitor devices and wakes up the microcontroller and PMIC if any unmasked fault is detected.

## Table of Contents

| 1 Circuit Design..........................................................................................................................................................................2 |  |
| - | - |
| 1.1 Power Supply (BAT, CVDD, DVDD, VIO pins)................................................................................................................... | 2 |
| 1.2 Inhibit Output (INH pin)...................................................................................................................................................... | 4 |
| 1.3 Communication to Host (MOSI/RX, MISO/TX, nCS, SCLK, nUART/SPI (SPI_RDY) pins)............................................... | 4 |
| 1.4 Fault Output (NFAULT pin).................................................................................................................................................6 |  |
| 1.5 Communication to Battery Monitor Device (COMHP, COMHN, COMLP, COMLN pins)....................................................6 |  |
| 2 Layout Guidelines...................................................................................................................................................................8 |  |
| 2.1 Ground Planes................................................................................................................................................................... | 8 |
| 2.2 Bypass Capacitors for Power Supplies and References....................................................................................................8 |  |
| 2.3 UART/SPI Communication.................................................................................................................................................8 |  |
| 2.4 Daisy Chain Communication..............................................................................................................................................8 |  |
| 3 Daisy Chain Signal Integrity................................................................................................................................................ | 10 |
| 3.1 Daisy Chain Receiver Threshold......................................................................................................................................10 |  |
| 3.2 Common and Differential Mode Noise............................................................................................................................. | 10 |
| 3.3 BCI Performance..............................................................................................................................................................11 |  |
| 3.4 Radiated Emissions Performance.................................................................................................................................... | 11 |
| 4 Summary............................................................................................................................................................................... | 12 |
| 5 References............................................................................................................................................................................ | 12 |
| 6 Revision History................................................................................................................................................................... | 12 |
| List of Figures | List of Figures |
| Figure 1-1. 12 V Battery and Automatic Host Wakeup................................................................................................................ | 3 |
| Figure 1-2. 5 V Regulated Supply and No Automatic Host Wakeup............................................................................................3 |  |
| Figure 1-3. UART Interface Used................................................................................................................................................ | 5 |
| Figure 1-4. SPI Interface Used.................................................................................................................................................... | 5 |
| Figure 1-5. Daisy Chain Isolation.................................................................................................................................................6 |  |
| Figure 2-1. Daisy Chain Layout Considerations.......................................................................................................................... | 9 |
| Figure 3-1. Daisy-chain Receiver Threshold............................................................................................................................. | 10 |
| Figure 3-2. X-Y Caps................................................................................................................................................................. | 11 |
| List of Tables | List of Tables |
| Table 1-1. Power Supply Design Considerations.........................................................................................................................4 |  |
| Table 1-2. INH Design Considerations.........................................................................................................................................4 |  |
| Table 1-3. SPI/UART Design Considerations.............................................................................................................................. | 6 |
| Trademarks | Trademarks |
| All trademarks are the property of their respective owners. |  |

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_001.png)

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_002.png)

## 1 Circuit Design

This section explains the circuit design recommendations for the BQ79600-Q1 device to function properly.

## 1.1 Power Supply (BAT, CVDD, DVDD, VIO pins)

BAT, CVDD, DVDD and VIO pins are supplies in BQ79600-Q1 used to provide power to different blocks in the chip.

BAT pin is the battery supply input which supplies the internal LDOs and wakeup circuit. When reverse wakeup feature is used, this pin should be connected to a 12 V battery through a 10 Ω resistor and bypassed to GND with a 0.1 µF/50 V capacitor, placing capacitor as close as possible to the pin. Battery voltage can be as low as 5.5 V and as high as 24 V. If reverse wakeup feature is not used, this pin can be connected to a regulated 5 V supply from the SBC/PMIC in the system with as low as 4.75 V and as high as 5.25 V.

CVDD pin is a dedicated 5 V supply for the vertical interface. This voltage is generated internally by the BQ79600-Q1 device. This pin needs to be decoupled with a 0.22 µF/10 V capacitor to GND for correct operation. Place capacitor as close as possible to CVDD pin and don't connect any external load to this pin. If reverse wakeup feature is not used and BAT pin is powered from a regulated 5V supply, connect CVDD directly to BAT pin and still connect the 0.22 µF/10 V decoupling capacitor.

DVDD pin is a 1.8 V regulated output to supply the internal digital circuits and it is generated internally by the BQ79600-Q1 device from the CVDD 5 V supply. It needs to be decoupled with a 0.22 µF/10 V capacitor to GND for correct operation. Place capacitor as close as possible to DVDD pin and don't connect any external load to this pin.

VIO pin is the power supply input for the UART and SPI I/O pins. This pin should be connected to an external regulated supply, typically 3.3 V or 5 V. The microcontroller voltage reference for UART or SPI I/O pins should be the same as the voltage reference used for VIO. In a typical application, this regulated voltage is generated by a PMIC in the system and is connected to both the BQ79600-Q1 VIO pin and the power supply pin for UART or SPI I/Os in the microcontroller. Decouple with a 0.1 µF/10 V capacitor to GND and place capacitor as close as possible to VIO pin. VIO should be powered before SCLK, nCS, RX/MOSI, TX/MISO, NFAULT, nUART/SPI (SPI\_RDY) are driven.

Figure 1-1 shows the recommended power supply circuit design when a 12 V battery is directly used to power the BQ79600-Q1 and reverse wakeup feature is used. Figure 1-2 shows the recommended power supply circuit design when a regulated 5 V supply is used to power the BQ79600-Q1 and reverse wakeup feature is not used.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_003.png)

Figure 1-1. 12 V Battery and Automatic Host Wakeup

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_004.png)

Figure 1-2. 5 V Regulated Supply and No Automatic Host Wakeup

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_005.png)

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_006.png)

Table 1-1. Power Supply Design Considerations

| Pin | Purpose | Reverse Wakeup Used | Reverse Wakeup Not Used |
| - | - | - | - |
| BAT | Supplies internal LDOs and wakeup circuit. | Connect to external 12 V battery through 10 Ω resistor and bypass to GND with 0.1 µF/50 V. | Connect to external 12 V battery through 10 Ω resistor and bypass to GND with 0.1 µF/50 V, or connect to regulated 5 V supply and short to CVDD. |
| CVDD | 5 V supply for daisy chain communications. | Decouple with 0.22 µF/10 V to GND. | Decouple with 0.22 µF/10 V to GND. If BAT powered with 5 V supply, connect this pin to BAT pin. |
| DVDD | 1.8 V supply for internal digital circuits. | Bypass with 0.22 µF/10 V capacitor to GND. | Bypass with 0.22 µF/10 V capacitor to GND. |
| VIO | 3.3 V or 5 V supply input for UART/SPI input/output pins. | Decouple with a 0.1 µF/10 V capacitor to GND. | Decouple with a 0.1 µF/10 V capacitor to GND. |

## 1.2 Inhibit Output (INH pin)

INH pin is a PMOS open drain output used to control the external voltage regulators such as a PMIC when reverse wakeup feature is used. This pin needs a 100 KΩ pull-down resistor to GND for correct functionality. If reverse wakeup feature is not used, connect INH directly to BAT pin.

Table 1-2. INH Design Considerations

| Pin | Purpose | Reverse Wakeup Used | Reverse Wakeup Not Used |
| - | - | - | - |
| INH | PMOS open drain output to control system voltage regulators. | Connect a 100 KΩ resistor to GND. | Connect this pin to BAT pin. Don't leave floating. |

## 1.3 Communication to Host (MOSI/RX, MISO/TX, nCS, SCLK, nUART/SPI (SPI\_RDY) pins)

The BQ79600-Q1 supports communication to the host microcontroller through either UART interface or SPI interface using MOSI/RX, MISO/TX, nCS, SCLK and nUART/SPI (SPI\_RDY) pins. The circuit configuration required to use each of these communication interfaces is described in this section.

## Note

MISO/TX pin is pulled high by the BQ79600-Q1 device when idle (nCS = HIGH). Therefore, the SPI interface cannot be shared with other slave devices. Use another SPI interface in the MCU for other slave devices.

## nUART/SPI (SPI\_RDY) pin is a digital I/O pin with 2 functions:

1. This pin is used to select SPI or UART interface. To use the UART interface, connect this pin to GND. To use the SPI interface, connect this pin to VIO through a 10-100 KΩ pull-up resistor and connect this pin to a GPIO pin from the microcontroller.
2. When SPI mode is selected, this pin has an additional function. After device initialization in SPI mode, this pin is an output signal from the BQ79600-Q1 that indicates to the host when data is ready to be read or written.

nCS pin is a digital input used as the active low chip select pin for SPI interface. In SPI mode, connect this pin to VIO with 10-100 KΩ pull-up resistor and to the nCS pin from the SPI master microcontroller. The BQ79600-Q1 device uses specific signal patterns received on MOSI/RX pin called "pings" that are used to change the power state of the device. In SPI mode, the pings are only valid if nCS is held low. To avoid unintended pings to be read by the device, nCS signal cannot be hardwired to GND when SPI interface is used. In UART mode, connect this pin to GND.

SCLK pin is the clock input for SPI interface. If SPI mode is selected, connect this pin to GND with a 10-100 KΩ pull-down resistor and connect to the SPI SCLK pin on the MCU. In UART mode, connect directly to GND.

MISO/TX pin is the SPI master input slave output or the UART transmitter output. Connect this pin to VIO with a 10-100 KΩ pull-up resistor at MCU side. If SPI interface is used, connect this pin to the SPI MISO pin on the MCU. If UART interface is used, connect to the UART RX pin on the MCU.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

MOSI/RX pin is the SPI master output slave input or the UART receiver input. Connect this pin to VIO with a 10-100 KΩ pull-up resistor. Don't leave it unconnected. If SPI interface is used, connect this pin to the SPI MOSI pin on the MCU. If UART interface is used, connect to the UART TX pin on the MCU.

Figure 1-3 shows the recommended design when the host MCU uses UART interface to communicate to BQ79600-Q1 device. For recommended design when SPI interface is used for communication between the host MCU and BQ79600-Q1 see Figure 1-4.

Figure 1-3. UART Interface Used

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_007.png)

Figure 1-4. SPI Interface Used

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_008.png)

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_002.png)

## Table 1-3. SPI/UART Design Considerations

| Pin | SPI Mode | UART Mode |
| - | - | - |
| MOSI/RX | Connect to VIO with a 10-100 KΩ pull-up resistor and to the MCU's SPI SIMO pin. | Connect to VIO with a 10-100 KΩ pull-up resistor and to the MCU's UART TX pin. |
| MISO/TX | Pull-up to VIO with a 10-100 KΩ resistor on the MCU side. Connect to the MCU's SPI SOMI pin. Do not connect other slave devices on the SPI bus since MISO line is pulled high by the BQ79600-Q1 device when idle. | Pull-up to VIO with a 10-100 KΩ resistor on the MCU side. Connect to the MCU's UART RX pin. |
| SCLK | Connect to GND with a 10-100 KΩ pull-down resistor and to the MCU's SPI SCLK pin. | Connect to GND. |
| nCS | Connect to VIO with 10-100 KΩ pull-up resistor and to the MCU's SPI nCS pin. | Connect to GND. |
| nUART/SPI (SPI _RDY) | Connect to VIO with 10-100 KΩ pull-up resistor and to a GPIO pin on the MCU. | Connect to GND. |

## 1.4 Fault Output (NFAULT pin)

NFAULT pin is an active low fault indicator that, in the event of a fault, will pull low to signal to the host that a fault has occurred. nFAULT is an open drain active low pin, and therefore it needs to be pulled up to VIO with a 100 KΩ resistor. Connect nFAULT to a GPIO on the host MCU. If not used, connect to GND. See Figure 1-3 with recommended NFAULT connection.

## 1.5 Communication to Battery Monitor Device (COMHP, COMHN, COMLP, COMLN pins)

COMHP, COMHN, COMLP and COMLN pins are AC coupled bi-directional input/output pins used for communication with TI's battery monitor ICs such as the BQ7961X-Q1 family of devices. To communicate in the North direction, COMHP/N differential pins of BQ79600-Q1 should be connected to the COMLP/N pins of the first battery monitor IC in the stack through proper isolation. Likewise, to communicate in the South direction, such as when ring architecture is used, COMLP/N differential pins of BQ79600-Q1 should be connected to the COMHP/N pins of the top of stack battery monitor IC through proper isolation. Leave these pins unconnected if not used.

To isolate between the low voltage system and the high voltage domain, transformer isolation is recommended as it is the most effective method for removing common mode noise from the system. Figure 1-5 shows the interface components values. The circuit shown in red is only needed if ring architecture is used.

Figure 1-5. Daisy Chain Isolation

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_009.png)

The benefit of using the ring architecture is that the host can continue communicating with the battery monitor stacked devices even when there is a break on the communication line between two stacked devices. In a non-ring scheme, a break between 2 devices would prevent communication to all upstream devices. When a ring architecture is used with BQ79600-Q1 bridge device and BQ7961X-Q1 stacked devices, if the host detects www.ti.com a broken communication interface it would be able to switch the communication direction to communicate with devices on both sides of the break. This allows for safe operation until the break in the lines is repaired. Steps on how to reverse the communication direction when ring architecture is used can be found in the device's data sheet.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_010.png)

Ring architecture also enables fault status transmitting when the BQ7961X-Q1 stacked devices are in SLEEP mode and BQ79600-Q1 is either in SLEEP mode or SHUTDOWN mode.

| Component | Purpose | Recommendation |
| - | - | - |
| Transformer | Transformer provides galvanic isolation between the Low Voltage and High Voltage domains. | HMU1228NL Transformer or HM2147NL Transformer. |
| Termination resistor | The purpose of this resistor is to prevent reflected signals from interfering in the communication. | 1 KΩ resistor between COMHP and COMHN pins. If ring architecture used, 1 KΩ resistor between COMLP and COMLN pins. There should be a termination resistor at each end of the connection on the BQ79600-Q1 side and on the BQ7961X-Q1 side. |
| Series resistor | Series termination resistance for impedance matching. | 51 Ω series resistor on both COMHN and COMNP lines as shown in Figure 1-5. If ring architecture used, also need 51 Ω series resistor on both COMLN and COMLP lines. |
| Bypass capacitors | Bypass capacitors to provide filtering as well as improving performance during BCI testing. | 100 pF/50 V capacitor to GND on both COMHN and COMHP. If ring architecture used, 100 pF/50 V capacitor to GND on both COMLN and COMLP. |
| ESD protection | It is recommended that ESD protection is added to provide ESD isolation on the communication lines. | PESD5V0L2BT ESD device. |
| Capacitor on transformer center terminal | Transformer needs to be center tapped with a 100 pF capacitor. | 100 pF/50 V capacitor. |

In all of these situations, the recommendation is based on how long the cable between boards is, and in all cases, twisted pair cabling is used between modules. The main purpose of these noise isolation methods is to remove common mode noise from the signal.

Any capacitance present on the communication line will have an effect on the performance. All intentional and parasitic capacitance should be calculated and taken into account.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_006.png)

## 2 Layout Guidelines

The layout for this device must be designed carefully. Any design outside these guidelines can affect the communication robustness and EMI performance. Care must be taken in the layout of signals to and from the device to avoid coupling noise onto sensitive inputs. The layout of ground and power connections, as well as communication signals, must also be made carefully.

## 2.1 Ground Planes

It is very important to establish a clean grounding scheme to ensure best performance of the device. There is one ground pin (GND) on the device. It is a good practice to use top and bottom PCB layers for signal routing, and use middle layers as ground planes. Even on a PCB layer that is mainly for signal routing, it is good practice to have a small island of ground pour if possible to provide a low-impedance ground, rather than simply a via through the ground trace to an lower ground plane. Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB layers.

There is a strong recommendation to have a minimum of four layers in the PCB, with one layer fully dedicated to an unbroken VSS plane (except thermal reliefs). Avoid placing tracks on this layer to maintain the unbroken integrity of the plane structure.

## 2.2 Bypass Capacitors for Power Supplies and References

The bypass capacitors of the following pins must be placed as close to the device pins as possible to ensure proper performance.

- BAT, VIO, CVDD, DVDD

## 2.3 UART/SPI Communication

To signal integrity on the communication to the host MCU, keep the traces on these pins as short and straight as possible.

- MISO/TX, MOSI/RX, SCLK, nCS, nUART/SPI (SPI\_RDY)

## 2.4 Daisy Chain Communication

It is important to have proper layout on the COMHP/N and COMLP/N circuits to have the best robust daisy chain communication.

Maintaining signal integrity on the daisy chain communication lines is critical to the success of this part.

1. Keep differential traces as short as possible and as straight as possible. Minimize turns and avoid any looping on the traces.
2. Keep the differential traces on the same layers. Run the trace in parallel with shielding and matching trace impedance.
3. Place the isolation components close to the connectors.
4. When using capacitive isolation, place the high voltage capacitor of the COMxP/N pair (where x = H, L) close to each other along the parallel traces.
5. Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB layers.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_003.png)

Figure 2-1. Daisy Chain Layout Considerations

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_011.png)

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_012.png)

## 3 Daisy Chain Signal Integrity

## 3.1 Daisy Chain Receiver Threshold

The thresholds at which the internal digital is able to properly detect a high vs. low transition are shown in the figure below. The key threshold voltage is 1.75 V for a high to be detected and -1.75 V for a low. However, at range between +/-1.13 V to +/-1.75 V there is a possibility that the digital will interpret this as a high/low signal but it is not certain until the 1.75 V threshold is reached.

For tones, the digital is purely looking at edge detection transition, so as long as there is a +1.75 V threshold polarity change to -1.75 V then the couplet will be detected properly. Therefore, the blank time where the signal may rise above 1.13 V after the tone couplet will be ignored.

For data communications, the threshold must remain above 1.75 V during the full 250 ns high and 250 ns low side to properly interpret the command.

Figure 3-1. Daisy-chain Receiver Threshold

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_013.png)

## 3.2 Common and Differential Mode Noise

X-Y caps are commonly used and may be required for extremely noisy environments.

- Differential mode noise goes out one wire and returns back on another wire. An X capacitor is placed between two lines to suppress the noise.
- Common mode noise goes out from both wires and returns back to the chassis through stray capacitance to ground. A Y capacitor is placed between the chassis as Figure 3-2 illustrates.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

## Battery Pack

Figure 3-2. X-Y Caps

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_014.png)

## Design Considerations

- Device placement is important. The daisy-chain cable should not be resting on the busbar or metal enclosure surface.

## 3.3 BCI Performance

Bulk Current Injection (BCI) was performed according to the ISO 11452-4 standard, using longer cable length (3 m) and a baud rate of 1 Mbps. The BCI noise was injected on the communication lines. There were 3 different isolation methods tested:

- Transformer isolation on BQ79600-Q1 to transformer isolation on BQ79616-Q1
- Transformer isolation on BQ79600-Q1 to capacitive isolation on BQ79616-Q1
- Transformer isolation on BQ79600-Q1 to capacitive and choke isolation on BQ79616-Q1

Contact your local TI sales representative for further information on BCI performance.

## 3.4 Radiated Emissions Performance

Radiated emissions test was performed according to CISPR 25 standard. The cable length was 1.7 m. There were 3 different isolation methods tested:

- Transformer isolation on BQ79600-Q1 to transformer isolation on BQ79616-Q1
- Transformer isolation on BQ79600-Q1 to capacitive isolation on BQ79616-Q1
- Transformer isolation on BQ79600-Q1 to capacitive and choke isolation on BQ79616-Q1

Contact your local TI sales representative for further information on radiated emissions performance.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_012.png)

## 4 Summary

The BQ79600-Q1 device can be configured to enable communication through UART or SPI between the microcontroller unit (MCU) and the battery monitor devices. This communication is performed through a robust daisy chain protocol that is compatible with our BQ7961X family devices using the COMHP, COMHN, COMLP, and COMLH AC coupled bi-directional I/O pins that utilize transformer isolation as the most effective method to remove noise. Additionally, our devices support ring architecture which enables a continuous and reliable communication between devices in the event of a break on the communication line by reversing the communication direction.

## 5 References

1. Texas Instruments, BQ79600-Q1 Automotive SPI/UART Communication Interface Functional-Safety Compliant with Automatic Host Wakeup, data sheet.
2. Texas Instruments, BQ79600-Q1 Software Design Reference, application note.
3. Texas Instruments, BQ7961x-Q1 Design Recommendations for High Voltage Automotive BMS, application note.

![Image](BQ79600-Q1%20Design%20Recommendations%20%28sluaa16a%29_files/img_015.png)

[www.ti.com](https://www.ti.com/)

## 6 Revision History

| Changes from Revision * (August 2020) to Revision A (October 2023) | Page |
| - | - |
| · Updated the numbering format for tables, figures, and cross-references throughout the document ................ | 1 |
| · Added Summary section.................................................................................................................................. | 12 |
| · Added References section............................................................................................................................... | 12 |

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2023, Texas Instruments Incorporated
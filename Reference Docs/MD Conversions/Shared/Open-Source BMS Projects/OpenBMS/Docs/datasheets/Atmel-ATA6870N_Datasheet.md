<!-- Converted from Atmel-ATA6870N_Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](Atmel-ATA6870N_Datasheet_files/img_001.png)

Atmel

## ATA6870N

## Li-Ion, NiMH Battery Measuring, Charge Balancing and Power-supply Circuit

## Features

## DATASHEET

- 12-bit battery-cell voltage measurement
- Simultaneous battery cells measurement in parallel
- Cell temperature measurement
- Charge Balancing Capability
- Parallel balancing of cells possible
- Integrated power supply for MCU
- Undervoltage detection
- Less than 10µA standby current
- Low cell imbalance current (&lt; 10µA)
- Hot plug-in capable
- Interrupt timer for cycling MCU wake-ups
- Cost-efficient solution due to cost-optimized 30V CMOS technology
- Reliable communication between stacked ICs due to level shifters with current sources and checksum monitoring of data
- Daisy-chainable
- Each IC monitors up to 6 battery cells
- 16 ICs (96 cells) per string
- No limit on number of strings
- Package QFN48 7mm ×7mm

## Applications

- Battery measurement, supply and monitoring IC for Li-ion and NiMH battery systems in Electric (EV) and Hybrid Electrical (HEV) Vehicles
- Electrical and hybrid electrical vehicles
- Li-Ion batteries as 12V lead-acid battery replacement
- Ebike, scooters
- Uninterruptible power supply (UPS)
- Smart grid

## Benefits

- Cost reduction due to integrated measurement circuit and high voltage power-supply

## 1. Description

The Atmel ® ATA6870N is a measurement and monitoring circuit designed for Li-ion and NiMH multicell battery stacks in hybrid electrical vehicles.

The Atmel ATA6870N monitors the battery-cell voltage and the battery-cell temperature with a 12-bit ADC.

The circuit also provides charge-balancing capability for each battery-cell.

In addition, a linear regulator is integrated to supply a microcontroller or other external components. Reliable communication between stacked ICs is achieved by level-shifters with current sources. The Atmel ATA6870N can be connected to three, four, five or six battery-cells. Up to 16 circuits (96 cells) can be cascaded in one string. The number of strings is not limited.

## 2. Block Diagram

Figure 2-1. Block Diagram

![Image](Atmel-ATA6870N_Datasheet_files/img_002.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Atmel

below

## 3. Pin Configuration

Figure 3-1. Pinning QFN48, 7 mm ×7 mm

![Image](Atmel-ATA6870N_Datasheet_files/img_004.png)

Table 3-1. Pin Description

| Pad Number | Pad Name | Function | Remark |
| - | - | - | - |
| Exposed Pad |  | Heatslug |  |
| 1 | DISCH5 | Output to drive external cell-balancing transistor |  |
| 2 | MBAT5 | Battery cell sensing line |  |
| 3 | DISCH4 | Output to drive external cell-balancing transistor |  |
| 4 | MBAT4 | Battery cell sensing line |  |
| 5 | DISCH3 | Output to drive external cell-balancing transistor |  |
| 6 | MBAT3 | Battery cell sensing line |  |
| 7 | DISCH2 | Output to drive external cell-balancing transistor |  |
| 8 | MBAT2 | Battery cell sensing line |  |
| 9 | DISCH1 | Output to drive external cell-balancing transistor |  |
| 10 | MBAT1 | Battery cell sensing line |  |
| 11 | IRQ | Interrupt output for MCU/ATA6870N below |  |
| 12 | CLK | System clock |  |
| 13 | CS_N | Chip select input from MCU/ATA6870N below |  |
| 14 | SCK | SPI clock input from MCU/ATA6870N below |  |
| 15 | MOSI | Master Out Slave In input from MCU | SPI data input |

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel Atmel

Table 3-1. Pin Description (Continued)

| Pad Number | Pad Name | Function | Remark |
| - | - | - | - |
| 16 | MISO | Master In Slave Out output for MCU | SPI data output |
| 17 | MFIRST | Select Master/Slave |  |
| 18 | DTST | Test-mode pin | Keep pin open (output) |
| 19 | SCANMODE | Test-mode pin | Connected to VSSA |
| 20 | CS_FUSE | Test-mode pin | Connected to VSSA |
| 21 | VDDFUSE | Test-mode pin | Connected to VSSA |
| 22 | DVSS | Digital negative supply |  |
| 23 | DVDD | Digital positive supply input (3.3V) | Connected to AVDD |
| 24 | GND | Ground |  |
| 25 | ATST | Test-mode pin | Keep pin open (output) |
| 26 | AVDD | 3.3V Regulator output |  |
| 27 | AVSS | Analog negative supply |  |
| 28 | TEMPVSS | Ground for temperature measuring |  |
| 29 | TEMP1 | Temperature measuring input 1 |  |
| 30 | TEMP2 | Temperature measuring input 2 |  |
| 31 | TEMPREF | Reference voltage for temperature measuring |  |
| 32 | BIASRES | Internal supply current adjustment |  |
| 33 | PWTST | Test - mode pin | Keep pin open (output) |
| 34 | POW_ENA | Power regulator enable/disable |  |
| 35 | PD_N_OUT | Power down output |  |
| 36 | VDDHVM | Power regulator output to supply e.g. an external microcontroller |  |
| 37 | VDDHVP | Power regulator supply voltage |  |
| 38 | PD_N | Power down input |  |
| 39 | MISO_IN | Master In Slave Out input from ATA6870N above |  |
| 40 | MOSI_OUT | Master Out Slave In output for ATA6870N above |  |
| 41 | SCK_OUT | SPI clock output for input of ATA6870N above |  |
| 42 | CS_N_OUT | Chip select output for input of ATA6870N above |  |
| 43 | CLK_OUT | System clock output for input of ATA6870N above |  |
| 44 | IRQ_IN | Interrupt input from ATA6870N above |  |
| 45 | VDDHV | Supply voltage |  |
| 46 | MBAT7 | Battery cell sensing line |  |
| 47 | DISCH6 | Output to drive external cell-balancing transistor |  |
| 48 | MBAT6 | Battery cell sensing line |  |

![Image](Atmel-ATA6870N_Datasheet_files/img_006.png)

## 4. ATA6870N System Overview

The Atmel ® ATA6870N can be stacked up to 16 times in one string. The communication with MCU is carried out on the lowest level through an SPI bus. The data on the SPI bus is transmitted to the 15 other Atmel ATA6870Ns using the communication interface implemented inside Atmel ATA6870N.

Figure 4-1. Battery Management Architecture with One Battery String

![Image](Atmel-ATA6870N_Datasheet_files/img_007.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel Atmel

Figure 4-2. Battery Management Architecture with Several Battery Strings

![Image](Atmel-ATA6870N_Datasheet_files/img_008.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_009.png)

## 5. Absolute Maximum Ratings

Stresses beyond those listed under "Absolute Maximum Ratings" may cause permanent damage to the device. This is a stress rating only and functional operation of the device at these or any other conditions beyond those indicated in the operational sections of this specification is not implied. Exposure to absolute maximum rating conditions for extended periods may affect device reliability.

Unless otherwise specified all voltages to pin VSSA.

| Parameters | Pin | Symbol | Min. | Max. | Unit |
| - | - | - | - | - | - |
| Ambient temperature |  | T A | -40 | +85 | °C |
| Junction temperature |  | T J | -40 | +125 | °C |
| Storage temperature |  | T S | -55 | +150 | °C |
| Battery cell voltage | MBAT(i+1), MBAT(i) | V MBAT(i+1) - V MBAT(i) | -0.3 | +5.5 | V |
| V VDDHV - V VMBAT7 max |  | V VDDHV - V VMBAT7 | -5.5 | +0.3 | V |
| V MBAT1 | MBAT1 | V MBAT1 | -0.3 | +0.3 | V |
| Supply voltage power regulator | VDDHVP | V VDDHVP | -0.3 | +33.6 | V |
| Operating supply voltage | VDDHV | V VDDHV | -0.3 | +30 | V |
| Supply voltage DVDD (regulator is off) | DVDD | V DVDD | -0.3 | +5.5 | V |
| Supply voltage AVDD (regulator is off) | AVDD | V AVDD | -0.3 | +5.5 | V |
| Test-input | VDDFUSE | V VDDFUSE | -0.3 | +5.5 | V |
| Reference voltage for temperature measuring (regulator is Off) | TEMPREF | V TEMPREF | -0.3 | VDD+0.3 | V |
| Supply voltage VDDHVM (regulator is Off) | VDDHVM | V VDDHVM | -0.3 | +5.5 | V |
| Digital ground | DVSS | V AVSS - V GND | -0.3 | +0.3 | V |
| Analog ground | AVSS | V AVSS - V GND | -0.3 | +0.3 | V |
| Digital/analog ground | AVSS, DVSS | V AVSS - V DVSS | -0.3 | +0.3 | V |
| Ground voltage for temperature measuring | TEMPVSS | V TEMPVSS | -0.3 | +0.3 | V |
| Input voltage for logic I/O pins | CLK, CS_N, SCK, MOSI, DTST, ATST, SCANMODE, MFIRST, POW_ENA, CS_FUSE, PWTST | V CLK , V CS_N , V SCK , V MOSI , V DTST , V ATST , V SCANMODE , V MFIRST , V POW_ENA , V CS_FUSE , V PWTST | -0.3 | VDD + 0.3 | V |
| Input voltage for logic I/O pins | IRQ, MISO | V IRQ , V MISO | -0.3 | +5.5 | V |
| Input voltage for analog I/O pins | TEMP1, TEMP2, BIASRES | V TEMP1 , V TEMP2 , V BIASRES | -0.3 | VDD + 0.3 | V |
| Input voltage for digital high voltage input pins | MISO_IN, IRQ_IN | V MISO_IN , V IRQ_IN | VDDHV - 0.3 | VDDHV + 0.3 | V |
| Voltage at digital high voltage output pins | MOSI_OUT, SCK_OUT, CS_N_OUT, CLK_OUT | V MOSI_OUT , V SCK_OUT , V CS_N_OUT , V CLK_OUT | VDDHV - 0.3 | VDDHV + 0.3 | V |
| Input: PD_N | PD_N | V PD_N | VDDHV - 5.5 | VDDHV + 0.3 | V |
| Output: PD_N_OUT | PD_N_OUT | V PD_N_OUT | -5.5 | +0.3 | V |
| Voltage at cell balancing outputs | DISCH(i) | VDISCH(i) | V MBAT(i) - 0.3 | V MBAT(i+1) + 0.3 | V |

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 5. Absolute Maximum Ratings (Continued)

Stresses beyond those listed under "Absolute Maximum Ratings" may cause permanent damage to the device. This is a stress rating only and functional operation of the device at these or any other conditions beyond those indicated in the operational sections of this specification is not implied. Exposure to absolute maximum rating conditions for extended periods may affect device reliability.

Unless otherwise specified all voltages to pin VSSA.

| Parameters | Pin | Symbol | Min. | Max. | Unit |
| - | - | - | - | - | - |
| HBM ESD ANSI/ESD-STM5.1 JESD22-A114 AEC-Q100 (002) |  | ESD | ±2 |  | kV |
|  |  |  | 500 |  | V |
| CDM ESD STM 5.3.1 | 1, 12, 13, 24, 25, 36, 37, 48 |  | 750 |  | V |
| Latch-up acc. to AECQ100-004, JESD78A |  | LATCH-UP | ±100 |  | mA |

## 6. Thermal Resistance

| Parameters | Symbol | Value | Unit |
| - | - | - | - |
| Package. QFN48 7×7 |  |  |  |
| Max. thermal resistance junction-ambient (1) | R thja max | 20 | K/W |
| Max. thermal resistance junction-case | R thjC max | TBD | K/W |

Note: 1. Package mounted on 4 large PCB (per JESD51-7) under natural convention as defined in JESD51-2.

## 7. Circuit Description and Electrical Characteristics

Unless otherwise specified all parameters in this section are valid for a supply voltage range of 6.9V &lt; V DDHV &lt; 30V and a battery cell voltage of V MBAT(i+1) - V MBAT(i) = 0V to 5V, -40°C &lt; T A &lt; 85°C. All values refer to pin VSSA, unless otherwise specified.

## 7.1 Operating Modes

The Atmel ® ATA6870N has two operation modes.

1. Power-down mode (PDmode)
2. Normal mode (NORM mode)

## 7.1.1 Power-down Mode

In power-down mode all blocks of the IC are switched off.

The circuit can be switched from Power-down to ON mode or back via the PD\_N input. If the pin is connected to VDDHV via an external optocoupler, for example, the circuit is in ON mode. If several Atmel ATA6870N are stacked, the power-down signal must be only provided for the IC on the top level of the stack. The next lower IC receives this information from the PD\_N\_OUT output of its upper IC. The PD\_N\_OUT pin must be connected to either the PD\_N pin of the next lower Atmel ATA6870N or to VSSA.

![Image](Atmel-ATA6870N_Datasheet_files/img_009.png)

Atmel Atmel

Figure 7-1. Power-down

![Image](Atmel-ATA6870N_Datasheet_files/img_010.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Table 7-1. Electrical Characteristics

| No. | Parameters | Test Conditions | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - | - |
| 1.1 | Maximum allowed input current in power-down mode (e.g., leakage current of an optocoupler) |  |  | PD_N | I PD_N |  |  | 50 | µA | A |
| 1.2 | Input current in ON mode |  |  | PD_N | I PD_N | 2.5 |  | 5 | mA | A |
| 1.3 | Maximum voltage (pin PD_N left open) | I PD_N = 0 to 50µA | I PD_N = 0 to 50µA | PD_N | V VDDHV - V PD_N |  |  | 5 | V | A |
| 1.4 | Propagation delay time from power-down mode to NORM mode | min slope I PD_N = | 1 mA msec ------------- | DVDD | t VDDON |  |  | 3 | ms | A |
| 1.5 | Propagation delay time from NORM mode to power-down mode |  |  | DVDD | t VDDOFF |  |  | 10 | ms | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

## 7.1.2 Normal Operating Mode (NORM Mode)

The Atmel ® ATA6870N turns on when the PD\_N signal is switched from low to high. The power supplies AVDD and DVDD as well as VDDHVM (if the input signal POW\_ENA = high) are turned on. The configuration registers are set to their default values. In NORM mode the Atmel ATA6870N can acquire analog data (voltage or temperature channels) upon request from the host microcontroller. When the host microcontroller orders an acquisition through the SPI bus, the IC starts digitizing all voltage and one temperature channel in parallel. The on-chip digital signal processor filters, in real time, the channel samples. When conversion and filtering are done, the data-ready interrupt to the host processor indicates the data availability. The MCU can now read the ADC result registers. The MCU reads the Atmel ATA6870N's status registers to check each IC and to acknowledge the interrupt. When Atmel ATA6870N is in NORM mode, the MCU can be active or in idle mode. In order to wake-up the MCU by an interrupt, the Low Frequency Timer (LFT) can be activated in Atmel ATA6870N. Interrupt is signaled with a high level on IRQ pin. The LFT is re-programmable on the fly and can be reset through SPI, but is not stoppable.

Figure 7-2. Atmel ATA6870N in NORM Mode

![Image](Atmel-ATA6870N_Datasheet_files/img_011.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_009.png)

Atmel

Table 7-2. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 2.1 | Supply voltage |  | VDDHV | V VDDHV | 6.9 |  | 30 | V | A |
| 2.2 | Current consumption IVDDHV (normal mode) |  | VDDHV | I VDDHV |  |  | 15 | mA | A |
| 2.3 | Current consumption in power-down mode (PDmode) I VDDHV + I MBAT(i) max (1) | V MBAT(i+1) - V MBAT(i) = 3.7V | VDDHV |  |  |  | 10 | µA | A |
| 2.4 | Imbalance from battery cell to battery cell in power-down mode (PDN Mode) | V MBAT(i+1) - V MBAT(i) = 3.7V | MBAT(i+1) | I MBAT(i+1) |  |  | 10 | µA | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

Note: 1. Largest input current of the cell inputs MBAT(i)

## 7.2 Interface to Battery Cells

Each input line MBAT(i) and the supply lines VDDHV, AVSS can be protected by additional resistors and a filter capacitor as shown below.

Figure 7-3. External Components between Atmel ATA6870N and the Battery Cells

![Image](Atmel-ATA6870N_Datasheet_files/img_012.png)

MBAT (i) are high impedance input (~2MΩ). Thus, external components can be added to protect ATA6870N chip against current spikes and overvoltage at battery cell level.

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

Table 7-3. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 3.1 | R_IN |  | MBAT(i) |  |  |  | 1 | kΩ | D |
| 3.2 | R_VDDHV |  | VDDHV |  |  |  | 50 | Ω | D |
| 3.3 | R_VSS |  | AVSS |  |  |  | 50 | Ω | D |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

## 7.3 Reduced Number of Battery Cells Configuration

It is possible for Atmel ® ATA6870N to operate with a reduced number of cells: 3, 4, 5, and 6 cell operation are possible. In these cases, the cell-chip inputs corresponding to the missing cells should be connected to the upper cell potential of the module.

Figure 7-4. Connection with 4 Cells only

![Image](Atmel-ATA6870N_Datasheet_files/img_013.png)

Battery cell 1 (MBAT1, MBAT2) and battery cell 6 (MBAT6, MBAT7) must always be used for the lowest/highest cell.

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Atmel

## 7.4 ATA6870N External MCU Supply

The Atmel ® ATA6870N provides a 3.3V power-supply for external components such as the microcontroller unit (MCU). The input pin for this supply is pin VDDHVP, and the output pin is VDDHVM. This regulator is able to supply the MCU directly from the topmost battery cell of a string. The power regulators of all stacked Atmel ATA6870N are therefore put in serial configuration to avoid imbalance.The regulator can be disabled with the digital input pin POW\_ENA.

Table 7-4. Truth Table

| Pin | Symbol | Value | Function |
| - | - | - | - |
| POW_ENA | V POW_ENA | Low High | Voltage regulator disabled Voltage regulator enabled |

Logic levels: Low = V DVSS , High = V DVDD

![Image](Atmel-ATA6870N_Datasheet_files/img_014.png)

Atmel Atmel

Figure 7-5. MCU Supply with the Internal Power Supply

![Image](Atmel-ATA6870N_Datasheet_files/img_015.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Table 7-5. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 4.1 | Supply voltage |  | VDDHVP | V VDDHVP | 6.9 |  | 33.3 | V | A |
| 4.2 | Output voltage |  | VDDHVM | V VDDHVM | 3.1 | 3.3 | 3.5 | V | A |
| 4.3 | DC output current |  | VDDHVM | I VDDHVM |  |  | 20 | mA | A |
| 4.4 | Peak output current (1) |  | VDDHVM | I VDDHVM |  |  | 50 | mA | A |
| 4.5 | Capacitor load (2) |  | VDDHVM |  | 30 | 33 |  | µF | D |
| 4.6 | Capacitor load (2) |  | VDDHVM |  | 200 | 220 |  | nF | D |
| 4.7 | High level input voltage |  | POW_ENA | V POW_ENA | 0.7 × V DVDD |  |  | V | A |
| 4.8 | Low level input voltage |  | POW_ENA | V POW_ENA |  |  | 0.3 × V DVDD | V | A |
| 4.9 | Hysteresis |  | POW_ENA | V POW_ENA | 0.05 × V DVDD |  |  | V | C |
| 4.10 | Input current | V POW_ENA = 0V to V DVDD | POW_ENA | I POW_ENA | -1 |  | +1 | µA | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

- Notes: 1. Maximum current the power regulator can provide, time limited by thermal consideration only

2. These capacitors are mandatory

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel Atmel

Figure 7-6. MCU Supply with an External Power Supply

![Image](Atmel-ATA6870N_Datasheet_files/img_016.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

## 7.5 Analog Blocks

## 7.5.1 Battery Voltage Measuring

Figure 7-7. Block Diagram Battery Voltage Measurement

![Image](Atmel-ATA6870N_Datasheet_files/img_017.png)

The battery voltage measurement block contains

- a 2-input multiplexer
- a voltage reference,
- a 12-bit ADC
- the upper part of digital voltage level shifters

## 7.5.1.1 Input Multiplexer

The multiplexer has 3 inputs. Each of the functions are described in the table below:

Table 7-6. Inputs of the Multiplexer

| Input | Function |
| - | - |
| V(MBAT (i+1) , MBAT (i) ) | Input voltage measurement |
| V(MBAT (i) , MBAT (i) ) | Offset error acquisition of ADC |

The multiplexer inputs are controlled by SPI.

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.5.1.2 12 Bits Incremental ADC

The purpose of this cell is to convert an analog input into a 12-bit digital word.

Table 7-7. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 5.1 | Accuracy of voltage channel (1) | Maximum input noise 0.5mVrms 2.2V < V MBAT(i+1) - V MBAT(i) < 4.5V | MBAT(i+1), MBAT(i) |  | -10 |  | +10 | mV | A |
| 5.1 | Accuracy of voltage channel (1) | Maximum input noise 0.5mVrms 0V < V MBAT(i+1) - V MBAT(i) < 5V | MBAT(i+1), MBAT(i) |  | -20 |  | +20 | mV | A |
| 5.1 | Accuracy of voltage channel (1) | Maximum input noise 0.5mVrms V MBAT(i+1) - V MBAT(i) = 3.7V T J = -20°C to +65°C | MBAT(i+1), MBAT(i) |  | -7 |  | +7 | mV | A |
| 5.1 | Accuracy of voltage channel (1) | Maximum input noise 0.5mVrms Aging (3) | MBAT(i+1), MBAT(i) |  | -11 |  | +11 | mV | C |
| 5.1 | Accuracy of voltage channel (1) | Maximum input noise 0.5mVrms Aging (4) | MBAT(i+1), MBAT(i) |  | -17 |  | +17 | mV | C |
| 5.2 | Input voltage range |  | MBAT(i+1), MBAT(i) | V MBAT(i+1) , V MBAT(i) | 0 |  | 5 | V | A |
| 5.3 | Input resolution (1 LSB) |  |  | V LSB |  | 1.5 |  | mV | D |
| 5.4 | Reference voltage |  |  | V Ref |  | 1.667 |  | V | D |
| 5.5 | Offset voltage |  | MBAT(i+1), MBAT(i) | V MBAT(i+1) , V MBAT(i) |  | 410 |  | LSB | A |
| 5.6 | Gain voltage |  | MBAT(i+1), MBAT(i) | V MBAT(i+1) , V MBAT(i) |  | 655 |  | LSB/V | A |
| 5.7 | System clock |  | CLK | f CLK | 450 | 500 | 550 | kHz | D |
| 5.8 | SPI interface clock |  | SCK | f SCK |  |  | 0.5 × f CLK |  | D |
| 5.9 | Conversion rate (2) | t conv = (2 12 + 1) / f CLK |  | t conv |  | 8.194 |  | ms | D |
| 5.10 | Input bandwidth |  | MBAT(i+1), MBAT(i) | f BW |  | 50 |  | Hz | D |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

- Notes: 1. The accuracy of the voltage channels is guaranteed with no external resistor in the MBAT(i), MBAT(i+1) lines.
2. Conversion rate without readout times of SPI
3. Aging temperature T J = 125°C, drift measured at 25°C and 85°C
4. Aging temperature T J = 125°C, drift measured at -40°C

![Image](Atmel-ATA6870N_Datasheet_files/img_018.png)

Atmel

## Converting ADC Results to Voltage

The silicon is factory adjusted by measuring offset voltage (VOffset) with both ADC inputs connected to MBATi and calibration of the adc(MBAT i+1 ) value to 3031 at MBAT i+1 = 4.0V (see Figure 7-8).

Figure 7-8. Characteristics of AD-converter

![Image](Atmel-ATA6870N_Datasheet_files/img_019.png)

adc(VOffset): ADC result with both ADC inputs connected to MBAT i (0V input voltage)

adc(VMBAT i+1 -VMBAT i ): Uncorrected ADC result of the ADC input voltage

## Standard Procedure with Frequent Offset Adjustment

To use the frequent offset adjustment of the ADC the following parameters need to be measured:

adc(VOffset) ADC result with both ADC inputs connected to MBAT i (0V input voltage)

adc(VMBAT i+1 -VMBAT i ) Uncorrected ADC result of the ADC input voltage

Calculation of the battery cell voltage:

VIn = 4V × (adc(VMBAT i+1 -VMBAT i ) - adc(VOffset)) / (3031 - adc(VOffset))

with VIn = V(MBAT i+1 )-V(MBAT i )

It's not necessary to measure VOffset during every measuring cycle.

Regular updates are sufficient.

## Standard Procedure without Offset Adjustment

With increasing input voltages the failure caused by the ADC can be ignored. In this case the battery cell voltage can be calculated by the following equation:

VIn = 4V × (adc(VMBAT i+1 -VMBAT i ) - 0.1 × 2 12 ) / (3031 - 0.1 × 2 12 )

The following simplification can be done with less than 1mV rounding error:

VIn = 1.52656 × 10 -3 × (adc(VMBAT i+1 -VMBAT i ) - 410)

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.5.1.3 Acquisition Time and Clocking

The acquisition time depends on the number of Atmel ® ATA6870Ns to be addressed.

Table 7-8. Electrical Characteristics

| Number of ATA6870N | SCK Frequency (kHz) | CLK Frequency (kHz) | Conversion Time (ms) | Total Acquisition Duration (ms) (1) |
| - | - | - | - | - |
| 1 | 250 | 500 | 8.2 | 9.5 |
| 2 | 250 | 500 | 8.2 | 10.2 |
| 3 | 250 | 500 | 8.2 | 10.8 |
| 4 | 250 | 500 | 8.2 | 11.5 |
| 5 | 250 | 500 | 8.2 | 12.2 |
| 6 | 125 | 500 | 8.2 | 17.0 |
| 7 | 125 | 500 | 8.2 | 18.4 |
| 8 | 125 | 500 | 8.2 | 19.7 |
| 9 | 125 | 500 | 8.2 | 21.1 |
| 10 | 62.5 | 500 | 8.2 | 36.1 |
| 11 | 62.5 | 500 | 8.2 | 38.8 |
| 12 | 62.5 | 500 | 8.2 | 41.5 |
| 13 | 62.5 | 500 | 8.2 | 44.2 |
| 14 | 62.5 | 500 | 8.2 | 46.8 |
| 15 | 62.5 | 500 | 8.2 | 49.5 |
| 16 | 62.5 | 500 | 8.2 | 52.2 |

Notes: 1. The total acquisition time takes the following into account:

- ADC conversion

- Reading of voltage values in burst mode for all ATA6870N devices,

- Reading of temperature values for all ATA6870N devices (only one temperature input is read).

SPI clock (pin SCK) must a maximum of half the frequency of the system clock CLK.

![Image](Atmel-ATA6870N_Datasheet_files/img_009.png)

Atmel

## 7.5.2 Battery Cell Discharge

Each battery cell can be discharged with an external resistor and an NMOS transistor.

Figure 7-9. External Circuit for Cell Balancing

![Image](Atmel-ATA6870N_Datasheet_files/img_020.png)

The pin DISCH(i) (Discharge for battery cell i) is intended to switch on the external discharge resistor in parallel to the battery cell to bypass charge current for cell balancing reasons.

The pin DISCH(i) is a digital output:

No discharge: V DISCH(i) = V MBAT(i)

Discharge: V DISCH(i) = V MBAT(i+1)

Table 7-9. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 6.1 | Operating voltage range |  | MBAT(i) | MBAT (i+1) - MBAT (i) | 1.5 |  | 5 | V | A |
| 6.2 | High-level output voltage | I DISCH(i) = -10µA, MBAT (i+1) - MBAT (i) = 1.5V to 5V | DISCH(i) | V DISCH(i) - V MBAT(i) | V MBAT(i+1) - 50 mV |  |  | V | A |
| 6.3 | High-level output voltage | I DISCH(i) = -1mA MBAT (i+1) - MBAT (i) = 3V to 5V | DISCH(i) | V DISCH(i) - V MBAT(i) | V MBAT(i+1) - 0.6V |  |  | V | A |
| 6.4 | Pull-down resistor (1) |  | DISCH(i)- MBAT(i) |  | 60 |  | 140 | kΩ | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

Note: 1. Integrated pull-down resistor between pins DISCH(i) and MBAT(i)

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.5.3 Temperature Channel

The temperature sensors are based on a resistor divider using a standard resistor and an NTC resistor. This resistor divider is connected to the reference of the ADC for temperature measuring. As the ADC is sharing same reference value, the output of temperature measurement with ADC is ratio metric.

Figure 7-10. Battery Cell Temperature Measurement

![Image](Atmel-ATA6870N_Datasheet_files/img_021.png)

During one measuring cycle only one temperature input can be measured by the ADC. The channel can be selected in the Operation Register (0x02) by the TempMode bit (bit 3).

The ADC output is equal to:

<!-- formula-not-decoded -->

Table 7-10. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 7.1 | Reference voltage |  | TEMPREF | V TEMPREF - V TEMPVSS | 1.1 | 1.2 | 1.3 | V | A |
| 7.2 | Reference voltage output current |  | TEMPREF | I TEMPREF |  |  | 2 | mA | A |
| 7.3 | Input voltage range |  | TEMP1 | V TEMP1 | 0 |  | V TEMPR EF | V | A |
| 7.4 | Input voltage range |  | TEMP2 | V TEMP2 | 0 |  | V TEMPR EF | V | A |
| 7.5 | Input current | VTEMPx = 1.2V | TEMPx | I TEMPx |  |  | 1 | µA | A |
| 7.6 | Code output for value(RES_NTCx) = value (RES_REFx) | V(TEMPi, TEMPVSS) = 0.5 × V(TEMPREF, TEMPVSS) |  |  | 931 D | 956 D | 981 D |  | A |
| 7.7 | Code output for value(RES_NTC) = 0 | V(TEMPi, TEMPVSS) = 0 |  |  | 385 D | 410 D | 435 D |  | A |
| 7.8 | Code output for value(RES_NTC) = infinite | V(TEMPi, TEMPVSS) = V(TEMPREF) |  |  | 1477 D | 1502 D | 1527 D |  | A |

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Atmel

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

## 7.5.4 Internal Voltage Regulator

The regulator output is pin AVDD. The pins AVDD and DVDD have to be connected together. An external filtering capacitor (10nF recommended) is used to filter and stabilize the function. The regulator output can be used to supply outside functions at the price of power supply imbalance between battery cells.

Table 7-11. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 8.1 | Supply voltage range |  | VDDHV | V VDDHV | 6.9 |  | 30 | V | A |
| 8.2 | Regulated output voltage |  | AVDD | V AVDD | 3.1 | 3.3 | 3.5 | V | A |
| 8.3 | Output current |  | AVDD | I AVDD | 0 |  | 5 | mA | A |
| 8.4 | C load (load capacitor) |  | C load |  | 9 | 10 |  | nF | D |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

## 7.5.5 Central Biasing

This block generates a precise bias current to supply internal blocks of the IC. Connection of any external loads to this pin is not allowed.

Table 7-12. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 9.1 | Biasing voltage |  | BIASRES | V BIASRES |  | 1.2 |  | V | A |
| 9.2 | External resistor |  |  | R Refbias |  | 121 |  | kΩ | D |
| 9.3 | Tolerance |  |  | ΔR Refbias | -1 |  | +1 | % | D |
| 9.4 | Maximum external parasitic capacitor |  | BIASRES | C External |  |  | 50 | pF | D |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

Figure 7-11. Internal Bias Current Generation

![Image](Atmel-ATA6870N_Datasheet_files/img_022.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.5.6 RC Oscillator

Table 7-13. Internal RC Oscillator Frequency

| No. Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - |
| 10.1 Oscillator frequency |  |  | f Osc | 45 | 50 | 55 | kHz | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

## 7.5.7 Power On Reset

The power on reset is used to initialize the digital part at power-up.

The power on reset circuit is functional when the voltage at pin DVDD is larger than V POROP .

There are two reset sources:

System "hard reset"

System hard reset occurs when the voltage at pin DVVD goes below the power on reset threshold.

ATA6870N registers are set to their initial values.

After t = t RESET , the MCU can access the Atmel ® ATA6870N.

Figure 7-12. Power On Reset

Table 7-14. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 11.1 | Power on reset functional |  | DVDD | V POROP |  |  | 0.8 | V | A |
| 11.2 | Power on reset off |  | DVDD | V POROFF | 1.5 |  | 2.5 | V | A |
| 11.3 | Power on reset hysteresis |  | DVDD | V POROFF - V PORON | 0.03 |  |  | V | C |
| 11.4 | Power on reset time |  |  | t RESET |  |  | 800 | µs | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Atmel

![Image](Atmel-ATA6870N_Datasheet_files/img_023.png)

## 7.6 Digital Part

## 7.6.1 General Features

The digital parts of the ATA6870N includes the following blocks:

- 4-wire-SPI full duplex communication with external host MCU
- SPI system protocol management (frames decoding) and configuration registers bank
- Interrupt to MCU management
- Operations decoding (voltage and/or temperature acquisition) and analog part control
- Low frequency timer (50kHz) for wake-up management

## 7.6.2 Host Interface

Figure 7-13. Host Interface

![Image](Atmel-ATA6870N_Datasheet_files/img_024.png)

The communication between Atmel ® ATA6870N (1) and its host MCU, as well as ATA6870N (n) and ATA6870N(n-1) is based on a 4 wire serial/parallel SPI interface (CS\_N, SCK, MISO, MOSI) and an interrupt line (IRQ). The SPI interface allows register read and write operations. The interrupt line indicates events that require host intervention.

Atmel ATA6870N(n)'s 4 wire-SPI bus inputs (CS\_N, SCK, MOSI) are up-shifted through level shifters. They are internally connected to the outputs CS\_N\_OUT, SCK\_OUT, MOSI\_OUT and connected to ATA6870N(n+1) (CS\_N, SCK, MOSI).

Atmel ATA6870N(n)'s 4 wire-SPI bus output (MISO) and ATA6870N(n)'s interrupt (IRQ) are down-shifted through level shifters and connected to ATA6870N(n-1) (MOSI\_IN, IRQ\_IN) or host MCU (n = 1).

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.6.3 Interrupt

In NORM mode (normal mode), the reasons for an interrupt request are:

- The availability of measured data (data ready)

When a voltage measurement is completed, the dataRdy flag is set in the status register.

The ATA6870N cannot decode any new incoming operation until the dataRdy flag is released.

- The low frequency timer (LFT) elapses (wakeup)

The wakeup flag is set in the status register when the LFT elapses. The LFT is controlled via the SPI interface.

- A transmission error is flagged during the last SPI transaction (the commError bit is set in the status register).
- If an undervoltage condition occurs. The undervoltage function is controllable via SPI interface.

A mask bit in the irqMask register corresponds to each interrupt source. The MCU must read the ATA6870N status register before the interrupt is cleared. With each SPI access a 16-bit IRQ state is sent via MISO to the MCU with the interrupt state of all stacked ATA6870N (see Section 7.6.4.1 "SPI Transaction Fields" on page 26).

In PDmode (power down), if the digital control part and MCU are not supplied, neither SPI command nor interrupt are transmitted over the interface.

## 7.6.4 SPI Interface

The full duplex SPI interface block allows communication with the host MCU using four wires (MISO, MOSI, SCK and CS\_N). SPI transactions are based on a byte-access MSB first protocol.

## 7.6.4.1 SPI Transaction Fields

Most of the time, the SPI frame is defined by 4 distinct fields:

IDENTIFICATION (2 bytes): 16-bit chip identification (MOSI), in parallel 16-bit IRQ state (MISO)

CONTROL (1 byte): 7-bit register address + 1-bit read/write information (MOSI)

DATA (k byte): k*8 bits data (MOSI or MISO depending on the access direction)

CHKSUM (1 byte): 8 bits if the Chksum\_ena bit is set in the Ctrl register (register 0x01, bit 4)

Figure 7-14. SPI Transaction Fields Organization

![Image](Atmel-ATA6870N_Datasheet_files/img_025.png)

Note: 1. Only send if chksum\_ena bit set to 1 in the Ctrl register

![Image](Atmel-ATA6870N_Datasheet_files/img_009.png)

Atmel

## 7.6.4.2 Identification Field

## Atmel ATA6870N Chip Identification

The two chip identification bytes are sent over MOSI to the Atmel ® ATA6870N(n) in the chain. The ATA6870N(n) checks the LSB. When LSB=1, the information is for this device. The SPI address will be decoded and the information processed. Independent from this the identification bytes are shifted by one bit to the right and transferred to the next ATA6870N(n) in the chain. The 2 identification bytes allows the identification of up to 16 ATA6870Ns.

Figure 7-15. Identification Field: Chip-ID Reception

![Image](Atmel-ATA6870N_Datasheet_files/img_026.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.6.4.3 ATA6870N IRQ Identification

Figure 7-16. IRQ Propagation Scheme

![Image](Atmel-ATA6870N_Datasheet_files/img_027.png)

ATA6870N(n) IRQ output is connected to ATA6870N(n-1) IRQ\_IN input.

ATA6870N(n-1) IRQ output is a logic OR between IRQ\_IN and its internal irq\_int signal.

ATA6870N(1) IRQ output is connected to MCU.

Figure 7-17. Identification Field: Interrupt State Emission

![Image](Atmel-ATA6870N_Datasheet_files/img_028.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Atmel With each SPI access, a 16- bit IRQ state is send via MISO synchronous to the identification field to the MCU with the interrupt state of all stacked Atmel ATA6870N. The MCU, interrupted by an ATA6870N, has to send the identification field to check the IRQ levels (in that case the checksum is not considered). It is also possible to continue the transaction with CONTROL and DATA field. The MCU decodes the identification field shifted in MISO input. When bit m is set, ATA6870N(16-m) is requesting interrupt.

Figure 7-18. Identification Field

![Image](Atmel-ATA6870N_Datasheet_files/img_029.png)

## 7.6.4.4 CONTROL Field

The CONTROL field defines the register to access and the direction (read/write). The size of the data (8, 16, or 112 bits) is defined by the address value in the CONTROL field.

Table 7-15. Control Field

| CONTROL Field | Bit7 | Bit6 | Bit5 | Bit4 | Bit3 | Bit2 | Bit1 | Bit0 |
| - | - | - | - | - | - | - | - | - |
|  | A6 | A5 | A4 | A3 | A2 | A1 | A0 | W/Rd |

## 7.6.4.5 DATA Field

The DATA field can be composed of 1, 2, or 14 bytes depending on the accessed register. Irrespective of the data direction, a byte is always transmitted with MSB first; a multi-byte word is transmitted with MSByte first.

Figure 7-19. CONTROL and DATA Fields - 8-bits Register Write

![Image](Atmel-ATA6870N_Datasheet_files/img_030.png)

Figure 7-20. CONTROL and DATA Fields - 8-bits Register Read

![Image](Atmel-ATA6870N_Datasheet_files/img_031.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_032.png)

Atmel In order to retrieve results from all channels in one Atmel ® ATA6870N without having to request for each channel, an SPI 112-bit read-only "burst access" (dataRd16Burst register; address = 0x7F) is implemented. When requested, the ATA6870N outputs its 6 voltage channels V6 to V1 and one of the two temperature channels T2 and T1 in sequence on the SPI bus. The diagrams below show the CONTROL and DATA fields of such an access.

Figure 7-21. CONTROL and DATA Fields - 16-bits Register Write

![Image](Atmel-ATA6870N_Datasheet_files/img_033.png)

Figure 7-22. CONTROL and DATA Fields - 16-bits Register Read

![Image](Atmel-ATA6870N_Datasheet_files/img_034.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_006.png)

Atmel One Atmel ® ATA6870N frame corresponds to the set of results obtained in one Atmel ATA6870N. An Atmel ATA6870N frame is formatted as follows:

Figure 7-23. CONTROL and DATA Fields - 112-bits Register Read

![Image](Atmel-ATA6870N_Datasheet_files/img_035.png)

Figure 7-24. SPI Access to dataRd16burst Register 0x7F

![Image](Atmel-ATA6870N_Datasheet_files/img_036.png)

When reading data of chained ATA6870N, data is transferred as follow:

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

Figure 7-25. Example with two Atmel ATA6870N in a Chain

![Image](Atmel-ATA6870N_Datasheet_files/img_037.png)

## 7.6.4.6 Communication Error

Correct communication can be verified using various functions of the Atmel ATA6870N.

For internal synchronization, it is mandatory to keep CLK running during any SPI access; CLK must be set on 4 clock cycles (at least) before SPI access starts, and must be kept on 4 clock cycles (at least) after SPI access ends up. Keeping at least 4 CLK clock cycles between two consecutive SPI accesses is mandatory. If this is not the case, the Atmel ATA6870Ns will detect an error in communication. The CommError bit will be set in the status register 0x06).

Figure 7-26. SPI Access and CLK Activity

![Image](Atmel-ATA6870N_Datasheet_files/img_038.png)

The Atmel ATA6870N verifies that complete bytes (8bits long) are always transmitted. A transition starts when CS\_N goes to low and it ends when CS\_N goes to high. The number of clock cycles (signal SCK) is monitored during the transition. This number of clock cycles has to be modulo 8. If the CS\_N length is not modulo 8 clock cycles, the bit CommError is set in the status register. This will cause an interrupt to the MCU if the CommError is not masked by the commErrorMsk bit in the IrqMask register.

## 7.6.4.7 CHKSUM Field

The Atmel ® ATA6870N provides the possibility of verifying the transmitted data using a checksum. Setting chksum\_ena bit to 1 in the Ctrl register (default = 0) activates the checksum feature.

The chksum field is an 8-bit checksum computed from the proceeding data (control and data fields, byte 3 to byte n-1). It is based on the polynomial x 8 +x 2 +x 1 +1. The way it is computed is depicted below:

Figure 7-27. LFSR-based Checksum Computation

![Image](Atmel-ATA6870N_Datasheet_files/img_039.png)

The checksum is calculated from the CONTROL field and DATA field by a polynomial division. The DATA field can consist of 1 byte up to 14 bytes (112-bit read-only "burst access"). The IDENTIFICATION field (2 bytes) is not used to generate the checksum. The checksum is always sent by the microcontroller, independent of read write mode.

The checksum is in the LFSR (linear feedback shift register) when the complete bitstream (the whole fields of the transaction) followed by 0x00 have been shifted in the LFSR.

The checksum verification on the complete data transmission was OK when the complete bitstream followed by the checksum have been shifted in the LFSR, and the content of the LFSR is 0x00. If this is not the case, the receiving ATA6870N will set the chkError bit in the status register. This will cause an interrupt to the MCU if the chkError is not masked by the chkErrorMsk bit in the IrqMask register. See the example below. The checksum is serially computed from the 8-bit value 0x57. So the bitstream 0x5700 is shifted in the LFSR. The resulting checksum is [f6o, f6i, f5i … f0i] at the last shift in cycle:

![Image](Atmel-ATA6870N_Datasheet_files/img_018.png)

Atmel During an SPI write access, the checksum is computed by the MCU and sent MSB first in the CHKSUM field. For an SPI read access, the checksum is computed by the Atmel ® ATA6870N and is checked by the MCU. During CHKSUM, MCU has to send 0x00 on MOSI, and must check that its own LFSR equals 0x00 at the end of CHKSUM field.

Table 7-16. checksum = [f6o, f6i, ... f0i] = 0xA2

| Input - X | f01 - 0 | f1i - 0 | f2i - 0 | f3i - 0 | f4i - 0 | f5i - 0 | f6i - 0 | f6o - 0 |
| - | - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| 5 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| D 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
| 0 | 0 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| 7 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 | 0 |
| D 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 1 | 0 | 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |
| 0 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 | 0 |
| D 0 | 0 | 1 | 1 | 0 | 1 | 0 | 1 | 1 |
| 0 | 1 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |
| 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 | 0 |
| 0 | 0 | 1 | 0 | 0 | 0 | 1 | 0 | 1 |

## 7.6.4.8 Device Position

For the Atmel ATA6870N (1), this is the device on the lowest level, the SPI has to work as a standard logic CMOS interface to the MCU. The SPI's between stacked ATA6870N have to work as level-shifters based on current sources. These different physical interfaces can be selected by the Pin MFIRST.

Table 7-17. Device Position

| MFIRST | Configuration |
| - | - |
| 0 | ATA6870N (2) to ATA6870N (n) |
| 1 | ATA6870N (1) |

Table 7-18. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 12.1 | High level input voltage |  | MFIRST | MFIRST | 0.7 × DVDD |  |  | V | A |
| 12.2 | Low level input voltage |  | MFIRST | MFIRST |  |  | 0.3 × DVDD | V | A |
| 12.3 | Hysteresis |  | MFIRST | MFIRST | 0.05 × DVDD |  |  | V | C |
| 12.4 | Input current | V MFIRST = 0V to V DVDD | MFIRST | MFIRST | -1 |  | +1 | µA | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.6.5 Digital Inputs and Outputs

## 7.6.5.1 Digital Output Characteristics

Digital Output Characteristics (MISO, IRQ)

If the Atmel ® ATA6870N is configured as first IC (master) in a string (MFIRST = 1), these pins are configured as an open drain output. If the ATA6870N is configured to be a stacked IC (MFIRST = 0), the output signals MISO and IRQ coming from the upper IC need to be transferred to the MISO and IRQ outputs of the master in the string via the MISO\_IN and IRQ\_IN inputs. In this case the MISO and IRQ outputs act as level shifters based on current sources.

Table 7-19. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 13.1 | Low level output voltage | I OUT = +5mA MFIRST = 1 | MISO, IRQ | V MISO , V IRQ |  |  | 0.2 × VDD | V | A |
| 13.2 | Low level output current | ±0.3V, MFIRST = 0 | MISO, IRQ | I MISO , I IRQ | -13 |  | -8 | µA | A |
| 13.3 | High level output current | ±0.3V, MFIRST = 0 | MISO, IRQ | I MISO , I IRQ | -65 |  | -40 | µA | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

Digital Output Characteristics (MOSI\_OUT, SCK\_OUT, CS\_N\_OUT, CLK\_OUT)

These outputs act as level shifters based on current sources. They transfer the input signals MOSI\_OUT, SCK\_OUT, CS\_N\_OUT, CLK\_OUT to the next IC above. If the ATA6870N is the IC on the top level of a string, these outputs must be connected to VDDHV.

Table 7-20. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 14.1 | Low level output current | VDDHV + 1V to VDDHV + 2V | (1) | V (1) | 25 |  | 55 | µA | A |
| 14.2 | High level output current | VDDHV + 1V to VDDHV + 2V | (1) | V (1) | -1 |  | +1 | µA | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

Note: 1. MOSI\_OUT, SCK\_OUT, CS\_N\_OUT, CLK\_OUT

## 7.6.5.2 Digital Input Characteristics

Digital Input Characteristics (MISO\_IN, IRQ\_IN)

Table 7-21. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 15.1 | Low level input current | (VDDHV + 1.4V) ±0.3V | MISO_IN, IRQ_IN | I MISO_IN I IRQ_IN | 13 |  |  | µA | A |
| 15.2 | High level input current | (VDDHV + 1.4V) ±0.3V | MISO_IN, IRQ_IN | I MISO_IN I IRQ_IN |  |  | 40 | µA | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

![Image](Atmel-ATA6870N_Datasheet_files/img_009.png)

Atmel Digital Input Characteristics (CS\_N, SCK, MOSI, CLK)

Table 7-22. Electrical Characteristics

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 16.1 | High level input voltage | MFIRST = 1 | (1) | V (1) | 0.7 × DVDD |  | DVDD | V | A |
| 16.2 | Low level input voltage | MFIRST = 1 | (1) | V (1) |  |  | 0.3 × DVDD | V | A |
| 16.3 | High level input current | MFIRST = 1 |  | I (1) | 50 |  | 100 | µA | A |
| 16.4 | Low level input current | MFIRST = 1 |  | I (1) | -130 |  | -70 | µA | A |
| 16.5 | Low level input current | MFIRST = 0, V (1) = 1V to 2V | (1) | I (1) | -55 |  | -35 | µA | A |
| 16.6 | High level input current | MFIRST = 0 V (1) = 1V to 2V | (1) | I (1) | -1 |  | +1 | µA | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter Note: 1. CS\_N, SCK, MOSI, CLK

## 7.6.5.3 Test-mode Pins

The test-mode pins DTST, ATST, PWTST (outputs) have to be kept open in the application. The test-mode pins SCANMODE and CS\_FUSE (inputs) have to be connected to VSSA. These inputs have an internal pull-down resistor. The test-mode pin VDDFUSE is a supply pin. It must also be connected to VSSA.

Table 7-23. Input Characteristics Pins SCANMODE, CS\_FUSE, VDDFUSE

| No. | Parameters | Test Conditions | Pin | Symbol | Min. | Typ. | Max. | Unit | Type* |
| - | - | - | - | - | - | - | - | - | - |
| 18.1 | Pull-down resistor |  | SCANMODE, CS_FUSE | R SCANMODE , R CS_FUSE | 50 |  | 200 | kΩ | A |

*) Type means: A = 100% tested, B = 100% correlation tested, C = Characterized on samples, D = Design parameter

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.7 Operations

## 7.7.1 Voltage and Temperature Measurement

At startup, the Atmel ® ATA6870N is supplied and is waiting for any operation request.

The available operations are:

- 6 channels voltage acquisition with a temperature acquisition
- with voltage = V(MBAT i+1 , MBAT i ) (standard operation) and with voltage = V(TEMP1 or TEMP2, TEMPVSS) (standard operation)
- with voltage = V(MBAT i , MBAT i ) (offset calibration: CalOffset operation) and with voltage = V(TEMPVSS, TEMPVSS) (offset calibration: CalOffset operation)

Operation completion is flagged to the host MCU via the IRQ output in conjunction with dataRdy bit set in the status register. In order to retrieve the full results in a single access, the user has to access the dataRd16burst register (112bits). Getting the results of a single channel (voltage or temperature) is also possible. For this, first select the channel to read through the ChannelReadSel register, then retrieve the channel value through the DataRd16 register. It is not possible to order a new operation until the previous operation has been acknowledged. The host MCU acknowledges the interrupt by reading the status register. This resets the dataRdy bit as well as the IRQ output, and enables the ATA6870N to start the next operation. Writing NoOp in the Operation register during an operation running aborts the current operation. In this case, the dataRdy bit is not set and interrupt is not requested to the host MCU. The Opstatus register flags whether operation is running, aborted, ended, or no operation is running.

## 7.7.2 Discharge Function

Each channel is independently dischargeable. Discharge is activated or deactivated by the register ChannelDischSel.

## 7.7.3 Low Frequency Timer Function

A low frequency timer (LFT), synchronous to internal 50 kHz oscillator provides the host MCU with a low power timer, which useful to either synchronize operations in the host MCU or monitor the Atmel ATA6870N's activity.

The LFT elapsing asserts an interrupt to the host MCU if the corresponding mask bit in the IrqMask register is not set.

Default is LFT not enabled. To enable the LFT, set the LFTimer\_ena bit to 1 in the Ctrl register.

LFT counting time is fully programmable in the register LFTimer.

Changing the LFTimer register restarts the LFT if the new counting time is smaller than the current value of the LFT. Otherwise, LFT runs until it reaches the new end value.

Asserting LFTRst bit in the Rstr register resets and restarts the LFT if the LFT is enabled. Otherwise, LFT is reset but not started.

Each ATA6870N will assert its own interrupt when the timer elapses. Depending on how the timer is used, the host MCU may mask LFTdone interrupts in the whole ATA6870Ns chain, except the first one. As internal RC oscillators are not synchronized, this prevents the MCU from being interrupted each time one of the LFT elapses.

## 7.7.4 Undervoltage Detection

A programmable undervoltage detection function is embedded in the ATA6870N. After being digitalized, each of the 6 voltages is compared to a programmable threshold defined in the UdvThresh register. If one of the six channels is out of the range defined by the threshold, an interrupt is requested to the host MCU if the corresponding udv mask bit is not set in the IrqMask register.

The default threshold is 1.5V.

As soon as MCU has acknowledged, undervoltage information is no more available to MCU, because status register is cleared when MCU reads it out. As a consequence, the next undervoltage interrupt cannot occur until the Atmel ATA6870N leaves its current undervoltage state.

![Image](Atmel-ATA6870N_Datasheet_files/img_040.png)

Atmel

## 7.8 Registers

Registers are read and written through the SPI interface.

Table 7-24. Register Mapping

| Register Address | Control Field Read Mode | Control Field Write Mode | Register Name | Access | Type | Function |
| - | - | - | - | - | - | - |
| 0x00 | 0x00 | - | RevID | R | 8 bits | Revision ID/value Mfirst, pow_on |
| 0x01 | 0x02 | 0x03 | Ctrl | RW | 8 bits | Control register |
| 0x02 | 0x04 | 0x05 | Operation | RW | 8 bits | Operation request |
| 0x03 | 0x06 | - | OpStatus | R | 8 bits | Operation status |
| 0x04 | - | 0x09 | Rstr | W | 8 bits | Software reset |
| 0x05 | 0x0A | 0x0B | IrqMask | RW | 8 bits | Mask interrupt sources |
| 0x06 | 0x0C | - | Status | R | 8 bits | Status interrupt sources |
| 0x08 | 0x10 | - | ChannelUdvStatus | R | 8 bits | Channels undervoltage status |
| 0x09 | 0x12 | 0x13 | ChannelDischSel | RW | 8 bits | Select channel to discharge |
| 0x0A | 0x14 | 0x15 | ChannelReadSel | RW | 8 bits | Select channel to read |
| 0x0B | 0x16 | 0x17 | LFTimer | RW | 8 bits | Low frequency timer control |
| 0x0C | 0x18 | - | CalibStatus | R | 8 bits | Reserved |
| 0x0D | 0x1A | 0x1B | FuseCtrl | RW | 8 bits | Reserved |
| 0x10 | 0x20 | 0x21 | UdvThresh | RW | 16 bits | Undervoltage detection threshold |
| 0x11 | 0x22 | - | DataRd16 | R | 16 bits | Single access to selected channel value |
| 0x12 | 0x24 | 0x25 | ATA6870NTest | RW | 16 bits | Reserved |
| 0x7F | 0xFE | - | DataRd16Burst | R | 112 bits | Burst Access to the whole channels (6 voltage and 1 temperature) |

## 7.8.1 Registers Content

## 7.8.1.1 RevID Register

Table 7-25. RevId Register Overview

| Register - Address | Register - Address | RevID - 0x00 | RevID - 0x00 | RevID - 0x00 | RevID - Reset Value | RevID - Reset Value | RevID - 0x02 |
| - | - | - | - | - | - | - | - |
| 7 (msb) | 6 | 5 | 4 | 3 | 2 | 1 | 0 (lsb) |
| x | x | x | pow_en | Mfirst |  | RevID |  |

Table 7-26. RevId Register Content

| Bit Field | Description |
| - | - |
| RevID | ATA6870N revision number, revision B: 0x02 |
| Mfirst | Status input pin MFIRST |
| pow_en | Status input pin POW_EN |

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.8.1.2 Ctrl Register

Table 7-27. Ctrl Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | Ctrl - 0x01 - 5 | Ctrl - 0x01 - 4 | Ctrl - 0x01 - 3 | Ctrl - Reset Value - 2 | Ctrl - Reset Value - 1 | Ctrl - 0x00 - 0 (lsb) |
| - | - | - | - | - | - | - | - |
| x | x | x | Chksum_ena | LFTimer_ena | TFMODE_ena | x | x |

Table 7-28. Ctrl Register Content

| Bit Field | Description |
| - | - |
| TFMode_ena | 0: Prevent ATA6870N to switch to test mode 1: Not allowed for customer use |
| LFTimer_ena | 0: Disable internal low frequency timer 1: Enable internal low frequency timer |
| Chksum_ena | 0: Disable SPI transaction checksum computation/check 1: Enable SPI transaction checksum computation/check |

## 7.8.1.3 Operation Register

Table 7-29. Operation Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | Operation - 0x02 - 5 4 | Operation - 0x02 - 3 | Operation - Reset Value - 2 1 | Operation - 0x02 - 0 (lsb) |
| - | - | - | - | - | - |
| x | x | OpMode | TempMode | VoltMode | OpRqst |

Table 7-30. Operation Register Content

| Bit Field | Description |
| - | - |
| OpRqst | 0: NoOp: No Operation, or abort current operation 1: AcqRqst: Start the analog to digital conversion An interrupt is generated when data is available in DataRd16/DataRd16Burst. |
| VoltMode | 00: Caloffset: select V(MBAT(i), MBAT(i)) as input of voltage channels. (offset calibration) 01: AcqV: select V(MBAT(i+1), MBAT(i)) as input of voltage channels (default) 10: Not allowed |
| TempMode | 0: Select TEMP1 input pin as input of temperature channel 1: Select TEMP2 input pin as input of temperature channel |
| OpMode | 00: 6 voltage channels and temperature acquisition 01: 6 voltage channels acquisition only 1X: Temperature acquisition only |

When a conversion operation is finished and the interrupt has been acknowledged by the MCU the operation register is automatically reset to "NoOp". Writing "NoOp" in the register when conversion operation is running, aborts the current operation. Other changes are not accepted during any operation.

![Image](Atmel-ATA6870N_Datasheet_files/img_006.png)

Atmel

Figure 7-28. Typical Data Acquisition Flow

![Image](Atmel-ATA6870N_Datasheet_files/img_041.png)

## 7.8.1.4 OpStatus Register

Table 7-31. OpStatus Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | OpStatus - 0x03 - 5 | OpStatus - 0x03 - 4 | OpStatus - 0x03 - 3 | OpStatus - Reset Value - 2 | OpStatus - 0x00 - 1 0 (lsb) |
| - | - | - | - | - | - | - |
| x | x | x | x | x | x | OpStatus |

Table 7-32. OpStatus Register Content

| Bit Field | Description |
| - | - |
| OpStatus | 00: No Operation 01: Operation is ongoing 10: Operation is finished, result is available 11: Operation is cancelled, result is not available |

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel The OPStatus register is reset when read after a completed or aborted operation. Reading the register before starting an operation is not mandatory. Reading data conversion results or reading the OpStatus register during an operation does not affect the OpStatus register.

Figure 7-29. Operation Status Register Management

![Image](Atmel-ATA6870N_Datasheet_files/img_042.png)

## 7.8.1.5 Rstr Register

Table 7-33. Rstr Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | Rstr - 0x04 - 5 | Rstr - 0x04 - 4 | Rstr - 0x04 - 3 | Rstr - Reset Value - 2 | Rstr - Reset Value - 1 | Rstr - 0x00 - 0 (lsb) |
| - | - | - | - | - | - | - | - |
| x | x | x | x | x | x | LFTRst | 0 |

Table 7-34. Rstr Register Content

| Bit Field | Description |
| - | - |
| LFTRst | 0: No reset 1: Low Frequency Timer software reset |

LFTRst resets and restarts the low frequency timer if not disabled (LFTimer\_ena = 0).

## 7.8.1.6 IrqMask Register

Table 7-35. IrqMask Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | IrqMask - 0x05 - 5 | IrqMask - 0x05 - 4 | IrqMask - 0x05 - 3 2 | IrqMask - Reset Value 0x00 - 1 | IrqMask - Reset Value 0x00 - 0 (lsb) |
| - | - | - | - | - | - | - |
| x | x | x | chkErrorMask | udvmask commErrorMask | LFTdoneMask | dataDryMask |

![Image](Atmel-ATA6870N_Datasheet_files/img_006.png)

Atmel

Table 7-36. IrqMask Register Content

| Bit Field | Description |
| - | - |
| dataRdyMask | Mask data ready interrupt when set to 1 |
| WakeupMask | Mask LFTdone interrupt when set to 1 |
| commErrorMask | Mask commError interrupt when set to 1 |
| udvMask | Mask undervoltage detection interrupt when set to 1 |
| chkErrorMask | Mask checksum error interrupt when set to 1 |

## 7.8.1.7 Status Register

Table 7-37. Status Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | Status - 0x06 - 5 | Status - 0x06 - 4 | Status - 0x06 - 3 | Status - Reset Value - 2 | Status - Reset Value - 1 | Status - 0x20 - 0 (lsb) |
| - | - | - | - | - | - | - | - |
| x | TFMdeOn | por | chkError | udv | commError | LFTdone | dataRdy |

Table 7-38. Status Register Content

| Bit Field | Description |
| - | - |
| dataRdy | Conversion finished |
| LFTdone | Low frequency timer elapsed |
| commError | Bad SPI command detected (wrong length) |
| udv | Undervoltage detected |
| chkError | Error on checksum check |
| Por | Power on reset detected |
| TFMdeOn | Test mode on |

Any bit among {dataRdy, LFTdone, commError, udv, chkError} set in the status register requests an interrupt to the external MCU if the corresponding mask bit in the IrqMask register is 0. Reading the status register acknowledges the interrupt and resets its content. Por and TFMdeOn cause no interrupt.

## 7.8.1.8 ChannelUdvStatus Register

Table 7-39. ChannelUdvStatus Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | ChannelUdvStatus - 0x08 - 5 | ChannelUdvStatus - 0x08 - 4 | ChannelUdvStatus - 0x08 - 3 | ChannelUdvStatus - Reset Value - 2 | ChannelUdvStatus - Reset Value - 1 | ChannelUdvStatus - 0x00 - 0 (lsb) |
| - | - | - | - | - | - | - | - |
| x | x | chUdv6_stat | chUdv5_stat | chUdv4_stat | chUdv3_stat | chUdv2_stat | chUdv1_stat |

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel Undervoltage is detected when voltage decreases under the threshold value defined in udvThresh register.

Table 7-40. ChannelUdvStatus Register Content

| Bit Field | Description |
| - | - |
| chUdv1_stat | 1: Undervoltage detected on channel 1 0: No undervoltage detected on channel 1 |
| chUdv2_stat | 1: Undervoltage detected on channel 2 0: No undervoltage detected on channel 2 |
| chUdv3_stat | 1: Undervoltage detected on channel 3 0: No undervoltage detected on channel 3 |
| chUdv4_stat | 1: Undervoltage detected on channel 4 0: No undervoltage detected on channel 4 |
| chUdv5_stat | 1: Undervoltage detected on channel 5 0: No undervoltage detected on channel 5 |
| chUdv6_stat | 1: Undervoltage detected on channel 6 0: No undervoltage detected on channel 6 |

When undervoltage is detected on a channel, the Atmel ® ATA6870N requests an interrupt if the UDVmask bit in the IRQMask register is 0.

## 7.8.1.9 ChannelDischSel Register

Table 7-41. ChannelDischSel Register Overview

| Register - Address - 7 (msb) | Register - Address - 6 | ChannelDischSel - 0x09 - 5 | ChannelDischSel - 0x09 - 4 | ChannelDischSel - 0x09 - 3 | ChannelDischSel - Reset Value - 2 | ChannelDischSel - 0x00 - 1 | ChannelDischSel - 0x00 - 0 (lsb) |
| - | - | - | - | - | - | - | - |
| x | x | chV6_disch | chV5_disch | chV4_disch | chV3_disch | chV2_disch | chV1_disch |

Table 7-42. ChannelDischSel Register Content

| Bit Field | Description |
| - | - |
| chV1_disch | 1: Enable voltage channel 1 discharge 0: Disable voltage channel 1 discharge |
| chV2_disch | 1: Enable voltage channel 2 discharge 0: Disable voltage channel 2 discharge |
| chV3_disch | 1: Enable voltage channel 3 discharge 0: Disable voltage channel 3 discharge |
| chV4_disch | 1: Enable voltage channel 4 discharge 0: Disable voltage channel 4 discharge |
| chV5_disch | 1: Enable voltage channel 5 discharge 0: Disable voltage channel 5 discharge |
| chV6_disch | 1: Enable voltage channel 6 discharge 0: Disable voltage channel 6 discharge |

The channels are dischargeable simultaneously.

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Atmel

## 7.8.1.10 ChannelReadSel Register

Table 7-43. ChannelReadSel Register Overview

| Register - Address | Register - Address | ChannelReadSel - 0x0A | ChannelReadSel - 0x0A | ChannelReadSel - 0x0A | ChannelReadSel - Reset Value | ChannelReadSel - 0x00 |
| - | - | - | - | - | - | - |
| 7 (msb) | 6 | 5 | 4 | 3 | 2 1 | 0 (lsb) |
|  |  |  |  |  | ChannelReadSel | ChannelReadSel |

Table 7-44. ChannelReadSel Register Content

| Bit Field | Description |
| - | - |
| ChannelReadSel | 111: Value of the LFT is returned in DataRd16 register 110: Temperature channel available in DataRd16 register 101: Voltage channel6, value available in DataRd16 register 100: Voltage channel5, value available in DataRd16 register 011: Voltage channel4, value available in DataRd16 register 010: Voltage channel3, value available in DataRd16 register 001: Voltage channel2, value available in DataRd16 register 000: Voltage channel1, value available in DataRd16 register |

This register can be used to quickly read a single channel without using a full burst access. The value of the selected channel will be available in the DataRd16 register. The value will always be updated by writing a channel address to the ChannelReadSel register. Data in this register is not valid during ongoing data conversion.

## 7.8.1.11 LFTimer Register

Table 7-45. LFTimer Register Overview

| Register - Address | LFTimer - Address | LFTimer - 0x0B | LFTimer - Reset Value | LFTimer - Reset Value | LFTimer - 0xF9 |
| - | - | - | - | - | - |
| 7 (msb) | 6 | 5 4 | 3 2 | 1 | 0 (lsb) |
| LFTPrescaler | LFTPrescaler | LFTDelay | LFTDelay | LFTDelay | LFTDelay |

Table 7-46. LFTimer Register Content

| Bit Field | Description |
| - | - |
| LFTDelay | Contains the present low frequency timer delay value |
| LFTPrescaler | 0: PrescalerValue = 1 1: PrescalerValue = 6 |

The default timer value is 59.965s (0xF9) for f OSC = 50kHz.

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel Formula for Delay Time calculation:

Figure 7-30. Block Diagram LFTimer

![Image](Atmel-ATA6870N_Datasheet_files/img_043.png)

<!-- formula-not-decoded -->

The LFT can be programmed to the following values (f OSC = 50kHz):

LFTprescaler = 0:

0.082s &lt;= duration &lt;= 10.486s, Increment = 82ms

LFTprescaler = 1:

492 ms &lt;= duration &lt;= 62.915s, Increment = 492ms

When LFT elapsed, an interrupt is requested unless LFTdoneMask bit is set in the IRQMask register.

For details on the tolerances for the oscillator, see Section 7.5.6 "RC Oscillator" on page 24.

Keeping at list 100 µs between two successive LFTimer register write accesses prevents internal metastability issues, which might result in bad LFTdelay decoding.

## 7.8.1.12 Test-Mode Register

Table 7-47. Test-Mode Register 1 Overview

| Register - Address - 7 (msb) | Register - Address - 6 | TESTmode1 - 0x0C - 5 | TESTmode1 - 0x0C - 4 | TESTmode1 - 0x0C - 3 | TESTmode1 - Reset Value - 2 | TESTmode1 - Reset Value - 1 | TESTmode1 - 0x03 - 0 (lsb) |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 |

Table 7-48. Test-Mode Register 2 Overview

| Register - Address - 7 (msb) | Register - Address - 6 | TESTmode2 - 0x0D - 5 | TESTmode2 - 0x0D - 4 | TESTmode2 - 0x0D - 3 | TESTmode2 - Reset Value - 2 | TESTmode2 - Reset Value - 1 | TESTmode2 - 0x07 - 0 (lsb) |
| - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 |

Table 7-49. Test-Mode Register 3 Overview

| Register - Address - 15 | Register - Address - 14 | Register - Address - 13 | Register - Address - 12 | UdvThresh - 0x12 - 11 | UdvThresh - 0x12 - 10 | UdvThresh - 0x12 - 9 | UdvThresh - 0x12 - 8 | UdvThresh - 0x12 - 7 | UdvThresh - 0x12 - 6 | UdvThresh - Reset value - 5 | UdvThresh - Reset value - 4 | UdvThresh - Reset value - 3 | UdvThresh - 0x0E00 - 2 | UdvThresh - 0x0E00 - 1 | UdvThresh - 0x0E00 - 0 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Test-mode registers 1, 2, and 3 are reserved for the factory calibration process. They are not allowed for customer use.

![Image](Atmel-ATA6870N_Datasheet_files/img_006.png)

Atmel

## 7.8.1.13 UdvThresh Register

Table 7-50. UdvThresh Register Overview

| Register - Address | Register - Address | Register - Address | Register - Address | UdvThresh - 0x10 | UdvThresh - 0x10 | UdvThresh - 0x10 | UdvThresh - 0x10 | UdvThresh - 0x10 | UdvThresh - 0x10 | UdvThresh - Reset value | UdvThresh - Reset value | UdvThresh - Reset value | UdvThresh - 0x0570 | UdvThresh - 0x0570 | UdvThresh - 0x0570 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| x | x | x | x | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh | udvThresh |

Table 7-51. UdvThresh Register Content

| Bit Field | Format | Description |
| - | - | - |
| udvThresh | 12 bits | Threshold for undervoltage detection |

Default value is 1.5V (0x0570, 1392 D )

1.5V = VREF × (1392 - 410) / (1502 - 410)

See also Section 7.5.1.2 "12 Bits Incremental ADC" on page 18.

## 7.8.1.14 DataRd16 Register

Table 7-52. DataRd16 Register Overview

| Register - Address | Register - Address | Register - Address | Register - Address | DataRd16 - 0x11 | DataRd16 - 0x11 | DataRd16 - 0x11 | DataRd16 - 0x11 | DataRd16 - 0x11 | DataRd16 - 0x11 | DataRd16 - Reset value | DataRd16 - Reset value | DataRd16 - Reset value | DataRd16 - 0x0000 | DataRd16 - 0x0000 | DataRd16 - 0x0000 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| x | x | x | x |  |  |  |  |  | DataRd16 |  |  |  |  |  |  |

Table 7-53. DataRd16 Register Content

| Bit Field | Format | Description |
| - | - | - |
| DataRd16 | 12 bits | Return selected channel value (see Section 7.8.1.10 "ChannelReadSel Register" on page 43) |

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 7.8.1.15 DataRd16burst Register

Table 7-54. DataRd16burst Register Overview

| Register - 111 | Register - Address - 110 | Register - Address - 109 | Register - Address - 108 | DataRd16Burst - 0x7F - 107 | DataRd16Burst - 0x7F - 106 | DataRd16Burst - 0x7F - 105 | DataRd16Burst - 0x7F - 104 | DataRd16Burst - 0x7F - 103 | DataRd16Burst - 0x7F - 102 | DataRd16Burst - Reset value - 101 | DataRd16Burst - Reset value - 100 | DataRd16Burst - Reset value - 99 | DataRd16Burst - 0x0000 - 98 | DataRd16Burst - 0x0000 - 97 | DataRd16Burst - 0x0000 - 96 |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| X | X | X | x | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data | Channel6 data |
| 95 | 94 | 93 | 92 | 91 | 90 | 89 | 88 | 87 | 86 | 85 | 84 | 83 | 82 | 81 | 80 |
| x | x | x | x | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data | Channel5 data |
| 79 | 78 | 77 | 76 | 75 | 74 | 73 | 72 | 71 | 70 | 69 | 68 | 67 | 66 | 65 | 64 |
| x | x | x | x | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data | Channel4 data |
| 63 | 62 | 61 | 60 | 59 | 58 | 57 | 56 | 55 | 54 | 53 | 52 | 51 | 50 | 49 | 48 |
| x | x | x | x | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data | Channel3 data |
| 47 | 46 | 45 | 44 | 43 | 42 | 41 | 40 | 39 | 38 | 37 | 36 | 35 | 34 | 33 | 32 |
| x | x | x | x | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data | Channel2 data |
| 31 | 30 | 29 | 28 | 27 | 26 | 25 | 24 | 23 | 22 | 21 | 20 | 19 | 18 | 17 | 16 |
| x | x | x | x | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data | Channel1 data |
| 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
| x | x | x | x | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data | Temperature data |

Table 7-55. DataRd16burst Register Content

| Bit Field | Format | Description |
| - | - | - |
| DataRd16burst | 112bits | Returns the values of all channels from one ATA6870N, including temperature measurement |

![Image](Atmel-ATA6870N_Datasheet_files/img_003.png)

Atmel

## Figure 7-31. Application

Figure 7-31 shows an application with 2 stacked Atmel ® ATA6870Ns.

![Image](Atmel-ATA6870N_Datasheet_files/img_044.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel

## 8. Ordering Information

| Extended Type Number | Package | MOQ |
| - | - | - |
| ATA6870N-PLPW | QFN48, 7 × 7 | 1,000 pieces |
| ATA6870N-PLQW | QFN48, 7 × 7 | 4,000 pieces |

## 9. Package Information

![Image](Atmel-ATA6870N_Datasheet_files/img_045.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_046.png)

09/07/11

| TITLE | GPC | DRAWING NO. | REV. |
| - | - | - | - |
| Package: VQFN_7x7_48L Exposed pad 5.6x5.6 |  | 6.543-5130.01-4 | 3 |

![Image](Atmel-ATA6870N_Datasheet_files/img_009.png)

Atmel

![Image](Atmel-ATA6870N_Datasheet_files/img_047.png)

specifications according to DIN technical drawings

Standard Singulation process Dimensions in mm

| COMMON DIMENSIONS (Unit of Measure = mm) - Symbol | COMMON DIMENSIONS (Unit of Measure = mm) - MIN | COMMON DIMENSIONS (Unit of Measure = mm) - NOM | COMMON DIMENSIONS (Unit of Measure = mm) - MAX | COMMON DIMENSIONS (Unit of Measure = mm) - NOTE |
| - | - | - | - | - |
| A | 0.8 | 0.9 | 1 |  |
| A1 | 0.0 | 0.02 | 0.05 |  |
| A3 | 0.15 | 0.2 | 0.25 |  |
| D | 6.9 | 7 | 7.1 |  |
| D2 | 5.45 | 5.6 | 5.75 |  |
| E | 6.9 | 7 | 7.1 |  |
| E2 | 5.45 | 5.6 | 5.75 |  |
| L | 0.3 | 0.4 | 0.5 |  |
| b | 0.16 | 0.23 | 0.3 |  |
| e |  | 0.5 BSC |  |  |

## 9.1 Markings

As a minimum, the devices will be marked with the following:

- Date code (year and week number)
- Atmel ® part number (ATA6870N)

## 10. Revision History

Please note that the following page numbers referred to in this section refer to the specific revision mentioned, not to this document.

| Revision No. | History |
| - | - |
| 9317B-AUTO-06/14 | · Put datasheet in the latest template |

![Image](Atmel-ATA6870N_Datasheet_files/img_005.png)

Atmel Atmel

![Image](Atmel-ATA6870N_Datasheet_files/img_048.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_049.png)

[X](https://www.facebook.com/AtmelCorporation)

![Image](Atmel-ATA6870N_Datasheet_files/img_050.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_051.png)

![Image](Atmel-ATA6870N_Datasheet_files/img_052.png)

[X](https://plus.google.com/117391618085377601886/posts)

![Image](Atmel-ATA6870N_Datasheet_files/img_053.png)

X X X

![Image](Atmel-ATA6870N_Datasheet_files/img_054.png)

[X](http://en.wikipedia.org/wiki/Atmel)

Atmel Corporation

1600 Technology Drive, San Jose, CA 95110 USA T: (+1)(408) 441.0311

F: (+1)(408) 436.4200

[| www.atmel.com](www.atmel.com)

© 2014 Atmel Corporation. / Rev.: Rev.: 9317B-AUTO-06/14

Atmel ® , Atmel logo and combinations thereof, Enabling Unlimited Possibilities ® , and others are registered trademarks or trademarks of Atmel Corporation in U.S. and other countries. Other terms and product names may be trademarks of others.

DISCLAIMER: The information in this document is provided in connection with Atmel products. No license, express or implied, by estoppel or otherwise, to any intellectual property right is granted by this document or in connection with the sale of Atmel products. EXCEPT AS SET FORTH IN THE ATMEL TERMS AND CONDITIONS OF SALES LOCATED ON THE ATMEL WEBSITE, ATMEL ASSUMES NO LIABILITY WHATSOEVER AND DISCLAIMS ANY EXPRESS, IMPLIED OR STATUTORY WARRANTY RELATING TO ITS PRODUCTS INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT. IN NO EVENT SHALL ATMEL BE LIABLE FOR ANY DIRECT, INDIRECT, CONSEQUENTIAL, PUNITIVE, SPECIAL OR INCIDENTAL DAMAGES (INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS AND PROFITS, BUSINESS INTERRUPTION, OR LOSS OF INFORMATION) ARISING OUT OF THE USE OR INABILITY TO USE THIS DOCUMENT, EVEN IF ATMEL HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. Atmel makes no representations or warranties with respect to the accuracy or completeness of the contents of this document and reserves the right to make changes to specifications and products descriptions at any time without notice. Atmel does not make any commitment to update the information contained herein. Unless specifically provided otherwise, Atmel products are not suitable for, and shall not be used in, automotive applications. Atmel products are not intended, authorized, or warranted for use as components in applications intended to support or sustain life.

SAFETY-CRITICAL, MILITARY, AND AUTOMOTIVE APPLICATIONS DISCLAIMER: Atmel products are not designed for and will not be used in connection with any applications where the failure of such products would reasonably be expected to result in significant personal injury or death ("Safety-Critical Applications") without an Atmel officer's specific written consent. Safety-Critical Applications include, without limitation, life support devices and systems, equipment or systems for the operation of nuclear facilities and weapons systems. Atmel products are not designed nor intended for use in military or aerospace applications or environments unless specifically designated by Atmel as military-grade. Atmel products are not designed nor intended for use in automotive applications unless specifically designated by Atmel as automotive-grade.
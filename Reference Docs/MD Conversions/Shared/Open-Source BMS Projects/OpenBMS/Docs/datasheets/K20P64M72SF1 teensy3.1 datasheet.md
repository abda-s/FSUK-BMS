<!-- Converted from K20P64M72SF1 teensy3.1 datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

## Freescale Semiconductor

Data Sheet: Technical Data

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_001.png)

## K20 Sub-Family

## Supports: MK20DX64VLH7, MK20DX128VLH7, MK20DX256VLH7

## Features

- Operating Characteristics
- Clocks
- 3 to 32 MHz crystal oscillator
- 32 kHz crystal oscillator
- Multi-purpose clock generator
- System peripherals
- Multiple low-power modes to provide power optimization based on application requirements
- 16-channel DMA controller, supporting up to 63 request sources
- External watchdog monitor
- Software watchdog
- Low-leakage wakeup unit
- Security and integrity modules
- Hardware CRC module to support fast cyclic redundancy checks
- 128-bit unique identification (ID) number per chip
- Human-machine interface
- Low-power hardware touch sensor interface (TSI)
- General-purpose input/output
- Analog modules
- Two 16-bit SAR ADCs
- Programmable gain amplifier (PGA) (up to x64) integrated into each ADC
- 12-bit DAC
- Three analog comparators (CMP) containing a 6-bit DAC and programmable reference input
- Voltage reference

- Voltage range: 1.71 to 3.6 V
- Flash write voltage range: 1.71 to 3.6 V
- Temperature range (ambient): -40 to 105°C

Document Number: K20P64M72SF1

Rev. 3, 11/2012

## K20P64M72SF1

- Timers
- Programmable delay block
- Eight-channel motor control/general purpose/PWM timer
- Two 2-channel quadrature decoder/general purpose timers
- Periodic interrupt timers
- 16-bit low-power timer
- Carrier modulator transmitter
- Real-time clock
- Communication interfaces
- USB full-/low-speed On-the-Go controller with onchip transceiver
- Controller Area Network (CAN) module
- SPI module
- Two I2C modules
- Three UART modules
- I2S module

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_002.png)

freescale

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_003.png)

## Table of Contents

| 1 Ordering parts...........................................................................3 | 1 Ordering parts...........................................................................3 | 1 Ordering parts...........................................................................3 |  |
| - | - | - | - |
| 1.1 | Determining valid orderable parts......................................3 | Determining valid orderable parts......................................3 |  |
| 2 Part | identification......................................................................3 | identification......................................................................3 |  |
| 2.1 | Description.........................................................................3 | Description.........................................................................3 |  |
| 2.2 | Format...............................................................................3 | Format...............................................................................3 |  |
| 2.3 | Fields.................................................................................3 | Fields.................................................................................3 |  |
| 2.4 | Example............................................................................4 | Example............................................................................4 |  |
| 3 Terminology and guidelines......................................................4 | 3 Terminology and guidelines......................................................4 | 3 Terminology and guidelines......................................................4 |  |
| 3.1 | Definition: Operating requirement......................................4 | Definition: Operating requirement......................................4 |  |
| 3.2 | Definition: Operating behavior...........................................5 | Definition: Operating behavior...........................................5 |  |
| 3.3 | Definition: Attribute............................................................5 | Definition: Attribute............................................................5 |  |
| 3.4 | Definition: Rating...............................................................6 | Definition: Rating...............................................................6 |  |
| 3.5 | Result of exceeding a rating..............................................6 | Result of exceeding a rating..............................................6 |  |
| 3.6 | Relationship between ratings and operating requirements......................................................................6 | Relationship between ratings and operating requirements......................................................................6 |  |
| 3.7 | Guidelines for ratings and operating requirements............7 | Guidelines for ratings and operating requirements............7 |  |
| 3.8 | Definition: Typical value.....................................................7 | Definition: Typical value.....................................................7 |  |
| 3.9 | Typical value conditions....................................................8 | Typical value conditions....................................................8 |  |
| 4 | Ratings......................................................................................9 | Ratings......................................................................................9 |  |
| 4.1 | Thermal handling ratings...................................................9 | Thermal handling ratings...................................................9 |  |
| 4.2 | Moisture handling ratings..................................................9 | Moisture handling ratings..................................................9 |  |
| 4.3 | ESD handling ratings.........................................................9 | ESD handling ratings.........................................................9 |  |
| 4.4 5 | Voltage and current operating ratings...............................9 General.....................................................................................10 | Voltage and current operating ratings...............................9 General.....................................................................................10 |  |
| 5.1 | AC electrical characteristics..............................................10 | AC electrical characteristics..............................................10 |  |
| 5.2 | Nonswitching electrical specifications...............................10 | Nonswitching electrical specifications...............................10 |  |
|  | 5.2.1 | Voltage and current operating requirements.........11 |  |
|  | 5.2.2 | LVD and POR operating requirements.................11 |  |
|  | 5.2.3 | Voltage and current operating behaviors..............12 |  |
|  | 5.2.4 | Power mode transition operating behaviors..........13 |  |
|  | 5.2.5 | Power consumption operating behaviors..............14 |  |
|  | 5.2.6 | Designing with radiated emissions in mind...........18 |  |
|  | 5.2.7 | Capacitance attributes..........................................18 |  |
| 5.3 | Switching | specifications.....................................................19 |  |
|  | 5.3.1 | Device clock specifications...................................19 |  |
|  | 5.3.2 General | switching | specifications...........................19 |
| 5.4 | Thermal | specifications.......................................................20 |  |
|  | 5.4.1 Thermal | operating | requirements...........................20 |
|  | 5.4.2 | Thermal attributes.................................................21 |  |

6 Peripheral operating requirements and behaviors....................21

6.1 Core modules....................................................................22

6.1.1 Debug trace timing specifications.........................22

6.1.2 JTAG electricals....................................................22

6.2 System modules................................................................25

6.3 Clock modules...................................................................25

6.3.1 MCG specifications...............................................25

6.3.2 Oscillator electrical specifications.........................27

6.3.3 32 kHz Oscillator Electrical Characteristics...........30

6.4 Memories and memory interfaces.....................................30

6.4.1 Flash electrical specifications................................30

6.4.2 EzPort Switching Specifications............................35

6.5 Security and integrity modules..........................................36

6.6 Analog...............................................................................36

6.6.1 ADC electrical specifications.................................36

6.6.2 CMP and 6-bit DAC electrical specifications.........43

6.6.3 12-bit DAC electrical characteristics.....................46

6.6.4 Voltage reference electrical specifications............49

6.7 Timers................................................................................50

6.8 Communication interfaces.................................................50

6.8.1 USB electrical specifications.................................50

6.8.2 USB DCD electrical specifications........................51

6.8.3 USB VREG electrical specifications......................51

6.8.4 CAN switching specifications................................52

6.8.5 DSPI switching specifications (limited voltage

range)....................................................................52

6.8.6 DSPI switching specifications (full voltage range).53

6.8.7 I2C switching specifications..................................55

6.8.8 UART switching specifications..............................55

6.8.9 I2S/SAI Switching Specifications..........................55

6.9 Human-machine interfaces (HMI)......................................60

6.9.1 TSI electrical specifications...................................60

7 Dimensions...............................................................................61

7.1 Obtaining package dimensions.........................................61

8 Pinout........................................................................................61

8.1 K20 Signal Multiplexing and Pin Assignments..................61

8.2 K20 Pinouts.......................................................................64

9 Revision History........................................................................65

## 1 Ordering parts

## 1.1 Determining valid orderable parts

Valid orderable part numbers are provided on the web. To determine the orderable part numbers for this device, go to www.freescale.com and perform a part number search for the following device numbers: PK20 and MK20 .

## 2 Part identification

## 2.1 Description

Part numbers for the chip have fields that identify the specific part. You can use the values of these fields to determine the specific part you have received.

## 2.2 Format

Part numbers for this device have the following format:

Q K## A M FFF R T PP CC N

## 2.3 Fields

This table lists the possible values for each field in the part number (not all combinations are valid):

Table continues on the next page...

| Field | Description | Values |
| - | - | - |
| Q | Qualification status | · M = Fully qualified, general market flow · P = Prequalification |
| K## | Kinetis family | · K20 |
| A | Key attribute | · D = Cortex-M4 w/ DSP · F = Cortex-M4 w/ DSP and FPU |
| M | Flash memory type | · N = Program flash only · X = Program flash and FlexMemory |

| Field | Description | Values |
| - | - | - |
| FFF | Program flash memory size | · 32 = 32 KB · 64 = 64 KB · 128 = 128 KB · 256 = 256 KB · 512 = 512 KB · 1M0 = 1 MB |
| R | Silicon revision | · Z = Initial · (Blank) = Main · A = Revision after main |
| T | Temperature range (°C) | · V = -40 to 105 · C = -40 to 85 |
| PP | Package identifier | · FM = 32 QFN (5 mm x 5 mm) · FT = 48 QFN (7 mm x 7 mm) · LF = 48 LQFP (7 mm x 7 mm) · LH = 64 LQFP (10 mm x 10 mm) · MP = 64 MAPBGA (5 mm x 5 mm) · LK = 80 LQFP (12 mm x 12 mm) · LL = 100 LQFP (14 mm x 14 mm) · MC = 121 MAPBGA (8 mm x 8 mm) · LQ = 144 LQFP (20 mm x 20 mm) · MD = 144 MAPBGA (13 mm x 13 mm) · MJ = 256 MAPBGA (17 mm x 17 mm) |
| CC | Maximum CPU frequency (MHz) | · 5 = 50 MHz · 7 = 72 MHz · 10 = 100 MHz · 12 = 120 MHz · 15 = 150 MHz |
| N | Packaging type | · R = Tape and reel · (Blank) = Trays |

## 2.4 Example

This is an example part number:

MK20DN512ZVMD10

## 3 Terminology and guidelines

## 3.1 Definition: Operating requirement

An operating requirement is a specified value or range of values for a technical characteristic that you must guarantee during operation to avoid incorrect operation and possibly decreasing the useful life of the chip.

## 3.1.1 Example

This is an example of an operating requirement, which you must meet for the accompanying operating behaviors to be guaranteed:

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| VDD | 1.0 V core supply voltage | 0.9 | 1.1 | V |

## 3.2 Definition: Operating behavior

An operating behavior is a specified value or range of values for a technical characteristic that are guaranteed during operation if you meet the operating requirements and any other specified conditions.

## 3.2.1 Example

This is an example of an operating behavior, which is guaranteed if you meet the accompanying operating requirements:

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| IWP | Digital I/O weak pullup/ pulldown current | 10 | 130 | µA |

## 3.3 Definition: Attribute

An attribute is a specified value or range of values for a technical characteristic that are guaranteed, regardless of whether you meet the operating requirements.

## 3.3.1 Example

This is an example of an attribute:

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| CIN_D | Input capacitance: digital pins | - | 7 | pF |

## 3.4 Definition: Rating

A rating is a minimum or maximum value of a technical characteristic that, if exceeded, may cause permanent chip failure:

- Operating ratings apply during operation of the chip.
- Handling ratings apply when the chip is not powered.

## 3.4.1 Example

This is an example of an operating rating:

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| VDD | 1.0 V core supply voltage | -0.3 | 1.2 | V |

## 3.5 Result of exceeding a rating

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_004.png)

Terminology and guidelines

## 3.6 Relationship between ratings and operating requirements

Handling (power off)

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_005.png)

## 3.7 Guidelines for ratings and operating requirements

Follow these guidelines for ratings and operating requirements:

- Never exceed any of the chip's ratings.
- During normal operation, don't exceed any of the chip's operating requirements.
- If you must exceed an operating requirement at times other than during normal operation (for example, during power sequencing), limit the duration as much as possible.

## 3.8 Definition: Typical value

A typical value is a specified value for a technical characteristic that:

- Lies within the range of values specified by the operating behavior
- Given the typical manufacturing process, is representative of that characteristic during operation when you meet the typical-value conditions or other specified conditions

Typical values are provided as design guidelines and are neither tested nor guaranteed.

## 3.8.1 Example 1

This is an example of an operating behavior that includes a typical value:

| Symbol | Description | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - |
| IWP | Digital I/O weak pullup/pulldown current | 10 | 70 | 130 | µA |

## 3.8.2 Example 2

This is an example of a chart that shows typical values for various voltage and temperature conditions:

■

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_006.png)

## 3.9 Typical value conditions

Typical values assume you meet the following conditions (or other conditions as specified):

| Symbol | Description | Value | Unit |
| - | - | - | - |
| TA | Ambient temperature | 25 | °C |
| VDD | 3.3 V supply voltage | 3.3 | V |

## 4 Ratings

## 4.1 Thermal handling ratings

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| TSTG | Storage temperature | -55 | 150 | °C | 1 |
| TSDR | Solder temperature, lead-free | - | 260 | °C | 2 |

1. Determined according to JEDEC Standard JESD22-A103, High Temperature Storage Life.

2. Determined according to IPC/JEDEC Standard J-STD-020, Moisture/Reflow Sensitivity Classification for Nonhermetic Solid State Surface Mount Devices.

## 4.2 Moisture handling ratings

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| MSL | Moisture sensitivity level | - | 3 | - | 1 |

1. Determined according to IPC/JEDEC Standard J-STD-020, Moisture/Reflow Sensitivity Classification for Nonhermetic Solid State Surface Mount Devices.

## 4.3 ESD handling ratings

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| VHBM | Electrostatic discharge voltage, human body model | -2000 | +2000 | V | 1 |
| VCDM | Electrostatic discharge voltage, charged-device model | -500 | +500 | V | 2 |
| ILAT | Latch-up current at ambient temperature of 105°C | -100 | +100 | mA |  |

1. Determined according to JEDEC Standard JESD22-A114, Electrostatic Discharge (ESD) Sensitivity Testing Human Body Model (HBM).

2. Determined according to JEDEC Standard JESD22-C101, Field-Induced Charged-Device Model Test Method for Electrostatic-Discharge-Withstand Thresholds of Microelectronic Components.

## 4.4 Voltage and current operating ratings

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| VDD | Digital supply voltage | -0.3 | 3.8 | V |

Table continues on the next page...

## General

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| IDD | Digital supply current | - | 185 | mA |
| VDIO | Digital input voltage (except RESET, EXTAL, and XTAL) | -0.3 | 5.5 | V |
| VAIO | Analog 1 , RESET, EXTAL, and XTAL input voltage | -0.3 | VDD + 0.3 | V |
| ID | Maximum current single pin limit (applies to all digital pins) | -25 | 25 | mA |
| VDDA | Analog supply voltage | VDD - 0.3 | VDD + 0.3 | V |
| VUSB_DP | USB_DP input voltage | -0.3 | 3.63 | V |
| VUSB_DM | USB_DM input voltage | -0.3 | 3.63 | V |
| VREGIN | USB regulator input | -0.3 | 6.0 | V |
| VBAT | RTC battery supply voltage | -0.3 | 3.8 | V |

1. Analog pins are defined as pins that do not have an associated general purpose I/O port function.

## 5 General

## 5.1 AC electrical characteristics

Unless otherwise specified, propagation delays are measured from the 50% to the 50% point, and rise and fall times are measured at the 20% and 80% points, as shown in the following figure.

Figure 1. Input signal measurement reference

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_007.png)

All digital I/O switching characteristics assume:

1. output pins
- have CL=30pF loads,
- are configured for fast slew rate (PORTx\_PCRn[SRE]=0), and
- are configured for high drive strength (PORTx\_PCRn[DSE]=1)
2. input pins
- have their passive filter disabled (PORTx\_PCRn[PFE]=0)

## 5.2 Nonswitching electrical specifications

## 5.2.1 Voltage and current operating requirements

Table 1. Voltage and current operating requirements

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| VDD | Supply voltage | 1.71 | 3.6 | V |  |
| VDDA | Analog supply voltage | 1.71 | 3.6 | V |  |
| VDD - VDDA | VDD-to-VDDA differential voltage | -0.1 | 0.1 | V |  |
| VSS - VSSA | VSS-to-VSSA differential voltage | -0.1 | 0.1 | V |  |
| VBAT | RTC battery supply voltage | 1.71 | 3.6 | V |  |
| VIH | Input high voltage · 2.7 V ≤ VDD ≤ 3.6 V · 1.7 V ≤ VDD ≤ 2.7 V | 0.7 × VDD 0.75 × VDD | - - | V V |  |
| VIL | Input low voltage · 2.7 V ≤ VDD ≤ 3.6 V · 1.7 V ≤ VDD ≤ 2.7 V | - - | 0.35 × VDD 0.3 × VDD | V V |  |
| VHYS | Input hysteresis | 0.06 × VDD | - | V |  |
| IICDIO | Digital pin negative DC injection current - single pin · VIN < VSS-0.3V | -5 | - | mA | 1 |
| IICAIO | Analog 2 , EXTAL, and XTAL pin DC injection current - single pin · VIN < VSS-0.3V (Negative current injection) · VIN > VDD+0.3V (Positive current injection) | -5 - | - +5 | mA | 3 |
| IICcont | Contiguous pin DC injection current -regional limit, includes sum of negative injection currents or sum of positive injection currents of 16 contiguous pins · Negative current injection · Positive current injection | -25 - | - +25 | mA |  |
| VRAM | VDD voltage required to retain RAM | 1.2 | - | V |  |
| VRFVBAT | VBAT voltage required to retain the VBAT register file | VPOR_VBAT | - | V |  |

1. All 5 V tolerant digital I/O pins are internally clamped to VSS through a ESD protection diode. There is no diode connection to VDD. If VIN greater than VDIO\_MIN (=VSS-0.3V) is observed, then there is no need to provide current limiting resistors at the pads. If this limit cannot be observed then a current limiting resistor is required. The negative DC injection current limiting resistor is calculated as R=(VDIO\_MIN-VIN)/|IIC|.
2. Analog pins are defined as pins that do not have an associated general purpose I/O port function.
3. All analog pins are internally clamped to VSS and VDD through ESD protection diodes. If VIN is greater than VAIO\_MIN (=VSS-0.3V) and VIN is less than VAIO\_MAX(=VDD+0.3V) is observed, then there is no need to provide current limiting resistors at the pads. If these limits cannot be observed then a current limiting resistor is required. The negative DC injection current limiting resistor is calculated as R=(VAIO\_MIN-VIN)/|IIC|. The positive injection current limiting resistor is calculated as R=(VIN-VAIO\_MAX)/|IIC|. Select the larger of these two calculated resistances.

## 5.2.2 LVD and POR operating requirements

## Table 2. VDD supply LVD and POR operating requirements

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| VPOR | Falling VDD POR detect voltage | 0.8 | 1.1 | 1.5 | V |  |
| VLVDH | Falling low-voltage detect threshold - high range (LVDV=01) | 2.48 | 2.56 | 2.64 | V |  |
| VLVW1H VLVW2H VLVW3H | Low-voltage warning thresholds - high range · Level 1 falling (LVWV=00) · Level 2 falling (LVWV=01) · Level 3 falling (LVWV=10) · Level 4 falling (LVWV=11) | 2.62 2.72 2.82 2.92 | 2.70 2.80 2.90 3.00 ±80 | 2.78 2.88 2.98 3.08 - 1.66 | V V V V | 1 |
| VLVW4H |  |  |  |  |  |  |
| VHYSH | Low-voltage inhibit reset/recover hysteresis - high range | - |  |  | mV |  |
| VLVDL | Falling low-voltage detect threshold - low range (LVDV=00) | 1.54 | 1.60 |  | V |  |
| VLVW1L VLVW2L VLVW3L | Low-voltage warning thresholds - low range · Level 1 falling (LVWV=00) · Level 2 falling (LVWV=01) | 1.74 | 1.80 1.90 | 1.86 1.96 | V | 1 |
|  |  | 1.84 |  |  | V |  |
|  | · Level 3 falling (LVWV=10) | 1.94 | 2.00 | 2.06 | V |  |
| VLVW4L | · Level 4 falling (LVWV=11) | 2.04 | 2.10 | 2.16 | V |  |
| VHYSL | Low-voltage inhibit reset/recover hysteresis - low range | - | ±60 | - | mV |  |
| VBG | Bandgap voltage reference | 0.97 | 1.00 | 1.03 | V |  |
| tLPO | Internal low power oscillator period - factory trimmed | 900 | 1000 | 1100 | μs |  |

1. Rising thresholds are falling threshold + hysteresis voltage

## Table 3. VBAT power operating requirements

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| VPOR_VBAT | Falling VBAT supply POR detect voltage | 0.8 | 1.1 | 1.5 | V |  |

## 5.2.3 Voltage and current operating behaviors

## Table 4. Voltage and current operating behaviors

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| VOH | Output high voltage - high drive strength · 2.7 V ≤ VDD ≤ 3.6 V, IOH = -9mA · 1.71 V ≤ VDD ≤ 2.7 V, IOH = -3mA | VDD - 0.5 VDD - 0.5 | - - | V V |  |
| VOH | Output high voltage - low drive strength · 2.7 V ≤ VDD ≤ 3.6 V, IOH = -2mA · 1.71 V ≤ VDD ≤ 2.7 V, IOH = -0.6mA | VDD - 0.5 VDD - 0.5 | - - | V V |  |
| IOHT | Output high current total for all ports | - | 100 | mA |  |
| VOL | Output low voltage - high drive strength · 2.7 V ≤ VDD ≤ 3.6 V, IOL = 9mA · 1.71 V ≤ VDD ≤ 2.7 V, IOL = 3mA | - - | 0.5 0.5 | V V |  |
| VOL | Output low voltage - low drive strength · 2.7 V ≤ VDD ≤ 3.6 V, IOL = 2mA · 1.71 V ≤ VDD ≤ 2.7 V, IOL = 0.6mA | - - | 0.5 0.5 | V V |  |
| IOLT | Output low current total for all ports | - | 100 | mA |  |
| IIN | Input leakage current (per pin) for full temperature range | - | 1 | μA | 1 |
| IIN | Input leakage current (per pin) at 25°C | - | 0.025 | μA | 1 |
| IOZ | Hi-Z (off-state) leakage current (per pin) | - | 1 | μA |  |
| RPU | Internal pullup resistors | 20 | 50 | kΩ | 2 |
| RPD | Internal pulldown resistors | 20 | 50 | kΩ | 3 |

1. Measured at VDD=3.6V

2. Measured at VDD supply voltage = VDD min and Vinput = VSS
3. Measured at VDD supply voltage = VDD min and Vinput = VDD

## 5.2.4 Power mode transition operating behaviors

All specifications except tPOR, and VLLSx→RUN recovery times in the following table assume this clock configuration:

- CPU and system clocks = 72 MHz
- Bus clock = 36 MHz
- Flash clock = 24 MHz

Table 5. Power mode transition operating behaviors

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| tPOR | After a POR event, amount of time from the point VDD reaches 1.71 V to execution of the first instruction across the operating temperature range of the chip. | - | 300 | μs | 1 |
|  | · VLLS1 → RUN | - | 112 | μs |  |
|  | · VLLS2 → RUN | - | 74 | μs |  |
|  | · VLLS3 → RUN | - | 73 | μs |  |
|  | · LLS → RUN | - | 5.9 | μs |  |
|  | · VLPS → RUN | - | 5.8 | μs |  |
|  | · STOP → RUN | - | 4.2 | μs |  |

1. Normal boot (FTFL\_OPT[LPBOOT]=1)

## 5.2.5 Power consumption operating behaviors

Table 6. Power consumption operating behaviors

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| IDDA | Analog supply current | - | - | See note | mA | 1 |
| IDD_RUN | Run mode current - all peripheral clocks disabled, code executing from flash · @ 1.8V · @ 3.0V | - - | 21.5 21.5 | 25 30 | mA mA | 2 |
| IDD_RUN | Run mode current - all peripheral clocks enabled, code executing from flash · @ 1.8V · @ 3.0V · @ 25°C · @ 125°C | - - - | 31 31 32 | 34 34 39 | mA mA mA | 3, 4 |
| IDD_WAIT | Wait mode high frequency current at 3.0 V - all peripheral clocks disabled | - | 12.5 | - | mA | 2 |
| IDD_WAIT | Wait mode reduced frequency current at 3.0 V - all peripheral clocks disabled | - | 7.2 | - | mA | 5 |
| IDD_VLPR | Very-low-power run mode current at 3.0 V - all peripheral clocks disabled | - | 0.996 | - | mA | 6 |
| IDD_VLPR | Very-low-power run mode current at 3.0 V - all peripheral clocks enabled | - | 1.46 | - | mA | 7 |

Table continues on the next page...

## General

Table 6. Power consumption operating behaviors (continued)

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| IDD_VLPW | Very-low-power wait mode current at 3.0 V - all peripheral clocks disabled | - | 0.61 | - | mA | 8 |
| IDD_STOP | Stop mode current at 3.0 V |  |  |  |  |  |
|  | · @ -40 to 25°C | - | 0.35 | 0.567 | mA |  |
|  | · @ 70°C | - | 0.384 | 0.793 | mA |  |
|  | · @ 105°C | - | 0.628 | 1.2 | mA |  |
| IDD_VLPS | Very-low-power stop mode current at 3.0 V |  |  |  |  |  |
|  | · @ -40 to 25°C | - | 5.9 | 32.7 | μA |  |
|  | · @ 70°C | - | 26.1 | 59.8 | μA |  |
|  | · @ 105°C | - | 98.1 | 188 | μA |  |
| IDD_LLS | Low leakage stop mode current at 3.0 V |  |  |  |  | 9 |
|  | · @ -40 to 25°C | - | 2.6 | 8.6 | μA |  |
|  | · @ 70°C | - | 10.3 | 29.1 | μA |  |
|  | · @ 105°C | - | 42.5 | 92.5 | μA |  |
| IDD_VLLS3 | Very low-leakage stop mode 3 current at 3.0 V |  |  |  |  | 9 |
|  | · @ -40 to 25°C | - | 1.9 | 5.8 | μA |  |
|  | · @ 70°C | - | 6.9 | 12.1 | μA |  |
|  | · @ 105°C | - | 28.1 | 41.9 | μA |  |
| IDD_VLLS2 | Very low-leakage stop mode 2 current at 3.0 V |  |  |  |  |  |
|  | · @ -40 to 25°C | - | 1.59 | 5.5 | μA |  |
|  | · @ 70°C | - | 4.3 | 9.5 | μA |  |
|  | · @ 105°C | - | 17.5 | 34 | μA |  |
| IDD_VLLS1 | Very low-leakage stop mode 1 current at 3.0 V |  |  |  |  |  |
|  | · @ -40 to 25°C | - | 1.47 | 5.4 | μA |  |
|  | · @ 70°C | - | 2.97 | 8.1 | μA |  |
|  | · @ 105°C | - | 12.41 | 32 | μA |  |
| IDD_VBAT | Average current with RTC and 32kHz disabled at 3.0 V |  |  |  |  |  |
|  | · @ -40 to 25°C | - | 0.19 | 0.22 | μA |  |
|  | · @ 70°C | - | 0.49 | 0.64 | μA |  |
|  | · @ 105°C | - | 2.2 | 3.2 | μA |  |

Table continues on the next page...

## General

Table 6. Power consumption operating behaviors (continued)

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| IDD_VBAT | Average current when CPU is not accessing RTC registers · @ 1.8V · @ -40 to 25°C · @ 70°C · @ 105°C · @ 3.0V · @ -40 to 25°C · @ 70°C · @ 105°C | - - - - - - | 0.57 0.90 2.4 0.67 1.0 2.7 | 0.67 1.2 3.5 0.94 1.4 3.9 | μA μA μA μA μA μA | 10 |

1. The analog supply current is the sum of the active or disabled current for each of the analog modules on the device. See each module's specification for its supply current.
2. 72MHz core and system clock, 36MHz bus clock, and 24MHz flash clock. MCG configured for FEE mode. All peripheral clocks disabled.
3. 72MHz core and system clock, 36MHz bus clock, and 24MHz flash clock. MCG configured for FEE mode. All peripheral clocks enabled.
4. Max values are measured with CPU executing DSP instructions.
5. 25MHz core, system, bus and flash clock. MCG configured for FEI mode.
6. 4 MHz core and system clock, 4 MHz and bus clock, and 1 MHz flash clock. MCG configured for BLPE mode. All peripheral clocks disabled. Code executing from flash.
7. 4 MHz core and system clock, 4 MHz and bus clock, and 1 MHz flash clock. MCG configured for BLPE mode. All peripheral clocks enabled but peripherals are not in active operation. Code executing from flash.
8. 4 MHz core and system clock, 4 MHz and bus clock, and 1 MHz flash clock. MCG configured for BLPE mode. All peripheral clocks disabled.
9. Data reflects devices with 128 KB of RAM. For devices with 64 KB of RAM, power consumption is reduced by 2 μA.
10. Includes 32kHz oscillator current and RTC operation.

## 5.2.5.1 Diagram: Typical IDD\_RUN operating behavior

The following data was measured under these conditions:

- MCG in FBE mode for 50 MHz and lower frequencies. MCG in FEE mode at greater than 50 MHz frequencies.
- USB regulator disabled
- No GPIOs toggled
- Code execution from flash with cache enabled
- For the ALLOFF curve, all peripheral clocks are disabled except FTFL

Figure 2. Run mode supply current vs. core frequency

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_008.png)

Figure 3. VLPR mode supply current vs. core frequency

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_009.png)

## 5.2.6 Designing with radiated emissions in mind

To find application notes that provide guidance on designing your system to minimize interference from radiated emissions:

1. [Go to www.freescale.com.](http://www.freescale.com/)
2. Perform a keyword search for "EMC design."

## 5.2.7 Capacitance attributes

Table 7. Capacitance attributes

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| CIN_A | Input capacitance: analog pins | - | 7 | pF |
| CIN_D | Input capacitance: digital pins | - | 7 | pF |

## 5.3 Switching specifications

## 5.3.1 Device clock specifications

Table 8. Device clock specifications

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| Normal run mode | Normal run mode | Normal run mode | Normal run mode | Normal run mode | Normal run mode |
| fSYS | System and core clock | - | 72 | MHz |  |
| fSYS_USB | System and core clock when Full Speed USB in operation | 20 | - | MHz |  |
| fBUS | Bus clock | - | 50 | MHz |  |
| fFLASH | Flash clock | - | 25 | MHz |  |
| fLPTMR | LPTMR clock | - | 25 | MHz |  |
| VLPR mode 1 | VLPR mode 1 | VLPR mode 1 | VLPR mode 1 | VLPR mode 1 | VLPR mode 1 |
| fSYS | System and core clock | - | 4 | MHz |  |
| fBUS | Bus clock | - | 4 | MHz |  |
| fFLASH | Flash clock | - | 0.5 | MHz |  |
| fERCLK | External reference clock | - | 16 | MHz |  |
| fLPTMR_pin | LPTMR clock | - | 25 | MHz |  |
| fLPTMR_ERCLK | LPTMR external reference clock | - | 16 | MHz |  |
| fFlexCAN_ERCLK | FlexCAN external reference clock | - | 8 | MHz |  |
| fI2S_MCLK | I2S master clock | - | 12.5 | MHz |  |
| fI2S_BCLK | I2S bit clock | - | 4 | MHz |  |

1. The frequency limitations in VLPR mode here override any frequency specification listed in the timing specification for any other module.

## 5.3.2 General switching specifications

These general purpose specifications apply to all signals configured for GPIO, UART, CAN, CMT, and I 2 C signals.

Table 9. General switching specifications

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
|  | GPIO pin interrupt pulse width (digital glitch filter disabled) - Synchronous path | 1.5 | - | Bus clock cycles | 1, 2 |
|  | GPIO pin interrupt pulse width (digital glitch filter disabled, analog filter enabled) - Asynchronous path | 100 | - | ns | 3 |

Table continues on the next page...

## Table 9. General switching specifications (continued)

| Symbol Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - |
| GPIO pin interrupt pulse width (digital glitch filter disabled, analog filter disabled) - Asynchronous path | 16 | - | ns | 3 |
| External reset pulse width (digital glitch filter disabled) | 100 | - | ns | 3 |
| Mode select (EZP_CS) hold time after reset deassertion | 2 | - | Bus clock cycles |  |
| Port rise and fall time (high drive strength) · Slew disabled · 1.71 ≤ VDD ≤ 2.7V · 2.7 ≤ VDD ≤ 3.6V · Slew enabled · 1.71 ≤ VDD ≤ 2.7V · 2.7 ≤ VDD ≤ 3.6V | - - - - | 12 6 36 24 | ns ns ns ns | 4 |
| Port rise and fall time (low drive strength) · Slew disabled · 1.71 ≤ VDD ≤ 2.7V · 2.7 ≤ VDD ≤ 3.6V · Slew enabled · 1.71 ≤ VDD ≤ 2.7V · 2.7 ≤ VDD ≤ 3.6V | - - - - | 12 6 36 24 | ns ns ns ns | 5 |

1. This is the minimum pulse width that is guaranteed to pass through the pin synchronization circuitry. Shorter pulses may or may not be recognized. In Stop, VLPS, LLS, and VLLSx modes, the synchronizer is bypassed so shorter pulses can be recognized in that case.
2. The greater synchronous and asynchronous timing must be met.
3. This is the minimum pulse width that is guaranteed to be recognized as a pin interrupt request in Stop, VLPS, LLS, and VLLSx modes.
4. 75pF load
5. 15pF load

## 5.4 Thermal specifications

## 5.4.1 Thermal operating requirements

## Table 10. Thermal operating requirements

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| TJ | Die junction temperature | -40 | 125 | °C |
| TA | Ambient temperature | -40 | 105 | °C |

## 5.4.2 Thermal attributes

| Board type | Symbol | Description | 64 LQFP | Unit | Notes |
| - | - | - | - | - | - |
| Single-layer (1s) | RθJA | Thermal resistance, junction to ambient (natural convection) | 59 | °C/W | 1, 2 |
| Four-layer (2s2p) | RθJA | Thermal resistance, junction to ambient (natural convection) | 41 | °C/W | 1, 3 |
| Single-layer (1s) | RθJMA | Thermal resistance, junction to ambient (200 ft./ min. air speed) | 48 | °C/W | 1,3 |
| Four-layer (2s2p) | RθJMA | Thermal resistance, junction to ambient (200 ft./ min. air speed) | 35 | °C/W | 1,3 |
| - | RθJB | Thermal resistance, junction to board | 23 | °C/W | 4 |
| - | RθJC | Thermal resistance, junction to case | 11 | °C/W | 5 |
| - | ΨJT | Thermal characterization parameter, junction to package top outside center (natural convection) | 3 | °C/W | 6 |

1. Junction temperature is a function of die size, on-chip power dissipation, package thermal resistance, mounting site (board) temperature, ambient temperature, air flow, power dissipation of other components on the board, and board thermal resistance.
2. Determined according to JEDEC Standard JESD51-2, Integrated Circuits Thermal Test Method Environmental Conditions-Natural Convection (Still Air) with the single layer board horizontal. For the LQFP, the board meets the JESD51-3 specification. For the MAPBGA, the board meets the JESD51-9 specification.
3. Determined according to JEDEC Standard JESD51-6, Integrated Circuits Thermal Test Method Environmental Conditions-Forced Convection (Moving Air) with the board horizontal. For the LQFP, the board meets the JESD51-7 specification.
4. Determined according to JEDEC Standard JESD51-8, Integrated Circuit Thermal Test Method Environmental
5. Conditions-Junction-to-Board. Board temperature is measured on the top surface of the board near the package.
5. Determined according to Method 1012.1 of MIL-STD 883, Test Method Standard, Microcircuits, with the cold plate temperature used for the case temperature. The value includes the thermal resistance of the interface material between the top of the package and the cold plate.
6. Determined according to JEDEC Standard JESD51-2, Integrated Circuits Thermal Test Method Environmental Conditions-Natural Convection (Still Air).

## 6 Peripheral operating requirements and behaviors

## 6.1 Core modules

## 6.1.1 Debug trace timing specifications

Table 11. Debug trace operating behaviors

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| Tcyc | Clock period | Frequency dependent | Frequency dependent | MHz |
| Twl | Low pulse width | 2 | - | ns |
| Twh | High pulse width | 2 | - | ns |
| Tr | Clock and data rise time | - | 3 | ns |
| Tf | Clock and data fall time | - | 3 | ns |
| Ts | Data setup | 3 | - | ns |
| Th | Data hold | 2 | - | ns |

Figure 4. TRACE\_CLKOUT specifications

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_010.png)

Figure 5. Trace data specifications

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_011.png)

## 6.1.2 JTAG electricals

Table 12. JTAG limited voltage range electricals

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 2.7 | 3.6 | V |

Table continues on the next page...

Table 12. JTAG limited voltage range electricals (continued)

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| J1 | TCLK frequency of operation · Boundary Scan · JTAG and CJTAG · Serial Wire Debug | 0 0 0 | 10 25 50 | MHz |
| J2 | TCLK cycle period | 1/J1 | - | ns |
| J3 | TCLK clock pulse width · Boundary Scan · JTAG and CJTAG · Serial Wire Debug | 50 20 10 | - - - | ns ns ns |
| J4 | TCLK rise and fall times | - | 3 | ns |
| J5 | Boundary scan input data setup time to TCLK rise | 20 | - | ns |
| J6 | Boundary scan input data hold time after TCLK rise | 0 | - | ns |
| J7 | TCLK low to boundary scan output data valid | - | 25 | ns |
| J8 | TCLK low to boundary scan output high-Z | - | 25 | ns |
| J9 | TMS, TDI input data setup time to TCLK rise | 8 | - | ns |
| J10 | TMS, TDI input data hold time after TCLK rise | 1 | - | ns |
| J11 | TCLK low to TDO data valid | - | 17 | ns |
| J12 | TCLK low to TDO high-Z | - | 17 | ns |
| J13 | TRST assert time | 100 | - | ns |
| J14 | TRST setup time (negation) to TCLK high | 8 | - | ns |

Table 13. JTAG full voltage range electricals

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V |
| J1 | TCLK frequency of operation · Boundary Scan · JTAG and CJTAG · Serial Wire Debug |  |  | MHz |
|  |  | 0 | 10 |  |
|  |  | 0 | 20 |  |
|  |  | 0 | 40 |  |
| J2 | TCLK cycle period | 1/J1 | - | ns |
| J3 | TCLK clock pulse width |  |  |  |
|  | · Boundary Scan | 50 | - | ns |
|  | · JTAG and CJTAG | 25 | - | ns |
|  | · Serial Wire Debug | 12.5 | - | ns |
| J4 | TCLK rise and fall times | - | 3 | ns |
| J5 | Boundary scan input data setup time to TCLK rise | 20 | - | ns |
| J6 | Boundary scan input data hold time after TCLK rise | 0 | - | ns |

Table continues on the next page...

Table 13. JTAG full voltage range electricals (continued)

| Symbol | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| J7 | TCLK low to boundary scan output data valid | - | 25 | ns |
| J8 | TCLK low to boundary scan output high-Z | - | 25 | ns |
| J9 | TMS, TDI input data setup time to TCLK rise | 8 | - | ns |
| J10 | TMS, TDI input data hold time after TCLK rise | 1.4 | - | ns |
| J11 | TCLK low to TDO data valid | - | 22.1 | ns |
| J12 | TCLK low to TDO high-Z | - | 22.1 | ns |
| J13 | TRST assert time | 100 | - | ns |
| J14 | TRST setup time (negation) to TCLK high | 8 | - | ns |

Figure 6. Test clock input timing

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_012.png)

Figure 7. Boundary scan (JTAG) timing

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_013.png)

Figure 8. Test Access Port timing

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_014.png)

Figure 9. TRST timing

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_015.png)

## 6.2 System modules

There are no specifications necessary for the device's system modules.

## 6.3 Clock modules

## 6.3.1 MCG specifications

## Table 14. MCG specifications

| Symbol | Description | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - | - |
| fints_ft | Internal reference frequency (slow clock) - factory trimmed at nominal VDD and 25 °C | Internal reference frequency (slow clock) - factory trimmed at nominal VDD and 25 °C | - | 32.768 | - | kHz |  |
| fints_t | Internal reference frequency (slow clock) - user trimmed | Internal reference frequency (slow clock) - user trimmed | 31.25 | - | 39.0625 | kHz |  |
| Δfdco_res_t | Resolution of trimmed average DCO output frequency at fixed voltage and temperature - using SCTRIM and SCFTRIM | Resolution of trimmed average DCO output frequency at fixed voltage and temperature - using SCTRIM and SCFTRIM | - | ± 0.3 | ± 0.6 | %fdco | 1 |
| Δfdco_res_t | Resolution of trimmed average DCO output frequency at fixed voltage and temperature - using SCTRIM only | Resolution of trimmed average DCO output frequency at fixed voltage and temperature - using SCTRIM only | - | ± 0.2 | ± 0.5 | %fdco | 1 |
| Δfdco_t | Total deviation of trimmed average DCO output frequency over voltage and temperature | Total deviation of trimmed average DCO output frequency over voltage and temperature | - | +0.5/-0.7 | - | %fdco | 1 |
| Δfdco_t | Total deviation of trimmed average DCO output frequency over fixed voltage and temperature range of 0-70°C | Total deviation of trimmed average DCO output frequency over fixed voltage and temperature range of 0-70°C | - | ± 0.3 | ± 0.3 | %fdco | 1 |
| fintf_ft | Internal reference frequency (fast clock) - factory trimmed at nominal VDD and 25°C | Internal reference frequency (fast clock) - factory trimmed at nominal VDD and 25°C | - | 4 | - | MHz |  |
| fintf_t | Internal reference frequency (fast clock) - user trimmed at nominal VDD and 25 °C | Internal reference frequency (fast clock) - user trimmed at nominal VDD and 25 °C | 3 | - | 5 | MHz |  |
| floc_low | Loss of external clock minimum frequency - RANGE = 00 | Loss of external clock minimum frequency - RANGE = 00 | (3/5) x fints_t | - | - | kHz |  |
| floc_high | Loss of external clock minimum frequency - RANGE = 01, 10, or 11 | Loss of external clock minimum frequency - RANGE = 01, 10, or 11 | (16/5) x fints_t | - | - | kHz |  |
| FLL | FLL | FLL | FLL | FLL | FLL | FLL | FLL |
| ffll_ref | FLL reference frequency range | FLL reference frequency range | 31.25 | - | 39.0625 | kHz |  |
| fdco | DCO output frequency range | Low range (DRS=00) 640 × ffll_ref | 20 | 20.97 | 25 | MHz | 2, 3 |
| fdco | DCO output frequency range | Mid range (DRS=01) 1280 × ffll_ref | 40 | 41.94 | 50 | MHz | 2, 3 |
| fdco | DCO output frequency range | Mid-high range (DRS=10) 1920 × ffll_ref | 60 | 62.91 | 75 | MHz | 2, 3 |
| fdco | DCO output frequency range | High range (DRS=11) 2560 × ffll_ref | 80 | 83.89 | 100 | MHz | 2, 3 |
| fdco_t_DMX32 | DCO output frequency | Low range (DRS=00) 732 × ffll_ref | - | 23.99 | - | MHz | 4, 5 |
| fdco_t_DMX32 | DCO output frequency | Mid range (DRS=01) 1464 × ffll_ref | - | 47.97 | - | MHz | 4, 5 |
| fdco_t_DMX32 | DCO output frequency | Mid-high range (DRS=10) 2197 × ffll_ref | - | 71.99 | - | MHz | 4, 5 |
| fdco_t_DMX32 | DCO output frequency | High range (DRS=11) 2929 × ffll_ref | - | 95.98 | - | MHz | 4, 5 |

Table continues on the next page...

Table 14. MCG specifications (continued)

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| Jcyc_fll | FLL period jitter | - | 180 | - | ps |  |
|  | · fVCO = 48 MHz · fVCO = 98 MHz | - | 150 | - |  |  |
| tfll_acquire | FLL target frequency acquisition time | - | - | 1 | ms | 6 |
| PLL | PLL | PLL | PLL | PLL | PLL | PLL |
| fvco | VCO operating frequency | 48.0 | - | 100 | MHz |  |
| Ipll | PLL operating current · PLL @ 96 MHz (fosc_hi_1 = 8 MHz, fpll_ref = 2 MHz, VDIV multiplier = 48) | - | 1060 | - | µA | 7 |
| Ipll | PLL operating current · PLL @ 48 MHz (fosc_hi_1 = 8 MHz, fpll_ref = 2 MHz, VDIV multiplier = 24) | - | 600 | - | µA | 7 |
| fpll_ref | PLL reference frequency range | 2.0 | - | 4.0 | MHz |  |
| Jcyc_pll | PLL period jitter (RMS) |  |  |  |  | 8 |
|  | · fvco = 48 MHz | - | 120 | - | ps |  |
|  | · fvco = 100 MHz | - | 50 | - | ps |  |
| Jacc_pll | PLL accumulated jitter over 1µs (RMS) |  |  |  |  | 8 |
|  | · fvco = 48 MHz | - | 1350 | - | ps |  |
|  | · fvco = 100 MHz | - | 600 | - | ps |  |
| Dlock | Lock entry frequency tolerance | ± 1.49 | - | ± 2.98 | % |  |
| Dunl | Lock exit frequency tolerance | ± 4.47 | - | ± 5.97 | % |  |
| tpll_lock | Lock detector detection time | - | - | 150 × 10 -6 + 1075(1/ fpll_ref) | s | 9 |

1. This parameter is measured with the internal reference (slow clock) being used as a reference to the FLL (FEI clock mode).
2. These typical values listed are with the slow internal reference clock (FEI) using factory trim and DMX32=0.
3. The resulting system clock frequencies should not exceed their maximum specified values. The DCO frequency deviation (Δfdco\_t) over voltage and temperature should be considered.
4. These typical values listed are with the slow internal reference clock (FEI) using factory trim and DMX32=1.
5. The resulting clock frequency must not exceed the maximum specified clock frequency of the device.
6. This specification applies to any time the FLL reference source or reference divider is changed, trim value is changed, DMX32 bit is changed, DRS bits are changed, or changing from FLL disabled (BLPE, BLPI) to FLL enabled (FEI, FEE, FBE, FBI). If a crystal/resonator is being used as the reference, this specification assumes it is already running.
7. Excludes any oscillator currents that are also consuming power while PLL is in operation.
8. This specification was obtained using a Freescale developed PCB. PLL jitter is dependent on the noise characteristics of each PCB and results will vary.
9. This specification applies to any time the PLL VCO divider or reference divider is changed, or changing from PLL disabled (BLPE, BLPI) to PLL enabled (PBE, PEE). If a crystal/resonator is being used as the reference, this specification assumes it is already running.

## 6.3.2 Oscillator electrical specifications

This section provides the electrical characteristics of the module.

## 6.3.2.1 Oscillator DC electrical specifications Table 15. Oscillator DC electrical specifications

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| VDD | Supply voltage | 1.71 | - | 3.6 | V |  |
| IDDOSC | Supply current - low-power mode (HGO=0) · 32 kHz | - | 500 | - | nA | 1 |
| IDDOSC | · 4 MHz | - | 200 | - | μA |  |
| IDDOSC | · 8 MHz (RANGE=01) | - | 300 | - | μA |  |
| IDDOSC | · 16 MHz | - | 950 | - | μA |  |
| IDDOSC | · 24 MHz | - | 1.2 | - | mA |  |
| IDDOSC | · 32 MHz | - | 1.5 | - | mA |  |
| IDDOSC | Supply current - high gain mode (HGO=1) · 32 kHz | - | 25 | - | μA | 1 |
| IDDOSC | · 4 MHz | - | 400 | - | μA |  |
| IDDOSC | · 8 MHz (RANGE=01) | - | 500 | - | μA |  |
| IDDOSC | · 16 MHz | - | 2.5 | - | mA |  |
| IDDOSC | · 24 MHz | - | 3 | - | mA |  |
| IDDOSC | · 32 MHz | - | 4 | - | mA |  |
| Cx | EXTAL load capacitance | - | - | - |  | 2, 3 |
| Cy | XTAL load capacitance | - | - | - |  | 2, 3 |
| RF | Feedback resistor - low-frequency, low-power mode (HGO=0) | - | - | - | MΩ | 2, 4 |
| RF | Feedback resistor - low-frequency, high-gain mode (HGO=1) | - | 10 | - | MΩ |  |
| RF | Feedback resistor - high-frequency, low-power mode (HGO=0) | - | - | - | MΩ |  |
| RF | Feedback resistor - high-frequency, high-gain mode (HGO=1) | - | 1 | - | MΩ |  |
| RS | Series resistor - low-frequency, low-power mode (HGO=0) | - | - | - | kΩ |  |
| RS | Series resistor - low-frequency, high-gain mode (HGO=1) | - | 200 | - | kΩ |  |
| RS | Series resistor - high-frequency, low-power mode (HGO=0) | - | - | - | kΩ |  |
| RS | Series resistor - high-frequency, high-gain mode (HGO=1) | - | 0 | - | kΩ |  |

Table continues on the next page...

## Table 15. Oscillator DC electrical specifications (continued)

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| Vpp 5 | Peak-to-peak amplitude of oscillation (oscillator mode) - low-frequency, low-power mode (HGO=0) | - | 0.6 | - | V |  |
| Vpp 5 | Peak-to-peak amplitude of oscillation (oscillator mode) - low-frequency, high-gain mode (HGO=1) | - | VDD | - | V |  |
| Vpp 5 | Peak-to-peak amplitude of oscillation (oscillator mode) - high-frequency, low-power mode (HGO=0) | - | 0.6 | - | V |  |
| Vpp 5 | Peak-to-peak amplitude of oscillation (oscillator mode) - high-frequency, high-gain mode (HGO=1) | - | VDD | - | V |  |

1. VDD=3.3 V, Temperature =25 °C
2. See crystal or resonator manufacturer's recommendation
3. Cx,Cy can be provided by using either the integrated capacitors or by using external components.
4. When low power mode is selected, RF is integrated and must not be attached externally.
5. The EXTAL and XTAL pins should only be connected to required oscillator components and must not be connected to any other devices.

## 6.3.2.2 Oscillator frequency specifications Table 16. Oscillator frequency specifications

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| fosc_lo | Oscillator crystal or resonator frequency - low frequency mode (MCG_C2[RANGE]=00) | 32 | - | 40 | kHz |  |
| fosc_hi_1 | Oscillator crystal or resonator frequency - high frequency mode (low range) (MCG_C2[RANGE]=01) | 3 | - | 8 | MHz |  |
| fosc_hi_2 | Oscillator crystal or resonator frequency - high frequency mode (high range) (MCG_C2[RANGE]=1x) | 8 | - | 32 | MHz |  |
| fec_extal | Input clock frequency (external clock mode) | - | - | 50 | MHz | 1, 2 |
| tdc_extal | Input clock duty cycle (external clock mode) | 40 | 50 | 60 | % |  |
| tcst | Crystal startup time - 32 kHz low-frequency, low-power mode (HGO=0) | - | 750 | - | ms | 3, 4 |
| tcst | Crystal startup time - 32 kHz low-frequency, high-gain mode (HGO=1) | - | 250 | - | ms | 3, 4 |
| tcst | Crystal startup time - 8 MHz high-frequency (MCG_C2[RANGE]=01), low-power mode (HGO=0) | - | 0.6 | - | ms | 3, 4 |
| tcst | Crystal startup time - 8 MHz high-frequency (MCG_C2[RANGE]=01), high-gain mode (HGO=1) | - | 1 | - | ms | 3, 4 |

1. Other frequency limits may apply when external clock is being used as a reference for the FLL or PLL.
2. When transitioning from FBE to FEI mode, restrict the frequency of the input clock so that, when it is divided by FRDIV, it remains within the limits of the DCO input clock frequency.
3. Proper PC board layout procedures must be followed to achieve specifications.

## Peripheral operating requirements and behaviors

4. Crystal startup time is defined as the time between the oscillator being enabled and the OSCINIT bit in the MCG\_S register being set.

## NOTE

The 32 kHz oscillator works in low power mode by default and cannot be moved into high power/gain mode.

## 6.3.3 32 kHz Oscillator Electrical Characteristics

This section describes the module electrical characteristics.

## 6.3.3.1 32 kHz oscillator DC electrical specifications

## Table 17. 32kHz oscillator DC electrical specifications

| Symbol | Description | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - |
| VBAT | Supply voltage | 1.71 | - | 3.6 | V |
| RF | Internal feedback resistor | - | 100 | - | MΩ |
| Cpara | Parasitical capacitance of EXTAL32 and XTAL32 | - | 5 | 7 | pF |
| Vpp 1 | Peak-to-peak amplitude of oscillation | - | 0.6 | - | V |

1. When a crystal is being used with the 32 kHz oscillator, the EXTAL32 and XTAL32 pins should only be connected to required oscillator components and must not be connected to any other devices.

## 6.3.3.2 32kHz oscillator frequency specifications

## Table 18. 32kHz oscillator frequency specifications

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| fosc_lo | Oscillator crystal | - | 32.768 | - | kHz |  |
| tstart | Crystal start-up time | - | 1000 | - | ms | 1 |
| vec_extal32 | Externally provided input clock amplitude | 700 | - | VBAT | mV | 2, 3 |

1. Proper PC board layout procedures must be followed to achieve specifications.
2. This specification is for an externally supplied clock driven to EXTAL32 and does not apply to any other clock input. The oscillator remains enabled and XTAL32 must be left unconnected.
3. The parameter specified is a peak-to-peak value and VIH and VIL specifications do not apply. The voltage of the applied clock must be within the range of VSS to VBAT.

## 6.4 Memories and memory interfaces

## 6.4.1 Flash electrical specifications

This section describes the electrical characteristics of the flash memory module.

K20 Sub-Family Data Sheet, Rev. 3, 11/2012.

## 6.4.1.1 Flash timing specifications - program and erase

The following specifications represent the amount of time the internal charge pumps are active and do not include command overhead.

Table 19. NVM program/erase timing specifications

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| thvpgm4 | Longword Program high-voltage time | - | 7.5 | 18 | μs |  |
| thversscr | Sector Erase high-voltage time | - | 13 | 113 | ms | 1 |
| thversblk32k | Erase Block high-voltage time for 32 KB | - | 52 | 452 | ms | 1 |
| thversblk256k | Erase Block high-voltage time for 256 KB | - | 104 | 904 | ms | 1 |

1. Maximum time based on expectations at cycling end-of-life.

## 6.4.1.2 Flash timing specifications - commands

## Table 20. Flash command timing specifications

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
|  | Read 1s Block execution time |  |  |  |  |  |
| trd1blk32k | · 32 KB data flash | - | - | 0.5 | ms |  |
| trd1blk256k | · 256 KB program flash | - | - | 1.7 | ms |  |
| trd1sec1k | Read 1s Section execution time (data flash sector) | - | - | 60 | μs | 1 |
| trd1sec2k | Read 1s Section execution time (program flash sector) | - | - | 60 | μs | 1 |
| tpgmchk | Program Check execution time | - | - | 45 | μs | 1 |
| trdrsrc | Read Resource execution time | - | - | 30 | μs | 1 |
| tpgm4 | Program Longword execution time | - | 65 | 145 | μs |  |
|  | Erase Flash Block execution time |  |  |  |  | 2 |
| tersblk32k | · 32 KB data flash | - | 55 | 465 | ms |  |
| tersblk256k | · 256 KB program flash | - | 122 | 985 | ms |  |
| tersscr | Erase Flash Sector execution time | - | 14 | 114 | ms | 2 |
|  | Program Section execution time |  |  |  |  |  |
| tpgmsec512p | · 512 B program flash | - | 2.4 | - | ms |  |
| tpgmsec512d | · 512 B data flash | - | 4.7 | - | ms |  |
| tpgmsec1kp | · 1 KB program flash | - | 4.7 | - | ms |  |
| tpgmsec1kd | · 1 KB data flash | - | 9.3 | - | ms |  |
| trd1all | Read 1s All Blocks execution time | - | - | 1.8 | ms |  |
| trdonce | Read Once execution time | - | - | 25 | μs | 1 |
| tpgmonce | Program Once execution time | - | 65 | - | μs |  |
| tersall | Erase All Blocks execution time | - | 175 | 1500 | ms | 2 |

Table continues on the next page...

## Table 20. Flash command timing specifications (continued)

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| tvfykey | Verify Backdoor Access Key execution time | - | - | 30 | μs | 1 |
| Swap Control execution time |  |  |  |  |  |  |
| tswapx01 | · control code 0x01 | - | 200 | - | μs |  |
| tswapx02 | · control code 0x02 | - | 70 | 150 | μs |  |
| tswapx04 | · control code 0x04 | - | 70 | 150 | μs |  |
| tswapx08 | · control code 0x08 | - | - | 30 | μs |  |
| tpgmpart32k | Program Partition for EEPROM execution time · 32 KB FlexNVM | - | 70 | - | ms |  |
| Set FlexRAM Function execution | time: |  |  |  |  |  |
| tsetramff | · Control Code 0xFF | - | 50 | - | μs |  |
| tsetram8k | · 8 KB EEPROM backup | - | 0.3 | 0.5 | ms |  |
| tsetram32k | · 32 KB EEPROM backup | - | 0.7 | 1.0 | ms |  |
| Byte-write to FlexRAM for EEPROM operation |  |  |  |  |  |  |
| teewr8bers | Byte-write to erased FlexRAM location execution time | - | 175 | 260 | μs | 3 |
|  | Byte-write to FlexRAM execution time: |  |  |  |  |  |
| teewr8b8k | · 8 KB EEPROM backup | - | 340 | 1700 | μs |  |
| teewr8b16k | · 16 KB EEPROM backup | - | 385 | 1800 | μs |  |
| teewr8b32k | · 32 KB EEPROM backup | - | 475 | 2000 | μs |  |
| Word-write to FlexRAM for EEPROM operation | Word-write to FlexRAM for EEPROM operation | Word-write to FlexRAM for EEPROM operation | Word-write to FlexRAM for EEPROM operation | Word-write to FlexRAM for EEPROM operation | Word-write to FlexRAM for EEPROM operation | Word-write to FlexRAM for EEPROM operation |
| teewr16bers | Word-write to erased FlexRAM location execution time | - | 175 | 260 | μs |  |
|  | Word-write to FlexRAM execution time: |  |  |  |  |  |
| teewr16b8k | · 8 KB EEPROM backup | - | 340 | 1700 | μs |  |
| teewr16b16k | · 16 KB EEPROM backup | - | 385 | 1800 | μs |  |
| teewr16b32k | · 32 KB EEPROM backup | - | 475 | 2000 | μs |  |
| Longword-write to FlexRAM for EEPROM operation | Longword-write to FlexRAM for EEPROM operation | Longword-write to FlexRAM for EEPROM operation | Longword-write to FlexRAM for EEPROM operation | Longword-write to FlexRAM for EEPROM operation | Longword-write to FlexRAM for EEPROM operation | Longword-write to FlexRAM for EEPROM operation |
| teewr32bers | Longword-write to erased FlexRAM location execution time | - | 360 | 540 | μs |  |
|  | Longword-write to FlexRAM execution time: |  |  |  |  |  |
| teewr32b8k | · 8 KB EEPROM backup | - | 545 | 1950 | μs |  |
| teewr32b16k | · 16 KB EEPROM backup | - | 630 | 2050 | μs |  |
| teewr32b32k | · 32 KB EEPROM backup | - | 810 | 2250 | μs |  |

1. Assumes 25 MHz flash clock frequency.

2. Maximum times for erase parameters based on expectations at cycling end-of-life.
3. For byte-writes to an erased FlexRAM location, the aligned word containing the byte must be erased.

## 6.4.1.3 Flash high voltage current behaviors

## Table 21. Flash high voltage current behaviors

| Symbol | Description | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - |
| IDD_PGM | Average current adder during high voltage flash programming operation | - | 2.5 | 6.0 | mA |
| IDD_ERS | Average current adder during high voltage flash erase operation | - | 1.5 | 4.0 | mA |

## 6.4.1.4 Reliability specifications

## Table 22. NVM reliability specifications

| Symbol | Description | Min. | Typ. 1 | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| Program Flash | Program Flash | Program Flash | Program Flash | Program Flash | Program Flash | Program Flash |
| tnvmretp10k | Data retention after up to 10 K cycles | 5 | 50 | - | years |  |
| tnvmretp1k | Data retention after up to 1 K cycles | 20 | 100 | - | years |  |
| nnvmcycp | Cycling endurance | 10 K | 50 K | - | cycles | 2  ![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_017.png) |
| Data Flash | Data Flash | Data Flash | Data Flash | Data Flash | Data Flash | Data Flash |
| tnvmretd10k | Data retention after up to 10 K cycles | 5 | 50 | - | years |  |
| tnvmretd1k | Data retention after up to 1 K cycles | 20 | 100 | - | years |  |
| nnvmcycd | Cycling endurance | 10 K | 50 K | - | cycles | 2  ![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_018.png) |
| FlexRAM as EEPROM | FlexRAM as EEPROM | FlexRAM as EEPROM | FlexRAM as EEPROM | FlexRAM as EEPROM | FlexRAM as EEPROM | FlexRAM as EEPROM |
| tnvmretee100 | Data retention up to 100% of write endurance | 5 | 50 | - | years |  |
| tnvmretee10 | Data retention up to 10% of write endurance | 20 | 100 | - | years |  |
|  | Write endurance |  |  |  |  | 3  ![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_016.png) |
| nnvmwree16 | · EEPROM backup to FlexRAM ratio = 16 | 35 K | 175 K | - | writes |  |
| nnvmwree128 | · EEPROM backup to FlexRAM ratio = 128 | 315 K | 1.6 M | - | writes |  |
| nnvmwree512 | · EEPROM backup to FlexRAM ratio = 512 | 1.27 M | 6.4 M | - | writes |  |
| nnvmwree4k | · EEPROM backup to FlexRAM ratio = 4096 | 10 M | 50 M | - | writes |  |
| nnvmwree8k | · EEPROM backup to FlexRAM ratio = 8192 | 20 M | 100 M | - | writes |  |

1. Typical data retention values are based on measured response accelerated at high temperature and derated to a constant 25°C use profile. Engineering Bulletin EB618 does not apply to this technology. Typical endurance defined in Engineering Bulletin EB619.
2. Cycling endurance represents number of program/erase cycles at -40°C ≤ Tj ≤ 125°C.
3. Write endurance represents the number of writes to each FlexRAM location at -40°C ≤Tj ≤ 125°C influenced by the cycling endurance of the FlexNVM (same value as data flash) and the allocated EEPROM backup per subsystem. Minimum and typical values assume all byte-writes to FlexRAM.

## 6.4.1.5 Write endurance to FlexRAM for EEPROM

When the FlexNVM partition code is not set to full data flash, the EEPROM data set size can be set to any of several non-zero values.

## Peripheral operating requirements and behaviors

The bytes not assigned to data flash via the FlexNVM partition code are used by the flash memory module to obtain an effective endurance increase for the EEPROM data. The built-in EEPROM record management system raises the number of program/erase cycles that can be attained prior to device wear-out by cycling the EEPROM data through a larger EEPROM NVM storage space.

While different partitions of the FlexNVM are available, the intention is that a single choice for the FlexNVM partition code and EEPROM data set size is used throughout the entire lifetime of a given application. The EEPROM endurance equation and graph shown below assume that only one configuration is ever used.

<!-- formula-not-decoded -->

## where

- Writes\_subsystem - minimum number of writes to each FlexRAM location for subsystem (each subsystem can have different endurance)
- EEPROM - allocated FlexNVM for each EEPROM subsystem based on DEPART; entered with the Program Partition command
- EEESPLIT - FlexRAM split factor for subsystem; entered with the Program Partition command
- EEESIZE - allocated FlexRAM based on DEPART; entered with the Program Partition command
- Write\_efficiency -
- 0.25 for 8-bit writes to FlexRAM
- 0.50 for 16-bit or 32-bit writes to FlexRAM
- nnvmcycd - data flash cycling endurance (the following graph assumes 10,000 cycles)

## Peripheral operating requirements and behaviors

Figure 10. EEPROM backup writes to FlexRAM

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_019.png)

## 6.4.2 EzPort Switching Specifications

## Table 23. EzPort switching specifications

| Num | Description | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V |
| EP1 | EZP_CK frequency of operation (all commands except READ) | - | fSYS/2 | MHz |
| EP1a | EZP_CK frequency of operation (READ command) | - | fSYS/8 | MHz |
| EP2 | EZP_CS negation to next EZP_CS assertion | 2 x tEZP_CK | - | ns |
| EP3 | EZP_CS input valid to EZP_CK high (setup) | 5 | - | ns |
| EP4 | EZP_CK high to EZP_CS input invalid (hold) | 5 | - | ns |
| EP5 | EZP_D input valid to EZP_CK high (setup) | 2 | - | ns |
| EP6 | EZP_CK high to EZP_D input invalid (hold) | 5 | - | ns |
| EP7 | EZP_CK low to EZP_Q output valid | - | 16 | ns |
| EP8 | EZP_CK low to EZP_Q output invalid (hold) | 0 | - | ns |
| EP9 | EZP_CS negation to EZP_Q tri-state | - | 12 | ns |

Figure 11. EzPort Timing Diagram

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_020.png)

## 6.5 Security and integrity modules

There are no specifications necessary for the device's security and integrity modules.

## 6.6 Analog

## 6.6.1 ADC electrical specifications

The 16-bit accuracy specifications listed in Table 24 and Table 25 are achievable on the differential pins ADCx\_DP0, ADCx\_DM0.

The ADCx\_DP2 and ADCx\_DM2 ADC inputs are connected to the PGA outputs and are not direct device pins. Accuracy specifications for these pins are defined in Table 26 and Table 27.

All other ADC channels meet the 13-bit differential/12-bit single-ended accuracy specifications.

## 6.6.1.1 16-bit ADC operating conditions

## Table 24. 16-bit ADC operating conditions

| Symbol | Description | Conditions | Min. | Typ. 1 | Max. | Unit | Notes |
| - | - | - | - | - | - | - | - |
| VDDA | Supply voltage | Absolute | 1.71 | - | 3.6 | V |  |
| ΔVDDA | Supply voltage | Delta to VDD (VDD - VDDA) | -100 | 0 | +100 | mV | 2 |
| ΔVSSA | Ground voltage | Delta to VSS (VSS - VSSA) | -100 | 0 | +100 | mV | 2 |
| VREFH | ADC reference voltage high |  | 1.13 | VDDA | VDDA | V |  |
| VREFL | ADC reference voltage low |  | VSSA | VSSA | VSSA | V |  |
| VADIN | Input voltage | · 16-bit differential mode · All other modes | VREFL VREFL | - - | 31/32 * VREFH VREFH | V |  |
| CADIN | Input capacitance | · 16-bit mode · 8-/10-/12-bit modes | - - | 8 4 | 10 5 | pF |  |
| RADIN | Input resistance |  | - | 2 | 5 | kΩ |  |
| RAS | Analog source resistance | 13-/12-bit modes fADCK < 4 MHz | - | - | 5 | kΩ | 3 |
| fADCK | ADC conversion clock frequency | ≤ 13-bit mode | 1.0 | - | 18.0 | MHz | 4 |
| fADCK | ADC conversion clock frequency | 16-bit mode | 2.0 | - | 12.0 | MHz | 4 |
| Crate | ADC conversion rate | ≤ 13 bit modes No ADC hardware averaging Continuous conversions enabled, subsequent | 20.000 | - | 818.330 | Ksps | 5 |
| Crate | ADC conversion rate | conversion time 16-bit mode No ADC hardware averaging Continuous conversions enabled, subsequent conversion time | 37.037 | - | 461.467 | Ksps | 5 |

1. Typical values assume VDDA = 3.0 V, Temp = 25 °C, fADCK = 1.0 MHz unless otherwise stated. Typical values are for reference only and are not tested in production.
2. DC potential difference.
3. This resistance is external to MCU. The analog source resistance must be kept as low as possible to achieve the best results. The results in this data sheet were derived from a system which has &lt; 8 Ω analog source resistance. The RAS/CAS time constant should be kept to &lt; 1ns.
4. To use the maximum ADC conversion clock frequency, the ADHSC bit must be set and the ADLPC bit must be clear.
5. For guidelines and examples of conversion rate calculation, download the ADC calculator tool

## Peripheral operating requirements and behaviors

Figure 12. ADC input impedance equivalency diagram

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_021.png)

## 6.6.1.2 16-bit ADC electrical characteristics

Table 25. 16-bit ADC characteristics (VREFH = VDDA, VREFL = VSSA)

| Symbol | Description | Conditions 1 | Min. | Typ. 2 | Max. | Unit | Notes |
| - | - | - | - | - | - | - | - |
| IDDA_ADC | Supply current |  | 0.215 | - | 1.7 | mA | 3 |
| fADACK | ADC asynchronous clock source | · ADLPC = 1, ADHSC = 0 · ADLPC = 1, ADHSC = 1 · ADLPC = 0, ADHSC = 0 · ADLPC = 0, ADHSC = 1 | 1.2 2.4 3.0 4.4 | 2.4 4.0 5.2 6.2 | 3.9 6.1 7.3 9.5 | MHz MHz MHz MHz | tADACK = 1/ fADACK |
|  | Sample Time | See Reference Manual chapter for sample times | See Reference Manual chapter for sample times | See Reference Manual chapter for sample times | See Reference Manual chapter for sample times | See Reference Manual chapter for sample times | See Reference Manual chapter for sample times |
| TUE | Total unadjusted error | · 12-bit modes · <12-bit modes | - - | ±4 ±1.4 | ±6.8 ±2.1 | LSB 4 | 5 |
| DNL | Differential non- linearity | · 12-bit modes · <12-bit modes | - - | ±0.7 ±0.2 | -1.1 to +1.9 -0.3 to 0.5 | LSB 4 | 5 |
| INL | Integral non- linearity | · 12-bit modes · <12-bit modes | - - | ±1.0 ±0.5 | -2.7 to +1.9 -0.7 to +0.5 | LSB 4 | 5 |
| EFS | Full-scale error | · 12-bit modes · <12-bit modes | - - | -4 -1.4 | -5.4 -1.8 | LSB 4 | VADIN = VDDA 5 |

Table continues on the next page...

## Table 25. 16-bit ADC characteristics (VREFH = VDDA, VREFL = VSSA) (continued)

| Symbol | Description | Conditions 1 | Min. | Typ. 2 | Max. | Unit | Notes |
| - | - | - | - | - | - | - | - |
| EQ | Quantization error | · 16-bit modes · ≤13-bit modes | - - | -1 to 0 - | - ±0.5 | LSB 4 |  |
| ENOB | Effective number of bits | 16-bit differential mode · Avg = 32 · Avg = 4 16-bit single-ended mode · Avg = 32 · Avg = 4 | 12.8 11.9 12.2 11.4 | 14.5 13.8 13.9 13.1 | - - - - | bits bits bits bits | 6 |
| SINAD | Signal-to-noise plus distortion | See ENOB | 6.02 × ENOB + 1.76 | 6.02 × ENOB + 1.76 | 6.02 × ENOB + 1.76 | dB |  |
| THD | Total harmonic distortion | 16-bit differential mode · Avg = 32 16-bit single-ended mode · Avg = 32 | - - | -94 -85 | - - | dB dB | 7 |
| SFDR | Spurious free dynamic range | 16-bit differential mode · Avg = 32 16-bit single-ended mode · Avg = 32 | 82 78 | 95 90 | - - | dB dB | 7 |
| EIL | Input leakage error |  | IIn × RAS | IIn × RAS | IIn × RAS | mV | IIn = leakage current (refer to the MCU's voltage and current operating ratings) |
|  | Temp sensor slope | Across the full temperature range of the device | - | 1.715 | - | mV/°C |  |
| VTEMP25 | Temp sensor voltage | 25 °C | - | 719 | - | mV |  |

1. All accuracy numbers assume the ADC is calibrated with VREFH = VDDA
2. Typical values assume VDDA = 3.0 V, Temp = 25°C, fADCK = 2.0 MHz unless otherwise stated. Typical values are for reference only and are not tested in production.
3. The ADC supply current depends on the ADC conversion clock speed, conversion rate and the ADLPC bit (low power). For lowest power operation the ADLPC bit must be set, the HSC bit must be clear with 1 MHz ADC conversion clock speed.
4. 1 LSB = (VREFH - VREFL)/2 N
5. ADC conversion clock &lt; 16 MHz, Max hardware averaging (AVGE = %1, AVGS = %11)
6. Input data is 100 Hz sine wave. ADC conversion clock &lt; 12 MHz.
7. Input data is 1 kHz sine wave. ADC conversion clock &lt; 12 MHz.

## Typical ADC 16-bit Differential ENOB vs ADC Clock 100Hz, 90% FS Sine Input

Figure 13. Typical ENOB vs. ADC\_CLK for 16-bit differential mode

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_022.png)

## Typical ADC 16-bit Single-Ended ENOB vs ADC Clock 100Hz, 90% FS Sine Input

14.00

Figure 14. Typical ENOB vs. ADC\_CLK for 16-bit single-ended mode

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_023.png)

## 6.6.1.3 16-bit ADC with PGA operating conditions Table 26. 16-bit ADC with PGA operating conditions

| Symbol | Description | Conditions | Min. | Typ. 1 | Max. | Unit | Notes |
| - | - | - | - | - | - | - | - |
| VDDA | Supply voltage | Absolute | 1.71 | - | 3.6 | V |  |
| VREFPGA | PGA ref voltage |  | VREF_OU T | VREF_OU T | VREF_OU T | V | 2, 3 |
| VADIN | Input voltage |  | VSSA | - | VDDA | V |  |
| VCM | Input Common Mode range |  | VSSA | - | VDDA | V |  |
| RPGAD | Differential input impedance | Gain = 1, 2, 4, 8 Gain = 16, 32 Gain = 64 | - - - | 128 64 32 | - - - | kΩ | IN+ to IN- 4 |
| RAS | Analog source resistance |  | - | 100 | - | Ω | 5 |
| TS | ADC sampling time |  | 1.25 | - | - | µs | 6 |
| Crate | ADC conversion rate | ≤ 13 bit modes No ADC hardware averaging | 18.484 | - | 450 | Ksps | 7 |
| Crate |  | Continuous conversions enabled Peripheral clock = 50 |  |  |  |  |  |
| Crate |  | MHz |  |  |  |  |  |
| Crate |  | 16 bit modes No ADC hardware averaging | 37.037 | - | 250 | Ksps | 8 |
| Crate |  | Continuous |  |  |  |  |  |
| Crate |  | conversions enabled |  |  |  |  |  |
| Crate |  | Peripheral clock = 50 MHz |  |  |  |  |  |

1. Typical values assume VDDA = 3.0 V, Temp = 25°C, fADCK = 6 MHz unless otherwise stated. Typical values are for reference only and are not tested in production.
2. ADC must be configured to use the internal voltage reference (VREF\_OUT)
3. PGA reference is internally connected to the VREF\_OUT pin. If the user wishes to drive VREF\_OUT with a voltage other than the output of the VREF module, the VREF module must be disabled.
4. For single ended configurations the input impedance of the driven input is RPGAD/2
5. The analog source resistance (RAS), external to MCU, should be kept as minimum as possible. Increased RAS causes drop in PGA gain without affecting other performances. This is not dependent on ADC clock frequency.
6. The minimum sampling time is dependent on input signal frequency and ADC mode of operation. A minimum of 1.25µs time should be allowed for Fin=4 kHz at 16-bit differential mode. Recommended ADC setting is: ADLSMP=1, ADLSTS=2 at 8 MHz ADC clock.
7. ADC clock = 18 MHz, ADLSMP = 1, ADLST = 00, ADHSC = 1
8. ADC clock = 12 MHz, ADLSMP = 1, ADLST = 01, ADHSC = 1

## 6.6.1.4 16-bit ADC with PGA characteristics with Chop enabled (ADC\_PGA[PGACHPb] =0)

## Table 27. 16-bit ADC with PGA characteristics

| Symbol | Description | Conditions | Min. | Typ. 1 | Max. | Unit | Notes |
| - | - | - | - | - | - | - | - |
| IDDA_PGA | Supply current | Low power (ADC_PGA[PGALPb]=0) | - | 420 | 644 | μA | 2 |
| IDC_PGA | Input DC current |  |  |  |  | A | 3 |
| IDC_PGA | Input DC current | Gain =1, VREFPGA=1.2V, VCM=0.5V | - | 1.54 | - | μA | 3 |
| IDC_PGA | Input DC current | Gain =64, VREFPGA=1.2V, VCM=0.1V | - | 0.57 | - | μA | 3 |
| G | Gain 4 | · PGAG=0 · PGAG=1 · PGAG=2 · PGAG=3 · PGAG=4 · PGAG=5 · PGAG=6 | 0.95 1.9 3.8 7.6 15.2 30.0 58.8 | 1 2 4 8 16 31.6 63.3 | 1.05 2.1 4.2 8.4 16.6 33.2 67.8 |  | RAS < 100Ω |
| BW | Input signal bandwidth | · 16-bit modes · < 16-bit modes | - - | - - | 4 40 | kHz kHz |  |
| PSRR | Power supply rejection ratio | Gain=1 | - | -84 | - | dB | VDDA= 3V ±100mV, fVDDA= 50Hz, 60Hz |
| CMRR | Common mode rejection ratio | · Gain=1 · Gain=64 | - - | -84 -85 | - - | dB dB | VCM= 500mVpp, fVCM= 50Hz, 100Hz |
| VOFS | Input offset voltage |  | - | 0.2 | - | mV | Output offset = VOFS*(Gain+1) |
| TGSW | Gain switching settling time |  | - | - | 10 | µs | 5 |
| dG/dT | Gain drift over full temperature range | · Gain=1 · Gain=64 | - - | 6 31 | 10 42 | ppm/°C ppm/°C |  |
| dG/dVDDA | Gain drift over supply voltage | · Gain=1 · Gain=64 | - - | 0.07 0.14 | 0.21 0.31 | %/V %/V | VDDA from 1.71 to 3.6V |
| EIL | Input leakage error | All modes |  | IIn × RAS |  | mV | IIn = leakage current (refer to the MCU's voltage and current operating ratings) |

Table continues on the next page...

Table 27. 16-bit ADC with PGA characteristics (continued)

| Symbol | Description | Conditions | Min. | Typ. 1 | Max. | Unit | Notes |
| - | - | - | - | - | - | - | - |
| VPP,DIFF | Maximum differential input signal swing |  | where VX | = VREFPGA | × 0.583 | V | 6 |
| SNR | Signal-to-noise ratio | · Gain=1 · Gain=64 | 80 52 | 90 66 | - - | dB dB | 16-bit differential mode, Average=32 |
| THD | Total harmonic distortion | · Gain=1 · Gain=64 | 85 49 | 100 95 | - - | dB dB | 16-bit differential mode, Average=32, fin=100Hz |
| SFDR | Spurious free dynamic range | · Gain=1 · Gain=64 | 85 53 | 105 88 | - - | dB dB | 16-bit differential mode, Average=32, fin=100Hz |
| ENOB | Effective number of bits | · Gain=1, Average=4 · Gain=64, Average=4 · Gain=1, Average=32 · Gain=2, Average=32 · Gain=4, Average=32 · Gain=8, Average=32 · Gain=16, Average=32 · Gain=32, Average=32 · Gain=64, Average=32 | 11.6 7.2 12.8 11.0 7.9 7.3 6.8 6.8 7.5 | 13.4 9.6 14.5 14.3 13.8 13.1 12.5 11.5 10.6 | - - - - - - - - - | bits bits bits bits bits bits bits bits bits | 16-bit differential mode,fin=100Hz |
| SINAD | Signal-to-noise plus distortion ratio | See ENOB | 6.02 × ENOB + 1.76 | 6.02 × ENOB + 1.76 | 6.02 × ENOB + 1.76 | dB |  |

1. Typical values assume VDDA =3.0V, Temp=25°C, fADCK=6MHz unless otherwise stated.
2. This current is a PGA module adder, in addition to ADC conversion currents.
3. Between IN+ and IN-. The PGA draws a DC current from the input terminals. The magnitude of the DC current is a strong function of input common mode voltage (VCM) and the PGA gain.

4. Gain = 2 PGAG

5. After changing the PGA gain setting, a minimum of 2 ADC+PGA conversions should be ignored.
6. Limit the input signal swing so that the PGA does not saturate during operation. Input signal swing is dependent on the PGA reference voltage and gain setting.

## 6.6.2 CMP and 6-bit DAC electrical specifications

## Table 28. Comparator and 6-bit DAC electrical specifications

| Symbol | Description | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - |
| VDD | Supply voltage | 1.71 | - | 3.6 | V |

Table continues on the next page...

## Table 28. Comparator and 6-bit DAC electrical specifications (continued)

| Symbol | Description | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - |
| IDDHS | Supply current, High-speed mode (EN=1, PMODE=1) | - | - | 200 | μA |
| IDDLS | Supply current, low-speed mode (EN=1, PMODE=0) | - | - | 20 | μA |
| VAIN | Analog input voltage | VSS - 0.3 | - | VDD | V |
| VAIO | Analog input offset voltage | - | - | 20 | mV |
| VH | Analog comparator hysteresis 1 · CR0[HYSTCTR] = 00 · CR0[HYSTCTR] = 01 · CR0[HYSTCTR] = 10 · CR0[HYSTCTR] = 11 | - - - - | 5 10 20 30 | - - - - | mV mV mV mV |
| VCMPOh | Output high | VDD - 0.5 | - | - | V |
| VCMPOl | Output low | - | - | 0.5 | V |
| tDHS | Propagation delay, high-speed mode (EN=1, PMODE=1) | 20 | 50 | 200 | ns |
| tDLS | Propagation delay, low-speed mode (EN=1, PMODE=0) | 80 | 250 | 600 | ns |
|  | Analog comparator initialization delay 2 | - | - | 40 | μs |
| IDAC6b | 6-bit DAC current adder (enabled) | - | 7 | - | μA |
| INL | 6-bit DAC integral non-linearity | -0.5 | - | 0.5 | LSB 3 |
| DNL | 6-bit DAC differential non-linearity | -0.3 | - | 0.3 | LSB |

1. Typical hysteresis is measured with input voltage range limited to 0.6 to VDD-0.6V.
2. Comparator initialization delay is defined as the time between software writes to change control inputs (Writes to DACEN, VRSEL, PSEL, MSEL, VOSEL) and the comparator output settling to a stable level.

3. 1 LSB = Vreference/64

## Peripheral operating requirements and behaviors

Figure 15. Typical hysteresis vs. Vin level (VDD=3.3V, PMODE=0)

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_024.png)

## Peripheral operating requirements and behaviors

Figure 16. Typical hysteresis vs. Vin level (VDD=3.3V, PMODE=1)

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_025.png)

## 6.6.3 12-bit DAC electrical characteristics

## 6.6.3.1 12-bit DAC operating requirements

## Table 29. 12-bit DAC operating requirements

| Symbol | Desciption | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| VDDA | Supply voltage | 1.71 | 3.6 | V |  |
| VDACR | Reference voltage | 1.13 | 3.6 | V | 1 |
| TA | Temperature | Operating temperature range of the device | Operating temperature range of the device | °C |  |
| CL | Output load capacitance | - | 100 | pF | 2 |
| IL | Output load current | - | 1 | mA |  |

1. The DAC reference can be selected to be VDDA or the voltage output of the VREF module (VREF\_OUT)
2. A small load capacitance (47 pF) can improve the bandwidth performance of the DAC

## 6.6.3.2 12-bit DAC operating behaviors

## Table 30. 12-bit DAC operating behaviors

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| IDDA_DACL P | Supply current - low-power mode | - | - | 150 | μA |  |
| IDDA_DACH P | Supply current - high-speed mode | - | - | 700 | μA |  |
| tDACLP | Full-scale settling time (0x080 to 0xF7F) - low-power mode | - | 100 | 200 | μs | 1 |
| tDACHP | Full-scale settling time (0x080 to 0xF7F) - high-power mode | - | 15 | 30 | μs | 1 |
| tCCDACLP | Code-to-code settling time (0xBF8 to 0xC08) - low-power mode and high-speed mode | - | 0.7 | 1 | μs | 1 |
| Vdacoutl | DAC output voltage range low - high-speed mode, no load, DAC set to 0x000 | - | - | 100 | mV |  |
| Vdacouth | DAC output voltage range high - high- speed mode, no load, DAC set to 0xFFF | VDACR -100 | - | VDACR | mV |  |
| INL | Integral non-linearity error - high speed mode | - | - | ±8 | LSB | 2 |
| DNL | Differential non-linearity error - VDACR > 2 V | - | - | ±1 | LSB | 3 |
| DNL | Differential non-linearity error - VDACR = VREF_OUT | - | - | ±1 | LSB | 4 |
| VOFFSET | Offset error | - | ±0.4 | ±0.8 | %FSR | 5 |
| EG | Gain error | - | ±0.1 | ±0.6 | %FSR | 5 |
| PSRR | Power supply rejection ratio, VDDA ≥ 2.4 V | 60 | - | 90 | dB |  |
| TCO | Temperature coefficient offset voltage | - | 3.7 | - | μV/C | 6 |
| TGE | Temperature coefficient gain error | - | 0.000421 | - | %FSR/C |  |
| Rop | Output resistance load = 3 kΩ | - | - | 250 | Ω |  |
| SR | Slew rate -80h→ F7Fh→ 80h |  |  |  | V/μs |  |
|  | · High power (SPHP) | 1.2 | 1.7 | - |  |  |
|  | · Low power (SPLP) | 0.05 | 0.12 | - |  |  |
| CT | Channel to channel cross talk | - | - | -80 | dB |  |
| BW | 3dB bandwidth |  |  |  | kHz |  |
|  | · High power (SPHP) | 550 | - | - |  |  |
|  | · Low power (SPLP) | 40 | - | - |  |  |

1. Settling within ±1 LSB
2. The INL is measured for 0 + 100 mV to VDACR -100 mV
3. The DNL is measured for 0 + 100 mV to VDACR -100 mV
4. The DNL is measured for 0 + 100 mV to VDACR -100 mV with VDDA &gt; 2.4 V
5. Calculated by a best fit curve from VSS + 100 mV to VDACR - 100 mV
6. VDDA = 3.0 V, reference select set for VDDA (DACx\_CO:DACRFS = 1), high power mode (DACx\_C0:LPEN = 0), DAC set to 0x800, temperature range is across the full range of the device

## Peripheral operating requirements and behaviors

Figure 17. Typical INL error vs. digital code

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_026.png)

Figure 18. Offset at half scale vs. temperature

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_027.png)

## 6.6.4 Voltage reference electrical specifications

Table 31. VREF full-range operating requirements

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| VDDA | Supply voltage | 1.71 | 3.6 | V |  |
| TA | Temperature | Operating temperature range of the device | Operating temperature range of the device | °C |  |
| CL | Output load capacitance | 100 | 100 | nF | 1, 2 |

1. CL must be connected to VREF\_OUT if the VREF\_OUT functionality is being used for either an internal or external reference.
2. The load capacitance should not exceed +/-25% of the nominal specified CL value over the operating temperature range of the device.

## Table 32. VREF full-range operating behaviors

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| Vout | Voltage reference output with factory trim at nominal VDDA and temperature=25C | 1.1915 | 1.195 | 1.1977 | V |  |
| Vout | Voltage reference output - factory trim | 1.1584 | - | 1.2376 | V |  |
| Vout | Voltage reference output - user trim | 1.193 | - | 1.197 | V |  |
| Vstep | Voltage reference trim step | - | 0.5 | - | mV |  |
| Vtdrift | Temperature drift (Vmax -Vmin across the full temperature range) | - | - | 80 | mV |  |
| Ibg | Bandgap only current | - | - | 80 | µA | 1 |
| Ilp | Low-power buffer current | - | - | 360 | uA | 1 |
| Ihp | High-power buffer current | - | - | 1 | mA | 1 |
| ΔVLOAD | Load regulation · current = ± 1.0 mA | - | 200 | - | µV | 1, 2 |
| Tstup | Buffer startup time | - | - | 100 | µs |  |
| Vvdrift | Voltage drift (Vmax -Vmin across the full voltage range) | - | 2 | - | mV | 1 |

1. See the chip's Reference Manual for the appropriate settings of the VREF Status and Control register.
2. Load regulation voltage is the difference between the VREF\_OUT voltage with no load vs. voltage with defined load

## Table 33. VREF limited-range operating requirements

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| TA | Temperature | 0 | 50 | °C |  |

## Table 34. VREF limited-range operating behaviors

| Symbol | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
| Vout | Voltage reference output with factory trim | 1.173 | 1.225 | V |  |

## 6.7 Timers

See General switching specifications.

## 6.8 Communication interfaces

## 6.8.1 USB electrical specifications

The USB electricals for the USB On-the-Go module conform to the standards documented by the Universal Serial Bus Implementers Forum. For the most up-to-date standards, visit http://www.usb.org.

## 6.8.2 USB DCD electrical specifications

## Table 35. USB DCD electrical specifications

| Symbol | Description | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - |
| VDP_SRC | USB_DP source voltage (up to 250 μA) | 0.5 | - | 0.7 | V |
| VLGC | Threshold voltage for logic high | 0.8 | - | 2.0 | V |
| IDP_SRC | USB_DP source current | 7 | 10 | 13 | μA |
| IDM_SINK | USB_DM sink current | 50 | 100 | 150 | μA |
| RDM_DWN | D- pulldown resistance for data pin contact detect | 14.25 | - | 24.8 | kΩ |
| VDAT_REF | Data detect voltage | 0.25 | 0.33 | 0.4 | V |

## 6.8.3 USB VREG electrical specifications

## Table 36. USB VREG electrical specifications

| Symbol | Description | Min. | Typ. 1 | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| VREGIN | Input supply voltage | 2.7 | - | 5.5 | V |  |
| IDDon | Quiescent current - Run mode, load current equal zero, input supply (VREGIN) > 3.6 V | - | 120 | 186 | μA |  |
| IDDstby | Quiescent current - Standby mode, load current equal zero | - | 1.1 | 10 | μA |  |
| IDDoff | Quiescent current - Shutdown mode · VREGIN = 5.0 V and temperature=25C · Across operating voltage and temperature | - - | 650 - | - 4 | nA μA |  |
| ILOADrun | Maximum load current - Run mode | - | - | 120 | mA |  |
| ILOADstby | Maximum load current - Standby mode | - | - | 1 | mA |  |
| VReg33out | Regulator output voltage - Input supply (VREGIN) > 3.6 V · Run mode · Standby mode | 3 2.1 | 3.3 2.8 | 3.6 3.6 | V V |  |
| VReg33out | Regulator output voltage - Input supply (VREGIN) < 3.6 V, pass-through mode | 2.1 | - | 3.6 | V | 2 |
| COUT | External output capacitor | 1.76 | 2.2 | 8.16 | μF |  |
| ESR | External output capacitor equivalent series resistance | 1 | - | 100 | mΩ |  |

Table continues on the next page...

## Table 36. USB VREG electrical specifications (continued)

| Symbol | Description | Min. | Typ. 1 | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| ILIM | Short circuit current | - | 290 | - | mA |  |

1. Typical values assume VREGIN = 5.0 V, Temp = 25 °C unless otherwise stated.

2. Operating in pass-through mode: regulator output voltage equal to the input voltage minus a drop proportional to ILoad.

## 6.8.4 CAN switching specifications

See General switching specifications.

## 6.8.5 DSPI switching specifications (limited voltage range)

The DMA Serial Peripheral Interface (DSPI) provides a synchronous serial bus with master and slave operations. Many of the transfer attributes are programmable. The tables below provide DSPI timing characteristics for classic SPI timing modes. Refer to the DSPI chapter of the Reference Manual for information on the modified transfer formats used for communicating with slower peripheral devices.

Table 37. Master mode DSPI timing (limited voltage range)

| Num | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
|  | Operating voltage | 2.7 | 3.6 | V |  |
|  | Frequency of operation | - | 25 | MHz |  |
| DS1 | DSPI_SCK output cycle time | 2 x tBUS | - | ns |  |
| DS2 | DSPI_SCK output high/low time | (tSCK/2) - 2 | (tSCK/2) + 2 | ns |  |
| DS3 | DSPI_PCSn valid to DSPI_SCK delay | (tBUS x 2) - 2 | - | ns | 1 |
| DS4 | DSPI_SCK to DSPI_PCSn invalid delay | (tBUS x 2) - 2 | - | ns | 2 |
| DS5 | DSPI_SCK to DSPI_SOUT valid | - | 8.5 | ns |  |
| DS6 | DSPI_SCK to DSPI_SOUT invalid | -2 | - | ns |  |
| DS7 | DSPI_SIN to DSPI_SCK input setup | 15 | - | ns |  |
| DS8 | DSPI_SCK to DSPI_SIN input hold | 0 | - | ns |  |

1. The delay is programmable in SPIx\_CTARn[PSSCK] and SPIx\_CTARn[CSSCK].
2. The delay is programmable in SPIx\_CTARn[PASC] and SPIx\_CTARn[ASC].

Figure 19. DSPI classic SPI timing - master mode

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_028.png)

Table 38. Slave mode DSPI timing (limited voltage range)

| Num | Description | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 2.7 | 3.6 | V |
|  | Frequency of operation |  | 12.5 | MHz |
| DS9 | DSPI_SCK input cycle time | 4 x tBUS | - | ns |
| DS10 | DSPI_SCK input high/low time | (tSCK/2) - 2 | (tSCK/2) + 2 | ns |
| DS11 | DSPI_SCK to DSPI_SOUT valid | - | 10 | ns |
| DS12 | DSPI_SCK to DSPI_SOUT invalid | 0 | - | ns |
| DS13 | DSPI_SIN to DSPI_SCK input setup | 2 | - | ns |
| DS14 | DSPI_SCK to DSPI_SIN input hold | 7 | - | ns |
| DS15 | DSPI_SS active to DSPI_SOUT driven | - | 14 | ns |
| DS16 | DSPI_SS inactive to DSPI_SOUT not driven | - | 14 | ns |

Figure 20. DSPI classic SPI timing - slave mode

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_029.png)

## 6.8.6 DSPI switching specifications (full voltage range)

The DMA Serial Peripheral Interface (DSPI) provides a synchronous serial bus with master and slave operations. Many of the transfer attributes are programmable. The tables below provides DSPI timing characteristics for classic SPI timing modes. Refer to the DSPI chapter of the Reference Manual for information on the modified transfer formats used for communicating with slower peripheral devices.

Table 39. Master mode DSPI timing (full voltage range)

| Num | Description | Min. | Max. | Unit | Notes |
| - | - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V | 1 |
|  | Frequency of operation | - | 12.5 | MHz |  |
| DS1 | DSPI_SCK output cycle time | 4 x tBUS | - | ns |  |
| DS2 | DSPI_SCK output high/low time | (tSCK/2) - 4 | (tSCK/2) + 4 | ns |  |
| DS3 | DSPI_PCSn valid to DSPI_SCK delay | (tBUS x 2) - 4 | - | ns | 2 |
| DS4 | DSPI_SCK to DSPI_PCSn invalid delay | (tBUS x 2) - 4 | - | ns | 3 |
| DS5 | DSPI_SCK to DSPI_SOUT valid | - | 10 | ns |  |
| DS6 | DSPI_SCK to DSPI_SOUT invalid | -4.5 | - | ns |  |
| DS7 | DSPI_SIN to DSPI_SCK input setup | 20.5 | - | ns |  |
| DS8 | DSPI_SCK to DSPI_SIN input hold | 0 | - | ns |  |

1. The DSPI module can operate across the entire operating voltage for the processor, but to run across the full voltage range the maximum frequency of operation is reduced.
2. The delay is programmable in SPIx\_CTARn[PSSCK] and SPIx\_CTARn[CSSCK].
3. The delay is programmable in SPIx\_CTARn[PASC] and SPIx\_CTARn[ASC].

Figure 21. DSPI classic SPI timing - master mode

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_030.png)

Table 40. Slave mode DSPI timing (full voltage range)

| Num | Description | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V |
|  | Frequency of operation | - | 6.25 | MHz |

Table continues on the next page...

Table 40. Slave mode DSPI timing (full voltage range) (continued)

| Num | Description | Min. | Max. | Unit |
| - | - | - | - | - |
| DS9 | DSPI_SCK input cycle time | 8 x tBUS | - | ns |
| DS10 | DSPI_SCK input high/low time | (tSCK/2) - 4 | (tSCK/2) + 4 | ns |
| DS11 | DSPI_SCK to DSPI_SOUT valid | - | 20 | ns |
| DS12 | DSPI_SCK to DSPI_SOUT invalid | 0 | - | ns |
| DS13 | DSPI_SIN to DSPI_SCK input setup | 2 | - | ns |
| DS14 | DSPI_SCK to DSPI_SIN input hold | 7 | - | ns |
| DS15 | DSPI_SS active to DSPI_SOUT driven | - | 19 | ns |
| DS16 | DSPI_SS inactive to DSPI_SOUT not driven | - | 19 | ns |

Figure 22. DSPI classic SPI timing - slave mode

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_031.png)

## 6.8.7 I 2 C switching specifications

See General switching specifications.

## 6.8.8 UART switching specifications

See General switching specifications.

## 6.8.9 I2S/SAI Switching Specifications

This section provides the AC timing for the I2S/SAI module in master mode (clocks are driven) and slave mode (clocks are input). All timing is given for noninverted serial clock polarity (TCR2[BCP] is 0, RCR2[BCP] is 0) and a noninverted frame sync (TCR4[FSP]

is 0, RCR4[FSP] is 0). If the polarity of the clock and/or the frame sync have been inverted, all the timing remains valid by inverting the bit clock signal (BCLK) and/or the frame sync (FS) signal shown in the following figures.

## 6.8.9.1 Normal Run, Wait and Stop mode performance over the full operating voltage range

This section provides the operating performance over the full operating voltage for the device in Normal Run, Wait and Stop modes.

Table 41. I2S/SAI master mode timing in Normal Run, Wait and Stop modes (full voltage range)

| Num. | Characteristic | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V |
| S1 | I2S_MCLK cycle time | 40 | - | ns |
| S2 | I2S_MCLK pulse width high/low | 45% | 55% | MCLK period |
| S3 | I2S_TX_BCLK/I2S_RX_BCLK cycle time (output) | 80 | - | ns |
| S4 | I2S_TX_BCLK/I2S_RX_BCLK pulse width high/low | 45% | 55% | BCLK period |
| S5 | I2S_TX_BCLK/I2S_RX_BCLK to I2S_TX_FS/ I2S_RX_FS output valid | - | 15 | ns |
| S6 | I2S_TX_BCLK/I2S_RX_BCLK to I2S_TX_FS/ I2S_RX_FS output invalid | -1.0 | - | ns |
| S7 | I2S_TX_BCLK to I2S_TXD valid | - | 15 | ns |
| S8 | I2S_TX_BCLK to I2S_TXD invalid | 0 | - | ns |
| S9 | I2S_RXD/I2S_RX_FS input setup before I2S_RX_BCLK | 20.5 | - | ns |
| S10 | I2S_RXD/I2S_RX_FS input hold after I2S_RX_BCLK | 0 | - | ns |

Figure 23. I2S/SAI timing - master modes

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_032.png)

Table 42. I2S/SAI slave mode timing in Normal Run, Wait and Stop modes (full voltage range)

| Num. | Characteristic | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V |
| S11 | I2S_TX_BCLK/I2S_RX_BCLK cycle time (input) | 80 | - | ns |
| S12 | I2S_TX_BCLK/I2S_RX_BCLK pulse width high/low (input) | 45% | 55% | MCLK period |
| S13 | I2S_TX_FS/I2S_RX_FS input setup before I2S_TX_BCLK/I2S_RX_BCLK | 5.8 | - | ns |
| S14 | I2S_TX_FS/I2S_RX_FS input hold after I2S_TX_BCLK/I2S_RX_BCLK | 2 | - | ns |
| S16 | I2S_TX_BCLK to I2S_TXD/I2S_TX_FS output invalid | 0 | - | ns |
| S17 | I2S_RXD setup before I2S_RX_BCLK | 5.8 | - | ns |
| S18 | I2S_RXD hold after I2S_RX_BCLK | 2 | - | ns |
| S19 | I2S_TX_FS input assertion to I2S_TXD output valid 1 | - | 25 | ns |

1. Applies to first bit in each frame and only if the TCR4[FSE] bit is clear

Figure 24. I2S/SAI timing - slave modes

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_033.png)

## 6.8.9.2 VLPR, VLPW, and VLPS mode performance over the full operating voltage range

This section provides the operating performance over the full operating voltage for the device in VLPR, VLPW, and VLPS modes.

Table 43. I2S/SAI master mode timing in VLPR, VLPW, and VLPS modes (full voltage range)

| Num. | Characteristic | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V |
| S1 | I2S_MCLK cycle time | 62.5 | - | ns |
| S2 | I2S_MCLK pulse width high/low | 45% | 55% | MCLK period |
| S3 | I2S_TX_BCLK/I2S_RX_BCLK cycle time (output) | 250 | - | ns |
| S4 | I2S_TX_BCLK/I2S_RX_BCLK pulse width high/low | 45% | 55% | BCLK period |
| S5 | I2S_TX_BCLK/I2S_RX_BCLK to I2S_TX_FS/ I2S_RX_FS output valid | - | 45 | ns |
| S6 | I2S_TX_BCLK/I2S_RX_BCLK to I2S_TX_FS/ I2S_RX_FS output invalid | 0 | - | ns |
| S7 | I2S_TX_BCLK to I2S_TXD valid | - | 45 | ns |
| S8 | I2S_TX_BCLK to I2S_TXD invalid | 0 | - | ns |
| S9 | I2S_RXD/I2S_RX_FS input setup before I2S_RX_BCLK | 53 | - | ns |
| S10 | I2S_RXD/I2S_RX_FS input hold after I2S_RX_BCLK | 0 | - | ns |

## Peripheral operating requirements and behaviors

Figure 25. I2S/SAI timing - master modes

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_032.png)

Table 44. I2S/SAI slave mode timing in VLPR, VLPW, and VLPS modes (full voltage range)

| Num. | Characteristic | Min. | Max. | Unit |
| - | - | - | - | - |
|  | Operating voltage | 1.71 | 3.6 | V |
| S11 | I2S_TX_BCLK/I2S_RX_BCLK cycle time (input) | 250 | - | ns |
| S12 | I2S_TX_BCLK/I2S_RX_BCLK pulse width high/low (input) | 45% | 55% | MCLK period |
| S13 | I2S_TX_FS/I2S_RX_FS input setup before I2S_TX_BCLK/I2S_RX_BCLK | 30 | - | ns |
| S14 | I2S_TX_FS/I2S_RX_FS input hold after I2S_TX_BCLK/I2S_RX_BCLK | 7.6 | - | ns |
| S15 | I2S_TX_BCLK to I2S_TXD/I2S_TX_FS output valid | - | 67 | ns |
| S16 | I2S_TX_BCLK to I2S_TXD/I2S_TX_FS output invalid | 0 | - | ns |
| S17 | I2S_RXD setup before I2S_RX_BCLK | 30 | - | ns |
| S18 | I2S_RXD hold after I2S_RX_BCLK | 6.5 | - | ns |
| S19 | I2S_TX_FS input assertion to I2S_TXD output valid 1 | - | 72 | ns |

1. Applies to first bit in each frame and only if the TCR4[FSE] bit is clear

Figure 26. I2S/SAI timing - slave modes

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_033.png)

## 6.9 Human-machine interfaces (HMI)

## 6.9.1 TSI electrical specifications

## Table 45. TSI electrical specifications

| Symbol | Description | Min. | Typ. | Max. | Unit | Notes |
| - | - | - | - | - | - | - |
| VDDTSI | Operating voltage | 1.71 | - | 3.6 | V |  |
| CELE | Target electrode capacitance range | 1 | 20 | 500 | pF | 1 |
| fREFmax | Reference oscillator frequency | - | 8 | 15 | MHz | 2, 3 |
| fELEmax | Electrode oscillator frequency | - | 1 | 1.8 | MHz | 2, 4 |
| CREF | Internal reference capacitor | - | 1 | - | pF |  |
| VDELTA | Oscillator delta voltage | - | 500 | - | mV | 2, 5 |
| IREF | Reference oscillator current source base current · 2 μA setting (REFCHRG = 0) · 32 μA setting (REFCHRG = 15) | - - | 2 36 | 3 50 | μA | 2, 6 |
| IELE | Electrode oscillator current source base current · 2 μA setting (EXTCHRG = 0) · 32 μA setting (EXTCHRG = 15) | - - | 2 36 | 3 50 | μA | 2, 7 |
| Pres5 | Electrode capacitance measurement precision | - | 8.3333 | 38400 | fF/count | 8 |
| Pres20 | Electrode capacitance measurement precision | - | 8.3333 | 38400 | fF/count | 9 |
| Pres100 | Electrode capacitance measurement precision | - | 8.3333 | 38400 | fF/count | 10 |
| MaxSens | Maximum sensitivity | 0.008 | 1.46 | - | fF/count | 11 |
| Res | Resolution | - | - | 16 | bits |  |
| TCon20 | Response time @ 20 pF | 8 | 15 | 25 | μs | 12 |
| ITSI_RUN | Current added in run mode | - | 55 | - | μA |  |
| ITSI_LP | Low power mode current adder | - | 1.3 | 2.5 | μA | 13 |

## Dimensions

1. The TSI module is functional with capacitance values outside this range. However, optimal performance is not guaranteed.
2. Fixed external capacitance of 20 pF.
3. REFCHRG = 2, EXTCHRG=0.
4. REFCHRG = 0, EXTCHRG = 10.
5. VDD = 3.0 V.
6. The programmable current source value is generated by multiplying the SCANC[REFCHRG] value and the base current.
7. The programmable current source value is generated by multiplying the SCANC[EXTCHRG] value and the base current.
8. Measured with a 5 pF electrode, reference oscillator frequency of 10 MHz, PS = 128, NSCN = 8; Iext = 16.
9. Measured with a 20 pF electrode, reference oscillator frequency of 10 MHz, PS = 128, NSCN = 2; Iext = 16.
10. Measured with a 20 pF electrode, reference oscillator frequency of 10 MHz, PS = 16, NSCN = 3; Iext = 16.
11. Sensitivity defines the minimum capacitance change when a single count from the TSI module changes. Sensitivity depends on the configuration used. The documented values are provided as examples calculated for a specific configuration of operating conditions using the following equation: (Cref * Iext)/( Iref * PS * NSCN)

The typical value is calculated with the following configuration:

Iext = 6 μA (EXTCHRG = 2), PS = 128, NSCN = 2, Iref = 16 μA (REFCHRG = 7), Cref = 1.0 pF

The minimum value is calculated with the following configuration:

Iext = 2 μA (EXTCHRG = 0), PS = 128, NSCN = 32, Iref = 32 μA (REFCHRG = 15), Cref = 0.5 pF

The highest possible sensitivity is the minimum value because it represents the smallest possible capacitance that can be measured by a single count.

12. Time to do one complete measurement of the electrode. Sensitivity resolution of 0.0133 pF, PS = 0, NSCN = 0, 1 electrode, EXTCHRG = 7.
13. REFCHRG=0, EXTCHRG=4, PS=7, NSCN=0F, LPSCNITV=F, LPO is selected (1 kHz), and fixed external capacitance of 20 pF. Data is captured with an average of 7 periods window.

## 7 Dimensions

## 7.1 Obtaining package dimensions

Package dimensions are provided in package drawings.

To find a package drawing, go to www.freescale.com and perform a keyword search for the drawing's document number:

| If you want the drawing for this package | Then use this document number |
| - | - |
| 64-pin LQFP | 98ASS23234W |

## 8 Pinout

## 8.1 K20 Signal Multiplexing and Pin Assignments

The following table shows the signals available on each pin and the locations of these pins on the devices supported by this document. The Port Control Module is responsible for selecting which ALT functionality is available on each pin.

| 64 LQFP _QFN | Pin Name | Default | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 ALT6 | ALT7 | EzPort |
| - | - | - | - | - | - | - | - | - | - | - |
| 1 | PTE0 | ADC1_SE4a | ADC1_SE4a | PTE0 |  | UART1_TX |  | I2C1_SDA | RTC_CLKOUT |  |
| 2 | PTE1/ LLWU_P0 | ADC1_SE5a | ADC1_SE5a | PTE1/ LLWU_P0 |  | UART1_RX |  | I2C1_SCL |  |  |
| 3 | VDD | VDD | VDD |  |  |  |  |  |  |  |
| 4 | VSS | VSS | VSS |  |  |  |  |  |  |  |
| 5 | USB0_DP | USB0_DP | USB0_DP |  |  |  |  |  |  |  |
| 6 | USB0_DM | USB0_DM | USB0_DM |  |  |  |  |  |  |  |
| 7 | VOUT33 | VOUT33 | VOUT33 |  |  |  |  |  |  |  |
| 8 | VREGIN | VREGIN | VREGIN |  |  |  |  |  |  |  |
| 9 | PGA0_DP/ ADC0_DP0/ ADC1_DP3 | PGA0_DP/ ADC0_DP0/ ADC1_DP3 | PGA0_DP/ ADC0_DP0/ ADC1_DP3 |  |  |  |  |  |  |  |
| 10 | PGA0_DM/ ADC0_DM0/ ADC1_DM3 | PGA0_DM/ ADC0_DM0/ ADC1_DM3 | PGA0_DM/ ADC0_DM0/ ADC1_DM3 |  |  |  |  |  |  |  |
| 11 | PGA1_DP/ ADC1_DP0/ ADC0_DP3 | PGA1_DP/ ADC1_DP0/ ADC0_DP3 | PGA1_DP/ ADC1_DP0/ ADC0_DP3 |  |  |  |  |  |  |  |
| 12 | PGA1_DM/ ADC1_DM0/ ADC0_DM3 | PGA1_DM/ ADC1_DM0/ ADC0_DM3 | PGA1_DM/ ADC1_DM0/ ADC0_DM3 |  |  |  |  |  |  |  |
| 13 | VDDA | VDDA | VDDA |  |  |  |  |  |  |  |
| 14 | VREFH | VREFH | VREFH |  |  |  |  |  |  |  |
| 15 | VREFL | VREFL | VREFL |  |  |  |  |  |  |  |
| 16 | VSSA | VSSA | VSSA |  |  |  |  |  |  |  |
| 17 | VREF_OUT/ CMP1_IN5/ CMP0_IN5/ ADC1_SE18 | VREF_OUT/ CMP1_IN5/ CMP0_IN5/ ADC1_SE18 | VREF_OUT/ CMP1_IN5/ CMP0_IN5/ ADC1_SE18 |  |  |  |  |  |  |  |
| 18 | DAC0_OUT/ CMP1_IN3/ ADC0_SE23 | DAC0_OUT/ CMP1_IN3/ ADC0_SE23 | DAC0_OUT/ CMP1_IN3/ ADC0_SE23 |  |  |  |  |  |  |  |
| 19 | XTAL32 | XTAL32 | XTAL32 |  |  |  |  |  |  |  |
| 20 | EXTAL32 | EXTAL32 | EXTAL32 |  |  |  |  |  |  |  |
| 21 | VBAT | VBAT | VBAT |  |  |  |  |  |  |  |
| 22 | PTA0 | JTAG_TCLK/ SWD_CLK/ EZP_CLK | TSI0_CH1 | PTA0 | UART0_CTS_ b/ UART0_COL_b | FTM0_CH5 |  |  | JTAG_TCLK/ SWD_CLK | EZP_CLK |
| 23 | PTA1 | JTAG_TDI/ EZP_DI | TSI0_CH2 | PTA1 | UART0_RX | FTM0_CH6 |  |  | JTAG_TDI | EZP_DI |

## Pinout

| 64 LQFP _QFN | Pin Name | Default | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | EzPort |
| - | - | - | - | - | - | - | - | - | - | - | - |
| 24 | PTA2 | JTAG_TDO/ TRACE_SWO/ EZP_DO | TSI0_CH3 | PTA2 | UART0_TX | FTM0_CH7 |  |  |  | JTAG_TDO/ TRACE_SWO | EZP_DO |
| 25 | PTA3 | JTAG_TMS/ SWD_DIO | TSI0_CH4 | PTA3 | UART0_RTS_b | FTM0_CH0 |  |  |  | JTAG_TMS/ SWD_DIO |  |
| 26 | PTA4/ LLWU_P3 | NMI_b/ EZP_CS_b | TSI0_CH5 | PTA4/ LLWU_P3 |  | FTM0_CH1 |  |  |  | NMI_b | EZP_CS_b |
| 27 | PTA5 | DISABLED |  | PTA5 | USB_CLKIN | FTM0_CH2 |  | CMP2_OUT | I2S0_TX_BCLK | JTAG_TRST_b |  |
| 28 | PTA12 | CMP2_IN0 | CMP2_IN0 | PTA12 | CAN0_TX | FTM1_CH0 |  |  | I2S0_TXD0 | FTM1_QD_ PHA |  |
| 29 | PTA13/ LLWU_P4 | CMP2_IN1 | CMP2_IN1 | PTA13/ LLWU_P4 | CAN0_RX | FTM1_CH1 |  |  | I2S0_TX_FS | FTM1_QD_ PHB |  |
| 30 | VDD | VDD | VDD |  |  |  |  |  |  |  |  |
| 31 | VSS | VSS | VSS |  |  |  |  |  |  |  |  |
| 32 | PTA18 | EXTAL0 | EXTAL0 | PTA18 |  | FTM0_FLT2 | FTM_CLKIN0 |  |  |  |  |
| 33 | PTA19 | XTAL0 | XTAL0 | PTA19 |  | FTM1_FLT0 | FTM_CLKIN1 |  | LPTMR0_ALT1 |  |  |
| 34 | RESET_b | RESET_b | RESET_b |  |  |  |  |  |  |  |  |
| 35 | PTB0/ LLWU_P5 | ADC0_SE8/ ADC1_SE8/ TSI0_CH0 | ADC0_SE8/ ADC1_SE8/ TSI0_CH0 | PTB0/ LLWU_P5 | I2C0_SCL | FTM1_CH0 |  |  | FTM1_QD_ PHA |  |  |
| 36 | PTB1 | ADC0_SE9/ ADC1_SE9/ TSI0_CH6 | ADC0_SE9/ ADC1_SE9/ TSI0_CH6 | PTB1 | I2C0_SDA | FTM1_CH1 |  |  | FTM1_QD_ PHB |  |  |
| 37 | PTB2 | ADC0_SE12/ TSI0_CH7 | ADC0_SE12/ TSI0_CH7 | PTB2 | I2C0_SCL | UART0_RTS_b |  |  | FTM0_FLT3 |  |  |
| 38 | PTB3 | ADC0_SE13/ TSI0_CH8 | ADC0_SE13/ TSI0_CH8 | PTB3 | I2C0_SDA | UART0_CTS_ b/ UART0_COL_b |  |  | FTM0_FLT0 |  |  |
| 39 | PTB16 | TSI0_CH9 | TSI0_CH9 | PTB16 |  | UART0_RX |  | FB_AD17 | EWM_IN |  |  |
| 40 | PTB17 | TSI0_CH10 | TSI0_CH10 | PTB17 |  | UART0_TX |  | FB_AD16 | EWM_OUT_b |  |  |
| 41 | PTB18 | TSI0_CH11 | TSI0_CH11 | PTB18 | CAN0_TX | FTM2_CH0 | I2S0_TX_BCLK | FB_AD15 | FTM2_QD_ PHA |  |  |
| 42 | PTB19 | TSI0_CH12 | TSI0_CH12 | PTB19 | CAN0_RX | FTM2_CH1 | I2S0_TX_FS | FB_OE_b | FTM2_QD_ PHB |  |  |
| 43 | PTC0 | ADC0_SE14/ TSI0_CH13 | ADC0_SE14/ TSI0_CH13 | PTC0 | SPI0_PCS4 | PDB0_EXTRG |  | FB_AD14 | I2S0_TXD1 |  |  |
| 44 | PTC1/ LLWU_P6 | ADC0_SE15/ TSI0_CH14 | ADC0_SE15/ TSI0_CH14 | PTC1/ LLWU_P6 | SPI0_PCS3 | UART1_RTS_b | FTM0_CH0 | FB_AD13 | I2S0_TXD0 |  |  |
| 45 | PTC2 | ADC0_SE4b/ CMP1_IN0/ TSI0_CH15 | ADC0_SE4b/ CMP1_IN0/ TSI0_CH15 | PTC2 | SPI0_PCS2 | UART1_CTS_b | FTM0_CH1 | FB_AD12 | I2S0_TX_FS |  |  |
| 46 | PTC3/ LLWU_P7 | CMP1_IN1 | CMP1_IN1 | PTC3/ LLWU_P7 | SPI0_PCS1 | UART1_RX | FTM0_CH2 | CLKOUT | I2S0_TX_BCLK |  |  |
| 47 | VSS | VSS | VSS |  |  |  |  |  |  |  |  |
| 48 | VDD | VDD | VDD |  |  |  |  |  |  |  |  |

## Pinout

| 64 LQFP _QFN | Pin Name | Default | ALT0 | ALT1 | ALT2 | ALT3 | ALT4 | ALT5 | ALT6 | ALT7 | EzPort |
| - | - | - | - | - | - | - | - | - | - | - | - |
| 49 | PTC4/ LLWU_P8 | DISABLED |  | PTC4/ LLWU_P8 | SPI0_PCS0 | UART1_TX | FTM0_CH3 | FB_AD11 | CMP1_OUT |  |  |
| 50 | PTC5/ LLWU_P9 | DISABLED |  | PTC5/ LLWU_P9 | SPI0_SCK | LPTMR0_ALT2 | I2S0_RXD0 | FB_AD10 | CMP0_OUT |  |  |
| 51 | PTC6/ LLWU_P10 | CMP0_IN0 | CMP0_IN0 | PTC6/ LLWU_P10 | SPI0_SOUT | PDB0_EXTRG | I2S0_RX_BCLK | FB_AD9 | I2S0_MCLK |  |  |
| 52 | PTC7 | CMP0_IN1 | CMP0_IN1 | PTC7 | SPI0_SIN | USB_SOF_ OUT | I2S0_RX_FS | FB_AD8 |  |  |  |
| 53 | PTC8 | ADC1_SE4b/ CMP0_IN2 | ADC1_SE4b/ CMP0_IN2 | PTC8 |  |  | I2S0_MCLK | FB_AD7 |  |  |  |
| 54 | PTC9 | ADC1_SE5b/ CMP0_IN3 | ADC1_SE5b/ CMP0_IN3 | PTC9 |  |  | I2S0_RX_BCLK | FB_AD6 | FTM2_FLT0 |  |  |
| 55 | PTC10 | ADC1_SE6b | ADC1_SE6b | PTC10 | I2C1_SCL |  | I2S0_RX_FS | FB_AD5 |  |  |  |
| 56 | PTC11/ LLWU_P11 | ADC1_SE7b | ADC1_SE7b | PTC11/ LLWU_P11 | I2C1_SDA |  | I2S0_RXD1 | FB_RW_b |  |  |  |
| 57 | PTD0/ LLWU_P12 | DISABLED |  | PTD0/ LLWU_P12 | SPI0_PCS0 | UART2_RTS_b |  | FB_ALE/ FB_CS1_b/ FB_TS_b |  |  |  |
| 58 | PTD1 | ADC0_SE5b | ADC0_SE5b | PTD1 | SPI0_SCK | UART2_CTS_b |  | FB_CS0_b |  |  |  |
| 59 | PTD2/ LLWU_P13 | DISABLED |  | PTD2/ LLWU_P13 | SPI0_SOUT | UART2_RX |  | FB_AD4 |  |  |  |
| 60 | PTD3 | DISABLED |  | PTD3 | SPI0_SIN | UART2_TX |  | FB_AD3 |  |  |  |
| 61 | PTD4/ LLWU_P14 | DISABLED |  | PTD4/ LLWU_P14 | SPI0_PCS1 | UART0_RTS_b | FTM0_CH4 | FB_AD2 | EWM_IN |  |  |
| 62 | PTD5 | ADC0_SE6b | ADC0_SE6b | PTD5 | SPI0_PCS2 | UART0_CTS_ b/ UART0_COL_b | FTM0_CH5 | FB_AD1 | EWM_OUT_b |  |  |
| 63 | PTD6/ LLWU_P15 | ADC0_SE7b | ADC0_SE7b | PTD6/ LLWU_P15 | SPI0_PCS3 | UART0_RX | FTM0_CH6 | FB_AD0 | FTM0_FLT0 |  |  |
| 64 | PTD7 | DISABLED |  | PTD7 | CMT_IRO | UART0_TX | FTM0_CH7 |  | FTM0_FLT1 |  |  |

## 8.2 K20 Pinouts

The below figure shows the pinout diagram for the devices supported by this document.

Many signals may be multiplexed onto a single pin. To determine what signals can be used on which pin, see the previous section.

## Revision History

Figure 27. K20 64 LQFP/QFN Pinout Diagram

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_034.png)

## 9 Revision History

The following table provides a revision history for this document.

## Table 46. Revision History

| Rev. No. | Date | Substantial Changes |
| - | - | - |
| 1 | 3/2012 | Initial public release |
| 2 | 4/2012 | · Replaced TBDs throughout. · Updated "Power consumption operating behaviors" table. · Updated "ADC electrical specifications" section. · Updated "VREF full-range operating behaviors" table. · Updated "I2S/SAI Switching Specifications" section. · Updated "TSI electrical specifications" table. |
| 3 | 11/2012 | · Updated orderable part numbers. · Updated the maximum input voltage (VADIN) specification in the "16-bit ADC operating conditions" section. · Updated the maximum IDDstby specification in the "USB VREG electrical specifications" section. |

## How to Reach Us:

## Home Page:

www.freescale.com

## Web Support:

http://www.freescale.com/support

## USA/Europe or Locations Not Listed:

Freescale Semiconductor Technical Information Center, EL516 2100 East Elliot Road Tempe, Arizona 85284 +1-800-521-6274 or +1-480-768-2130 www.freescale.com/support

## Europe, Middle East, and Africa:

Freescale Halbleiter Deutschland GmbH Technical Information Center Schatzbogen 7 81829 Muenchen, Germany +44 1296 380 456 (English) +46 8 52200080 (English) +49 89 92103 559 (German) +33 1 69 35 48 48 (French) www.freescale.com/support

## Japan:

Freescale Semiconductor Japan Ltd. Headquarters ARCO Tower 15F 1-8-1, Shimo-Meguro, Meguro-ku, Tokyo 153-0064 Japan 0120 191014 or +81 3 5437 9125 support.japan@freescale.com

## Asia/Pacific:

Freescale Semiconductor China Ltd. Exchange Building 23F No. 118 Jianguo Road Chaoyang District Beijing 100022 China +86 10 5879 8000 support.asia@freescale.com

Information in this document is provided solely to enable system and software implementers to use Freescale Semiconductors products. There are no express or implied copyright licenses granted hereunder to design or fabricate any integrated circuits or integrated circuits based on the information in this document.

Freescale Semiconductor reserves the right to make changes without further notice to any products herein. Freescale Semiconductor makes no warranty, representation, or guarantee regarding the suitability of its products for any particular purpose, nor does Freescale Semiconductor assume any liability arising out of the application or use of any product or circuit, and specifically disclaims any liability, including without limitation consequential or incidental damages. "Typical" parameters that may be provided in Freescale Semiconductor data sheets and/or specifications can and do vary in different applications and actual performance may vary over time. All operating parameters, including "Typicals", must be validated for each customer application by customer's technical experts. Freescale Semiconductor does not convey any license under its patent rights nor the rights of others. Freescale Semiconductor products are not designed, intended, or authorized for use as components in systems intended for surgical implant into the body, or other applications intended to support or sustain life, or for any other application in which failure of the Freescale Semiconductor product could create a situation where personal injury or death may occur. Should Buyer purchase or use Freescale Semiconductor products for any such unintended or unauthorized application, Buyer shall indemnify Freescale Semiconductor and its officers, employees, subsidiaries, affiliates, and distributors harmless against all claims, costs, damages, and expenses, and reasonable attorney fees arising out of, directly or indirectly, any claim of personal injury or death associated with such unintended or unauthorized use, even if such claims alleges that Freescale Semiconductor was negligent regarding the design or manufacture of the part.

RoHS-compliant and/or Pb-free versions of Freescale products have the functionality and electrical characteristics as their non-RoHS-complaint and/or non-Pb-free counterparts. For further information, see http://www.freescale.com or contact your Freescale sales representative.

For information on Freescale's Environmental Products program, go to http://www.freescale.com/epp.

Freescale™ and the Freescale logo are trademarks of Freescale Semiconductor, Inc. All other product or service names are the property of their respective owners.

© 2012 Freescale Semiconductor, Inc.

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_035.png)

![Image](K20P64M72SF1%20teensy3.1%20datasheet_files/img_036.png)

freescale
<!-- Converted from TJA1057 Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

\_

## TJA1057

## High-speed CAN transceiver

Rev. 8.1 - 2 March 2026

Product data sheet

![Image](TJA1057%20Datasheet_files/img_001.png)

## 1 General description

The TJA1057 is part of the Mantis family of high-speed CAN transceivers. It provides an interface between a Controller Area Network (CAN) protocol controller and the physical two-wire CAN bus. The transceiver is designed for high-speed CAN applications in the automotive industry, providing the differential transmit and receive capability to (a microcontroller with) a CAN protocol controller.

The TJA1057 offers a feature set optimized for 12 V automotive applications, with significant improvements over first- and second-generation CAN transceivers from NXP, such as the TJA1050, and excellent electromagnetic compatibility (EMC) performance. The TJA1057 also displays ideal passive behavior to the CAN bus when the supply voltage is off.

Variants with a VIO pin can be interfaced directly with microcontrollers with supply voltages from 3.3 V to 5 V.

The TJA1057 implements the CAN physical layer as defined in ISO 11898-2:2024 third edition and SAE J2284-1 to SAE J2284-5. The TJA1057T is specified for data rates up to 1 Mbit/s. Additional timing parameters defining loop delay symmetry are specified for the other variants. This implementation enables reliable communication in the CAN FD fast phase at data rates up to 5 Mbit/s. The TJA1057B and TJA1057C feature shorter propagation delay, supporting larger network topologies.

These features make the TJA1057 an excellent choice for HS-CAN networks that only require basic CAN functionality.

## 2 Features and benefits

## 2.1 General

- Fully ISO 11898-2:2024, SAE J2284-1 to SAE J2284-5 and SAE J1939-14 compliant 1
- Optimized for use in 12 V automotive systems
- Low electromagnetic emission and high electromagnetic immunity, according to EMC standards IEC TS62228 and SAE J2962-2:2019 2
- AEC-Q100 qualified
- Dark green product (halogen free and Restriction of Hazardous Substances (RoHS) compliant)
- Shorter propagation delay on the TJA1057B and TJA1057C variants supports larger network topologies (see Table 8)
- Variants with a VIO pin allow for direct interfacing with 3.3 V to 5 V microcontrollers. Variants without a VIO pin can interface with 3.3 V and 5 V-supplied microcontrollers, provided the microcontroller I/Os are 5 V tolerant.

1 Compliant with the exception of parameters V\_CM(STEP) and V\_CM(PP); intended as an indication of emission performance. Note that the device fullfills the EMC requirements, as evidenced through IBEE reports available on request.

2 Verified by an external test house for TJA1057B/C.

![Image](TJA1057%20Datasheet_files/img_002.png)

[NXO](https://www.nxp.com/)

![Image](TJA1057%20Datasheet_files/img_003.png)

## TJA1057

High-speed CAN transceiver

- Both VIO and non-VIO variants are available in SO8 and leadless HVSON8 (3.0 mm × 3.0 mm) packages; HVSON8 with improved Automated Optical Inspection (AOI) capability.

## 2.2 Predictable and fail-safe behavior

- Functional behavior predictable under all supply conditions
- Transceiver disengages from the bus (high-ohmic) when the supply voltage drops below the undervoltage threshold
- Transmit Data (TXD) dominant time-out function
- Internal biasing of TXD and S input pins

## 2.3 Protection

- High ESD handling capability on the bus pins (8 kV IEC and HBM)
- Bus pins protected against transients in automotive environments
- Undervoltage detection on pins VCC and VIO
- Thermally protected

## 2.4 TJA1057 CAN FD (applicable to all product variants except TJA1057T)

- Timing guaranteed for data rates up to 5 Mbit/s

## 3 Quick reference data

## Table 1. Quick reference data

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - |
| VCC | supply voltage |  | 4.5 | - | 5.5 | V |
| VIO | supply voltage on pin VIO |  | 2.91 | - | 5.5 | V |
| Vuvd(VCC) | undervoltage detection voltage on pin VCC |  | 3.5 | 4 | 4.3 | V |
| Vuvd(VIO) | undervoltage detection voltage on pin VIO |  | 2.1 | - | 2.8 | V |
| ICC | supply current | Silent mode | 0.1 | - | 1.2 | mA |
| ICC |  | Normal mode; bus recessive | 2 | 5 | 10 | mA |
| ICC |  | Normal mode; bus dominant | 20 | 45 | 70 | mA |
| IIO | supply current on pin VIO | Silent mode | - | 3 | 16 | μA |
| IIO |  | Normal mode |  |  |  |  |
| IIO |  | recessive; VTXD = VIO | - | 7 | 30 | μA |
| IIO |  | dominant; VTXD = 0 V | - | 110 | 320 | μA |
| VESD | electrostatic discharge voltage | IEC 61000-4-2 at pins CANH and CANL | -8 | - | +8 | kV |
| VCANH | voltage on pin CANH | limiting value according to IEC60134 | -42 | - | +42 | V |
| VCANL | voltage on pin CANL | limiting value according to IEC60134 | -42 | - | +42 | V |
| Tvj | virtual junction temperature |  | -40 | - | +150 | °C |

![Image](TJA1057%20Datasheet_files/img_004.png)

## 4 Ordering information

High-speed CAN transceiver

Table 2. Ordering information

| Type number [1] | Package - Name | Package - Description | Package - Version |
| - | - | - | - |
| TJA1057T TJA1057BT TJA1057CT TJA1057GT TJA1057GT/3 | SO8 | plastic small outline package; 8 leads; body width 3.9 mm | SOT96-1 |
| TJA1057BTK TJA1057CTK TJA1057GTK TJA1057GTK/3 | HVSON8 | plastic thermal enhanced very thin small outline package; no leads; 8 terminals; body 3 ⨯ 3 ⨯ 0.85 mm | SOT782-1 |

[1] TJA1057GT(K)/3 and TJA1057BT(K) with VIO pin; all variants other than TJA1057T support CAN FD.

![Image](TJA1057%20Datasheet_files/img_005.png)

## 5 Block diagram

High-speed CAN transceiver

![Image](TJA1057%20Datasheet_files/img_006.png)

1. Pin 5 is not connected in non-VIO product variants.
2. VIO = VCC in non-VIO product variants.

Figure 1. Block diagram

![Image](TJA1057%20Datasheet_files/img_004.png)

## 6 Pinning information

High-speed CAN transceiver

## 6.1 Pinning

![Image](TJA1057%20Datasheet_files/img_007.png)

## 6.2 Pin description

Table 3. Pin description

| Symbol | Pin | Type [1] | Description |
| - | - | - | - |
| TXD | 1 | I | transmit data input |
| GND [2] | 2 | G | ground |
| VCC | 3 | P | supply voltage |
| RXD | 4 | O | receive data output; reads out data from the bus lines |
| n.c. | 5 | - | not connected in TJA1057T, TJA1057GT, TJA1057CT, TJA1057GTK and TJA1057CTK |
| VIO | 5 | P | supply voltage for I/O level adapter in TJA1057GT(K)/3 and TJA1057BT(K) |
| CANL | 6 | AIO | LOW-level CAN bus line |
| CANH | 7 | AIO | HIGH-level CAN bus line |
| S | 8 | I | Silent mode control input |

[1] I: digital input; O: digital output; AIO: analog input/output; P: power supply; G: ground.

[2] HVSON8 package die supply ground is connected to both the GND pin and the exposed center pad. The GND pin must be soldered to board ground. For enhanced thermal and electrical performance, it is recommended that the exposed center pad also be soldered to board ground.

![Image](TJA1057%20Datasheet_files/img_008.png)

## 7 Functional description

High-speed CAN transceiver

## 7.1 Operating modes

The TJA1057 supports two operating modes, Normal and Silent. The operating mode is selected via pin S. See Table 4 for a description of the operating modes under normal supply conditions.

Table 4. Operating modes

| Mode | Inputs - Pin S | Inputs - Pin TXD | Outputs - CAN driver | Outputs - Pin RXD |
| - | - | - | - | - |
| Normal | LOW | LOW | dominant | LOW |
| Normal |  | HIGH | recessive | LOW when bus dominant |
| Normal |  |  |  | HIGH when bus recessive |
| Silent | HIGH | x [1] | biased to recessive | LOW when bus dominant |
| Silent |  |  |  | HIGH when bus recessive |

- [1] 'x' = don't care.

## 7.1.1 Normal mode

A LOW level on pin S selects Normal mode. In this mode, the transceiver can transmit and receive data via the bus lines, CANH and CANL (see Figure 1 for the block diagram). The differential receiver converts the analog data on the bus lines into digital data which is output on pin RXD. The slopes of the output signals on the bus lines are controlled internally and are optimized in a way that guarantees the lowest possible EME.

## 7.1.2 Silent mode

A HIGH level on pin S selects Silent mode. The transmitter is disabled in Silent mode, releasing the bus pins to recessive state. All other IC functions, including the receiver, continue to operate as in Normal mode. Silent mode can be used to prevent a faulty CAN controller disrupting all network communications.

## 7.2 Fail-safe features

## 7.2.1 TXD dominant time-out function

A 'TXD dominant time-out' timer is started when pin TXD is set LOW. If the LOW state on this pin persists for longer than tto(dom)TXD, the transmitter is disabled, releasing the bus lines to recessive state. This function prevents a hardware and/or software application failure from driving the bus lines to a permanent dominant state (blocking all network communications). The TXD dominant time-out timer is reset when pin TXD is set HIGH.

## 7.2.2 Internal biasing of TXD and S input pins

Pins TXD and S have internal pull-ups to VCC (or VIO in variants with a VIO pin) to ensure a safe, defined state in case one or both of these pins are left floating. Pull-up currents flow in these pins in all states; both pins should be held HIGH in Silent mode to minimize supply current.

![Image](TJA1057%20Datasheet_files/img_009.png)

High-speed CAN transceiver

## 7.2.3 Undervoltage detection on pins VCC and VIO (TJA1057GT(K)/3 and TJA1057BT(K) variants)

If VCC or VIO drops below the undervoltage detection level, Vuvd(VCC)/Vuvd(VIO), the transceiver switches off and disengages from the bus (zero load; bus pins floating) until the supply voltage has recovered. The output drivers are enabled once both VCC and VIO are again within their operating ranges and TXD has been reset to HIGH.

## 7.2.4 Overtemperature protection

The output drivers are protected against overtemperature conditions. If the virtual junction temperature exceeds the shutdown junction temperature, Tj(sd), both output drivers are disabled. When the virtual junction temperature drops below Tj(sd) again, the output drivers recover once TXD has been reset to HIGH (waiting for TXD to go HIGH prevents output driver oscillation due to small variations in temperature).

## 7.2.5 VIO supply pin (TJA1057GT(K)/3 and TJA1057BT(K) variants)

Pin VIO should be connected to the microcontroller supply voltage (see Figure 5). This will adjust the signal levels on pins TXD, RXD and S to the I/O levels of the microcontroller.

For versions of the TJA1057 without a VIO pin, the VIO input is internally connected to VCC. The signal levels on pins TXD, RXD and S are set to levels compatible with 5 V microcontrollers. This allows the device to interface with both 3.3 V and 5 V-supplied microcontrollers, provided the microcontroller I/Os are 5 V tolerant.

![Image](TJA1057%20Datasheet_files/img_005.png)

## 8 Limiting values

High-speed CAN transceiver High-speed CAN transceiver

In accordance with the Absolute Maximum Rating System (IEC 60134); all voltages are referenced to ground. Table 5. Limiting values

| Symbol | Parameter | Conditions |  | Min | Max | Unit |
| - | - | - | - | - | - | - |
| Vx | voltage on pin x [1] | on pins CANH, CANL |  | -42 | +42 | V |
|  |  | on pins VCC, VIO |  | -0.3 | +7 | V |
|  |  | on any other pin | [2] | -0.3 | VIO [3] + 0.3 | V |
| V(CANH-CANL) | voltage between pin CANH and pin CANL |  |  | -27 | +27 | V |
| Vtrt | transient voltage | on pins CANH, CANL | [4] |  |  |  |
|  |  | pulse 1 |  | -100 | - | V |
|  |  | pulse 2a |  | - | 75 | V |
|  |  | pulse 3a |  | -150 | - | V |
|  |  | pulse 3b |  | - | 100 | V |
| VESD | electrostatic discharge voltage | IEC 61000-4-2 (150 pF, 330 Ω discharge circuit) | [5] |  |  |  |
|  |  | on pins CANH and CANL |  | -8 | +8 | kV |
|  |  | SAE J2962-2:2019 (330 pF, 2kΩ) on pins CANH, CANL | [6] |  |  |  |
|  |  | powered air discharge |  | -15 | +15 | kV |
|  |  | powered contact discharge |  | -8 | +8 | kV |
|  |  | Human Body Model (HBM) |  |  |  |  |
|  |  | on any pin | [7] | -4 | +4 | kV |
|  |  | on pins CANH and CANL | [8] | -8 | +8 | kV |
|  |  | Machine Model (MM); 200 pF, 0.75 μH, 10 Ω | [9] |  |  |  |
|  |  | on any pin |  | -200 | +200 | V |
|  |  | Charged Device Model (CDM) | [10] |  |  |  |
|  |  | on corner pins |  | -750 | +750 | V |
|  |  | on any other pin |  | -500 | +500 | V |
| Tvj | virtual junction temperature |  | [11] | -40 | +150 | °C |
| Tstg | storage temperature |  | [12] | -55 | +150 | °C |

[1] The device can sustain voltages up to the specified values over the product lifetime, provided applied voltages (including transients) never exceed these values.

[2] Maximum voltage should never exceed 7 V.

[3] VIO + 0.3 = VCC + 0.3 in the non-VIO product variants.

[4] Verified by an external test house according to IEC TS 62228, Section 4.2.4; parameters for standard pulses defined in ISO 7637.

[5] Verified by an external test house according to IEC TS 62228, Section 4.3.

[6] Verified by an external test house according to ISO 10605 for TJA1057B/C.

[7] According to AEC-Q100-002.

[8] Pins stressed to reference group containing all ground and supply pins, emulating the application circuits (Figure 4 and Figure 5). HBM pulse as specified in AEC-Q100-002 used.

[9] According to AEC-Q100-003.

[10] According to AEC-Q100-011.

![Image](TJA1057%20Datasheet_files/img_003.png)

[11] In accordance with IEC 60747-1. An alternative definition of virtual junction temperature is: Tvj = Tamb + P ⨯ Rth(vj-a), where Rth(vj-a) is a fixed value to be used for the calculation of Tvj. The rating for Tvj limits the allowable combinations of power dissipation (P) and ambient temperature (Tamb).

[12] Tstg in application according to IEC61360-4. For component transport and storage conditions, see instead IEC61760-2.

## 9 Thermal characteristics

Table 6. Thermal characteristics

Value determined for free convection conditions on a JEDEC 2S2P board.

| Symbol | Parameter | Conditions [1] | Typ | Unit |
| - | - | - | - | - |
| Rth(j-a) | thermal resistance from junction to ambient | SO8 package; in free air | 94 | K/W |
|  |  | HVSON8 package; in free air | 54 | K/W |
| Rth(j-c) | thermal resistance from junction to case | HVSON8 package; in free air | 16 | K/W |
| Ѱj-top | thermal characterization parameter from junction to top of package | SO8 package; in free air | 13 | K/W |
|  |  | HVSON8 package; in free air | 6 | K/W |

[1] According to JEDEC JESD51-2, JESD51-5 and JESD51-7 at natural convection on 2s2p board. Board with two inner copper layers (thickness: 35 μm) and thermal via array under the exposed pad connected to the first inner copper layer (thickness: 70 μm).

## 10 Static characteristics

## Table 7. Static characteristics

Tvj = -40 °C to +150 °C; VCC = 4.5 V to 5.5 V; VIO = 2.91 V to 5.5 V [1] ; RL = 60 Ω; CL = 100 pF unless otherwise specified; all voltages are defined with respect to ground; positive currents flow into the IC. [2]

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - |
| Supply; pin VCC | Supply; pin VCC | Supply; pin VCC | Supply; pin VCC | Supply; pin VCC | Supply; pin VCC | Supply; pin VCC |
| VCC | supply voltage |  | 4.5 | - | 5.5 | V |
| Vuvd(VCC) | undervoltage detection voltage on pin VCC |  | [3] 3.5 | 4 | 4.3 | V |
| ICC | supply current | Silent mode; VTXD = VIO [4] | 0.1 | - | 1.2 | mA |
| ICC |  | Normal mode |  |  |  |  |
| ICC |  | recessive; VTXD = VIO [4] | 2 | 5 | 10 | mA |
| ICC |  | dominant; VTXD = 0 V | 20 | 45 | 70 | mA |
| ICC |  | dominant; short circuit on bus lines; VTXD = 0 V; -3 V < (VCANH = VCANL) < +18 V | 2 | 80 | 110 | mA |
| I/O level adapter supply; pin VIO [1] | I/O level adapter supply; pin VIO [1] | I/O level adapter supply; pin VIO [1] | I/O level adapter supply; pin VIO [1] | I/O level adapter supply; pin VIO [1] | I/O level adapter supply; pin VIO [1] | I/O level adapter supply; pin VIO [1] |
| VIO | supply voltage on pin VIO |  | 2.91 | - | 5.5 | V |
| Vuvd(VIO) | undervoltage detection voltage on pin VIO |  | [3] 2.1 | - | 2.8 | V |
| IIO | supply current on pin VIO | Silent mode | - | 3 | 16 | μA |
| IIO |  | Normal mode |  |  |  |  |
| IIO |  | recessive; VTXD = VIO [4] | - | 7 | 30 | μA |
| IIO |  | dominant; VTXD = 0 V | - | 110 | 320 | μA |

Table 7. Static characteristics...continued

![Image](TJA1057%20Datasheet_files/img_005.png)

Tvj = -40 °C to +150 °C; VCC = 4.5 V to 5.5 V; VIO = 2.91 V to 5.5 V [1] ; RL = 60 Ω; CL = 100 pF unless otherwise specified; all voltages are defined with respect to ground; positive currents flow into the IC. [2]

| Symbol | Parameter | Conditions |  | Min Typ | Max | Unit |
| - | - | - | - | - | - | - |
| Silent mode control input; pin S | Silent mode control input; pin S | Silent mode control input; pin S | Silent mode control input; pin S | Silent mode control input; pin S | Silent mode control input; pin S | Silent mode control input; pin S |
| VIH | HIGH-level input voltage |  |  | 2 - | VIO [4] + 0.3 | V |
| VIL | LOW-level input voltage |  |  | -0.3 - | 0.8 | V |
| IIH | HIGH-level input current | VS = VIO [4] | -1 | - | +1 | μA |
| IIL | LOW-level input current | VS = 0 V |  | -15 - | -1 | μA |
| CAN transmit data input; pin TXD | CAN transmit data input; pin TXD | CAN transmit data input; pin TXD | CAN transmit data input; pin TXD | CAN transmit data input; pin TXD | CAN transmit data input; pin TXD | CAN transmit data input; pin TXD |
| VIH | HIGH-level input voltage |  |  | 2 - | VIO [4] + 0.3 | V |
| VIL | LOW-level input voltage |  |  | -0.3 - | 0.8 | V |
| IIH | HIGH-level input current | VTXD = VIO [4] | -5 | - | +5 | μA |
| IIL | LOW-level input current | VTXD = 0 V |  | -260 - | -30 | μA |
| Ci | input capacitance |  | [5] - | 5 | 10 | pF |
| CAN receive data output; pin RXD | CAN receive data output; pin RXD | CAN receive data output; pin RXD | CAN receive data output; pin RXD | CAN receive data output; pin RXD | CAN receive data output; pin RXD | CAN receive data output; pin RXD |
| IOH | HIGH-level output current | VRXD = VIO [4] - 0.4 V |  | -9 -3 | -1 | mA |
| IOL | LOW-level output current | VRXD = 0.4 V; bus dominant | 1 | - | 12 | mA |
| Bus lines; pins CANH and CANL | Bus lines; pins CANH and CANL | Bus lines; pins CANH and CANL | Bus lines; pins CANH and CANL | Bus lines; pins CANH and CANL | Bus lines; pins CANH and CANL | Bus lines; pins CANH and CANL |
| VO(dom) | dominant output voltage | VTXD = 0 V; t < tto(dom)TXD |  |  |  |  |
| VO(dom) | dominant output voltage | pin CANH; RL = 50 Ω to 65 Ω |  | 2.75 3.5 | 4.5 | V |
| VO(dom) | dominant output voltage | pin CANL; RL = 50 Ω to 65 Ω | 0.5 | 1.5 | 2.25 | V |
| Vdom(TX)sym | transmitter dominant voltage symmetry | Vdom(TX)sym = VCC - VCANH - VCANL |  | -400 - | +400 | mV |
| VTXsym | transmitter voltage symmetry | VTXsym = VCANH + VCANL; fTXD = 250 kHz, 1 MHz and 2.5 MHz; CSPLIT = 4.7 nF | [5] [6] 0.9VCC | - | 1.1VCC | V |
| VO(dif) | differential output voltage | dominant; VTXD = 0 V; t < tto(dom)TXD |  |  |  |  |
| VO(dif) | differential output voltage | RL = 50 to 65 Ω |  | 1.5 - | 3 | V |
| VO(dif) | differential output voltage | RL = 45 Ω to 70 Ω |  | 1.4 - | 3.3 | V |
| VO(dif) | differential output voltage | RL = 2240 Ω | 1.5 | - | 5 | V |
| VO(dif) |  | recessive; VTXD = VIO [4] ; no load |  | -50 - | +50 | mV |
| VO(rec) | recessive output voltage | VTXD = VIO [4] ; no load | 2 | 0.5VCC | 3 | V |
| Vth(RX)dif | differential receiver threshold voltage | Normal/Silent mode; -12 V ≤ VCANL ≤ +12 V; -12 V ≤ VCANH ≤ +12 V |  | 0.5 - | 0.9 | V |
| Vrec(RX) | receiver recessive voltage | Normal/Silent mode; -12 V ≤ VCANL ≤ +12 V; -12 V ≤ VCANH ≤ +12 V | [5] -4 | - | 0.5 | V |
| Vdom(RX) | receiver dominant voltage | Normal/Silent mode; -12 V ≤ VCANL ≤ +12 V; | [5] 0.9 | - | 9.0 | V |

High-speed CAN transceiver Tvj = -40 °C to +150 °C; VCC = 4.5 V to 5.5 V; VIO = 2.91 V to 5.5 V [1] ; RL = 60 Ω; CL = 100 pF unless otherwise specified; all voltages are defined with respect to ground; positive currents flow into the IC. [2]

Table 7. Static characteristics...continued

![Image](TJA1057%20Datasheet_files/img_005.png)

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - |
|  |  | -12 V ≤ VCANH ≤ +12 V |  |  |  |  |
| Vhys(RX)dif | differential receiver hysteresis voltage | Normal mode; -12 V ≤ VCANL ≤ +12 V; -12 V v VCANH ≤ +12 V | 50 | - | 300 | mV |
| IO(sc)dom | dominant short-circuit output current | VTXD = 0 V; t < tto(dom)TXD; VCC = 5 V |  |  |  |  |
| IO(sc)dom | dominant short-circuit output current | pin CANH; VCANH = -15 V to +40 V | -100 | -70 | - | mA |
| IO(sc)dom | dominant short-circuit output current | pin CANL; VCANL = -15 V to +40 V | - | 70 | 100 | mA |
| IO(sc)rec | recessive short-circuit output current | Normal mode; VTXD = VCC; VCANH = VCANL = -27 V to +32 V | -5 | - | +5 | mA |
| IL | leakage current | VCC = 0 V or VCC = VIO = shorted to ground via 47 kΩ; VCANH = VCANL = 5 V | -5 | - | +5 | μA |
| Ri | input resistance | -2 V ≤ VCANL ≤ +7 V; -2 V ≤ VCANH ≤ +7 V | [5] 9 | 15 | 28 | kΩ |
| ΔRi | input resistance deviation | 0 V ≤ VCANL ≤ +5 V; 0 V ≤ VCANH ≤ +5 V | [5] -3 | - | +3 | % |
| Ri(dif) | differential input resistance | -2 V ≤ VCANL ≤ +7 V; -2 V ≤ VCANH ≤ +7 V | [5] 19 | 30 | 52 | kΩ |
| Ci(cm) | common-mode input capacitance |  | [5] - | - | 20 | pF |
| Ci(dif) | differential input capacitance |  | [5] - | - | 10 | pF |
| Temperature detection | Temperature detection | Temperature detection | Temperature detection | Temperature detection | Temperature detection | Temperature detection |
| Tj(sd) | shutdown junction temperature |  | [5] - | 185 | - | °C |

[1] Only the TJA1057GT(K)/3 and TJA1057BT(K) variants have a VIO pin; all circuitry is connected to VCC in the other variants..

[2] All parameters are guaranteed over the virtual junction temperature range by design. Factory testing uses correlated test conditions to cover the specified temperature and power supply voltage range.

[3] Undervoltage is detected between min and max values. Undervoltage is guaranteed to be detected below min value and guaranteed not to be detected above max value.

[4] VIO = VCC in non-VIO product variants.

[5] Not tested in production; guaranteed by design.

[6] The test circuit used to measure the bus output voltage symmetry (which includes CSPLIT) is shown in Figure 7.

High-speed CAN transceiver

![Image](TJA1057%20Datasheet_files/img_005.png)

## 11 Dynamic characteristics

High-speed CAN transceiver

## Table 8. Dynamic characteristics

Tvj = -40 °C to +150 °C; VCC = 4.5 V to 5.5 V; VIO = 2.91 V to 5.5 V [1] ; RL = 60 Ω; CL = 100 pF unless specified otherwise; all voltages are defined with respect to ground. [2]

| Symbol | Parameter | Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - |
| Transceiver timing; pins CANH, CANL, TXD and RXD; see Figure 3 and Figure 6 | Transceiver timing; pins CANH, CANL, TXD and RXD; see Figure 3 and Figure 6 | Transceiver timing; pins CANH, CANL, TXD and RXD; see Figure 3 and Figure 6 | Transceiver timing; pins CANH, CANL, TXD and RXD; see Figure 3 and Figure 6 | Transceiver timing; pins CANH, CANL, TXD and RXD; see Figure 3 and Figure 6 | Transceiver timing; pins CANH, CANL, TXD and RXD; see Figure 3 and Figure 6 | Transceiver timing; pins CANH, CANL, TXD and RXD; see Figure 3 and Figure 6 |
| td(TXD-busdom) | delay time from TXD to bus dominant | TJA1057B/C; Normal mode | [3] - | 62 | 90 | ns |
| td(TXD-busdom) |  | other variants; Normal mode | [3] - | 65 | 105 | ns |
| td(TXD-busrec) | delay time from TXD to bus recessive | TJA1057B/C; Normal mode | [3] - | 75 | 90 | ns |
| td(TXD-busrec) |  | other variants; Normal mode | [3] - | 90 | 105 | ns |
| td(busdom-RXD) | delay time from bus dominant to RXD | TJA1057B/C; Normal mode | [3] - | 60 | 100 | ns |
| td(busdom-RXD) |  | other variants; Normal mode | [3] - | 60 | 115 | ns |
| td(busrec-RXD) | delay time from bus recessive to RXD | TJA1057B/C; Normal mode | [3] - | 90 | 110 | ns |
| td(busrec-RXD) |  | other variants; Normal mode | [3] - | 65 | 135 | ns |
| td(TXDL-RXDL) | delay time from TXD LOW to RXD LOW | TJA1057B/C; Normal mode | 50 | - | 195 | ns |
| td(TXDL-RXDL) |  | other variants; Normal mode | 50 | - | 230 | ns |
| td(TXDL-RXDL) |  | other variants; Normal mode; VCC = 4.75 V to 5.25 V | 50 | - | 210 | ns |
| td(TXDH-RXDH) | delay time from TXD HIGH to RXD HIGH | TJA1057B/C; Normal mode | 50 | - | 195 | ns |
| td(TXDH-RXDH) | delay time from TXD HIGH to RXD HIGH | other variants; Normal mode | 50 | - | 230 | ns |
| td(TXDH-RXDH) | delay time from TXD HIGH to RXD HIGH | other variants; Normal mode; VCC = 4.75 V to 5.25 V | 50 | - | 210 | ns |
| CAN FD timing characteristics according to ISO 11898-2:2024 parameter set B (tbit(TXD) ≥ 200 ns, up to 5 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set B (tbit(TXD) ≥ 200 ns, up to 5 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set B (tbit(TXD) ≥ 200 ns, up to 5 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set B (tbit(TXD) ≥ 200 ns, up to 5 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set B (tbit(TXD) ≥ 200 ns, up to 5 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set B (tbit(TXD) ≥ 200 ns, up to 5 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set B (tbit(TXD) ≥ 200 ns, up to 5 Mbit/s); see Figure 3 and Figure 6 |
| Δtbit(bus) | transmitted recessive bit width deviation | Δtbit(bus) = tbit(bus) - tbit(TXD) | -45 | - | +10 | ns |
| Δtbit(RXD) | received recessive bit width deviation | Δtbit(RXD) = tbit(RXD) - tbit(TXD) | -80 | - | +20 | ns |
| Δtrec | receiver timing symmetry | Δtrec = tbit(RXD) - tbit(bus) | -45 | - | +15 | ns |
| CAN FD timing characteristics according to ISO 11898-2:2024 parameter set A (tbit(TXD) ≥ 500 ns, up to 2 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set A (tbit(TXD) ≥ 500 ns, up to 2 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set A (tbit(TXD) ≥ 500 ns, up to 2 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set A (tbit(TXD) ≥ 500 ns, up to 2 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set A (tbit(TXD) ≥ 500 ns, up to 2 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set A (tbit(TXD) ≥ 500 ns, up to 2 Mbit/s); see Figure 3 and Figure 6 | CAN FD timing characteristics according to ISO 11898-2:2024 parameter set A (tbit(TXD) ≥ 500 ns, up to 2 Mbit/s); see Figure 3 and Figure 6 |
| Δtbit(bus) | transmitted recessive bit width deviation | Δtbit(bus) = tbit(bus) - tbit(TXD) | -65 | - | +30 | ns |
| Δtbit(RXD) | received recessive bit width deviation | Δtbit(RXD) = tbit(RXD) - tbit(TXD) | -100 | - | +50 | ns |
| Δtrec | receiver timing symmetry | Δtrec = tbit(RXD) - tbit(bus) | -65 | - | +40 | ns |
| Dominant time-out time | Dominant time-out time | Dominant time-out time | Dominant time-out time | Dominant time-out time | Dominant time-out time | Dominant time-out time |
| tto(dom)TXD | TXD dominant time-out time | VTXD = 0 V; Normal mode | [4] 0.8 | 3 | 6.5 | ms |

[1] Only the TJA1057GT(K)/3 and TJA1057BT(K) variants have a VIO pin; the VIO input is internally connected to VCC in the other variants.

[2] All parameters are guaranteed over the junction temperature range by design. Factory testing uses correlated test conditions to cover the specified temperature and power supply voltage range.

[3] Not tested in production; guaranteed by design.

[4] Time-out occurs between the min and max values. Time-out is guaranteed not to occur below the min value; time-out is guaranteed to occur above the max value.

![Image](TJA1057%20Datasheet_files/img_005.png)

:

二

Figure 3. CAN transceiver timing diagram according to ISO 11898-2:2024

## High-speed CAN transceiver

![Image](TJA1057%20Datasheet_files/img_010.png)

## 12 Application information

The minimum external circuitry needed with the TJA1057 is shown in Figure 4 and Figure 5. See the Application Hints (Section 12.2) for further information about external components and PCB layout requirements.

## 12.1 Application diagrams

![Image](TJA1057%20Datasheet_files/img_011.png)

Figure 5. Typical TJA1057 application with a 3.3 V microcontroller (VIO variants)

![Image](TJA1057%20Datasheet_files/img_005.png)

High-speed CAN transceiver

![Image](TJA1057%20Datasheet_files/img_012.png)

## 12.2 Application hints

Further information on the application of the TJA1057 can be found in NXP application hints AH1308 Application Hints - Standalone high-speed CAN transceivers Mantis TJA1044/TJA1057 and Dual-Mantis TJA1046.

## 13 Test information

![Image](TJA1057%20Datasheet_files/img_013.png)

![Image](TJA1057%20Datasheet_files/img_014.png)

![Image](TJA1057%20Datasheet_files/img_005.png)

## 13.1 Quality information

This product has been qualified in accordance with the Automotive Electronics Council (AEC) standard Q100 Rev-G - Failure mechanism based stress test qualification for integrated circuits, and is suitable for use in automotive applications.

High-speed CAN transceiver

## 14 Package outline

High-speed CAN transceiver

| UNIT | A max. | A 1 | A 2 | A 3 | b p | c | D (1) | E (2) | e | H E | L | L p | Q | v | w | y | (1) Z | θ |
| - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - | - |
| mm | 1.75 | 0.25 0.10 | 1.45 1.25 | 0.25 | 0.49 0.36 | 0.25 0.19 | 5.0 4.8 | 4.0 3.8 | 1.27 | 6.2 5.8 | 1.05 | 1.0 0.4 | 0.7 0.6 | 0.25 | 0.25 | 0.1 | 0.7 0.3 | 8 o |
| inches | 0.069 | 0.010 0.004 | 0.057 0.049 | 0.01 | 0.019 0.014 | 0.0100 0.0075 | 0.20 0.19 | 0.16 0.15 | 0.05 | 0.244 0.228 | 0.041 | 0.039 0.016 | 0.028 0.024 | 0.01 | 0.01 | 0.004 | 0.028 0.012 | 0 o |

| OUTLINE VERSION | REFERENCES - IEC | REFERENCES - JEDEC | REFERENCES - JEITA | EUROPEAN PROJECTION | ISSUE DATE |
| - | - | - | - | - | - |
| SOT96-1 | 076E03 | MS-012 |  |  | 99-12-27 03-02-18 |

Figure 8. Package outline SOT96-1 (SO8)

![Image](TJA1057%20Datasheet_files/img_015.png)

![Image](TJA1057%20Datasheet_files/img_005.png)

## High-speed CAN transceiver

Figure 9. Package outline SOT782-1 (HVSON8)

![Image](TJA1057%20Datasheet_files/img_016.png)

![Image](TJA1057%20Datasheet_files/img_008.png)

## 15 Handling information

High-speed CAN transceiver

All input and output pins are protected against ElectroStatic Discharge (ESD) under normal handling. When handling ensure that the appropriate precautions are taken as described in JESD625-A or equivalent standards.

## 16 Soldering of SMD packages

This text provides a very brief insight into a complex technology. A more in-depth account of soldering ICs can be found in Application Note AN10365 "Surface mount reflow soldering description".

## 16.1 Introduction to soldering

Soldering is one of the most common methods through which packages are attached to Printed Circuit Boards (PCBs), to form electrical circuits. The soldered joint provides both the mechanical and the electrical connection. There is no single soldering method that is ideal for all IC packages. Wave soldering is often preferred when through-hole and Surface Mount Devices (SMDs) are mixed on one printed wiring board; however, it is not suitable for fine pitch SMDs. Reflow soldering is ideal for the small pitches and high densities that come with increased miniaturization.

## 16.2 Wave and reflow soldering

Wave soldering is a joining technology in which the joints are made by solder coming from a standing wave of liquid solder. The wave soldering process is suitable for the following:

- Through-hole components
- Leaded or leadless SMDs, which are glued to the surface of the printed circuit board

Not all SMDs can be wave soldered. Packages with solder balls, and some leadless packages which have solder lands underneath the body, cannot be wave soldered. Also, leaded SMDs with leads having a pitch smaller than ~0.6 mm cannot be wave soldered, due to an increased probability of bridging.

The reflow soldering process involves applying solder paste to a board, followed by component placement and exposure to a temperature profile. Leaded packages, packages with solder balls, and leadless packages are all reflow solderable.

Key characteristics in both wave and reflow soldering are:

- Board specifications, including the board finish, solder masks and vias
- Package footprints, including solder thieves and orientation
- The moisture sensitivity level of the packages
- Package placement
- Inspection and repair
- Lead-free soldering versus SnPb soldering

## 16.3 Wave soldering

Key characteristics in wave soldering are:

- Process issues, such as application of adhesive and flux, clinching of leads, board transport, the solder wave parameters, and the time during which components are exposed to the wave
- Solder bath specifications, including temperature and impurities

![Image](TJA1057%20Datasheet_files/img_005.png)

## 16.4 Reflow soldering

Key characteristics in reflow soldering are:

- Lead-free versus SnPb soldering; note that a lead-free reflow process usually leads to higher minimum peak temperatures (see Figure 10) than a SnPb process, thus reducing the process window
- Solder paste printing issues including smearing, release, and adjusting the process window for a mix of large and small components on one board
- Reflow temperature profile; this profile includes preheat, reflow (in which the board is heated to the peak temperature) and cooling down. It is imperative that the peak temperature is high enough for the solder to make reliable solder joints (a solder paste characteristic). In addition, the peak temperature must be low enough that the packages and/or boards are not damaged. The peak temperature of the package depends on package thickness and volume and is classified in accordance with Table 9 and Table 10

Table 9. SnPb eutectic process (from J-STD-020D)

|  |  |  |
| - | - | - |
| Package thickness (mm) | Package reflow temperature (°C) | Package reflow temperature (°C) |
|  | Volume (mm³) | Volume (mm³) |
|  | < 350 | ≥ 350 |
| < 2.5 | 235 | 220 |
| ≥ 2.5 | 220 | 220 |

Table 10. Lead-free process (from J-STD-020D)

| Package thickness (mm) | Package reflow temperature (°C) - Volume (mm³) - < 350 | Package reflow temperature (°C) - Volume (mm³) - 350 to 2000 | Package reflow temperature (°C) - Volume (mm³) - > 2000 |
| - | - | - | - |
| < 1.6 | 260 | 260 | 260 |
| 1.6 to 2.5 | 260 | 250 | 245 |
| > 2.5 | 250 | 245 | 245 |

Moisture sensitivity precautions, as indicated on the packing, must be respected at all times.

Studies have shown that small packages reach higher temperatures during reflow soldering, see Figure 10.

High-speed CAN transceiver

![Image](TJA1057%20Datasheet_files/img_004.png)

## High-speed CAN transceiver

![Image](TJA1057%20Datasheet_files/img_017.png)

For further information on temperature profiles, refer to Application Note AN10365 "Surface mount reflow soldering description".

![Image](TJA1057%20Datasheet_files/img_005.png)

## TJA1057

High-speed CAN transceiver

## 17 Appendix: ISO 11898-2:2024 parameter cross-reference lists

Table 11. ISO 11898-2:2024 to NXP data sheet parameter conversion [1]

| ISO 11898-2:2024 - Parameter | Notation | NXP data sheet - Symbol | NXP data sheet - Parameter |
| - | - | - | - |
| HS-PMA maximum ratings of VCAN_H, VCAN_L and VDiff | HS-PMA maximum ratings of VCAN_H, VCAN_L and VDiff | HS-PMA maximum ratings of VCAN_H, VCAN_L and VDiff | HS-PMA maximum ratings of VCAN_H, VCAN_L and VDiff |
| Maximum rating | VDiff | V(CANH-CANL) | voltage between pin CANH and pin CANL |
| General maximum rating | VCAN_H | Vx | voltage on pin x |
| Optional: Extended maximum rating | VCAN_L |  |  |
| HS-PMA recessive output characteristics, bus biasing active/inactive | HS-PMA recessive output characteristics, bus biasing active/inactive | HS-PMA recessive output characteristics, bus biasing active/inactive | HS-PMA recessive output characteristics, bus biasing active/inactive |
| Single ended output voltage on CAN_H | VCAN_H | VO(rec) | recessive output voltage |
| Single ended output voltage on CAN_L | VCAN_L |  |  |
| Differential output voltage | VDiff | VO(dif) | differential output voltage |
| HS-PMA dominant output characteristics | HS-PMA dominant output characteristics | HS-PMA dominant output characteristics | HS-PMA dominant output characteristics |
| Single ended voltage on CAN_H | VCAN_H | VO(dom) | dominant output voltage |
| Single ended voltage on CAN_L | VCAN_L |  |  |
| Differential voltage on normal bus load | VDiff | VO(dif) | differential output voltage |
| Differential voltage on effective resistance during arbitration |  |  |  |
| Optional: Differential voltage on extended bus load range |  |  |  |
| Maximum HS-PMA driver output current | Maximum HS-PMA driver output current | Maximum HS-PMA driver output current | Maximum HS-PMA driver output current |
| Absolute current on CAN_H | ICAN_H | IO(sc) | short-circuit output current |
| Absolute current on CAN_L | ICAN_L |  |  |
| HS-PMA static receiver input characteristics, bus biasing active/inactive | HS-PMA static receiver input characteristics, bus biasing active/inactive | HS-PMA static receiver input characteristics, bus biasing active/inactive | HS-PMA static receiver input characteristics, bus biasing active/inactive |
| Recessive state differential input voltage range | VDiff | Vth(RX)dif | differential receiver threshold voltage |
| Dominant state differential input voltage range |  | Vrec(RX) | receiver recessive voltage |
|  |  | Vdom(RX) | receiver dominant voltage |
| HS-PMA receiver input resistance (matching) | HS-PMA receiver input resistance (matching) | HS-PMA receiver input resistance (matching) | HS-PMA receiver input resistance (matching) |
| Differential internal resistance | RDIFF_pas_rec | Ri(dif) | differential input resistance |
| Single-ended internal resistance | RSE_pas_rec_H RSE_pas_rec_L | Ri | input resistance |
| Matching of internal resistance | mR | ΔRi | input resistance deviation |
| HS-PMA maximum leakage currents on CAN_H and CAN_L, unpowered | HS-PMA maximum leakage currents on CAN_H and CAN_L, unpowered | HS-PMA maximum leakage currents on CAN_H and CAN_L, unpowered | HS-PMA maximum leakage currents on CAN_H and CAN_L, unpowered |
| Leakage current on CAN_H, CAN_L | ICAN_H ICAN_L | IL | leakage current |
| HS-PMA driver symmetry | HS-PMA driver symmetry | HS-PMA driver symmetry | HS-PMA driver symmetry |
| Driver symmetry | Vsym_vcc | VTXsym | transmitter voltage symmetry |
| Optional HS-PMA transmit dominant time-out | Optional HS-PMA transmit dominant time-out | Optional HS-PMA transmit dominant time-out | Optional HS-PMA transmit dominant time-out |
| Transmit dominant time-out | tdom | tto(dom)TXD | TXD dominant time-out time |

## NXP Semiconductors

![Image](TJA1057%20Datasheet_files/img_005.png)

## TJA1057

Table 11. ISO 11898-2:2024 to NXP data sheet parameter conversion [1] ...continued

## High-speed CAN transceiver

| ISO 11898-2:2024 - Parameter | Notation | NXP data sheet - Symbol | NXP data sheet - Parameter |
| - | - | - | - |
| HS-PMA implementation loop delay requirements for parameter sets A, B and C | HS-PMA implementation loop delay requirements for parameter sets A, B and C | HS-PMA implementation loop delay requirements for parameter sets A, B and C | HS-PMA implementation loop delay requirements for parameter sets A, B and C |
| Loop delay for parameter sets A and B | tLoop | td(TXDH-RXDH) | delay time from TXD HIGH to RXD HIGH |
| Loop delay for parameter set C |  | td(TXDL-RXDL) | delay time from TXD LOW to RXD LOW |
| Propagation delay from TXD to CAN_H/CAN_L for parameter set C | tprop(TXD_BUS) | td(TXD-busdom) | delay time from TXD to bus dominant |
| Propagation delay from CAN_H/CAN_L to RXD for parameter set C |  | td(TXD-busrec) | delay time from TXD to bus recessive |
|  | tprop(BUS_RXD) | td(busdom-RXD) | delay time from bus dominent to RXD |
|  |  | td(busrec-RXD) | delay time from bus recessive to RXD |
| HS-PMA implementation data signal timing requirements for parameter sets A, B and C | HS-PMA implementation data signal timing requirements for parameter sets A, B and C | HS-PMA implementation data signal timing requirements for parameter sets A, B and C | HS-PMA implementation data signal timing requirements for parameter sets A, B and C |
| Transmitted recessive bit width variation | tΔBit(Bus) | Δtbit(bus) | transmitted recessive bit width deviation |
| Received recessive bit width variation | tΔBit(RXD) | Δtbit(RXD) | received recessive bit width deviation |
| Receiver timing symmetry | tΔREC | Δtrec | receiver timing symmetry |
| HS-PMA implementation SIC timing and impedance for parameter set C | HS-PMA implementation SIC timing and impedance for parameter set C | HS-PMA implementation SIC timing and impedance for parameter set C | HS-PMA implementation SIC timing and impedance for parameter set C |
| Differential internal resistance (CAN_H to CAN_L) | RDIFF_act_rec | Ri(dif)actrec | active recessive phase differential input resistance |
| Internal single-ended resistance | RSE_act_rec | Ri(actrec) | active recessive phase input resistance |
| Start time of active signal improvement phase | tact_rec_start | td(TXD- busactrec)start | delay time from TXD to bus active recessive start |
| End time of active signal improvement phase | tact_rec_end | td(TXD- busactrec)end | delay time from TXD to bus active recessive end |
| Start time of passive recessive phase | tpas_rec_start | td(TXD- buspasrec)start | delay time from TXD to bus passive recessive start |
| PMA voltage wake-up control timing | PMA voltage wake-up control timing | PMA voltage wake-up control timing | PMA voltage wake-up control timing |
| CAN activity filter time, long/short | tFilter | twake(busdom) twake(busrec) | bus dominant wake-up time bus recessive wake-up time |
| Wake-up time-out | tWake | tto(wake)bus | bus wake-up time-out time |
| Wake-up pattern signaling | tFlag | tstartup(RXD) | RXD start-up time |
| Wake-up pattern signaling |  | tstartup(INH) | INH start-up time |
| Wake-up pattern signaling |  | tstartup(ERR_N) | ERR_N start-up time |
| Number of recessive bits before next SOF | Number of recessive bits before next SOF | Number of recessive bits before next SOF | Number of recessive bits before next SOF |
| Number of recessive bits before a new SOF shall be accepted | nBits_idle | Nbit(idle) | number of idle bits before a SOF is accepted |
| BitFilter in CAN FD data phase | BitFilter in CAN FD data phase | BitFilter in CAN FD data phase | BitFilter in CAN FD data phase |
| CAN FD data phase bitfilter (option 1) | ρBitfilter_option1 | tfltr(bit)dom | dominant bit filter time |
| CAN FD data phase bitfilter (option 2) | ρBitfilter_option2 |  |  |
| HS-PMA bus biasing control timing | HS-PMA bus biasing control timing | HS-PMA bus biasing control timing | HS-PMA bus biasing control timing |
| Time-out for bus inactivity | tSilence | tto(silence) | bus silence time-out time |
| Bus bias reaction time | tBias | td(busact-bias) | bus bias reaction time |

![Image](TJA1057%20Datasheet_files/img_004.png)

High-speed CAN transceiver

- [1] A number of proprietary NXP parameters are equivalent to parameters defined in ISO 11898-2:2024, but use different symbols. This conversion table allows ISO parameters to be cross-referenced with their NXP counterparts. The NXP parameters are defined in the Static and Dynamic characteristics tables. The conversion table provides a comprehensive listing - individual devices may not include all parameters.

## 18 Revision history

Table 12. Revision history

| Document ID | Release date | Description |
| - | - | - |
| TJA1057 v.8.1 | 02 March 2026 | · Table 11 in Section 17 has been updated. |
| TJA1057 v.8.0 | 10 September 2024 | Product data sheet Modifications: · ISO 11898-2:2016 upgraded to ISO 11898-2:2024 throughout · Section 2.1: EMC compliance updated · Table 5: SAE J2962-2:2019 VESD entries added · Table 8: Formatting of CAN (FD) timing characteristics revised · Original Figs. 3 and 4 combined in new single Figure 3 · Section 17: cross-reference table updated |
| TJA1057 v.7.0 | 16 January 2023 | Product data sheet |
| TJA1057 v.6.0 | 24 August 2017 | Product data sheet |
| TJA1057 v.5.1 | 23 May 2016 | Product data sheet |
| TJA1057 v.5.0 | 28 January 2016 | Product data sheet |
| TJA1057 v.4.0 | 10 July 2015 | Product data sheet |
| TJA1057 v.3.0 | 19 November 2014 | Product data sheet |
| TJA1057 v.2.0 | 30 October 2013 | Product data sheet |
| TJA1057 v.1.0 | 30 May 2013 | Preliminaly data sheet; initial version |

![Image](TJA1057%20Datasheet_files/img_005.png)

## Legal information

High-speed CAN transceiver

## Data sheet status

| Document status [1][2] | Product status [3] | Definition |
| - | - | - |
| Objective [short] data sheet | Development | This document contains data from the objective specification for product development. |
| Preliminary [short] data sheet | Qualification | This document contains data from the preliminary specification. |
| Product [short] data sheet | Production | This document contains the product specification. |

- [1] Please consult the most recently issued document before initiating or completing a design.
- [2] The term 'short data sheet' is explained in section "Definitions".
- [3] The product status of device(s) described in this document may have changed since this document was published and may differ in case of multiple devices. The latest product status information is available on the Internet at URL https://www.nxp.com.

## Definitions

Draft - A draft status on a document indicates that the content is still under internal review and subject to formal approval, which may result in modifications or additions. NXP Semiconductors does not give any representations or warranties as to the accuracy or completeness of information included in a draft version of a document and shall have no liability for the consequences of use of such information.

Short data sheet - A short data sheet is an extract from a full data sheet with the same product type number(s) and title. A short data sheet is intended for quick reference only and should not be relied upon to contain detailed and full information. For detailed and full information see the relevant full data sheet, which is available on request via the local NXP Semiconductors sales office. In case of any inconsistency or conflict with the short data sheet, the full data sheet shall prevail.

Product specification - The information and data provided in a Product data sheet shall define the specification of the product as agreed between NXP Semiconductors and its customer, unless NXP Semiconductors and customer have explicitly agreed otherwise in writing. In no event however, shall an agreement be valid in which the NXP Semiconductors product is deemed to offer functions and qualities beyond those described in the Product data sheet.

## Disclaimers

Limited warranty and liability - Information in this document is believed to be accurate and reliable. However, NXP Semiconductors does not give any representations or warranties, expressed or implied, as to the accuracy or completeness of such information and shall have no liability for the consequences of use of such information. NXP Semiconductors takes no responsibility for the content in this document if provided by an information source outside of NXP Semiconductors.

In no event shall NXP Semiconductors be liable for any indirect, incidental, punitive, special or consequential damages (including - without limitation - lost profits, lost savings, business interruption, costs related to the removal or replacement of any products or rework charges) whether or not such damages are based on tort (including negligence), warranty, breach of contract or any other legal theory.

Notwithstanding any damages that customer might incur for any reason whatsoever, NXP Semiconductors' aggregate and cumulative liability towards customer for the products described herein shall be limited in accordance with the Terms and conditions of commercial sale of NXP Semiconductors.

Right to make changes - NXP Semiconductors reserves the right to make changes to information published in this document, including without limitation specifications and product descriptions, at any time and without notice. This document supersedes and replaces all information supplied prior to the publication hereof.

Applications - Applications that are described herein for any of these products are for illustrative purposes only. NXP Semiconductors makes no representation or warranty that such applications will be suitable for the specified use without further testing or modification.

Customers are responsible for the design and operation of their applications and products using NXP Semiconductors products, and NXP Semiconductors accepts no liability for any assistance with applications or customer product design. It is customer's sole responsibility to determine whether the NXP Semiconductors product is suitable and fit for the customer's applications and products planned, as well as for the planned application and use of customer's third party customer(s). Customers should provide appropriate design and operating safeguards to minimize the risks associated with their applications and products.

NXP Semiconductors does not accept any liability related to any default, damage, costs or problem which is based on any weakness or default in the customer's applications or products, or the application or use by customer's third party customer(s). Customer is responsible for doing all necessary testing for the customer's applications and products using NXP Semiconductors products in order to avoid a default of the applications and the products or of the application or use by customer's third party customer(s). NXP does not accept any liability in this respect.

Limiting values - Stress above one or more limiting values (as defined in the Absolute Maximum Ratings System of IEC 60134) will cause permanent damage to the device. Limiting values are stress ratings only and (proper) operation of the device at these or any other conditions above those given in the Recommended operating conditions section (if present) or the Characteristics sections of this document is not warranted. Constant or repeated exposure to limiting values will permanently and irreversibly affect the quality and reliability of the device.

Terms and conditions of commercial sale - NXP Semiconductors products are sold subject to the general terms and conditions of commercial sale, as published at https://www.nxp.com/profile/terms, unless otherwise agreed in a valid written individual agreement. In case an individual agreement is concluded only the terms and conditions of the respective agreement shall apply. NXP Semiconductors hereby expressly objects to applying the customer's general terms and conditions with regard to the purchase of NXP Semiconductors products by customer.

No offer to sell or license - Nothing in this document may be interpreted or construed as an offer to sell products that is open for acceptance or the grant, conveyance or implication of any license under any copyrights, patents or other industrial or intellectual property rights.

![Image](TJA1057%20Datasheet_files/img_005.png)

## TJA1057

Suitability for use in automotive applications - This NXP product has been qualified for use in automotive applications. If this product is used by customer in the development of, or for incorporation into, products or services (a) used in safety critical applications or (b) in which failure could lead to death, personal injury, or severe physical or environmental damage (such products and services hereinafter referred to as "Critical Applications"), then customer makes the ultimate design decisions regarding its products and is solely responsible for compliance with all legal, regulatory, safety, and security related requirements concerning its products, regardless of any information or support that may be provided by NXP. As such, customer assumes all risk related to use of any products in Critical Applications and NXP and its suppliers shall not be liable for any such use by customer. Accordingly, customer will indemnify and hold NXP harmless from any claims, liabilities, damages and associated costs and expenses (including attorneys' fees) that NXP may incur related to customer's incorporation of any product in a Critical Application.

Quick reference data - The Quick reference data is an extract of the product data given in the Limiting values and Characteristics sections of this document, and as such is not complete, exhaustive or legally binding.

Export control - This document as well as the item(s) described herein may be subject to export control regulations. Export might require a prior authorization from competent authorities.

HTML publications - An HTML version, if available, of this document is provided as a courtesy. Definitive information is contained in the applicable document in PDF format. If there is a discrepancy between the HTML document and the PDF document, the PDF document has priority.

Translations - A non-English (translated) version of a document, including the legal information in that document, is for reference only. The English version shall prevail in case of any discrepancy between the translated and English versions.

## High-speed CAN transceiver

Security - Customer understands that all NXP products may be subject to unidentified vulnerabilities or may support established security standards or specifications with known limitations. Customer is responsible for the design and operation of its applications and products throughout their lifecycles to reduce the effect of these vulnerabilities on customer's applications and products. Customer's responsibility also extends to other open and/or proprietary technologies supported by NXP products for use in customer's applications. NXP accepts no liability for any vulnerability. Customer should regularly check security updates from NXP and follow up appropriately. Customer shall select products with security features that best meet rules, regulations, and standards of the intended application and make the ultimate design decisions regarding its products and is solely responsible for compliance with all legal, regulatory, and security related requirements concerning its products, regardless of any information or support that may be provided by NXP.

NXP has a Product Security Incident Response Team (PSIRT) (reachable at PSIRT@nxp.com) that manages the investigation, reporting, and solution release to security vulnerabilities of NXP products.

NXP B.V. - NXP B.V. is not an operating company and it does not distribute or sell products.

## Trademarks

Notice: All referenced brands, product names, service names, and trademarks are the property of their respective owners.

NXP - wordmark and logo are trademarks of NXP B.V.

Mantis - is a trademark of NXP B.V.

![Image](TJA1057%20Datasheet_files/img_005.png)

## TJA1057

## Contents

| 1 | General description .........................................1 |  |
| - | - | - |
| 2 | Features and benefits | ..................................... 1 |
| 2.1 | General | .............................................................. 1 |
| 2.2 | Predictable and fail-safe behavior | ..................... 2 |
| 2.3 | Protection | ...........................................................2 |
| 2.4 | TJA1057 CAN FD (applicable to all product variants except TJA1057T) ................................2 |  |
| 3 | Quick reference data | .......................................2 |
| 4 | Ordering information | .......................................3 |
| 5 | Block diagram | ..................................................4 |
| 6 | Pinning information | .........................................5 |
| 6.1 | Pinning | ...............................................................5 |
| 6.2 | Pin description | ...................................................5 |
| 7 | Functional description | .................................... 6 |
| 7.1 | Operating modes | ............................................... 6 |
| 7.1.1 | Normal mode | .....................................................6 |
| 7.1.2 | Silent mode | ........................................................6 |
| 7.2 | Fail-safe features | ...............................................6 |
| 7.2.1 | TXD dominant time-out function | ........................ 6 |
| 7.2.2 | Internal biasing of TXD and S input pins | ........... 6 |
| 7.2.3 | Undervoltage detection on pins VCC and VIO (TJA1057GT(K)/3 and TJA1057BT(K) variants) ............................................................. ...............................7 | 7 |
| 7.2.4 | Overtemperature protection |  |
| 7.2.5 | VIO supply pin (TJA1057GT(K)/3 and TJA1057BT(K) variants) .................................... | 7 |
| 8 | Limiting values | ................................................ 8 |
| 9 | Thermal characteristics | .................................. 9 |
| 10 | Static characteristics | .......................................9 |
| 11 | Dynamic characteristics | ............................... 12 |
| 12 | Application information | ................................ 13 |
| 12.1 | Application diagrams | ....................................... 13 |
| 12.2 | Application hints .............................................. | 14 |
| 13 | Test information | .............................................14 |
| 13.1 | Quality information | ...........................................15 |
| 14 | Package outline | ............................................. 16 |
| 15 | Handling information | .....................................18 |
| 16 | Soldering of SMD packages | ......................... 18 |
| 16.1 | Introduction to soldering | ............................. |
| 16.2 | Wave and reflow soldering | ......................... |
| 16.3 | Wave soldering ........................................... |  |
| 16.4 | Reflow soldering | ......................................... |
| 17 | Appendix: ISO 11898-2:2024 parameter cross-reference lists ......................................21 |  |
| 18 | Revision history | .............................................23 |
|  | Legal information | ...........................................24 |
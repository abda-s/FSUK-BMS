<!-- Converted from TIDA-010271 Design Guide (tiduf46).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

www.ti.com Description

## Design Guide: TIDA-010271

## Stackable Battery Management Unit Reference Design for Energy Storage Systems

## Description

This reference design is a full cell-temperature sensing and high cell-voltage accuracy Lithium-ion (Li-ion), lithium iron phosphate (LiFePO4) battery pack (32s). The design monitors each cell voltage, cell temperature, and protects the battery pack to secure safe use. This design uses an onboard and offboard daisy-chain communication interface for a cost-effective stacked bus connection. These features make this reference design applicable for high-capacity battery pack applications.

## Resources

[TIDA-010271](https://www.ti.com/tool/TIDA-010271)

[BQ79616, TPS22810-Q1](https://www.ti.com/product/TPS22810-Q1)

Design Folder

Product Folder

TMUX1308, TMUX1574

Product Folder

ISO7742, TMUX1102

Product Folder

TSD05C, ESD441, ESD2CAN24-Q1

Product Folder

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_001.png)

[Ask our TI E2E™ support experts](https://e2e.ti.com/support/applications/ti_designs/)

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_002.png)

## Features

- ±1.5-mV voltage accuracy at 25°C without calibration
- Internal cell balancing up to 100 mA, with the option for higher-capacity support through an external balancing circuit
- Full cell-temperature sensing with multiplexer (MUX)
- Robust and programmable battery cell and pack protection
- Robust daisy-chain communication with data reclocking and ring architecture
- 15 μA in shutdown mode
- Optional isolated universal asynchronous receiver and transmitter (UART) interface for microcontroller and controller area network (CAN) communication

## Applications

- [Battery energy storage system](https://www.ti.com/solution/energy-storage-battery-packs-with-bms)
- [Other industrial battery pack (&gt;=10S)](https://www.ti.com/solution/battery-pack-industrial-10s)

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_003.png)

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_004.png)

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_005.png)

## 1 System Description

Currently, the battery energy storage systems (BESS) play an important role in residential, commercial and industrial, grid energy storage, and management. A BESS has various high-voltage system structures. Commercial and industrial and grid BESS contain several racks that each contain packs in stack. Residential BESS only contains packs.

A pack is a basic module composing the BESS. A pack consists of battery cells in a matter of series and parallel connection. The number of cell channels varies from 12 to 64. Since the battery cells require a proper working and storage temperature, voltage range, current range for lifecycle and safety, the designer must monitor and protect the battery cell in the pack level.

A battery management unit (BMU) is a controller that monitors the voltage and temperature of each battery cell in the pack for a complete lifecycle. High measurement accuracy for voltage and temperature monitoring is required for the BMU. The information collected by the BMU is transmitted to the rack-level controller battery control unit (BCU) for safety and charging management. A robust and fast-speed communication is also required between the BMU and the BCU.

Safety, regulations, and cost concerns drive the need for a LiFePO4 battery in a BESS. The LiFePO4 battery charge or discharge curve remains fairly linear for the approximately 85% to 100% state of charge (SOC) range, but the curve abruptly changes in slope in the approximately 10% to approximately 85% SOC range. This becomes significant when choosing what voltage accuracy is acceptable in a BESS design. For most conditions, measuring accuracy in 3 mV to 5 mV is required to calculate a high SOC accuracy and a wide depth of discharge (DOD).

For a communication interface, a controller area network (CAN) is traditionally and widely used for robustness of communication. A CAN structure controller needs a microcontroller unit (MCU), a digital isolator, and an isolated power module to operate the CAN communication function.

A daisy chain can replace a CAN design. Compared with the CAN interface, only a couple of transformers are needed in the BMU. Thus, a daisy chain design shows an advantage in cost over a CAN especially in high-capacity battery pack applications since cost is a concern for a CAN structure in large-capacity BESS which consist of many BMU nodes and CAN interface devices. Insulation requirements also raise cost because the reinforced insulation required between the BMU and BCU communication interface necessitates a digital isolator and isolated power module.

This design focuses on large capacity battery pack applications and applications that can be applied in residential, commercial and industrial, grid BESS, and so forth. The design uses two BQ79616 devices (battery monitor, balancer, and integrated hardware protector) to monitor each cell voltage, the temperature of a 32s battery pack, and to protect the pack against situations that include cell overvoltage, cell undervoltage, and overtemperature. The design contains four TMUX1308 devices for a GPIO expansion ratio of 8:1 to measure up to 32s cell temperature and one TMUX1574 device for serial peripheral interface (SPI) expansion to restore pack information in an external electrically-erasable programmable read-only memory (EEPROM). The design uses an internal cell balancing (CB) to get 100-mA balancing current per cell channel and reserves an external CB circuit for a potential larger balancing current.

The onboard communication between two BQ79616 devices uses capacitor-isolated daisy chain. The offboard communication between the BMU and BMU or BCU uses transformer-isolated daisy chain. The design also reserves an isolated UART interface to the offboard MCU which can be used in the CAN structure.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_006.png)

[www.ti.com](https://www.ti.com/)

## 2 System Overview

The design uses two BQ79616 devices to monitor each cell voltage, the temperature of a 32 cells battery pack, and to protect the pack against all unusual situations, including cell overvoltage, cell undervoltage, and overtemperature. In Figure 2-1, the top BQ79616 device is the BQ79616-A2 and the bottom BQ79616 device is the BQ79616-A1. The forward daisy-chain communication direction is from the BQ79616-A1 device to the BQ79616-A2 device.

Each BQ79616 has 8 GPIO pins for temperature sensing and 16 VC pins for voltage sensing. To monitor the temperatures for all the VC channels with fewer GPIO pins, two TMUX1308 multiplexers are used. The multiplexers expand temperature-sensing capabilities of one BQ79616 from 8 channels to 16 channels. The TMUX1574 is used to expand GPIO4 through GPIO7 of BQ79616 to an external SPI EEPROM that restores pack information.

To run diagnostics for the TMUX1308, each channel of the TMUX1308 can be connected one at a time to the TSREF output pin of BQ79616. TSREF is set at a high or low voltage level, according to the BCU command. The BCU then polls the MUX channels and determines if the voltage reported on the MUX channel connected to TSREF matches the TSREF pin output. This diagnostic method can show if the MUX is stuck on a specific channel or reporting voltages corresponding to incorrect channels.

In this design, the GPIO8 pin is reserved for a humidity sensor interface.

The CVDD pin on the BQ79616 is used to supply power to the TMUX1308, TMUX1574, external EEPROM, and humidity sensor. Since CVDD provides a constant-on power supply, the pin can cause leakage current to external loads when the BQ79616 is in SHUTDOWN mode. TPS22810 is enabled by GPIO3 of the BQ79616, and the device is used to switch the power supply output from CVDD to prevent unintended leakage current.

BQ79616 supports the UART interface to the MCU. An ISO7742 is placed between the BQ79616 and MCU to isolate the TX and RX pins of each device. Since the TX and CVDD pins of the BQ79616 are a constanton power supply, these pins can cause leakage current to the ISO7742 in SHUTDOWN mode. A PMOS, TMUX1102, and optocoupler are used to block the leakage current. To initiate UART communication, the MCU needs enable the optocoupler to switch on the PMOS and TMUX1102 from the MCU side.

This design also uses a BJT network for external passive cell balancing. The internal passive cell balancing resistors can support up to 100 mA of balancing current. The voltage across the internal passive cell balancing resistors are used to switch ON the external BJTs for internal passive cell balancing.

To isolate communication, the design uses two high-voltage capacitors for daisy chain communication between two BQ79616 and two transformers in daisy chain communication between the BMUs or the BCU.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_007.png)

## 2.1 Block Diagram

Figure 2-1 shows the system block diagram.

Figure 2-1. TIDA-010271 Block Diagram

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_008.png)

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_009.png)

[www.ti.com](https://www.ti.com/)

## 2.2 Design Considerations

## 2.2.1 Multiplexer Network and Switch Strategy

Figure 2-2 shows the strategy of reading all thermistors and cell voltages. Two TMUX1308 devices are used to multiplex 16 Negative Temperature Coefficient (NTC) thermistors to one BQ79616. The BQ79616 uses three GPIOs (GPIO5, GPIO6, and GPIO7) to address the 8 NTC thermistor channels of the TMUX1308 and two GPIOs (GPIO1 and GPIO2) to read the common output pin from two TMUX1308 devices. This means 5 GPIOs can switch 16 NTC thermistors. If more thermistors are required, 6 GPIOs can switch 24 NTC thermistors.

Figure 2-2. Strategy of Reading all Thermistors and Cell Voltages

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_010.png)

Although the number of NTC thermistors can easily be increased using the TMUX1308 or a different multiplexer, the system still needs an efficient switching strategy to connect all 16 NTC thermistors in a safe time defined by regulation.

The loop of NTC thermistor switching consists of a broadcast write to all the stacked BQ79616 GPIO5 to 7 pins and a broadcast read of the TSREF and GPIO1 to GPIO2. The design needs 8 loops to read the temperature data from 16 NTC thermistors. Supposing the number of stacked BMUs is N, and the design uses a BQ79600 base device (not counted when determining N), then one loop spends 14+4 × 2×N\_BMU-1 +60 μs to perform the broadcast write to the GPIO5 to7 pins on all devices. A broadcast read of the TSREF and GPIO1 to GPIO2 takes 14+4 × 2×N\_BMU-1 +60+14+4 × 2 ×N\_BMU-1 +90 × 2 ×N\_BMU μs.

If the BESS rack voltage is 1500 V, and one rack consists of 470 pieces of battery cells in series, then use 15 BMUs (30 BQ79616 devices) to monitor all the battery cells. Performing one loop to read temperature data from the stacked BQ79616 devices takes 4.11 ms and polls 2 out of the 16 NTC thermistors on each BQ79616 in the stack. Reading temperature data from all 16 NTC thermistors on each BQ79616 in the stack takes 32.880 ms. Following the NTC thermistors data reading, 11.706 ms are required to read the cell voltage (VCELL) data of all the stacked BQ79616 devices. The total time spent gathering temperature and VCELL data for a 1500-V rack is about 44 ms, which meets GBT34131-2023 standards (100 ms for VCELL and 1 s for NTC thermistors).

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_007.png)

## 2.2.2 Cell Balancing

Figure 2-3 shows the cell balancing circuit.

Figure 2-3. Cell Balancing Circuit

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_011.png)

The design uses an internal field-effect transistor (FET) to achieve a 100-mA balancing current. Assuming the given condition: an initial CB voltage of 3.5 V, the final CB voltage is 3.3 V. To achieve 100-mA balancing current while the CB voltage is 3.5 V, Rcb6 = Rcb5 = 15 Ω is used.

The voltage across the Rcb5 also provides bias voltage to the external cell balancing NPN transistor. The Rcbe value can be determined based on the CB voltage and desired external cell balancing current. Rb needs to meet two conditions:

1. Condition 1: NPN transistor work in the saturation region for a small heat dissipation area: ic &lt; Coefficient × hfe × ib. hfe is the DC current transfer static ratio of the NPN transistor. The ic-hfe curve is found in the NPN transistor data sheet. While the ic equals the desired external cell balancing current, the corresponding maximum hfe in the whole temperature range can be used to meet condition 1. The coefficient is usually set to 2 to keep the NPN transistor in saturation region by a safe margin.
2. Condition 2: UBE &gt; UBE(on). UBE(on) is the base-emitter turn-on voltage. UBE(on) must be smaller than the voltage across the Rcb5 and as small as possible to enable an easy selection of Rb.

This design uses 300 Ω for Rb, which can support an external cell balancing current as large as 600 mA.

## 2.2.3 Stacked AFE Communication

For very high cell count systems, BQ79616 devices can be stacked in series to monitor battery cells. This design uses two BQ79616 devices to monitor up to 32s battery cells. The bottom BQ79616 monitors the lower 16s battery cells, and the top BQ79616 monitors the upper 16s battery cells. The bottom BQ79616 device shares the same ground as BAT-, while the top BQ79616 references 16s top-of-stack voltage as ground. Isolation is required to communicate with the top BQ79616 device. This design uses a capacitor-isolated daisy chain between two BQ79616 devices and a transformer-isolated daisy chain to the offboard BMU or BCU. The BMU is designed to support both the forward and reverse communication directions. The communication direction from the bottom BQ79616 to the top BQ79616 is North (Forward). The communication direction from the top BQ79616 to the bottom BQ79616 is South (Reverse). Figure 2-4 shows the ring communication of the BMUs.

Figure 2-4. BMU Ring Communication

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_012.png)

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_006.png)

[www.ti.com](https://www.ti.com/)

The BCU issues pings to the BQ79600 using SPI. Pings are non-comm signals for simple actions, such as WAKE and SHUTDOWN. Commands are used to transmit data. The BQ79600 can send and receive tones to and from the stacked BQ79616 in the North and South in a duty cycle. Considering the GBT34131-2023 standards, the voltage cycle needs to be less than 100 ms, and the temperature cycle needs to be less than 1 second.

## 2.2.4 Isolated UART Interface to MCU

The design reserves an isolated UART interface to the MCU for a CAN structure. The ISO7742 is used to connect the UART interface of the BQ79616 and the MCU. Since the CVDD and TX pins of the BQ79616 supply a constant voltage in both SHUTDOWN and ACTIVE modes, the ISO7742 is powered from the VCC (CVDD) and input (TX) when the BQ79616 SHUTDOWN mode of the ISO7742 is directly connected to BQ79616.

Figure 2-5 shows the ISO7742 circuit directly connected to the BQ79616.

Figure 2-5. ISO7742 Circuit Directly Connected to BQ79616

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_013.png)

The TMUX1102 is used to block the current from the TX pin. The TMUX1102 has a powered-off protection feature and high bandwidth of 300 MHz, which is suitable for the TX signal transmit path. A PMOS is used to block the CVDD pin connection from the BQ79616 to the ISO7742 unidirectionally. Both the TMUX1102 and PMOS are enabled by an optocoupler pulldown signal controlled by the MCU.

Figure 2-5 shows the ISO7742 circuit connected to TMUX and PMOS.

Figure 2-6. ISO7742 Circuit Connected to TMUX and PMOS

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_014.png)

## 2.3 Highlighted Products

## 2.3.1 BQ79616

The BQ79616 device provides high-accuracy cell voltage measurements in less than 200 μs for 16-series battery modules in high-voltage battery management systems in HEV and EV. The monitor offers different channel options in the same package type, providing pin-to-pin compatibility and supporting high reuse of the established software and hardware across any platform. The integrated front-end filters enable the system to implement with simple, low voltage rating, differential RC filters on the cell input channels. The integrated, post-ADC, low-pass filters enable filtered, DC-like, voltage measurements for better state of charge (SOC) calculation. This device supports autonomous internal cell balancing with temperature monitoring to auto-pause and resume balancing to avoid an overtemperature condition.

## 2.3.2 TMUX1308

The TMUX1308-Q1 and TMUX1309-Q1 devices are general purpose complementary metal-oxide semiconductor (CMOS) multiplexers (MUX). The TMUX1308-Q1 is an 8:1, 1-channel (single-ended) MUX, while the TMUX1309-Q1 is a 4:1, 2-channel (differential) MUX. The devices support bidirectional analog and digital signals on the source (Sx) and drain (Dx) pins ranging from GND to VDD.

The TMUX13xx-Q1 devices have an internal injection current control feature which eliminates the need for external diode and resistor networks typically used to protect the switch and keep the input signals within the supply voltage. The internal injection current control circuitry allows signals on disabled signal paths to exceed the supply voltage without affecting the signal of the enabled signal path. Additionally, the TMUX13xx-Q1

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_015.png)

devices do not have an internal diode path to the supply pin, which eliminates the risk of damaging components connected to the supply pin or providing unintended power to the supply rail.

All logic inputs have 1.8-V logic compatible thresholds, providing both transistor-transistor logic (TTL) and CMOS logic compatibility when operating with a valid supply voltage. Fail-safe logic circuitry allows voltages on the control pins to be applied before the supply pin, protecting the device from potential damage.

## 2.3.3 TMUX1574

The TMUX1574 is a CMOS switch. The TMUX1574 offers 2:1 SPDT switch configuration with 4-channels. A wide operating supply of 1.5 V to 5.5 V allows for use in a broad array of applications from servers and communication equipment to industrial applications. The device supports bidirectional analog and digital signals on the source (SxA, SxB) and drain (Dx) pins and can pass signals above supply up to VDD × 2, with a maximum input and output voltage of 5.5 V.

Powered-off protection up to 3.6 V on the signal path of the TMUX1574 provides isolation when the supply voltage is removed (VDD = 0 V). Without this protection feature, switches can back-power the supply rail through an internal electrostatic discharge (ESD) diode and cause potential damage to the system.

Fail-safe logic circuitry allows voltages on the logic control pins to be applied before the supply pin, protecting the device from potential damage. All control inputs have 1.8-V logic compatible thresholds, providing both TTL and CMOS logic compatibility when operating in the valid supply voltage range. Integrated pulldown resistor on the logic pins removes external components to reduce the system size and cost.

## 2.3.4 TMUX1102

The TMUX1101 and TMUX1102 devices are precision CMOS single-pole, single-throw (SPST) switches. A wide operating supply of 1.08 V to 5.5 V allows for use in a broad array of applications from medical equipment to industrial systems. The devices support bidirectional analog and digital signals on the source (S) and drain (D) pins ranging from GND to VDD.

The logic control input (SEL) has 1.8-V logic compatible thresholds, providing both TTL and CMOS logic compatibility when operating within the valid supply voltage range. The switch of the TMUX1101 is turned on when SEL is logic 1, while the TMUX1102 is turned on when SEL is logic 0. Fail-safe logic circuitry allows voltages on the SEL pin to be applied before the supply pin, protecting the device from potential damage.

The TMUX110x devices are part of the precision switches and multiplexers family. These devices have very low on and off leakage currents and low charge injection, allowing them to be used in high-precision measurement applications. A low supply current of 3 nA and small package. (data sheet = A low supply current of 3 nA and small package options enable use in portable applications.)

## 2.3.5 TPS22810

The TPS22810 is a single-channel load switch with configurable rise time and with an integrated quick output discharge (QOD). In addition, the device features thermal shutdown to protect the device against high junction temperatures. Because of this feature, safe operating area of the device is inherently provided. The device contains an N-channel MOSFET that can operate over an input voltage range of 2.7 V to 18 V. The SOT23-5 (DBV) package can support a maximum current of 2 A. A WSON (DRV) package can support a maximum current of 3 A. The switch is controlled by an on and off input, which is capable of interfacing directly with low-voltage control signals.

The configurable rise time of the device greatly reduces inrush current caused by large bulk load capacitances, thereby reducing or eliminating power supply droop. Undervoltage lock-out is used to turn off the device if the VIN voltage drops below a threshold value, making sure that the downstream circuitry is not damaged by being supplied by a voltage lower than intended. The configurable QOD pin controls the fall time of the device to allow design flexibility for power down.

The TPS22810 is available in a leaded, SOT-23 package (DBV) which allows visual inspection of the solder joints, as well as a WSON package (DRV). The device is characterized for operation over the free-air temperature range of -40˚C to +105˚C.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_016.png)

[www.ti.com](https://www.ti.com/)

## 2.3.6 ISO7742

The ISO774x devices are high-performance, quad-channel digital isolators with 5000-VRMS (DW package) and 3000-VRMS (DBQ package) isolation ratings per UL 1577. This family includes devices with reinforced insulation ratings according to VDE, CSA, TUV and CQC. The ISO7741B device is designed for applications that require basic insulation ratings only. The ISO774x devices provide high electromagnetic immunity and low emissions at low power consumption, while isolating CMOS or LVCMOS digital I/Os. Each isolation channel has a logic input and output buffer separated by a double capacitive silicon dioxide (SiO2) insulation barrier. These devices come with enable pins which can be used to put the respective outputs in high impedance for multi-master driving applications and to reduce power consumption.

The ISO7740 device has all four channels in the same direction, the ISO7741 device has three forward and one reverse-direction channels, and the ISO7742 device has two forward and two reverse-direction channels. If the input power or signal is lost, default output is high for devices without suffix F and low for devices with suffix F.

## 2.3.7 TSD05C

The TSD05C is a bidirectional transient voltage suppressor (TVS) protection diode designed for clamping harmful transients such as ESD and surge. The TSD05C is rated to dissipate ESD strikes up to ±30 kV (contact and air gap discharge) and also meets the maximum level specified in the IEC 61000-4-2 international standard (Level 4). For surges, the device can clamp 8- to 20-µs surges with peak pulse currents up to 30 A in accordance with the IEC 61000-4-5 standard.

This device also features a 4-pF (typical) IO capacitance enabling the device to protect high-speed data lines. The low dynamic resistance and low clamping voltage provides system-level protection against transient events.

Combining the robust clamping performance and low capacitance of this device, TSD05C is an excellent TVS diode to protect both data lines and power lines in many different applications.

The TSD05C is offered in the industry standard, leaded SOD-323 package providing easy soldering.

## 2.3.8 ESD441

The ESD441 is a unidirectional ESD protection diode for protecting data lines and other I/O ports. The ESD441 is rated to dissipate ESD strikes up to ±30 kV per the IEC 61000-4-2 international standard (greater than Level 4).

This device features a 1-pF (typical) IO capacitance enabling high-speed interfaces protection for protocols such as USB 2.0. The extremely low dynamic resistance (0.1 Ω) and clamping voltage (7.6 V at 16 TLP) is specified for system-level protection against transient events.

The 30-kV ESD rating and 6.2-A surge provides robust transient protection in a tiny package for protecting 5.5-V power rails in portable electronics and other space-constrained applications such as wearables.

The ESD441 is offered in the industry standard 0201 (DPL) package.

## 2.3.9 ESD2CAN24-Q1

The ESD2CANxx24-Q1 is a bidirectional ESD protection diode for CAN interface protection. The ESD2CANxx24-Q1 is rated to dissipate contact ESD strikes beyond the maximum level specified in the ISO 10605 automotive standard (±30-kV Contact, ±30-kV Air gap). The low dynamic resistance and low clamping voltage enables system-level protection against transient events. This protection is key because automotive systems require a high level of robustness and reliability for safety applications.

This device features a low IO capacitance per channel and a pinout to suit two automotive CAN bus lines (CANH and CANL) from the damage caused by ESD and other transients. Additionally, the 3-pF (typical) or less line capacitance of the ESD2CANxx24-Q1 is suitable for CAN, CANFD, CAN SiC, and CAN-XL applications that can support data rates up to 10Mbps.

The ESD2CANxx24-Q1 is offered in two leaded packages for easy flow-through routing.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_005.png)

## 3 Hardware, Software, Testing Requirements, and Test Results

The key performances of the TIDA-010271 were tested in a TI lab, the end equipment used and test processes and results are described in this section.

Table 3-1 describes the hardware connections for the TIDA-010271 board.

Table 3-1. Top 16s Battery Connector

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J21-3 | A2_CELL0 | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J21-4 | A2_CELL0S | Negative terminal of CELL1, actual sense connection for VC0 path of top BQ79616 |
| J21-5 | A2_CELL1 | Positive terminal of CELL1, negative terminal of CELL2 of top BQ79616 |
| J21-6 | A2_CELL2 | Positive terminal of CELL2, negative terminal of CELL3 of top BQ79616 |
| J21-7 | A2_CELL3 | Positive terminal of CELL3, negative terminal of CELL4 of top BQ79616 |
| J21-8 | A2_CELL4 | Positive terminal of CELL4, negative terminal of CELL5 of top BQ79616 |
| J21-9 | A2_CELL5 | Positive terminal of CELL5, negative terminal of CELL6 of top BQ79616 |
| J21-10 | A2_CELL6 | Positive terminal of CELL6, negative terminal of CELL7 of top BQ79616 |
| J21-11 | A2_CELL7 | Positive terminal of CELL7, negative terminal of CELL8 of top BQ79616 |
| J21-12 | A2_CELL8 | Positive terminal of CELL8, negative terminal of CELL9 of top BQ79616 |
| J21-13 | A2_CELL9 | Positive terminal of CELL9, negative terminal of CELL10 of top BQ79616 |
| J21-14 | A2_CELL10 | Positive terminal of CELL10, negative terminal of CELL11 of top BQ79616 |
| J21-15 | A2_CELL11 | Positive terminal of CELL11, negative terminal of CELL12 of top BQ79616 |
| J21-16 | A2_CELL12 | Positive terminal of CELL12, negative terminal of CELL13 of top BQ79616 |
| J21-17 | A2_CELL13 | Positive terminal of CELL13, negative terminal of CELL14 of top BQ79616 |
| J21-18 | A2_CELL14 | Positive terminal of CELL14, negative terminal of CELL15 of top BQ79616 |
| J21-19 | A2_CELL15 | Positive terminal of CELL15, negative terminal of CELL16 of top BQ79616 |
| J21-20 | A2_CELL16 | Positive terminal of CELL16, actual sense connection to VC16 path of top BQ79616 |
| J21-21 | A2_CELL_TOP | Positive terminal of CELL16, direct connection to BAT, LDOIN of top BQ79616 |

Table 3-2. Top 16s Thermistor Connector

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J9-1 | A2_NTC0_C | Connection to 10-kΩ pullup and thermistor0 of top BQ79616 |
| J9-2 | A2_NTC1_C | Connection to 10-kΩ pullup and thermistor1 of top BQ79616 |
| J9-3 | A2_NTC2_C | Connection to 10-kΩ pullup and thermistor2 of top BQ79616 |
| J9-4 | A2_NTC3_C | Connection to 10-kΩ pullup and thermistor3 of top BQ79616 |
| J9-5 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J9-6 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J9-7 | A2_NTC4_C | Connection to 10-kΩ pullup and thermistor4 of top BQ79616 |
| J9-8 | A2_NTC5_C | Connection to 10-kΩ pullup and thermistor5 of top BQ79616 |
| J9-9 | A2_NTC6_C | Connection to 10-kΩ pullup and thermistor6 of top BQ79616 |
| J9-10 | A2_NTC7_C | Connection to 10-kΩ pullup and thermistor7 of top BQ79616 |
| J9-11 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J9-12 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J9-13 | A2_NTC8_C | Connection to 10-kΩ pullup and thermistor8 of top BQ79616 |
| J9-14 | A2_NTC9_C | Connection to 10-kΩ pullup and thermistor9 of top BQ79616 |
| J9-15 | A2_NTC10_C | Connection to 10-kΩ pullup and thermistor10 of top BQ79616 |
| J9-16 | A2_NTC11_C | Connection to 10-kΩ pullup and thermistor11 of top BQ79616 |
| J9-17 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J9-18 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J9-19 | A2_NTC12_C | Connection to 10-kΩ pullup and thermistor12 of top BQ79616 |

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_016.png)

[www.ti.com](https://www.ti.com/)

## Table 3-2. Top 16s Thermistor Connector (continued)

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J9-20 | A2_NTC13_C | Connection to 10-kΩ pullup and thermistor13 of top BQ79616 |
| J9-21 | A2_NTC14_C | Connection to 10-kΩ pullup and thermistor14 of top BQ79616 |
| J9-22 | A2_NTC15_C | Connection to 10-kΩ pullup and thermistor15 of top BQ79616 |
| J9-23 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |
| J9-24 | A2_GND | Negative terminal of CELL1, connected directly to AVSS GND of top BQ79616 |

Table 3-3. Top Daisy-Chain (COMH) Connector

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J31-3 | ISO_A2_COMMH_P | COM high-side positive |
| J31-4 | ISO_A2_CO/MMH_N | COM high-side negative |

## Table 3-4. Humidity Sensor Connector

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J1-1 | A2_CVDD | 5-V power supply for Humidity sensor |
| J1-2 | A2_RHS_T_MUX | Temperature analog output from Humidity sensor |
| J1-3 | A2_GPIO8 | Humidity analog output from Humidity sensor |
| J1-4 | A2_GND | GND for Humidity sensor |

## Table 3-5. Bottom 16s Battery Connector

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J10-3 | A1_CELL0 | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J10-4 | A1_CELL0S | Negative terminal of CELL1, actual sense connection for VC0 path of bottom BQ79616 |
| J10-5 | A1_CELL1 | Positive terminal of CELL1, negative terminal of CELL2 of bottom BQ79616 |
| J10-6 | A1_CELL2 | Positive terminal of CELL2, negative terminal of CELL3 of bottom BQ79616 |
| J10-7 | A1_CELL3 | Positive terminal of CELL3, negative terminal of CELL4 of bottom BQ79616 |
| J10-8 | A1_CELL4 | Positive terminal of CELL4, negative terminal of CELL5 of bottom BQ79616 |
| J10-9 | A1_CELL5 | Positive terminal of CELL5, negative terminal of CELL6 of bottom BQ79616 |
| J10-10 | A1_CELL6 | Positive terminal of CELL6, negative terminal of CELL7 of bottom BQ79616 |
| J10-11 | A1_CELL7 | Positive terminal of CELL7, negative terminal of CELL8 of bottom BQ79616 |
| J10-12 | A1_CELL8 | Positive terminal of CELL8, negative terminal of CELL9 of bottom BQ79616 |
| J10-13 | A1_CELL9 | Positive terminal of CELL9, negative terminal of CELL10 of bottom BQ79616 |
| J10-14 | A1_CELL10 | Positive terminal of CELL10, negative terminal of CELL11 of bottom BQ79616 |
| J10-15 | A1_CELL11 | Positive terminal of CELL11, negative terminal of CELL12 of bottom BQ79616 |
| J10-16 | A1_CELL12 | Positive terminal of CELL12, negative terminal of CELL13 of bottom BQ79616 |
| J10-17 | A1_CELL13 | Positive terminal of CELL13, negative terminal of CELL14 of bottom BQ79616 |
| J10-18 | A1_CELL14 | Positive terminal of CELL14, negative terminal of CELL15 of bottom BQ79616 |
| J10-19 | A1_CELL15 | Positive terminal of CELL15, negative terminal of CELL16 of bottom BQ79616 |
| J10-20 | A1_CELL16 | Positive terminal of CELL16, actual sense connection to VC16 path of bottom BQ79616 |
| J10-21 | A1_CELL_TOP | Positive terminal of CELL16, direct connection to BAT, LDOIN of bottom BQ79616 |

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_005.png)

## Table 3-6. Bottom 16s Thermistor Connector

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J11-1 | A1_NTC0_C | Connection to 10-kΩ pullup and thermistor0 of bottom BQ79616 |
| J11-2 | A1_NTC1_C | Connection to 10-kΩ pullup and thermistor1 of bottom BQ79616 |
| J11-3 | A1_NTC2_C | Connection to 10-kΩ pullup and thermistor2 of bottom BQ79616 |
| J11-4 | A1_NTC3_C | Connection to 10-kΩ pullup and thermistor3 of bottom BQ79616 |
| J11-5 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J11-6 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J11-7 | A1_NTC4_C | Connection to 10-kΩ pullup and thermistor4 of bottom BQ79616 |
| J11-8 | A1_NTC5_C | Connection to 10-kΩ pullup and thermistor5 of bottom BQ79616 |
| J11-9 | A1_NTC6_C | Connection to 10-kΩ pullup and thermistor6 of bottom BQ79616 |
| J11-10 | A1_NTC7_C | Connection to 10-kΩ pullup and thermistor7 of bottom BQ79616 |
| J11-11 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J11-12 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J11-13 | A1_NTC8_C | Connection to 10-kΩ pullup and thermistor8 of bottom BQ79616 |
| J11-14 | A1_NTC9_C | Connection to 10-kΩ pullup and thermistor9 of bottom BQ79616 |
| J11-15 | A1_NTC10_C | Connection to 10-kΩ pullup and thermistor10 of bottom BQ79616 |
| J11-16 | A1_NTC11_C | Connection to 10-kΩ pullup and thermistor11 of bottom BQ79616 |
| J11-17 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J11-18 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J11-19 | A1_NTC12_C | Connection to 10-kΩ pullup and thermistor12 of bottom BQ79616 |
| J11-20 | A1_NTC13_C | Connection to 10-kΩ pullup and thermistor13 of bottom BQ79616 |
| J11-21 | A1_NTC14_C | Connection to 10-kΩ pullup and thermistor14 of bottom BQ79616 |
| J11-22 | A1_NTC15_C | Connection to 10-kΩ pullup and thermistor15 of bottom BQ79616 |
| J11-23 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |
| J11-24 | A1_GND | Negative terminal of CELL1, connected directly to AVSS GND of bottom BQ79616 |

## Table 3-7. Bottom Daisy-Chain (COML) Connector

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J30-1 | ISO_A1_COMML_N | COM low-side negative |
| J30-2 | ISO_A1_COMML_P | COM low-side positive |

## Table 3-8. Bottom Host Interface

| CONNECTOR AND PIN ASSIGNMENTS | FUNCTION OR SCHEMATIC NET | NOTES |
| - | - | - |
| J12-1 | NA |  |
| J12-2 | NA |  |
| J12-3 | A1_NFAULT_C |  |
| J12-4 | NA |  |
| J12-5 | A1_GND_ISO |  |
| J12-6 | A1_USB2ANY_3.3V |  |
| J12-7 | A1_USB2ANY_TX_3.3 |  |
| J12-8 | A1_USB2ANY_RX_3.3 |  |
| J12-9 | NA |  |
| J12-10 | NA |  |

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_009.png)

[www.ti.com](https://www.ti.com/)

## 3.1 Hardware Requirements

Table 3-9 summarizes the equipment used for testing.

Table 3-9. Test Equipment Summary

| EQUIPMENT | MODEL OR DESCRIPTION |
| - | - |
| Multimeter | Agilent 34401A |
| Battery simulator | TZ1104 |
| USB2ANY | TI HAP655 |
| Logic Analyzer | Kingst LA5016 |

The Battery Management Studio (bqStudio) Software is recommended when debugging the board for the first time.

## 3.2 Test Setup

Use the following procedures before running this design board. The design was constructed with 32s pack configurations. The board was tested using 24s-battery simulator to simulate the total pack. The bottom 16s cell channels are connected to the bottom BQ79616 device. The negative terminal of cell17 is connected to A2\_CELL0 and the positive terminal of cell24 is connected to A2\_TOP.

Figure 3-1 shows the BMU test setup.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_017.png)

Figure 3-1. BMU Test Setup

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_018.png)

## 3.3 Test Results

## 3.3.1 Cell Voltage Accuracy

This design does not perform any calibrations to further improve the cell voltage accuracy since the BQ79616 already achieves ±1.5-mV accuracy at 25°C. The typical voltage range of a LiFePO4 cell is 2.5 V (0% SOC) about 3.65 V (100% SOC), so the design uses a battery simulator to provide cell voltages from 2.5 V to 3.7V to verify the VCELL accuracy of the BMU.

The maximum error of all cell channels for the bottom BMU is 1.3 mV at a room temperature of 27°C.

Figure 3-2 shows the cell voltage accuracy.

Figure 3-2. Cell Voltage Accuracy

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_019.png)

## 3.3.2 Temperature Sensing Accuracy

A thermistor card board is used to verify the temperature sensing accuracy of the BMU in a climate chamber. A thermocouple with an accuracy of ±1°C is connected to NTC thermistor 6. The BMU NTC thermistor resistance RNTC\_0 can be calculated with VNTC from the GPIO1 and TSREF voltages. The test uses two methods to calculate the temperature. A simple Steinhart-Hart equation (Equation 1) accurate for a small range is used to calculate the BMU NTC thermistor temperature.

For better accuracy, a Thermistor R/T Table look-up and linear fit method is used to calculate the temperature.

<!-- formula-not-decoded -->

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_009.png)

[www.ti.com](https://www.ti.com/)

Figure 3-3 shows temperature sensing accuracy. The maximum temperature error is 1°C in -35°C to 85°C.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_020.png)

Figure 3-3. Temperature Sensing Accuracy

Figure 3-4 shows thermistor voltage accuracy. The maximum voltage error is 2 mV in -35°C to 85°C.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_021.png)

Figure 3-4. Thermistor Voltage Accuracy

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_005.png)

## 3.3.3 Cell Voltage and Temperature Sensing Timings

This test uses one BMU and a BCU. The test point is found in Figure 2-1 including T1-GPIO5, T2-GPIO6, T3-GPIO5, T4-GPIO2, and T5-COML of the bottom BQ79616 device. The test software of Cell Voltage and Temperature Sensing Timings follows the steps in Figure 2-2.

Figure 3-5 shows the cell voltage and temperature sensing timings.

Figure 3-5. Cell Voltage and Temperature Sensing Timings

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_022.png)

The test needs eight steps to read all the NTC thermistor voltages. Each step contains a broadcast write to set TMUX1308 and a broadcast read of TSREF and GPIO1 to GPIO2 from all the BQ79616 devices in the stacked BMUs. Reading 2 NTC thermistor voltages for each BQ79616 in the stack is one step and takes 675 μs. Reading all the voltages takes 8 steps and 6.637 ms. The sum of steps for reading all NTC (NTC0 to NTC31) voltages and cell voltages (VCELL1 to VCELL32) for the entire stack of BQ79616 devices takes 8.225 ms.

To easily verify that the configuration of the GPIO1 and GPIO2 pins and TMUX1308 is correct, NTC15 is set as a fixed 100-Ω pulldown that a logic analyzer can recognize as a signal 0. It can be learned that the eight status transfer of TMUX1308 works correctly.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_023.png)

[www.ti.com](https://www.ti.com/)

## 3.3.4 Cell Balancing and Thermal Performance

The test uses a battery simulator to test the bottom BQ79616 device of the BMU at room temperature (27°C) and 3.5-V cell voltage. Auto-balancing control is used and CB FETs are enabled in an odd and even manner with a duty cycle of 30 minutes. After 30 minutes of odd or even manner cell balancing, the temperature is stable.

Table 3-10 shows the cell balancing current from a battery simulator. The power supply current to BQ79616 is near 15.3 mA. The cell current of each channel is near 109 mA.

Table 3-10. Cell Balancing Current From Battery Simulator

| CELL | CELL VOLTAGE (V) | CURRENT (A) | CELL | CELL VOLTAGE (V) | CURRENT (A) | CELL | CELL VOLTAGE (V) | CURRENT (A) |
| - | - | - | - | - | - | - | - | - |
| 8 | 3.5000 | 0.0153 | 16 | 3.5000 | 0.0150 | 24 | 3.5003 | 0.0000 |
| 7 | 3.5000 | 0.1242 | 15 | 3.5001 | 0.1242 | 23 | 3.5002 | 0.0000 |
| 6 | 3.5003 | 0.0152 | 14 | 3.5001 | 0.0152 | 22 | 3.5001 | 0.0000 |
| 5 | 3.5000 | 0.1241 | 13 | 3.5000 | 0.1242 | 21 | 3.5001 | 0.0000 |
| 4 | 3.4996 | 0.0152 | 12 | 3.5000 | 0.0152 | 20 | 3.5000 | 0.0000 |
| 3 | 3.5005 | 0.1229 | 11 | 3.4998 | 0.1242 | 19 | 3.4998 | 0.0000 |
| 2 | 3.5000 | 0.0152 | 10 | 3.5002 | 0.0152 | 18 | 3.5005 | 0.0000 |
| 1 | 3.4999 | 0.1231 | 9 | 3.5002 | 0.1233 | 17 | 3.5000 | 0.0000 |

The following images show the cell balancing thermal performance at room temperature. Figure 3-6 is the top side thermal image and Figure 3-7 shows the bottom side thermal image.

Figure 3-6. Top Side of Board

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_024.png)

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_025.png)

Figure 3-7. Bottom Side of Board

The maximum temperature rise is 19°C.

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_026.png)

## 3.3.5 Current Consumption

Figure 3-8 shows the test point of the current consumption in BMU test setup. Two working modes are tested including shutdown mode and active mode. Cell16 and cell32 were selected as test points for current because they are the locations where the power supply cable directly connects to the BAT pin of the BQ79616. In both modes, the battery simulator sets 3.2-V cell voltage.

Figure 3-8. Test Point of Current Consumption in BMU Test Setup

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_027.png)

In active mode, the BCU runs the test loop in Figure 2-2 in 100-ms duty cycle. In shutdown mode, the leakage current to the BQ79616 BAT pin is 14.6 μA and 15.5 μA. In active mode, the working current is 18.39 mA and 18.22 mA. Table 3-11 shows the BMU current consumption from the battery.

Table 3-11. BMU Current Consumption From Battery

| DESCRIPTION | DESCRIPTION | Icell16 | Icell32 |
| - | - | - | - |
| Shutdown Mode | Current (μA) | 14.60 | 15.50 |
| Active Mode | Current (mA) | 18.39 | 18.22 |

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_016.png)

[www.ti.com](https://www.ti.com/)

The test also uses an isolated UART interface to communicate with the BMU instead of the BCU. A USB2ANY is used to enable the optocoupler. When the enable signal is sent to the optocoupler, the BMU transfers from shutdown mode to standby mode. At this time, CVDD of BQ79616 is switched to the ISO7742 and a leakage current near 5.393 mA flows to ISO7742. After the UART communication starts, the BMU enters the active mode and the leakage current to ISO7742 rises to 7.042 mA. Table 3-12 shows BMU current consumption to the isolated UART interface.

Table 3-12. BMU Current Consumption to Isolated UART Interface

| DESCRIPTION | DESCRIPTION | I_CVDD |
| - | - | - |
| Shutdown Mode | Current (μA) | 0.001 |
| Standby Mode | Current (mA) | 5.393 |
| Active Mode | Current (mA) | 7.042 |

![Image](TIDA-010271%20Design%20Guide%20%28tiduf46%29_files/img_005.png)

## 4 Design and Documentation Support

## 4.1 Design Files

## 4.1.1 Schematics

To download the schematics, see the design files at TIDA-010271.

## 4.1.2 BOM

To download the schematics, see the design files at TIDA-010271.

## 4.2 Tools and Software

## Tools

[USB2ANY](https://www.ti.com/tool/USB2ANY)

USB2ANY interface adapter

## Software

BQSTUDIO Battery Management Studio (bqStudio) Software

CCSTUDIO Code Composer Studio™ integrated development environment (IDE)

## 4.3 Documentation Support

1. Texas Instruments, LiFePO4 Design Considerations Application Note
2. Texas Instruments, BQ79616-Q1 Software Design Reference Application Note
3. [Texas Instruments, How to stack battery monitors for high-cell-count industrial applications E2E™ forum](https://e2e.ti.com/blogs_/b/powerhouse/posts/how-to-stack-battery-monitors-for-high-cell-count-industrial-applications)
4. Texas Instruments, Expanding Functionality of Cell Supervision Unit in Battery Management Systems Application Brief

## 4.4 Support Resources

TI E2E™ support forums are an engineer's go-to source for fast, verified answers and design help - straight from the experts. Search existing answers or ask your own question to get the quick design help you need.

Linked content is provided "AS IS" by the respective contributors. They do not constitute TI specifications and do not necessarily reflect TI's views; see TI's Terms of Use.

## 4.5 Trademarks

TI E2E™ and E2E™, and are trademarks of Texas Instruments. All trademarks are the property of their respective owners.

## 5 About the Author

JUNHUA YAN, is a TI system engineer from the SEM Industrial Grid Infrastructure and Power Delivery team. Junhua focuses on battery pack and energy storage system applications and has created several designs to address industrial battery pack design challenges.

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2023, Texas Instruments Incorporated
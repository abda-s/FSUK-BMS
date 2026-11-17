<!-- Converted from BQ7961x-Q1 High Voltage BMS Design Recommendations (slvae87b).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

www.ti.com Table of Contents

## User's Guide

## BQ7961x-Q1 Design Recommendations for High Voltage Automotive BMS

Taylor Vogt

## ABSTRACT

The BQ79616-Q1 provides high-accuracy cell voltage measurements for 6S to 16S battery modules in &lt;200 µs. The integrated front end filters enable the system to implement simple, low-cost, differential RC filters on the cell input channels. The integrated, post-ADC, low-pass filters enable filtered, DC-like, voltage measurements for better SOC calculation. This device supports autonomous internal cell balancing with temperature monitoring to auto-pause and resume balancing to avoid an overtemperature condition.

The inclusion of the isolated, bidirectional, daisy chain ports supports both capacitor- and transformer-based isolation, allowing the use of the most effective components for centralized or distribution architectures commonly found in the xEV powertrain system. This device also includes eight GPIOs and auxiliary inputs that can be used for NTC thermistor measurements.

## Table of Contents

| 1 NPN LDO Supply.....................................................................................................................................................................3 |  |
| - | - |
| 2 AVDD, CVDD Outputs and DVDD, NEG5, REFHP and REFHM........................................................................................... | 4 |
| 3 OTP Programming..................................................................................................................................................................6 |  |
| 4 Cell Voltage Sense (VCn) and Cell Balancing (CBn)........................................................................................................... | 7 |
| 5 Bus Bar Support................................................................................................................................................................... | 13 |
| 6 TSREF....................................................................................................................................................................................22 |  |
| 7 General Purpose Input-Output (GPIO) Configurations..................................................................................................... | 22 |
| 8 Base and Bridge Device Configuration.............................................................................................................................. | 25 |
| 9 Daisy-Chain Stack Configuration........................................................................................................................................29 |  |
| 10 Multidrop Configuration.....................................................................................................................................................36 |  |
| 11 Main ADC Digital LPF......................................................................................................................................................... | 38 |
| 12 AUX Anti Aliasing Filter (AAF)...........................................................................................................................................38 |  |
| 13 Layout Guidelines...............................................................................................................................................................39 |  |
| 14 BCI Performance.................................................................................................................................................................42 |  |
| 15 Common and Differential Mode Noise..............................................................................................................................42 |  |
| 16 Summary............................................................................................................................................................................. | 43 |
| 17 References.......................................................................................................................................................................... | 43 |
| 18 Revision History................................................................................................................................................................. | 44 |
| List of Figures | List of Figures |
| Figure 1-1. Power Supply Schematic.......................................................................................................................................... | 3 |
| Figure 2-1. Regulator Connection for Base Device..................................................................................................................... | 5 |
| Figure 4-1. Cell Voltage Monitoring............................................................................................................................................. | 7 |
| Figure 4-2. Internal CB Diagram (no adjacent cell balancing).....................................................................................................8 |  |
| Figure 4-3. Cell Balancing Resistor Example Calculation........................................................................................................... | 9 |
| Figure 4-4. Adjacent Cell Balancing.......................................................................................................................................... | 10 |
| Figure 4-5. External FET Cell Balancing....................................................................................................................................11 |  |
| Figure 4-6. Connecting Fewer Than 16 Cells............................................................................................................................12 |  |
| Figure 5-1. Alternative Bus Bar Connection to the Lower Stack Device....................................................................................14 |  |
| Figure 5-2. Example of BBP/BBN Connections at Different Module Size..................................................................................15 |  |
| Figure 5-3. BBP or BBN Connection With Bus Bar Connected in any Middle VC Channel ..................................................... | 16 |
| Figure 5-4. BBP or BBN Connection With Bus Bar Connected Above Top of a Module .......................................................... | 17 |

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_001.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_002.png)

| Figure 5-5. Bus Bar Connected Any Middle Individual VC Channel .........................................................................................18 |  |
| - | - |
| Figure 5-6. Bus Bar Connected Individual VC Channel Above the Top of a Module.................................................................19 |  |
| Figure 5-7. Two Bus Bars Connections Using Two Different VC Channel.................................................................................20 |  |
| Figure 5-8. Multiple Bus Bar Connections Utilizing the BBP/N Pins..........................................................................................21 |  |
| Figure 5-9. Internal CB Diagram With the Bus Bar Connection.................................................................................................22 |  |
| Figure 7-1. GPIO Ratiometric Measurement............................................................................................................................. | 23 |
| Figure 7-2. Example SPI Master Connections...........................................................................................................................24 |  |
| Figure 7-3. 8 NTC Thermistors With SPI Slave Device............................................................................................................. | 25 |
| Figure 8-1. Communication With the Bridge Device BQ79600-Q1............................................................................................26 |  |
| Figure 8-2. Using BQ79616-Q1 as Base Device with Isolation Circuit......................................................................................26 |  |
| Figure 8-3. Communication Pings............................................................................................................................................. | 27 |
| Figure 8-4. Communication Tones.............................................................................................................................................27 |  |
| Figure 8-5. Diagram for Ping or Tone Propagation....................................................................................................................28 |  |
| Figure 9-1. Daisy Chain Structure With a Base Device.............................................................................................................30 |  |
| Figure 9-2. Daisy Chain Structure With a Bridge Device...........................................................................................................31 |  |
| Figure 9-3. Components Required for Cap Coupled Daisy Chain in the Same PCB................................................................ | 32 |
| Figure 9-4. Components Required for Cap Coupled Daisy Chain in Different PCB.................................................................. | 32 |
| Figure 9-5. Components Required for Cap-Choke Daisy Chain With Cabling.......................................................................... | 32 |
| Figure 9-6. Components Required for Transformer Coupled Daisy Chain................................................................................33 |  |
| Figure 9-7. Example of Changing Communication Direction in Daisy Chain.............................................................................34 |  |
| Figure 9-8. Heartbeat or Fault Tone Traveling Direction............................................................................................................35 |  |
| Figure 9-9. Reclocking Bit Compression Example.................................................................................................................... | 36 |
| Figure 10-1. Multi-Drop Configuration....................................................................................................................................... | 37 |
| Figure 13-1. Grounding Layout Consideration...........................................................................................................................40 |  |
| Figure 13-2. Separate Ground Plane per Device on the Same PCB.........................................................................................41 |  |
| Figure 13-3. Daisy Chain Layout Considerations...................................................................................................................... | 42 |
| Figure 15-1. XY Caps................................................................................................................................................................ | 43 |
| List of Tables | List of Tables |
| Table 8-1. UART Physical Layer Check List.............................................................................................................................. | 29 |
| Table 11-1. Main ADC LPF fcutoff for VCELL and Bus Bar Measurement.................................................................................. | 38 |
| Table 12-1. AAF Settling Time................................................................................................................................................... | 38 |

Trademarks

All trademarks are the property of their respective owners.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

## 1 NPN LDO Supply

The device is powered by BAT pin and the LDOIN pin, with which the LDOIN pin is regulated by the preregulation circuit form with an external NPN. The device can be powered by a battery module with as low as 9V (without OTP programming) on the BAT pin.

Filter the BAT and LDOIN pins separately from the cell. This is to protect against hotplug, in-rush current, and other relevant noise. Recommended filters are RBAT = 30Ω / .25W, CBAT = 0.01µF / 100V for the BAT pin, two resistors in series for best thermal performance: RNPNC1 = 100Ω / .75W, RNPNC2 = 200Ω / .75W and capacitor CNPNC = 0.22µF / 100V for the collector. LDOIN is the input for the external LDO supply for the BQ79616-Q1. Figure 1-1 shows the typical circuit.

Main current path to power the device

Figure 1-1. Power Supply Schematic

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_004.png)

The resistor values and NPN can be further optimized from the reference schematic values based on the min and max module voltages for different projects.

Select the NPN Transistor based on the following criteria:

1. Collector-emitter breakdown voltage (BVCEO) &gt; 80-100V (or the module voltage, plus any derating)
2. DC gain (β, or approximately equal to hfe (AC gain)) &gt; 80 at the expected load current
3. Collector-based capacitance &lt; 35pF at typical base-voltage range
4. Power handling ≥ 1W
5. Current handling &gt; 100mA

The resistor RNPNB in Figure 1-1 serves several purposes:

1. Limits inrush current
2. Shares some power dissipation away from the NPN transistor
3. Combine with the CNPN to serve as a filter

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_005.png)

## where

- VBAT(min) is minimum battery module voltage which depends on the number of cells in series and minimum voltage per cell
- VCE(SAT) = VCE min at VBE(on), from transistor data sheet
- ILOAD is inrush current during startup or maximum active current and any external loading on CVDD

Connect the filter on the LDOIN supply (CLDOIN ) for stability. Use CLDOIN = 0.1µF with a voltage rating of 10V.

## 2 AVDD, CVDD Outputs and DVDD, NEG5, REFHP and REFHM

AVDD, CVDD, and DVDD are regulated outputs derived from the LDOIN input. Each of these regulator outputs have a bypass capacitor to avoid noise with a 10% tolerance due to the fact that a larger capacitance slows startup. REFHP is an internal reference voltage and NEG5V is a regulated voltage provided by an internal charge pump.

Each regulator provides power for delicate internal subsystems. Do not connect external circuitry or additional loads to these regulators beyond those described in the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet.

Place the bypass capacitors of the following pins as close to the device pins as possible to make sure of proper performance, especially the REFHP capacitor. TI recommends to help performance with derating and emissions performance to utilize a small capacitor in parallel with each bypass LDO capacitor of 10-22%. For example, on CVDD, TI recommends both 22nF and 100nF capacitors in parallel with 4.7μF decoupling capacitor to help reduce emissions. These need to be designed extremely close to the pins of the IC in the layout for best effect.

## 2.1 Base Device

- AVDD is a 5V regulated output which supplies internal circuits. AVDD must be bypassed to AVSS with a 1µF/10V capacitor. Do not connect any additional loads to AVDD.
- CVDD is a power supply for stack communication and tied to internally as I/O power supply. CVDD supplies the stack daisy chain communication transceiver circuit. Bypass CVDD with a 4.7µF/10V and 100nF and 22nF for improved emissions and performance. capacitor to CVSS.
- DVDD is a 1.8V regulated output that is used to power the digital logic inside the chip. Connect with a 1μF/10V capacitor to DVSS. Do not connect any additional loads to DVDD.
- NEG5V is a -5V supply provided by an internal charge pump. Connect with a 0.1µF/10V capacitor to AVSS.
- REFHP is a precision reference output pin. A 1µF/10V bypass capacitor must be connected from REFHP to REFHM directly for proper operation of the part.
- REFHM is the precision reference ground for the internal precision reference. Connect DVSS, CVSS, ADC\_AVSS, REFHM, and AVSS externally. All VSS pins must not be left unconnected.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

迎

[www.ti.com](https://www.ti.com/)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_006.png)

## Note

TI recommends to add 470nF/16V from CB16 to BAT for hotplug robustness not shown in figure. See the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet for details.

## 2.2 Design Summary

- Decouple bypass capacitors on AVDD, CVDD, DVDD, and REFHP pins to the ground plane. Refer to layout guidelines for details.
- Bypass the NEG5V pin to AVSS with a 0.1µF/10V capacitor.
- Put all capacitors as close to pins as possible.

Figure 2-1. Regulator Connection for Base Device

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_005.png)

## 3 OTP Programming

There are memory locations that are programmable in non-volatile memory (NVM) using OTP (One Time Programmable). The memory space is divided in two groups: factory space and customer space. The factory space stores the device configurations that are essential for normal operation. This space is not accessible by the host. The customer space contains the default device settings that the host system can customize for the application configuration. This space is readable and programmable by the host.

Follow the procedures found below for OTP programming:

1. Unlock the OTP programming.
- a. Write the following data to OTP\_PROG\_UNLOCK1A to OTP\_PROG\_UNLOCK1D:
- i. OTP\_PROG\_UNLOCK1A &lt;- data 0x02
- ii. OTP\_PROG\_UNLOCK1B &lt;- data 0xB7
- iii. OTP\_PROG\_UNLOCK1C &lt;- data 0x78
- iv. OTP\_PROG\_UNLOCK1D &lt;- data 0xBC
- b. Do another write with following data to OTP\_PROG\_UNLOCK2A to OTP\_PROG\_UNLOCK2D registers.
- i. OTP\_PROG\_UNLOCK2A &lt;- data 0x7E
- ii. OTP\_PROG\_UNLOCK2B &lt;- data 0x12
- iii. OTP\_PROG\_UNLOCK2C &lt;- data 0x08
- iv. OTP\_PROG\_UNLOCK2D &lt;- data 0x6F

## Note

Each block of registers must be written in order (that is A,B,C, then D) with no other writes or reads between. The best practice is to use the same Write command to update. If there is any attempt to update the registers out of sequence or if another register is written/read between writes, the entire sequence must be redone.

2. Check to confirm the OTP unlock procedure is successful.
- a. Read to confirm OTP\_PROG\_STAT[UNLOCK] = 1.

## Note

Issuing a Read command after step 1 is allowed, but issuing a [PROG\_GO] must be the next write command after the unlock procedures.

3. Select the proper OTP page and start the OTP programing.
- a. To program page1, set OTP\_PROG\_CTRL[PAGESEL][PROG\_GO] = 0x01, OR
- b. To program page2, set OTP\_PROG\_CTRL[PAGESEL][PROG\_GO] = 0x03.
4. Wait tPROG for the OTP programming to complete.
5. Check to make sure there is no error during OTP programming. The following bits are expected to be '1' after a successful OTP programming.
- a. OTP\_PROG\_STAT[DONE] = 1, OTP programming is done. No other bit shall be set in this register.
- b. If page 1 is programmed, OTP\_CUST*\_STAT*[PROGOK], [TRY], [OVOK] and [UVOK] bits shall be '1'. Other bits shall be '0'.
- c. If page 2 is programmed, OTP\_CUST1\_STAT[LOADED], [PROGOK], [TRY], [OVOK], and [UVOK] bits shall be '1'. Other bits in OTP\_CUST*\_STAT shall be '0'.
6. Issue a digital reset to reload the registers with the updated OTP values.
- a. CONTROL1[SOFT\_RESET] = 1

During the programming procedure, the device performs a programming voltage stability test prior to actually programming the OTP. If a programming voltage fails the stability test, the device does not set the OTP\_CUST*\_STAT[TRY] bit, giving the customer another attempt to program the page again.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_007.png)

[www.ti.com](https://www.ti.com/)

If the host incorrectly selected a page for programming, then the OTP\_PROG\_STAT[PROGERR] bit is set. This indicates that the selected page is not available to be programmed. Select the correct page and retry programming.

## 4 Cell Voltage Sense (VCn) and Cell Balancing (CBn)

Voltage monitoring is done through the VCn pins while cell balancing is done through the CBn pins. Each of the VCn pins is measured by the main SAR ADC to make sure of the most accurate readings. Getting an accurate reading for these connections is critical to achieve maximum performance so adhere to the following design recommendations.

## 4.1 Cell Voltage Sense (VCn)

The VCn pins are the primary inputs for measuring the cell voltages. VC0 is the low side reference to the negative terminal of the bottom cell and VC16 is the high side reference to the positive terminal of the top cell.

Connect the inputs to the cells using series resistors to limit current into the pins and protect the IC from system transients. When fewer than 16 cells are used on the BQ79616-Q1, the lower cells must be used in order. Unused cell connections can be found in the scenarios shown in Figure 4-1.

Recommended filter capacitor for VCn pins is 0.47μF/16V.

100Ω is recommended as a series filter resistor for VCn pins. 100Ω is an optimized value to protect VCn pins from hotplug and provide better filtering. But, if another value is considered other than 100Ω, then simulate for selecting the optimized value for the system.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_008.png)

## Note

TI recommends to add 470nF/16V from CB16 to BAT for hotplug robustness not shown in the figure. See the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet for details.

Figure 4-1. Cell Voltage Monitoring

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

## 4.2 Cell Balancing (CBn)

The device integrates internal cell balancing MOSFETs (CBFET) across each CB channel to enable passive cell balancing. The cell balancing control can be configured in two ways: auto and manual - using the BAL\_CTRL2[AUTO\_BAL] bit. To set up cell balancing control, refer to Set Up Cell Balancing section in the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet.

The balancing current is determined by the cell voltage, the external resistor in series with the CB pin, and the internal CBFET RDS(ON). This document introduces how to select an external resistor to get the desired cell balancing current.

## 4.2.1 Non-Adjacent Cell Balancing

Auto balancing control is configured by setting [AUTO\_BAL] = 1. In auto balancing control mode, CBFETs are enabled in an odd and even sequence.

Figure 4-2. Internal CB Diagram (no adjacent cell balancing)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_010.png)

Figure 4-2 shows the cell balancing current path. Cell balancing current (ICB ) is dependent on cell voltage (VCELL) and the resistance of the balancing path (2 × RCB+ RDS(ON)). The equation is shown in Equation 2. RCB is the series resistor. RDS(ON) is the resistance of the internal FET when on. The higher the total resistance of the path, the lower the cell balancing current that flows.

To get a target cell balancing current, RCB can be chosen by following two steps.

Step 1 : Select RCB value

The RCB value can be calculated considering the desired cell balancing current at the highest RDS(ON) at the highest operating temperature using the equation in Equation 3.

Step 2 : Calculate RCB power rating www.ti.com Power rating for RCB can be calculated with the highest cell balancing current at the minimum RDS(ON). An example calculation for how to select the value of RCB and power rating to get the desired cell balancing current is shown in Figure 4-3.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_011.png)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Assume desired cell Balancing Current is 240 mA at 80°C with 4.2 cell voltage.

## 1. Calculation for Cell Balancing Resistor

VBAT = 4.2V → Voltage of Battery

IcB = 240 mA → Desired Cell Balancing Current

Rps(on) = 5 Ω → Maximum Resistance of Internal FET at 80°C

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2. Calculation for Power rating for RcB at worst case

VBAT = 4.2V → Voltage of Battery

RcB = 6.25 Ω → Cell Balancing Resistor

Rps(on)= 1.25 Ω → Minimum Resistance of Internal FET at Cold Ambient

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

RCB Power rating = 0.58 W

Figure 4-3. Cell Balancing Resistor Example Calculation

Passive balancing dissipates heat to the die, increasing the die temperature as balancing current increases. Refer to the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet for the recommended maximum balancing current according to the ambient temperature.

## 4.2.2 Adjacent Cell Balancing

Manual balancing control is configured by setting [AUTO\_BAL] = 0. In manual balancing control mode, the host can enable two consecutive CBFETs, and a maximum of eight total CBFETs can be enabled (see Figure 4-4).

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

However, when two adjacent channels are enabled, the balancing current is twice as high or higher than the non-adjacent channel balancing current. The system designer shall take this into account if adjacent cell balancing is used. See Equation 4 to select the right adjacent cell balancing series resistor (RCB).

Figure 4-4. Adjacent Cell Balancing

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_012.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_013.png)

## 4.2.3 Cell Balancing With External FET

<!-- formula-not-decoded -->

The BQ79616-Q1 can handle 240mA max at 105°C. If more current is needed, then the cell balancing pins are able to support an external FET as shown in Figure 4-5. Cell balancing current with external FET can be calculated using equation below. Details for that configuration can be found in the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet.

There are a few things to keep in mind regarding external balancing. First, the series resistors between the FET and pin are there to protect the pins during hot plug and the capacitor is there to make sure that the FET does not turn on during hot plug. Be aware of the following conditions that need to be considered when selecting the FET.

1. The VDS must be selected based on derating requirements determined by the stack voltage.
2. The VGS threshold must be low enough to turn on with the lowest battery voltage planned for balancing. The gate of the MOSFET sees half of the battery voltage, so the VGS of the MOSFET must be selected to provide sufficiently low RDS(ON) at half of the lowest battery voltage.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

Figure 4-5. External FET Cell Balancing

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_014.png)

## 4.3 Using Fewer Than 16 Cells

As stated earlier, the BQ79616-Q1 can support between six and 16 cells. The VCn inputs must be used in ascending order starting with VC0. See Figure 4-6 scenarios for more information on connecting fewer than 16 cells.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_015.png)

[www.ti.com www.ti.com](https://www.ti.com/)

(a) Customized PCB for certain channels applications - Short unused pins to BAT Pin

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_016.png)

(c) One PCB for all channels applications - For BQ79616: Configured for 15 VC and CB If floating the unused VC and CB pins, capacitors in black corresponding to CB pins need to be populated, but capacitors and resistors in grey corresponding to VC and CB pins need to be unpopulated

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_017.png)

(b) One PCB for all channels applications - For BQ79616: Configured for 16 VC and CB

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_018.png)

(d) One PCB for all channels applications - For BQ79612: Configured for 12 VC and CB If floating the unused VC and CB pins, capacitors in black corresponding to CB pins need to be populated, but capacitors and resistors in grey corresponding to VC and CB pins need to be unpopulated

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_019.png)

Figure 4-6. Connecting Fewer Than 16 Cells

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_020.png)

## 4.3.1 Design Summary

- Cell balancing current, ICB, is dependent on cell voltage and resistance of the path.
- The CBn resistor value must be selected considering desired balancing current at the highest ambient temperature. Use the formula in Equation 3 to calculate the correct resistance.
- A 100Ω resistor is recommended as a series resistor for VCn pins. A 100Ω resistor is an optimized value to protect VCn pins and provide accuracy in cell voltage readings.
- VCn input connections must start with the lowest input, VC0, and then be connected in ascending order.
- CBn inputs used must correspond to the VCn used.
- For more than 240mA of charging current, use an external FET. Details can be found in the BQ79616-Q1 data sheet.

## 5 Bus Bar Support

The device supports bus bar measurement in two type of connections. First, the bus bar can be connected to a dedicated bus bar channel through the BBP and BBN pins. Alternatively, the bus bar can be connected to a VC channel. This section introduces both methods of connecting the bus bar and cell balancing handling for each configuration.

## 5.1 Bus Bar on BBP or BBN

The device provides a dedicated bus bar channel through the BBP or BBN pins for bus bar connection and measurement. This is a floating channel allowing the bus bar to be connected to any cell except the bottom cell of a module.

Instead of using the BBP or BBN with the bottom cell (VC1-VC0), the bus bar can be connected to the BBP or BBN of the lower stack device alternatively as shown as Figure 5-1.

Using the bus bar channel maximizes the use of cell channels in the device across different module size. As described in Figure 5-2, a 4 x 12 cell can be monitored by three CMC without wasting any pins while connecting the bus bar to BBP/BBN.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_021.png)

Figure 5-1. Alternative Bus Bar Connection to the Lower Stack Device

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_022.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_023.png)

The * represents the bus bar location at each module size example.

Figure 5-2. Example of BBP/BBN Connections at Different Module Size

## 5.2 Typical Connection

When the bus bar connected to BBP or BBN, this allows for a single cell channel (VC channel) to be shared with a cell and a bus bar (see Figure 5-3). Usually, such a connection introduces additional IR error to the cell measurement to the system. The dedicated bus bar channel through BBP or BBN supported in the device allows the host to measure the bus bar voltage to obtain the actual cell measurement.

The connection in Figure 5-3 applies if the bus bar is connected to any middle VC channel. That is, in a single device, there is a cell connected above and below the BBP or BBN channel. To support hotplug on the bus bar channel, the device only requires a 400Ω filter resistor each on BBP or BBN pins and a 0.47µF/16V differential capacitor across BBP or BBN pins.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_024.png)

Note

TI recommends to add 470nF/16V from CB16 to BAT for hotplug robustness not shown in above figure. See the data sheet for details.

Figure 5-3. BBP or BBN Connection With Bus Bar Connected in any Middle VC Channel

If the bus bar connected to BBP or BBN is placed at the top of a module (see Figure 5-4), then this connection is the exception in the BBP/N case that a cell channel is NOT being shared. In this connection, actual cell measurements are made through the VC channels and the host does not require performed addition calculation.

The connection in Figure 5-4 applies if the bus bar is connected to the top of the module, where in a single device, no cell is connected above the bus bar. To support hotplug on the bar channel, besides the 400Ω filter resistor each on BBP or BBN pins and a 0.47µF/16V differential capacitor across BBP or BBN pins. If the bus bar is used above the top cell, then an additional 0.47µF/16V differential capacitor is needed to connect from BBN to the top CB pin. This additional capacitor forms a complete capacitor ladder from all the cells in the module to the bus bar, allowing high spike voltage during hotplug to distributor across the capacitor ladder.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

www.ti.com Note

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_025.png)

TI recommends to add 470nF/16V from CB16 to BAT for hotplug robustness not shown in figure. See theBQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet for details.

Figure 5-4. BBP or BBN Connection With Bus Bar Connected Above Top of a Module

## 5.2.1 Cell Balancing Handling

Since the bus bar is shared with a cell to a cell channel, there is no special handling on the cell balancing control. The host shall be aware that additional IR error is introduced to the VCB\_DONE detection (through VC channel) on the shared channel.

## 5.3 Bus Bar on Individual VC Channel

With the bus bar connected to a VC channel individually, the upper CB pin on that channel shall be left floating to avoid forward biasing the internal CBFET (see Figure 5-5 connection). This connection applies to the bus bar connecting to any middle VC channel individually. That is, in a single device, there is a cell connected above and below the VC channel with the bus bar connected.

To make sure of hotplug performance, the CB channel where the bus bar is connected still has the differential capacitor CCB in Figure 5-5 , even if the upper CB pin is floating. This capacitor forms a complete capacitor ladder from all the cells and the bus bar connected to the device, allowing high voltage spikes during hotplug to be distributed across the capacitor ladder.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_021.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_026.png)

Note

TI recommends to add 470nF/16V from CB16 to BAT for hotplug robustness not shown in figure. See the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet for details.

Figure 5-5. Bus Bar Connected Any Middle Individual VC Channel

If the bus bar is connected to above the top of a module to an individual VC channel (see Figure 5-6 connection), then the upper CB pin on that channel is left floating, but the CB differential capacitor (CCB in Figure 5-6) is still connected. Additionally, an RC filter is connected from the top CB pin to the BAT pin. This additional RC filter (using the same RC values as the other RC filters on the CB pins) is to make sure a complete capacitor ladder. This is used to distribute high voltage spikes with the same RC constant as the rest of the CB pins during a hotplug event.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

www.ti.com Note

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_027.png)

TI recommends to add 470nF/16V from CB16 to BAT for hotplug robustness not shown in figure. See the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet for details.

Figure 5-6. Bus Bar Connected Individual VC Channel Above the Top of a Module

## 5.4 Multiple Bus Bar Connections

## 5.4.1 Two Bus Bar Connections to One Device

Two bus bars can be connected to VC channels individually as shown in Figure 5-7. The first bus bar is connected to the channel VC4-VC3. CB4 is floated for a cell balancing path. Likewise, the second bus bar is connected to the channel VC6 -VC7. CB7 is also floated. Each bus bar must be at least two channels apart.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_028.png)

Figure 5-7. Two Bus Bars Connections Using Two Different VC Channel

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_029.png)

## 5.4.2 Three Bus Bar Connections to One Device

A BQ79616-Q1 supports up to three bus bar connections to a single device. An additional bus bar can be connected to dedicated bus bar pins (BBP/N) while connecting two bus bars to each VC channel as described in Figure 5-8. The first and the third bus bars are connected to each channels, VC4-VC3, and VC7-VC6, respectively. The second bus bar is connected to the dedicated bus bar pins, BBP/N.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

Figure 5-8. Multiple Bus Bar Connections Utilizing the BBP/N Pins

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_030.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_005.png)

## 5.4.3 Cell Balancing Handling

When the bus bar is connected to the VC channel, the system must turn on two adjacent internal FETs to balance the cell above the bus bar as shown in Figure 5-9. The system must use manual balancing mode to turn on two adjacent FETs. Since two series CB FETs must be turned on to cell balance, the balancing current is slightly lower. See Equation 5 to calculate cell balancing current when the bus bar is connected to the VC channel.

Figure 5-9. Internal CB Diagram With the Bus Bar Connection

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_031.png)

<!-- formula-not-decoded -->

## 6 TSREF

TSREF is a supply reference to bias external NTCs and can be bypassed to AVSS with a 1µF/10V capacitor. When thermistors are used for temperature measurements, connect TSREF to the top of the resistor divider network as described in Section 7.1. The BQ79616-Q1 supports ratiometric measurement through the main ADC. The integrated OT, UT comparators have a wide range of programmable thresholds to support different R1 and R2 resistor ratios. Do not connect TSREF to other pins for power.

## 7 General Purpose Input-Output (GPIO) Configurations

There are eight GPIO pins available on BQ79616-Q1. These pins can be used for temperature measurement, measurement of DC analog signals, digital input or output, and SPI. The behavior of the pins can be selected in the non-volatile RAM as described in the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional www.ti.com Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet. If the signal goes off the board, then protect the input using a zener diode at the pin.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_032.png)

Unused GPIO pins have an external 10kΩ pulldown resistor to AVSS.

## 7.1 Ratiometric Temperature Measurement

Ratiometric voltage measurement is most commonly used for external temperature sensing. To measure an external temperature sensor, the GPIO connections must have a resistor divider from TSREF to AVSS with the GPIO connected to the center tap. The NTC can then be connected from TSREF to GPIO or from GPIO to AVSS. Optionally, the GPIO input can be filtered using a low-pass filter (CGPIO and RGPIO) to reduce highfrequency noise as shown Figure 7-1.

Pass criteria: No change of the ratiometric measurement before or after changing the TSREF voltage

Figure 7-1. GPIO Ratiometric Measurement

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_033.png)

The main ADC measures TSREF and GPIO voltages in the round robin. A microcontroller calculates the ratiometric voltage by Equation 6.

Temperature accuracy is affected by ADC measurement error and external component error. Using ratiometric measurement greatly reduces the ADC measurement error. Furthermore, the better the tolerance of the external circuit, the more accurate temperature sensing.

<!-- formula-not-decoded -->

## 7.2 SPI Mode

One use of GPIO [7:4] is as a SPI master. Connection of the pins in SPI mode is the same as general digital connections, but SPI configuration replaces the GPIO pin configuration. Figure 7-2 shows an example connection of GPIO[7:4] for digital signaling or SPI mode.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_034.png)

device

Figure 7-2. Example SPI Master Connections

Tie unused GPIO pins to AVSS through a 10kΩ pulldown resistor. By default, the GPIO pins are configured internally as an input with a weak pulldown resistor, so program the GPIO configuration appropriately to avoid leakage current.

## 7.2.1 Support 8 NTC Thermistors With SPI Slave Device

A single 4-channel 2:1 switch can be use to switch between SPI and thermistor input. Single switches available at TI and can be powered from CVDD as shown in Figure 7-3.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

Figure 7-3. 8 NTC Thermistors With SPI Slave Device

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_035.png)

Enabling TSREF selects the B paths of the switch, which are all connected to NTCs for temperature measurement. Disabling TSREF disables all the thermistor networks, and also selects the A paths of the switch to allow SPI communication. This configuration has no impact to the temperature measurement diagnostic and has ASIL-D compliance on the temperature measurement.

## 7.2.2 Design Summary

1. Connect external temperature sensor to GPIOs using a voltage divider network.
2. GPIO pins used for temperature measurement must have a pullup resistor to TSREF equivalent to the resistance of the NTC at nominal temperature. Each input must also have a 1kΩ resistor and 1µF capacitor.
3. GPIO pins with signals connecting from off-board must use a zener diode clamp.
4. DC voltage readings need a 1kΩ resistor and 1µF capacitor.
5. To use GPIOs in SPI mode, use GPIO4 through GPIO7. Unused GPIOs must be pulled low to GND.
6. GPIO pins are all programmed as inputs with a weak pulldown, leaving the inputs floating. The pins must not be allowed to remain as floating inputs. Reprogram the pins to become outputs or add a pulldown resistor.
7. The BQ79616-Q1 can support 8 NTC thermistors with SPI slave device using 4 channel 2:1 switch and this configuration has no impact to temperature measurement diagnostic.

## 8 Base and Bridge Device Configuration

Single-ended communication lines with the BQ79616-Q1 normally refers to the base device in a stack that communicates with the host microcontroller through SPI and UART (SPI only available using BQ79600-Q1). There are two main ways to configure the base device. The first is using the BQ79600-Q1 as a bridge device as shown in Figure 8-1 and the second utilizes an isolation circuit with the base device as described in Figure 8-2. This document introduces using BQ79616-Q1 as a base device. Refer to the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet and design considerations to use communication extender, bridge device. An overview of how a bridge device is configured as shown in Figure 8-1.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_021.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_036.png)

Ring Enables Fault Feature

Figure 8-1. Communication With the Bridge Device BQ79600-Q1

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_037.png)

Figure 8-2. Using BQ79616-Q1 as Base Device with Isolation Circuit

## 8.1 Power Mode Pings and Tones

## 8.1.1 Power Mode Pings

A ping is a specific high-low-high signal sent from MCU to the base device through the RX pin. Pings are used on the base device as only the base device is connected to the host from which the UART RX is accessible. The device detects the low pulse duration of the ping to differentiate between the different pings. There are total of 4 different pings as shown in Figure 8-3.

- a WAKE ping through RX pin
- a SHUTDOWN ping through RX pin
- a SLEEPtoACTIVE ping through RX pin
- a HW\_RESET ping through RX pin

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

Figure 8-3. Communication Pings

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_038.png)

## 8.1.2 Power Mode Tones

Stack devices are woken up by tones. A tone is a set number of specific couplets sent through the differential communication lines COMH and COML. When a device wakes up by a tone, this is not a base device but must be a stack device. The device configures the COMH and COML port based on stack or base detection accordingly. There is a total of four different power modes related to tones as seen in Figure 8-4. In addition, there are two extra tones related to FAULT. See Device Fault Summary, Fault Tone, and Heartbeat sections in the BQ79616-Q1 data sheet for details.

- a WAKE tone through COMH/L
- a SLEEPtoACTIVE tone through COMH/L
- a SHUTDOWN tone through COMH/L
- a HW\_RESET tone through COMH/L

Figure 8-4. Communication Tones

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_039.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

## 8.1.3 Ping and Tone Propagation

During normal operation, a host can send a WAKE or SLEEPtoACTIVE ping to the base device and the corresponding tone is generated to the rest of the stack devices as seen in Figure 8-5. During system development, if there is a need to send WAKE or SLEEPtoACTIVE to only some of the devices in the daisy chain, then the host can use the CONTROL1[SEND\_WAKE] or CONTROL1[SEND\_SLPTOACT] bits. The SHUTDOWN and HW\_RESET ping or tone are mostly used as a communication recovery attempt. Hence these pings/tones are non-propagable.

Figure 8-5. Diagram for Ping or Tone Propagation

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_040.png)

## 8.2 UART Physical Layer

The device can operation as a standalone device such as in a multidrop configuration (DEV\_CONF[MULTIDROP\_EN] = 1) or as a base or stack device in a daisy chain configuration (DEV\_CONF[MULTIDROP\_EN] = 0). In multidrop configuration, the daisy chain communication is disabled and the host communicates only with a single device through the UART interface. This section introduces the UART interface configuration focusing on daisy chain communication.

The UART sends data on the TX pin and receives data on the RX pin. When idle, the TX and RX are high. The UART interface requires that RX is pulled up to CVDD through a 100kΩ resistor on the base device. The RX is pulled up on the BQ79616 side. Do not leave RX unconnected. Make sure RX is connected directly to CVDD for stack devices.

TX is disabled in stack devices, but must be pulled high through a 100kΩ resistor on the host side on the base device to prevent triggering an invalid communication frame when the communication cable is not attached, or during power-off or SHUTDOWN state when TX is high impedance. TX is always pulled to CVDD internally while in ACTIVE or SLEEP mode, whether enabled or disabled. Leave TX unconnected if not used in stack devices. NFAULT is an active low fault indicator that, in the event of a fault, pulls low to signal to the host that a fault has www.ti.com occurred. Due to this fact the NFAULT pin has a 100kΩ pullup resistor to CVDD. If the device is a stack device, then NFAULT can be left unconnected.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_011.png)

Refer to Table 8-1 for information on base device communication using a digital isolator.

Table 8-1. UART Physical Layer Check List

| List | Pin | Base Device | Stacked Devices | Top of Stack Device |
| - | - | - | - | - |
| 1 | RX | 100kΩ pullup to CVDD, 51pF to GND | CVDD | CVDD |
| 2 | TX | 100kΩ pullup on Host side | Float | Float |
| 3 | COMML+ | COMMH+ of Top of Stack | COMMH+ of lower device | COMMH+ of lower device |
| 4 | COMML- | COMMH+ of Top of Stack | COMMH- of lower device | COMMH- of lower device |
| 5 | COMMH+ | COMML+ of upper device | COMML+ of upper device | COMML+ of Base Device |
| 6 | COMMH- | COMML- of upper device | COMML- of upper device | COMML- of Base Device |
| 7 | NFAULT | 100kΩ pullup to CVDD | Float | Float |

## 8.2.1 Design Considerations

- For the base device, provide a 100kΩ pullup resistor for RX and NFAULT to CVDD and RX on the host side.
- For stacked devices, leave NFAULT and TX floating
- For stacked devices, tie RX to CVDD
- When BQ79600-Q1 is used as a bridge device, also pull up RX and TX with a 100kΩ resistor, and NFAULT with a 100kΩ resistor to CVDD.

## 9 Daisy-Chain Stack Configuration

In the stacked configuration, the main microcontroller first communicates through a BQ79616-Q1 base device using the UART communications interface. Communication is then relayed up the chain of connected slave BQ79616-Q1 devices using a proprietary differential communications protocol over AC-coupled differential links interconnected by the COMMH± and COMML± pins. A high level diagram of this can be seen in Figure 9-1.

In the case of BQ79616 -Q1 working with a BQ79600-Q1 communication extender, the host microcontroller first communicates through a bridge device by UART or SPI. A command is then moved up the chain of connected slave BQ79616-Q1 devices through COML and COMH pins vertically as described in Figure 9-2.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_028.png)

Figure 9-1. Daisy Chain Structure With a Base Device

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_041.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

Figure 9-2. Daisy Chain Structure With a Bridge Device

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_042.png)

## 9.1 Communication Line Isolation

Many applications require multiple, daisy-chained BQ79616-Q1 devices that are separated by cables or located on the same PCB. The cables can introduce additional challenges and additional components are needed for noisy environments. There are three different implementations to this noise problem: capacitor-only isolation, capacitor and choke isolation, and transformer isolation. Each of these implementations are detailed in the following sections.

## 9.1.1 Capacitor Only Isolation

The first implementation, capacitor isolation, is the best choice for reducing noise and providing voltage isolation for ICs that are located on the same PCB. Figure 9-3 shows how this configuration look for two ICs connected on the same PCB. A 10kΩ termination resistor must be added at the high and low sides. In addition a 49Ω resistor and 220pF capacitor must be added on each line on both the high and low side to proved additional filtering. The capacitor must be 2.2nF with a voltage rating twice that of the local cell stack. For example, for a 400V system, a 800V capacitor is needed. This configuration must be done on both the COMM± lines.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_021.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_043.png)

Components Required for Cap Coupled Daisy Chain on the same PCB

Figure 9-3. Components Required for Cap Coupled Daisy Chain in the Same PCB

Figure 9-4 shows capacitive coupling isolation between two separated PCB. The capacitor needs to be 2.2nF with a voltage range twice that of the local cell stack. One capacitor is sufficient, but if additional safety is needed, then two can be used; one at each end of the cable. In this case, a 220pF capacitor must be used. Capacitance has a direct effect on performance, so all intended and parasitic capacitance must be taken into account when choosing components.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_044.png)

Components Required for Cap Coupled Daisy Chain on different pcb

Figure 9-4. Components Required for Cap Coupled Daisy Chain in Different PCB

## 9.1.2 Capacitor and Choke Isolation

If the cable length is greater than 2m, then the recommendation is that the capacitor only isolation be implemented. Instead, a common mode choke must be added. A single or dual choke can be used. In the dual common-mode filter, a 100µH and 470µH must be used. In a single filter mode, the line must have TDK 51µH 2.8kΩ choke (part number ACT45B-510-2P-TL003).

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_045.png)

Components Required for cap-choke Daisy Chain with Cabling www.ti.com

Figure 9-5. Components Required for Cap-Choke Daisy Chain With Cabling

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_020.png)

## 9.1.3 Transformer Isolation

Transformer isolation is the most effective method for removing common mode noise from the system. The two options for this implementation can be seen in Figure 9-6. The following parameters are recommended for the transformer selection:

- Inductance = 150-600µH
- Isolation Voltage = 2500V, AC

The HMU1228 transformer is recommended and is recommended to be center tapped with a 100pF capacitor. ESD562-Q1 TVS diode can be added optionally for ESD protection.

Figure 9-6. Components Required for Transformer Coupled Daisy Chain

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_046.png)

Regardless of which isolation method is chosen, there are a few things that are common among all of them. First, is the 220pF capacitor and 49Ω resistor before the ESD isolation on both the high and low side on both the positive and negative lines.

Lastly, each design has a termination resistor. The purpose of this resistor is to prevent reflected signals from interfering in the communication. The recommendation is that a 1kΩ be used.

In all of these situations, the recommendation is based off how long the cable between boards is, and in all cases, twisted pair cabling is used between modules. The main purpose of these noise isolation methods is to remove common mode noise from the signal. More details can be found in Section 15.

The recommendation is that with any design that is chosen, that additional ESD protection is added. The ESD562-Q1 is shown in the following sections to provide ESD isolation on the communication lines.

## 9.1.4 Design Summary

- For devices located on the same PCB, there must be a 2.2nF isolation capacitor on each COMM± line with a voltage rating twice that of the cell stack.
- In addition to the isolation method, there must be a termination resistor at each end of the connection for devices located on the same PCB and for between PCBs.
- There are three types of noise isolation methods that can be employed when communicating through a cable:
1. Capacitor-only isolation
- a. Only recommended for cables less than 2m
2. Capacitor and choke isolation
- a. Cables longer than 2m
- b. Part number: ACT45B-510-2P-TL003 for single mode choke
3. Transformer Isolation
- a. HMU1228 and HM2147 transformer is recommended
- ESD562-Q1 is recommended between communication lines to add ESD isolation
- Any capacitance present on the communication line can have an effect on the performance. All intentional and parasitic capacitance must be calculated and taken into effect.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

## 9.2 Ring Communication

The daisy chain communication for the device allows for the use of a ring architecture. In this architecture, a cable break between two devices does not prevent communication to all upstream devices as in a normal non-ring scheme. When the host detects a broken communication interface, the device allows the host to switch the communication direction to communicate with devices on both sides of the break. This allows for safe operation until the break in the lines is repaired.

The CONTROL1[DIR\_SEL] controls the communication direction. The devices reconfigure the COMH and COML ports depending on the [DIR\_SEL] and the [TOP\_STACK] setting. The auto addressing procedure is needed to readdress the device addresses for the reverse communication direction.

The following is an example on how to change the communication direction to [DIR\_SEL] = 1 to the entire daisy chain.

1. Host clears the previous Top of Stack device
- In this step, the previous TOS device re-enable COMH.
2. Host sends single device write to change the base device [DIR\_SEL] = 1 (see figure (a) in Figure 9-7)
- The base device disables the COMH and enable the COML
3. Host sends broadcast write reverse direction to change the rest of the devices' [DIR\_SEL] = 1 (see figure (b) in Figure 9-7)
- In this step, the entire daisy chain is set up to communicate in the [DIR\_SEL] = 1 direction (that is, each device set up to transmit command frames sent by host from the COMH to the COML)
4. Host performs auto addressing procedure to set up device address in the DIR1\_ADDR register (see figure (c) in Figure 9-7)
- Unless the devices have been reset, host can skip the dummy read/write steps to synchronize the DLL in the auto addressing procedure
5. Host sets up the new Top of Stack device (see figure (c) in Figure 9-7)
- In this step, the new ToS device disables the COML transmitter

Figure 9-7. Example of Changing Communication Direction in Daisy Chain

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_047.png)

Ring architecture also enables fault status transmitting in sleep. In SLEEP mode, the following fault detections are still active.

- Customer and factory OTP shadowed registers CRC check
- Device thermal warning
- Power supplies OV, UV, oscillation detection

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_048.png)

## [www.ti.com](https://www.ti.com/)

- If OVUV protectors are enabled, cell OV and UV detection
- If OTUT protectors are enabled, thermistors OT and UT detection

Since communication is not available in SLEEP, the device provides an option to transmit the fault status through Heartbeat (device in no fault state) and Fault Tone (device in fault state). These tones are transmitted in the same direction as a communication command frame, which is based on the CONTROL1[DIR\_SEL] setting. For the tone signal to return back to the base device (so NFAULT can be triggered if needed), a ring architecture must be used to support transmitting the fault status in SLEEP mode.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_049.png)

- (a) Traveling direction with [DIR\_SEL] = 0

(b) Traveling direction with [DIR\_SEL] = 1

Figure 9-8. Heartbeat or Fault Tone Traveling Direction

## 9.3 Reclocking

The BQ7916-Q1 regenerates each communication signal before BQ7916-Q1 sends the signal on to the next device. This feature is to prevent compression of a signal as this moves up the stack. Reclocking generates an waveform but also adds about 4µs of delay.

Figure 9-9 shows images from an experiment in which 18 BQ79606-Q1 EVMs were daisy chained together to observe the bit compression. There is almost no difference in the bit-width between the base and top of stack board. This is due to the reclocking feature. Reclocking allows for a longer daisy chain cable between board and also increased the number of stackable devices in the system.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_021.png)

Figure 9-9. Reclocking Bit Compression Example

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_050.png)

## 9.3.1 Design Summary

- Ring architecture allows for the host to continue communication to all devices in the event of a break.
- Re-clocking the communication signals preserves the signal integrity but adds delay into the design.

## 10 Multidrop Configuration

An alternative to the daisy-chain configuration is multi-drop. Here, all of the BQ79616-Q1 devices are seen as base devices and connected in parallel. This configuration does not support auto-addressing. Figure 10-1 shows a high level representation of this set up. For more information, refer to the BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector data sheet.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

www.ti.com LV System

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_051.png)

## Note

TI recommends to add 470nF/16V from CB16 to BAT for hotplug robustness not shown in above figure. See the data sheet for details.

Figure 10-1. Multi-Drop Configuration

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_005.png)

## 11 Main ADC Digital LPF

Each differential VC channel measurement is equipped with a post-ADC LPF. The LPFs have much lower cutoff frequency (fcutoff). There are 7 fcutoff options: 6.5Hz, 13Hz, 26Hz, 53Hz, 111Hz, 240Hz, and 600Hz, configurable through the ADC\_CONF1[LPF\_VCELL2:0] setting. Once an fcutoff value is selected and the LPFs are enabled by setting ADC\_CTRL1[LPF\_VCELL\_EN] = 1, the same fcutoff setting applies to all VC channel measurements. Configure the post ADC low-pass filter cut-off frequency for VCELL measurement as shown in Table 11-1.

The differential BBP and BBN measurement also has a digital LPF, enabled by the ADC\_CTRL1[LPF\_BB\_EN] bit. The LPF for the BB channel has the same seven fcutoff options as for the VC measurements. Since the signal across the bus bar can be noisier than the VC measurement and needs a different fcutoff setting than the VC channel, the device provides a separate LPF configuration parameter, ADC\_CONF1[LPF\_BB2:0], for the BB channel, allowing the host to set a different fcutoff for the BB and VC measurements. Configure the post ADC low-pass filter cut-off frequency for bus bar measurement by referring to Table 11-1.

Table 11-1. Main ADC LPF fcutoff for VCELL and Bus Bar Measurement

| ADC_CONF1[LPF_VCELL 2:0], ADC_CONF1[LPF_BB 2:0] | Cut-Off Frequency | Settling Time |
| - | - | - |
| 0x0 | 6.5Hz | 154ms |
| 0x1 | 13Hz | 77ms |
| 0x2 | 26Hz | 38ms |
| 0x3 | 53Hz | 19ms |
| 0x4 | 111Hz | 9ms |
| 0x5 | 240Hz | 4ms |
| 0x6 | 600Hz | 1.6ms |
| 0x7 | 240Hz | 4ms |

## 12 AUX Anti Aliasing Filter (AAF)

The AUX ADC path serves as a redundancy path to the main ADC measurement on cell voltage measurements and the bus bar measurement. This also has the front end filters of a BCI filter and an AAF filter in the AUX ADC path. However, unlike the main ADC path with an individual front end filter for each channel, the cell voltages (taken from the CB0 to CB16 pins) and bus bar (taken from BBP and BBN pins) inputs in the AUX path are multiplexed to share the same BCI filter and AAF filter.

Because the front end filters are shared, the device has to wait for the AAF filter to settle before making any valid CB channel or BB channel measurement. The default AAF fcutoff is 1.3kHz as in the main ADC path, which translates to additional 4ms settling time to complete a single CB or BB channel measurement. As this AUX path is intended for diagnostic use as an option for the MCU to reduce the diagnostic time, the device provides four AAF settling time options as seen in the Table 12-1. The settling time is configured by the ADC\_CONF1[AUX\_SETTLE1:0] bits. Configure the AUX CELL settling time as listed in Table 12-1. If a longer settling time is allowed, then the measurement is more accurate.

Table 12-1. AAF Settling Time

| ADC_CONF1[AUX_SETTLE 1:0] | Settling Time |
| - | - |
| 00 | 4.3ms |
| 01 | 2.3ms |
| 10 | 1.3ms |
| 11 | 300µs |

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_052.png)

## 13 Layout Guidelines

The layout for this device must be designed carefully. Design outside these guidelines can affect the ADC accuracy and EMI performance. Care must be taken in the layout of signals to and from the device to avoid coupling noise onto sensitive inputs. The layout of ground and power connections, and make communication signals carefully.

## 13.1 Ground Planes

Establish a clean grounding scheme to make sure of best performance of the device. There are three ground pins (AVSS, DVSS, CVSS) for the internal power supplies of the device and one ground reference (REFHM) for the precision reference. There are noisy grounds and quiet grounds that are separated in the layout initially and joint together in a lower PCB layer. The external components (for example, bypass capacitors) are tied to the proper grounding group if possible to keep the separation of noisy and quiet grounds apart.

- AVSS ground:
- Bypass capacitor for these pins: BAT, VC0, CB0, LDOIN, TSREF
- Package lower pad
- DVSS ground:
- Bypass capacitor for DVDD
- GPIO filter capacitor (if used). This can also connect to AVSS ground plane if needed
- CVSS ground:
- Bypass capacitor for CVDD
- The bypass capacitors for COMHP/N and COMLP/N
- REFHM ground:
- Bypass capacitor for REFHP
- If possible, then separate out REFHM from AVSS on the signal connection layer and reconnect REFHM to the AVSS ground plane on a lower layer

Even on a PCB layer that is mainly for signal routing, a best practice to have as small an island of ground pour as possible to provide a low impedance ground, rather than simply by down the ground trace to an lower ground plane.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_028.png)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_053.png)

## Note

The vias shown above are on all four layers. Layer 4 is not shown but includes any traces needed for bottom layer components and a solid ground plane otherwise.

Figure 13-1. Grounding Layout Consideration

There is a strong recommendation to have a minimum of four layers in the PCB, with one fully dedicated as an unbroken VSS plane (except thermal reliefs). Avoid placing tracks on this layer to maintain the unbroken integrity of the plane structure.

If multiple devices are placed on the same PCB, then each device has a ground plane with proper layout clearance.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

Figure 13-2. Separate Ground Plane per Device on the Same PCB

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_054.png)

## 13.2 Bypass Capacitors for Power Supplies and References

Place the bypass capacitors of the following pins as close to the device pins as possible to make sure of proper performance, especially the REFHP capacitor. TI recommends to help performance with derating and emissions performance to utilize a small capacitor in parallel with each bypass LDO capacitor of 10-22%. For example, on CVDD, TI recommends both a 22nF and 100nF capacitors in parallel with 4.7μF decoupling capacitor to help reduce emissions. These need to be designed extremely close to the pins of the IC in the layout for best effect.

- REFHP, BAT, LDOIN, AVDD, DVDD, CVDD, TSREF, NEG5V

## 13.3 Cell Voltage Sensing

Cell voltage sensing traces (VC pins and CB pins) shall be placed in parallel with impedance matching.

The balancing traces (CB pins) are sized properly to carry the maximum balancing current and make sure of proper thermal performance for the application.

TI recommends to use separate cables, connector tabs, and PCB traces for the BAT pin and top VC pin connection. The same applies to the AVSS and VC0 connections. This is to avoid the device current impacting the top and bottom cell voltage measurements.

If the same cable and connector tab are used for the BAT or top VC pins connections and AVSS or VC0 pins connections, then the PCB trace going to the BAT or top VC pins and AVSS or VC0 pins are separated at the connector tabs. The device current goes through the cell to the PCB cable, which can introduce IR error across the cable connection to the top and bottom cell measurements.

## 13.4 Daisy Chain Communication

Maintaining signal integrity while in a stacked configuration is critical to the success of this part. To maximize immunity from interfering signals, there are a couple design choices that need to be made. For transformer based communication, be sure to select a transformer that provides adequate isolation.

1. Keep differential traces as short as possible and as straight as possible. Minimize turns and avoid any looping on the traces.
2. Keep the differential traces on the same layers. Run the trace in parallel with shielding and matching trace impedance.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

3. Place the isolation components close to the connectors.
4. When using capacitive isolation, place the high voltage capacitor of the COMxP/N pair (where x = H, L) close to each other along the parallel traces.
5. Create a keep-out area (no other traces and no ground plane) around the daisy chain components in all PCB layers.

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_055.png)

## Note

The vias go through all 4 layers. Layer 4 is not shown as the bottom layer can include traces for any bottom side components and a solid ground plane otherwise.

## 14 BCI Performance

Bulk Current Injection (BCI) was performed according to the ISO 11452-4 standard. The cable length was 1.7m with a baud rate of 1Mbps. The BCI noise was injected on the communication lines. There were three different isolation methods that were tested: capacitive only, cap and choke, and transformer. Contact a local TI sales representative for further information on BCI performance.

## 15 Common and Differential Mode Noise

X-Y caps are commonly used and can be required for extremely noisy environments.

- Differential mode noise goes out one wire and returns back on another wire. An X capacitor is placed between two lines to suppress the noise.
- Common mode noise goes out from both wires and returns back to the chassis through stray capacitance to ground. A Y capacitor is placed between the chassis as Figure 15-1 illustrates.

Figure 13-3. Daisy Chain Layout Considerations

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

## Battery Pack

Figure 15-1. XY Caps

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_056.png)

## 15.1 Design Consideration

- Device placement is important. The daisy-chain cable must not be resting on the bus bar or metal enclosure surface.

## 16 Summary

This application note provides design recommendations for automotive battery management systems using the BQ7961x-Q1. The system can implement simple, low-cost, differential RC filters on the cell input channels by using integrated front end filters. There are eight GPIOs and auxiliary inputs that can be used for NTC thermistor measurements on the device.

## 17 References

- [Texas Instruments, BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector, data sheet](https://www.ti.com/lit/pdf/SLUSE81)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_009.png)

## 18 Revision History

Changes from Revision A (October 2023) to Revision B (June 2025)

![Image](BQ7961x-Q1%20High%20Voltage%20BMS%20Design%20Recommendations%20%28slvae87b%29_files/img_057.png)

· Updated Daisy Chain Isolation diagrams to include ESD562-Q1.....................................................................29

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2025, Texas Instruments Incorporated
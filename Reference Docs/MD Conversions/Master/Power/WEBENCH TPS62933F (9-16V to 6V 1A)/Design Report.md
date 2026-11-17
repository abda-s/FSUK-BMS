<!-- Converted from Design Report.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](Design%20Report_files/img_001.png)

INSTRUMENTS

## WEBENCH ® Design Report

Design : 3 TPS62933FDRLR

TPS62933FDRLR 14V-22V to 3.30V @ 2A

![Image](Design%20Report_files/img_002.png)

## Electrical BOM

| Name | Manufacturer | Part Number | Properties | Qty | Price | Footprint |
| - | - | - | - | - | - | - |
| Cboot | TDK | C0603X5R1A104K030BC Series= X5R | Cap= 100.0 nF ESR= 70.0 mOhm VDC= 10.0 V IRMS= 0.0 A | 1 | $0.01 | 0201 2 mm 2 |
| Cff | MuRata | GRM1555C1E6R8CA01D Series= C0G/NP0 | Cap= 6.8 pF ESR= 1.0 mOhm VDC= 25.0 V IRMS= 0.0 A | 1 | $0.01 | 0402 3 mm 2 ■ |
| Cin | Taiyo Yuden | MSAST21GBB5106MTNA01 Series= X5R | Cap= 10.0 uF ESR= 5.463 mOhm VDC= 25.0 V IRMS= 2.36768 A | 1 | $0.04 | 0805 7 mm 2 |
| Cinx | AVX | 06033C104KAT2A Series= X7R | Cap= 100.0 nF ESR= 50.0 mOhm VDC= 25.0 V IRMS= 0.0 A | 1 | $0.01 | 0603 5 mm 2 |
| Cout | MuRata | GRM32ER61C476KE15L Series= X5R | Cap= 47.0 uF ESR= 3.037 mOhm VDC= 16.0 V IRMS= 4.59346 A | 1 | $0.17 | 1210_280 15 mm 2 |
| Css | MuRata | GRM155R71A333KA01D Series= X7R | Cap= 33.0 nF ESR= 1.0 mOhm VDC= 10.0 V IRMS= 0.0 A | 1 | $0.01 | 0402 3 mm 2 ■ |
| L1 | NIC Components | NPI52P7R8MTRF | L= 7.8 µH 18.0 mOhm | 1 | $0.54 | IND_NPI52P 445 mm 2 |
| Renb | Vishay-Dale | CRCW0402169KFKED Series= CRCW..e3 | Res= 169.0 kOhm Power= 63.0 mW Tolerance= 1.0% | 1 | $0.01 | 0402 3 mm 2 ■ |
| Rent | Vishay-Dale | CRCW04021M18FKED Series= CRCW..e3 | Res= 1.18 MOhm Power= 63.0 mW Tolerance= 1.0% | 1 | $0.01 | 0402 3 mm 2 ■ |
| Rfbb | Vishay-Dale | CRCW040210K0FKED Series= CRCW..e3 | Res= 10.0 kOhm Power= 63.0 mW | 1 | $0.01 | 0402 3 mm 2 ■ |

VinMin = 9.0V VinMax = 16.0V Vout = 6.0V Iout = 1.0A

Device = TPS62933FDRLR Topology = Buck Created = 2026-10-21 06:30:57.079 BOM Cost = $1.32 BOM Count = 12 Total Pd = 0.28W

Tolerance= 1.0%

![Image](Design%20Report_files/img_003.png)

![Image](Design%20Report_files/img_004.png)

| Name | Manufacturer | Part Number | Properties | Qty | Price | Footprint |
| - | - | - | - | - | - | - |
| Rfbt | Vishay-Dale | CRCW040264K9FKED Series= CRCW..e3 | Res= 64.9 kOhm Power= 63.0 mW Tolerance= 1.0% | 1 | $0.01 | 0402 3 mm 2 |
| U1 | Texas Instruments | TPS62933FDRLR | Switcher | 1 | $0.48 | DRL0008A-MFG |

![Image](Design%20Report_files/img_005.png)

![Image](Design%20Report_files/img_006.png)

![Image](Design%20Report_files/img_007.png)

![Image](Design%20Report_files/img_008.png)

![Image](Design%20Report_files/img_009.png)

## Operating Values

| # | Name | Value | Category | Description |
| - | - | - | - | - |
| 1. | Cin IRMS | 514.851 mA | Capacitor | Input capacitor RMS ripple current |
| 2. | Cin Pd | 1.448 mW | Capacitor | Input capacitor power dissipation |
| 3. | Cout IRMS | 277.89 mA | Capacitor | Output capacitor RMS ripple current |
| 4. | Cout Pd | 234.53 µW | Capacitor | Output capacitor power dissipation |
| 5. | IC Ipk | 1.481 A | IC | Peak switch current in IC |
| 6. | IC Pd | 260.63 mW | IC | IC power dissipation |
| 7. | IC Tj | 100.703 degC | IC | IC junction temperature |
| 8. | IC Tolerance | 16.0 mV | IC | IC Feedback Tolerance |
| 9. | ICThetaJA Effective | 60.25 degC/W | IC | Effective IC Junction-to-Ambient Thermal Resistance |
| 10. | Iin Avg | 392.64 mA | IC | Average input current |

Copyright © 2026, Texas Instruments Incorporated

![Image](Design%20Report_files/img_010.png)

# Name Value Category Description 11. Ipp percentage 96.264 % Inductor Inductor ripple current percentage (with respect to average inductor current) 12. L Ipp 962.64 mA Inductor Peak-to-peak inductor ripple current 13. L Pd 19.39 mW Inductor Inductor power dissipation 14. Cin Pd 1.448 mW Power Input capacitor power dissipation 15. Cout Pd 234.53 µW Power Output capacitor power dissipation 16. IC Pd 260.63 mW Power IC power dissipation 17. L Pd 19.39 mW Power Inductor power dissipation 18. Total Pd 282.198 mW Power Total Power Dissipation 19. BOM Count 12 System Information Total Design BOM count 20. Cross Freq 36.798 kHz System Information Bode plot crossover frequency 21. Duty Cycle 38.04 % System Information Duty cycle 22. Efficiency 95.508 % System Information Steady state efficiency 23. FootPrint 499.0 mm 2 System Information Total Foot Print Area of BOM components 24. Frequency 500.0 kHz System Information Switching frequency 25. Gain Marg -23.113 dB System Information Bode Plot Gain Margin 26. Inductor ripple current requirement used for Inductor selection 40.0 % System Information Custom Inductor ripple current (% of average inductor current) requirement used for Inductor selection 27. Iout 1.0 A System Information Iout operating point 28. Iout transient step used for Cout calculations 500.0 mA System Information Custom Transient current step requirement that was used for Cout selection (A). 29. Low Freq Gain 100.602 dB System Information Gain at 1Hz 30. Mode FCCM System Information Conduction Mode 31. Overshoot Value 5.844 mV System Information Theoretical Vout Overshoot Value 32. Phase Marg 52.106 deg System Information Bode Plot Phase Margin 33. Pout 6.0 W System Information Total output power 34. Total BOM $1.32 System Information Total BOM Cost 35. Undershoot Value 25.984 mV System Information Theoretical Vout Undershoot Value 36. Vin 16.0 V System Information Vin operating point 37. Vin p-p 283.242 mV System Information Peak-to-peak input voltage 38. Vout 6.0 V System Information Operational Output Voltage 39. Vout Actual 5.992 V System Information Vout Actual calculated based on selected voltage divider resistors 40. Vout Ripple requirement used for Cout calculations 1.0 % System Information Custom maximum output ripple requirement that was used for Cout selection(% of Vout). 41. Vout Tolerance 3.786 % System Information Vout Tolerance based on IC Tolerance (no load) and voltage divider resistors if applicable 42. Vout p-p 8.917 mV System Information Peak-to-peak output ripple voltage 43. Vout transient requirement used for Cout calculations 3.0 % System Information Custom Transient voltage change requirement that was used for Cout selection (% of Vout).

## Design Inputs

| Name | Value | Description |
| - | - | - |
| Iout | 1.0 | Maximum Output Current |
| SoftStart | 5.0 ms | Soft Start Time (ms) |
| VinMax | 16.0 | Maximum input voltage |
| VinMin | 9.0 | Minimum input voltage |
| Vout | 6.0 | Output Voltage |
| base_pn | TPS62933F | Base Product Number |
| source | DC | Input Source Type |
| Ta | 85.0 | Ambient temperature |
| UserFsw | 500.0 k | Customer Selected Frequency |

![Image](Design%20Report_files/img_011.png)

## WEBENCH ® Assembly

## Component Testing

Some published data on components in datasheets such as Capacitor ESR and Inductor DC resistance is based on conservative values that will guarantee that the components always exceed the specification. For design purposes it is usually better to work with typical values. Since this data is not always available it is a good practice to measure the Capacitance and ESR values of Cin and Cout, and the inductance and DC resistance of L1 before assembly of the board. Any large discrepancies in values should be electrically simulated in WEBENCH to check for instabilities and thermally simulated in WebTHERM to make sure critical temperatures are not exceeded.

## Soldering Component to Board

If board assembly is done in house it is best to tack down one terminal of a component on the board then solder the other terminal. For surface mount parts with large tabs, such as the DPAK, the tab on the back of the package should be pre-tinned with solder, then tacked into place by one of the pins. To solder the tab town to the board place the iron down on the board while resting against the tab, heating both surfaces simultaneously. Apply light pressure to the top of the plastic case until the solder flows around the part and the part is flush with the PCB. If the solder is not flowing around the board you may need a higher wattage iron (generally 25W to 30W is enough).

## Initial Startup of Circuit

It is best to initially power up the board by setting the input supply voltage to the lowest operating input voltage 9.0V and set the input supply's current limit to zero. With the input supply off connect up the input supply to Vin and GND. Connect a digital volt meter and a load if needed to set the minimum Iout of the design from Vout and GND. Turn on the input supply and slowly turn up the current limit on the input supply. If the voltage starts to rise on the input supply continue increasing the input supply current limit while watching the output voltage. If the current increases on the input supply, but the voltage remains near zero, then there may be a short or a component misplaced on the board. Power down the board and visually inspect for solder bridges and recheck the diode and capacitor polarities. Once the power supply circuit is operational then more extensive testing may include full load testing, transient load and line tests to compare with simulation results.

## Load Testing

The setup is the same as the initial startup, except that an additional digital voltmeter is connected between Vin and GND, a load is connected between Vout and GND and a current meter is connected in series between Vout and the load. The load must be able to handle at least rated output power + 50% ( 7.5 watts for this design). Ideally the load is supplied in the form of a variable load test unit. It can also be done in the form of suitably large power resistors. When using an oscilloscope to measure waveforms on the prototype board, the ground leads of the oscilloscope probes should be as short as possible and the area of the loop formed by the ground lead should be kept to a minimum. This will help reduce ground lead inductance and eliminate EMI noise that is not actually present in the circuit.

![Image](Design%20Report_files/img_012.png)

## Design Assistance

1. Master key : 449BC8006F0FF2369FE1DD851832FF32[v1]
2. [TPS62933F Product Folder : http://www.ti.com/product/TPS62933F : contains the data sheet and other resources.](http://www.ti.com/product/TPS62933F)

![Image](Design%20Report_files/img_013.png)

Important Notice and Disclaimer

TI provides technical and reliability data (including datasheets), design resources (including reference designs), application or other design advice, web tools, safety information, and other resources AS IS and with all faults, and disclaims all warranties. These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

Providing these resources does not expand or otherwise alter TI's applicable Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with TI products.
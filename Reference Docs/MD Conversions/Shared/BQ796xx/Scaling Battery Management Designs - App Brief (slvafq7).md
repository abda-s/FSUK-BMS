<!-- Converted from Scaling Battery Management Designs - App Brief (slvafq7).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

[www.ti.com](https://www.ti.com/)

## Application Brief

## Scaling accurate battery management designs across energy storage systems

## Introduction

In energy storage system (ESS) applications, it is challenging to efficiently manage the number of batteries required to scale energy storage demand. For example, in utility-scale (1- to 2-kV) systems, there can be over 300 lithium-ion cells in series that each require accurate monitoring to determine the state-of-charge estimations, as well as protections to identify the need for maintenance or detect fault conditions.

## Daisy-chaining with TI's BQ79616 to streamline battery pack communications

In larger battery packs requiring multiple battery monitors, the challenge is streamlining cell voltage communications back to the host processor. Alternative to a complex system requiring a dedicated host for each 16S module or an external transceiver, the BQ79616 offers an integrated daisy protocol which enables a more efficient means of maintaining communications integrity.

Figure 1 shows a vertical interface configuration where two BQ79616 battery monitor pins drive twisted-pair cabling in north and south directions. At the bottom of the chain is the controller module, where the BQ79600-Q1 bridge integrated circuit is used for high-voltage isolation, and translates the cell data from the vertical interface to Universal Asynchronous Receiver Transmitter (UART) or Serial Peripheral Interface (SPI) and to the host processor. Galvanic or capacitively coupled isolation of each device in the chain is possible. Optionally, a ring configuration can serve as a redundant communications path in the event of a fault or break in the chain.

Figure 1. Typical daisy-chain configuration using the BQ79616

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_001.png)

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_002.png)

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_003.png)

Using the vertical interface to daisy-chain battery communications offers flexibility in the design of both the cell and controller modules to various battery architectures. Daisy chaining allows for isolation of the pack For example, the user can connect the twisted-pair cabling across cell-monitoring printed circuit boards (PCBs) spaced ³3 m apart or run short traces between BQ79616 monitors on the same PCB. Both options require only minimal isolation components to separate module ground planes and withstand electromagnetic interference.

In Figure 1, the controller module uses the BQ79600-Q1 as the bridge communications device and the BQ79731-Q1 pack monitor. The BQ79616 delivers reliable battery monitoring with an integrated communications protocol to scale isolated cell modules efficiently, with a differential protocol or vertical interface proven to withstand harsh automotive or ESS environments. With 16 monitoring channels per device and up to 64 that can be daisy-chained, there is flexibility to design across 48-V to &gt;1.5-kV ESS systems.

The BQ79731-Q1 can monitor pack-level current, high-voltage contactors and insulation resistance to feed back into state-of-charge estimations. Similar to the BQ79731-Q1 for pack monitoring, a stand-alone device the BQ79616 can translate cell data directly to the host processor through UART, a feature that allows the use of the same software and hardware design across a varying number of cells in energy storage platforms. In larger &gt;1-kV grid scale systems, the BQ79616 is optimized for system communications with minimal overhead.

## Stacking with BQ76952 for systems requiring multiple battery monitors

The BQ76952 is a 16-cells-in-series battery monitor that comes without integrated daisy-chain communications. Some of the advantages include an integrated Coulomb counter, high-side field-effect transistor (FET) driver, and programmable low-dropout regulators.

To best meet the challenge of stacking BQ76952 monitors, the addition of external isolators and Controller Area Network (CAN) transceivers can enable reliable communications. Figure 2 shows the basics of enabling use of the BQ76952 in ESS applications.

Figure 2. Stacking Configuration with an Isolated BQ76952 to CAN

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_004.png)

To bolster communication integrity within stacked BQ76952 devices, the TCAN1042 CAN transceiver can chain cell-module data back to the host. Additionally, there are considerations to take full advantage of the integrated FET driver, protections and host processor communications www.ti.com Figure 3 is a block diagram stacking two BQ76952 battery monitors. This configuration uses external circuitry to control low-side protection N-channel FETs. The I 2 C buses from each device route to a host microcontroller, with the upper device using a 2.5-kV I 2 C isolator. Compared to a design that features only one battery monitor, this example requires a few extra components to wake both monitors from shutdown mode. Proper load-detection functionality when the protection FETs are disabled requires additional components.

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_005.png)

Figure 3. Stacking Configuration with BQ76952 Battery Monitors

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_006.png)

Depending on the stacking configuration, carefully connect both the communication and protection signals. The BQ76952 provides logic-level outputs that match the controls used for the high-side FET drivers. These outputs are driven based on the local LDO of each monitor, which features a programmable voltage as high as 5 V. Combining these signals from stacked devices helps control low-side N-channel FETs, as shown in Figure 4.

Figure 4. Combined Protection Design for BQ76952 Battery Monitors

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_007.png)

The BQ76952 includes a shutdown mode for lower current consumption. To wake from shutdown mode and return to normal operation, use one of two methods:

- Apply a voltage to the LD pin. (A voltage on the LD pin normally occurs when a charger is connected).
- Pull the TS2 pin, which provides a weak 5-V level with a 5-MΩ source impedance while in shutdown to VSS.

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_003.png)

Make sure that all monitors in the stack include a wake-up method so that the entire system functions correctly. Applying a voltage to the LD pin on the device by attaching a charger induces wake-up, but it is important to add appropriate circuitry to limit the voltage at each pin to the specifications in the data sheet.

The BQ76952 supports up to 400-kHz I 2 C, SPI, and high-speed data input and output communications. Each device is configurable with a separate I 2 C address. Using TI's ISO1640 isolator facilitates communication to the upper devices, as in the Industrial Battery Management Module for 20S Applications Reference Design. Another option is level-shifting using discrete circuitry. Figure 5 shows an example using discrete circuitry with SPI communications.

Figure 5. Serial Communication in a Stacked Design with BQ76952 Battery Monitors

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_008.png)

## Load detection considerations when stacking with BQ76952

The BQ76952 includes load-detection functionality to determine whether the load has been removed from a pack while the FETs are disabled. It is important to make sure this signal is communicating across all devices in the stack; otherwise, the presence of a load determines the operating state of the battery monitors, and all monitors in the stack must be in the same mode at any given time. Use this detection functionality for recovery if a short-circuit or overcurrent event results in disabled FETs.

Load-detection functionality is specifically designed for use with high-side FETs, but can be adapted for use in a system with low-side FETs. With the FETs off, the bq76952 periodically sources a 100-µA current out of the LD pin and measure the voltage of the pin. The device detects whether the load has been removed based on if the measured voltage is above versus below a 4-V threshold. Figure 6 shows a load-detection circuit example using a stacked configuration with low-side FETs.

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_009.png)

[www.ti.com](https://www.ti.com/)

Figure 6. Load Detection in a Stacked Configuration with BQ76952 Battery Monitors

![Image](Scaling%20Battery%20Management%20Designs%20-%20App%20Brief%20%28slvafq7%29_files/img_010.png)

## Cell balancing considerations

When chaining together multiple battery monitors, the cells connected to the bottom device can become imbalanced with the cells connected to the top device. To avoid imbalances caused by unequal power dissipation within the stack, configuring each device in the stack to enable the same set of modules or components internally keeps power dissipation balanced.

Consider balancing the external circuitry powered from the LDOs of the stacked devices. TI's BQ79616 and BQ76952 monitors support random-cell-attach hot plugging, but it is important to review the specific guidelines for each device to assess the design for various stacking configurations.

## Conclusion

The emergence of battery technology in ESS applications presents new challenges. As the storage capacity scales higher to drive transition to renewable sources, stacking multiple battery monitors is required to make sure full coverage of the pack. TI's scalable battery-management designs support varying requirements across utility-scale, commercial battery backup unit and residential energy systems. To optimize efficiency and system costs, ESS designers must analyze these configurations to best fit system requirements.

## Additional Resources

- Texas Instruments, BQ79616 16-Series Battery Monitor, Balancer, and Integrated Hardware Protector, data sheet.
- Texas Instruments, Improving Voltage Measurement Accuracy in Battery Monitoring Systems, technical article.
- Texas Instruments,Improving Temperature Measurement Accuracy in Battery Monitoring Systems, technical article.
- [Texas Instruments, Easy Configuration of BQ76942, BQ76952 Battery Monitors, application report.](https://www.ti.com/lit/pdf/slua991)
- [Texas Instruments, BQ76952 and BQ76942 battery monitors, video.](https://training.ti.com/bq76952-and-bq76942-battery-monitors)

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2024, Texas Instruments Incorporated
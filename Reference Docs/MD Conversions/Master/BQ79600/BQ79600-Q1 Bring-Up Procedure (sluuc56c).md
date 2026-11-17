<!-- Converted from BQ79600-Q1 Bring-Up Procedure (sluuc56c).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

www.ti.com Table of Contents

## User's Guide

## BQ79600-Q1 Bring-Up Procedure

## ABSTRACT

The BQ79600-Q1 device serves as a bridge device between a host controller and BQ7961x-Q1 battery monitoring devices. With the inclusion of universal asynchronous redriver/transmitter (UART) and serial peripheral interface (SPI) to communicate to the host, and daisy chain communication ports to talk to BQ7961xQ1 devices, the BQ79600-Q1 can translate data from the host to the battery monitoring devices and vice versa. This user's guide details the necessary steps to wake up and initialize a stack of BQ7961x-Q1 devices using BQ79600-Q1 as a bridge device between the host and the battery monitors.

## Table of Contents

| 1 Example Wakeup and Initialization Procedure.................................................................................................................... 2 |
| - |
| 1.1 Device Setup......................................................................................................................................................................2 |
| 1.2 Wakeup Overview.............................................................................................................................................................. 3 |
| 1.3 Auto-Addressing Overview.................................................................................................................................................3 |
| 2 References.............................................................................................................................................................................. 5 |
| 3 Revision History......................................................................................................................................................................5 |
| List of Figures |
| Figure 1-1. Basic System Diagram..............................................................................................................................................2 |
| Figure 1-2. Wakeup Flowchart.....................................................................................................................................................3 Figure 1-3. Auto-Addressing Flowchart....................................................................................................................................... 4 |

## Trademarks

All trademarks are the property of their respective owners.

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_001.png)

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_002.png)

## 1 Example Wakeup and Initialization Procedure

In this section, a generic Wakeup and Initialization procedure is described and can be used as a general reference. As an example, it is assumed that a BQ79600-Q1 is used as a communications bridge, and six BQ79616-Q1 are used to monitor a stack of 96 cells in series. It is assumed that a baud rate of 1 MBaud is used for UART communication to the host, or when using SPI the host provides a clock between 2-6 Mhz. For an example diagram, see Figure 1-1.

Figure 1-1. Basic System Diagram

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_003.png)

There are three required major steps for bringing up a stack of BQ79600-Q1 and BQ79616-Q1 devices:

- Device Setup
- Wakeup
- Auto-Addressing

## 1.1 Device Setup

In order to set up the BQ79600-Q1 device for communication to the host, it is important to set SPI\_RDY and nCS pins in the correct state when using SPI or UART before the device is powered. If UART mode is used, connect SPI\_RDY and nCS to GND. If using SPI mode, connect SPI\_RDY and nCS to VIO through a 10-100 kΩ pull-up resistor.

To connect the BQ79600-Q1 device to the BQ79616-Q1 device, connect the twisted pair cable as show in Figure 1-1.

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_004.png)

[www.ti.com](https://www.ti.com/)

## 1.2 Wakeup Overview

After configuring all required peripherals on the host microcontroller unit (MCU), begin by pulling nCS low so pings can be sent. Furthermore, MOSI or TX signal from the MCU is used to send wake pings to the MOSI/RX pin of the base BQ79600-Q1. Additionally, send commands that instruct the BQ79600-Q1 to propagate a wake tone to the rest of the stacked BQ79616-Q1 devices.

1. Send two consecutive WAKE pings. The procedure for a single WAKE ping is described as:
- a. When using SPI, hold nCS low and after 2μs send a WAKE ping on MOSI/RX by pulling the line low for 2.75ms (tHLD\_WAKE) to wake the BQ79600-Q1. Following this, wait 2 us and then bring nCS back high.
- b. When using UART, send a WAKE ping on MOSI/RX by pulling the line low for 2.75 ms (tHLD\_WAKE) to wake the BQ79600-Q1.
2. Wait at least 3.5 ms (tSU(WAKE\_SHUT)) to allow BQ79600-Q1 device to enter ACTIVE mode.
3. Send a single device write to BQ79600-Q1 to set CONTROL1[SEND\_WAKE]=1, which wakes up all stacked BQ79616-Q1 devices.
4. After host completes sending the command, wait appropriate time to allow all devices to receive the WAKE tone and enter ACTIVE mode before starting Auto-Address sequence:
- The duration of a WAKE tone is about 1.6 ms.
- The time it takes for a BQ79616-Q1 device to enter ACTIVE mode from shutdown is about 10 ms.

To calculate the total time to wait, add the WAKE tone duration plus the time to enter ACTIVE mode (total of 11.6 ms) and multiply the result by the number of stacked BQ79616-Q1 devices.

## Note

If device is shut down through SHUTDOWN ping, the COMH RX and COML RX are disabled at next wake up. In such case, on step 1, host needs to first send a WAKE ping, wait tSU(WAKE\_SHUT) and then send a second WAKE ping. COMH RX and COML RX will be enabled after the second WAKE ping. Then proceed with steps 2 to 4.

Figure 1-2. Wakeup Flowchart

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_005.png)

## 1.3 Auto-Addressing Overview

Properly addressing the BQ79600-Q1 and each BQ79616-Q1 device in a stack is critical for proper operation of the devices. In addition to the summary of the following main points, all devices must be addressed sequentially up the stack, with a best practice of starting from address 0x00 for the bridge device.

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_006.png)

- Follow the WAKEUP procedure to make sure that all devices are awake and available for auto-addressing.
- Dummy stack write 0x00 to registers OTP\_ECC\_DATAIN1 to OTP\_ECC\_DATAIN8 (register address 0x343 to 0x34A) on the BQ79616-Q1. This is a total of 8 stack writes (one for each register) to synchronize the DLLs
- used for reclocking the daisy chain interface.
- Broadcast write 0x01 to register address 0x309 CONTROL1 to enable auto addressing.
- Broadcast write consecutively to register address 0x306 DIR0\_ADDR the values 0x00, 0x01, 0x02, and so forth to set the north communication device addresses.
- Broadcast write 0x02 to register address 0x308 to set BQ79616-Q1 as stack devices.
- Single device write 0x03 to register address 0x308 of top device (device 6 in this example) to set it as the top of the stack. Please note that this step is critical for broadcast reads to work properly!
- Stack read registers OTP\_ECC\_DATAIN1 to OTP\_ECC\_DATAIN8 (register address 0x343 to 0x34A). This is a total of 8 stack reads (one for each register) intended to sync up internal DLL.
- Stack read register address 0x306 to verify that all stack devices have been addressed correctly.
- Single device read from the base BQ79600-Q1 device the register address 0x2001 and verify that the value is 0x14.
- Proceed to register initialization.

Figure 1-3. Auto-Addressing Flowchart

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_007.png)

![Image](BQ79600-Q1%20Bring-Up%20Procedure%20%28sluuc56c%29_files/img_008.png)

[www.ti.com](https://www.ti.com/)

## 2 References

1. [Texas Instruments, BQ79600-Q1 Automotive SPI/UART Communication Interface Functional-Safety Compliant With Automatic Host Wakeup Data Sheet](https://www.ti.com/lit/pdf/slusds1)
2. [Texas Instruments, BQ79616-Q1, BQ79616H-Q1, BQ79614-Q1, BQ79612-Q1 Functional Safety-Compliant Automotive 16S/14S/12S Battery Monitor, Balancer and Integrated Hardware Protector (SLUSE81)](https://www.ti.com/lit/pdf/SLUSE81)

## 3 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

| Changes from Revision B (October 2023) to Revision C (January 2026) | Page |
| - | - |
| · Updated Step 1 in the Wakeup Overview section for double WAKE ping procedure.........................................3 |  |
| · Updated Wakeup Flowchart diagram................................................................................................................. | 3 |

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATASHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you fully indemnify TI and its representatives against any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale, TI's General Quality Guidelines, or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products. Unless TI explicitly designates a product as custom or customer-specified, TI products are standard, catalog, general purpose devices.

TI objects to and rejects any additional or different terms you may propose.

IMPORTANT NOTICE

Copyright © 2026, Texas Instruments Incorporated Last updated 10/2025
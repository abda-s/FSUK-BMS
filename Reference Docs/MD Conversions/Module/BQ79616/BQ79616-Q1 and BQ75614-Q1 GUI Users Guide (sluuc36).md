<!-- Converted from BQ79616-Q1 and BQ75614-Q1 GUI Users Guide (sluuc36).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

www.ti.com Table of Contents

## User's Guide

## BQ79616-Q1 and BQ75614-Q1 GUI User's Guide

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_001.png)

## ABSTRACT

This document provides a guide to install, set up, and use the BQ79616-Q1 graphical user interface (GUI). In this document, the basic functionalities of the GUI are documented with the intent of reducing the time needed to become familiar with the GUI.

Table of Contents

| 1 Getting Started........................................................................................................................................................................3 |  |
| - | - |
| 2 GUI Home Page.....................................................................................................................................................................12 |  |
| 3 Cell Monitor...........................................................................................................................................................................13 |  |
| 4 Cell Balancing.......................................................................................................................................................................18 |  |
| 5 Protector................................................................................................................................................................................20 |  |
| 6 Communication Control.......................................................................................................................................................21 |  |
| 7 Diagnostics............................................................................................................................................................................22 |  |
| 8 Command Sequence............................................................................................................................................................ | 23 |
| 9 Faults..................................................................................................................................................................................... | 24 |
| 10 Register Map....................................................................................................................................................................... | 25 |
| 11 Debug...................................................................................................................................................................................27 |  |
| 12 Current Sensing..................................................................................................................................................................28 |  |
| 13 Troubleshooting..................................................................................................................................................................28 |  |
| List of Figures | List of Figures |
| Figure 1-1. Paste .txt Firmware File into the Firmware Folder.....................................................................................................4 |  |
| Figure 1-2. Successful Hardware Connection Message..............................................................................................................4 |  |
| Figure 1-3. BQ79616 EVM Connections..................................................................................................................................... | 5 |
| Figure 1-4. BQ79600 GUI Communication Control Page............................................................................................................6 |  |
| Figure 1-5. Bridge Control Tab.....................................................................................................................................................8 |  |
| Figure 1-6. Bridge Control Debug Tab.........................................................................................................................................8 |  |
| Figure 1-7. J10 USB2ANY Connection........................................................................................................................................9 |  |
| Figure 1-8. Example Configuration............................................................................................................................................10 |  |
| Figure 1-9. 5V Connection......................................................................................................................................................... | 11 |
| Figure 2-1. GUI Home Page......................................................................................................................................................12 |  |
| Figure 3-1. BQ79616 GUI Cell Monitor Page............................................................................................................................ | 13 |
| Figure 3-2. Opening Communication Between the EVM and the GUI.......................................................................................13 |  |
| Figure 3-3. Device Fault Display in Cell Monitoring Page......................................................................................................... | 14 |
| Figure 3-4. GPIO/Temperature Tab........................................................................................................................................... | 15 |
| Figure 3-5. GPIO Config Pop Up Window................................................................................................................................. | 16 |
| Figure 3-6. BQ79616 GUI Detailed Device View.......................................................................................................................17 |  |
| Figure 4-1. BQ79616 GUI Cell Balancing Page........................................................................................................................ | 18 |
| Figure 5-1. BQ79616 GUI Protector Page.................................................................................................................................20 |  |
| Figure 6-1. BQ79616 GUI Communication Control Page..........................................................................................................21 |  |
| Figure 7-1. Diagnostics Tab.......................................................................................................................................................22 |  |
| Figure 8-1. Command Sequence Tab........................................................................................................................................23 |  |
| Figure 9-1. Faults Tab................................................................................................................................................................24 |  |
| Figure 10-1. BQ79616 GUI Register Map Page........................................................................................................................25 |  |
| Figure 10-2. BQ79616 GUI Register Map Field View................................................................................................................26 |  |
| Figure 11-1. BQ79616 GUI Debug Page................................................................................................................................... | 27 |

Taylor Vogt

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_002.png)

## List of Tables

| Table 11-1. Initialization Bytes....................................................................................................................................................27 |
| - |

## Trademarks

All trademarks are the property of their respective owners.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

## 1 Getting Started

## 1.1 Installing the GUI

In the following sections, we will step through the instructions to properly install each item in order. Start by downloading the below files 1) for GUI executable and 2) for the required USB2ANY firmware.

·

- Download Software GUI via link: https://www.ti.com/product/BQ79616-Q1#design-development##softwaredevelopment

USB2ANY Explorer installer folder (this can be downloaded from http://www.ti.com/tool/USB2ANY and downloading USB2ANY Explorer Software under Key Document)

- USB2ANY SDK installer (2\_USB2ANY\_2.8.2.0\_SDK\_Setup.exe)

## 1.1.1 Uninstalling and Updating the BQ79616 GUI

*Very Important* The current latest version of the GUI is bqAutoEval 1.0.4. If you have used a previous older version then you must uninstall the previous version before you update to this newer version. The steps are below:

1. Close out of all instances of the BQ79616 GUI. Ensure that there are no remaining Node.js processes running in the background by ending them from the task manager.
2. The uninstaller can be found in C:\Program Files (x86)\Texas Instruments\BQ79616. Run the uninstaller.
3. The uninstaller may ask you if you want to uninstall GUI Composer Runtime if there are no additional dependencies on GUI Composer Runtime on the user's computer. Do NOT uninstall GUI Composer Runtime or you will have to repeat step 1.1.2 below.
4. Extract the components of the new installer and run them from any location in the user's PC.

## 1.1.2 Installing GUI Composer Runtime

1. If you already have the GUI Composer Runtime Installer downloaded from previously using an older GUI version and did not uninstall it, then you may skip step 2.
2. When you run the GUI executable software link from the bq79616 product folder, you will be prompted to download the GUI Composer Runtime. Ensure to follow instructions and accept downloading the GUI Composer Runtime 7.4.0.

## 1.1.3 Updating USB2ANY Firmware

This step is crucial to having the GUI work correctly without any errors, and may be the first issue if you run into any problems when first connecting to the EVM. If you do not do this correctly, the GUI will notify you that either your USB2ANY Hardware is not connected properly or that you have an outdated firmware version. If the GUI recognizes this, it will prompt you with the latest firmware and further instructions to update the USB2ANY.

1. To properly use the latest bqAutoEval GUI v1.0.4, you are required to update to firmware version 3\_1\_1\_14. This file is named USB2ANY\_3\_1\_1\_14 - BQAutoEval.txt. Skip to step 5 if USB2ANY is brand new. Upon opening the GUI, it will prompt to update automatically.
2. Download and extract the contents of the USB2ANY Explorer installer folder (this can also downloaded from http://www.ti.com/tool/USB2ANY and downloading USB2ANY Explorer Software under Key Document) and run the executable from within it. Keep all default installation folder locations.
3. To update the USB2ANY firmware,ensure you have downloaded the USB2ANY SDK and ran the executable (2\_USB2ANY\_2.8.2.0\_SDK\_Setup.exe). If the default location from the installation wizard was not changed, the folder can be found in C:\Program Files (x86)\TI USB2ANY SDK.
4. Ensure the USB2ANY firmware file "USB2ANY\_3\_1\_1\_14 - BQAutoEval.txt" is saved somewhere to the hard drive. Copy the "USB2ANY\_3\_1\_1\_14 - BQAutoEval.txt" file and paste it into the Firmware folder as in the below image.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_004.png)

Figure 1-1. Paste .txt Firmware File into the Firmware Folder

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_005.png)

5. Connect the USB2ANY to the computer. Press the Windows icon, search for USB2ANY Firmware Loader, and launch it. If the firmware loader does not show up in the search, reinstall the USB2ANY Explorer. Click Yes on the dialog box that mentions that the firmware loader is legacy software. If the firmware loader requests to update the firmware to version 2.8.2.0, press cancel. If the USB2ANY has never had its firmware updated before, additional steps a, b, and c below need to be followed to update the firmware. Otherwise, skip the below steps a, b, and c and go to step 6.
- a. The USB2ANY firmware loader will prompt you to locate the BSL button in order to update the firmware. Follow the steps given in the Firmware Loader as below. Do not close the USB2ANY Firmware Loader at any point during this process.
- b. Check that the USB2ANY is disconnected from the computer. Locate the BSL button, which is underneath a small hole in the USB2ANY housing next to the mini USB port.
- c. While keeping the button depressed (a small paper clip works well), connect the USB2ANY to the computer. If it is done correctly, the USB2ANY firmware loader will no longer prompt you to locate the BSL button and instead allow you to click Update Firmware and then follow the next steps to program the latest firmware as below.
6. In the firmware loader, ensure that "USB2ANY\_3\_1\_1\_14 - BQAutoEval.txt" appears in the field labeled Update to firmware version:. Press Update Firmware. The below image shows an earlier outdated firmware version so please ensure the above text file is correct.

## 1.1.4 Installing the GUI

1. Download and navigate to the BQ79616 installer folder (3\_BQAutoEvalPG2.0\_1.0\_installer\_win.zip). Extract the contents and run the setup executable from within the extracted folder. Keep all default installation folder locations and press yes to all prompted dialogue.
2. To launch the GUI, navigate to C:\Program Files (x86)\Texas Instruments\BQ79616 and run the BQ79616 application.
3. The device should automatically connect upon launching the GUI, and the connection status should be reflected at the bottom of the window. If the device does not connect, unplug the USB2ANY from the computer, reload the GUI, and plug the USB2ANY back into the computer. Otherwise, you may have incorrectly updated the firmware and may need to return to section 1.1.3.

Figure 1-2. Successful Hardware Connection Message

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_006.png)

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_007.png)

[www.ti.com](https://www.ti.com/)

## 1.1.5 Starting Up the EVM

This section outlines connections specifically for the BQ79616EVM. For information of powering and connecting other EVMs to the host PC, please refer to BQ79600EVM Connections or BQ79631EVM Connections.

Figure 1-3. BQ79616 EVM Connections

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_008.png)

1. Apply a minimum 18 V DC power supply across VSTACK and GND.
2. Connect the appropriate jumpers. Refer to the BQ79616 EVM user's guide.
3. Connect the 10-pin ribbon cable to the USB2ANY and to the EVM (key side up)

## 1.2 BQ79600-Q1 Device Key Differences

When using the BQ79600EVM with the BQAutoEval GUI, there are a few key differences that exist specifically for this device that may not apply directly to the information presented in the rest of the document. These details will be discussed below.

## 1.2.1 Connections

To properly supply power and connect the BQ79600EVM to the host PC and other EVMs, please perform the following steps:

1. Apply either 12 V or 5 V to TP8 or TP9 while making sure that J3 and J1 are configured for the correct supply voltage.
2. Connect the appropriate jumpers. Refer to the BQ79600 EVM user's guide, and pay special attention to what communications mode is needed for the device (SPI or UART).
3. Connect the 10-pin ribbon cable to the USB2ANY and to the EVM (key side up).

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_002.png)

4. Use the J14 COMML and J15 COMMH connectors to connect the BQ79600EVM bridge device to any devices being used in the stack.

## Note

The BQ79600EVM should always be configured as the bridge device if it is being used in the system.

## 1.2.2 Cell Monitor Tab

While the Cell monitor tab is used by other devices such as the BQ79616-Q1, BQ79614-Q1, and BQ79631-Q1 to monitor parameters such as VC, GPIO, and current sense data, this information is not pertinent to the function of the BQ79600-Q1 device. Therefore, this device will not appear in the cell monitor tab of the BQAutoEval GUI. This does NOT mean that the device is not connected.

## 1.2.3 Communication Control

Figure 1-4. BQ79600 GUI Communication Control Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_009.png)

This page is used for controlling the power mode and communications of the base 600 device and any stack devices that are connected. Furthermore, the user can monitor faults seen at the top right, as well as change the communications direction.

## Communication Configuration

Under this tab, the user can configure the following settings:

- TX Holdoff: Integer between 0-255; specifies the number of bit periods the UART transmitter waits after the last bit reception before starting transmission.
- Communication Timeout Thresholds

Short Comm Timeout: Timer resets every time a valid response or command frame is received; sets CTS system fault when timer expires.

Long Comm Timeout: Allows the host to put the device in SLEEP or SHUTDOWN modes for power saving; timer resets every time a valid response or command frame is received; executes Long Timeout Action when the timer expires.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_010.png)

## [www.ti.com](https://www.ti.com/)

- Long Timeout Action: On a long timeout, either send the device to SLEEP and set a CTL system fault or send the device to SHUTDOWN.

## Power Mode Control

Under this tab, the user can configure the following settings:

- Current Device (xxx): This allows the user to control the power state of the currently selected device through the device selected drop-down menu. Users can send a selected device to shutdown, sleep, or soft reset.
- Tones to Next Device: This allows the user to control tones that are sent to the next device up the stack. When in use, users must make sure to change the device selected in the drop-down if they are trying to send tones to different devices.
- Ping to Bridge Device: This allows the user to control the power state of the current bridge device by sending pings to it.

## Debug

Under this tab, the user can configure the following settings:

- VIF/UART Baud: This allows the user to control the baud rate of the VIf/UART. Additonally, users can see fault indicators on the COM lines of the base 600 device.
- Debug Control and Comms Status: Users can enable and disable the ability to modify the functionality of the COM ports. With the debug control enabled, users can turn on and off the COMH and COML ports.

## 1.2.4 Bridge Control

In this tab, users can control the bridge device and monitor, mask, and reset faults, as well as debug communications issues on the SPI, UART, and daisy chain interface. At the top of the screen is the communications mode that is being used for this device. Users must make sure and set this to the correct setting for their use.

- Control: Here users can enable or disable:
- The sniff detector
- nFault
- Receiver tones
- Heartbeat
- Comm fault detection
- INH
- UART stop bits

These all enable and disable features on the 600 device.

- Fault Control: In this part of the page, users can reset, mask, and unmask faults for the 600 bridge device.
- Fault Status: This contains all of the fault registers, along with the respective bits within them, so that the user can see which specific faults of each fault register are being set. If a certain element is red, it means that this bit is active and has been set by the device.
- Diagnostics: Here, users can cause CRC faults on the device in order to test fault detection on 616 devices further up the stack, as well as on the 600 device itself. Additionally, users can perform power diagnostics and trigger the INH PMOS pullup.
- SPI Interface: This section can be used to set the SPI clk speed that the USB2ANY propagates to the 600 device.
- Debug: Expanding the debug tab offers an even more detailed breakdown of the faults, allowing the user to trace back top level faults to specific errors in the communications, power, and so forth.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_011.png)

Figure 1-5. Bridge Control Tab

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_012.png)

Figure 1-6. Bridge Control Debug Tab

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_013.png)

## 1.3 BQ79631-Q1 Device Key Differences

When using the BQ79631EVM with the BQAutoEval GUI, there are a few key differences that exist specifically for this device. These specific details will be discussed below.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_014.png)

## 1.3.1 Connections

## USB2ANY Connection

To connect the BQ79631EVM directly to the PC via UART connection, connect the USB2ANY cable to the 10pin J10 connector on the BQ79631EVM as seen in the figure below.

Figure 1-7. J10 USB2ANY Connection

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_015.png)

## Daisy Chain Communications

If the user wishes to use the BQ79631EVM as part of a stack of other EVMs, connections will be made to the COMMH and COMML connections through the J27 and J26 connectors. If the BQ79631EVM is configured as the bridge device, the USB2ANY connection will provide communication between the EVM and the host PC while the J27 connector will connect the BQ79631EVM to any other EVMS in the stack.

If another device such as the BQ79600EVM is being used as the bridge device, the J26 connection on the BQ79631EVM should be connected to the bridge device and the J27 connection should be connected to the next device in the stack if other devices are being used.

This example has the BQ79631EVM configured as the bridge device and the BQ79616EVMs configured as stack devices.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_011.png)

Figure 1-8. Example Configuration

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_016.png)

## BQ79631EVM Power Connections

Power to enable the use of the BQ79631EVM is supplied through the 5V\_LV connector on the left side of the board. Simply connect the positive and negative terminals of a power supply set to 5V to the pins 5V\_LV and GNDLV respectively.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_007.png)

For more information on specific connections needed to make measurements through the BQ79631EVM, please refer to the BQ79631EVM Users Guide.

Figure 1-9. 5V Connection

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_017.png)

## 1.3.2 Cell Monitor Tab

While the other BQ devices use the cell monitor tab of the BQAutoEval GUI to monitor cell voltages directly, the bq79631-Q1 uses the VC channels to measure the certain pack voltage deltas according to the connections highlighted in the bq79631EVM User Guide. These pins are all configured in the same manner as discussed in Measurement Display.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_002.png)

## 2 GUI Home Page

Figure 2-1. GUI Home Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_018.png)

Before the user can see the above home page, there is a menu to select bridge device. Ensure the user selects whichever device is connected directly to the host PC via UART connection as the bridge device and any other devices that are connected through daisy chain as stack devices. This selection also applies if the user is attempting to use the GUI with the BQ75614-Q1, BQ79614-Q1, and BQ79612-Q1 devices. If the user is attempting to use the BQ79600-Q1 device, it is recommended to select the BQ79600-Q1 as the bridge device and all other EVMs as stack devices.

After selecting the bridge device, the GUI home page appears and offers a 3D view of the EVM in the middle. On the left is space for a video that will go over basic information to get started with the EVM and GUI, and this video is currently in development. Access buttons to different pieces of technical documentation are at the bottom of the home page and will be available after the device has been fully released online.

The pages of the GUI can be accessed either using the quick access buttons on the right or the sidebar, both highlighted in red in the figure above. It is generally best to start with the cell monitor page to properly 1) Wakeup 2) Auto address and 3) Start Polling the device.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_019.png)

[www.ti.com](https://www.ti.com/)

## 3 Cell Monitor

Access this page from the home page by pressing the Cell Monitor icon or by selecting the icon on the sidebar. This page should normally be the first one that the user accesses in order to properly 1) Wakeup and 2) Auto Address 3) Start Polling to start to read back data. If the user does not properly Wakeup and Auto address in that sequence, then the device will be unresponsive.

From this page, the user can easily monitor VCELL, GPIO, and temperature measurements for all connected devices. The cell monitoring page also offers a visual representation of cell measurements and faults, enabling quick evaluation of cell conditions.

The figure belows shows cell measurements for three connected devices with all 16 cells enabled.

Figure 3-1. BQ79616 GUI Cell Monitor Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_020.png)

## 3.1 Starting up the Device

To get started with the BQ79616 EVM and GUI:

1. From the Cell Monitor page, Wake Up the devices and Run Auto Address.
2. Under View Poll Settings, specify the number of cells for each connected device.

Figure 3-2. Opening Communication Between the EVM and the GUI

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_021.png)

This opens up the communication channel between the GUI and the device and communicates to the device which cells to measure and monitor for fault conditions.

## 3.2 Cell Monitor Settings

At the top of the cell monitoring page, the user can find relevant settings that allow for easy configuration of cell measurements. These settings control all connected devices.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_002.png)

- Communication Direction: Toggles between north and south, indicates direction of auto-addressing and tone propagation. In this release of the GUI, ensure that North is selected.
- Low Pass Filtering: Sets the cutoff frequency of the post-ADC digital filter for both cell and bus bar voltage measurements.
- Sampling Type: Toggles between single and continuous ADC run modes.
- AUX ADC: Enables AUX ADC continuous run mode to enable a valid BAT voltage measurement.

In Single run mode, each press of the Start Polling button updates the cell measurements just once. In Continuous mode, the cell measurements updates automatically at the selected refresh rate once polling has started.

## 3.3 Measurement Display

The measurement display is where voltage and temperature measurements can be found. Under the Cell Voltage tab, all 16 cell measurements can be monitored along with battery module voltage (if the resistor ladder is in use, this is the supply voltage) and bus bar voltage. The user also has the option to display the unconverted hexadecimal values from the corresponding VCELL*\_HI/LO registers or the unfiltered cell measurements. The user can customize which of these items to display at any time using the Manage Columns window to select and deselect each cell. The user can display a cell balancing status indicator. If the Faults column is selected, clicking on the pop-up button next to the status light displays a detailed fault summary for each device.

Figure 3-3. Device Fault Display in Cell Monitoring Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_022.png)

Upon waking the device and running auto addressing, the user can expect to see the following faults:

- FAULT\_SYS[DRST]: Triggered because of power on reset (POR)
- FAULT\_POWER3[AVDDUV\_DRST] &amp; [AVDDREFUV\_DRST]: Triggered because of POR
- If multiple devices are connected, FAULT\_COMM3[FCOMM\_DET]: Device detects faults in devices further up the stack. This fault does not trigger for the device at the top of the stack. (This can be disabled by using the Embedded Fault checkbox at the top of the menu to the right of the display hex values toggle button)

Clear faults by clicking the Clear button at the top of the fault display and start polling to update the fault and status lights. All of the fault lights should be green with the possible exception of the OTP fault, which triggers if polling has been run since the polling sequence sets the number of active cells. To mask this fault on a single device, you can either select the Set button (Mask CUST\_CRC) at the top of the menu or navigate to the Register Map page, search for the register FAULT\_MSK2, and change bits MSK\_OTP\_CRC and MSK\_OTP\_DATA to 1. To mask this fault for multiple connected devices, perform a broadcast write from the Debug page using the following data:

- Initialization byte: 0xD0
- Register Address: 0x11

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_023.png)

## [www.ti.com](https://www.ti.com/)

## · Data Bytes: 0x60

Press write. The all fault lights for the devices should turn green.

Under the GPIO/Temperature tab, the converted measurements of the eight GPIO pin voltages and the two die temperatures are displayed. Like the previous tab, the user can also customize the display using Manage Columns and display the unconverted hex values directly from the corresponding registers. To enable GPIO's for ADC measurements, refer to the below section for details on the GPIO/Temperature tab.

In the GPIO/Temperature tab, there is a CONFIG button on the right hand side shown below. This allows the user to configure all GPIOs for an individual device, this button and pop up window are shown below. Please take note that after you change any GPIO settings, you will need to Stop and then Start Polling in order to properly set your GPIO settings. This is because the device requires the Main ADC to be reset to acknowledge any setting changes.

Figure 3-4. GPIO/Temperature Tab

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_024.png)

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_002.png)

Figure 3-5. GPIO Config Pop Up Window

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_025.png)

## 3.4 Detailed Device View

The user can navigate to a detailed device view by clicking on any of the underlined device addresses. At the top of the page, a grid representation of cell voltages and cell balancing status allows the user evaluate cell status at a glance. The right-hand side of the page houses a collapsible board details pane where the status bits of each board and fault summary are displayed. Clicking on any of the individual cells in the grid displays its OVUV fault status in the bottom right-hand corner.

On the bottom of the page is a time domain cell voltage plot. While polling is running, the plot updates itself with the new data points. The user can select which cell waveforms to display by clicking on the "+" button. There are several buttons in the upper right-hand corner of the plot area to interact with the plot. The user has multiple zoom options, can display numerical data within the plot area, and can save an image of the plot. You can also export this data vs. time to a .csv file by clicking the red export button at the top right of the plotting window. Note that the user must be polling to export any data over time.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_014.png)

[www.ti.com](https://www.ti.com/)

Figure 3-6. BQ79616 GUI Detailed Device View

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_026.png)

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_002.png)

## 4 Cell Balancing

Access the Cell Balancing page from the home page or the sidebar. From this page, the user can quickly configure cell balancing settings. This includes the ability to change balancing modes, set balancing timers, and set balancing stop conditions.

## Note

This page will not be used for devices that do not utilize the cell balancing feature such as the BQ79631EVM and BQ79600EVM.

Figure 4-1. BQ79616 GUI Cell Balancing Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_027.png)

## 4.1 Balancing Timetable

Here, the timers for all of the cells and the module can be set. At the top left, the user can set a timer for All Cells. In addition, the user can save the current timing profile as a .txt file and can load from it at any time. In Manual mode, check boxes appear and are used to evaluate whether or not a cell combination is valid.

To manually turn off a cell for balancing, set the timer to 0 seconds and press Run.

## 4.2 Balancing Sequence

The BQ79616 supports two cell balancing modes: auto and manual. Below are descriptions on how to get started with either mode.

## 4.2.1 Auto Balancing

In auto cell balancing, cells are balanced in an odd and even sequence, switching every duty cycle period. Because the device automatically sets up this balancing sequence, there are no constraints placed on which cells can be selected for balancing in auto balancing mode.

To configure auto balancing, set cell timers and select a Duty Cycle Time.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_028.png)

## 4.2.2 Manual Balancing

In manual cell balancing, all cells selected by the user are balanced at the same time. Because of this, there must be constraints placed on the cell combinations that can be chosen. The BQ79616 has two conditions that must be satisfied by a valid cell selection.

- No more than eight cells can be selected at once.
- If the user would like to Select Adjacent Cells, no more than two consecutive cells can be selected. With the setting disabled, no adjacent cells can be selected.

If any of these conditions are not satisfied, the GUI alerts the user that the cell combination is invalid.

To configure manual balancing, select a valid cell combination and set cell timers.

## 4.3 Thresholds

The next step in configuring cell balancing is setting voltage and temperature thresholds, which BQ79616 can use to stop and pause cell balancing, respectively. The fields under the Thresholds section control the VCBDONE and OTCB thresholds. The user can also control whether or not balancing aborts upon the detection of an unmasked fault by checking Stop Balancing on Fault.

## 4.3.1 VCBDONE Threshold

Here, the VCBDONE threshold can be set, and this stop threshold is monitored for each individual cell. This means that each cell continues balancing until VCBDONE is reached independent of all other cells.

This threshold, when met, stops the balancing of each cell independent of how much time is left on the timer of the cell and also marks balancing as complete.

## 4.3.2 OTCB Threshold

During passive balancing, heat is generated in the internal CBFET and external balancing resistors. Because of this, the BQ79616 features an overtemperature threshold specific to cell balancing, called OTCB. If this temperature threshold is reached during cell balancing at any point, cell balancing immediately pauses for all cells. OTCB is represented as a percentage of TSREF. Balancing resumes when the temperature drops by the amount specified by COOLOFF.

Note that to use this feature, the OT protector must be enabled and set to round robin mode.

## 4.4 Start Balancing

After the user has successfully configured the balancing sequence and thresholds, the user can start balancing by pressing Run. Whenever balancing settings are changed, the user must press Run again to issue the changes to the device.

Balancing can be paused and resumed by pressing Pause Balancing. Note that this does not stop balancing, and the CB RUN indicator will still be green.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_029.png)

## 5 Protector

From this page, the user can set the voltage and temperature protection thresholds for any device in the system. Also present on this page are status and fault lights to monitor the condition of the connected devices.

Figure 5-1. BQ79616 GUI Protector Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_030.png)

## 5.1 Threshold Settings

Under the Voltage Protection section, the user can configure the OV and UV thresholds. Voltages beyond these thresholds trigger faults, and the faults are reflected in the status lights on the right side of the page. Use the drop-down menu to edit the thresholds and press Write OVUV to write to the corresponding registers.

In the Temperature Protection section, the user can set the OT and UT thresholds. To use the temperature protections, first enable TSREF via the Register Map page by setting bit 0 of register CONTROL2 to 1. Like the OTCB threshold, the OTUT thresholds are represented as percentages of TSREF. Once set, press Write OTUT to write the thresholds to the corresponding register and start the protectors in the selected run mode.

In addition, the GPIOs that are connected to external thermistors must be selected in the selection box. This configures the GPIOs for both ADC readings and OTUT protection and tells the device not to ignore the fault detection result.

## 5.2 Protector Run Modes

The user can also change protector modes from this page. The standard protection mode is Round Robin. In round robin mode, all active cells and GPIOs are sequentially evaluated against the corresponding protection thresholds, and faults are triggered if a threshold is crossed.

The BQ79616 also supports a protector mode called Single Channel Run. In this mode, the user can lock the OVUV and OTUT protectors to a single cell and GPIO, respectively. The user can also configure the threshold lock setting.

The last supported protector modes are the OVUV and OTUT built-in self test cycles.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_031.png)

[www.ti.com](https://www.ti.com/)

## 6 Communication Control

Figure 6-1. BQ79616 GUI Communication Control Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_032.png)

## 6.1 Communication Configuration

Under this tab, the user can configure the following settings:

- TX Holdoff: Integer between 0-255, specifies the number of bit periods the UART transmitter waits after the last bit reception before starting transmission.
- Communication Timeout Thresholds
- Short Comm Timeout: Timer resets every time a valid response or command frame is received, sets CTS system fault when timer expires.
- Long Comm Timeout: Allows the host to put the device in SLEEP or SHUTDOWN modes for power saving, timer resets every time a valid response or command frame is received, executes Long Timeout Action when timer expires.
- Long Timeout Action: On a long timeout, either send the device to SLEEP and set a CTL system fault or send the device to SHUTDOWN.

The GUI also supports communication debug mode of the BQ79616, which can be enabled via the Debug Control slider. Debug mode grants the user control of the COMH/L receivers and transmitters, and also allows the user to toggle the UART TX and UART Mirror functions on stack devices. Note that the base device should always have its UART TX enabled and UART mirror disabled, so these toggles are disabled for broadcast and base device communication modes.

## 6.2 Control Register and Tones

This tab provides the user with the ability to both send tones and change bits in the CONTROL1 register of a device via buttons labeled by function.

A tone is a set of pulses that travels through COMH and COML ports. For the BQ79616, WAKE and SLEEPtoACTIVE tones are propagable, meaning that once one device receives either tone, it generates the same tone to send to the next device up the stack. Conversely, SHUTDOWN and HW RESET tones are nonpropagable, meaning that a tone is not generated to the next device in the stack. Therefore, to shutdown or reset all connected devices, all CONTROL1 registers must be written to.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_033.png)

This tab also features other relevant tones and CONTROL1 bits. All buttons on this tab are grouped by general function: wake, shutdown, reset, sleep, and communication. Variations of each function exist to allow greater flexibility in controlling the connected devices.

## 7 Diagnostics

The Diagnostics tab provides the user a sneak preview into the workings of the system level diagnostics that the BQ devices provide. These are highly important functions for designing a safe, ASIL rated system.

On the left hand side, there are start/stop buttons that turn on/off the MAIN &amp; AUX ADCs that are both required to be ON for the device to allow diagnostics to be completed. Below the start/stop buttons are AUX ADC settings that the user can configure to lock to certain channels, gpios, or change the settling time.

After the user has started the main/aux adcs and set desired aux settings the user can select a diagnostic mode in the dropdown above the green "start diagnostics" button. As an example, the Cell Voltage Measurement diagnostic is shown below. This diagnostic will do a simple comparison between the Main ADC voltage level and the AUX ADC level for the selected AUX channel(s). Once the user selects their desired voltage threshold, select green"Start Diagnostics" button which will either trigger a notification that the diagnostic completed or aborted. See the BQ79616-Q1 datasheet for details on abort conditions. If the diagnostic completed, it will update the VCCB1, VCCB2, LPF text to red or green. Green meaning that there are no failures in the corresponding register and red indicating that there are failures. Hover over VCCB1 to see the linked register (FAULT\_COMP\_VCCB1). If the VCCB1 text is red, then the user can then navigate to the register map and search for FAULT\_COMP\_VCCB1 to see the exact bit level cell failures.

Figure 7-1. Diagnostics Tab

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_034.png)

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_035.png)

[www.ti.com](https://www.ti.com/)

## 8 Command Sequence

The Command Sequence tab allows the user to easily create custom commands and organize them into a script. This allows the user flexibility to run different sets of sequences and add delays in between.

On the left side is where the user actually inputs the command of choice and can send the frame to the command dialog window in the center. To get more detailed information on how the command dialog menu works, please select the "Help" icon on the bottom right below the command dialog window. The user can send several commands to this dialog window and then Save or Load this as a .txt file. Pressing the Start button will actually send the commands to the device and the data will be shown in the transaction log on the right hand side of the page. This log can be saved to a file. The user can also save several scripts to quick access buttons using the empty slots at the top middle of the page.

Commands can be written to any device in the system through this page by changing the device address on the left side of the page.

Figure 8-1. Command Sequence Tab

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_036.png)

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_037.png)

## 9 Faults

The Faults tab provides the user a quick access page to view all current status of the device faults and an easier method to mask faults. The user can select the SHOW button on the right hand side underneath the FAULT DETAILS column in order to view the faults in more detail, reset certain fault registers, and mask them.

Figure 9-1. Faults Tab

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_038.png)

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_007.png)

[www.ti.com](https://www.ti.com/)

## 10 Register Map

The register map page displays all relevant writeable and readable registers for any devices being used. The registers are grouped by general function, that is measurements, protection, and so forth. If there are multiple connected devices, the device being displayed can be switched with a drop-down menu at the top of the page.

Figure 10-1. BQ79616 GUI Register Map Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_039.png)

## 10.1 Register Display

In the register display, registers are displayed with their names, addresses, and values. Double clicking on any bit flips the value and immediately writes it to the corresponding register. In Deferred Write mode, register writes can be queued up and executed by pressing either write button. Upon selecting a register, an information button next to the register name appears. Clicking on the button reveals more about the selected register, including the default value and information about the fields within the register.

A field view also opens up on the right side of the screen that allows the user to directly edit certain register fields. Selecting a field in the field view also displays an information button. Clicking on it displays the name of a field, the bits it occupies within the register, and its type.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_037.png)

Figure 10-2. BQ79616 GUI Register Map Field View

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_040.png)

The registers are grouped by general function, making it easy to find relevant registers when debugging or operating the device via the register map. The user can also search for the registers in the search bar by name or address (leading with 0x...).

## 10.2 Register Read

An individual register can be read by selecting a register and pressing Read Register, and pressing Read All Registers reads all registers for a single device. Auto-read can be enabled to update the values in the register map at a selected time interval.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_007.png)

[www.ti.com](https://www.ti.com/)

## 11 Debug

From this page, the user can directly perform register reads and writes to the connected devices. This provides some extended functionality that is not present on the GUI front end.

Figure 11-1. BQ79616 GUI Debug Page

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_041.png)

## 11.1 Write and Read

The first step in communicating with the device is to use the initialization byte that corresponds to the intended communication type. A summary of the different initialization bytes available to the user can be found in the table below.

Table 11-1. Initialization Bytes

| Communication Type | Initialization Byte (1) |
| - | - |
| Single Device Read | 0x80 |
| Single Device Write | 0x9* |
| Stack Read | 0xA0 |
| Stack Write | 0xB* |
| Broadcast Read | 0xC0 |
| Broadcast Write | 0xD* |

(1) For write operations, replace asterisks with the number of bytes to be written minus one up to a maximum of 8 bytes written simultaneously.

Second, the user specifies the device to be communicated to via the Device Address field. This field is only available for single device communication, as the stack and broadcast communication modes communicate to multiple devices. Third, the user specifies the Register Address to be written to. Last, the user fills out the Data Bytes field. For a read, the data bytes should be the number of bytes to be read minus one. For a write, the data bytes are the bytes to be written.

For both reads and writes, the user should then press the Write button. For read commands, a write button press also performs a read from the device, and the response is populated in the response bytes window.

![Image](BQ79616-Q1%20and%20BQ75614-Q1%20GUI%20Users%20Guide%20%28sluuc36%29_files/img_002.png)

## 12 Current Sensing

For users attempting to take current sense measurements using the SRP/SRN pins of the BQ75614-Q1 or BQ79631-Q1 device, the steps are explained below using this GUI:

- 1) First open the GUI and select the bq75614-Q1 or bq79631-Q1 device as the bridge. Then initialize the device in the "CELL MONITOR" tab, and begin ADC measurements by pressing: 1. WAKE UP 2. AUTO ADDRESS 3. Start Polling
- 2) Get a voltage reading from the CS ADC via two columns in the cell monitor page. There is a 16 bit reading and a 24 bit reading populated in the two columns that will update by default when polling is enabled.
- 3) If the user would like to convert manually, they can use the values from the CURRENT\_HI/MID/LO registers (hex value of the registers to read are 0x5D6-0x5D8). Then the value needs to be converted to decimal and multiplied by 14.9nV from the datasheet (when using 24-bit result).

## 13 Troubleshooting

## 13.1 Common Issues

1. If the GUI does not prompt the Hardware Connected indicator at the bottom left, it is likely a USB2ANY firmware issue or connection. Please restart the steps in section 1.1.3 and carefully read over the proper steps.
2. If the GUI ever has any issues in terms of updating data or buttons not responding:
- a. Right click anywhere on the GUI and Reload app. Wake up the devices and run auto addressing.
- b. If the problem persists, reload the latest firmware on the USB2ANY via the USB2ANY Firmware Loader even if it has already been loaded previously.

## 13.2 Best Practices

The best method to first ensure proper communication is to first navigate to the cell monitor page and then 1) Click Wake Up 2) Click Auto Address (the # of devices you have powered on the stack should populate into the table with all 0's) 3) Start Polling and ensure data is updating in the table.

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2022, Texas Instruments Incorporated
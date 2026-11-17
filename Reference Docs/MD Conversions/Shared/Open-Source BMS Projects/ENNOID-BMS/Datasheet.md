<!-- Converted from Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

## ENNOID

## Applications

- Electric vehicles
- Drones
- Energy storage
- Research programs

## Product summary

ENNOID-BMS is a configurable battery management system consisting of a Master board based on an STM32 microcontroller connected through an ISOSPI interface to several modular slave boards. ENNOIDBMS can monitor the specifics temperatures, currents &amp; voltages that are critical for any lithium-ion battery packs. Based on the monitored inputs &amp; the configured parameters, the master board can allow or interrupt the flow of energy from the battery pack by switching the state of external heavy-duty contactors. ENNOID-BMS can measure each cell voltage level &amp; can trigger the passive balancing function during charging for cells above the configured limit to ensure that all cells have a similar State-Of-Charge (SOC). Parameters can be configured through the ENNOIDBMS-Tool software running on a USB connected host computer.

## Block diagram

Figure 1 : Simplified block diagram

![Image](Datasheet_files/img_001.png)

## Features

- Modular with master/slave topology
- 12S, 15S &amp; 18S slaves board options
- Master board options: High Voltage (Master-HV) &amp; Low voltage (Master-LV)
- Up to 500A continuous operation
- Integrated bi-directional current sensor
- 12V drive coil outputs for charge, discharge &amp; auxiliary circuits
- Communication between slaves &amp; master through a two-wire daisy chained ISOSPI interface
- Isolated CAN bus interface
- Isolated charger detection circuit
- Voltage measurement for battery pack &amp; load
- Build-in precharge circuits
- USB interface for programming and firmware upgrades through an easy to use graphical user interface
- OLED Display, serial output &amp; power button
- 0V to 5V cell voltage operation

## ENNOID-BMS

## Datasheet

![Image](Datasheet_files/img_002.png)

## Master-LV board

Our Master-LV boards is able to monitor battery packs with voltages of 150V or less.

## Particularities:

- 150V maximum allowed voltage
- Single PCB pattern for bolt-on main contactor (EVC500 or similar)
- No isolation IC between power &amp; logic

Figure 1: Master-LV board

![Image](Datasheet_files/img_003.png)

## ENNOID-BMS

## Datasheet

![Image](Datasheet_files/img_004.png)

## Master-HV board

Our Master-HV boards is able to monitor battery packs with voltages of up to 400V.

## Particularities:

- 400V maximum allowed voltage
- Dual PCB patterns for bolt-on main contactors (EVC500 or similar)
- Isolation for current sensor
- Isolation for pack &amp; load voltages measurements

Figure 2 : Master-HV board

![Image](Datasheet_files/img_005.png)

## Master pinout

| Pinout name | Pinout description | Pinout description |
| - | - | - |
| Power* | + | Positive output for PSU |
| Power* | - | Negative output for PSU |
| 12V | + | Positive 12V input |
| 12V | - | Negative 12V input |
| Discharge | + | Positive 12V ouput for discharge contactor |
| Discharge | - | GND |
| E-Stop* | + | Positive E-Stop terminal |
| E-Stop* | - | Negative E-Stop terminal |
| Charger |  | Not connected when using an external charger input |
| Charger | + | Voltage monitoring to charger |
| Charge* | + | Positive 12V ouput for Charge contactor |
| Charge* | - | GND |
| Cooling* | + | Positive 12V ouput for cooling contactor |
| Cooling* | - | GND |
| ISOSPI | PA | Isolated ISOSPI communication 2 wire interfaces with slave boards |
| ISOSPI | MA | Isolated ISOSPI communication 2 wire interfaces with slave boards |
| USB* | Micro-USB interface with ENNOID-BMS-tool software on a computer | Micro-USB interface with ENNOID-BMS-tool software on a computer |
| CAN* | EN | External enable signal |
| CAN* | 5V | External 5V for CAN |
| CAN* | H | CANH |
| CAN* | L | CANL |
| CAN* | GND | CANGND |
| OLED* | 3.3V | +3.3V |
| OLED* | RST | No connect |
| OLED* | SDA | SDA signal output for OLED display |
| OLED* | SCL | SCL signal output for OLED display |
| OLED* | GND | ISOGND |
| Power Button* | GND | ISOGND |
| Power Button* | N.O. | Normally open pin for power button |
| Power Button* | 3.3V | No connect +3.3V |
| Power Button* | LED | +3.3V for LED (optional) |
| Power Button* | GND | ISOGND |
| Debug* | +3.3V | +3.3V |
| Debug* | SWCLK | SWCLK |
| Debug* | ISOGND | ISOGND |
| Debug* | SWDIO | SWDIO |
| Debug* | NRST | NRST |

*Not mandatory for operation

## ENNOID

## Slave board LTC68XX

The slave board are equipped with LTC68XX multicell battery monitor IC. The slave boards are powered directly by the lithium-ion cells they monitor. LTC6811, LTC6812, &amp; LTC6813 based slave boards are offered.

![Image](Datasheet_files/img_006.png)

Figure 3: Slave board ( LTC6811-12S shown )

| Pinout name | Pinout description | Pinout description |
| - | - | - |
| PA-MA | Isolated ISOSPI communication 2 wire interfaces towards previous slave board or master board | Isolated ISOSPI communication 2 wire interfaces towards previous slave board or master board |
| PB-MB | Isolated ISOSPI communication 2 wire interfaces towards next slave board | Isolated ISOSPI communication 2 wire interfaces towards next slave board |
| Cells** | 0 | Connect to negative voltage of the battery module |
| Cells** | 1 to XX | Connect all subsequent pins to the next cells positive voltage levels. |
| Temp* | GND | Common temperature sensors negative terminal |
| Temp* | 2 to X | Individual temperature sensor positive terminal. |

- *Not mandatory for operation. Channel 1 is used for internal slave board temperature measurement. All channels can be disabled with ENNOID-BMS Tool. Recommended to use with : NTC 100kΩ β:4250
- ** If not all cells measurement channels are required, the user should short all the remaining unused channels with the last used measurement channel for better precision or leave unconnected. Ex: LTC6812 slave board monitoring 13 cells, Pin 13, 14 &amp; 15 should be all connected together to the last positive cell terminal.

## ENNOID-BMS

## Datasheet

![Image](Datasheet_files/img_004.png)

## ENNOID

## Other related hardware

## Current sensor

We recommend using ENNOID-BMS integrated 500A current sensor. Other CAN bus current sensors are also supported.

## Power supply

We recommend using our ENNOID-BMS PSU board: 0-400V input isolated with 12V-5A DC output

ENNOID-BMS require a 12V power supply which can supply power for the Master-BMS board. A peak current of approx. 3A is required for a few milliseconds for closing the high current external contactors. Only a few milliamps are required afterward closing. The power supply must be able to handle contactors peak loads.

## OLED display

SSD1306 compatible OLED display is not mandatory for operating ENNOID-BMS but is recommended.

## Power button

Power button N.O. type toggle switch is normally required for activating ENNOID-BMS. External activation of ENNOID-BMS is also possible through CAN bus.

## Contactor

EVC500 or similar contactors with built-in economizer are required.

![Image](Datasheet_files/img_004.png)

## Software

Download ENNOID-BMS-Tool software for windows:

[https://github.com/EnnoidMe/ENNOID-BMS-Tool/releases](https://github.com/EnnoidMe/ENNOID-BMS-Tool/releases)

![Image](Datasheet_files/img_007.png)

## ENNOID-BMS configuration

1. Connect at minimum a 12V power supply to ENNOID-BMS Master board.
2. Connect a host computer running the ENNOID-BMS-Tool to the ENNOID-BMS master board with a micro USB cable. (Warning: some cheap USB cables cannot carry data and won't work with ENNOIDBMS) Power LED indicator should light up. Click connect on the connection page. The app should now show "connected" in the right side bottom corner.
3. Go into firmware tab and upload latest firmware (this step is needed only for initial setup or uploading a new firmware version)
4. Under "Master Settings" tab, user can define all parameters of the BMS. Modified parameters can be read, applied &amp; saved by clicking on the associated buttons on the right-side panel.
5. After initial configuration, the user can connect battery, ISOSPI &amp; load.
6. For real-time data logging &amp; for testing purposes, the "Data Analysis" tab shows in real time the measured pack voltage, load voltage, current, Temperatures, BMS status &amp; all cells voltages. You need to click on the "RT" button on the right side of the screen to activate real time communication.
7. Once properly configured, you can operate the ENNOID-BMS &amp; your personalized battery pack without a host computer.
8. For specific projects, the power button &amp; the OLED display can be bypassed by using the CAN bus communication option. The BMS can be configured to communicate through CAN bus with a motor controller, charger &amp; with a vehicle control unit that implement the VESC standard.
9. Other standard or features can be developped for the user uppon special request. Contact us : kevin.dionne@ennoid.me

Enjoy!
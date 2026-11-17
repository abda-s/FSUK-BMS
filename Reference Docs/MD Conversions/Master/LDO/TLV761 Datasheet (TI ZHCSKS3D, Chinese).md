<!-- Converted from TLV761 Datasheet (TI ZHCSKS3D, Chinese).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_001.png)

ÍNSTRUMENTS

## 1 特性

- 与采用选定封装的业界通用 LM1117 和 TLV1117 (x1117) 器件引脚对引脚兼容
- 输入电压范围 VIN：2.5V 至 18V（20V 绝对最大额 定值）
- 输出电压范围 VOUT：
- 0.8V 至 13V（固定值，100mV 阶跃）
- 输出电流：高达 1A
- 低静态电流 IQ：
- 60µA（典型值，关断时约 1.5µA）
- 在线路和负载范围内 ±1% 的输出精度
- 高 PSRR：1kHz 频率下为 60dB，1MHz 频率下为 40dB
- 内部软启动时间：500µs（典型值）
- 折返电流限制和热保护
- 与 1µF 的陶瓷输出电容器搭配使用时可保持稳定
- 温度范围：-40°C 至 +125°C
- 封装：
- 4 引脚 6.5mm x 7mm SOT-223
- 3 引脚 6.6mm x 10.11mm TO-252

## 2 应用

- [电器](http://www.ti.com/applications/industrial/appliances/overview.html)
- [家庭影院和娱乐系统](http://www.ti.com/applications/personal-electronics/home-theater-entertainment/overview.html)
- [电机驱动器](http://www.ti.com/applications/industrial/motor-drives/overview.html)
- [HVAC 和楼宇安全系统](http://www.ti.com/applications/industrial/building-automation/overview.html)
- [智能电表](https://www.ti.com/solution/electricity-meter)

COUT 为 22µF 时的浪涌电流

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_002.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_003.png)

## TLV761 18V、1A、固定输出线性稳压器

## 3 说明

TLV761 是一款线性稳压器，在传统 x1117 稳压器 （TLV1117 或 LM1117）的基础上改进了功能，具有更 严格的输出精度和低静态电流 (IQ)，可降低待机功耗。 TLV761 与其他采用 SOT-223、TO-252 封装且具有固 定输出的稳压器引脚对引脚兼容。

TLV761 输入电压范围为 2.5V 至 18V，提供的输出电 压范围为 0.8V 至 13V，可支持各种应用。

TLV761 的宽带宽 PSRR 性能通常在 1kHz 时大于 60dB，在 1MHz 时大于 40dB，因此有助于减小上游 直流/直流转换器的开关频率，并更大限度地减少后置 稳压器滤波。

此外，TLV761 还具有内部软启动功能，可减少启动期 间的浪涌电流，这有助于通过尽可能减少输入电容来节 省设计空间和成本。TLV761 具有折返电流限制，可在 高负载电流故障或短路事件期间限制器件的功率耗散。

## 封装信息

| 器件型号 | 封装 (1) | 封装尺寸 (2) |
| - | - | - |
| TLV761 | DCY（SOT-223， 4） | 6.5mm × 7mm |
| TLV761 | KVU（TO-252，3） | 6.6mm × 10.11mm |

- (1) 如需更多信息，请参阅机械、封装和可订购信息。
- (2) 封装尺寸（长 × 宽）为标称值，并包括引脚（如适用）。

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_004.png)

[TLV761](https://www.ti.com.cn/product/cn/tlv761?qgpn=tlv761)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_005.png)

## Table of Contents

| 1 特性................................................................................... 1 2 应用................................................................................... 1 3 说明................................................................................... 1 4 Pin Configuration and Functions...................................3 5 Specifications.................................................................. 4 5.1 Absolute Maximum Ratings........................................ 4 5.2 ESD Ratings............................................................... 4 5.3 Recommended Operating Conditions.........................4 5.4 Thermal Information....................................................5 5.5 Electrical Characteristics.............................................5 5.6 Typical Characteristics................................................6 6 Detailed Description......................................................10 6.1 Overview...................................................................10 6.2 Functional Block Diagram.........................................10 6.3 Feature Description...................................................10 6.4 Device Functional Modes..........................................12 7 Application and Implementation..................................13 | 7.1 Application Information............................................. 13 7.2 Typical Application.................................................... 15 7.3 Best Design Practices...............................................17 7.4 Power Supply Recommendations.............................17 7.5 Layout....................................................................... 18 8 Device and Documentation Support............................19 8.1 Device Support......................................................... 19 8.2 Documentation Support............................................ 19 8.3 接收文档更新通知..................................................... 19 8.4 支持资源....................................................................19 8.5 Trademarks...............................................................19 8.6 静电放电警告............................................................ 19 8.7 术语表....................................................................... 19 9 Revision History............................................................ 20 10 Mechanical, Packaging, and Orderable Information.................................................................... 20 |
| - | - |

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_006.png)

## 4 Pin Configuration and Functions

图 4-1. DCY Package, 4-Pin SOT-223 (Top View)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_007.png)

图 4-2. KVU Package, 3-Pin TO-252 (Top View)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_008.png)

表 4-1. Pin Functions

| PIN - NAME | PIN - DCY | PIN - KVU | PIN - FUNCTION | DESCRIPTION |
| - | - | - | - | - |
| GND | 1 | 1 | - | Ground pin |
| OUT | 2, Tab | 2, Tab | O | Output pin. Use the recommended capacitor value as listed in the Recommended Operating Conditions table. Place the output capacitor as close to the OUT and GND pins of the device as possible. |
| IN | 3 | 3 | I | Input pin. Use the recommended capacitor value as listed in the Recommended Operating Conditions table. Place the input capacitor as close to the IN and GND pins of the device as possible. |

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_009.png)

## 5 Specifications

## 5.1 Absolute Maximum Ratings

Over operating free-air temperature range (unless otherwise noted) (1)

|  |  | MIN | MAX | UNIT |
| - | - | - | - | - |
| Voltage (2) | VIN | -0.3 | 20 | V |
| Voltage (2) | VOUT (3) | -0.3 | VIN + 0.3 | V |
| Current | Maximum output current | Internally limited | Internally limited | A |
| Power | Power dissipation | Package limited (4) | Package limited (4) | W |
| Temperature | Operating junction (TJ) | -50 | 150 | °C |
| Temperature | Storage (TSTG) | -65 | 150 | °C |

(1) Stresses beyond those listed under Absolute Maximum Rating may cause permanent damage to the device. These are stress ratings only, which do not imply functional operation of the device at these or any other conditions beyond those indicated under Recommended Operating Condition. Exposure to absolute-maximum-rated conditions for extended periods may affect device reliability.

- (2) All voltages with respect to GND.
- (3) VIN + 0.3 V or 18 V (whichever is smaller).
- (4) See thermal information for further details.

## 5.2 ESD Ratings

|  |  |  | VALUE | UNIT |
| - | - | - | - | - |
| V(ESD) | Electrostatic discharge | Human body model (HBM), per ANSI/ESDA/ JEDEC JS-001, all pins (1) | ±3000 | V |
| V(ESD) |  | Charged device model (CDM), per JEDEC specification JESD22-C101, all pins (2) | ±1000 | V |

- (1) JEDEC document JEP155 states that 500-V HBM allows safe manufacturing with a standard ESD control process.
- (2) JEDEC document JEP157 states that 250-V CDM allows safe manufacturing with a standard ESD control process.

## 5.3 Recommended Operating Conditions

over operating free-air temperature range (unless otherwise noted)

|  |  | MIN | NOM | MAX | UNIT |
| - | - | - | - | - | - |
| VIN | Input voltage | 2.5 |  | 18 | V |
| VOUT | Output voltage | 0.8 |  | 13.5 | V |
| IOUT | Output current (2.5 V ≤ VIN < 3 V) | 0 |  | 0.8 | A |
| IOUT | Output current (VIN ≥ 3 V) | 0 |  | 1 | A |
| COUT ESR | Output capacitor ESR | 2 |  | 500 | mΩ |
| COUT | Output capacitor (1) | 1 | 2.2 | 220 | µF |
| CIN | Input capacitor (2) |  | 1 |  | µF |
| TJ | Junction temperature | -40 |  | 125 | °C |

- (1) Effective output capacitance of 0.47 µF minimum required for stability.

(2) An input capacitor is not required for LDO stability. However, an input capacitor with an effective value of 0.47 μF minimum is recommended to counteract the effect of source resistance and inductance, which may in some cases cause symptoms of systemlevel instability such as ringing or oscillation, especially in the presence of load transients

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_010.png)

## 5.4 Thermal Information

| THERMAL METRIC (1) | THERMAL METRIC (1) | TLV761 - DCY (SOT-223) - 4 PINS | TLV761 - KVU (TO-252) - 4 PINS | UNIT |
| - | - | - | - | - |
| RθJA | Junction-to-ambient thermal resistance | 95.4 | 67.2 | °C/W |
| RθJC(top) | Junction-to-case (top) thermal resistance | 55.6 | 71.8 | °C/W |
| RθJB | Junction-to-board thermal resistance | 33.7 | 45.5 | °C/W |
| ΨJT | Junction-to-top characterization parameter | 13.9 | 31.6 | °C/W |
| ΨJB | Junction-to-board characterization parameter | 33.4 | 45.4 | °C/W |
| RθJC(bot) | Junction-to-case (bottom) thermal resistance | N/A | 40.5 | °C/W |

(1) For more information about traditional and new thermal metrics, see the Semiconductor and IC Package Thermal Metrics application note.

## 5.5 Electrical Characteristics

specified at TJ = -40°C to 125°C, VIN = VOUT(nom) + 1.5V or VIN = 2.5V (whichever is greater), IOUT = 10mA, CIN = 1.0µF and COUT = 1.0µF (unless otherwise noted); typical values are at TJ= 25ºC

| PARAMETER | PARAMETER | TEST CONDITIONS | MIN | TYP | MAX | UNIT |
| - | - | - | - | - | - | - |
| VOUT | Nominal output accuracy | TJ = 25°C | -1 |  | 1 | % |
| VOUT | Output accuracy over temperature | VIN ≥ 3.0V, VOUT(NOM) ≤ 9.0V, 1mA ≤ IOUT ≤ 1A | - 1.75 |  | 1.75 | % |
| VOUT | Output accuracy over temperature | VOUT(NOM) > 9.0V, 1mA ≤ IOUT ≤ 1A | -1.5 |  | 1.5 | % |
| ΔVOUT(ΔVIN) | Line regulation (1) | VOUT(NOM) ≤ 9.0V, VOUT(NOM) + 1.5V ≤ VIN ≤ 18V, IOUT = 10mA |  |  | 0.02 | %/V |
| ΔVOUT(ΔVIN) | Line regulation (1) | VOUT(NOM) > 9.0V, VOUT(NOM) + 1.5V ≤ VIN ≤ 18V, IOUT = 10mA |  |  | 9.9 | mV |
| ΔVOUT(Δ IOUT) | Load regulation | 1mA ≤ IOUT ≤ 1A, VIN ≥ 3.0V |  | 0.1 | 0.75 | %/A |
| VDO | Dropout voltage (2) | VIN ≥ 3.0V, IOUT = 1A |  | 0.9 | 1.6 | V |
| ICL | Output current limit | VOUT = 0.9 x VOUT(NOM) , VIN ≥ 3.0V | 1.1 |  | 1.6 | A |
| ISC | Short-circuit current limit | VOUT = 0V | 150 | 250 | 350 | mA |
| IQ | Quiescent current | IOUT = 0mA |  | 65 | 100 | µA |
| IPULLDOWN | Output pulldown current (3) | VIN = 1.8V, VOUT = 2.5V | 0.7 |  | 1.1 | mA |
| PSRR | Power-supply rejection ratio | VIN = 3.3V, VOUT = 1.8V, IOUT = 300mA, f = 120Hz |  | 70 |  | dB |
| Vn | Output noise voltage | BW = 10Hz to 100kHz, VIN = 3.3V, VOUT = 0.8V, IOUT = 100mA |  | 60 |  | µVRMS |
| VUVLO+ | UVLO threshold rising | VIN rising |  | 2.2 | 2.4 | V |
| VUVLO(HYS) | UVLO hysteresis |  |  | 130 |  | mV |
| VUVLO- | UVLO threshold falling | VIN falling | 1.9 |  |  | V |
| TSD(shutdown) | Thermal shutdown temperature | Temperature increasing |  | 180 |  | ºC |
| TSD(reset) | Thermal shutdown reset temperature | Temperature falling |  | 160 |  | ºC |

(1) Line regulation is measured with VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater).

(2) VDO is measured with VIN = 95% x VOUT(nom) for fixed output devices. VDO is not measured for fixed output devices when VOUT &lt; 2.5 V.

(3) IPULLDOWN is measured with VIN = 1.8 V (lower than UVLO falling threshold, with LDO in disabled state) and 2.5 V applied on VOUT externally.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_011.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_012.png)

## 5.6 Typical Characteristics

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_013.png)

For VIN ≥ 3.0 V

图 5-1. VOUT Accuracy vs IOUT

0.2

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_014.png)

IOUT = 10 mA

图 5-2. VOUT Accuracy vs VIN

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_015.png)

IOUT = 0 mA

图 5-3. IQ vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_016.png)

IOUT = 0 mA

图 5-4. IQ Increase Below Minimum VIN

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_017.png)

图 5-5. IGND vs IOUT

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_018.png)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.4 A/µs

图 5-6. IOUT Transient From 0 mA to 100 mA

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_019.png)

## 5.6 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.5 A/µs

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_020.png)

图 5-7. IOUT Transient From 1 mA to 1 A

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_021.png)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.8 A/µs

图 5-8. IOUT Transient From 250 mA to 850 mA

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_022.png)

VIN = 5 V VOUT = 3.3 V, IOUT = 1 A, VIN ramp rate = 0.6 V/µs

图 5-9. VIN Transient in Dropout From 4 V to 13 V

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_023.png)

VOUT = 3.3 V, IOUT = 33 µA, VIN ramp rate = 1.6 V/µs

图 5-10. VIN Transient From 5 V to 16 V

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_024.png)

图 5-11. VDO vs VIN

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_025.png)

IOUT = 0.8 A

图 5-12. VDO vs VIN

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_011.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_012.png)

## 5.6 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

图 5-13. UVLO Thresholds vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_026.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_027.png)

For VIN ≥ 3.0 V

图 5-14. VDO vs IOUT

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_028.png)

For VIN ≥ 3.0 V

图 5-15. Foldback Current Limit vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_029.png)

图 5-16. Foldback Current Limit vs Temperature

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_030.png)

VOUT = 1.8 V, VIN = 3.3 V

图 5-17. PSRR vs IOUT

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_031.png)

0001

VOUT = 1.8 V, IOUT = 0.55 A

图 5-18. PSRR vs VIN

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_032.png)

## 5.6 Typical Characteristics (continued)

at operating temperature TJ = 25°C, VIN = VOUT(NOM) + 1.5 V or 2.5 V (whichever is greater), IOUT = 10 mA, CIN = 1.0 µF, and COUT = 1.0 µF (unless otherwise noted)

IOUT = 0.1 A, RMS noise BW = 10 Hz to 100 kHz

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_033.png)

图 5-19. Output Noise (Vn) vs VOUT

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_034.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_011.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_012.png)

## 6 Detailed Description

## 6.1 Overview

The TLV761 is a low quiescent current, high PSRR linear regulator capable of sourcing load current up to 1 A. This device is designed for high current applications such as appliances where there are increasingly stringent requirements for standby and active power consumption.

This device features integrated foldback current limit, thermal shutdown, internal output pulldown, and undervoltage lockout (UVLO). This device delivers excellent line and load transient performance. The TLV761 is low noise and exhibits very good PSRR. The operating ambient temperature range of the device is -40°C to +125°C.

## 6.2 Functional Block Diagram

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_035.png)

## 6.3 Feature Description

## 6.3.1 Dropout Voltage

Dropout voltage (VDO) is defined as the input voltage minus the output voltage (VIN - VOUT) at the rated output current (IRATED), where the pass transistor is fully on. IRATED is the maximum IOUT listed in the Recommended Operating Conditions table. The pass transistor is in the ohmic or triode region of operation, and acts as a switch. The dropout voltage indirectly specifies a minimum input voltage greater than the nominal programmed output voltage at which the output voltage is expected to stay in regulation. If the input voltage falls to less than the nominal output regulation, then the output voltage falls as well.

For a CMOS regulator, the dropout voltage is determined by the drain-source on-state resistance (RDS(ON)) of the pass transistor. Therefore, if the linear regulator operates at less than the rated current, the dropout voltage for that current scales accordingly. The following equation calculates the RDS(ON) of the device.

<!-- formula-not-decoded -->

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_036.png)

## 6.3.2 Foldback Current Limit

The device has an internal current limit circuit that protects the regulator during transient high-load current faults or shorting events. The current limit is a hybrid brick-wall-foldback scheme. The current limit transitions from a brick-wall scheme to a foldback scheme at the foldback voltage (VFOLDBACK). In a high-load current fault with the output voltage above VFOLDBACK, the brick-wall scheme limits the output current to the current limit (ICL). When the voltage drops below VFOLDBACK, a foldback current limit activates that scales back the current as the output voltage approaches GND. When the output is shorted, the device supplies a typical current called the shortcircuit current limit (ISC). ICL and ISC are listed in the Electrical Characteristics table.

For this device, VFOLDBACK = 50% × VOUT(nom).

The output voltage is not regulated when the device is in current limit. When a current limit event occurs, the device begins to heat up because of the increase in power dissipation. When the device is in brick-wall current limit, the pass transistor dissipates power [(VIN - VOUT) × ICL]. When the device output is shorted and the output is below VFOLDBACK, the pass transistor dissipates power [(VIN - VOUT) × ISC]. If thermal shutdown is triggered, the device turns off. After the device cools down, the internal thermal shutdown circuit turns the device back on. If the output current fault condition continues, the device cycles between current limit and thermal shutdown. For more information on current limits, see the Know Your Limits application note.

图 6-1 shows a diagram of the foldback current limit.

图 6-1. Foldback Current Limit

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_037.png)

## 6.3.3 Undervoltage Lockout (UVLO)

The device has an independent undervoltage lockout (UVLO) circuit that monitors the input voltage, allowing a controlled and consistent turn on and off of the output voltage. To prevent the device from turning off if the input drops during turn on, the UVLO has hysteresis as specified in the Electrical Characteristics table.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_038.png)

X

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_009.png)

## 6.3.4 Thermal Shutdown

The device contains a thermal shutdown protection circuit to disable the device when the junction temperature (TJ) of the pass transistor rises to TSD(shutdown) (typical). Thermal shutdown hysteresis assures that the device resets (turns on) when the temperature falls to TSD(reset) (typical).

The thermal time-constant of the semiconductor die is fairly short, thus the device may cycle on and off when thermal shutdown is reached until power dissipation is reduced. Power dissipation during start-up can be high from large VIN - VOUT voltage drops across the device or from high inrush currents charging large output capacitors. Under some conditions, the thermal shutdown protection disables the device before start-up completes.

For reliable operation, limit the junction temperature to the maximum listed in the Recommended Operating Conditions table. Operation above this maximum temperature causes the device to exceed operational specifications. Although the internal protection circuitry of the device is designed to protect against thermal overall conditions, this circuitry is not intended to replace proper heat sinking. Continuously running the device into thermal shutdown or above the maximum recommended junction temperature reduces long-term reliability.

## 6.4 Device Functional Modes

## 6.4.1 Device Functional Mode Comparison

表 6-1 shows the conditions that lead to the different modes of operation. See the Electrical Characteristics table for parameter values.

表 6-1. Device Functional Mode Comparison

| OPERATING MODE | PARAMETER - VIN | PARAMETER - IOUT | PARAMETER - TJ |
| - | - | - | - |
| Normal operation | VIN > VOUT(nom) + VDO and VIN > VIN(min) | IOUT < IOUT(max) | TJ < TSD(shutdown) |
| Dropout operation | VIN(min) < VIN < VOUT(nom) + VDO | IOUT < IOUT(max) | TJ < TSD(shutdown) |
| Disabled (any true condition disables the device) | VIN < VUVLO | Not applicable | TJ > TSD(shutdown) |

## 6.4.2 Normal Operation

The device regulates to the nominal output voltage when the following conditions are met:

- The input voltage is greater than the nominal output voltage plus the dropout voltage (VOUT(nom) + VDO)
- The output current is less than the current limit (IOUT &lt; ICL)
- The device junction temperature is less than the thermal shutdown temperature (TJ &lt; TSD)

## 6.4.3 Dropout Operation

If the input voltage is lower than the nominal output voltage plus the specified dropout voltage, but all other conditions are met for normal operation, the device operates in dropout mode. In this mode, the output voltage tracks the input voltage. During this mode, the transient performance of the device becomes significantly degraded because the pass transistor is in the ohmic or triode region, and acts as a switch. Line or load transients in dropout can result in large output-voltage deviations.

When the device is in a steady dropout state (defined as when the device is in dropout, VIN &lt; VOUT(NOM) + VDO, directly after being in a normal regulation state, but not during start-up), the pass transistor is driven into the ohmic or triode region. When the input voltage returns to a value greater than or equal to the nominal output voltage plus the dropout voltage (VOUT(NOM) + VDO), the output voltage can overshoot for a short period of time while the device pulls the pass transistor back into the linear region.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_039.png)

## 7 Application and Implementation

## 备注

以下应用部分中的信息不属于TI 器件规格的范围，TI 不担保其准确性和完整性。TI 的客 户应负责确定 器件是否适用于其应用。客户应验证并测试其设计，以确保系统功能。

## 7.1 Application Information

## 7.1.1 Recommended Capacitor Types

The device is designed to be stable using low equivalent series resistance (ESR) ceramic capacitors at the input and output. Multilayer ceramic capacitors have become the industry standard for these types of applications and are recommended, but must be used with good judgment. Ceramic capacitors that employ X7R-, X5R-, and C0G-rated dielectric materials provide relatively good capacitive stability across temperature, whereas the use of Y5V-rated capacitors is discouraged because of large variations in capacitance.

Regardless of the ceramic capacitor type selected, the effective capacitance varies with operating voltage and temperature. Generally, expect the effective capacitance to decrease by as much as 50%. The input and output capacitors recommended in the Recommended Operating Conditions table account for an effective capacitance of approximately 50% of the nominal value.

## 7.1.2 Input and Output Capacitor Requirements

Although an input capacitor is not required for stability, good analog design practice is to connect a capacitor from IN to GND. This capacitor counteracts reactive input sources and improves transient response, input ripple, and PSRR. An input capacitor is recommended if the source impedance is more than 0.5 Ω. A higher value capacitor may be necessary if large, fast rise-time load or line transients are anticipated or if the device is located several inches from the input power source.

Dynamic performance of the device is improved with the use of an output capacitor. Use an output capacitor within the range specified in the Recommended Operating Conditions table for stability.

## 7.1.3 Reverse Current

Excessive reverse current can damage this device. Reverse current flows through the intrinsic body diode of the pass transistor instead of the normal conducting channel. At high magnitudes, this current flow degrades the long-term reliability of the device.

Conditions where reverse current can occur are outlined in this section, all of which can exceed the absolute maximum rating of VOUT ≤ VIN + 0.3 V.

- If the device has a large COUT and the input supply collapses with little or no load current
- The output is biased when the input supply is not established
- The output is biased above the input supply

If reverse current flow is expected in the application, external protection is recommended to protect the device. Reverse current is not limited in the device, so external limiting is required if extended reverse voltage operation is anticipated.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_038.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_009.png)

## 图 7-1 shows one approach for protecting the device.

图 7-1. Example Circuit for Reverse Current Protection Using a Schottky Diode

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_040.png)

## 7.1.4 Power Dissipation (PD)

Circuit reliability requires consideration of the device power dissipation, location of the circuit on the printed circuit board (PCB), and correct sizing of the thermal plane. The PCB area around the regulator must have few or no other heat-generating devices that cause added thermal stress.

To first-order approximation, power dissipation in the regulator depends on the input-to-output voltage difference and load conditions. The following equation calculates power dissipation (PD).

<!-- formula-not-decoded -->

备注

Power dissipation can be minimized, and therefore greater efficiency can be achieved, by correct selection of the system voltage rails. For the lowest power dissipation use the minimum input voltage required for correct output regulation.

For devices with a thermal pad, the primary heat conduction path for the device package is through the thermal pad to the PCB. Solder the thermal pad to a copper pad area under the device. This pad area must contain an array of plated vias that conduct heat to additional copper planes for increased heat dissipation.

The maximum power dissipation determines the maximum allowable ambient temperature (TA) for the device. According to the following equation, power dissipation and junction temperature are most often related by the junction-to-ambient thermal resistance (RθJA) of the combined PCB and device package and the temperature of the ambient air (TA).

<!-- formula-not-decoded -->

Thermal resistance (RθJA) is highly dependent on the heat-spreading capability built into the particular PCB design, and therefore varies according to the total copper area, copper weight, and location of the planes. The junction-to-ambient thermal resistance listed in the Thermal Information table is determined by the JEDEC standard PCB and copper-spreading area, and is used as a relative measure of package thermal performance.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_019.png)

## 7.1.5 Estimating Junction Temperature

The JEDEC standard now recommends the use of psi (Ψ) thermal metrics to estimate the junction temperatures of the linear regulator when in-circuit on a typical PCB board application. These metrics are not thermal resistance parameters and instead offer a practical and relative way to estimate junction temperature. These psi metrics are determined to be significantly independent of the copper area available for heat-spreading. The Thermal Information table lists the primary thermal metrics, which are the junction-to-top characterization parameter (ψJT) and junction-to-board characterization parameter (ψJB). These parameters provide two methods for calculating the junction temperature (TJ). As described in the following equations, use the junctionto-top characterization parameter (ψJT) with the temperature at the center-top of device package (TT) to calculate the junction temperature. Use the junction-to-board characterization parameter (ψJB) with the PCB surface temperature 1 mm from the device package (TB) to calculate the junction temperature.

<!-- formula-not-decoded -->

## where:

- PD is the dissipated power
- TT is the temperature at the center-top of the device package

<!-- formula-not-decoded -->

## where:

- TB is the PCB surface temperature measured 1 mm from the device package and centered on the package edge

For detailed information on the thermal metrics and how to use them, see the Semiconductor and IC Package Thermal Metrics application note.

## 7.2 Typical Application

The TLV761 is a low quiescent current linear regulator designed for high current applications. Unlike most typical high current linear regulators, the TLV761 consumes significantly less quiescent current. This device delivers excellent line and load transient performance. The device is low noise and exhibits a very good PSRR. As a result, the TLV761 is designed for high current applications that require very sensitive power-supply rails.

This regulator offers both current limit and thermal protection. The operating ambient temperature range of the device is -40°C to +125°C.

图 7-2 shows a typical application circuit for this device.

图 7-2. Typical Application Circuit

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_041.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_038.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_009.png)

## 7.2.1 Design Requirements

For this design example, use the parameters listed in 表 7-1 as the input parameters.

表 7-1. Design Parameters

| PARAMETER | DESIGN REQUIREMENT |
| - | - |
| Input voltage | 12 V |
| Output voltage | 3.3 V |
| Output current | 50 mA |

## 7.2.2 Detailed Design Procedure

For this design example, the 3.3-V, fixed-version TLV76133 is selected and is powered by a standard 12-V input supply. The dropout voltage (VDO) is kept within the TLV761 dropout voltage specification for the 3.3-V output voltage option to keep the device in regulation under all load and temperature conditions for this design. A 1.0µF output capacitor is recommended for excellent load transient response. The input capacitor is optional and is used to reduce the input impedance of the circuit and improve the transient response.

As with any regulator, increasing the size of the output capacitor reduces overshoot and undershoot magnitude.

## 7.2.3 Application Curves

图 7-3. IOUT Transient From 0 mA to 100 mA

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_042.png)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.5 A/µs

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_043.png)

图 7-4. IOUT Transient From 1 mA to 1 A

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_044.png)

VIN = 5 V, VOUT = 3.3 V, ramp rate = 0.8 A/µs

图 7-5. IOUT Transient From 250 mA to 850 mA

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_045.png)

VIN = 5 V VOUT = 3.3 V, IOUT = 1 A, VIN ramp rate = 0.6 V/µs

图 7-6. VIN Transient in Dropout From 4 V to 13 V

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_046.png)

[www.ti.com.cn](https://www.ti.com.cn/)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_047.png)

## 7.3 Best Design Practices

Place input and output capacitors as close to the device as possible.

Use a ceramic output capacitor.

Do not exceed the device absolute maximum ratings.

## 7.4 Power Supply Recommendations

Connect a low output impedance power supply directly to the INPUT pin of the device . Inductive impedances between the input supply and the INPUT pin can create significant voltage excursions at the INPUT pin during start-up or load transient events.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_011.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_048.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_049.png)

## 7.5 Layout

## 7.5.1 Layout Guidelines

Place input and output capacitors as close to the device pins as possible. To improve characteristic AC performance such as PSRR, output noise, and transient response, design the board with separate ground planes for VIN and VOUT, with the ground plane connected only at the GND pin of the device. In addition, the ground connection for the output capacitor must be connected directly to the GND pin of the device. Higher value ESR capacitors can degrade PSRR performance.

## 7.5.2 Layout Examples

图 7-9. Layout Example for DCY (SOT-223) Package

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_050.png)

图 7-10. Layout Example for KVU (TO-252) Package

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_051.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_052.png)

## 8 Device and Documentation Support

## 8.1 Device Support

## 8.1.1 Device Nomenclature

## 表 8-1. Available Options

| PRODUCT (1) (2) | DESCRIPTION |
| - | - |
| TLV761 abxxxy | ab is the nominal output voltage, hexadecimal coding is used. · a is used for the unit level of the output voltage. · b is used for the tenth level of the output voltage. For example, use 33 for 3.3V, A0 for 10.0V, C0 for 12.0V, and D0 for 13.0V. xxx is the package designator. y is the package quantity. |

- (1) For the most current package and ordering information, see the Package Option Addendum at the end of this document, or visit the device product folder at www.ti.com.
- (2) The device is available in factory-programmable fixed output voltage increments of 50mV upon request.

## 8.2 Documentation Support

## 8.2.1 Related Documentation

For related documentation see the following:

- [Texas Instruments, TLV1117 Adjustable and Fixed Low-Dropout Voltage Regulator data sheet](https://www.ti.com/lit/pdf/SLVS561)
- [Texas Instruments, LM1117 800-mA Low-Dropout Linear Regulator data sheet](https://www.ti.com/lit/pdf/SNOS412)

## 8.3 接收文档更新通知

要接收文档更新通知，请导航至 ti.com 上的器件产品文件夹。点击通知 进行注册，即可每周接收产品信息更改摘 要。有关更改的详细信息，请查看任何已修订文档中包含的修订历史记录。

## 8.4 支持资源

TI E2E™ 中文支持论坛是工程师的重要参考资料，可直接从专家处获得快速、经过验证的解答和设计帮助。搜索 现有解答或提出自己的问题，获得所需的快速设计帮助。

链接的内容由各个贡献者"按原样"提供。这些内容并不构成 TI 技术规范，并且不一定反映 TI 的观点；请参阅 TI 的使用条款。

## 8.5 Trademarks

TI E2E™ is a trademark of Texas Instruments.

所有商标均为其各自所有者的财产。

## 8.6 静电放电警告

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_053.png)

## 8.7 术语表

TI 术语表 本术语表列出并解释了术语、首字母缩略词和定义。

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_011.png)

静电放电 (ESD) 会损坏这个集成电路。德州仪器 (TI) 建议通过适当的预防措施处理所有集成电路。如果不遵守正确的处理 和安装程序，可能会损坏集成电路。

ESD 的损坏小至导致微小的性能降级，大至整个器件故障。精密的集成电路可能更容易受到损坏，这是因为非常细微的参 数更改都可能会导致器件与其发布的规格不相符。

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_009.png)

## 9 Revision History

## 注：以前版本的页码可能与当前版本的页码不同

| Changes from Revision C (April 2024) to Revision D (May 2025) | Page |
| - | - |
| · 将 KVU 状态从预发布更改为量产数据 ...............................................................................................................1 · |  |
| 将最大输入电压范围 (VIN) 从 16V 改为 18V ......................................................................................................1 |  |
| · 更改了特性中的输出精度要点.............................................................................................................................1 |  |
| · Added Application Curves section....................................................................................................................16 |  |
| · Changed Available Options table..................................................................................................................... | 19 |
| Changes from Revision B (February 2023) to Revision C (April 2024) | Page |
| · 向文档中添加了 KVU (TO-252) 封装作为预告信息 ............................................................................................1 |  |
| · Added KVU package information to Pin Configuration and Functions section...................................................3 |  |
| · Increased absolute maximum ratings to 20V for Input pin................................................................................. | 4 |
| · Added thermal numbers for KVU (TO-252) package......................................................................................... | 5 |
| · Changed output voltage value from 5 V to 3.3 V in Design Parameters table................................................. | 16 |
| · Added Layout Example for KVU (TO-252) Package image to Layout Examples section................................ | 18 |

## 10 Mechanical, Packaging, and Orderable Information

The following pages include mechanical, packaging, and orderable information. This information is the most current data available for the designated devices. This data is subject to change without notice and revision of this document. For browser-based versions of this data sheet, refer to the left-hand navigation.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_054.png)

www.ti.com

## PACKAGING INFORMATION

| Orderable part number | Status (1) | Material type (2) | Package &#124; Pins | Package qty &#124; Carrier | RoHS (3) | Lead finish/ Ball material (4) | MSL rating/ Peak reflow (5) | Op temp (°C) | Part marking (6) |
| - | - | - | - | - | - | - | - | - | - |
| PTLV76118DCYR | Obsolete | Preproduction | SOT-223 (DCY) &#124; 4 | - | - | Call TI | Call TI | -40 to 125 |  |
| TLV76112DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76112C |
| TLV76112DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76112C |
| TLV76118DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76118C |
| TLV76118DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76118C |
| TLV76125DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76125C |
| TLV76125DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76125C |
| TLV76130DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76130C |
| TLV76130DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76130C |
| TLV76133DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76133C |
| TLV76133DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76133C |
| TLV76133KVUR | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76133 |
| TLV76133KVUR.A | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76133 |
| TLV76136DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76136C |
| TLV76136DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76136C |
| TLV76150DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76150C |
| TLV76150DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76150C |
| TLV76150KVUR | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76150 |
| TLV76150KVUR.A | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV76150 |
| TLV76180DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76180C |
| TLV76180DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 76180C |
| TLV761C0DCYR | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 761C0C |
| TLV761C0DCYR.A | Active | Production | SOT-223 (DCY) &#124; 4 | 2500 &#124; LARGE T&R | Yes | SN | Level-2-260C-1 YEAR | -40 to 125 | 761C0C |
| TLV761C0KVUR | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV761C0 |
| TLV761C0KVUR.A | Active | Production | TO-252 (KVU) &#124; 3 | 2500 &#124; LARGE T&R | Yes | SN | Level-3-260C-168 HR | -40 to 125 | TLV761C0 |

(1) Status: For more details on status, see our product life cycle.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_054.png)

INSTRUMENTS

www.ti.com

## PACKAGE OPTION ADDENDUM

6-Nov-2025

- (2) Material type: When designated, preproduction parts are prototypes/experimental devices, and are not yet approved or released for full production. Testing and final process, including without limitation quality assurance, reliability performance testing, and/or process qualification, may not yet be complete, and this item is subject to further changes or possible discontinuation. If available for ordering, purchases will be subject to an additional waiver at checkout, and are intended for early internal evaluation purposes only. These items are sold without warranties of any kind.
- (3) RoHS values: Yes, No, RoHS Exempt. See the TI RoHS Statement for additional information and value definition.
- (4) Lead finish/Ball material: Parts may have multiple material finish options. Finish options are separated by a vertical ruled line. Lead finish/Ball material values may wrap to two lines if the finish value exceeds the maximum column width.
- (5) MSL rating/Peak reflow: The moisture sensitivity level ratings and peak solder (reflow) temperatures. In the event that a part has multiple moisture sensitivity ratings, only the lowest level per JEDEC standards is shown. Refer to the shipping label for the actual reflow temperature that will be used to mount the part to the printed circuit board.
- (6) Part marking: There may be an additional marking, which relates to the logo, the lot trace code information, or the environmental category of the part.

Multiple part markings will be inside parentheses. Only one part marking contained in parentheses and separated by a "~" will appear on a part. If a line is indented then it is a continuation of the previous line and the two combined represent the entire part marking for that device.

Important Information and Disclaimer:The information provided on this page represents TI's knowledge and belief as of the date that it is provided. TI bases its knowledge and belief on information provided by third parties, and makes no representation or warranty as to the accuracy of such information. Efforts are underway to better integrate information from third parties. TI has taken and continues to take reasonable steps to provide representative and accurate information but may not have conducted destructive testing or chemical analysis on incoming materials and chemicals. TI and TI suppliers consider certain information to be proprietary, and thus CAS numbers and other limited information may not be available for release.

In no event shall TI's liability arising out of such information exceed the total purchase price of the TI part(s) at issue in this document sold by TI to Customer on an annual basis.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_055.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

27-May-2025

## TAPE AND REEL INFORMATION

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_056.png)

## QUADRANT ASSIGNMENTS FOR PIN 1 ORIENTATION IN TAPE

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_057.png)

| Device | Package Type | Package Drawing | Pins | SPQ | Reel Diameter (mm) | Reel Width W1 (mm) | A0 (mm) | B0 (mm) | K0 (mm) | P1 (mm) | W (mm) | Pin1 Quadrant |
| - | - | - | - | - | - | - | - | - | - | - | - | - |
| TLV76112DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76118DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76125DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76130DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76133DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76133KVUR | TO-252 | KVU | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| TLV76136DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76150DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV76150KVUR | TO-252 | KVU | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |
| TLV76180DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV761C0DCYR | SOT-223 | DCY | 4 | 2500 | 330.0 | 12.4 | 7.05 | 7.4 | 1.9 | 8.0 | 12.0 | Q3 |
| TLV761C0KVUR | TO-252 | KVU | 3 | 2500 | 330.0 | 16.4 | 6.9 | 10.5 | 2.7 | 8.0 | 16.0 | Q2 |

## *All dimensions are nominal

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_058.png)

ÎNSTRUMENTS

www.ti.com

## PACKAGE MATERIALS INFORMATION

27-May-2025

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_059.png)

*All dimensions are nominal

| Device | Package Type | Package Drawing | Pins | SPQ | Length (mm) | Width (mm) | Height (mm) |
| - | - | - | - | - | - | - | - |
| TLV76112DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76118DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76125DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76130DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76133DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76133KVUR | TO-252 | KVU | 3 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76136DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76150DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76150KVUR | TO-252 | KVU | 3 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV76180DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV761C0DCYR | SOT-223 | DCY | 4 | 2500 | 340.0 | 340.0 | 38.0 |
| TLV761C0KVUR | TO-252 | KVU | 3 | 2500 | 340.0 | 340.0 | 38.0 |

TRANSISTOR OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_060.png)

Images above are just a representation of the package family, actual package may vary. Refer to the product data sheet for package details.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_061.png)

INSTRUMENTS

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_062.png)

4

## PACKAGE OUTLINE

## TO-252 - 2.52 mm max height

SCALE 1.50

TO-252

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_063.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Shape may vary per different assembly sites.
4. Reference JEDEC registration TO-252.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_064.png)

## TO-252 - 2.52 mm max height

TO-252

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_065.png)

NOTES: (continued)

5. This package is designed to be soldered to a thermal pad on the board. For more information, see Texas Instruments literature numbers SLMA002(www.ti.com/lit/slm002) and SLMA004 (www.ti.com/lit/slma004).
6. Vias are optional depending on application, refer to device data sheet. It is recommended that vias under paste be filled, plugged or tented.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_066.png)

## TO-252 - 2.52 mm max height

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_067.png)

NOTES: (continued)

7. Laser cutting apertures with trapezoidal walls and rounded corners may offer better paste release. IPC-7525 may have alternate design recommendations.

8. Board assembly site may have different recommendations for stencil design.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_064.png)

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_068.png)

SCALE 2. 0

## SOT-223 - 1.8 mm max height

PLASTIC SMALL OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_069.png)

## NOTES:

1. All linear dimensions are in millimeters. Any dimensions in parenthesis are for reference only. Dimensioning and tolerancing per ASME Y14.5M.
2. This drawing is subject to change without notice.
3. Reference JEDEC TO-261.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_070.png)

PLASTIC SMALL OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_071.png)

NOTES: (continued)

4. Publication IPC-7351 may have alternate designs.
5. Solder mask tolerances between and around signal pads can vary based on board fabrication site.

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_066.png)

## SOT-223 - 1.8 mm max height

PLASTIC SMALL OUTLINE

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_072.png)

SOLDER PASTE EXAMPLE BASED ON 0.125 mm THICK STENCIL SCALE:8X

4214843/C 05/2026

![Image](TLV761%20Datasheet%20%28TI%20ZHCSKS3D,%20Chinese%29_files/img_066.png)

## 重要通知和免责声明

TI"按原样"提供技术和可靠性数据（包括数据表）、设计资源（包括参考设计）、应用或其他设计建议、网络工具、安全信息和其他资源，不 保证没有瑕疵且不做出任何明示或暗示的担保，包括但不限于对适销性、与某特定用途的适用性或不侵犯任何第三方知识产权的暗示担保。

这些资源可供使用 TI 产品进行设计的熟练开发人员使用。您将自行承担以下全部责任：(1) 针对您的应用选择合适的 TI 产品，(2) 设计、验 证并测试您的应用，(3) 确保您的应用满足相应标准以及任何其他安全、安保法规或其他要求。

这些资源如有变更，恕不另行通知。TI 授权您仅可将这些资源用于研发本资源所述的 TI 产品的相关应用。严禁以其他方式对这些资源进行复 制或展示。您无权使用任何其他 TI 知识产权或任何第三方知识产权。对于因您对这些资源的使用而对 TI 及其代表造成的任何索赔、损害、 成本、损失和债务，您将全额赔偿，TI 对此概不负责。

TI 提供的产品受 TI 销售条款)、TI 通用质量指南 或 ti.com 上其他适用条款或 TI 产品随附的其他适用条款的约束。TI 提供这些资源并不会扩 展或以其他方式更改 TI 针对 TI 产品发布的适用的担保或担保免责声明。 除非德州仪器 (TI) 明确将某产品指定为定制产品或客户特定产品， 否则其产品均为按确定价格收入目录的标准通用器件。

TI 反对并拒绝您可能提出的任何其他或不同的条款。

IMPORTANT NOTICE

版权所有 © 2026，德州仪器 (TI) 公司

最后更新日期：2025 年 10 月
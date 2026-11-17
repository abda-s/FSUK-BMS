<!-- Converted from PC817 Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](PC817%20Datasheet_files/img_001.png)

## ● 特点(Features):

- 1.电流转换比(CTR: 最小 50% 工作条件 IF=5mA, VCE =5V)

Current conversion ratio (Min 100% Working condition IF=5mA, VCE=5V )

2. 绝缘电压：(VISO=5,000Vrms) Insulation Voltage = 5,000Vrms
3. 响应时间 (tr: TYP. 6μs；tf: TYP. 5μs)工作条件 VCE=2V, IC=2mA, RL=100 Ω) Response Time (tr: TYP. 6μs；tf: TYP. 5μs)working condition VCE=2V, IC=2mA, RL=100 Ω)
4. ESD：HBM8000V&amp;MM2000V

## ● 说明 (Instructions)

1. 系列光耦合器的组成是：由一个GaAs 的发射管和一个 NPN的晶体管组成 PC 817
2. photocoupler consist of one piece of GaAs emitter and one piece of NPN transistor PC 817
2. 的引脚中心距是2.54mm Pin pitch of PC 817 is 2.54mm PC 817

## ● 应用范围 (Application Range)

- 1.开关电源.Switching power supply
- 2.电表.Ammeter
- 3.电脑. Computer
- 4.器具的应用, 测量机. Instrumental application, measurement machine
- 5.贮存器, 复印机, 自动售货机. Imbursement equipments, duplicating machine, automat
- 6.家用电器, 如风扇等. Family-use electric equipments, such as fans
- 7.信号传输系统. Signal transforming systems

## · Block Diagram and Package 框架结构

![Image](PC817%20Datasheet_files/img_002.png)

## 包装标记和订购信息

| 规格型号 | 规格型号 | 丝印情况 | 包装(PCS) |
| - | - | - | - |
| PC817X | DIP-4/SMD-4(SMD-4P) | PC817X | 2000 |

- ●The "x" in the printed word represents the product segment: A、B、C、D or others

印字中的"x"代表产品CTR分档：A、B、C、D等

![Image](PC817%20Datasheet_files/img_003.png)

![Image](PC817%20Datasheet_files/img_004.png)

![Image](PC817%20Datasheet_files/img_001.png)

## ● 最大绝对额定值 (常温=25℃) Max Absolute rated Value (Normal Temperature=25℃)

| 参数 Parameter | 参数 Parameter | 符号 Symbol | 额定值 Rated Value | 单位 Unit |
| - | - | - | - | - |
| 输入 Inout | 顺向电流 Forward Current | IF | 50 | mA |
| 输入 Inout | 逆向电压 Reverse Voltage | VR | 6 | V |
| 输入 Inout | 功消耗率 Consume Power | P | 70 | mW |
| 输出 Output | 集极与射极电压 Collector and emitter Voltage | VCEO | 35 | V |
| 输出 Output | 射极与集极电压 Emitter and collector Voltage | VECO | 6 | V |
| 输出 Output | 集极电流Collector Current | IC | 50 | mA |
| 输出 Output | 消耗功率Consume Power | PC | 150 | mW |
| 总功率消耗 Total Consume Power | 总功率消耗 Total Consume Power | Ptot | 200 | mW |
| *1 绝缘电压 | Insulation Voltage | Viso | 5,000 | Vrms |
| 最大绝缘电压 Max Insulation Voltage | 最大绝缘电压 Max Insulation Voltage | VIOTM | 6,000 | V |
| 额定脉冲绝缘电压 Rated Impulse Insulation Voltage | 额定脉冲绝缘电压 Rated Impulse Insulation Voltage | VIORM | 630 | V |
| 工作温度 Working Temperature | 工作温度 Working Temperature | Topr | -55 to + 110 | ℃ |
| 存贮温度 Deposit Temperature | 存贮温度 Deposit Temperature | Tstg | -55 to + 125 | ℃ |
| *2 焊锡温度 Soldering Temperature | *2 焊锡温度 Soldering Temperature | Tsol | 260 | ℃ |

- *1. 交流测试, 时间1分钟，湿度. =40~60% AC Test, 1 minute, humidity = 40~60% 如下是绝缘测试的方法. Insulation test method as below:
- (1) 将产品的两端短路。 Short circuit both terminals of photocoupler
- (2) 测试绝缘电压时无电流通过。No Current when testing insulation voltage
- (3) 测试时加正弦波形电压。Adding sine wave voltage when testing
- *2. 锡焊时间为10秒 soldering time is 10 seconds

## ● 光电特性(常温=25℃) Opto-electronic Characteristics

| 参数 Parameter | 参数 Parameter | 符号 Symbol | 条件 Condition | 最小 Min | 中.Mid ium | 最 大 Max | 单位 Unit |
| - | - | - | - | - | - | - | - |
| 输入 Input | 顺向电压Forward Current | VF | IF=20mA | --- | 1.20 | 1.40 | V |
| 输入 Input | 逆向电流Reverse Voltage | IR | VR=5V | --- | --- | 5 | uA |
| 输入 Input | 集极电容Collector capacitance | Ct | V=0, f=1MHz | --- | 30 | 250 | pF |
| 输出 Output | 集极至射极电流 Collector to emitter Current | ICEO | VCE=70V, IF=0mA | --- | --- | 150 | nA |
| 输出 Output | 集极与射极衰减电压 Collector and Emitter attenuation Voltage | BVCEO | IC=0.1mA IF=0mA | 70 | --- | --- | V |
| 输出 Output | 射极与集极衰减电压 Emitter and Collector attenuation Voltage | BVECO | IE=10μA IF=0mA | 6 | --- | --- | V |

![Image](PC817%20Datasheet_files/img_005.png)

| 传输特性 Transforming Characteristics | *1 电流转换比 Current conversion ratio | CTR | IF=5mA VCE=5V | 50 | --- | 600 | % |
| - | - | - | - | - | - | - | - |
| 传输特性 Transforming Characteristics | 集极与射极饱和电压Collector and Emitter Saturation Voltage | VCE(sat) | IF=20mA IC= 1mA | --- | 0.1 | 0.2 | V |
| 传输特性 Transforming Characteristics | 绝缘阻抗 Insulation Impedance | Riso | DC500V 40~60%R.H. | 5×10 10 | 1×10 11 | --- | Ω |
| 传输特性 Transforming Characteristics | 电容量 capacotance | Cf | V=0, f=1MHz | --- | 0.6 | 1 | pF |
| 传输特性 Transforming Characteristics | 转换频率Transforming Frequency | fc | VCE=5V, IC=2mA RL=100Ω, -3dB | --- | 80 | --- | kHz |
| 传输特性 Transforming Characteristics | 上升时间 Rise time | tr | VCE=2V, IC=2mA | --- | 6 | 18 | μs |
| 传输特性 Transforming Characteristics | 下降时间 Descend Time | tf | RL=100Ω | --- | 5 | 18 | μs |

-  电流转换比Current Conversion Ratio = IC / IF × 100%

## ● 电流转换比的等级分类 Grades of Current conversion ratio

说明 : 工作条件: IF=5mA, VCE=5V, Ta=25℃.

| 等级标示 Grade Sign | 最小.Min (%) | 最大.Max (%) |
| - | - | - |
| A | 100 | 160 |
| B | 130 | 260 |
| C | 200 | 400 |
| D | 300 | 600 |
| A or B or C or D | 50 | 600 |

Note: Working condition: IF=5mA, VCE=5V, Ta=25℃.

![Image](PC817%20Datasheet_files/img_001.png)

## RATING AND CHARACTERISTIC CURVES (PC817)

Fig.1 Forword Current vs. Ambient Temperatute

![Image](PC817%20Datasheet_files/img_006.png)

Fig.3 Collector-emitter Saturation Voltage vs. Forward Current

![Image](PC817%20Datasheet_files/img_007.png)

Fig.5 Current Transfer Ratio vs. Forward Current

![Image](PC817%20Datasheet_files/img_008.png)

Fig.2 Collector Power Dissiption vs. Ambient Temperature

![Image](PC817%20Datasheet_files/img_009.png)

Fig.4 Forward Current vs. Forward Voltage

![Image](PC817%20Datasheet_files/img_010.png)

Fig.6 Collector Current vs. Collector-emitter Voltage

![Image](PC817%20Datasheet_files/img_011.png)

![Image](PC817%20Datasheet_files/img_012.png)

## RATING AND CHARACTERISTIC CURVES (PC817)

Fig.7 Relative Current Transfer Ratio vs. Ambient Temperature

![Image](PC817%20Datasheet_files/img_013.png)

Fig.9 Collector Dark Current vs. Ambient Temperature

6

Fig.11 Frequency Response

![Image](PC817%20Datasheet_files/img_014.png)

![Image](PC817%20Datasheet_files/img_015.png)

Fig.8 Collector-emitter Saturation Voltage vs. Ambient Temperature

![Image](PC817%20Datasheet_files/img_016.png)

Fig.10 Response Time vs. Load Resistance

![Image](PC817%20Datasheet_files/img_017.png)

Test Circuit for Response Time

![Image](PC817%20Datasheet_files/img_018.png)

![Image](PC817%20Datasheet_files/img_019.png)

![Image](PC817%20Datasheet_files/img_005.png)

## Outline Dimensions 外形尺寸

Unit: mm (inch)

![Image](PC817%20Datasheet_files/img_020.png)

4-pin DIP

![Image](PC817%20Datasheet_files/img_021.png)

4-pin SMD(SMD-4P)

![Image](PC817%20Datasheet_files/img_022.png)

## Attention

- ■ Any and all HUA XUAN YANG ELECTRONICS products described or contained herein do not have specifications that can handle applications that require extremely high levels of reliability, such as life-support systems, aircraft's control systems, or other applications whose failure can be reasonably expected to result in serious physical and/or material damage. Consult with your HUA XUAN YANG ELECTRONICS representative nearest you before using any HUA XUAN YANG ELECTRONICS products described or contained herein in such applications.
- ■ HUA XUAN YANG ELECTRONICS assumes no responsibility for equipment failures that result from using products at values that exceed, even momentarily, rated values (such as maximum ratings, operating condition ranges, or other parameters) listed in products specifications of any and all HUA XUAN YANG ELECTRONICS products described or contained herein.
- ■ Specifications of any and all HUA XUAN YANG ELECTRONICS products described or contained herein stipulate the performance, characteristics, and functions of the described products in the independent state, and are not guarantees of the performance, characteristics, and functions of the described products as mounted in the customer's products or equipment. To verify symptoms and states that cannot be evaluated in an independent device, the customer should always evaluate and test devices mounted in the customer's products or equipment.
- ■ HUA XUAN YANG ELECTRONICS CO.,LTD. strives to supply high-quality high-reliability products. However, any and all semiconductor

products fail with some probability. It is possible that these probabilistic failures could give rise to accidents or events that could endanger human lives, that could give rise to smoke or fire, or that could cause damage to other property. When designing equipment, adopt safety measures so that these kinds of accidents or events cannot occur. Such measures include but are not limited to protective circuits and error prevention circuits for safe design, redundant design, and structural design.

- ■ In the event that any or all HUA XUAN YANG ELECTRONICS products(including technical data, services) described or contained herein are controlled under any of applicable local export control laws and regulations, such products must not be exported without obtaining the export license from the authorities concerned in accordance with the above law.
- ■ No part of this publication may be reproduced or transmitted in any form or by any means, electronic or mechanical, including photocopying and recording, or any information storage or retrieval system, or otherwise, without the prior written permission of HUA XUAN YANG ELECTRONICS CO.,LTD.
- ■ Information (including circuit diagrams and circuit parameters) herein is for example only ; it is not guaranteed for volume production. HUA XUAN YANG ELECTRONICS believes information herein is accurate and reliable, but no guarantees are made or implied regarding its use or any infringements of intellectual property rights or other rights of third parties.
- ■ Any and all information described or contained herein are subject to change without notice due to product/technology improvement, etc. When designing equipment, refer to the "Delivery Specification" for the HUA XUAN YANG ELECTRONICS product that you intend to use.
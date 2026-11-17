<!-- Converted from MIC39100 Datasheet (Microchip DS20005834A).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_001.png)

MICROCHIP

## MIC39100/1/2

## 1A, Low Voltage, Low Dropout Regulator with Reversed-Battery Protection

## General Description

The MIC39100, MIC39101, and MIC39102 are 1A low dropout linear voltage regulators that provide low voltage, high current output from an extremely small package. The MIC39100/1/2 offers extremely low dropout (typically 410 mV at 1A) and low ground current (typically 11 mA at 1A).

The MIC39100 is a Þxed output regulator offered in the SOT-223 package. The MIC39101 and MIC39102 are Þxed and adjustable regulators, respectively, in a thermally enhanced 8-lead SOIC package.

The MIC39100/1/2 is ideal for PC add-in cards that need to convert from standard 5V to 3.3V, 3.3V to 2.5V, or 2.5V to 1.8V. A guaranteed maximum dropout voltage of 630 mV over all operating conditions allows the MIC39100/1/2 to provide 2.5V from a supply as low as 3.13V and 1.8V from a supply as low as 2.43V.

The MIC39100/1/2 is fully protected with overcurrent limiting, thermal-shutdown, and reverse-battery protection. Fixed voltages of 5.0V, 3.3V, 2.5V, and 1.8V are available on MIC39100/1 with adjustable output voltages to 1.24V on MIC39102.

## Features

- Fixed and Adjustable Output Voltages to 1.24V
- 410 mV Typical Dropout at 1A Load
- Best Recommended for 3.0V to 2.5V Conversion
- Best Recommended for 2.5V to 1.8V Conversion
- 1A Minimum Guaranteed Output Current
- 1% Initial Accuracy
- Low Ground Current
- Current-Limiting and Thermal-Shutdown Protection
- Reversed-Battery and Reversed-Leakage Protection
- Fast Transient Response
- Low ProÞle SOT-223 Package
- Power SO-8 Package

## Applications

- LDO Linear Regulator for PC Add-In Cards
- High-EfÞciency Linear Power Supplies
- SMPS Post Regulator
- Multimedia and PC Processor Supplies
- Battery Chargers
- Low Voltage Microcontrollers and Digital Logic

## Package Types

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_002.png)

## Typical Application Circuits

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_003.png)

## Functional Block Diagrams

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_004.png)

## MIC39100/1/2

## 1.0 ELECTRICAL CHARACTERISTICS

## Absolute Maximum Ratings †

| Supply Voltage (VIN).................................................................................................................................... -20V to +20V |
| - |
| Enable Voltage (VEN) ................................................................................................................................................+20V |
| ESD Rating ............................................................................................................................................................ Note 1 |
| Maximum Power Dissipation (PD(MAX)) .................................................................................................................. Note 2 |
| Operating Ratings ‡ |
| Supply Voltage (VIN).................................................................................................................................+2.25V to +16V |
| Enable Voltage (VEN) ................................................................................................................................................+16V |

† Notice: Stresses above those listed under "Absolute Maximum Ratings" may cause permanent damage to the device. This is a stress rating only and functional operation of the device at those or any other conditions above those indicated in the operational sections of this specification is not intended. Exposure to maximum rating conditions for extended periods may affect device reliability.

‡ Notice: The device is not guaranteed to function outside its operating ratings.

- Note 1: Devices are ESD sensitive. Handling precautions are recommended. Human body model, 1.5 kΩ in series with 100 pF.
- 2: PD(MAX) = (TJ(MAX) - TA) ÷ θJA, where θJA depends upon the printed circuit layout (see Application Information).

## TABLE 1-1: ELECTRICAL CHARACTERISTICS

Electrical Characteristics: VIN = VOUT + 1V; VEN = 2.25V; TJ = +25°C, bold values indicate -40°C ≤ TJ ≤ +125°C, unless noted. Note 1

| Parameter | Symbol | Min. | Typ. | Max. | Units | Conditions |
| - | - | - | - | - | - | - |
| Output Voltage | VOUT | -1 | - | 1 | % | IOUT = 10 mA |
| Output Voltage | VOUT | -2 | - | 2 | % | 10 mA ≤ IOUT ≤ 1A, VOUT +1V ≤ VIN ≤ 8V |
| Line Regulation | - | - | 0.06 | 0.5 | % | IOUT = 10 mA, VOUT + 1V ≤ VIN ≤ 16V |
| Load Regulation | - | - | 0.2 | 1 | % | VIN = VOUT + 1V, 10 mA ≤ IOUT ≤ 1A |
| Output Voltage Temperature Coefficient | ∆VOUT/ ∆T | - | 40 | 100 | ppm/°C | Note 2 |
| Dropout Voltage, Note 3 | VDO | - | 140 | 200 | mV | IOUT = 100 mA, ∆VOUT = -1% |
| Dropout Voltage, Note 3 | VDO | - | 140 | 250 | mV | IOUT = 100 mA, ∆VOUT = -1% |
| Dropout Voltage, Note 3 | VDO | - | 275 | - | mV | IOUT = 500 mA, ∆VOUT = -1% |
| Dropout Voltage, Note 3 | VDO | - | 300 | 500 | mV | IOUT = 750 mA, ∆VOUT = -1% |
| Dropout Voltage, Note 3 | VDO | - | 410 | 550 | mV | IOUT = 1A, ∆VOUT = -1% |
| Dropout Voltage, Note 3 | VDO | - | 410 | 630 | mV | IOUT = 1A, ∆VOUT = -1% |
| Ground Current, Note 4 | IGND | - | 400 | - | µA | IOUT = 100 mA, VIN = VOUT + 1V |
| Ground Current, Note 4 | IGND | - | 4 | - | mA | IOUT = 500 mA, VIN = VOUT + 1V |
| Ground Current, Note 4 | IGND | - | 6.5 | - | mA | IOUT = 750 mA, VIN = VOUT + 1V |
| Ground Current, Note 4 | IGND | - | 11 | 20 | mA | IOUT = 1A, VIN = VOUT + 1V |
| Current Limit | IOUT(LIM) | - | 1.8 | 2.5 | A | VOUT = 0V, VIN = VOUT + 1V |
| Enable Input | Enable Input | Enable Input | Enable Input | Enable Input | Enable Input | Enable Input |
| Enable Input Voltage | VEN | - | - | 0.8 | V | Logic LOW (Off) |
| Enable Input Voltage | VEN | 2.25 | - | - | V | Logic HIGH (On) |

## TABLE 1-1: ELECTRICAL CHARACTERISTICS (CONTINUED)

Electrical Characteristics: VIN = VOUT + 1V; VEN = 2.25V; TJ = +25°C, bold values indicate -40°C ≤ TJ ≤ +125°C,

unless noted. Note 1

| Parameter | Symbol | Min. | Typ. | Max. | Units | Conditions |
| - | - | - | - | - | - | - |
| Enable Input Current | IEN | 1 | 15 | 30 | µA | VEN = 2.25V |
| Enable Input Current | IEN | - | - | 75 | µA | VEN = 2.25V |
| Enable Input Current | IEN | - | - | 2 | µA | VEN = 0.8V |
| Enable Input Current | IEN | - | - | 4 | µA | VEN = 0.8V |
| Flag Output | Flag Output | Flag Output | Flag Output | Flag Output | Flag Output | Flag Output |
| Output Leakage Voltage | IFLG(LEAK) | - | 0.01 | 1 | µA | VOH = 16V |
| Output Leakage Voltage | IFLG(LEAK) | - | 0.01 | 2 | µA | VOH = 16V |
| Output Low Voltage | VFLG(DO) | - | 210 | 300 | mV | VIN = 2.250V, IOL = 250 µA, Note 5 |
| Output Low Voltage | VFLG(DO) | - | 210 | 400 | mV | VIN = 2.250V, IOL = 250 µA, Note 5 |
| Low Threshold | VFLG | 93 | - | - | % | % of VOUT |
| High Threshold | VFLG | - | - | 99.2 | % | % of VOUT |
| Hysteresis | VFLG | - | 1 | - | % | - |
| MIC39102 Only | MIC39102 Only | MIC39102 Only | MIC39102 Only | MIC39102 Only | MIC39102 Only | MIC39102 Only |
| Reference Voltage | - | 1.228 | 1.240 | 1.252 | V | IOUT = 10 mA |
| Reference Voltage | - | 1.215 | 1.240 | 1.265 | V | IOUT = 10 mA |
| Reference Voltage | - | 1.203 | - | 1.277 | V | Note 6 |
| Adjust Pin Bias Current | - | - | 40 | 80 | nA | - |
| Adjust Pin Bias Current | - | - | 40 | 120 | nA | - |
| Reference Voltage Temperature Coefficient | - | - | 20 | - | ppm/°C | - |
| Adjust Pin Bias Current Temperature Coefficient | - | - | 0.1 | - | nA/°C | - |

- Note 1: Specification for packaged product only.
- 2: Output voltage temperature coefficient is ∆VOUT(WORST CASE) ÷ (TJ(MAX) - TJ(MIN)), where TJ(MAX) = +125°C and TJ(MIN) = -40°C.
- 3: VDO = VIN - VOUT when VOUT decreases to 99% of its nominal output voltage with VIN = VOUT + 1V. For output voltages below 2.25V, dropout voltage is the input-to-output voltage differential with the minimum input voltage being 2.25V. Minimum input operating voltage is 2.25V.
- 4: IGND is the quiescent current (IIN = IGND + IOUT).
- 5: For a 2.5V device, VIN = 2.250V (device is in dropout).
- 6: VREF ≤ VOUT ≤ (VIN - 1V), 2.25V ≤ VIN ≤ 16V, 10 mA ≤ IL ≤ 1A, TJ = TMAX.

## TEMPERATURE SPECIFICATIONS (Note 1)

| Parameters | Sym. | Min. | Typ. | Max. | Units | Conditions |
| - | - | - | - | - | - | - |
| Temperature Ranges |  |  |  |  |  |  |
| Junction Operating Temperature Range | TJ | -40 | - | +125 | °C | - |
| Storage Temperature Range | TS | -65 | - | +150 | °C | - |
| Lead Temperature | - | - | - | +260 | °C | Soldering, 5s |
| Package Thermal Resistances |  |  |  |  |  |  |
| Thermal Resistance SOT-223 | θJC | - | 15 | - | °C/W | - |
| Thermal Resistance SOIC-8 | θJC | - | 20 | - | °C/W | - |

Note 1: The maximum allowable power dissipation is a function of ambient temperature, the maximum allowable junction temperature and the thermal resistance from junction to air (i.e., TA, TJ, θJA). Exceeding the maximum allowable power dissipation will cause the device operating junction temperature to exceed the maximum +125°C rating. Sustained junction temperatures above +125°C can impact the device reliability.

## 2.0 TYPICAL PERFORMANCE CURVES

Note: The graphs and tables provided following this note are a statistical summary based on a limited number of samples and are provided for informational purposes only. The performance characteristics listed herein are not tested or guaranteed. In some graphs or tables, the data presented may be outside the specified operating range (e.g., outside specified power supply range) and therefore outside the warranted range.

FIGURE 2-1: Power Supply Rejection Ratio.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_005.png)

FIGURE 2-2: Power Supply Rejection Ratio.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_006.png)

FIGURE 2-3: Power Supply Rejection Ratio.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_007.png)

FIGURE 2-4: Power Supply Rejection Ratio.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_008.png)

FIGURE 2-5: Dropout Voltage vs. Output Current.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_009.png)

FIGURE 2-6: Dropout Voltage vs. Temperature.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_010.png)

FIGURE 2-7: Dropout Characteristics (2.5V).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_011.png)

FIGURE 2-8: Dropout Characteristics (3.3V).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_012.png)

FIGURE 2-9: Ground Current vs. Output Current.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_013.png)

FIGURE 2-10: Ground Current vs. Supply Voltage (2.5V).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_014.png)

FIGURE 2-11: Ground Current vs. Supply Voltage (2.5V).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_015.png)

FIGURE 2-12: Ground Current vs. Supply Voltage (3.3V).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_016.png)

FIGURE 2-13: Ground Current vs. Supply Voltage (3.3V).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_017.png)

FIGURE 2-14: Ground Current vs. Temperature.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_018.png)

FIGURE 2-15: Ground Current vs. Temperature.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_019.png)

FIGURE 2-16: Ground Current vs. Temperature.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_020.png)

FIGURE 2-17: Output Voltage vs. Temperature.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_021.png)

FIGURE 2-18: Short-Circuit vs. Temperature.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_022.png)

FIGURE 2-19: Error Flag Voltage vs. Pull-Up Resistor Value.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_023.png)

FIGURE 2-20: Enable Current vs.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_024.png)

Temperature.

FIGURE 2-21: Flag-Low Voltage vs. Temperature.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_025.png)

FIGURE 2-22: Load Transient Response.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_026.png)

FIGURE 2-23: Load Transient Response.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_027.png)

FIGURE 2-24: Line Transient Response.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_028.png)

## 3.0 PIN DESCRIPTIONS

The descriptions of the pins are listed in Table 3-1.

TABLE 3-1: PIN FUNCTION TABLE

| Pin Number MIC39100 | Pin Number MIC39101 | Pin Number MIC39102 | Pin Name | Description |
| - | - | - | - | - |
| - | 1 | 1 | EN | Enable (Input): CMOS-compatible control input. Logic HIGH = enable; logic LOW or OPEN = shutdown. |
| 1 | 2 | 2 | IN | Supply (Input). |
| 3 | 3 | 3 | OUT | Regulator Output. |
| - | 4 | - | FLG | Flag (Output): Open-collector error flag output. Active LOW = output undervoltage. |
| - | - | 4 | ADJ | Adjustable Input: Feedback input. Connect to resistive voltage-divider network. |
| 2, TAB | 5, 6, 7, 8 | 5, 6, 7, 8 | GND | Ground. |

## 4.0 APPLICATION INFORMATION

The MIC39100/1/2 is a high performance, low dropout voltage regulator suitable for moderate to high current voltage regulator applications. Its 630 mV dropout voltage at full load and over temperature makes it especially valuable in battery-powered systems and as high efÞciency noise Þlters in post-regulator applications. Unlike older NPN-pass transistor designs, where the minimum dropout voltage is limited by the base-to-emitter voltage drop and collector-to-emitter saturation voltage, dropout performance of the PNP output of these devices is limited only by the low VCE saturation voltage.

A trade-off for the low dropout voltage is a varying base drive requirement that reduces the drive requirement to only 2% of the load current.

The MIC39100/1/2 regulator is fully protected from damage due to fault conditions. Linear current limiting is provided. Output current during overload conditions is constant. Thermal shutdown disables the device when the die temperature exceeds the maximum safe operating temperature. Transient protection allows device (and load) survival even when the input voltage spikes above and below nominal. The output structure of these regulators allows voltages in excess of the desired output voltage to be applied without reverse current ßow.

FIGURE 4-1: Capacitor Requirements.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_029.png)

## 4.1 Output Capacitor

The MIC39100/1/2 requires an output capacitor to maintain stability and improve transient response. Proper capacitor selection is important to ensure proper operation. The MIC39100/1/2 output capacitor selection is dependent upon the equivalent series resistance (ESR) of the output capacitor to maintain stability. When the output capacitor is 10 µF or greater, the output capacitor should have an ESR less than 2Ω. This will improve transient response as well as promote stability. Ultra-low ESR capacitors (&lt;100 mΩ), such as ceramic-chip capacitors, may promote instability. These very low ESR levels may cause an oscillation and/or underdamped transient response. A low-ESR solid tantalum capacitor works extremely well and provides good transient response and stability over temperature. Aluminum electrolytics can also be used, as long as the ESR of the capacitor is &lt;2Ω.

The value of the output capacitor can be increased without limit. Higher capacitance values help to improve transient response and ripple rejection and reduce output noise.

## 4.2 Input Capacitor

An input capacitor of 1 µF or greater is recommended when the device is more than four inches away from the bulk ac supply capacitance or when the supply is a battery. Small, surface mount, ceramic chip capacitors can be used for bypassing. Larger values will help to improve ripple rejection by bypassing the input to the regulator, further improving the integrity of the output voltage.

## 4.3 Error Flag

The MIC39101 features an error ßag (FLG) that monitors the output voltage and signals an error condition when this voltage drops 5% below its expected value. The error ßag is an open-collector output that pulls low under fault conditions and may sink up to 10 mA. Low output voltage signiÞes a number of possible problems, including an overcurrent fault (the device is in current-limit) or low input voltage. The ßag output is inoperative during overtemperature conditions. A pull-up resistor from FLG to either VIN or VOUT is required for proper operation. For information regarding the minimum and maximum values of pull-up resistance, refer to Figure 2-19.

## 4.4 Enable Input

The MIC39101 and MIC39102 feature an active-HIGH enable input (EN) that allows on/off control of the regulator. Current drain reduces to zero when the device is shutdown, with only microamperes (µA) of leakage current. The EN input has TTL/CMOS-comparable thresholds for simple logic interfacing. EN can be directly tied to VIN and pulled-up to the maximum supply voltage.

## 4.5 Transient Response and 3.3V to 2.5V or 2.5V to 1.8V Conversion

The MIC39100/1/2 has excellent transient response to variations in input voltage and load current. The device has been designed to respond quickly to load current variations and input voltage variations. Large output capacitors are not required to obtain this performance. A standard 10 µF output capacitor, preferably tantalum, is all that is required. Larger values help to improve performance even further.

By virtue of its low dropout voltage, this device does not saturate into dropout as readily as similar NPN-based designs. When converting from 3.3V to 2.5V or 2.5V to 1.8V, the NPN-based regulators are already operating in dropout, with typical dropout requirements of 1.2V or greater. To convert down to 2.5V or 1.8V without operating in dropout, NPN-based regulators require an input voltage of 3.7V at the very least.

The MIC39100 regulator will provide excellent performance with an input as low as 3.0V or 2.5V respectively. This gives the PNP-based regulators a distinct advantage over older, NPN-based linear regulators.

## 4.6 Minimum Load Current

The MIC39100/1/2 regulator is speciÞed between Þnite loads. If the output current is too small, leakage currents dominate and the output voltage rises. A 10 mA minimum load current is necessary for proper regulation.

## 4.7 Adjustable Regulator Design

The MIC39102 allows programming the output voltage anywhere between 1.24V and the 16V maximum operating rating of the family. Two resistors are used. Resistors can be quite large, up to 1 MΩ, because of the very high input impedance and low bias current of the sense comparator: The resistor values are calculated by Equation 4-1:

## EQUATION 4-1:

<!-- formula-not-decoded -->

Where:

VOUT Desired output voltage.

Applications with widely varying load currents may scale the resistors to draw the minimum load current required for proper operation (Figure 4-2).

FIGURE 4-2: Adjustable Regulator with Resistors.

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_030.png)

## EQUATION 4-2:

<!-- formula-not-decoded -->

## 4.8 Power SOIC-8 Thermal Characteristics

One of the secrets of the MIC39101/2's performance is its power SO-8 package. Lower thermal resistance means more output current or higher input voltage for a given package size.

Lower thermal resistance is achieved by joining the four ground leads with the die attach paddle to create a single-piece electrical and thermal conductor. This concept has been used by MOSFET manufacturers for years, proving very reliable and cost effective for the user.

Thermal resistance consists of two main elements, θJC (junction-to-case thermal resistance) and θCA (case-to-ambient thermal resistance, see Figure 4-3). θJC is the resistance from the die to the leads of the package. θCA is the resistance from the leads to the ambient air and it includes θCS (case-to-sink thermal resistance) and θSA (sink-to-ambient thermal resistance).

FIGURE 4-3:

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_031.png)

Thermal Resistance.

Using the power SOIC-8 reduces the θJC dramatically and allows the user to reduce θCA. The total thermal resistance, θJA, (junction-to-ambient thermal resistance) is the limiting factor in calculating the maximum power dissipation capability of the device. Typically, the power SOIC-8 has a θJC of 20°C/W, which is significantly lower than the standard SOIC-8 (typically 75°C/W). θCA is reduced due to the capability of soldering Pins 5 through 8 directly to a ground plane.

## MIC39100/1/2

This significantly reduces the case-to-sink thermal resistance as well as the sink-to-ambient thermal resistance.

Low dropout linear regulators from Microchip are rated to a maximum junction temperature of +125°C. It is important not to exceed this maximum junction temperature during operation of the device. To prevent this maximum junction temperature from being exceeded, the appropriate ground plane heat sink must be used.

Figure 4-4 shows copper area versus power dissipation with each trace corresponding to a different temperature rise above ambient.

FIGURE 4-4: Copper Area vs. Power SOIC Power Dissipation (∆TJA).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_032.png)

From these curves, the minimum area of copper necessary for the part to operate safely can be determined. The maximum allowable temperature rise must be calculated to determine operation along which curve.

For example, the maximum ambient temperature is 50°C, the ∆T is determined as in Equation 4-3:

## EQUATION 4-3:

<!-- formula-not-decoded -->

Where:

∆T TJ(MAX) - TA(MAX)

TJ(MAX) +125°C

TA(MAX) Max. ambient operating temperature Using Figure 4-4, the minimum amount of required copper can be determined based on the required power dissipation. Power dissipation in a linear regulator is calculated as in Equation 4-4:

## EQUATION 4-4:

<!-- formula-not-decoded -->

Using a 2.5V output device and a 3.3V input at an output current of 1A, the power dissipation is calculated as in Equation 4-5:

## EQUATION 4-5:

```
P D 3.3V 2.5V - ( )1A 3.3V + 11 mA × 800 mW 36 mW + 836 mW = = =
```

From Figure 4-4, the minimum amount of copper required to operate this application at a ∆T of 75°C is 160 mm 2 .

## 4.9 Quick Method

Determine the power dissipation requirements for the design along with the maximum ambient temperature at which the device will be operated. Refer to Figure 4-5, which shows safe operating curves for three different ambient temperatures: 25°C, 50°C, and 85°C. From these curves, the minimum amount of copper can be determined by knowing the maximum power dissipation required. If the maximum ambient temperature is 50°C and the power dissipation is as above, 836 mW, the curve in Figure 4-5 shows that the required area of copper is 160 mm 2 .

The θJA of this package is ideally 63°C/W, but it will vary depending upon the availability of copper ground plane to which it is attached.

FIGURE 4-5: Copper Area vs. Power SOIC Power Dissipation (TA).

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_033.png)

## MIC39100/1/2

## 5.0 PACKAGING INFORMATION

## 5.1 Package Marking Information

3-Pin SOT-223* (MIC39100)

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_034.png)

8-Pin SOIC* (MIC39101)

XXXXX

-X.XXX

WNNN

8-Pin SOIC* (MIC39102)

XXX

XXXXXXX

WNNN

Example

39100

2.58103P

Example

39101

-3.3Y

6987

Example

MIC 39102YM

3112

Legend: XX...X Product code or customer-specific information

Y

Year code (last digit of calendar year)

YY Year code (last 2 digits of calendar year)

WW Week code (week of January 1 is week '01')

NNN Alphanumeric traceability code

e

*

Pb-free JEDEC ® designator for Matte Tin (Sn)

This package is Pb-free. The Pb-free JEDEC designator ( ) 3 e

can be found on the outer packaging for this package.

●, ▲, ▼ Pin one index is identified by a dot, delta up, or delta down (triangle mark).

In the event the full Microchip part number cannot be marked on one line, it will be carried over to the next line, thus limiting the number of available characters for customer-specific information. Package may or may not include the corporate logo.

Underbar (\_) and/or Overbar (⎯) symbol may not be to scale.

3

Note:

## 3-Lead SOT-223 Package Outline and Recommended Land Pattern

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_035.png)

## 8-Lead SOIC Package Outline and Recommended Land Pattern

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_036.png)

## APPENDIX A: REVISION HISTORY

## Revision A (August 2017)

- Converted Micrel document MIC39100/1/2 to Microchip data sheet DS20005834A.
- Minor text changes throughout.

## PRODUCT IDENTIFICATION SYSTEM

To order or obtain information, e.g., on pricing or delivery, contact your local Microchip representative or sales office.

PART NO.

Device

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_037.png)

X

XX

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_038.png)

Package Voltage Temperature Media Type

Device:

Voltage:

MIC39100/1/2: 1A, Low Voltage, Low Dropout Regulator

1.8 = 1.8V

2.5 = 2.5V

3.3 = 3.3V

5.0 = 5.0V

&lt;blank&gt;= Adjustable (MIC39102 Only)

Temperature: Y = -40°C to +125°C W = -40°C to +125°C (with high-melting solder exemption)

Package:

M = 8-Lead SOIC

Media Type:

S = 3-Lead SOT-223 (MIC39100 Only)

&lt;blank&gt;= 78/Tube (MIC39100)

&lt;blank&gt;= 95/Tube (MIC39101/2)

TR = 2,500/Reel

## Examples:

a) MIC39100-1.8WS:

1A, Low Voltage, Low Dropout

Regulator, 1.8V,

-40°C to +125°C, 3-Lead SOT-223, 78/Tube

- b) MIC39100-3.3WS-TR: 1A, Low Voltage, Low Dropout

Regulator, 3.3V,

-40°C to +125°C, 3-Lead SOT-223, 2,500/Reel

- c) MIC39101-2.5YM:

1A, Low Voltage, Low Dropout

Regulator, 2.5V,

-40°C to +125°C, 8-Lead

SOIC, 95/Tube

- d) MIC39101-5.0YM-TR: 1A, Low Voltage, Low Dropout

Regulator, 5.0V,

-40°C to +125°C, 8-Lead

SOIC, 2,500/Reel

1A, Low Voltage, Low Dropout Regulator, Adjustable Voltage, -40°C to +125°C, 8-Lead SOIC, 95/Tube

1A, Low Voltage, Low Dropout Regulator, Adjustable Voltage, -40°C to +125°C, 8-Lead SOIC, 2,500/Reel

- e) MIC39102YM:

f) MIC39102YM-TR:

Note 1: Tape and Reel identifier only appears in the catalog part number description. This identifier is used for ordering purposes and is not printed on the device package. Check with your Microchip Sales Office for package availability with the Tape and Reel option.

NOTES:

## Note the following details of the code protection feature on Microchip devices:

- Microchip products meet the specification contained in their particular Microchip Data Sheet.
- Microchip believes that its family of products is one of the most secure families of its kind on the market today, when used in the intended manner and under normal conditions.
- There are dishonest and possibly illegal methods used to breach the code protection feature. All of these methods, to our knowledge, require using the Microchip products in a manner outside the operating specifications contained in Microchip's Data Sheets. Most likely, the person doing so is engaged in theft of intellectual property.
- Microchip is willing to work with the customer who is concerned about the integrity of their code.
- Neither Microchip nor any other semiconductor manufacturer can guarantee the security of their code. Code protection does not mean that we are guaranteeing the product as "unbreakable."

Code protection is constantly evolving. We at Microchip are committed to continuously improving the code protection features of our products. Attempts to break Microchip's code protection feature may be a violation of the Digital Millennium Copyright Act. If such acts allow unauthorized access to your software or other copyrighted work, you may have a right to sue for relief under that Act.

Information contained in this publication regarding device applications and the like is provided only for your convenience and may be superseded by updates. It is your responsibility to ensure that your application meets with your specifications. MICROCHIP MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND WHETHER EXPRESS OR IMPLIED, WRITTEN OR ORAL, STATUTORY OR OTHERWISE, RELATED TO THE INFORMATION, INCLUDING BUT NOT LIMITED TO ITS CONDITION, QUALITY, PERFORMANCE, MERCHANTABILITY OR FITNESS FOR PURPOSE. Microchip disclaims all liability arising from this information and its use. Use of Microchip devices in life support and/or safety applications is entirely at the buyer's risk, and the buyer agrees to defend, indemnify and hold harmless Microchip from any and all damages, claims, suits, or expenses resulting from such use. No licenses are conveyed, implicitly or otherwise, under any Microchip intellectual property rights unless otherwise stated.

Microchip received ISO/TS-16949:2009 certification for its worldwide headquarters, design and wafer fabrication facilities in Chandler and Tempe, Arizona; Gresham, Oregon and design centers in California and India. The Company's quality system processes and procedures are for its PIC ® MCUs and dsPIC ® DSCs, KEELOQ ® code hopping devices, Serial EEPROMs, microperipherals, nonvolatile memory and analog products. In addition, Microchip's quality system for the design and manufacture of development systems is ISO 9001:2000 certified.

## QUALITY MANAGEMENT SYSTEM CERTIFIED BY DNV

== ISO/TS 16949 ==

## Trademarks

The Microchip name and logo, the Microchip logo, AnyRate, AVR, AVR logo, AVR Freaks, BeaconThings, BitCloud, CryptoMemory, CryptoRF, dsPIC, FlashFlex, flexPWR, Heldo, JukeBlox, KEELOQ, KEELOQ logo, Kleer, LANCheck, LINK MD, maXStylus, maXTouch, MediaLB, megaAVR, MOST, MOST logo, MPLAB, OptoLyzer, PIC, picoPower, PICSTART, PIC32 logo, Prochip Designer, QTouch, RightTouch, SAM-BA, SpyNIC, SST, SST Logo, SuperFlash, tinyAVR, UNI/O, and XMEGA are registered trademarks of Microchip Technology Incorporated in the U.S.A. and other countries.

ClockWorks, The Embedded Control Solutions Company, EtherSynch, Hyper Speed Control, HyperLight Load, IntelliMOS, mTouch, Precision Edge, and Quiet-Wire are registered trademarks of Microchip Technology Incorporated in the U.S.A.

Adjacent Key Suppression, AKS, Analog-for-the-Digital Age, Any Capacitor, AnyIn, AnyOut, BodyCom, chipKIT, chipKIT logo, CodeGuard, CryptoAuthentication, CryptoCompanion, CryptoController, dsPICDEM, dsPICDEM.net, Dynamic Average Matching, DAM, ECAN, EtherGREEN, In-Circuit Serial Programming, ICSP, Inter-Chip Connectivity, JitterBlocker, KleerNet, KleerNet logo, Mindi, MiWi, motorBench, MPASM, MPF, MPLAB Certified logo, MPLIB, MPLINK, MultiTRAK, NetDetach, Omniscient Code Generation, PICDEM, PICDEM.net, PICkit, PICtail, PureSilicon, QMatrix, RightTouch logo, REAL ICE, Ripple Blocker, SAM-ICE, Serial Quad I/O, SMART-I.S., SQI, SuperSwitcher, SuperSwitcher II, Total Endurance, TSHARC, USBCheck, VariSense, ViewSpan, WiperLock, Wireless DNA, and ZENA are trademarks of Microchip Technology Incorporated in the U.S.A. and other countries.

SQTP is a service mark of Microchip Technology Incorporated in the U.S.A.

Silicon Storage Technology is a registered trademark of Microchip Technology Inc. in other countries.

GestIC is a registered trademark of Microchip Technology Germany II GmbH &amp; Co. KG, a subsidiary of Microchip Technology Inc., in other countries.

All other trademarks mentioned herein are property of their respective companies.

© 2017, Microchip Technology Incorporated, All Rights Reserved. ISBN: 978-1-5224-2098-9

![Image](MIC39100%20Datasheet%20%28Microchip%20DS20005834A%29_files/img_039.png)

## Worldwide Sales and Service

## ASIA/PACIFIC

Asia Pacific Office Suites 3707-14, 37th Floor Tower 6, The Gateway Harbour City, Kowloon

Hong Kong Tel: 852-2943-5100 Fax: 852-2401-3431

Australia - Sydney Tel: 61-2-9868-6733 Fax: 61-2-9868-6755

China - Beijing Tel: 86-10-8569-7000 Fax: 86-10-8528-2104

China - Chengdu Tel: 86-28-8665-5511 Fax: 86-28-8665-7889

China - Chongqing Tel: 86-23-8980-9588 Fax: 86-23-8980-9500

China - Dongguan Tel: 86-769-8702-9880

China - Guangzhou Tel: 86-20-8755-8029

China - Hangzhou Tel: 86-571-8792-8115 Fax: 86-571-8792-8116

China - Hong Kong SAR Tel: 852-2943-5100 Fax: 852-2401-3431

China - Nanjing Tel: 86-25-8473-2460 Fax: 86-25-8473-2470

China - Qingdao Tel: 86-532-8502-7355 Fax: 86-532-8502-7205

China - Shanghai Tel: 86-21-3326-8000 Fax: 86-21-3326-8021

China - Shenyang Tel: 86-24-2334-2829 Fax: 86-24-2334-2393

China - Shenzhen Tel: 86-755-8864-2200 Fax: 86-755-8203-1760

China - Wuhan Tel: 86-27-5980-5300 Fax: 86-27-5980-5118

China - Xian Tel: 86-29-8833-7252 Fax: 86-29-8833-7256

ASIA/PACIFIC

China - Xiamen Tel: 86-592-2388138 Fax: 86-592-2388130

China - Zhuhai Tel: 86-756-3210040 Fax: 86-756-3210049

India - Bangalore Tel: 91-80-3090-4444 Fax: 91-80-3090-4123

India - New Delhi Tel: 91-11-4160-8631 Fax: 91-11-4160-8632

India - Pune Tel: 91-20-3019-1500

Japan - Osaka Tel: 81-6-6152-7160 Fax: 81-6-6152-9310

Japan - Tokyo Tel: 81-3-6880- 3770 Fax: 81-3-6880-3771

Korea - Daegu Tel: 82-53-744-4301 Fax: 82-53-744-4302

Korea - Seoul Tel: 82-2-554-7200 Fax: 82-2-558-5932 or 82-2-558-5934

Malaysia - Kuala Lumpur Tel: 60-3-6201-9857 Fax: 60-3-6201-9859

Malaysia - Penang Tel: 60-4-227-8870 Fax: 60-4-227-4068

Philippines - Manila Tel: 63-2-634-9065 Fax: 63-2-634-9069

Singapore Tel: 65-6334-8870 Fax: 65-6334-8850

Taiwan - Hsin Chu Tel: 886-3-5778-366 Fax: 886-3-5770-955

Taiwan - Kaohsiung Tel: 886-7-213-7830

Taiwan - Taipei Tel: 886-2-2508-8600 Fax: 886-2-2508-0102

Thailand - Bangkok Tel: 66-2-694-1351 Fax: 66-2-694-1350

## AMERICAS

Corporate Office 2355 West Chandler Blvd. Chandler, AZ 85224-6199 Tel: 480-792-7200 Fax: 480-792-7277 Technical Support:

[http://www.microchip.com/ support](http://support.microchip.com/)

Web Address:

www.microchip.com

Atlanta Duluth, GA Tel: 678-957-9614 Fax: 678-957-1455

Austin, TX Tel: 512-257-3370

Boston Westborough, MA Tel: 774-760-0087 Fax: 774-760-0088

Chicago Itasca, IL Tel: 630-285-0071 Fax: 630-285-0075

Dallas Addison, TX Tel: 972-818-7423 Fax: 972-818-2924

Detroit Novi, MI Tel: 248-848-4000

Houston, TX Tel: 281-894-5983

Indianapolis Noblesville, IN Tel: 317-773-8323 Fax: 317-773-5453 Tel: 317-536-2380

Los Angeles Mission Viejo, CA Tel: 949-462-9523 Fax: 949-462-9608 Tel: 951-273-7800

Raleigh, NC Tel: 919-844-7510

New York, NY Tel: 631-435-6000

San Jose, CA Tel: 408-735-9110 Tel: 408-436-4270

Canada - Toronto Tel: 905-695-1980 Fax: 905-695-2078

## EUROPE

Austria - Wels Tel: 43-7242-2244-39 Fax: 43-7242-2244-393

Denmark - Copenhagen Tel: 45-4450-2828 Fax: 45-4485-2829

Finland - Espoo Tel: 358-9-4520-820

France - Paris Tel: 33-1-69-53-63-20 Fax: 33-1-69-30-90-79

France - Saint Cloud Tel: 33-1-30-60-70-00

Germany - Garching Tel: 49-8931-9700 Germany - Haan Tel: 49-2129-3766400

Germany - Heilbronn Tel: 49-7131-67-3636

Germany - Karlsruhe Tel: 49-721-625370

Germany - Munich Tel: 49-89-627-144-0 Fax: 49-89-627-144-44

Germany - Rosenheim Tel: 49-8031-354-560

Israel - Ra'anana Tel: 972-9-744-7705

Italy - Milan Tel: 39-0331-742611 Fax: 39-0331-466781

Italy - Padova Tel: 39-049-7625286

Netherlands - Drunen Tel: 31-416-690399 Fax: 31-416-690340

Norway - Trondheim Tel: 47-7289-7561

Poland - Warsaw Tel: 48-22-3325737

Romania - Bucharest Tel: 40-21-407-87-50

Spain - Madrid Tel: 34-91-708-08-90 Fax: 34-91-708-08-91

Sweden - Gothenberg Tel: 46-31-704-60-40

Sweden - Stockholm Tel: 46-8-5090-4654

UK - Wokingham Tel: 44-118-921-5800 Fax: 44-118-921-5820
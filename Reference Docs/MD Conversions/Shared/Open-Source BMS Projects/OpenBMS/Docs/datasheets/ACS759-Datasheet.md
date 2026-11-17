<!-- Converted from ACS759-Datasheet.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](ACS759-Datasheet_files/img_001.png)

Allegro

## Thermally Enhanced, Fully Integrated, Hall Effect-Based Linear Current Sensor IC With 100 μΩ Current Conductor and Optimized Performance at 3.3 V

## Features and Benefits

- Industry-leading noise performance through proprietary amplifier and filter design techniques
- Integrated shield greatly reduces capacitive coupling from current conductor to die due to high dV/dt signals, and prevents offset drift in high-side, high voltage applications
- Total output error improvement through gain and offset trim over temperature
- Small package size, with easy mounting capability
- Monolithic Hall IC for high reliability
- Ultra-low power loss: 100 μΩ internal conductor resistance
- Galvanic isolation allows use in economical, high-side current sensing in high voltage systems
- 3.0 to 3.6 V, single supply operation

Continued on the next page…

![Image](ACS759-Datasheet_files/img_002.png)

## Package: 5-pin package

![Image](ACS759-Datasheet_files/img_003.png)

![Image](ACS759-Datasheet_files/img_004.png)

Additional leadforms available for qualifying volumes

## Description

The Allegro™ ACS759 family of current sensor ICs provides economical and precise solutions for AC or DC current sensing. Typical applications include motor control, load detection and management, power supply and DC-to-DC converter control, inverter control, and overcurrent fault detection.

The device consists of a precision, low-offset linear Hall circuit with a copper conduction path located near the die. Applied current flowing through this copper conduction path generates a magnetic field which the Hall IC converts into a proportional voltage. Device accuracy is optimized through the close proximity of the magnetic signal to the Hall transducer. A precise, proportional output voltage is provided by the low-offset, chopper-stabilized BiCMOS Hall IC, which is programmed for accuracy at the factory.

High level immunity to current conductor dV/dt and stray electric fields, offered by Allegro proprietary integrated shield technology, guarantees low output voltage ripple and low offset drift in high-side, high voltage applications.

The output of the device has a positive slope (&gt;VCC / 2) when an increasing current flows through the primary copper conduction path (from terminal 4 to terminal 5), which is the path used for current sampling. The internal resistance of this conductive path is 100 μΩ typical, providing low power loss.

The thickness of the copper conductor allows survival of the device at high overcurrent conditions. The terminals of the

Continued on the next page…

## Typical Application

Application 1. The ACS759 outputs an analog signal, VOUT , that varies linearly with the bidirectional AC or DC primary current, IP , within the range specified. CF is for optimal noise management, with values that depend on the application.

![Image](ACS759-Datasheet_files/img_005.png)

## ACS759xCB

## Thermally Enhanced, Fully Integrated, Hall Effect-Based

Linear Current Sensor IC

With 100 μΩ Current Conductor and Optimized Performance at 3.3 V

## Features and Benefits (continued)

- 120 kHz typical bandwidth
- 3 μs output rise time in response to step input current
- Output voltage proportional to AC or DC currents
- Factory-trimmed for accuracy
- Extremely stable output offset voltage
- Nearly zero magnetic hysteresis

## Selection Guide

| Part Number1 | Package - Terminals | Package - Signal Pins | Primary Sampled Current , IP (A) | Sensitivity Sens (Typ.) (mV/A)2 | Current Directionality | TOP (°C) | Packing3 |
| - | - | - | - | - | - | - | - |
| ACS759LCB-050B-PFF-T | Formed | Formed | ±50 | 26.4 | Bidirectional | -40 to 150 | 34 pieces per tube |
| ACS759LCB-100B-PFF-T | Formed | Formed | ±100 | 13.2 | Bidirectional | -40 to 150 | 34 pieces per tube |
| ACS759KCB-150B-PFF-T | Formed | Formed | ±150 | 8.8 | Bidirectional | -40 to 125 | 34 pieces per tube |
| ACS759KCB-150B-PSS-T | Straight | Straight | ±150 | 8.8 | Bidirectional | -40 to 125 | 34 pieces per tube |
| ACS759ECB-200B-PFF-T | Formed | Formed | ±200 | 6.6 | Bidirectional | -40 to 85 | 34 pieces per tube |
| ACS759ECB-200B-PSS-T | Straight | Straight | ±200 | 6.6 | Bidirectional | -40 to 85 | 34 pieces per tube |

1Additional leadform options available for qualified volumes.

2With VCC = 3.3 V.

3Contact Allegro for additional packing options.

## Description (continued)

conductive path are electrically isolated from the signal leads (pins 1 through 3). This allows the ACS759 family of sensor ICs to be used in applications requiring electrical isolation without the use of opto-isolators or other costly isolation techniques.

The device is fully calibrated prior to shipment from the factory. The ACS759 family is lead (Pb) free. All leads are plated with 100% matte tin, and there is no Pb inside the package. The heavy gauge leadframe is made of oxygen-free copper.

![Image](ACS759-Datasheet_files/img_006.png)

![Image](ACS759-Datasheet_files/img_007.png)

Allegro

## ACS759xCB

## Absolute Maximum Ratings

| Characteristic | Symbol | Notes | Rating | Unit |
| - | - | - | - | - |
| Forward Supply Voltage | VCC |  | 8 | V |
| Reverse Supply Voltage |  | VRCC | -0.5 | V |
| Forward Output Voltage |  | VIOUT | 28 | V |
| Reverse Output Voltage |  | VRIOUT | -0.5 | V |
| Output Source Current | IOUT(Source) | VIOUT to GND | 3 | mA |
| Output Sink Current | IOUT(Sink) | VCC to VIOUT | 1 | mA |
| Nominal Operating Ambient | TOP | Range E | -40 to 85 | ºC |
| Temperature | TOP | Range K | -40 to 125 | ºC |
| Temperature |  | Range L | -40 to 150 | ºC |
| Maximum Junction | TJ(max) |  | 165 | ºC |
| Storage Temperature | Tstg |  | -65 to 165 | ºC |

## Isolation Characteristics

| Characteristic | Symbol | Notes | Rating | Unit |
| - | - | - | - | - |
| Dielectric Strength Test Voltage* | VISO | Agency type-tested for 60 seconds per UL standard 60950-1, 2nd Edition | 3000 | VAC |
| Working Voltage for Basic Isolation | VWFSI | For basic (single) isolation per UL standard 60950-1, 2nd Edition | 990 700 | VDC or Vpk Vrms |
| Working Voltage for Reinforced Isolation | VWFRI | For reinforced (double) isolation per UL standard 60950-1, 2nd Edition | 636 | VDC or Vpk |
|  | VWFRI | For reinforced (double) isolation per UL standard 60950-1, 2nd Edition | 450 | Vrms |

* Allegro does not conduct 60-second testing. It is done only during the UL certification process.

![Image](ACS759-Datasheet_files/img_007.png)

Allegro

## ACS759xCB

## Thermal Characteristics may require derating at maximum conditions

| Characteristic | Symbol | Test Conditions* | Value | Unit |
| - | - | - | - | - |
| Package Thermal Resistance | RθJA | Mounted on the Allegro evaluation board with 2800 mm2 (1400 mm2 on component side and 1400 mm2 on opposite side) of 4 oz. copper con- nected to the primary leadframe and with thermal vias connecting the copper layers. Performance is based on current flowing through the primary leadframe and includes the power consumed by the PCB. | 7 | ºC/W |

*Additional thermal information available on the Allegro website

## Typical Overcurrent Capabilities1,2

| Characteristic | Symbol | Notes | Rating | Unit |
| - | - | - | - | - |
| Overcurrent | IPOC | TA = 25°C, 1s duration, 1% duty cycle | 1200 | A |
|  | IPOC | TA = 85°C, 1s duration, 1% duty cycle | 900 | A |
|  | IPOC | TA = 150°C, 1s duration, 1% duty cycle | 600 | A |

1Test was done with Allegro evaluation board. The maximum allowed current is limited by TJ(max) only.

2For more overcurrent profiles, please see FAQ on the Allegro website, www.allegromicro.com.

![Image](ACS759-Datasheet_files/img_007.png)

Allegro

## ACS759xCB

## Functional Block Diagram

![Image](ACS759-Datasheet_files/img_008.png)

Pin-out Diagram

![Image](ACS759-Datasheet_files/img_009.png)

## Terminal List Table

| Number | Name | Description |
| - | - | - |
| 1 | VCC | Device power supply terminal |
| 2 | GND | Signal ground terminal |
| 3 | VIOUT | Analog output signal |
| 4 | IP+ | Terminal for current being sampled |
| 5 | IP- | Terminal for current being sampled |

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

## ACS759xCB

## With 100 μΩ Current Conductor and Optimized Performance at 3.3 V

## COMMON OPERATING CHARACTERISTICS1 valid at TOP = -40°C to 150°C and VCC = 3.3 V, unless otherwise specified

| Characteristic | Symbol | Test Conditions | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - | - |
| Supply Voltage | VCC |  | 3 | 3.3 | 3.6 | V |
| Supply Current | ICC | Output open | - | 10 | 13.5 | mA |
| Power-On Delay | tPOD | TA = 25°C | - | 10 | - | μs |
| Rise Time2 | tr | IP step = 60% of IP+, 10% to 90% rise time, TA = 25°C, COUT = 0.47 nF | - | 3 | - | μs |
| Propagation Delay Time2 | tPROP | TA = 25°C, COUT = 0.47 nF | - | 1 | - | μs |
| Response Time | tRESPONSE | Measured as sum of tPROP and tr | - | 4 | - | μs |
| Internal Bandwidth3 | BWi | -3 dB; TA = 25°C, COUT = 0.47 nF | - | 120 | - | kHz |
| Output Load Resistance | RLOAD(MIN) | VIOUT to GND | 4.7 | - | - | kΩ |
| Output Load Capacitance | CLOAD(MAX) | VIOUT to GND | - | - | 10 | nF |
| Primary Conductor Resistance | RPRIMARY | TA = 25°C | - | 100 | - | μΩ |
| Symmetry2 | ESYM | Over half-scale of Ip | - | 100 | - | % |
| Quiescent Output Voltage4 | VIOUT(Q) | IP = 0 A, TA = 25°C | - | VCC/2 | - | V |
| Ratiometry2 | VRAT | VCC = 3 to 3.6 V | - | 100 | - | % |

1Device is factory-trimmed at 3.3 V, for optimal accuracy.

2See Characteristic Definitions section of this datasheet.

3Calculated using the formula BWi = 0.35 / tr.

4VIOUT(Q) may drift over the lifetime of the device by as much as ±20 mV.

![Image](ACS759-Datasheet_files/img_007.png)

Allegro

## ACS759xCB

## With 100 μΩ Current Conductor and Optimized Performance at 3.3 V

## X050B PERFORMANCE CHARACTERISTICS1: TOP = -40°C to 150°C, VCC = 3.3 V, unless otherwise specified

| Characteristic | Symbol | Test Conditions | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - | - |
| Primary Sampled Current | IP |  | -50 | - | 50 | A |
| Sensitivity | SensTA | Full scale of IP applied for 5 ms, TA = 25°C | - | 26.4 | - | mV/A |
| Sensitivity | Sens (TOP)HT | Full scale of IP applied for 5 ms, TOP = 25°C to 150°C | - | 26.5 | - | mV/A |
| Sensitivity | Sens (TOP)LT | Full scale of IP applied for 5 ms,TOP = -40°C to 25°C | - | 26 | - | mV/A |
| Noise2 | VNOISE | TA= 25°C, 10 nF on VIOUT pin to GND | - | 6.6 | - | mV |
| Nonlinearity | ELIN | Up to full scale of IP , IP applied for 5 ms | - | <±1 | - | % |
| Electrical Offset Voltage3 | VOE(TA) | IP = 0 A, TA = 25°C | - | ±5 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)HT | IP = 0 A, TOP = 25°C to 150°C | - | ±10 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)LT | IP = 0 A, TOP = -40°C to 25°C | - | ±25 | - | mV |
| Magnetic Offset Error | IERROM | IP = 0 A, TA = 25°C, after excursion of 50 A | - | 125 | - | mA |
| Total Output Error4 | ETOT(HT) | Over full scale of IP , IP applied for 5 ms, TOP = 25°C to 150°C | - | ±1.5 | - | % |
| Total Output Error4 | ETOT(LT) | Over full scale of IP , IP applied for 5 ms, TOP = -40°C to 25°C | - | ±3.5 | - | % |

1See Characteristic Performance Data page for parameter distributions over temperature range.

2±3 sigma noise voltage.

3V OE(TOP) drift is referred to ideal VIOUT(Q) = 1/2 VCC.

4Percentage of IP. Output filtered.

## X100B PERFORMANCE CHARACTERISTICS1: TOP = -40°C to 150°C, VCC = 3.3 V, unless otherwise specified

| Characteristic | Symbol | Test Conditions | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - | - |
| Primary Sampled Current |  | IP | -100 | - | 100 | A |
| Sensitivity | SensTA | Full scale of IP applied for 5 ms, TA = 25°C | - | 13.2 | - | mV/A |
| Sensitivity | Sens (TOP)HT | Full scale of IP applied for 5 ms, TOP = 25°C to 150°C | - | 13.2 | - | mV/A |
| Sensitivity | Sens (TOP)LT | Full scale of IP applied for 5 ms, TOP = -40°C to 25°C | - | 13 | - | mV/A |
| Noise2 | VNOISE | TA= 25°C, 10 nF on VIOUT pin to GND | - | 4 | - | mV |
| Nonlinearity | ELIN | Up to full scale of IP , IP applied for 5 ms | - | <±1 | - | % |
| Electrical Offset Voltage3 | VOE(TA) | IP = 0 A, TA = 25°C | - | ±5 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)HT | IP = 0 A, TOP = 25°C to 150°C | - | ±10 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)LT | IP = 0 A, TOP = -40°C to 25°C | - | ±25 | - | mV |
| Magnetic Offset Error | IERROM | IP = 0 A, TA = 25°C, after excursion of 100 A | - | 185 | - | mA |
| Total Output Error4 | ETOT(HT) | Over full scale of IP , IP applied for 5 ms, TOP = 25°C to 150°C | - | ±1.8 | - | % |
| Total Output Error4 | ETOT(LT) | Over full scale of IP , IP applied for 5 ms, TOP = -40°C to 25°C | - | ±4 | - | % |

1See Characteristic Performance Data page for parameter distributions over temperature range.

2±3 sigma noise voltage.

3V OE(TOP) drift is referred to ideal VIOUT(Q) = 1/2 VCC.

4Percentage of IP. Output filtered.

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

## ACS759xCB

## With 100 μΩ Current Conductor and Optimized Performance at 3.3 V

## X150B PERFORMANCE CHARACTERISTICS1: TOP = -40°C to 125°C, VCC = 3.3 V, unless otherwise specified

| Characteristic | Symbol | Test Conditions | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - | - |
| Primary Sampled Current | IP |  | -150 | - | 150 | A |
| Sensitivity | SensTA | Full scale of IP applied for 5 ms, TA = 25°C | - | 8.7 | - | mV/A |
| Sensitivity | Sens (TOP)HT | Full scale of IP applied for 5 ms, TOP = 25°C to 125°C | - | 8.8 | - | mV/A |
| Sensitivity | Sens (TOP)LT | Full scale of IP applied for 5 ms, TOP = -40°C to 25°C | - | 8.6 | - | mV/A |
| Noise2 | VNOISE | TA= 25°C, 10 nF on VIOUT pin to GND | - | 3 | - | mV |
| Nonlinearity | ELIN | Up to full scale of IP , IP applied for 5 ms | - | <±1 | - | % |
| Electrical Offset Voltage3 | VOE(TA) | IP = 0 A, TA = 25°C | - | ±5 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)HT | IP = 0 A, TOP = 25°C to 125°C | - | ±5 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)LT | IP = 0 A, TOP = -40°C to 25°C | - | ±10 | - | mV |
| Magnetic Offset Error | IERROM | IP = 0 A, TA = 25°C, after excursion of 150 A | - | 235 | - | mA |
| Total Output Error4 | ETOT(HT) | Over full scale of IP , IP applied for 5 ms, TOP = 25°C to 125°C | - | ±2 | - | % |
| Total Output Error4 | ETOT(LT) | Over full scale of IP , IP applied for 5 ms, TOP = -40°C to 25°C | - | ±4 | - | % |

1See Characteristic Performance Data page for parameter distributions over temperature range.

2±3 sigma noise voltage.

3V OE(TOP) drift is referred to ideal VIOUT(Q) = 1/2 VCC.

4Percentage of IP. Output filtered.

## X200B PERFORMANCE CHARACTERISTICS1: TOP = -40°C to 85°C, VCC = 3.3 V, unless otherwise specified

| Characteristic | Symbol | Test Conditions | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - | - |
| Primary Sampled Current |  | IP | -200 | - | 200 | A |
| Sensitivity | SensTA | Full scale of IP applied for 5 ms, TA = 25°C | - | 6.6 | - | mV/A |
| Sensitivity | Sens (TOP)HT | Full scale of IP applied for 5 ms, TOP = 25°C to 85°C | - | 6.7 | - | mV/A |
| Sensitivity | Sens (TOP)LT | Full scale of IP applied for 5 ms, TOP = -40°C to 25°C | - | 6.5 | - | mV/A |
| Noise2 | VNOISE | TA= 25°C, 10 nF on VIOUT pin to GND | - | 2 | - | mV |
| Nonlinearity | ELIN | Up to full scale of IP , IP applied for 5 ms | - | <±1 | - | % |
| Electrical Offset Voltage3 | VOE(TA) | IP = 0 A, TA = 25°C | - | ±5 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)HT | IP = 0 A, TOP = 25°C to 85°C | - | ±5 | - | mV |
| Electrical Offset Voltage3 | VOE(TOP)LT | IP = 0 A, TOP = -40°C to 25°C | - | ±10 | - | mV |
| Magnetic Offset Error | IERROM | IP = 0 A, TA = 25°C, after excursion of 200 A | - | 268 | - | mA |
| Total Output Error4 | ETOT(HT) | Over full scale of IP , IP applied for 5 ms, TOP = 25°C to 85°C | - | ±2 | - | % |
| Total Output Error4 | ETOT(LT) | Over full scale of IP , IP applied for 5 ms, TOP = -40°C to 25°C | - | ±4 | - | % |

1See Characteristic Performance Data page for parameter distributions over temperature range.

2±3 sigma noise voltage.

3V OE(TOP) drift is referred to ideal VIOUT(Q) = 1/2 VCC .

4Percentage of IP. Output filtered.

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

## ACS759xCB

## Characteristic Performance Data

Data taken using the ACS759LCB-50B

## Accuracy Data

Electrical Offset Voltage versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_011.png)

Sensitivity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_012.png)

Nonlinearity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_013.png)

Symmetry versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_014.png)

![Image](ACS759-Datasheet_files/img_015.png)

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

## ACS759xCB

## Characteristic Performance Data

Data taken using the ACS759LCB-100B

## Accuracy Data

Electrical Offset Voltage versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_016.png)

Sensitivity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_017.png)

Nonlinearity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_018.png)

Symmetry versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_019.png)

2

![Image](ACS759-Datasheet_files/img_020.png)

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

## ACS759xCB

## Characteristic Performance Data

Data taken using the ACS759LCB-150B

## Accuracy Data

Electrical Offset Voltage versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_021.png)

Sensitivity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_022.png)

Nonlinearity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_023.png)

Symmetry versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_024.png)

2

![Image](ACS759-Datasheet_files/img_025.png)

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

## ACS759xCB

## Characteristic Performance Data

Data taken using the ACS759LCB-200B

## Accuracy Data

Electrical Offset Voltage versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_026.png)

Sensitivity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_027.png)

Nonlinearity versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_028.png)

Symmetry versus Ambient Temperature

![Image](ACS759-Datasheet_files/img_029.png)

![Image](ACS759-Datasheet_files/img_030.png)

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

## ACS759xCB

## Characteristic Performance Data

Data taken using the ACS759LCB-100

## Timing Data

![Image](ACS759-Datasheet_files/img_031.png)

## Response Time

![Image](ACS759-Datasheet_files/img_032.png)

## Propagation Delay Time

t (2 μs/div.)

![Image](ACS759-Datasheet_files/img_033.png)

![Image](ACS759-Datasheet_files/img_034.png)

![Image](ACS759-Datasheet_files/img_010.png)

Allegro

t (2 μs/div.)

## ACS759xCB

## Characteristic Definitions

## Definitions of Accuracy Characteristics

Sensitivity (Sens). The change in device output in response to a 1 A change through the primary conductor. The sensitivity is the product of the magnetic circuit sensitivity (G / A) and the linear IC amplifier gain (mV/G). The linear IC amplifier gain is programmed at the factory to optimize the sensitivity (mV/A) for the half-scale current of the device.

Noise (VNOISE). The noise floor is derived from the thermal and shot noise observed in Hall elements. Dividing the noise (mV) by the sensitivity (mV/A) provides the smallest current that the device is able to resolve.

Nonlinearity (ELIN). The degree to which the voltage output from the IC varies in direct proportion to the primary current through its half-scale amplitude. Nonlinearity in the output can be attributed to the saturation of the flux concentrator approaching the half-scale current. The following equation is used to derive the linearity:

<!-- formula-not-decoded -->

where

∆ gain = the gain variation as a function of temperature changes from 25ºC,

% sat = the percentage of saturation of the flux concentrator, which becomes significant as the current being sampled approaches half-scale ±IP , and

VIOUT\_half-scale amperes = the output voltage (V) when the sampled current approximates half-scale ±IP .

Symmetry (ESYM). The degree to which the absolute voltage output from the IC varies in proportion to either a positive or negative half-scale primary current. The following equation is used to derive symmetry:

<!-- formula-not-decoded -->

Ratiometry. The device features a ratiometric output. This means that the quiescent voltage output, VIOUTQ, and the magnetic sensitivity, Sens, are proportional to the supply voltage, VCC.

The ratiometric change (%) in the quiescent voltage output is defined as:

<!-- formula-not-decoded -->

and the ratiometric change (%) in sensitivity is defined as:

<!-- formula-not-decoded -->

Quiescent output voltage (VIOUT(Q)). The output of the device when the primary current is zero. For bidirectional devices, it nominally remains at VCC Ú 2. Thus, VCC = 3.3 V translates into VIOUT(QBI) = 1.65 V. For unidirectional devices, it nominally remains at 0.1 × VCC. Thus, VCC = 3.3 V translates into VIOUT(QUNI) = 0.33 V. Variation in VIOUT(Q) can be attributed to the resolution of the Allegro linear IC quiescent voltage trim, magnetic hysteresis, and thermal drift.

Electrical offset voltage (VOE). The deviation of the device output from its ideal quiescent value of VCC Ú 2 for bidirectional and 0.1 × VCC for unidirectional devices, due to nonmagnetic causes.

Magnetic offset error (IERROM). The magnetic offset is due to the residual magnetism (remnant field) of the core material. The magnetic offset error is highest when the magnetic circuit has been saturated, usually when the device has been subjected to a full-scale or high-current overload condition. The magnetic offset is largely dependent on the material used as a flux concentrator. The larger magnetic offsets are observed at the lower operating temperatures.

Total Output Error (ETOT). The maximum deviation of the actual output from its ideal value, also referred to as accuracy, illustrated graphically in the output voltage versus current chart on the following page.

ETOT is divided into four areas:

- 0 A at 25°C. Accuracy at the zero current flow at 25°C, without the effects of temperature.
- 0 A over Δ temperature. Accuracy at the zero current flow including temperature effects.
- Half-scale current at 25°C. Accuracy at the the half-scale current at 25°C, without the effects of temperature.
- Half-scale current over Δ temperature. Accuracy at the halfscale current flow including temperature effects.

![Image](ACS759-Datasheet_files/img_007.png)

Allegro

## ACS759xCB

With 100 μΩ Current Conductor and Optimized Performance at 3.3 V

## Definitions of Dynamic Response Characteristics

Power-On Time (tPO). When the supply is ramped to its operating voltage, the device requires a finite time to power its internal components before responding to an input magnetic field. Power-On Time, tPO , is defined as the time it takes for the output voltage to settle within ±10% of its steady state value under an applied magnetic field, after the power supply has reached its minimum specified operating voltage, VCC(min), as shown in the chart at right.

Rise time (tr). The time interval between a) when the device reaches 10% of its full scale value, and b) when it reaches 90% of its full scale value. The rise time to a step response is used to derive the bandwidth of the device, in which ƒ(-3 dB) = 0.35 / tr. Both tr and tRESPONSE are detrimentally affected by eddy current losses observed in the conductive IC ground plane.

![Image](ACS759-Datasheet_files/img_035.png)

Propagation delay (tPROP). The time required for the device output to reflect a change in the primary current signal. Propagation delay is attributed to inductive loading within the linear IC package, as well as in the inductive loop formed by the primary conductor geometry. Propagation delay can be considered as a fixed time offset and may be compensated.

![Image](ACS759-Datasheet_files/img_036.png)

Output Voltage versus Sampled Current

![Image](ACS759-Datasheet_files/img_037.png)

Total Output Error at 0 A and at Half-Scale Current

![Image](ACS759-Datasheet_files/img_038.png)

![Image](ACS759-Datasheet_files/img_039.png)

## ACS759xCB

## Chopper Stabilization Technique

Chopper Stabilization is an innovative circuit technique that is used to minimize the offset voltage of a Hall element and an associated on-chip amplifier. Allegro patented a Chopper Stabilization technique that nearly eliminates Hall IC output drift induced by temperature or package stress effects.

This offset reduction technique is based on a signal modulationdemodulation process. Modulation is used to separate the undesired DC offset signal from the magnetically induced signal in the frequency domain. Then, using a low-pass filter, the modulated DC offset is suppressed while the magnetically induced signal passes through the filter. The anti-aliasing filter prevents aliasing from happening in applications with high frequency signal components which are beyond the user's frequency range of interest.

As a result of this chopper stabilization approach, the output voltage from the Hall IC is desensitized to the effects of temperature and mechanical stress. This technique produces devices that have an extremely stable Electrical Offset Voltage, are immune to thermal stress, and have precise recoverability after temperature cycling.

This technique is made possible through the use of a BiCMOS process that allows the use of low-offset and low-noise amplifiers in combination with high-density logic integration and sample and hold circuits.

Concept of Chopper Stabilization Technique

![Image](ACS759-Datasheet_files/img_040.png)

![Image](ACS759-Datasheet_files/img_007.png)

Allegro

## Package CB, 5-pin package, leadform PFF

![Image](ACS759-Datasheet_files/img_041.png)

![Image](ACS759-Datasheet_files/img_042.png)

Allegro

![Image](ACS759-Datasheet_files/img_043.png)

## C Standard Branding Reference View

- N = Device part number
- T = Temperature code
- A = Amperage range
- L = Lot number
- Y = Last two digits of year of manufacture
- W = Week of manufacture
- = Supplier emblem

For Reference Only; not for tooling use (reference DWG-9111, DWG-9110) Dimensions in millimeters

Dimensions exclusive of mold flash, gate burrs, and dambar protrusions Exact case and lead configuration at supplier discretion within limits shown

Dambar removal intrusion

Perimeter through-holes recommended

A

B

- C Branding scale and appearance at supplier discretion

Creepage distance, current terminals to signal pins: 7.25 mm Clearance distance, current terminals to signal pins: 7.25 mm Package mass: 4.63 g typical

## Package CB, 5-pin package, leadform PSS

![Image](ACS759-Datasheet_files/img_044.png)

Creepage distance, current terminals to signal pins: 7.25 mm Clearance distance, current terminals to signal pins: 7.25 mm Package mass: 4.63 g typical

![Image](ACS759-Datasheet_files/img_045.png)

Allegro

## ACS759xCB

Thermally Enhanced, Fully Integrated, Hall Effect-Based

Linear Current Sensor IC

With 100 μΩ Current Conductor and Optimized Performance at 3.3 V

Copyright ©2011-2013, Allegro MicroSystems, LLC

Allegro MicroSystems, LLC reserves the right to make, from time to time, such de par tures from the detail spec i fi ca tions as may be required to permit improvements in the per for mance, reliability, or manufacturability of its products. Before placing an order, the user is cautioned to verify that the information being relied upon is current.

Allegro's products are not to be used in life support devices or systems, if a failure of an Allegro product can reasonably be expected to cause the failure of that life support device or system, or to affect the safety or effectiveness of that device or system.

The in for ma tion in clud ed herein is believed to be ac cu rate and reliable. How ev er, Allegro MicroSystems, LLC assumes no re spon si bil i ty for its use; nor for any in fringe ment of patents or other rights of third parties which may result from its use.

For the latest version of this document, visit our website:

www.allegromicro.com

![Image](ACS759-Datasheet_files/img_007.png)

Allegro
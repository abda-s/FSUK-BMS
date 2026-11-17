<!-- Converted from RTQ2539A Datasheet (Richtek).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_001.png)

## 3A, 6.5V, Ultra-Low Noise, Ultra-Low Dropout Linear Regulator

## General Description

The RTQ2539A is a high-current (3A), low-noise (6.8μVRMS), high accuracy (1% over line, load, and temperature), low-dropout linear regulator (LDO) capable of sourcing 3A with extremely low dropout (max. 130mV). The device supports single input supply voltage as low to 1.1V, which makes it easy to use.

The low-noise, high PSRR and high output current capability makes the RTQ2539A ideal to power noise-sensitive devices such as analog-to-digital converters (ADCs), digital-to-analog converters (DACs), and RF components. With very high accuracy, remote sensing, and soft-start capabilities to reduce inrush current, the RTQ2539A is ideal for powering digital loads such as FPGAs, DSPs, and ASICs.

The external enable control and power good indicator function make the control sequence easier. The output noise immunity is enhanced by adding external bypass capacitor on the NR/SS pin. The device is fully specified over the temperature range of TJ = -40°C to 125°C and is offered in a WQFN-12L 2.2x2.5 (FC) package.

## Features

-  Input Voltage Range : 1.1V to 6.5V
-  Output Voltage Range : 0.8 V to 5.5V
-  Accurate Output Voltage Accuracy (1%) Over Line, Load and Temperature
-  Ultra High PSRR : 40dB at 500kHz
-  Excellent Noise Immunity
- 6.8μVRMS at 0.8V Output
- 10μVRMS at 3.3V Output
-  Ultra Low Dropout Voltage : 130mV at 3A
-  Enable Control
-  Programmable Soft-Start Output
-  Stable with a 47μF or Larger Ceramic Output Capacitor
-  Support Power-Good Indicator Function
-  RoHS Compliant and Halogen Free
-  Junction Temperature Range : -40°C to 125°C

## Applications

-  Portable Electronic Devices

-  Wireless Infrastructures : SerDes, FPGA, DSP
-  RF, IF Components : VCO, ADC, DAC, LVDS

## Simplified Application Circuit

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_002.png)

## RTQ2539A

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_003.png)

## Ordering Information

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_004.png)

## Note :

Richtek products are Richtek Green Policy compliant and compatible with the current requirements of IPC/JEDEC J-STD-020.

## Marking Information

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_005.png)

00 : Product Code

W : Date Code

## Pin Configuration

(TOP VIEW)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_006.png)

WQFN-12L 2.2x2.5 (FC)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_007.png)

## Functional Pin Description

| Pin No. | Pin Name | Pin Function |
| - | - | - |
| 1, 2 | VIN | Supply input. A general 47µF ceramic capacitor should be placed as close as possible to this pin for better noise rejection. |
| 3 | EN | Enable control input. Connecting this pin to logic high enables the regulator, and driving this pin low puts it into shutdown mode. The device can have VIN and VEN sequenced in any order without causing damage to the device. However, to ensure the soft-start function to work as intended, certain sequencing rules must be applied. Enabling the device after VIN is present is preferred. |
| 4 | NR/SS | Noise-reduction and soft-start pin. Decoupling this pin to GND with an external capacitor CNR/SS can not only reduce output noise to very low levels but also slow down the rising of VOUT, providing a soft-start behavior. For low-noise applications, a 10nF to 1µF CNR/SS is suggested. |
| 5 | NC | No internal connection. Leaving these pins floating does not affect the functionality of the chip. By connecting these pins to GND, design engineers could extend the GND copper coverage on the PCB top layer to enhance the thermal convection. |
| 6, 7, 12 | GND | Ground. The exposed pad must be soldered to a large PCB and connected to GND for maximum power dissipation. |
| 8 | PGOOD | Power good indicator output. An open-drain output and active high when the output voltage reaches 88% of the target. The pin is pulled to ground when the output voltage is lower than its specified thresholds, including EN shutdown, OCP and OTP. |
| 9 | FB | Feedback voltage input. This pin is used to set the desired output voltage via an external resistive divider. The feedback reference voltage is 0.8V typically. |
| 10, 11 | VOUT | LDO output pins. A 47µF or larger ceramic capacitor (22µF or greater effective capacitance) is required for stability. Place the output capacitor as close to the device as possible and minimize the impedance between VOUT pin and load. |

## Functional Block Diagram

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_008.png)

## Operation

The RTQ2539A operates with single supply input ranging from 1.1V to 6.5V and is capable of delivering up to 3A current to the output. The device features high PSRR and low noise to provide a clean supply to the application.

A low-noise reference and error amplifier are included to reduce device noise. The NR/SS capacitor filters the noise from the reference, and the feed-forward capacitor filters the noise from the error amplifier. The high power-supply rejection ratio (PSRR) of the RTQ2539A minimizes the coupling of input supply noise to the output.

## Enable and Shutdown

The RTQ2539A provides an EN pin, as an external chip enable control, to enable or disable the device. VEN below 0.5 V turns the regulator off and enters the shutdown mode, while VEN above 1.1V turns the regulator on. When the regulator is shut down, the ground current is reduced to a maximum of 25μA. The enable circuitry has hysteresis (typically 50mV) for use with relatively slowly ramping analog signals.

If not used, connect the EN pin as close as possible to the largest capacitance on the input to prevent voltage droops on the VIN line from triggering the enable circuit.

## Programmable Soft-Start

The noise-reduction capacitor (CNR/SS) reduces noise and programs the soft-start ramp time during turn-on. When EN and UVLO exceed the respective threshold voltage, the RTQ2539A activates a quick-start circuit to charge the noise reduction capacitor (CNR/SS) and then the output voltage ramps up.

## Power Good

The power-good circuit monitors the feedback pin voltage to indicate the status of the output voltage. The opendrain PGOOD pin requires an external pull-up resistor to an external supply, and any downstream device can receive power-good as a logic signal that can be used for sequencing. A pull-up resistor from 10kΩ to 100kΩ is recommended. Make sure that the external pull-up supply voltage results in a valid logic signal for the receiving device or devices.

## RICHTEK

After start-up, the PGOOD pin becomes high impedance when the feedback voltage exceeds VPGOOD\_HYS (typically 90% of 0.8V reference voltage level). The PGOOD is pulled to GND when the feedback pin voltage falls below the VIT\_PGOOD. When En is low, the current limit or OTP levels are reached.

## Under-Voltage Lockout (UVLO)

The UVLO circuit monitors the input voltage to prevent the device from turning on before VIN rises above the VUVLO threshold. The UVLO circuit also disables the output of the device when VIN falls below the lockout voltage (VUVLO - ΔVUVLO). The UVLO circuit responds quickly to glitches on VIN and attempts to disable the output of the device if VIN collapses.

## Internal Current Limit (ILIM)

The RTQ2539A continuously monitors the output current to protect the device against high load current faults or short events. The current limit circuitry is not intended to allow operation above the rated current of the device. Continuously running the RTQ2539A above the rated current degrades the reliability of the device.

During current limit, the output voltage falls when load impedance decreases. If the output voltage is low, excessive power may cause the output thermal shutdown.

A foldback feature limits the short-circuit current to protect the regulator from damage under all load conditions. If the load current demand exceeds the foldback current limit before EN goes high, the device does not turn on.

## Over-Temperature Protection (OTP)

The RTQ2539A implements thermal shutdown protection. The device is disabled when the junction temperature (TJ) exceeds 160°C (typical). The LDO automatically turns on again when the temperature falls below 140°C (typical).

For reliable operation, limit the junction temperature to a maximum of 125°C. Continuously running the RTQ2539A into thermal shutdown or above a junction temperature of 125°C reduces long-term reliability.

## Output Active Discharge

When the device is disabled, the RTQ2539A discharges the LDO output (via VOUT pins) through an internal current sink to ground. Do not rely on the active discharge circuit for discharging a large amount of output capacitance after the input supply collapses because reverse current can possibly flow from the output to the input. External current protection should be added if the device works at reverse voltage state.

## RTQ2539A

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_009.png)

| Absolute Maximum Ratings (Note 1) |  |
| - | - |
|  VIN, PGOOD, EN --------------------------------------------------------------------------------------------------------- | -0.3V to 7V |
|  VOUT------------------------------------------------------------------------------------------------------------------------- | -0.3V to 7V |
|  NR/SS, FB ------------------------------------------------------------------------------------------------------------------ | -0.3V to 3.6V |
|  Lead Temperature (Soldering, 10 sec.) ------------------------------------------------------------------------------- | 260°C |
|  Junction Temperature----------------------------------------------------------------------------------------------------- | 150°C |
|  Storage Temperature Range -------------------------------------------------------------------------------------------- | -65°C to 150°C |
| ESD Ratings (Note 2)  ESD Susceptibility HBM (Human Body Model) ---------------------------------------------------------------------------------------------- | 2kV |
| Recommended Operating Conditions (Note 3)  Supply Input Voltage, VIN -----------------------------------------------------------------------------------------------  Junction Temperature Range-------------------------------------------------------------------------------------------- | 1.1V to 6.5V -40°C to 125°C |

## Thermal Information (Note 4 and Note 5)

| Thermal Parameter | Thermal Parameter | WQFN-12L 2.2x2.5 (FC) | Unit |
| - | - | - | - |
| θJA | Junction-to-ambient thermal resistance (JEDEC standard) | 54.8 | °C/W |
| θJC(Top) | Junction-to-case (top) thermal resistance | 53 | °C/W |
| θJC(Bottom) | Junction-to-case (bottom) thermal resistance | 16.1 | °C/W |
| θJA(EVB) | Junction-to-ambient thermal resistance (specific EVB) | 49.9 | °C/W |
| ΨJC(Top) | Junction-to-top characterization parameter | 0.2 | °C/W |
| ΨJB | Junction-to-board characterization parameter | 27.2 | °C/W |

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_010.png)

## Electrical Characteristics

Over operating temperature range (TJ = -40°C to 125°C), (1.1V ≤ VIN &lt; 6.5V and VIN ≥ VOUT(TARGET) + 0.3 V, VOUT(TARGET) = 0.8V, VOUT connected to 50Ω to GND, VEN = 1.1 V, CIN = 10μF, COUT = 47μF, CNR/SS = 0nF, CFF = 0nF, and PGOOD pin pulled up to VIN with 100kΩ, unless otherwise noted. (Note 6)

| Parameter | Symbol | Test Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - |
| Operating Input Voltage Range | VIN |  | 1.1 | -- | 6.5 | V |
| Feedback Reference Voltage | VREF |  | -- | 0.8 | -- | V |
| NR/SS Pin Voltage | VNR/SS |  | -- | 0.8 | --- | V |
| Under-Voltage Lockout | VUVLO | VIN increasing | -- | 1.02 | 1.085 | V |
| Under-Voltage Lockout | ∆VUVLO | Hysteresis | -- | 100 | -- | mV |
| Output Voltage Range |  | Using external resistors | 0.8 | -- | 5.5 | V |
| Output Voltage Accuracy (Note 7) | VOUT | VIN = VOUT + 0.3V, 0.8V ≤ VOUT ≤ 5.5V, 1mA ≤ IOUT ≤ 3A | -1 | -- | 1 | % |
| Line Regulation | ∆VOUT/∆VIN | IOUT = 1mA, 1.1V ≤ VIN ≤ 6.5 V | -- | 0.05 | -- | %/V |
| Load Regulation | ∆VOUT/∆IOUT | 1mA ≤ IOUT ≤ 3A | -- | 0.08 | -- | %/A |
| Dropout Voltage | VDROP | VIN = 1.1V to 6.5V, IOUT = 3A, VFB = 0.8V - 3% | -- | -- | 130 | mV |
| Output Current Limit | ILIM | VOUT = 90% VOUT(TARGET), VIN = VOUT(TARGET) + 400mV | 3.5 | 4.2 | 4.8 | A |
| Short-Circuit Current Limit | ISC | RLOAD = 20mΩ, under foldback operation | -- | 1.5 | -- | A |
| Ground Pin Current |  | Minimum load, VIN = 6.5V, IOUT = 5mA | -- | 3 | 4 | mA |
| Ground Pin Current | IGND | Maximum load, VIN = 1.4V, IOUT = 3A | -- | 4.3 | 5.5 | mA |
| Ground Pin Current |  | Shutdown, PGOOD = Open, VIN = 6.5V, VEN = 0.5V | -- | 1.2 | 25 | µA |
| EN Pin Current | IEN | VIN = 6.5V, VEN = 0V and 6.5V | -0.1 | -- | 0.1 | µA |
| EN Pin High-Level Input Voltage | VEN_H | Enable device | 1.1 | -- | 6.5 | V |
| EN Pin Low-Level Input Voltage | VEN_L | Disable device | 0 | -- | 0.5 |  |
| PGOOD Pin Threshold | VIT_PGOOD | For the direction PGOOD signal falling with decreasing VOUT | 0.82 x VOUT | 0.883 x VOUT | 0.93 x VOUT | V |
| PGOOD Pin Hysteresis | VPGOOD_HYS | For PGOOD signal rising | -- | 2% x VOUT | -- | V |
| PGOOD Pin Low- Level Output Voltage | VPGOOD_L | VOUT < VIT_PGOOD, IPGOOD = -1mA (current into device) | -- | -- | 0.4 | V |

## RTQ2539A

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_003.png)

| Parameter | Symbol | Test Conditions | Test Conditions | Min | Typ | Max | Unit |
| - | - | - | - | - | - | - | - |
| PGOOD Pin Leakage Current | IPGOOD_LK | VOUT > VIT_PGOOD , VPGOOD = 6.5V | VOUT > VIT_PGOOD , VPGOOD = 6.5V | -- | -- | 1 | µA |
| NR/SS Pin Charging Current | INR/SS | VNR/SS = GND, VIN = 6.5V | VNR/SS = GND, VIN = 6.5V | 4 | -- | 9 | µA |
| FB Pin Leakage Current | IFB | VIN = 6.5V | VIN = 6.5V | -100 | -- | 100 | nA |
| Power Supply Rejection Ratio | PSRR | VIN - VOUT = 0.4V, IOUT = 3A, CNR/SS = 100nF, CFF = 10nF, COUT = 47µF//10µF//10µF | f = 10kHz, VOUT = 0.8V | -- | 42 | -- | dB |
| Power Supply Rejection Ratio | PSRR | VIN - VOUT = 0.4V, IOUT = 3A, CNR/SS = 100nF, CFF = 10nF, COUT = 47µF//10µF//10µF | f = 500kHz, VOUT = 0.8V | -- | 39 | -- | dB |
| Power Supply Rejection Ratio | PSRR | VIN - VOUT = 0.4V, IOUT = 3A, CNR/SS = 100nF, CFF = 10nF, COUT = 47µF//10µF//10µF | f = 10kHz, VOUT = 5V | -- | 40 | -- | dB |
| Power Supply Rejection Ratio | PSRR | VIN - VOUT = 0.4V, IOUT = 3A, CNR/SS = 100nF, CFF = 10nF, COUT = 47µF//10µF//10µF | f = 500kHz, VOUT = 5V | -- | 25 | -- | dB |
| Output Noise Voltage | eNO | BW = 10Hz to 100kHz, IOUT = 3A, CNR/SS = 100nF, CFF = 10nF, COUT = 47μF &#124;&#124; 10μF &#124;&#124; 10μF | VIN = 1.1V, VOUT = 0.8V | -- | 6.8 | -- | µVRMS |
| Output Noise Voltage | eNO | BW = 10Hz to 100kHz, IOUT = 3A, CNR/SS = 100nF, CFF = 10nF, COUT = 47μF &#124;&#124; 10μF &#124;&#124; 10μF | VIN = 3.6V, VOUT = 3.3V | -- | 10 | -- | µVRMS |
| Output Noise Voltage | eNO | BW = 10Hz to 100kHz, IOUT = 3A, CNR/SS = 100nF, CFF = 10nF, COUT = 47μF &#124;&#124; 10μF &#124;&#124; 10μF | VOUT = 5 V | -- | 16 | -- | µVRMS |
| Thermal Shutdown Threshold | TSD | Temperature increasing | -- | 160 | -- |  | °C |
| Thermal Shutdown Threshold | TSD | Temperature decreasing | -- | 140 | -- |  | °C |

- Note 1. Stresses beyond those listed under "Absolute Maximum Ratings" may cause permanent damage to the device. These are stress ratings only, and functional operation of the device at these or any other conditions beyond those indicated in the operational sections of the specifications is not implied. Exposure to absolute maximum rating conditions may affect device reliability.
- Note 2. Devices are ESD sensitive. Handling precautions are recommended.
- Note 3. The device is not guaranteed to function outside its operating conditions.
- Note 4. For more information about thermal parameter, see the Application and Definition of Thermal Resistances report, AN061.
- Note 5. θJA(EVB), ψJC(Top) and ψJB are measured on a high effective-thermal-conductivity four-layer test board which is in size of 70mm x 50mm; furthermore, all layers with 1 oz. Cu. Thermal resistance/parameter values may vary depending on the PCB material, layout, and test environmental conditions.
- Note 6. VOUT(TARGET) is the expected VOUT value set by the external feedback resistors. The 50Ω load is disconnected when the test conditions specify an IOUT value.
- Note 7. External resistor tolerance is not taken into account.

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_011.png)

## Typical Application Circuit

Figure 1. Configuration Circuit for VOUT Adjusted by a Resistive Divider

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_012.png)

Table 1. Recommended Feedback-Resistor Values

| Output Voltage (V) | External Restive Divider Combinations - R1 (kΩ) | External Restive Divider Combinations - R2 (kΩ) |
| - | - | - |
| 0.9 | 12.4 | 100 |
| 1 | 12.4 | 49.9 |
| 1.2 | 12.4 | 24.9 |
| 1.5 | 12.4 | 14.3 |
| 1.8 | 12.4 | 10 |
| 2.5 | 12.4 | 5.9 |
| 3.3 | 11.8 | 3.74 |
| 4.5 | 11.8 | 2.55 |
| 5 | 12.4 | 2.37 |

Table 2. Recommended External Components

| Component | Description | Vendor P/N |
| - | - | - |
| CFF, CNR/SS | 10nF, 50V, X7R, 0603 | GRM033R71E103KE14 (Murata) |
| CIN, *COUT | 47µF, 10V, X5R, 0805 | GRM21BR61A476ME15 (Murata) |

* : Considering the effective capacitance derated with biased voltage level, the COUT component needs to satisfy the effective capacitance at least 22µF or above at targeted output level for stable and normal operation.

## Typical Operating Characteristics

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_013.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_003.png)

## Output Noise vs. Frequency and Output Voltage

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_014.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_015.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_016.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_017.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_018.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_019.png)

## Load Transient Response

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_020.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_021.png)

## Dropout Voltage vs. Output Current

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_022.png)

## Load Transient Response vs. Load Slew Rate

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_023.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_024.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_025.png)

## Application Information

Richtek's component specification does not include the following information in the Application Information section. Thereby no warranty is given regarding its validity and accuracy. Customers should take responsibility to verify their own designs and reserve suitable design margin to ensure the functional suitability of their components and systems.

The RTQ2539A is a high-current, low-noise, high-accuracy, low-dropout linear regulator which is capable of sourcing 3A with maximum dropout of 130mV. The input voltage operating range is 1.1V to 6.5V, and the adjustable output voltage is 0.8V to 5.5V according to the external resistor setting to get the required output target.

## Output Voltage Setting

The output voltage of the RTQ2539A can be set by external resistors to achieve different output targets.

By using external resistors, the output voltage is determined by the values of R1 and R2 as shown in Figure 2. The values of R1 and R2 can be calculated for any voltage value using the following formula :

Figure 2. Output Voltage Set by External Resistors

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_026.png)

## Dropout Voltage

The dropout voltage refers to the voltage difference between the VIN and VOUT pins while operating at a specific output current. The dropout voltage VDROP can also be expressed as the voltage drop on the pass-FET at a specific output current (IRATED) while the pass-FET is fully operating in the ohmic region, and the pass-FET can be characterized as a resistance RDS(ON). Thus, the dropout voltage can be defined as (VDROP = VIN - VOUT = RDS(ON) x IRATED). For normal operation, the suggested LDO operating range is (VIN &gt; VOUT + VDROP) for good transient response and PSRR performance. However, operation in the ohmic region will degrade the performance severely.

## CIN and COUT Selection

The RTQ2539A is designed to support low-seriesresistance (ESR) ceramic capacitors. X7R, X5R, and COGrated ceramic capacitors are recommended due to its good capacitive stability across different temperatures, whereas the use of Y5V-rated capacitors is not recommended because of large capacitance variations.

However, the capacitance of ceramic capacitors varies with operating voltage and temperature, and design engineers must be aware of these characteristics. Ceramic capacitors are usually recommended to be derated by 50%. A 47μF or greater output ceramic capacitor (or 22μF effective capacitance) is suggested to ensure stability. Input capacitance is selected to minimize transient input drop during load current steps. For general applications, an input capacitor of at least 47μF is highly recommended for minimal input impedance. If the trace inductance between the RTQ2539A input pin and power supply is high, a fast load transient can cause VIN voltage level ringing above the absolute maximum voltage rating which damages the device. Adding more input capacitors is available to restrict the ringing and keep it below the device absolute maximum ratings.

Generally, a 47μF 0805-sized ceramic capacitor in parallel with two 10μF 0805-sized ceramic capacitor ensures the minimum effective capacitance at high input voltage and high output voltage requirement. Place these capacitors as close to the pins as possible for optimum performance and to ensure stability.

## Feed-Forward Capacitor (CFF)

The RTQ2539A is designed to be stable without the external feed-forward capacitor (CFF). However, a 10nF external feed-forward capacitor optimizes the transient, noise, and PSRR performances. A higher capacitance of CFF can also be used, but the start-up time will be longer and the power-good signal will incorrectly indicate that the output voltage is settled.

## Soft-Start and Noise Reduction (CNR/SS)

The RTQ2539A is designed for a programmable, monotonic soft-start time during the output rising, which can be achieved via an external capacitor (CNR/SS) on NR/SS pin. Using an external CNR/SS is recommended for general application; it is not only for the in-rush current minimization but also to help reduce the noise component from the internal reference.

During the monotonic start-up procedure, the error amplifier of the RTQ2539A tracks the voltage ramp of the external soft-start capacitor (CNR/SS) until the voltage approaches the internal reference 0.8V. The soft-start ramp time can be calculated with Equation a1, which depends on the soft-start charging current (INR/SS), the soft-start capacitance (CNR/SS), and the internal reference 0.8V (VREF).

<!-- formula-not-decoded -->

For noise-reduction, CNR/SS in conjunction with an internal noise-reduction resistor forms a low-pass filter (LPF) and filters out the noise from the internal bandgap reference before being amplified via the error amplifier, thus reducing the total device noise floor.

## Input Inrush Current

During start-up, the input Inrush current into the VIN pin consists of the sum of load current and the charging current of the output capacitor. The inrush current is difficult to measure because the input capacitor must be removed, which is not recommended. Generally, the soft-start inrush current can be estimated by Equation b1, where VOUT(t) is the instantaneous output voltage of the power-on ramp, dVOUT(t) / dt is the slope of the VOUT ramp and RLOAD is the resistive load impedance.

<!-- formula-not-decoded -->

## Under-Voltage Lockout (UVLO)

The Under-Voltage Lockout (UVLO) threshold is the minimum input operational voltage range that ensures the device stays disabled. Figure 3 explains that the UVLO circuits are triggered between three different input voltage events (duration a, b and c), assuming VEN ≥ VEN\_H all the time. For duration "a", the input voltage starts rising. When VIN is over the UVLO rising threshold, VOUT starts the power-on process. Then when Vout reaches the target level, it is under regulation. During "b". Although the power line has a voltage drop, it does not drop below the UVLO low threshold (falling threshold). As a result, the device maintains normal operation, and VOUT is still regulated. At duration "c", VIN drops below the UVLO falling threshold, so the control loop is disabled and there is no regulation. Meanwhile, VOUT drops. For general application, instant power line transient with long power trace at the VIN pin may have VIN level unstable and force a trap as shown in duration "c", which makes VOUT collapse. In this case, adding more input capacitance or improving input trace layout on PCB are effective to improve input power stabilization.

Figure 3. Under-Voltage Lockout Trigger Conditions and Output Variation

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_027.png)

## Power-Good (PGOOD) Function

The power-good function monitors the voltage level at the feedback pin to indicate whether the output voltage status is normal or not. This function enables other devices to receive the RTQ2539A's power-good signal as a logic signal that can be used for the sequence design of the system application. The PGOOD pin is an open-drain structure and an external pull-up resistor connected to an external supply is necessary. The pull-up resistor value between 10kΩ to 100kΩ is recommended for proper operation. The lower limit of 10kΩ results from the maximum pull-down strength of the power-good transistor, and the upper limit of 100kΩ results from the maximum leakage current at the power-good node.

Figure 4 demonstrates some PGOOD scenarios versus VIN, EN and protection status. During "a", VEN is higher than the VEN\_H threshold, and the device is under operation. In this period, VOUT starts rising (the rising time is related to the soft-start capacitor CNR/SS). When VOUT is over the PGOOD hysteresis threshold, the reflected feedback voltage VFB exceeds VPGOOD\_HYS threshold. Consequently, the PGOOD pin becomes a high impedance node. The duration "b" indicates some unpredictable operation (e.g., OTP, OCP or severe output voltage drop caused by very fast load variation). When VFB is lower than the VIT\_PGOOD threshold, VPGOOD is pulled to GND, which indicates that the output voltage is not ready. In duration "c", VOUT has a small drop which is not lower than the PGOOD falling threshold; the PGOOD pin remains in high impedance. After VEN becomes logic "0", VPGOOD is pulled to GND as shown in duration "d".

Figure 4. PGOOD Trigger Scenario with Different Operating Status

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_028.png)

## Reverse Current Protection

The reverse current from VOUT to VIN that flows through the body diode of the pass element instead of the normal conducting channel can happen if the maximum VOUT exceeds VIN + 0.3V; in this case, the pass element may be damaged.

For example, if the output is biased above the input supply voltage level or the input supply has an instant drop at light load operation that makes VIN &lt; VOUT. As shown in Figure 5, an external Schottky diode can be added to prevent the pass element from being damaged by the reverse current.

Figure 5. Application Circuit for Reverse Current Protection

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_029.png)

## Thermal Considerations

The junction temperature should never exceed the absolute maximum junction temperature TJ(MAX), listed under Absolute Maximum Ratings, to avoid permanent damage to the device. The maximum allowable power dissipation depends on the thermal resistance of the IC package, the PCB layout, the rate of surrounding airflow, and the difference between the junction and ambient temperatures. The maximum power dissipation can be calculated using the following formula :

<!-- formula-not-decoded -->

where TJ(MAX) is the maximum junction temperature, TA is the ambient temperature, and θJA is the junction-to-ambient thermal resistance.

For continuous operation, the maximum operating junction temperature indicated under Recommended Operating Conditions is 125°C. The junction-to-ambient thermal resistance, θJA(EVB), is highly package dependent. For a WQFN-12L 2.2x2.5 (FC) package, the thermal resistance, θJA(EVB), is 49.9°C/W on a standard high effective-thermalconductivity four-layer test board. The maximum power dissipation at TA = 25°C can be calculated as below :

PD(MAX) = (125°C - 25°C) / (49.9°C/W) = 2W for a WQFN-12L 2.2x2.5 (FC) package.

The maximum power dissipation depends on the operating ambient temperature for the fixed TJ(MAX) and the thermal resistance, θJA(EVB). The derating curves in Figure 6 allows the designer to see the effect of rising ambient temperature on the maximum power dissipation.

Figure 6. Derating Curve of Maximum Power Dissipation

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_030.png)

## Layout Considerations

For best performance of the RTQ2539A, the PCB layout suggestions below are highly recommended. All circuit components should be placed on the same side and as close to the respective LDO pin as possible. Place the ground return path connection to the input and output capacitor. Connect the ground plane with a wide copper surface for good thermal dissipation. Using vias and long power traces for the input and output capacitors connections is not recommended and has negative effects on performance. Figure 7 shows a layout example that reduces conduction trace loops, helping to minimize inductive parasitics and load transient effects while improving the circuit stability.

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_031.png)

Figure 7. PCB Layout Guide

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_032.png)

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_003.png)

## Outline Dimension

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_033.png)

A1

W-Type 12L QFN 2.2x2.5 Package (FC)

| Symbol | Dimensions In Millimeters - Min | Dimensions In Millimeters - Max | Dimensions In Inches - Min | Dimensions In Inches - Max |
| - | - | - | - | - |
| A | 0.700 | 0.800 | 0.028 | 0.031 |
| A1 | 0.000 | 0.050 | 0.000 | 0.002 |
| A3 | 0.175 | 0.250 | 0.007 | 0.010 |

Tolerance

±0.050

## Footprint Information

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_034.png)

| Package | Number of Pin | Tolerance |
| - | - | - |
| V/W/U/XQFN2.2x2.5-12(FC) | 12 | ±0.05 |

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_003.png)

## Packing Information

## Tape and Reel Data

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_035.png)

| Package Type | Tape Size (W1) (mm) | Pocket Pitch (P) (mm) | Reel Size (A) - (mm) | Reel Size (A) - (in) | Units per Reel | Trailer (mm) | Leader (mm) | Reel Width (W2) Min./Max. (mm) |
| - | - | - | - | - | - | - | - | - |
| QFN/DFN 2.2x2.5 | 12 | 8 | 180 | 7 | 1,500 | 160 | 600 | 12.4/14.4 |

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_036.png)

- C, D and K are determined by component size. The clearance between the components and the cavity is as follows:
- For 12mm carrier tape: 0.5mm max.

| Tape Size | W1 - Max. | P - Min. | P - Max. | B - Min. | B - Max. | F - Min. | F - Max. | ØJ - Min. | ØJ - Max. | H - Max. |
| - | - | - | - | - | - | - | - | - | - | - |
| 12mm | 12.3mm | 7.9mm | 8.1mm | 1.65mm | 1.85mm | 3.9mm | 4.1mm | 1.5mm | 1.6mm | 0.6mm |

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_011.png)

## Tape and Reel Packing

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_037.png)

| Container - Package | Reel - Size | Units | Box - Item | Box - Size(cm) | Box - Reels | Box - Units | Carton - Item | Carton - Size(cm) | Carton - Boxes | Carton - Unit |
| - | - | - | - | - | - | - | - | - | - | - |
| QFN/DFN 2.2x2.5 | 7" | 1,500 | Box A | 18.3*18.3*8.0 | 3 | 4,500 | Carton A | 38.3*27.2*38.3 | 12 | 54,000 |
|  | 7" | 1,500 | Box E | 18.6*18.6*3.5 | 1 | 1,500 | For Combined or Partial Reel. | For Combined or Partial Reel. | For Combined or Partial Reel. | For Combined or Partial Reel. |

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_038.png)

## Packing Material Anti-ESD Property

| Surface Resistance | Aluminum Bag | Reel | Cover tape | Carrier tape | Tube | Protection Band |
| - | - | - | - | - | - | - |
| Ω/cm 2 | 10 4 to 10 11 | 10 4 to 10 11 | 10 4 to 10 11 | 10 4 to 10 11 | 10 4 to 10 11 | 10 4 to 10 11 |

## Richtek Technology Corporation

14F, No. 8, Tai Yuen 1 st Street, Chupei City

Hsinchu, Taiwan, R.O.C.

Tel: (8863)5526789

## RIHEK

Richtek products are sold by description only. Richtek reserves the right to change the circuitry and/or specifications without notice at any time. Customers should obtain the latest relevant information and data sheets before placing orders and should verify that such information is current and complete. Richtek cannot assume responsibility for use of any circuitry other than circuitry entirely embodied in a Richtek product. Information furnished by Richtek is believed to be accurate and reliable. However, no responsibility is assumed by Richtek or its subsidiaries for its use; nor for any infringements of patents or other rights of third parties which may result from its use. No license is granted by implication or otherwise under any patent or patent rights of Richtek or its subsidiaries.

![Image](RTQ2539A%20Datasheet%20%28Richtek%29_files/img_039.png)

## Datasheet Revision History

| Version | Date | Description | Item |
| - | - | - | - |
| 01 | 2023/9/15 | Modify | Features on P1 Ordering Information on P2 Electrical Characteristics on P7 Application Information on P13 |
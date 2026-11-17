<!-- Converted from TI SLVAES1A BLDC Driver Guide (high-side gate drive).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

www.ti.com Table of Contents

## Application Note

## Brushless-DC Motor Driver Considerations and Selection Guide

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_001.png)

## ABSTRACT

The usage of Brushless-DC (BLDC) motors is becoming more commonplace in the automotive and industrial markets. Although more challenging to spin, Texas Instruments' BLDC motor drivers make spinning BLDC motors as simple as possible by reducing design complexity while improving system efficiency. TI offers a diverse portfolio of BLDC motor drivers that support various architectures, integration, and control methods to best suit a wide range of applications. The portfolio is grouped into driver, control, and safety families that each include key technologies. These technologies enable developers to design smaller and more efficient systems, decrease design complexity, and meet functional safety standards and certifications.

## Table of Contents

| 1 Motor Considerations and Why Brushless DC Motors?.....................................................................................................3 |
| - |
| 2 Motor Driver Architecture...................................................................................................................................................... 4 |
| 2.1 Gate Driver vs Integrated FET Driver: Power, Voltage, and Current Requirements.......................................................... 4 |
| 2.2 Three Use Cases: Speed, Torque, or Position:..................................................................................................................5 |
| 2.3 Control Methods: Trap, Sine, or FOC.................................................................................................................................6 |
| 2.4 Sensored Versus Sensorless.............................................................................................................................................8 |
| 2.5 Current Sense Amplifiers................................................................................................................................................. 10 |
| 2.6 Interface............................................................................................................................................................................11 |
| 2.7 Power Integration............................................................................................................................................................. 11 |
| 2.8 100% Duty Cycle Support................................................................................................................................................12 |
| 3 Texas Instruments' Brushless-DC Motor Drivers.............................................................................................................. 13 |
| 3.1 Gate Drivers: DRV8x and DRV3x family..........................................................................................................................13 |
| 3.2 Integrated MOSFET: DRV831x Family.............................................................................................................................15 |
| 3.3 Control and Gate Driver: MCx Family.............................................................................................................................. 15 |
| 3.4 Full Integration: MCx831x and DRV10x Family............................................................................................................... 16 |
| 4 Conclusion............................................................................................................................................................................ 18 |
| 5 Revision History................................................................................................................................................................... 18 |
| List of Figures |
| Figure 1-1. Motor Driver Considerations and Selection Process.................................................................................................3 |
| Figure 2-1. Motor Driver Architectures.........................................................................................................................................4 |
| Figure 2-2. Comparison of Three Use Cases..............................................................................................................................6 |
| Figure 2-3. Trapezoidal Control (120°)........................................................................................................................................ 7 7 |
| Figure 2-4. Sinusoidal Control (180°).......................................................................................................................................... |
| Figure 2-5. Field-Oriented Control State Vector Diagram............................................................................................................8 |
| Figure 2-6. Determining Motor Position Using Hall Effect Sensors............................................................................................. 8 |
| Figure 2-7. Estimating Back-EMF Using a BEMF Comparator....................................................................................................9 |
| Figure 2-8. Calculating Back-EMF Using Known Motor Parameters and a First-Order Differential 9 |
| Equation............................. Figure 2-9. CSA Integration Using External Shunt Resistors.................................................................................................... 10 |
| Figure 2-10. CSA integration Using Internal Low-Side Current Sensing...................................................................................10 |
| Figure 2-11. Types of Interfaces in BLDC Motor Drivers............................................................................................................11 |
| 2-12. Examples of Buck and LDO Regulators Integrated in BLDC Motor Drivers..........................................................12 Figure 2-13. Bootstrap and Trickle Charge Pump (left) and Charge Pump (right) Architectures in BLDC Motor Drivers..........12 |
| Figure |
| Figure 3-1. Gate Driver Architecture for DRV8x/DRV3x Families..............................................................................................13 |
| Figure 3-2. Simplified Schematics for DRV8328 and DRV835x Industrial Gate Drivers........................................................... 13 |
| Figure 3-3. Simplified Schematic for DRV3205 Functional Safety Gate Driver......................................................................... 14 Figure 3-4. Integrated FET Architecture for DRV831x Families................................................................................................ 15 |

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_002.png)

| Figure 3-5. Simplified Schematics for DRV8311 and DRV8316 Integrated FET Drivers...........................................................15 |  |
| - | - |
| Figure 3-6. Control and Gate Driver Architecture for MCx Families.......................................................................................... | 15 |
| Figure 3-7. Full Integration Architecture for DRV10x and MCx831x Families........................................................................... | 16 |
| Figure 3-8. Simplified Schematics for MCT8316A and MCF8316A Devices.............................................................................17 |  |
| Figure 3-9. Simplified Schematics for DRV10974 and DRV10987 Devices.............................................................................. | 17 |
| List of Tables | List of Tables |
| Table 1-1. Comparison of Motor Types........................................................................................................................................3 |  |
| Table 2-1. Motor Driver Architectures.......................................................................................................................................... | 5 |
| Table 2-2. Comparison of Control Methods................................................................................................................................. | 6 |
| Table 2-3. Interfaces in TI's BLDC Motor Driver Families.......................................................................................................... | 11 |
| Table 3-1. Highlighted Control Features in MCF and MCT Devices.......................................................................................... | 16 |

## Trademarks

All trademarks are the property of their respective owners.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_003.png)

[www.ti.com](https://www.ti.com/)

## 1 Motor Considerations and Why Brushless DC Motors?

Brushless-DC (BLDC) motor usage is becoming more and more common for various applications due to the performance benefits they have over alternate motor types such as brushed-DC and stepper motors. As Table 1-1 shows, BLDC motors are more efficient, quieter, and have better power density, higher torque, higher speed, and longer lifetime when compared to brushed-DC and stepper motors.

Table 1-1. Comparison of Motor Types

| Motor Type | Pros | Cons |
| - | - | - |
| Brushless DC | Long life, quiet, optimal power density | Design complexity, higher cost |
| Brushed DC | Low cost, easy to use | Noisy, EMI wear-out, sparking |
| Stepper | Long life, quiet, open-loop position and speed control | Current control needed, not as power efficient as BLDC, noisy |

The significant benefits that BLDC motors have come with one important disadvantage: higher design complexity. Product development with BLDC motors requires knowledge of how to design an efficient system and get the motor to spin. Texas Instrument's BLDC team is working to reduce this barrier to entry and simplify BLDC design with innovative motor driver devices. This document serves to simplify BLDC design by exploring the considerations in selecting a BLDC motor driver (Figure 1-1).

Figure 1-1. Motor Driver Considerations and Selection Process

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_004.png)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_005.png)

## 2 Motor Driver Architecture

The first step in selecting a BLDC driver is to determine what type of architecture is best suited for an application. Architectures range from integrated FET drivers for low- to mid-power applications up to gate drivers enabling multi-kW motor drive systems. In addition, TI's BLDC portfolio offers integrated control drivers for both sensored and sensorless sinusoidal and trapezoidal control. Figure 2-1 illustrates the various motor driver architectures in TI's BLDC portfolio such as gate drivers (Blue), integrated FET drivers (Blue + Purple, and sensored vs sensorless integrated control (Green + Blue or Green + Blue + Purple).

Figure 2-1. Motor Driver Architectures

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_006.png)

## 2.1 Gate Driver vs Integrated FET Driver: Power, Voltage, and Current Requirements

Determining supply voltage, output current, and motor power in a system is one of the first steps in selecting what type of motor driver architecture is needed for an application.

Supply voltages come from two categories: battery powered and line powered. In both battery and line powered systems, the supply can vary in voltage, so a motor driver should support at least the maximum voltage of the battery with extra headroom in the case of voltage feedback or transients in the system. TI recommends using a motor driver rated up to 1.2 × the maximum voltage for well-regulated supplies and low-power motors, and 1.5 to 2 times for high-power motors and battery systems. Texas Instruments has a wide-ranging portfolio of motor drivers that support up to 56-V battery systems.

In general, integrated versus external FET architectures have different power requirements. High power (&gt; 70W) systems use gate drivers and low-to-mid-power systems (&lt; 70W) use integrated FET drivers. External FETs are able to drive higher power than integrated FETs because they are not constrained by the size of the single-chip integrated FET driver device. For integrated FET solutions, peak current, RMS current, and RDS(on) of the internal FETs are important considerations that directly relate to the motor power. For external FET solutions, the RDS(on) and current ratings of the external MOSFETs relate to the power the motor can drive.

- Integrated FET
- Motor power for integrated FET architectures can be calculated by Equation 1, where VM is the motor voltage and IRMS is the nominal current of the motor. P = VM × IRMS

<!-- formula-not-decoded -->

- Peak current is the maximum short duration current in a motor that can be caused by switching, inrush, or parasitic effects. Many motor drivers today have built in protection such as overcurrent protection. The peak current is the maximum current that can be driven before overcurrent protection kicks in. TI's Integrated FET drivers can drive up to tens of amps in peak current.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_007.png)

## [www.ti.com](https://www.ti.com/)

- RMS current (or continuous current) is the nominal current of the motor and directly relates to the power dissipation of the motor.
- For high-power systems, it may be difficult to find an integrated FET driver to meet peak and RMS current specifications, which means that the system needs to use a gate driver instead of an integrated FET driver.
- Gate Driver + External FET:
- External FET architectures can drive much more power than internal FET architectures because of the lower RDS(on) of external FETs. The larger size of external FETs allows their RDS(on) to be much lower without affecting motor driver die size. For example, an internal device may have an RDS(on) of hundreds of milliohms while an external FET may have less than 10 mΩ.
- Gate driver current is the current supplied to the gates of the external MOSFETS, which controls the rate of ON/OFF switching. Although not directly related to motor power, it is an important consideration as it relates to the slew rate, EMI performance, and thermal performance of the MOSFETs. TI gate driver architectures can source up 3.5-A of current and sink up to 4.5-A of gate driver current.
- The relationship between gate drive current and rise time to switch the FET on is calculated in Equation 2, where QGD is the gate-to-drain capacitance of the FET (which is the major contributor of the VDS slew rate of the FET) and IDRIVE is the gate drive current. QGD = IDRIVE × trise (2)
- If IDRIVE gate current is too high, it can cause overshoot, undershoot, or switch-node ringing that negatively affects EMI performance. Conversely, if IDRIVE gate current is too low, thermal losses can increase in the MOSFETs due to power dissipation from switching losses, where the motor current is continuing to flow during the MOSFET saturation region.
- In some gate drivers, such as TI's Smart Gate Drivers, gate current can be easily configured through the IDRIVE setting without the need to redesign external circuitry between the gate drivers and external FETs. This provides designers more flexibility in configuring their system for EMI versus thermal tradeoffs. For more information on TI's Smart Gate Drive technology, see Section 3.1.1.

Table 2-1 compares the specifications of gate driver and integrated FET driver architectures.

Table 2-1. Motor Driver Architectures

|  | Gate Driver | Integrated FET Driver |
| - | - | - |
| Power | High power (typically > 70W) | Low to mid power (typically < 70W) |
| Voltage Range | Up to 100 V | Normally 60 V or less |
| Gate Driver Current | Greater than 3.5-A/4.5-A of source/sink current | - |
|  | - | Peak Current Up to 13-A |
|  | External | MOSFETs Internal |
| Thermal | Power is dissipated in external MOSFETs | Limited by the size of the integrated package |
| Solution Size | Larger | Smaller |

## 2.2 Three Use Cases: Speed, Torque, or Position:

Motor Drivers are typically used for three applications that are well suited for specific motor driver architectures. As discussed in Section 2.1, the power, voltage, and current determine whether a gate driver or integrated FET driver architecture is best. The next consideration is whether or not to integrate control depending on one of the three following use cases and their typical applications:

- Speed: the motor should maintain a variable or consistent speed
- Appliance fans, vacuum cleaners, laptop cooling fans, blowers, ceiling fans
- Torque: the motor should be used to apply a force
- Power tools, electric bikes, automated doors and gates, power seats, smart locks

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_008.png)

- Position (servo control): the motor should move to a certain position, be able to hold the position and move back and forth
- IP Network Camera, drone gimbal, collaborative robots, HVAC damper

Figure 2-2 highlights the relationship between the three use cases and their corresponding architectures.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_009.png)

Figure 2-2. Comparison of Three Use Cases

## 2.3 Control Methods: Trap, Sine, or FOC

Many Brushless-DC motor commutation methods can be used to satisfy specific system requirements. Commutation methods vary largely on the motor type, application, and solution needed for the system. Each motor control method can be implemented from an external microcontroller or integrated into the motor driver. TI's BLDC motor drivers provide a wide portfolio of integrated trapezoidal, sinusoidal, and Field-oriented control in the Control &amp; Gate Driver and Full Integration portfolios.

Motor construction should be the main factor of choosing a control method. Brushless DC motors are wound trapezoidally or sinusoidally, determined by their Back-EMF (BEMF) waveform. To maximize torque and efficiency, the current driving the motor should match the shape of the Back-EMF waveform. Application type (torque, speed, or position) should also be considered when selecting a control method to optimize performance parameters.

A high-level overview of control method performance parameters are listed in Table 2-2.

Table 2-2. Comparison of Control Methods

|  | Trapezoidal | Sinusoidal | Field-Oriented Control |
| - | - | - | - |
| Algorithm complexity | Low | Medium | High |
| Motor efficiency (MTPA) | Low | Medium | High |
| Maximum speed | High | Low | Medium (Standard FOC) High (Field Weakening) |
| MOSFET switching losses | Low | High | High |
| Torque ripple | High | Medium | Low |
| Audible noise | High | Low | Low |

For more detailed information on how each control method works and their advantages, visit TI's Precision Lab Videos on BLDC Motor Drivers.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_010.png)

[www.ti.com](https://www.ti.com/)

## 2.3.1 Trapezoidal

Trapezoidal commutation is the most basic method of spinning a 3-phase Brushless-DC motor. This is accomplished by energizing the windings in a 6-step pattern every 60 electrical degrees so that one phase souring motor current, another phase is sinking motor current, and the last phase remains unconnected (Hi-Z). This produces a 120° trapezoidal-shaped current waveform for each phase (Figure 2-3).

Trap can be sensored or sensorless to determine the position of the motor and commutate the motor effectively. It is a low-cost, simple solution to implement that can generate high amounts of torque and speed and minimal MOSFET switching losses. However, it is low resolution and results in torque ripple and audible noise due to a non-ideal current drive.

Figure 2-3. Trapezoidal Control (120°)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_011.png)

## 2.3.2 Sinusoidal

Sinusoidal commutation is another commutation method that drives current through all three phases at a time and the current waveforms in all three motor windings vary smoothly and sinusoidally for 180 electrical degrees (Figure 2-4). A sinusoidal magnetic flux from the stator attracts the rotor permanent magnets to smoothly spin the rotor. Motors with sinusoidal BEMF generate very low torque ripple because the motor current is also sinusoidal and the delivered torque is constant. This means that the motor is acoustically quiet with good power efficiency. However, in sinusoidal commutation, switching losses are high as the commutation occurs throughout 180 electrical degrees with no window for High-Z.

In sensored controls, commutation signals (varying PWM duty cycle waveforms for each phase) are generated based on rotor position to drive the MOSFETS and generate smooth sinusoidal modulation of stator currents. In sensorless controls, a commutation look-up table is implemented. Based on BEMF estimation, commutation signals drive the MOSFETS to generate smooth sinusoidal modulation of stator currents.

Figure 2-4. Sinusoidal Control (180°)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_012.png)

## 2.3.3 Field-Oriented Control

FOC, shortened for Field-oriented Control, is an efficient commutation technique used to precisely and efficiently control the speed and torque of the motor. As the name suggests, FOC techniques orient the stator field perpendicular to rotor flux to achieve maximum torque.

Implementation of FOC can be highly complicated as it requires complex software and processing power to handle mathematical transforms and computations, such as Clarke Park, inverse Clarke, and inverse Park transforms. If position and speed are estimated sensorlessly from phase stator currents and voltages, the microcontroller must be fast enough to estimate the angle and velocity as the motor spins. This may require the use of real-time Digital Signal Processors (DSPs) to pipeline these math calculations or implement large lookup tables while the rest of the transformations are simultaneously being calculated. High-precision encoders are needed for FOC applications that require high accuracy, such as actuators and robotic arms. Based on the resolution of the encoders, positions can be precisely controlled with minimum torque ripple.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_013.png)

To simplify the design process, TI's MCF devices in the MCx control family integrates code-free Field-oriented control into the motor driver. These highly integrated BLDC motor drivers eliminate the need to develop, maintain and qualify motor-control software, which eliminates months of design time. Additionally, MCF devices intelligently extract motor parameters, enabling designers to quickly tune a motor while delivering consistent system performance regardless of motor manufacturing variations. Because these motor drivers integrate sensorless technology to determine rotor position, they eliminate the need for external sensors, which reduces system cost and increases reliability.

For external microcontrollers, TI provides sensorless-FOC solutions through its InstaSPIN™ library. It allows users to be able to identify, tune, and fully control motor parameters through real-time 3-phase voltage and current monitoring. In addition, a user-tuned speed controller and field controller allows the motor to obtain optimal speeds than designed.

Figure 2-5. Field-Oriented Control State Vector Diagram

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_014.png)

## 2.4 Sensored Versus Sensorless

When commutating a Brushless-DC motor, the position of the rotor must be known at all times to spin the motor with high efficiency and directional control. TI Motor Drivers incorporate both sensored and sensorless solutions. They can be implemented with or without an external MCU to detect position feedback and satisfy a wide variety of system designs.

## 2.4.1 Sensored

Sensored solutions incorporate the use of encoders, resolvers, or Hall-effect sensors to detect the position of the rotor relative to the stator at all times for proper commutation. A popular solution is Hall-effect sensors, which detect magnetic fields of the permanent rotor magnet and translate the changing magnetic fields into logic-level signals. These signals can be used as direct inputs into the motor driver or MCU to efficiently commutate the motor driver (Figure 2-6).

Speed, torque, and position applications can all use sensored solutions.

Figure 2-6. Determining Motor Position Using Hall Effect Sensors

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_015.png)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_010.png)

[www.ti.com](https://www.ti.com/)

## 2.4.2 Sensorless

Sensorless solutions remove any sensored components from the design, which helps save on BOM costs. Many TI motor drivers can detect the position of the brushless-DC motor without the use of Hall-effect sensors by either measuring back-EMF voltages generated on unconnected windings of the motor driver (Figure 2-7) or internally estimating the back-EMF voltage (Es) generated (Figure 2-8) using winding resistance (R), winding inductance (L), phase current (Is), and motor voltage (Vs).

Sensorless control is typically used for speed applications since the motor generates enough Back-EMF when it is spinning at a constant speed. Position control cannot be sensorless, and torque control is difficult to implement sensorlessly.

Figure 2-7. Estimating Back-EMF Using a BEMF Comparator

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_016.png)

Back-EMF

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_017.png)

Figure 2-8. Calculating Back-EMF Using Known Motor Parameters and a First-Order Differential Equation

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_013.png)

## 2.5 Current Sense Amplifiers

Current sense feedback is important in a motor system to implement closed-loop torque control or detect current limits. TI's BLDC motor drivers can offer 1x, 2x, or 3x current sense amplifiers (CSAs) to sense the motor phase currents and provide as analog voltage feedback for a microcontroller's analog-to-digital converter. There are two CSA architectures implemented in TI BLDC motor drivers: external shunt resistors and integrated low-side current sensing.

In external shunt resistor architectures, the motor current through an external shunt produces a proportional CSA output voltage. These are used mostly in gate driver architectures as the shunt resistors are rated for high power and are in the range of milliohms.

Figure 2-9. CSA Integration Using External Shunt Resistors

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_018.png)

Integrated low-side current sensing architectures do not require an external shunt resistor; the motor current going into the low-side MOSFET is sensed and converted into an analog voltage using current mirroring technology. This form of current sensing is used mostly in integrated MOSFET BLDC motor drivers.

Figure 2-10. CSA integration Using Internal Low-Side Current Sensing

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_019.png)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_010.png)

[www.ti.com](https://www.ti.com/)

## 2.6 Interface

Before spinning a BLDC motor, there are many driver settings that must be configured and tuned appropriately for the motor system to be robust and efficient. For example, some of these settings can be overcurrent protection thresholds, gate drive current settings, or PWM input mode. TI BLDC motor drivers offer a variety of interfaces to simplify configuring settings, diagnose motor faults, or even control the motor itself. The 4 interfaces supported are Serial Peripheral Interface (SPI), Hardware (H/W), Inter-inter communication (I 2 C), and Texas Instruments SPI (tSPI).

Figure 2-11. Types of Interfaces in BLDC Motor Drivers

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_020.png)

SPI - SPI interfaces use a traditional 4-wire SPI protocol and up to 10 MHz clock speed to read/write data to one or more motor driver devices. SPI devices allow for configurability of many motor settings in control register maps and allow for detailed fault diagnosis in status register maps.

H/W - Hardware interfaces use 2-5 dedicated pins set by external resistors to configure driver settings. On some devices, the hardware pins replace the SPI wires with four adjustable settings, and many other settings are fixed internally in the device. Hardware devices help simplify the motor driver design and development process.

I 2 C - I 2 C devices uses only two wires with external pullup resistors to configure multiple devices up to 400 kHz maximum frequency. These devices offer configurable settings and fault diagnosis through control and status registers.

tSPI - tSPI interface uses a traditional 4-wire SPI interface to control up to 15 motors independently. tSPI commands gives PWM duty cycle and frequency information for each addressable tSPI device to control each motor. This interface reduces the number of control wires for 3-phase motors by (N*6)-4 and significantly reduces the system size.

Table 2-3 gives a quick comparison of which families include which interfaces.

Table 2-3. Interfaces in TI's BLDC Motor Driver Families

|  | Gate Driver (DRV8x, DRV3x) | Integrated FET (DRV831x) | Control + Gate Driver (MCx) | Full Integration (MCx831x) |
| - | - | - | - | - |
| SPI | ✓ | ✓ |  |  |
| Hardware | ✓ | ✓ | ✓ | ✓ |
| I 2 C |  |  | ✓ | ✓ |
| tSPI |  | ✓ |  |  |

## 2.7 Power Integration

To supply external rails to power other devices or circuits in the system (such as MCUs and CSA reference voltages), many TI BLDC motor drivers offer integrated buck regulators and linear dropout regulators (LDOs) regulators. These regulators offer high efficiency without the need

Integrated buck regulators can support up to 600-mA external load current depending on the device. The output voltage of the regulator can be adjustably designed or configured over SPI/hardware on many devices.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_021.png)

Integrated LDOs can support up to 100-mA external load current for a fixed 3.3-V or 5-V rail (AVDD or DVDD) depending on the device.

Figure 2-12. Examples of Buck and LDO Regulators Integrated in BLDC Motor Drivers

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_022.png)

## 2.8 100% Duty Cycle Support

The high-side N-type MOSFET in an external powerstage requires about 10-V higher than the motor voltage to fully enhance the MOSFET. In some applications, this FET needs to be on for the entire PWM period (100% duty cycle support), which presents challenges in design to provide a regulated gate voltage and gate current. TI provides two choices of integration to support 100% duty cycle for high-side MOSFET enhancement: bootstrap or charge pump architectures.

Bootstrap architectures use external bootstrap capacitors to provide high-side MOSFET enhancement from an externally provided or internally generated gate drive voltage (GVDD). In order to refresh the bootstrap capacitors, the high-side FET must be switched off and the low-side FET must be switched on for a minimum amount of time. To support 100% duty cycle, a trickle charge pump is integrated into the device to keep the high-side MOSFET enhanced. Bootstrap architectures are low-cost, small in integration, and have high efficiency.

Charge pump architectures integrate a doubler or tripler charge pump controller to regulate the high-side gate drive voltage from the motor driver supply voltage. This eliminates the need for external bootstrap capacitors and requires only two capacitors for charge pump operation. A doubler or tripler charge pump allows for lower minimum supply voltage requirements to generate the high-side MOSFET gate drive voltage.

Figure 2-13. Bootstrap and Trickle Charge Pump (left) and Charge Pump (right) Architectures in BLDC Motor Drivers

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_023.png)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_024.png)

[www.ti.com](https://www.ti.com/)

## 3 Texas Instruments' Brushless-DC Motor Drivers

TI's Brushless DC Motor Driver portfolio supports various combinations of the architecture and use cases discussed above. The portfolio is divided into four groups: Gate Drivers (DRV8x and DRV3x family), Integrated MOSFET Drivers (DRV831x family), Integrated Control Drivers (MCx family), and Full Integration (MCx831x and DRV10x family). Each family supports industrial and automotive grade devices and comes in a variety of packages, variants, and integrations.

The following sections will provide details about the key technologies that each family supports. To learn more about the specific products in each family, visit ti.com/bldc .

## 3.1 Gate Drivers: DRV8x and DRV3x family

Figure 3-1. Gate Driver Architecture for DRV8x/DRV3x Families

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_025.png)

## 3.1.1 DRV8x Family

TI's DRV8x family of gate drivers includes industrial and automotive gate drive solutions with protection, sensing, or power management solutions. DRV8x devices include charge pump and bootstrap architectures, which are two ways of providing high-side N-type MOSFET enhancement up to 100% duty cycle. Many devices support 6x PWM input signals for motor control, but some options include 3x PWM or 1x PWM interfaces to reduce the number of PWM inputs needed from an external MCU. These devices eliminate the need for external components or control signals to create safe, simple, and robust motor drive applications. DRV8x devices range in voltages from 4.5-V to 102-V and are intended for up to 56-V systems.

Many devices includes TI's Understanding Smart Gate Drive technology, which provides a combination of

protection features and gate-drive configurability. Many features include MOSFET slew rate adjustability, closedloop dead time, integrated gate fault protection, and strong pulldowns to prevent accidental dV/dt turn-ons. These internal gate-drive circuits allow designers to quickly and easily optimize switching losses and EMI performance by configuring gate registers through SPI commands or hardware resistors rather than redesigning a schematic. By integrating performance and protection circuitry into the chip, this not only reduces the system size and total cost but also provides enhanced flexibility, ease of use, and design simplicity when compared to discretely built or non-Smart-Gate-Drive drivers.

TI's gate drivers include additional optional integration such as current sensing and power supplies. Integrated current sense amplifiers (CSAs) can measure the phase currents of the low-side FETs through external shunt resistors and send this information to the microcontroller as sense voltages. Select DRV8x devices offer integrated charge pumps, trickle charge pumps, LDOs, or buck regulators to supply power to microcontrollers or provide system voltage rails with exceptional efficiency and low input quiescent current. This further reduces system size and cost, and helps enable easier manufacturing sourcing.

Figure 3-2. Simplified Schematics for DRV8328 and DRV835x Industrial Gate Drivers

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_026.png)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_005.png)

## 3.1.2 DRV3x Family

TI's DRV32xx family of 3-phase gate drivers is designed for customers developing Functional Safety automotive motor systems. TI's DRV32xx family includes devices tailored for 12-V and 48-V automotive battery profiles. The devices are available in both AEC-Q100 Grade 1 (-40°C to 125°C ambient temperature) and Grade 0 (-40°C to 150°C ambient temperature) qualified packages. These devices are developed using an ISO-26262 certified workflow and include additional diagnostic and monitoring features to enable system designers targeting ASIL ratings up to ASIL-D.

DRV32x gate drivers also come with additional supporting documentation to help enable system designers to achieve their targeted ASIL rating. The Safety Manual includes detailed explanations for the monitoring and diagnostic features assumed by the Safety Element Out of Context (SEOoC). The Safety Analysis Report includes a detailed Failure Mode Effect and Diagnostic Analysis (FMEDA) and FIT rate calculation for the device.

Figure 3-3. Simplified Schematic for DRV3205 Functional Safety Gate Driver

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_027.png)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_028.png)

[www.ti.com](https://www.ti.com/)

## 3.2 Integrated MOSFET: DRV831x Family

Figure 3-4. Integrated FET Architecture for DRV831x Families

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_029.png)

TI's DRV831x family include integrated MOSFET solutions to further save board space and reduce overall system cost. Integrated MOSFET solutions provide efficient switching and current control to maximize output current capability from a single integrated circuit. To control MOSFET switching, many integrated and external MOSFET architectures utilize 1x, 3x, 6x, or tSPI control schemes. These PWM modes allow the designer to support various commutation and control methods as well as free up I/O pins for the MCU. TI provides a variety of low power (&lt;15W) and medium-power (&lt;70W) integrated MOSFET solutions.

Many integrated MOSFET drivers includes three integrated CSAs to sense low-side FET current, which removes the need for external shunt resistors. Additionally, some devices include adjustable buck regulators and LDOs to provide external supply rails in a thermally efficient package. Integrated MOSFET drivers provide a variety of configurable protection features to guard the device against abnormal supply voltages, overcurrent events, or overtemperature.

Figure 3-5. Simplified Schematics for DRV8311 and DRV8316 Integrated FET Drivers

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_030.png)

## 3.3 Control and Gate Driver: MCx Family

Figure 3-6. Control and Gate Driver Architecture for MCx Families

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_031.png)

TI's MCx family of control &amp; gate drivers integrates control functionality into the driver for a device that can spin the motor without MCU assistance. Integrated control allows for code-free trapezoidal and field-oriented control via programmable EEPROM and configuring settings over a I 2 C or hardware interface. Control and gate driver devices are intended for &gt;70W motor drive systems to provide a smaller BOM size for systems that traditionally use an external MCU for traditional motor control. These devices require external N-type power MOSFETs and 1 or more current sense resistor(s) for accurate trapezoidal or Field-oriented control.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_013.png)

The controller in MCx devices allows for speed control through an analog input, PWM input with varying duty cycle and frequency, or speed command. The MCx family of devices can come in I 2 C, SPI, or hardware interfaces to support a variety of low-cost MCUs for configuration. There is configurability for all stages of motor control, including pre-startup, startup, open-loop, closed-loop, and motor stop. To assist with configuring settings, GUIs and tuning guides are available for evaluation.

MCF (integrated Field-oriented control) devices offer a variety of unique features. The Motor Parameter Extraction Tool (MPET) automatically performs motor identification to determine electrical parameters such as motor resistance, inductance, and flux, and mechanical parameters such as moment of inertia and coefficient of friction. Additionally, MCF devices auto-tunes PI controller gains using the identified mechanical and electrical parameters to achieve speed and torque regulation and stability.

MCT (integrated trapezoidal control) devices support up to 3 kHz electrical frequency and have less than 50 ms of startup and 150 ms of deceleration time. The control algorithm supports 120° and 150° current modulation to improve acoustic performance and includes lead angle adjustment to optimize the motor efficiency. Additionally, MCT devices includes an Active Demagnetization feature to reduce power losses from low-inductance motors.

Table 3-1. Highlighted Control Features in MCF and MCT Devices

| MCF Devices (integrated Field-oriented control) | MCT Devices (integrated trapezoidal control) |
| - | - |
| Offline motor parameters measurement with Motor Parameter Extraction Tool (MPET) | Supports up to 3 kHz electrical frequency |
| 5-point configurable speed profile support | Very fast startup time (< 50 ms) |
| Improved acoustic performance with automatic dead time compensation | Fast Deceleration (< 150 ms) |
| Speed Loop with accuracy of 3% with internal clock and 1% with external clock reference at room temperature | Supports 120° or 150° modulation to improve acoustic performance |
| Auto-tuned torque and speed PI controller gains | Active Demagnetization to reduce power losses |
| Spread spectrum and slew rate for EMI mitigation | Lead angle adjust to optimize efficiency |

MCx device features include driver fault protections such as overtemperature, overvoltage, undervoltage, overcurrent, cycle-by-cycle current limit, etc. There are also controller fault protections for IPD, MPET, abnormal speed/BEMF, motor lock, speed/torque saturation, etc. Finally, MCx devices may include power integration options such as an LDO, adjustable buck regulator, and integrated bootstrap with trickle charge pump architecture for high-side MOSFET enhancement.

## 3.4 Full Integration: MCx831x and DRV10x Family

Figure 3-7. Full Integration Architecture for DRV10x and MCx831x Families

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_032.png)

## 3.4.1 MCx831x Family

TI's MC831x family of Fully Integrated motor drivers brings in both motor control and MOSFETs to offer a one-chip solution for motor drivers. Integrated control allows for code-free trapezoidal and field-oriented control settings with only an external MCU needed for configuring settings over I. These devices range from 4.5-V to 40-V and up to 8-A peak current and supports motor drives up to &lt;70W.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_010.png)

[www.ti.com](https://www.ti.com/)

TI's MCx family of control and gate drivers integrates control functionality into the driver for a device that can spin the motor without MCU assistance. Integrated control and MOSFETs allows for complete system-on-chip solution for code-free trapezoidal and field-oriented control via programmable EEPROM and configuring settings over an I 2 C or hardware interface. Fully integrated MCx831x devices provide the smallest BOM size for systems that traditionally use an external MCU and N-type power MOSFETs for traditional motor control. Current sensing is integrated into the device without the need for external sense resistors. The MCx831x devices include an integrated charge pump for high-side MOSFET enhancement as well as an adjustable buck regulator and LDO to support external logic-level power rails.

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_033.png)

monitoring, 12-bit DAC

Figure 3-8. Simplified Schematics for MCT8316A and MCF8316A Devices

## 3.4.2 DRV10x family

TI's DRV10x family of motor drivers includes gate drivers, integrated MOSFET, and integrated control functionality to spin a motor without an external microcontroller. DRV10x devices minimize noise and vibration with true and accurate 180° sinusoidal algorithms. Our motor drivers feature trap, sine, and FOC control variants for optimal efficiency in a variety of motors. Sensorless algorithms further reduce design complexity by removing Hall sensors.

The DRV10x family provides simple control of motor speed by applying a PWM input to control the magnitude of the drive voltage. This is accomplished by driving the PWM pin with an analog voltage or writing the speed command directly through the I 2 C port and monitoring the FG pin for speed feedback. An adjustable lead angle feature in DRV10x devices allows the user to optimize the driver efficiency by aligning the phase current and the phase Back-EMF. Lead angle adjustment achieves the best efficiency regardless of the motor parameters and load conditions. DRV10x devices deliver current to the motor with an input supply voltage ranging from 2.1-V to 30-V. In some devices, if the power supply voltage is higher than the maximum voltage threshold, the device stops driving the motor and protects the device circuitry. DRV10x devices feature an integrated step-down regulator to accurately step down the supply voltage to either 5-V or 3.3-V for powering both internal and external circuits. Devices are available in either a sleep mode or a standby mode version to conserve power when the motor is not running.

Figure 3-9. Simplified Schematics for DRV10974 and DRV10987 Devices

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_034.png)

![Image](TI%20SLVAES1A%20BLDC%20Driver%20Guide%20%28high-side%20gate%20drive%29_files/img_013.png)

## 4 Conclusion

As using BLDC motors is becoming more common in applications today, understanding the architecture options and key considerations when choosing a specific BLDC motor driver is important to get the most out of a design, whether that be for size optimization, increasing thermal efficiency, lessening commutation complexity, or lowering total BOM cost. As discussed in this document, TI's BLDC motor driver portfolio supports various architectures and use cases to enable designers of all applications to get the most out of their BLDC systems. To learn more about BLDC's motor driver solutions, visit the products page at http://www.ti.com/motor-drivers/ brushless-dc-bldc-drivers/products.html.

## 5 Revision History

NOTE: Page numbers for previous revisions may differ from page numbers in the current version.

| Changes from Revision * (June 2020) to Revision A (May 2022) | Page |
| - | - |
| · Updated the numbering format for tables, figures, and cross-references throughout the document..................1 |  |
| · Updated Section 1.............................................................................................................................................. | 3 |
| · Updated Section 2.3.3........................................................................................................................................ | 7 |
| · Added Section 2.5............................................................................................................................................ | 10 |
| · Added Section 2.6.............................................................................................................................................11 |  |
| · Added Section 2.7.............................................................................................................................................11 |  |
| · Added Section 2.8............................................................................................................................................ | 12 |
| · Updated Section 3.1......................................................................................................................................... | 13 |
| · Updated Section 3.2......................................................................................................................................... | 15 |
| · Updated Section 3.3......................................................................................................................................... | 15 |
| · Updated Section 3.4......................................................................................................................................... | 16 |

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2022, Texas Instruments Incorporated
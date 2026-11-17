<!-- Converted from UVA - Racing BMS (Link and Schroer Capstone Report 2024).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

## Racing Battery Management System

A Technical Report submitted to the Department of Electrical and Computer Engineering

Presented to the Faculty of the School of Engineering and Applied Science University of Virginia · Charlottesville, Virginia

In Partial Fulfillment of the Requirements for the Degree Bachelor of Science, School of Engineering

John Link Spring, 2024

Capstone Project Team Members Silas Schroer Gabriel Binning Asad Shamsiev

On my honor as a University Student, I have neither given nor received unauthorized aid on this assignment as defined by the Honor Guidelines for Thesis-Related Assignments

Advisor

Adam Barnes - Department of Computer and Electrical Engineering

## Table of Contents

| 1. Statement of Work | 3 |
| - | - |
| John Link | 3 |
| Silas Schroer | 3 |
| Asad Shamsiev | 3 |
| Gabriel Binning | 3 |
| 2. Abstract | 4 |
| 3. Background | 4 |
| 4. Societal Impact Constraints | 6 |
| 5. Physical Constraints | 7 |
| Cost Constraints | 7 |
| Design and Manufacturing Constraints | 7 |
| Tools Utilized | 7 |
| 6. External Standards | 8 |
| 7. Intellectual Property Issues | 9 |
| 8. Project Description | 10 |
| Performance Objectives and Specifications | 10 |
| How It Works | 10 |
| Technical Details | 133 |
| Test Plans | 177 |
| 9. Timeline | 199 |
| 10. Costs | 21 |
| 11. Final Results | 222 |
| 12. Future Work | 244 |
| 13. References | 255 |
| 14. Appendix | 277 |

## Table of Figures

| Figure 1: BMS Block Diagram | 10 |
| - | - |
| Figure 2: Pre-charge/Discharge Circuit | 11 |
| Figure 3: Cell Monitoring Circuit | 12 |
| Figure 4: BQ79656 Functional Block Diagram | 13 |
| Figure 5: Distributed BMS View | 15 |
| Figure 6: Breadboard Test | 17 |
| Figure 7: Original GANTT Chart Responsibilities | 19 |
| Figure 8: Final GANTT Chart Responsibilities | 20 |
| Figure 9: Cell Balancing Graph | 23 |
| Figure 10: Original GANTT Chart | 27 |
| Figure 11: Final GANTT Chart | 27 |
| Table 1: Total Cost Spreadsheet | 28 |
| Table 2: Cost of Producing 10k Distributed BMS PCBs | 32 |
| Table 3: Cost of Producing 10k Precharge/Discharge PCBs | 34 |
| Table 4: Cost of Producing 10k Microcontrollers | 34 |

## 1. Statement of Work

## John Link

My primary responsibility was designing the precharge discharge schematic and the corresponding PCB. This task required a deep understanding of electrical circuits and precision in layout design, ensuring that our system would function efficiently and safely. Additionally, I was actively involved in the design and review of the BMS slave. This aspect of the project was particularly challenging, requiring meticulous attention to detail and a thorough understanding of battery management principles. Beyond the hardware design, I also took on the significant task of writing the embedded C code for the microcontroller. This required not only programming skills but also a keen understanding of how the software interacts with and controls the hardware components. My role was critical in integrating various parts of our project, and I am proud of the contribution I made towards achieving our objectives.

## Silas Schroer

In my role, I led the design of the Battery Management System (BMS) cell monitoring circuit, with a focus on safety. I significantly contributed to the Printed Circuit Board (PCB) design, ensuring that the layout was efficient, met all technical requirements, and fit within the tight mechanical constraints of the battery pack design. I acted as the main point of contact during technical discussions with Texas Instruments (TI) engineers, which was crucial in troubleshooting and gaining a deeper understanding of our hardware. Additionally, I assisted in the PCB assembly and validation process, conducting thorough tests to ensure the functionality and reliability of the system.

## Asad Shamsiev

I aided in selecting the original microcontroller, the STM32. I also read through the BQ79656 datasheet comprehensively and built a test circuit (across 5 breadboards) to test its functionality. This was a difficult task, because it seemed as if the entire circuit would have to be built to turn the chip on. Additionally, I wrote a Flask API, so I could send voltage information to my computer via Arduino code, which I contributed to. Finally, I made the web interface that displays the information received on the Flask API. This was part of our video demonstration submission.

## Gabriel Binning

Throughout the design of the distributed BMS PCB, I aided in circuit design, design rule checking, and part checking. For the circuit design, I added cell sensing modules to the circuit schematic. For the design rule checking, I compiled a list of Formula Rules and IPC standards that pertained to our project and ensured they were added to the design rules and strictly followed. Finally, I helped verify that the parts we were going to place on the PCB were rated for the voltages, currents, and power that were going to be going through them. Concurrently, but mostly after the PCB was fully designed, I started working on communications with the chip and our microcontroller. This involved using an AD2, various microcontrollers, and software programs to send and receive UART data to and from the BQ chip. This work also involved analyzing communication software developed by TI for the chip, and outlining how we could implement features of the provided software.

## 2. Abstract

Our project pertains to the creation of a battery management system (BMS) for an electric race vehicle. BMSs are used in the automotive industry to extend the battery life of electric vehicles through conditioning of the cells in the battery pack. Battery packs consist of lithium-based battery cells, often in series, with some form of casing and cooling system to preserve the units' health. A BMS complements these components and acts as a master controller. If there are disparities in a module, the BMS balances voltage and state of charge (SoC) via cell balancing, the use of switching transistors and diodes to balance out measurements in a module [1]. In our project, we developed a BMS tailored for the intense heat and velocity conditions of competitive racing.

## 3. Background

Initially, the BatteryBoyz had multiple ideas for the course project, ranging from tZhe electrification of bikes to AI-driven smart locks. However, after considering the strengths of our collective, and assessing the limitations of Virginia Motorsports's Formula SAE program, we converged on this BMS project. Our goal is to help the organization transfer its success in the IC competition to the EV competition. One of the biggest goals for the FSAE team is to finish the Electric Endurance event, which involves driving at high speeds for over 30 minutes straight, without recharging [17]. To help achieve this goal, we designed a specialized BMS to manage cell charge distribution and ensure efficient battery operation, so that the battery will last in the short term as well as the long term.

Both John Link and Silas Schroer are heavily involved in Virginia Motorsports, with John Link serving as Software &amp; Electric Vehicle Development Lead, and Silas as FSAE Low Voltage Electrical Lead. Gabriel Binning also has a history in embedded systems &amp; circuity, and is ambitiously pursuing a minor in Biology to strengthen his understanding of complex systems. Asad Shamsiev has hoards of experience in software development and a foundational understanding of hardware. At the University of Birmingham, Asad worked with BMS modeling in MATLAB and Simulink in his graduate Electrical Power Systems course. Additionally, all 4 group members have a notable amount of experience in the industry of computing &amp; hardware, via research and relevant internships.

Since electric racing vehicles are a (relatively) new phenomenon, research on student-built BMS's is sparse. However, some relevant projects have been completed in recent years. One of them, coming from the Slovak University of Technology in Bratislava, had a similar end goal: to tailor a BMS for a student-built race car. The project leads designed 2 PCBs: one for the BMS, and the other for the low voltage monitoring system. Similarly, their vehicle already had a battery box, so they had to embed their BMS into the existing current design. For cell balancing, however, they opted for more advanced methods of SoC estimation (e.g. Kalman filters), avoiding simpler methods, such as open-circuit voltage (OCV) [3]. Plus, their report did not specify design choices made to account for high-temperature conditions.

Another related project is from the Pimpri Chinchwad College of Engineering in Pune, India. Similarly, the project leads were optimizing their vehicle's battery systems for India's annual Formula Bharat. Much like the Slovakian project, they chose a BMS/slave design, but they opted for the simpler Coulomb Counting Method for SoC/energy estimation [4]. However, their project pertained to the design of a complete, grand battery system, with the BMS aspect only being a subsect of their project. They used far more complex tools-e.g. insulation monitoring devices (IMDs), isolation relays, etc.-than we'll need.

Finally, another related project was conducted at the University of Las Palmas de Gran Canaria in Spain. This group of electronic engineers made a BMS for an electric motorbike and designed 3 PCBs: one for the BMS, another for the "burnt" resistors (those releasing heat as a result of the passive cell balancing), and another for the CAN bus [8]. We used 2 primary PCBs: a main control boardt, and the BMS itself. Additionally, our final design is more replicable, enabling it to support far more battery cells. This is because we need to fuel an entire car, as opposed to a relatively smaller motorbike.

Overall, there were not many related projects. The ones we found had similar goals as us, but our more complicated &amp; expensive circuit design, as well as our custom specifications (e.g. needing to tolerate high heat &amp; velocities), make our project one-of-a-kind. However, the examples above were still valuable resources, as they gave us ideas on how to construct our PCBs and test them.

Finally, as touched upon above, each member of the group has a strong base in electronics and software. The CpE section of our group-John, Asad, and Gabe-have taken Operating Systems, Program &amp; Data Representation, Computer Architecture, the ECE Fundamentals series, and other related CS/ECE electives (such as Digital Signal Processing). Silas, the sole EE representative, has dived deeper into electrical classes, taking courses like VLSI, Electromagnetic Fields, and Digital Logic Design. Finally, John has been a part of UVA's Autonomous Vehicles team since his 1st-year. Combined with his heavy involvement in Virginia Motorsports, this project idea was right up his alley, so his passion and expertise played a huge role in our group's success.

## 4. Societal Impact Constraints

The main group affected by our BMS is the members of Virginia Motorsports, namely the students physically operating the car &amp; working on the car. This is because our project is the primary feature of the car's battery pack. If it does not operate correctly under high-stress racing conditions, the battery could become unstable and activate the shutdown circuit, which would stop the car and end the race.

We tried to mitigate this risk via several design choices. The web interface, if correctly wired to the car, constantly informs the driver about the battery's conditions, so they may act to prevent dangerous situations. The shutdown circuit also protects the driver, as it prevents the battery from operating in extreme conditions, where it could catch fire or explode. Therefore, the negative effects of losing power have been minimized.

The other group affected, the students working on the car, have the potential to accidentally touch a high-voltage trace in the midst of operation. For this reason, our PCBs have appropriate warning labels ("HIGH-VOLTAGE: DANGER!") to dissuade members from touching them. In addition, all of our PCB's are coated and use shrouded connectors to ensure that there is almost no possibility of engineers causing shorts by working on the PCBs. The final design also wraps the battery pack in an electrically insulated container. Overall, we had safety at the forefront of our minds while designing the BMS.

Furthermore, there are controversies surrounding lithium-ion batteries, which we made extensive use of. Major companies, such as Apple, Tesla, and Microsoft, have been accused of enabling child labor in the mines of DR Congo [13]. Finding a supplier for the pouch cell design that we wanted to use was a struggle, as the designs are relatively new, and the global demand for battery cells is high. We also wanted to find used cells if possible, because of the child labor concerns and because the process of producing new battery cells is unsustainable. We ended up finding a reputable distributor based in China that was able to supply us with used pouch cells within the timeframe of this capstone project, which enabled us to build a test battery pack.

Finally, improper disposal of lithium-ion batteries can hurt the local Charlottesville community. The cathodes of lithium-ion batteries are made of cobalt, which is incredibly toxic to humans. Its mining has been linked to numerous birth defects in DR Congo. Additionally, it can pollute both water and soil [13]. Another study was done on the toxicity of lithium-ion batteries, notably from disposed smartphones. Copper and aluminum, both of which are toxic to humans, are often used as conductors in these products. There are a plethora of other toxic chemicals as well, albeit in trace amounts, such as vanadium, lead, and thallium. One smartphone's battery had 33.10 mg/L

of lead, eclipsing the nationally set 5 mg/L limit [6]. Therefore, we have employed the services of Call2Recycle, a climate-responsible organization, for the disposal of dysfunctional batteries [18].

## 5. Physical Constraints

## Cost Constraints

A major constraint was cost. The allotted $500 from Professor Barnes was not enough for our chosen components and the assembly of our multi-layered PCBs. Thankfully, because this project was done conjunctly with Virginia Motorsports, we were able to receive club funding. Therefore, cost, while still a barrier, was not a crippling constraint. Still, we were unable to pay a PCB manufacturer to populate our actual BMS PCB with our components, as our quoted price was over $3000. So, we had to solder these components carefully, as to prevent frying our components and the BQ79656.

## Design and Manufacturing Constraints

Another constraint was the availability of one of our main components. The BQ79600 was a crucial piece of our original design, as it was made specifically to communicate with multiple, stacked BQ79656 components [19]. It could relay the information over UART for our microcontroller's use.

However, this component got back-ordered, and its arrival was delayed to late December. To fix this issue, we had to put the functionality of the communication chip onto the microcontroller, which took a lot of extra coding. This issue, however, was quickly solved, as we reached out to Texas Instruments in order to obtain sample code that allowed our microcontroller to communicate with our BQ79656, in lieu of the missing BQ79600.

## Tools Utilized

We used a variety of tools. Some, we were familiar with: Visual Studio Code and Waveforms. These tools were used to collaborate on code. Gabe and Asad used VS Code's LiveShare feature in order to work on communications code concurrently, enabling them to establish communication between the microcontroller and the BQ79656. WaveForms was used due to our group's familiarity with it, as all of us had used it in ECE 2660: ECE Fundamentals II. Furthermore, we used multimeters to verify the voltages and currents being applied in our breadboards and, later, PCBs. This was crucial in establishing communication between components, as communication could only occur if correct currents were being supplied to specific pins.

Some tools were new, Altium and BQAutoEval being the most prominent. We decided to use Altium over NI Multisim, because of its widespread industry usage and cloud support. Altium was difficult to learn, and we had many problems. A big problem was our licenses expiring, individual design changes not saving to the server, and creating rule-abiding PCB traces and footprints. These problems were ultimately fixed, but they caused setbacks. The last tool, BQAutoEval, was used to test communication with the BMS chips. We never got this tool to work properly because it was designed to communicate with the main communication module, the BQ79600, and not the individual BMS chips. Thankfully, with the combination of WaveForms and our C code, we were able to test communications without it.

## 6. External Standards

We had to adhere to the Institute of Printed Circuits (IPC) standards on PCB design, the Formula Society of Automotive Engineers (FSAE) requirements on high-voltage circuitry, and UVA's custom high-voltage regulations.

Most of the relevant IPC standards overlapped with FSAE requirements, especially the trace width and spacing requirements. FSAE standards, however, were generally more strict and thorough than those of the IPC. For example, FSAE standards required that we provide galvanic isolation between battery packs, not solder in the middle of high current paths, and install overcurrent protection features. We focused on standards pertaining to batteries and high voltages, though, as the installation of the BMS in the vehicle, amongst other car-based responsibilities, is beyond the scope of this project. Virginia Motorsports members are aware of this limitation and will be sure to follow the relevant standards to see our design succeed on the track [17].

John and Silas also had to complete high-voltage training with UVA EHS. This training took place in person over the course of 3 hours. Topics covered in this training included proper PPE and arc flash safety. Based on their professional recommendations, we have scoped out articles of PPE, namely high-voltage insulation gloves, to work on the battery.

Moreover, for the battery pack itself, we had to follow numerous International Electrotechnical Commission (IEC) standards, namely, IEC 62281 [20]. Their standards pertained to ideal packaging and operating conditions of lithium batteries. We had to ensure our numbers did not go out of their predefined ranges. For example, the batteries have to remain in a stable range of (around) 20 centigrade to 60. Otherwise, if the temperature gets too low, lithium plating will occur. On the flip side, if it gets too high, thermal runaway will occur. Both of these are dangerous, harmful to battery operations, and can lead to premature battery death. Furthermore, if voltage gets too high, it can also lead to lithium plating [5].

Finally, another formal regulation we had to follow is IEC 61508-1:2010, which pertains to the safety of "electrical/electronic/programmable electronic safety-related systems". It is considered the gold standard for addressing dangers associated with electrical safety systems, and it tries to eliminate any potential hazard [15]. However, whereas IEC 61508 is more general, ISO 26262 applies to electronic safety systems in road vehicles specifically. Much like IEC 61508, it tries to eliminate hazards at their sources, from all phases of the product development lifecycle [16]. We used all of these formal regulations above to approach our designs with the intent to maximize our success.

## 7. Intellectual Property Issues

Overall, our project does not meet the criteria for patentability. A significant portion of our communication software either draws inspiration from or directly incorporates elements from software copyrighted by Texas Instruments (TI). Additionally, our circuit schematic and printed circuit board (PCB) design have been heavily guided by the specifications outlined in TI's BQ79656 datasheet. While our project does feature several unique elements, such as the precharge/discharge circuit, web interface, and test board, we believe these innovations do not represent a substantial departure from existing patents to warrant a new patent.

For instance, our advanced battery module is similar to that of the innovative Kangwoo Lee, an engineer at Samsung. His patent, WO2019013492A1, presents a unique battery module design featuring stacked cells, reminiscent of our own approach. This module integrates heat sinks, insertion holes, and tailor-made battery configurations, where the arrangement of cathodes and electrodes is optimized for peak power output [21]. Furthermore, the field of battery management systems is similarly dense. A standout contribution comes from Ivan Loncarevic at Denmark's Lithium Balance AS. His patent, US20210050731A1, originally filed as a WO patent in 2007, focuses on a microcontroller-based system. This system monitors individual cell voltages and temperatures, and activates a shutdown mechanism if these voltages or temperatures exceed preset limits, utilizing sensing slaves and current amplifiers for this purpose [22].

Other designs, such as Shandong Luneng Software Technology Co., Ltd, significantly surpass ours in complexity. Their battery management system includes innovative features like integrated fire detectors and sensors that anticipate and react to fires/explosions. Additionally, it monitors carbon monoxide levels to maintain them within predefined standards, and it also is capable of predicting thermal runaway through the detection of alkaline gas generation. Given these advanced features, it appears improbable that our design is patentable [23]. Our best bet would be to add a distinguishing feature to our design, to make it unique from the thousands of similar ones. Potentially, we could push efforts toward the web interface, but this is for future Virginia Motorsports members to decide.

## 8. Project Description

## Performance Objectives and Specifications

The BMS can:

1. Successfully monitor temperature and voltage on each cell of the battery pack
2. Successfully cool and dissipate heat throughout the battery pack
3. Perform active cell balancing
4. Keep energy waste below a predefined threshold
5. Relay information about the batteries to the user through a web interface
6. Shut down the battery charging/discharging if conditions exceed temperature/voltage thresholds from user input

Three aspects that have been added are the monitoring of voltage, performing active cell balancing, and shutting down the battery when certain thresholds are met. When we were creating the proposal we did not know that there were chips on the market for monitoring voltage, temperature, and performing cell balancing. This discovery allowed us to increase the complexity of our design and ultimately increase the BMS's features. The shutdown feature was added later in the project as we learned from Formula Team rules that the battery must be connected to a shutdown circuit when the voltages and temperatures reach predefined threshold values. This increased functionality is a safety measure we didn't expect to include during our developmental process but ultimately found pretty easy to implement and it allowed us to prove our threshold values and circuitry were working correctly.

## How It Works

Figure 1: BMS Block Diagram

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_001.png)

The BMS consists of three major components: the pre-charge/discharge circuit, the cell monitoring circuit, and the main control board.

Figure 2: Pre-charge/Discharge Circuit

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_002.png)

The pre-charge/discharge circuit consists of switches and capacitors that allow voltage differences between the battery and the load to be equalized before connection, and to drain voltage from the load when they are disconnected. The precharge portion of this circuit prevents current from rushing out of the battery and overloading the load on initial contact by having the battery charge a capacitor, whose charge is then promptly released onto the connector. This equalizes the voltage of the two sides of the circuit for a brief period, so the connectors for the battery and the load can come into contact without an excessive amount of current. After the load and battery are disconnected, the discharge portion drains the capacitor, allowing the voltage on the load to be zero out, so people can access the car's interior safely.

Figure 3: Cell Monitoring Circuit

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_003.png)

The cell monitoring circuit consists of power regulators, filters, communication buses and a TI BQ79616 chip. This system communicates with the main control unit. If any cells go over a threshold value, a shutdown signal will be sent, which will activate the shutdown circuit, disconnecting the battery from the load/charging port. This circuit also performs active cell balancing for the cells of the battery, increasing the battery's total capacity.

The main control circuit consists of an Arduino Uno R4 microcontroller. This microcontroller communicates with the cell monitoring circuit over UART and relays the information over a CAN bus, which can be used for logging, debugging, and communication throughout the rest of the vehicle's systems. It also sends the voltage data to a web server for a simplified visual that describes the state of all the battery cells. This main control unit can turn the cell monitoring circuit on/off, set the threshold values for voltage and temperature, and initiate cell balancing during charging. This main control unit is necessary, as there will be five stacks of lithium-ion cell stacks in the final vehicle, so there will need to be five monitoring circuits. It acts as a simplified interface between a user and all the battery's cells, although most of the controls will be automated in the final design.

## Technical Details

Figure 4: BQ79656 Functional Block Diagram

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_004.png)

## Distributed BMS PCB

Technical Goals and Implementation

- Cell Monitoring and Balancing:
- Objective: Ensure each cell operates within its safe voltage range.
- Technical Reasoning: By maintaining the voltage of each cell within a specified range, the team aimed to enhance the overall lifespan and efficiency of the battery pack. This balance prevents cell overcharge and deep discharge, which can significantly degrade battery health.
- Design Approach: Implementing active cell balancing, leveraging the BQ79656's integrated balancing transistors, allowed for real-time adjustments in cell voltages. This approach was more efficient than passive balancing, as it minimized energy dissipation and improved the energy transfer between cells.
- Temperature Monitoring:
- Objective: Continuously monitor cell temperature to prevent thermal runaways.
- Technical Reasoning: Temperature monitoring is vital for lithium-ion cells like the AHP8AU1 due to their sensitivity to temperature extremes. Thermal runaways can lead to catastrophic failures, so precise temperature monitoring is crucial for safety.
- Design Approach: Integrating multiple temperature sensors within the cell array and interfacing them with the BQ79656 for real-time temperature data acquisition.
- Communication and Control:
- Objective: Implement a robust communication protocol for real-time monitoring and control.
- Technical Reasoning: Effective communication is key in a BMS to relay cell status information to the central controller for prompt decision-making.
- Design Approach: The team chose a daisy-chained communication setup to streamline data transmission. They employed impedance matching on communication buses to minimize signal reflection and loss, ensuring high fidelity in data transmission.
- Safety Features:
- Objective: Incorporate safety mechanisms like over-voltage, under-voltage, and over-temperature protections.
- Technical Reasoning: Safety mechanisms are crucial to protect the battery and associated systems from extreme operating conditions that could lead to failures or hazards.
- Design Approach: The BMS was programmed to initiate pre-defined safety protocols automatically, like disconnecting the battery from the load or charger in dangerous conditions.

## Role of BQ79656 ASIC: DATASHEET HERE

- Multi-Cell Monitoring:
- Design Choice: Perfect for managing the 16-cell series, providing a compact and efficient monitoring solution.
- High Accuracy:
- Design Choice: Essential for the precision required in monitoring the AHP8AU1 cells, ensuring the longevity and safety of the battery pack.
- Daisy Chain Capability:
- Design Choice: Allowed for scalability in the system and efficiency in communication, reducing the complexity and wiring requirements.
- Integrated Balancing Transistors:
- Design Choice: Enabled active cell balancing, crucial for maintaining cell health and prolonging battery life.
- Communication Protocol:
- Design Choice: Supported robust data transmission, crucial for the real-time decision-making process in the BMS.
- Circuit Design and Implementation:
- Voltage Sense Lines: The team paid meticulous attention to the routing and shielding of voltage sense lines to prevent noise interference, ensuring accurate voltage readings.
- Impedance Matching: Impedance matching on communication buses was a critical design element. It minimized signal degradation over the communication lines, ensuring reliable data transmission.
- Software and Control Algorithms:
- Custom Software: Developed to interface seamlessly with the BQ79656, extracting and processing data for operational decisions.
- Control Algorithms: These were sophisticated, ensuring dynamic balancing of cells, regulation of charge-discharge cycles, and activation of safety protocols under specific conditions.

Figure 5: Distributed BMS View

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_005.png)

## Precharge Discharge

Technical Implementation:

- Circuit Design:
- The circuit includes a high-voltage contactor and a time-delay relay, controlling the precharge and discharge sequences.
- A precharge resistor is incorporated to limit the inrush current during the initial charging phase.
- Time-Delay Relay Integration:
- A time-delay relay was selected for its adjustable delay settings, allowing for precise control over the precharge and discharge timings.
- The relay was configured to close the precharge circuit upon vehicle startup, initiating a controlled charging process.
- Discharge Process:
- The discharge circuit was designed to safely dissipate the residual charge in the capacitors over a large resistor when the vehicle is turned off
- This is connected to a normally closed relay to ensure that in the event of a power failure the capacitors are safely discharged
- Control Logic:
- Custom control logic was implemented in the vehicle's control unit to monitor the operation of the precharge-discharge circuit.

## Software

Technical Implementation:

- Communication:
- The main board communicates with the BMS slave via UART communcation at 1,000,000 baud rate
- A seperate pin on the BMS slave board outputs an error state to let the controller know that something is wrong
- The BMS slave is set to automatically go to sleep in the event of a communication fault
- Monitoring:
- Both cell voltages and cell temperatures are measured onboard the BMS slave and sent to the main board
- Temps and voltages are compared to the limits of the cells at 2Hz and is adjustable
- In the event of out of bounds error the main board will automatically disable the battery pack
- State Machine:
- The state machine uses the conditions of the battery pack to determine the state of the pack

- A ready state enables the precharge circuit and a fault state disables the contactors and dissipates the energy
- Fault Recovery:
- When a fault occurs the software clears the errors and tests again to determine if the fault is still present
- The state machine can enter and exit the fault states safely allowing for

## Test Plans

Our battery module, equipped with 16 cells and terminals for both positive and negative ends, underwent extensive testing to ensure circuit functionality. Initially, we constructed a preliminary circuit on a breadboard, guided by TI's recommended design. This phase presented significant challenges, requiring adjustments in various components, particularly the pull-up resistor placements and values. A notable modification was in the resistors connected to the NPNB pin. Initially, we utilized the S8050 transistor; however, its low heat tolerance led to it being replaced due to overheating issues. Our schematic spanned across five breadboards, meticulously arranged with consistent nodes and interconnected through resistors ranging from 10K to 100K ohms. This setup was instrumental in achieving a stable baud rate. Our experiments revealed that 100 Ohm resistors were optimal for the positive terminals, and a baud rate of 1MBps provided the best performance.

Figure 6: Breadboard Test

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_006.png)

In this setup, we successfully confirmed that the chip was capable of powering on and transmitting signals. Initially, we utilized the USB2ANY interface for direct signal transmission and reception, bypassing the need for MCU code. This process involved leveraging the BQAutoEval program for signal communication. At first, the signals comprised random bits.

However, after a thorough examination of the datasheet, we gained a clear understanding of the sequence order and the significance of each bit. The verification of the chip's power-on capability was a lengthy process, stretching over several weeks, primarily due to inconsistencies in the circuitry. Once we overcame this hurdle and had a comprehensive grasp of the USB2ANY's functionality, we progressed to developing custom code for the MCU to manually interpret the signals. Initially, we encountered challenges with the STM32 microcontroller and consequently shifted to using the Arduino Uno R4. This transition proved beneficial, as our team members found the Arduino platform more user-friendly.

After transitioning to the Arduino platform, our project experienced a significant ease in development. The Arduino's user-friendly code structure and visually appealing Integrated Development Environment (IDE) played a key role in this improvement. Our first step involved writing a basic 'WriteBytes' code to establish communication with the BQ79656 chip. Initially, we received bytes of data that were not immediately understandable, but this marked an important milestone in our progress.

Subsequently, we focused on developing structured commands to periodically read the voltages, specifically at intervals of 197 microseconds, as recommended by the datasheet. These readings were continuously displayed on the terminal. Achieving consistent results within this roundrobin cycle was time-consuming and required precision.

A significant challenge we faced was interpreting the raw data returned by the chip. To resolve this, we reached out to Texas Instruments (TI) for guidance. They advised us on the conversion process, which involved a simple multiplication by 0.17037, particularly for temperature readings. Once we implemented this solution and began receiving coherent data on the Serial Monitor, we could conclusively verify the accuracy of the BQ79656 chip and subsequently the Distrubuted BMS PCB. It consistently read around 3.2V for each terminal, confirming its effectiveness.

The pre-charge/discharge circuit, designed to prevent the batteries from fusing together during shutdown events, was tested using an oscilloscope. We input specific voltage levels into the circuit, simulating operational conditions. We checked that the relay part of the circuit worked, and that the capacitors slowly converged towards the input's value, which it did. It did not allow for high inrush currents, which is what we were looking for. We also checked that, when a shutdown signal was sent, that the capacitors' voltages were discharged slowly, preventing a sudden decrease in voltage, which can cause welding among the batteries. While we did not test its functionality on an actual car, we can safely assume that our independent testing will translate to a car, given our design is implemented properly.

Testing of all states of the BMS were conducted to ensure reliability of the state machine. In addition, charge, discharge, and steady state monitoring and fault conditions were tested and validated. Fault recovery and handling were tested by unplugging communications, cell voltage taps, and temperature sensors.

## 9. Timeline

Figure 7: Original GANTT Chart Responsibilities

| Get everyone into Altium | Silas | 100% | 8/30/23 | 9/13/23 |
| - | - | - | - | - |
| Set a Meeting Time/Location | Gabe | 100% | 8/30/23 | 9/6/23 |
| Define Detailed Block Diagram | Silas / John | 60% | 9/6/23 | 9/13/23 |
| Pick Battery Cells / Design Battery Pack | Silas / John | 50% | 9/6/23 | 9/13/23 |
| Pick a Microcontroller | Assd | 100% | 9/6/23 | 9/11/23 |
| PCB Research | Gabe / Asad | 30% | 9/6/23 | 9/27/23 |
| Embedded Controller Startup | John | 50% | 9/11/23 | 9/25/23 |
| Detailed Budget | John / Silas | 0% | 9/13/23 | 9/15/23 |
| Design Schematics | Silas / John | 0% | 9/15/23 | 9/29/23 |
| Define Manufacturing Process/Equipment Gabe |  | 20% | 9/15/23 | 9/29/23 |
| Create Test Plan | Gabe / Asad | 0% | 9/11/23 | 9/25/23 |
| Design PCB's | Asad | 0% | 9/29/23 | 10/6/23 |
| Design Physical BMS Layout | John / Gabe | 0% | 9/29/23 | 10/6/23 |
| Pick Connector/Accessory Hardware | Asad / Silas | 0% | 9/29/23 | 10/6/23 |
| Create Poster | Battery Boyz | 0% | 9/27/23 | 10/6/23 |
| Order Accessory Components | Silas | 0% | 10/6/23 | 10/9/23 |
| Assemble Test Bench/Prototype Battery | John / Silas | 0% | 10/6/23 | 10/27/23 |
| Midterm Design Review | Battery Boyz | 0% | 10/10/23 | 10/10/23 |
| PCB Orders | John | 0% | 10/10/23 | 10/24/23 |
| Populate PCBs | Battery Boyz | 0% | 10/24/23 | 10/31/23 |
| Test | Battery Boyz | 0% | 11/1/23 | 11/10/23 |
| Final Project Report | Battery Boyz | 0% | 11/10/23 | 12/5/23 |
| Final Project Demo | Battery Boyz | 0% | 12/5/23 | 12/8/23 |

Figure 8: Final GANTT Chart Responsibilities

| Get everyone into Altium | Silas | 100% | 8/30/23 | 9/13/23 |
| - | - | - | - | - |
| Set a Meeting Time/Location | Gabe | 100% | 8/30/23 | 9/6/23 |
| Define Detailed Block Diagram | Silas / John | 100% | 9/6/23 | 9/21/23 |
| Pick Battery Cells / Design Battery Pack | Silas / John | 100% | 9/6/23 | 9/13/23 |
| Pick a Microcontroller | Asad | 100% | 9/6/23 | 9/11/23 |
| PCB Research | Gabe / Asad | 100% | 9/6/23 | 9/27/23 |
| Embedded Controller Startup | John | 100% | 9/11/23 | 9/25/23 |
| Detailed Budget | John / Silas | 80% | 9/21/23 | 10/21/23 |
| Design Schematics | Silas / John | 90% | 9/23/23 | 10/18/23 |
| Define Manufacturing Process/Equipment | t Gabe | 100% | 9/23/23 | 10/7/23 |
| Create Test Plan | Gabe / Asad | 80% | 9/11/23 | 10/26/23 |
| Design PCB's | John / Silas | 90% | 10/7/23 | 10/22/23 |
| Design Physical BMS Layout | John / Gabe | 50% | 10/7/23 | 10/19/23 |
| Pick Connector/Accessory Hardware | Asad / Silas | 90% | 10/7/23 | 10/17/23 |
| Create Poster | Battery Boyz | 100% | 9/27/23 | 10/6/23 |
| Order Accessory Components | Silas | 75% | 10/17/23 | 10/20/23 |
| Assemble Test Bench/Prototype Battery | John / Silas | 0% | 10/22/23 | 11/12/23 |
| Midterm Design Review | Battery Boyz | 75% | 10/10/23 | 10/11/23 |
| PCB Orders | John | 33% | 10/10/23 | 10/24/23 |
| Populate PCBs | Battery Boyz | 0% | 10/24/23 | 10/31/23 |
| Test PCBs | Battery Boyz | 0% | 11/1/23 | 11/10/23 |
| Final Project Report | Battery Boyz | 0% | 11/10/23 | 12/5/23 |
| Final Project Demo | Battery Boyz | 0% | 12/5/23 | 12/8/23 |

In Figures 7 and 8 we outline the original and final timeline responsibilities and dates. In the appendix we have the full charts but could not include them here while making them readable.

Our original timeline mostly matched our final. However, due to small hiccups and design changes, we had a few single-week additions. One of our major issues was the back-ordering of the BQ79600, so we had to change our designs to allow the microcontroller to take its functionality. This set our PCB and schematic design back a few weeks, as we had to alter our design and write new code.

However, the main discrepancy between our original and final timelines pertains to PCB design. In our original timeline, we planned for our test bench to be completed and operable by midOctober. However, we experienced communication issues with the BQ79656 and were unable to verify functionality. Because of this, we did not know what circuit to put on a PCB, so we had to scramble and breadboard various different circuits to achieve functionality. Thankfully, Silas built out our PCB ahead of time, so as soon as we sorted communications in November, he could make slight alterations, and we could receive our PCBs quickly.

## 10. Costs

In the appendix we outline the total expenditures from our design of the BMS (see Table 1). Overall we spent $872.93 on 16 PCBs, a couple of tools for testing, and about a thousand components, which include resistors, capacitors, relays, header pins, diodes, mounts, and LEDs. The cost does not include the battery packs, wires, or electronic components that were either provided to us or purchased for previous projects. This was a relatively expensive project due to the relatively high cost of high-voltage components and the purchasing &amp; populating of a PCB. Ignoring supplementary costs, the final design of this project cost approximately $304 for two fully populated PCBs and a microcontroller.

We also outlined the costs of manufacturing 10k unit quantities for each of the segments of our BMS in the appendix. The predicted total costs for manufacturing 10k of each segment of our design is $470,192.80 for the distributed BMS PCB (Table 2), $1,645,400.20 for the precharge/discharge PCB (Table 3), and $275,000.00 for the microcontrollers (Table 4). This is a total cost of $2,390,593 to create 10k of our designs at a cost of $239.06 per unit. However, this cost does not include the population of the PCB or connecting wires. Wire is generally inexpensive; however, battery designs could vary, and it is unlikely that the wire we used will be suitable for all use cases. As for populating the PCB, from our initial quotes, it would have cost approximately $3,000 to populate 5 of the distributed BMS PCBs, which would drastically increase our total cost. The more cost-effective option would be to either A) hire people to populate the PCBs or B) simply provide the components and PCBs, and have the customer populate them.

Another thing to consider is that only one microcontroller and pre-charge/discharge PCB will be needed for most applications. However, depending on the quantity of battery packs, a customer could reasonably purchase multiple distributed BMS PCBs. This is the case for our project, as we only created a single distributed BMS PCB, but Virginia Motorsports will need five for the final car design. This would make manufacturing 10k "BMS kits" difficult, as there would be no way to predict how many distributed BMS PCBs to create, along with the 10k pre-charge/ discharge PCBs and microcontrollers.

## 11. Final Results

We created a functional battery management system that performs active cell balancing for a 16 cell battery module of the FSAE car. The scope of this project was to create a working prototype of the final system design that captures all required BMS behavior and validates the full design plan. Our demonstration will include the process of enabling the BMS system. Then, a user input will enable the tractive system, which will cause our pre-charge/discharge circuit to charge up the load side of the high voltage contactors, then close those contactors when voltages are equalized. Throughout this process, our BMS effectively monitors cell voltage from every cell and cell temperature from 8 out of 16 of the cells. Our system wirelessly transmits to a web interface, which displays historical plots of the data as well as fault states. If any faults occur, our main controller is notified and fires a fault output that opens high voltage contactors and discharges the high voltage buses within 15 seconds, so that the system may be worked on safely. The main controller also controls an LED that indicates when there is high voltage on the load side of the high voltage contactors, so that engineers know what systems are safe to work on. In summary, our project represents a working prototype of the High-Voltage System for UVA's first electric racing vehicle, and our designs will be used as the basis for the entire vehicle electrical system.

## Charging

Our code was meticulously designed to enable precise charging of our battery module up to a pre-set maximum level, ensuring the charging process would halt at this point. Adhering to the FSAE operational guidelines, we configured the Over Voltage Threshold (OV\_THRESH) at 4.25 V. This allowed us to achieve a consistent charge level of exactly 4.25 V without exceeding it. We programmed the OV\_THRESH register (address 0x25) to this specific voltage, along with setting the Under Voltage Threshold (UV\_THRESH, address 0x24) at 3V. We determined these voltage ranges to be optimal for our car's performance, in line with the recommendations of the FSAE guidelines. The effectiveness of our configuration is showcased in our demonstration video.

## Discharging

As mentioned in the Charging section, we configured the Under Voltage Threshold (UV\_THRESH) to 3.0V, representing the lowest point the batteries could reach during discharge. Similar to the charging process, upon activating the batteries and initiating the Analog-to-Digital Converter (ADC), we observed that the batteries maintained their discharge level and did not drop below this threshold. Thus, we believe both the discharge and charging goals were successfully met.

## Monitoring, Relaying, Cooling, and Dissipating

Our team confidently met these expectations with an efficient monitoring system. We developed a user-friendly web interface, leveraging Flash and React.js, to display cell voltage readings. This interface was seamlessly integrated with an Arduino Uno R4, equipped with a WiFi module, enabling it to connect to the same network for transmitting HTTP requests. These requests facilitated real-time data display on the front end. Besides cell voltage, our system was also capable of showing temperature readings. However, this feature was not included in the final presentation as temperature variations were minimal and not impactful in our motor's operation during the demo environment.

Regarding cooling, our design includes a robust safety feature: the ability to shut down the circuit or the entire car operation when the temperature exceeds a certain threshold. This is achieved by setting the OTUT\_CTRL, specifically bits 6 to 4, to a predetermined value. This mechanism works in tandem with the GPIO pins connected to thermistors, allowing us to effectively dissipate heat by shutting down the circuit. This accumulation of heat and voltage is safely dissipated through the pre-charge/discharge circuit. Although this approach does not actively dissipate or cool during operation, we consider it a successful strategy. Actively cooling during a vehicle's operation often proves impractical, as the vehicle continuously generates heat. In that context, attempting active heat dissipation is somewhat of a futile effort. This is an example of how our expectations evolved as the semester progressed.

## Active Cell Balancing

Figure 9. Cell Balancing Graph

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_007.png)

To prove that our system was able to perform active cell balancing properly we discharged half of the cells about a volt and kept the other cells at their full capacity. We then reconnected all the cells, hooked the battery up to a charger, and sent a command for the BQ chip to perform active cell balancing. Figure 9 shows the results where it can be seen that the cells that started at a lower voltage were charged before the cells who were already near their capacity. This demonstrates the principle of active cell balancing as charge is distributed to cells that could hold more charge instead of stopping charging once a single cell reaches its individual peak.

## Energy Waste

Addressing energy waste in our battery management system, particularly with the BQ79656, was a complex aspect of our project. Initially uncertain about our chip selection, we ultimately chose the BQ79656, which fit well with our system. But, it presented a challenge in quantifying energy waste. The chip's passive cell balancing releases some energy as heat, a factor we couldn't precisely measure. While we accessed other data like voltage, temperature, and faults with ease, we could not quantify energy loss. However, our focus on writing efficient code, influenced by our learnings in advanced courses (e.g. Operating Systems and Computer Architecture), helped minimize resource usage and thus, waste in the microcontroller. Although direct measurement of energy waste in the chip was unclear, our effective heat and state management (ACTIVE, SHUTDOWN, SLEEP modes) leads us to believe we minimized energy waste to the best of our abilities. So, in the end, even though this criteria evolved and turned obsolete, we still feel we met it.

## 12. Future Work

The first suggestion would be the addition of the BQ79600. We desperately wanted to use it, but its back-order caused us to reshuffle the cards. Its addition should be relatively simple, as its functionality is nearly identical to the microcontroller and can, accordingly, be implemented in its place. However, the microcontroller would then need to be connected to it via its UART pin [19]. Furthermore, for its role, it is the superior component, as it was made specifically to communicate with multiple BQ79656 components. It is low power, especially when in SHUTDOWN or SLEEP mode, and can easily send messages up a chain of BQ79656 components.

Another aspect of future work would be the addition of cooling mechanisms controlled by the BMS for the battery. This would allow the battery to operate under the extreme conditions of racing. We have heat sinks and and shutdown circuits to prevent heat from degrading the PCBs and battery but a cooling solution like a fan that would take hot air away from the battery would allow it to work longer under harsh conditions.

The entire electrical system for UVA's FSAE EV racing vehicle will be based on the design of this BMS. Future work will include several other PCB designs, and an extensive wiring harness to bring together over $40,000 worth of components in a modular, clean, and effective way.

## 13. References

[1] D. Ranawat and M. P. R. Prasad, "A Review on Electric Vehicles with perspective of Battery Management System," in 2018 International Conference on Electrical, Electronics, Communication, Computer, and Optimization Techniques (ICEECCOT), Dec. 2018, pp. 1539-1544. doi: 10.1109/ICEECCOT43722.2018.9001321.

[2] J. Guo, Y. Li, K. Pedersen, and D.-I. Stroe, "Lithium-Ion Battery Operation, Degradation, and Aging Mechanism in Electric Vehicles: An Overview," Energies, vol. 14, no. 17, pp. 122, 2021.

[3] M. Baťa and D. Mikle, "Battery Management System Hardware Design for a Student Electric Racing Car," IFAC-PapersOnLine, vol. 52, no. 27, pp. 74-79, Jan. 2019, doi: 10.1016/j.ifacol.2019.12.736.

[4] N. Tarle, R. Kulkarni, N. Desale, and V. Pawar, "Design of a Battery Management System for Formula Student Electric Race Vehicle," in 2019 5th International Conference On Computing, Communication, Control And Automation (ICCUBEA), Sep. 2019, pp. 1-6. doi: 10.1109/ICCUBEA47591.2019.9128526.

[5] D. Marcos et al., "A Safety Concept for an Automotive Lithium-based Battery Management System," in 2019 Electric Vehicles International Conference (EV), Oct. 2019, pp. 1-6. doi: 10.1109/EV.2019.8892986.

[6] D. H. P. Kang, M. Chen, and O. A. Ogunseitan, "Potential Environmental and Human Health Impacts of Rechargeable Lithium Batteries in Electronic Waste," ACS Publications, May 03, 2013. https://pubs.acs.org/doi/pdf/10.1021/es400614y (accessed Sep. 16, 2023).

[7] "How to design an intelligent battery junction box for advanced EV battery management systems - Automotive - Technical articles - TI E2E support forums," Jan. 04, 2023.

[https://e2e.ti.com/blogs\_/b/behind\_the\_wheel/posts/how-to-design-intelligent-batteryjunction-box-for-advanced-ev-battery-management-systems (accessed Sep. 16, 2023).](https://e2e.ti.com/blogs_/b/behind_the_wheel/posts/how-to-design-intelligent-battery-junction-box-for-advanced-ev-battery-management-systems)

[8] J. Cabrera, A. Vega, F. Tobajas, V. Déniz and H. A. Fabelo, "Design of a reconfigurable Li-Ion Battery Management System (BMS)," 2014 XI Tecnologias Aplicadas a la Ensenanza de la

Electronica (Technologies Applied to Electronics Teaching) (TAEE), Bilbao, Spain, 2014, pp. 1-6, doi: 10.1109/TAEE.2014.6900162. https://ieeexplore.ieee.org/document/6900162 [9] H. Wang, S. Zhang, T. Qiu, H. Liu, L. He, and Z. Wang, "Battery Management System Design for Industrial Manufacture," in 2022 IEEE 25th International Conference on Computer Supported Cooperative Work in Design (CSCWD), May 2022, pp. 1065-1070. doi: 10.1109/CSCWD54268.2022.9776233.

[10] "STM32CubeMX projects | CLion," CLion Help.

https://www.jetbrains.com/help/clion/embedded-development.html (accessed Sep. 19, 2023). [11] W. C. Lee, D. Drury, and P. Mellor, "Comparison of passive cell balancing and active cell balancing for automotive batteries," in 2011 IEEE Vehicle Power and Propulsion Conference, Sep. 2011, pp. 1-7. doi: 10.1109/VPPC.2011.6043108.

[12] "BQ79616-Q1 | Buy TI Parts | TI.com." https://www.ti.com/product/BQ79616-Q1/partdetails/BQ79616PAPRQ1 (accessed Sep. 19, 2023).

[13] "Energies | Free Full-Text | A Paradox over Electric Vehicles, Mining of Lithium for Car Batteries." https://www.mdpi.com/1996-1073/15/21/7997 (accessed Sep. 19, 2023).

[14] N. Wiersma and R. Pareja, "Safety != Security: On the Resilience of ASIL-D Certified Microcontrollers against Fault Injection Attacks," in 2017 Workshop on Fault Diagnosis and Tolerance in Cryptography (FDTC), Sep. 2017, pp. 9-16. doi: 10.1109/FDTC.2017.15.

[15] "IEC 61508-1:2010 | IEC Webstore | functional safety, smart city." https://webstore.iec.ch/publication/5515 (accessed Sep. 19, 2023). [16] 14:00-17:00, "ISO 26262-1:2011," ISO. https://www.iso.org/standard/43464.html (accessed Sep. 19, 2023). [17] Endurance Track &amp; Fuel/Energy Efficiency Event Description - Formula SAE. Formula SAE. (2023, June 8). https://www.fsaeonline.com/Page.aspx?pageid=fa25ca79-3a7a-4b3f803f-7bdddb3b2c57 [18] How to Dispose of Batteries. Home Depot. (n.d.). https://www.homedepot.com/c/ab/how-to-dispose-ofbatteries/9ba683603be9fa5395fab90124a115f1 [19] BQ79600-Q1. Texas Instruments. (n.d.). https://www.ti.com/product/BQ79600-Q1 [20] IEC 62281:2019 - Safety of primary and secondary lithium cells and batteries during transport. International Electrotechnical Commission. (2019, April 10). https://webstore.iec.ch/publication/61994

[21] WO2019013492A1: Battery module and battery pack including same. Google Patents. (2019, January 17).

https://patents.google.com/patent/WO2019013492A1/en?q=(battery+management+system+p cb+electric+vehicle)&amp;oq=battery+management+system+pcb+electric+vehicle&amp;page=3

[22] Loncarevic, I. (2021, February 18). US20210050731A1: Battery management system. Google Patents.

https://patents.google.com/patent/US20210050731A1/en?q=(battery+management+system) &amp;oq=battery+management+system

[23] CN111060821B: Battery management system and method with early warning function of lithium battery fault. Google Patents. (2022, February 25).

https://patents.google.com/patent/CN111060821B/en?q=(battery+management+system)&amp;oq =battery+management+system&amp;page=1

## 14. Appendix

## Timeline

Figure 10: Original GANTT Chart

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_008.png)

Figure 11: Final GANTT Chart

![Image](UVA%20-%20Racing%20BMS%20%28Link%20and%20Schroer%20Capstone%20Report%202024%29_files/img_009.png)

## Cost Breakdowns

| Name | Description | Unit Price | Quantity | Price |
| - | - | - | - | - |
| 08052A221JAT2A | Ceramic Capacitor, Multilayer, Ceramic, 200V, 5% +Tol, 5% -Tol, C0G, 30ppm/Cel TC, 0.00022uF, Surface Mount, 0805 | $0.15 | 20 | $2.92 |
| ERA-3AEB301V | Fixed Resistor, Thin Film, 0.1W, 300ohm, 75V, 0.1% +/-Tol, 25ppm/Cel, Surface Mount, 0603 | $0.21 | 8 | $1.68 |
| GRM033R61A104KE15D | Ceramic Capacitor, Multilayer, Ceramic, 10V, 10% +Tol, 10% -Tol, X5R, 15% TC, 0.1uF, Surface Mount, 0201 | $0.03 | 40 | $1.20 |
| GRM033R61A222KA01D | Ceramic Capacitor, Multilayer, Ceramic, 10V, 10% +Tol, 10% -Tol, X5R, 15% TC, 0.0022uF, Surface Mount, 0201 | $0.01 | 20 | $0.10 |
| GRM155R60J475ME47D | Ceramic Capacitor, Multilayer, Ceramic, 6.3V, 20% +Tol, 20% -Tol, X5R, 15% TC, 4.7uF, Surface Mount, 0402 | $0.10 | 8 | $0.80 |
| GRM155R71H103KA88D | Ceramic Capacitor, Multilayer, Ceramic, 50V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.01uF, Surface Mount, 0402 | $0.01 | 40 | $0.48 |
| GRM188R71C474KA88D | Ceramic Capacitor, Multilayer, Ceramic, 16V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.47uF, Surface Mount, 0603 | $0.05 | 100 | $5.20 |
| GRM188R71E224KA88D | Ceramic Capacitor, Multilayer, Ceramic, 25V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.22uF, Surface Mount, 0603 | $0.10 | 8 | $0.80 |
| 824521151 | WE-TVSP SMT Power TVS Diode, DO-214AA, Bidirectional, 600W, 15VDC | $0.54 | 8 | $4.32 |
| CRCW060350R0FKEA | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 50ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.04 | 20 | $0.84 |
| GRM55DR72E105KW01L | Ceramic Capacitor, Multilayer, Ceramic, 250V, 10% +Tol, 10% -Tol, X7R, 15% TC, 1uF, Surface Mount, 2220 | $1.05 | 16 | $16.75 |
| FUSE-1A/32V-3 | Fast Acting Fuse, 1 A, 32 V, -55 to 90 degC, 2- Pin SMD, RoHS, Tape and Reel | $1.37 | 20 | $27.34 |
| MMBTA42LT1G | Small Signal Bipolar Transistor, 0.5A I(C), 300V V(BR)CEO, 1-Element, NPN, Silicon, TO-236AB | $0.20 | 10 | $2.00 |
| ERA-3AEB102V | Fixed Resistor, Thin Film, 0.1W, 1000ohm, 75V, 0.1% +/-Tol, 25ppm/Cel, Surface Mount, 0603 | $0.14 | 30 | $4.17 |

| ERJ-1GNF1000C | Fixed Resistor, Metal Glaze/thick Film, 0.05W, 100ohm, 25V, 1% +/-Tol, 200ppm/Cel, Surface Mount, 0201 | $0.03 | 50 | $1.50 |
| - | - | - | - | - |
| ERJ-1GNF10R0C | Fixed Resistor, Metal Glaze/thick Film, 0.05W, 10ohm, 25V, 1% +/-Tol, 200ppm/Cel, Surface Mount, 0201 | $0.03 | 50 | $1.50 |
| ERJ-2RKF1002X | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 10000ohm, 50V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0402 | $0.01 | 50 | $0.45 |
| ERJ-3EKF30R0V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 30ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.02 | 10 | $0.24 |
| BQ79656PAPRQ1 | Crucial BMS ASIC | $19.64 | 2 | $39.28 |
| 662002236022 | WR-MPC3 SMT Male Right Angled Header with Plastic Pegs, pitch 3mm, 2p | $1.32 | 20 | $26.32 |
| 66200411022 | WR-MPC3 THT Male Right Angled Header with Plastic Pegs, pitch 3mm, 4p | $1.04 | 5 | $5.20 |
| BQ79616 BMS Slave |  | $19.78 | 3 | $59.34 |
| 64 Pin Breakout Board |  | $15.79 | 1 | $15.79 |
| Solder Mask for Breakout |  | $11.59 | 1 | $11.59 |
| New STM32 Microcontroller(s) | We're getting 2 of these. 2nd is spare. | $7.96 | 2 | $15.92 |
| BQ79600PWRQ1 |  | $9.81 | 2 | $19.62 |
| KRM55WR71H476MH13L | Metal Terminal Type Multilayer Ceramic Capacitors for Consumer Electronics & Industrial Equipment/KRM Series | $3.84 | 6 | $23.04 |
| SL44-E3/57T | Rectifier Diode, Schottky, 1 Phase, 1 Element, 4A, 40V V(RRM), Silicon, DO-214AB | $0.72 | 6 | $4.32 |
| RF201L2SDDTE25 | Fast Recovery Diode (AEC-Q101 Qualified) | $0.86 | 4 | $3.44 |
| H3FA-A-DC12 | Time Delay & Timing Relays 12VDC 1s-10m Contact SPST-NO+SPST-NC | $85.03 | 1 | $85.03 |
| LI12-1A85 | Reed Relay 12VDC 680Ohm 1A SPST- NO(30x10x10.4)mm THT Dry | $11.63 | 1 | $11.63 |
| DBR71210 | High Voltage relays 10kV & 15kV | $59.43 | 1 | $59.43 |
| LV IN | WR-MPC3 MICRO POWER CONNECTORS 3 | $0.63 | 10 | $6.30 |
| AP101 3K J | Thick Film Resistors - Through Hole 100W 3 Kohm High Power | $10.08 | 3 | $30.24 |
| Impedance Analyzer |  | $31.29 | 1 | $31.29 |

| Precharge Discharge PCB | Purchased from JLCpcb | $16.25 | 1 | $16.25 |
| - | - | - | - | - |
| Test PCB | Purchased from JLCpcb | $18.17 | 5 | $90.86 |
| Final PCB | Purchased from JLCpcb | $7.19 | 10 | $71.87 |
| Precharge Discharge PCB | Purchased from Advanced | $35.00 | 1 | $35.00 |
| KGM21ECG2D221JU | CAP CER 220PF 200V C0G/NP0 0805 | $0.19 | 10 | $1.90 |
| 885012206036 | CAP CER 2200PF 16V X7R 0603 | $0.02 | 10 | $0.21 |
| KGM31HR71E474KU | CAP CER 0.47UF 25V X7R 1206 | $0.13 | 50 | $6.50 |
| C0805C103K1RAC7210 | CAP CER SMD 0805 .01UF 100V X7R | $0.05 | 10 | $0.45 |
| C0603C105K4RAC7867 | CAP CER 1UF 16V X7R 0603 | $0.06 | 10 | $0.63 |
| CC0603KRX7R7BB104 | CAP CER 0.1UF 16V X7R 0603 | $0.04 | 15 | $0.57 |
| C0805C224K1RAC7800 | CAP CER 0.22UF 100V X7R 0805 | $0.29 | 5 | $1.45 |
| C0603C475K8PAC7867 | CAP CER 4.7UF 10V X5R 0603 | $0.18 | 10 | $1.77 |
| PESD1CAN,215 | TVS DIODE 24VWM 70VC TO236AB | $0.34 | 10 | $3.43 |
| LTSTC170KGKT | LED GREEN CLEAR SMD | $0.16 | 10 | $1.63 |
| FCX495TA | TRANS NPN 150V 1ASOT89-3 | $0.36 | 10 | $3.58 |
| ERJ-3EKF30R0V | RES SMD 30OHM 1% 1/10W 0603 | $0.03 | 10 | $0.27 |
| ERJ-3EKF1000V | RES SMD 100OHM 1% 1/10W 0603 | $0.03 | 20 | $0.54 |
| ERJ-3GEYJ100V | RES SMD 10OHM 5% 1/10W 0603 | $0.03 | 20 | $0.52 |
| ERJ-3EKF1002V | RES SMD 10KOHM 1% 1/10W 0603 | $0.03 | 15 | $0.41 |
| CRCW1206200RFKEA | RES SMD 200OHM 1% 1/4W 1206 | $0.05 | 10 | $0.47 |
| CRCW06031K00FKEA | RES SMD 1KOHM 1% 1/10W 0603 | $0.03 | 10 | $0.26 |
| ERJ-6ENF1003V | RES SMD 100KOHM 1% 1/8W 0805 | $0.05 | 10 | $0.47 |
| ISO7742QDWQ1 | BGTL ISO 5000VRMS 4CH 16SOIC | $3.87 | 2 | $7.74 |
| 3314G-1-500E | TRIMMER 50OHM 0.25W GW TOP ADJ | $1.65 | 4 | $6.60 |
| 61300511121 | CONN HEADER VERT 5POS 2.54MM | $0.26 | 5 | $1.30 |
| RMCF0603FT1K00 | RES 1K OHM 1% 1/10W 0603 | $0.01 | 15 | $0.20 |
| BQ79656PAPRQ1 | Power Supply Support Circuit, Fixed, 1 Channel, PQFP64 | $19.26 | 2 | $38.52 |
| 08052A221JAT2A | Ceramic Capacitor, Multilayer, Ceramic, 200V, 5% +Tol, 5% -Tol, C0G, 30ppm/Cel TC, 0.00022uF, Surface Mount, 0805 | $0.26 | 4 | $1.02 |
| C1608C0G2E222J080AA | MULTILAYER CERAMIC CHIP CAPACITORS, 1608, Commercial grade, general (Up to 75V) | $0.20 | 4 | $0.80 |

| 12063C474KAT2A | Ceramic Capacitor, Multilayer, Ceramic, 25V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.47uF, Surface Mount, 1206 | $0.03 | 34 | $0.85 |
| - | - | - | - | - |
| C0805C103K1RAC7210 | Ceramic Capacitor, Multilayer, Ceramic, 100V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.01uF, Surface Mount, 0805 | $0.10 | 1 | $0.10 |
| Capacitor 1uF +/- 10% 16V 0603 | Chip Capacitor, 1 uF, +/- 10%, 16 V, 0603 (1608 Metric) | $0.10 | 4 | $0.40 |
| CC0603KRX7R7BB104 | Ceramic Capacitor, Multilayer, Ceramic, 16V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.1uF, Surface Mount, 0603 | $0.02 | 10 | $0.16 |
| C0805C224K1RACTU | Ceramic Capacitor, Multilayer, Ceramic, 100V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.22uF, Surface Mount, 0805 | $0.04 | 1 | $0.04 |
| Capacitor 4.7µF +/-20% 10V 0603 | Chip Capacitor, 4.7µF +/-20%, 10V, 0603, Thickness 1 mm | $0.03 | 1 | $0.03 |
| 662102136022 | WR-MPC3 SMT Male Right Angled Header with Snap-In Plastic Pegs, pitch 3mm, 2p | $2.76 | 2 | $5.52 |
| PESD1CAN,215 | Diode ESD (Uni-directional) | $0.38 | 2 | $0.75 |
| LTST-C170KGKT | Single Color LED, Green, Water Clear, 1.4mm | $0.32 | 1 | $0.32 |
| 0451001.NRL | LITTELFUSE - 0451001.NRL - Fuse | $1.44 | 1 | $1.44 |
| 0459.500UR | Surface Mount Fuses 125V .5A Fast Acting | $0.61 | 17 | $10.37 |
| 61300511121 | WR-PHD Pin Header, THT, Vertical, pitch 2.54mm, 1 Row, 5P | $0.26 | 1 | $0.26 |
| 66200211122 | WR-MPC3 THT Male Vertical Header, pitch 3mm, 2p | $0.28 | 8 | $2.24 |
| 3314G-1-500E | Trimmer, Cermet, 0.25W, 50ohm, 300V, 20% +/-Tol, -100,100ppm/Cel, 1 Turn(s), 2018 | $1.31 | 4 | $5.24 |
| FCX495TA | Transistor BJT NPN | $0.46 | 1 | $0.46 |
| ERA-3AEB102V | Fixed Resistor, Thin Film, 0.1W, 1000ohm, 75V, 0.1% +/-Tol, 25ppm/Cel, Surface Mount, 0603 | $0.14 | 10 | $1.39 |
| ERJ-3EKF30R0V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 30ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.10 | 1 | $0.10 |
| ERJ-3EKF1000V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 100ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.01 | 17 | $0.10 |
| ERJ-3GEYJ100V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 10ohm, 75V, 5% +/-Tol, 200ppm/Cel, Surface Mount, 0603 | $0.01 | 17 | $0.10 |

Table 1: Total Cost Spreadsheet

| ERJ-3EKF1002V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 10000ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.01 | 8 | $0.05 |
| - | - | - | - | - |
| CRCW1206200RFKEA | Fixed Resistor, Metal Glaze/thick Film, 0.25W, 200ohm, 200V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 1206 | $0.10 | 1 | $0.10 |
| CRCW06031K00FKEA | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 1000ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.10 | 1 | $0.10 |
| Resistor 100k +/-1% 0805 125 mW | Chip Resistor, 100 KOhm, +/- 1%, 0.125 W, -55 to 155 degC, 0805 (2012 Metric) | $0.01 | 2 | $0.02 |
| Arduino R4 |  | $27.50 | 1 | $27.50 |
|  |  |  | Total | $872.93 |

| Distributed BMS PCB - Name | Distributed BMS PCB - Description | Distributed BMS PCB - Unit Price | Distributed BMS PCB - Quantity (x10000) | Distributed BMS PCB - Price |
| - | - | - | - | - |
| BQ79656PAPRQ1 | Power Supply Support Circuit, Fixed, 1 Channel, PQFP64 | $11.9 6 | 20000 | $239,107.40 |
| 08052A221JAT2A | Ceramic Capacitor, Multilayer, Ceramic, 200V, 5% +Tol, 5% -Tol, C0G, 30ppm/Cel TC, 0.00022uF, Surface Mount, 0805 | $0.06 | 40000 | $2,373.20 |
| C1608C0G2E222J080AA | MULTILAYER CERAMIC CHIP CAPACITORS, 1608, Commercial grade, general (Up to 75V) | $0.04 | 40000 | $1,450.40 |
| 12063C474KAT2A | Ceramic Capacitor, Multilayer, Ceramic, 25V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.47uF, Surface Mount, 1206 | $0.05 | 340000 | $18,210.40 |
| C0805C103K1RAC7210 | Ceramic Capacitor, Multilayer, Ceramic, 100V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.01uF, Surface Mount, 0805 | $0.01 | 10000 | $113.80 |
| Capacitor 1uF +/- 10% 16V 0603 | Chip Capacitor, 1 uF, +/- 10%, 16 V, 0603 (1608 Metric) | $0.02 | 40000 | $785.20 |
| CC0603KRX7R7BB104 | Ceramic Capacitor, Multilayer, Ceramic, 16V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.1uF, Surface Mount, 0603 | $0.01 | 100000 | $547.00 |
| C0805C224K1RACTU | Ceramic Capacitor, Multilayer, Ceramic, 100V, 10% +Tol, 10% -Tol, X7R, 15% TC, 0.22uF, Surface Mount, 0805 | $0.07 | 10000 | $700.70 |
| Capacitor 4.7µF +/-20% 10V 0603 | Chip Capacitor, 4.7µF +/-20%, 10V, 0603, Thickness 1 mm | $0.21 | 10000 | $2,100.00 |
| 662102136022 | WR-MPC3 SMT Male Right Angled Header with Snap-In Plastic Pegs, pitch 3mm, 2p | $0.01 | 20000 | $102.50 |
| PESD1CAN,215 | Diode ESD (Uni-directional) | $0.08 | 20000 | $1,671.60 |
| LTST-C170KGKT | Single Color LED, Green, Water Clear, 1.4mm | $0.05 | 10000 | $516.50 |
| 0451001.NRL | LITTELFUSE - 0451001.NRL - Fuse | $0.57 | 10000 | $5,697.70 |
| 0459.500UR | Surface Mount Fuses 125V .5A Fast Acting | $0.65 | 170000 | $111,132.40 |

Table 2: Cost of Producing 10k Distributed BMS PCBs

| 61300511121 | WR-PHD Pin Header, THT, Vertical, pitch 2.54mm, 1 Row, 5P | $0.13 | 10000 | $1,280.00 |
| - | - | - | - | - |
| 66200211122 | WR-MPC3 THT Male Vertical Header, pitch 3mm, 2p | $0.21 | 80000 | $16,560.00 |
| 3314G-1-500E | Trimmer, Cermet, 0.25W, 50ohm, 300V, 20% +/-Tol, -100,100ppm/Cel, 1 Turn(s), 2018 | $0.78 | 40000 | $31,108.00 |
| FCX495TA | Transistor BJT NPN | $0.14 | 10000 | $1,378.70 |
| ERA-3AEB102V | Fixed Resistor, Thin Film, 0.1W, 1000ohm, 75V, 0.1% +/-Tol, 25ppm/Cel, Surface Mount, 0603 | $0.03 | 100000 | $3,167.00 |
| ERJ-3EKF30R0V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 30ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.01 | 10000 | $64.20 |
| ERJ-3EKF1000V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 100ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.00 | 170000 | $787.10 |
| ERJ-3GEYJ100V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 10ohm, 75V, 5% +/-Tol, 200ppm/Cel, Surface Mount, 0603 | $0.00 | 170000 | $719.10 |
| ERJ-3EKF1002V | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 10000ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.01 | 80000 | $406.40 |
| CRCW1206200RFKEA | Fixed Resistor, Metal Glaze/thick Film, 0.25W, 200ohm, 200V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 1206 | $0.01 | 10000 | $110.50 |
| CRCW06031K00FKEA | Fixed Resistor, Metal Glaze/thick Film, 0.1W, 1000ohm, 75V, 1% +/-Tol, 100ppm/Cel, Surface Mount, 0603 | $0.01 | 10000 | $53.50 |
| Resistor 100k +/-1% 0805 125 mW | Chip Resistor, 100 KOhm, +/- 1%, 0.125 W, -55 to 155 degC, 0805 (2012 Metric) | $0.04 | 20000 | $749.40 |
| Final PCB | Purchased from JLCpcb | $2.93 | 10000 | $29,300.10 |
|  |  |  | Total | $470,192.80 |

Table 3: Cost of Producing 10k Precharge/Discharge PCBs

| Precharge/Discharge PCB - Name | Precharge/Discharge PCB - Description | Precharge/Discharge PCB - Unit Price | Precharge/Discharge PCB - Quantity (x10000) | Precharge/Discharge PCB - Price |
| - | - | - | - | - |
| KRM55WR71H476MH13L | Metal Terminal Type Multilayer Ceramic Capacitors for Consumer Electronics & Industrial Equipment/KRM Series | $1.98 | 60000 | $118,532.40 |
| SL44-E3/57T | Rectifier Diode, Schottky, 1 Phase, 1 Element, 4A, 40V V(RRM), Silicon, DO-214AB | $0.32 | 60000 | $19,289.40 |
| RF201L2SDDTE25 | Fast Recovery Diode (AEC-Q101 Qualified) | $0.32 | 40000 | $12,874.80 |
| H3FA-A-DC12 | Time Delay & Timing Relays 12VDC 1s-10m Contact SPST-NO+SPST-NC | $67.13 | 10000 | $671,328.00 |
| LI12-1A85 | Reed Relay 12VDC 680Ohm 1A SPST-NO(30x10x10.4)mm THT Dry | $8.57 | 10000 | $85,685.90 |
| DBR71210 | High Voltage relays 10kV & 15kV | $52.45 | 10000 | $524,462.00 |
| LV IN | WR-MPC3 MICRO POWER CONNECTORS 3 | $0.52 | 100000 | $52,400.00 |
| AP101 3K J | Thick Film Resistors - Through Hole 100W 3 Kohm High Power | $4.72 | 30000 | $141,527.70 |
| Precharge Discharge PCB | Purchased from JLCpcb | $1.93 | 10000 | $19,300.00 |
|  |  |  | Total | $1,645,400.20 |

Table 4: Cost of Producing 10k Microcontrollers

| Main Communication Board - Name | Main Communication Board - Description | Main Communication Board - Unit Price | Main Communication Board - Quantity (x10000) | Main Communication Board - Price |
| - | - | - | - | - |
| Arduino R4 | Microcontroller | 27.5 | 10000 | $275,000.00 |
|  |  |  | Total | $275,000.00 |
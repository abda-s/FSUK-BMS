<!-- Converted from PCCOE Pune - Design of BMS for FS Electric Race Vehicle (Conference Paper).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

## Design of a Battery Management System for Formula Student Electric Race Vehicle

Niranjan Tarle Electronics and Telecommunication PCCOE Pune, India tarleniranjan98@gmail.com

Nainesh Desale Electronics and Telecommunication PCCOE Pune, India naineshdesale9@gmail.com

Abstract-Formula Student is an International student design competition, a platform for students to use their design, manufacturing knowledge and management skills to solve complex race car engineering challenges. The students are tasked to design and build a single-seater open cockpit, formulastyle race car. Formula student is not just about designing a race car, students are also exposed to the challenges of project and resource management, budget planning and teamwork. To keep pace with the changing face of the automotive industry i.e. the electric powertrains, Formula Student has evolved as well with the introduction of Formula Student Electric competition. Lithium Ion batteries with their high energy density and power density are an appealing solution for people trying to build compact and lighter battery packs but if they are used outside of their safe area of operation, cell starts degrading. A battery monitoring and management system is a necessity to make the most of this amazing cell chemistry and ensure the safety of the car as well as surrounding.

Keywords- Battery management system (BMS), Electric Vehicles (EV), Formula Student (FS), Batteries.

## I. INTRODUCTION

The task is to design and build a race car within Formula Student rules which can complete all dynamic events competitively at the competition, notable guidelines being maximum Tractive System voltage should not exceed 600 VDC and maximum electrical power should not exceed 80 KW. The Tractive System and Low Voltage System are galvanically isolated from each other, meaning the insulation resistance between them is &gt;500Ω/V [1]. The 2018 vehicle was driven by "AC-9" a three phase AC induction motor from HI Performance Electric Vehicle Systems (HPEVS). It has a peak power of 40KW, peak torque of 80 Nm and maximum RPM of 7000. The Accumulator consists of A123 systems' 26Ah lithium ion cells (NMC chemistry, see TABLE I).

Rishikesh Kulkarni Electronics and Telecommunication PCCOE Pune, India rishikul99@gmail.com

Vishal Pawar Electronics and Telecommunication K.K.W.I.E.E.R Nashik, India vishalpawar1502@gmail.com

20 such cells are connected in series to get a peak voltage of 84V and nominal voltage of 72V. The cells are arranged in 20s3p configuration, total of 60 cells to get the required current and satisfy the energy requirement of the vehicle. The accumulator is divided into 4 modules having configuration 5s3p which are connected in series using maintenance plugs which can also be used to isolate modules whenever needed. The accumulator has a capacity of 81Ah and total energy of 6.8KWh. The charging time of the accumulator is 4 hrs. In a single charge, the vehicle can travel a distance of 30 Km, with the top speed being 99 kmph. The accumulator is isolated from the rest of the vehicle using two relays called Accumulator Isolation Relays (AIRs) [1]. Both these AIRs are controlled by a shutdown circuit, the race car has a shutdown circuit with power stages and interlock which shutdown the car in 13 different ways out of which one is Battery Management System (BMS) and Insulation Monitoring Device (IMD). Because of their high energy density, power density, low self-discharge, minimal maintenance, high open circuit voltage and quick charging, lithium-ion cells were the first choice [2].

TABLE I CELL SPECIFICATION

| Manufacturer | A123 Systems |
| - | - |
| Nominal Capacity | 26 Ah |
| Max. Voltage | 4.2 V |
| Nominal Voltage | 3.7V |
| Min. Voltage | 2.8V |
| Max. O/P Current | 350A for 10s |
| Nominal O/P Current | 155A |
| Charging Current | 1C |
| Max. Temperature | 55°C |

Fig. 1. Electrical System Block Diagram

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_001.png)

To prevent the lithium-ion cells from working outside their Safe Area of Operation (SOA) they need to be continuously monitored, also due to manufacturing tolerances between different cells, different contact resistances and charging/discharging cycles, the life of cells may degrade or cell may reach it's under voltage threshold before other cells because of which there will always be some unused energy in the accumulator [3].

Battery Management System monitors and measures voltage, current and temperature of cells inside the accumulator, these values are used to calculate the State of Charge (SOC), State of Health (SOH) and Depth of Discharge (DOD) of the accumulator. Texas Instruments' bq76PL455AQ1 is chosen as monitoring IC for the BMS.

## II. DESIGN CONSIDERATIONS

## A. Cell Voltage and Temperature measurement

The device has a built-in 14-bit (Successive approximation) ADC whose results can be converted to 16 bits by oversampling the voltage sense and temperature sensor inputs and averaging the readings. Fig 2. Shows graph of 2 lithium ion cells of capacity 1.5Ah and 1.1Ah discharged at different currents (Plot of Voltage vs. Ah capacity) Referring to the same graph we can see that the voltage of cell drops only by a few mV when cell's capacity is in between 0.1Ah and 0.8Ah (as evident in A123 1.1Ah @ 18A cell) [4]. A 10-bit ADC with reference voltage of Vref = 5.00V has least count of 4.88 mV, a 12-bit ADC with reference voltage of Vref

= 5.00V has least count of 1.22mV, a 14-bit ADC with reference voltage of Vref = 5.00V has least count of 0.30mV, a 16-bit ADC with reference voltage of Vref = 5.00V has least count of 76.23µV.

Fig. 2. Discharge Voltage of Lithium Iron Phosphate [5]

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_002.png)

Thus, a higher resolution ADC will enable measurement of cell voltages and temperature with greater accuracy. A master microcontroller sends request to BMS master board for cell voltage and temperature values. If the cell crosses Overvoltage, Undervoltage, Overtemperature, Undertemperature thresholds, the microcontroller electrically isolates the battery pack from the vehicle by turning off the Accumulator Isolation Relays (AIR). Voltage sense wires are crimped to lugs which are bolted to cell tabs for voltage measurement. Similarly, choosing a proper NTC thermistor required the study of various critical parameters such as temperature, range, accuracy, stability, packaging and noise immunity, these vary according to the niche of application requiring disc type, chip type, epoxy, surface mount and lug type. The scope of this application required NTC lug type thermistors as temperature sensors.

## B. Current measurement

It is wise to choose a noncontact current sensor for current measurements. A shunt resistor in the output path for current calculation can result in heating of the resistor (e.g. braking while accelerating the vehicle) which changes the otherwise constant value of the resistance. This generates inaccurate readings. DHAB S/161 dual channel Hall Effect based current sensor is used for Tractive System current measurement. It measures current flowing through positive pole of battery pack. Channel 2 of sensor measures current up to 800A, where sensor output of 2.5V (if supply voltage = 5V) means 0A of current and 5V output means 800A of current. This gives us output change of 3.12mV/A. Hence a microcontroller with ADC of at least 12-bit resolution is required for measuring current. In case current drawn is greater than that recommended in datasheet, Tractive system is shut-down by turning off the AIRs. A 3.3V and a 5V regulator is integrated within the chip which regulates the output voltage which is used to power the master microcontroller, the chip and current sensor. Hence the BMS, microcontroller and current sensor are part of HV system.

## C. Cell Balancing

During discharge of battery pack the difference in internal resistance, contact resistance of cell tabs and busbar cause unequal drop in voltage across each cell. Similar is the case while charging. The difference between the voltages of two cells can range from a few mV to few volts. E.g.- Lets consider a hypothetical situation where a battery pack of 5 cells with voltages 3.95V, 4.00V, 3.90V, 4.05V, 4.22V respectively. Cell balancing is one solution to counteract these problems. The cell connections are made using aluminium busbars (Cell tabs and busbars are bolted together). No two cells have the exact same internal resistance.

Fig. 3. Difference in cell voltages after charging of the battery

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_003.png)

The BMS wil stop charging as the 5 th cell has charged to its peak voltage, this limits us from charging the battery pack to its full capacity. In a different scenario, consider a battery pack of 5 cells with voltages 3.15V, 3.00V, 3.17V, 2.81V, 3.20V respectively. We cannot discharge the battery pack any further as cell no. 5 has reached its minimum voltage, thus we cannot utilize the energy remaining in the pack [3].

Another problem that arises due to unbalanced cell string is reduced total pack voltage resluting in earlier cut-off of devices on the Tractive System and hence a part of the battery pack's capacity remains unused during discharging. Considering high-voltage batteries with a large number of cells in series, the problem of cell unbalancing is even more pronounced and as a result, the voltage is not even along the cell string. This obligates the need of reliable and accurate cell balancing circuits in applications with more cells.

Fig. 4. Difference in cell voltages after discharging of battery.

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_004.png)

It is evident from above examples that, if the cell voltages had been equal we could have made the optimum use of our battery pack. We can work around this problem by designing a simple circuit for cell voltage equlization.

Fig. 5. Passive Balancing Schematic Diagram

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_005.png)

By shorting the two terminals of a cell using an appropriately sized resistor, it can be discharged and its voltage can be reduced to voltages of other cells. This type of circuit can be achieved using a MOSFET and a discharge resistor as shown in Fig. 1. The resistor (R1) and LED (LED1) act as an active indicator of the balancing process. The balancing circuit is controlled by the BMS controller by sending a HIGH signal to the gate of N channel MOS. For the above circuit, the maximum balancing current is 84mA (I = V / R) which can be increased by decreasing the value of resistor R1.

## III. STATE OF CHARGE (SOC)

Determination of the SOC of a battery is a challenging task which depends on the battery type and on the application where the battery is used. Accurate SOC estimation is one of the main tasks of battery management systems, which will help improve the system performance and reliability, and will also lengthen the lifetime of the battery [4].

According to FS guidelines the BMS should primarily monitor the voltage, temperature and current and shutdown the vehicle if any thresholds are violated (achieved by cutting off the supply voltage to AIRs). SOC gauging is not mandatory but SOC estimate is a crucial parameter that aids the team as well as car to decide how the car should progress in a race i.e. whether to run at maximum power in the 22 km endurance race or limit the power to motor based on SOC value and slowdown but complete the event. The existing methods for SOC estimation can be classified into five different groups - the conventional method, the adaptive filter algorithm, the learning algorithm, the nonlinear observer, and the hybrid algorithm. Out of which conventional method is very common. Conventional method consists of Coulomb Counting (Ampere-hour counting), the Open Circuit Voltage (OCV) method, the impedance and Internal Resistance (IR) method, the electrochemical method, and the modelbased method. Out of these, coulomb counting and voltage method are prominent methods of SOC estimation of Li-ion based batteries [4].

## A. Coulomb counting

Coulomb counting is by far easy and most widely accepted and used SOC estimation method with less computational complexity in contrast to the voltage method. The terms, ampere hour counting or current integration are often synonymously used with Coulomb counting. Coulomb counting works exceptionally well with Li-ion cells that offer high columbic efficiency while managing a low selfdischarge. In Coulomb Counting method the charging or discharging current is integrated over total time of charge or discharging time, respectively.

<!-- formula-not-decoded -->

SOC(0) is initial SOC of the cell and can be calculated by OCV,

Ib is the charging or discharging current at k, if we consider the columbic efficiency (η) then Ib also can be written as (ηIa),

Iloss is the self-discharging current of the cells,

Cn is the nominal capacity of the battery, when the battery is unused then Cn = Cmax and it decreases with time/use.

However, the releasable charge is always less than the stored charge in the charging and discharging cycle. The biggest advantage of the Ah counting method is its low power computation cost, so it is widely used for battery SOC estimation.

## IV. STATE OF HEALTH (SOH)

The typical estimated life cycle of a Lithium-Ion cell is 1000 cycles which decrease in number with every charge and discharge cycle, due to the application of cell outside its SOA the health of the cell reduces. The condition of a cell can be described by the State of Health (SOH) which is the ability to deliver the specified performance. The SOH of a cell is 100% (which corresponds to maximum capacity of the cell) at the time of manufacturing and it decreases over time with use and then reaches to 0%. In simple words SOH is the ratio of maximum capacity of the cell to rated capacity i.e.

<!-- formula-not-decoded -->

Any parameter such as impedance or conductance of a cell which changes with the age of a cell can be used/calculated to estimate the SOH of a cell. There are various methods to estimate the SOH of a cell out of which Open Circuit Voltage (OCV), Coulomb Counting and Kalman Filter are mainly being used. SOH is a relative phenomenon, its value depends upon the condition of new battery, for the same purpose we need to log the data of each cell right from starting [4]. SOH can be calculated from Depth of Discharge and State of Charge from the equation:

<!-- formula-not-decoded -->

Depth of Discharge is:

<!-- formula-not-decoded -->

## V. INSULATION MONITORING

The race car has two voltage systems both having independent voltage sources. The peculiarity of these systems is that only the Low Voltage System has an active conductor directly connected to chassis ground. In an event of a short between high voltage system and low voltage system ground (chassis of vehicle) a leakage current will flow from High voltage system to Low voltage system and isolation is lost between the two, high enough voltage difference will give rise to an arc which might even flow through the air at the point of the fault to create a short circuit. The resulting change in resistance is called the fault resistance. Isolation is checked via monitoring the insulation resistance between Tractive System and Low Voltage System using an Insulation Monitoring Device (IMD). To ensure that the systems are isolated, the resistance between the two has to be high. The IMD used is the Bender A-ISOMETER iso-F1 IR-3203 [5]. The value of the fault resistance is 500 Ω/V. A sample case of fault resistance calculation

Fault Resistance = 500 Ω/V x Maximum TS Voltage = 500 Ω/V x 84V Fault Resistance = 42 kΩ

The IMD is expected to shut the Tractive System off within 30s when the insulation resistance falls below the threshold value. The IMD has three ground pins which are installed at various points of the chassis to increase redundancy. This IMD monitors the condition of insulation on the DC side as well as AC motor side of the powertrain. It generates a unique pulse which is superimposed on the high voltage and its presence is detected in the low voltage systems. The latest measured insulation condition is available as a PWM signal output. The OKHS output, which is galvanically isolated, of the IMD is used to switch off the tractive system.

## VI. INVEHICLE COMMUNICATION

Each BMS module monitors voltage and temperature of 10 cell. The modules are connected to each other in daisy stack configuration. The first module from Top of cell stack is the BMS master and the rest are the slaves. Texas Instruments LAUNCHXL F28379D LAUNCHPAD is used as master controller for the BMS and the master can control multiple slave devices. The LAUNCHPAD is connected via UART only to the BMS master board. The information flow is from the last BMS slave to the BMS master and then to LAUNCHPAD. Each BMS module is isolated from each other.

Fig. 6. BMS Concept

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_006.png)

The baud rate set for UART communication is 250000 bits per second. The BMS uses two differential communication links, one for data and command and the other for faults. The modules can also be configured by connecting the BMS master to the Computer (TI's software for bq76PL455A EVM) using FTDI Serial to USB converter. The LAUNCHPAD communicates with other electronic control units of the vehicle using CAN, sharing vital information such as cell voltages, temperature, current, SOC and faults. The LAUNCHPAD logs the real time cell data in SD card to study battery behavior and gather data for simulation and validation. As stated earlier the LAUNCHPAD, BMS modules, sensors are all part of HV system, so data transmission from HV system to control system and low voltage electronics should be galvanically isolated. Isolation between HV and LV increases safety while working on LVS of vehicle and prevents TS current to enter LVS and also improves noise immunity.

## VII. EXPERIMENTAL SETUP

The proposed BMS design, implemented using the bq76PL455A-Q1 is a battery monitoring and protection device, designed for high-reliability automotive applications. The integrated high-speed, differential, capacitor-isolated communications interface allows up to sixteen bq76PL455AQ1 devices to communicate with a host via a single highspeed Universal Asynchronous Receiver/Transmitter (UART) interface. The PCB is designed keeping the aforementioned features in mind. Highly accurate monitoring and protection, Passive Balancing with external n-FETs, engineered for high system robustness, 1-Mb/s stackable isolated differential-UART, helps achieve high levels of functional safety and support for open wire detection. Since the bq76PL455A-Q1 measures small changes in voltage, care has been taken in the layout of signals to and from the device to avoid coupling noise onto sensitive inputs. The layout of ground and power connections, as well as communication signals has also been made carefully. To ensure the best possible accuracy performance. The Common Mode Chokes are placed close to the daisy-chain cable connector to provide a high-impedance path to common-mode noise as it enters the board. Creation of a good ground plane in the layout is crucial to getting optimal performance from the device.

Fig. 7. Top-view render of the designed BMS PCB

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_007.png)

The renders shown in fig. 7 and fig. 8 provide a realistic view of the assembled PCB from the top and bottom respectively. The fabricated PCB measures an exact 112mm X 86mm of standard FR4 substrate with two signal layers and an option of four layers if two internal power planes are added for noise immunity purposes. Surface mount components of Imperial code 1206 (Metric 3216) were chosen as the package allows for hand soldering in prototype and low volume batches while still being reasonably smaller with the flexibility of pick and place assembly process in high volume production batches.

Fig 8. Bottom-view render of the designed BMS PCB

![Image](PCCOE%20Pune%20-%20Design%20of%20BMS%20for%20FS%20Electric%20Race%20Vehicle%20%28Conference%20Paper%29_files/img_008.png)

This design approach allows for tailored style functionality within the generic design and an easy means to expand or reduce storage capacity as to the requirements of the end user. This is all achieved by including the necessary expandability through low cost and a low component part count [6]. The PCB traces provided for differential communications are as short as possible. To ensure that the voltage between pins does not violate the absolute maximum ratings and recommended operation conditions during hotplug or other unusual conditions, two back-to-back signal diodes are provided at two appropriate places. The battery voltage input also includes a low-pass filter using a 0.1-μF capacitor and a 100-Ω resistor to avoid voltage stress during cell connection (hot-plug). Zener diodes, series resistor and bypass capacitors are connected between the voltage input pins meant for overvoltage protection and a path for inrush current during a hot-plug event. To achieve the best performance in noisy environments, automotive grade common-mode filters minimum for proper operation were chosen for differential daisy-chain communications. The differential signal lines are isolated between ICs by a DC blocking capacitor.

## VIII. CONCLUSION

A typical Formula Student Battery Management System must measure the Voltage and Current for sampling time of 500ms and Temperature of cell for sampling time of 1 second. Similar solution is proposed in this paper using bq76PL455AQ1. Passive balancing with bq76 for cell voltage equalization has been implemented in this design. The master and slave BMS modules along with the LAUNCHPAD are stacked together vertically to achieve a centralized BMS topology. The BMS will be mounted inside the accumulator container and will monitor it during both charge and discharge. The vehicle will be tested for 500kms which helps to test the BMS in extreme conditions and work further upon to improve its reliability. The BMS is designed from the ground up, keeping in mind the consideration for automotive grade power electronic systems and hence can be used in any EV, HEV, PHEV, E-Bike and E-Scooters alike.

## REFERENCES

- [1] FORMULA BHARAT 2020 Rule book
- [2] Affanni, A. Bellini, G. Franceschini, P. Guglielmi and C. Tassoni, "Battery choice and management for new-generation electric vehicles," in IEEE Transactions on Industrial Electronics, vol. 52, no. 5, pp. 1343-1349, Oct. 20052
- [3] Andrea, Battery Management Systems for Large Lithium Ion Battery Packs. Artech House, 1st ed., 2010
- [4] BU-903: How to Measure State-of-charge
- [5] Bender Insulation Monitoring Device, IMD Datasheet and User Manual
- [6] Design and Implementation of an Optimal Battery Management System for Hybrid ElectricVehicles Mark Bowkett, Kary Thanapalan, Thomas Stockley, Mark Hathway, Jonathan Williams
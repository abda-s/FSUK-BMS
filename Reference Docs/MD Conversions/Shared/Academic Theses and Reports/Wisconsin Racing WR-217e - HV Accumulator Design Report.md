<!-- Converted from Wisconsin Racing WR-217e - HV Accumulator Design Report.pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

## Design Report of the High Voltage Battery Pack for Formula SAE Electric

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_001.png)

Liam West, Barry Shepherd, Nathaniel Karabon, Josh Howell, Mike Pyrtko Department of Mechanical Engineering University of Wisconsin-Madison

December 12th, 2016

## Executive Summary

This year, Wisconsin Racing (Formula SAE at UW-Madison) is building its first ever fully electric race car in addition to the combustion engine powered race car that it traditionally builds. Powering the electric race car is the accumulator, which is a custom-built lithium ion battery pack that includes all of the controllers and hardware necessary to regulate the battery, as well as the power distribution for the motor controllers. Being that this is the first electric vehicle that Wisconsin Racing has attempted to make, a significant amount of time was devoted to background research and decision matrices to ensure that the accumulator met the performance goals and followed all of the FSAE rules. Using a lap simulator for the endurance event at the FSAE competition at Lincoln, the electrical performance goals were established. Extensive lists of components such as battery cells and battery management systems were created so that potential options could be compared side-by-side to find the optimal component. To meet the FSAE rules, structural and thermal FEA was performed on the design as it progressed. Constantly changing designs in the rest of the vehicle meant that the accumulator design had to be continuously updated to accommodate those changes.

After months of iterative development, the structural design of the accumulator has been finalized and is being fabricated. A cooling system has been incorporated into the accumulator that can be modified once the thermal model has been validated against test data to ensure that the cells remain within safe operating temperature ranges throughout the endurance event. In addition, a prototype for the braking system needed for the accumulator charging cart to meet FSAE rules has been fabricated.

The next steps for the project are to fabricate the accumulator structure and purchase all of the components. Once the accumulator has been put together, testing both inside and out of the vehicle will be conducted to ensure proper operation of the system.

## Table of Contents

| Executive Summary ........................................................................................................................................................... | 2 |
| - | - |
| Introduction - Background ................................................................................................................................................. | 5 |
| Reaching Current State of Design ...................................................................................................................................... | 5 |
| Background Research .................................................................................................................................................... | 6 |
| Battery Cells .............................................................................................................................................................. | 6 |
| Rules and Regulation ................................................................................................................................................. | 6 |
| Current Design ................................................................................................................................................................... | 7 |
| Cells ............................................................................................................................................................................... | 7 |
| Cell Selection ............................................................................................................................................................. | 7 |
| Cell Configuration ..................................................................................................................................................... | 9 |
| Cell Temperature Monitoring .................................................................................................................................. | 12 |
| Battery Management System Selection ....................................................................................................................... | 13 |
| Charging System .......................................................................................................................................................... | 14 |
| Charging Cart ........................................................................................................................................................... | 14 |
| Charger..................................................................................................................................................................... | 14 |
| Cooling System ............................................................................................................................................................ | 16 |
| Separation and Connectivity ........................................................................................................................................ | 16 |
| Fusing ...................................................................................................................................................................... | 16 |
| Accumulator Insulation Relays ................................................................................................................................ | 17 |
| Wiring ...................................................................................................................................................................... | 18 |
| Overall Accumulator .................................................................................................................................................... | 20 |
| Electrical Parameters ............................................................................................................................................... | 20 |
| Physical Parameters ................................................................................................................................................. | 21 |
| Location in Vehicle .................................................................................................................................................. | 22 |
| Analysis ........................................................................................................................................................................... | 23 |
| Finite Element Analysis ............................................................................................................................................... | 23 |
| Cooling ........................................................................................................................................................................ | 27 |
| Calculations ............................................................................................................................................................. | 27 |
| Thermal Modeling ................................................................................................................................................... | 29 |
| Appendix A: ..................................................................................................................................................................... | 32 |
| Relevant FSAE Rules .................................................................................................................................................. | 32 |
| Table A-1 Relevant FSAE Structural Accumulator Rules and Regulations ............................................................ | 32 |
| Table A-2 Relevant FSAE Charging Rules and Regulations ................................................................................... | 33 |
| Table A-3 Relevant FSAE Accumulator Electrical Rules and Regulations .................................................. | 34 |
| Appendix B: ..................................................................................................................................................................... | 36 |
| Decision Matrices and Informative Calculations ......................................................................................................... | 36 |
| Table B-1: Battery cells that were considered for using in the accumulator. ........................................................... | 36 |

| Table B-2: Battery management system decision matrix. ........................................................................................ | 37 |
| - | - |
| Figure B-1: Equations used for calculating the specific heat of lithium ion batteries using a data from a calorimeter test. ........................................................................................................................................................................... | 38 |
| Figure B-2: Equations used for calculating the brake force required to stop the charging in 0.5 [m] with spring deflection of 0.01 [m]. ............................................................................................................................................. | 38 |
| Appendix C: ..................................................................................................................................................................... | 39 |
| Component Datasheets ................................................................................................................................................. | 39 |
| Samsung INR18650-25R Technical Data ................................................................................................................ | 39 |
| Energus Power Solutions Li8P25RT Technical Data .............................................................................................. | 39 |
| Orion Battery Management System Technical Data ................................................................................................ | 40 |
| Coroplast High Voltage Wiring Technical Data ...................................................................................................... | 41 |
| TE Raychem 22 AWG Accumulator Low Voltage Wiring Technical Data ............................................................ | 41 |
| TE EV200AAANA Accumulator Insulation Relay Technical Data ........................................................................ | 42 |
| Eaton Bussman 170M3418 Main Tractive System Fuse Technical Data ................................................................ | 42 |
| Eaton Bussmann 160LET Motor Controller Fuse Technical Data .......................................................................... | 43 |
| ElCon PFC 5000 5kW 96V 44A Battery Charger Technical Data .......................................................................... | 43 |
| References ........................................................................................................................................................................ | 45 |

## Introduction - Background

Every year, the Society of Automotive Engineers (SAE) holds a competition for college undergraduates to design an automotive vehicle. The goal for the competing teams is to design and build a 1/3-scale Formula-style race car with the best overall design, manufacturing, performance, and cost. Going through the design process from concept to completion gives students priceless experience in design, simulation, and hands on knowledge. Although Wisconsin Racing, the University of Wisconsin - Madison's Formula SAE (FSAE) team, has been successful for the last two decades in the internal combustion engine competition, the rise in global warming and increasing pollution levels, has made it essential to find a viable alternative to the internal combustion engine powered car [2]. With this responsibility, it is imperative that engineers have the necessary knowledge and experience with fossil fuel saving methods. This year, the team has put it upon themselves to build two cars, the traditional combustion vehicle and an all-new formula electric race car. This will greatly expand the field of expertise on the team and prepare us for an evolving job environment. However, designing an electric vehicle for the first time will be a tremendous undertaking. In order to make this project more manageable, both vehicles will attempt to use as many of the same components as possible. To further insure our success, we have taken one of the most dissimilar vehicle design component under the guidance of a knowledgeable faculty advisor through senior design.

The aim of this project is to design and build the high voltage battery pack for a FSAE electric racecar. The high voltage battery pack will need to contain the battery cells, fuses, battery management system and much more. The driving constraints for the project are the FSAE rules, performance goals, and integration within the rest of the vehicle as it is being designed. Because the team has never built a high voltage battery pack before, extensive background research and calculations were performed to begin the design. One of excellent source of inspiration was the accumulator designs of other FSAE electric teams [1][3]. As the design progressed, numerous changes had to be made to comply with all FSAE rules and to be compatible with constantly changing packaging constraints from the rest of the vehicle. After months of hard work, the design for the accumulator meets all goals and requirements has been finalized. The next steps are to order all of the necessary components and begin fabricating the accumulator with the goal of being able to test in the spring.

## Reaching Current State of Design

Reaching the final accumulator design was a complex and iterative process. With no clear starting point and multiple ways to design an accumulator, significant time had to be devoted to background research, calculations, and ideation to ensure an optimal final product.

## Background Research

## Battery Cells

Battery Manufacturers. It was quickly discovered that there are several options for battery manufacturers throughout the world. The majority of battery companies are located in Asia, such as Melasta, LG Chem, and Samsung. One of the biggest difficulties involved with working with foreign companies is the added complexity of international purchasing and shipping. To attempt to avoid these complications, extra emphasis was put into finding battery companies with distributor locations within the United States such as A123 Systems and Turnigy Power Systems.

Battery Models and Performance Specs. Most battery manufacturers that were identified made several different types of battery cells. There were two categories of cells based on geometry: cylindrical and pouch. The cylindrical cells have their electrodes wrapped into a tube with the terminals at either end of the cylinder [4]. The electrodes in pouch cells lay parallel to each other in a single plane, forming a flat rectangular shape with the terminals at the same edge of the cell. Lithium ion pouch cells need to be under pressure to operate at peak performance. One advantage of the cylindrical cells is that their construction acts as a pressure vessel and holds the cell at the ideal pressure, while the pouch cells need an external structure to apply the necessary pressure which complicates the overall design [4]. Despite this advantage, cylindrical cells are more difficult to package efficiently since pouch cells have more options for attaching electrical leads to the terminals.

Student Designed Lap Simulator. A great deal of time was put into the development of this year's student designed lap simulator, or "Lapsim." Lapsim is a Matlab script that will take an overhead image of a track with a known pixel to physical distance ratio, and run a theoretical vehicle through that track. This script considers wind resistance, downforce, wheel slip, roll, pitch, yaw and many other vehicle dynamics and physical characteristics (weight, estimated center of gravity, etc.). This is what drives our design, since this tells us how much energy the car will need in the battery to complete all the events at the competition. With a generous completion safety factor of 1.2, Lapsim told us that we needed around 6.5 kWhr of energy while running the car extremely aggressively and operating all parasitic losses at 100% the entire time.

## Rules and Regulation

Structures. There are many rules that are pertinent to the design of the chassis and structure for the accumulator. The major rules, found in Table A-1, that must be taken into great consideration are what materials the accumulator structure can be constructed of, the minimum thickness that each given material must be and the accelerations that the structure must withstand while being fully loaded in the vehicle. Many of the pertinent regulations are listed in detail in rule EV3.4.6. The reason for the strictness of this rule is because if the accumulator chassis is damaged it can become a serious safety hazard to the overall vehicle, the drivers and those near the vehicle as well as potentially rendering the vehicle inoperable and out of the competition.

Charging. There are several rules related specifically to accumulator charging and they are mostly focused on safety. The most important rules related to charging are listed in Table A-2. The majority of the rules deal with being able to monitor the accumulator during charging and being able to stop charging in case a fault occurs. Rule EV5.8.1 specifically states that the charging shut down circuit needs to consist of at least one 25 mm shutdown button, the insulation monitoring device, and the battery management system. Another important pair of rules are EV8.2.2 and EV8.2.3, which state that the accumulator must be removed from the vehicle for charging. They also state that, when the accumulator is outside the vehicle, it must be transported on hand cart that can support the weight of the entire accumulator and is equipped with a dead man's brake.

Electrical. The most significant rules with regards to the electrical side of the accumulator are related to energy limits, controls, isolation, and grounding. These rules are located in Table A3. Our competition limits our battery pack to a maximum voltage of 300 V and maximum power output of 80 kW. All equipment that is used to work on the accumulator must be properly insulated. The cells need to be broken into segments with a maximum potential between cells of 6 MJ and a maximum voltage of 120 V. All frame components within 100 mm of the high voltage system must be less than 5 ohms to ground and all fasteners and other components within 100 mm must have less than 300 ohms to ground. The accumulator needs to be properly fused and must have at least two isolation relays.

## Current Design

Using the design constraints provided by lapsim and our motor controllers, we had to design a system that had a maximum voltage around 120 V and a capacity of around 6.5 kWhr that passes rules and fits within our space constraints. The cells and the battery management system were the first components that were determined since they drive a lot of other component selection and design, and holds more mass and volume than any other component in the accumulator.

## Cells

## Cell Selection

To ensure optimal performance from the accumulator, a significant amount of time was devoted towards extensively investigating as many battery cell options as possible. Both packaging criteria and performance data was considered. For each cell researched, the nominal voltage, capacity, peak discharge, and mass were recorded. A full list of batteries considered can be found in Table B-1 in Appendix B. From the voltage and capacity, the total number of cells needed and what configuration they would be arranged in was calculated. The configuration is determined such that you calculate the amount of series connections necessary to obtain the maximum accumulator voltage as seen in equation 1 below.

Maximum accumulator voltage [V] = maximum cell voltage [V] * # series connections [1]

Knowing this number of necessary series cells, we can now calculate the number of parallel connections between the batteries in order to obtain the proper capacity.

With these two calculations, we now know how many batteries are required and have a rough estimate of total battery weight and volume. The specific power was also calculated by taking the maximum power output of the cell and dividing it by the cell mass. Performance characteristics such as specific power allow the cells to be directly compared to each other so that the most ideal cell with the largest specific power could be identified [5]. Energus, a battery pack manufacturer from Lithuania, contacted the team about its products. They manufacture an 8-cell module that is specifically geared towards Formula SAE Electric which features threaded connections for ease of assembly, internal circuitry that outputs the highest cell temperature, and built in fuses.

Figure 1: 1s8p Energus Power Solutions Submodules

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_002.png)

The battery cells used are a cylindrical, 2.5 Ah lithium polymer battery in a standard 18650 form factor from Samsung. These Samsung INR18650-25R cells were purchased and assembled into the 1s8p configuration submodule from Energus Power Solutions for easier monitoring, packaging and assembly.

Table 1 Main cell specification

| Cell Manufacturer and Type | Samsung INR18650-25R |
| - | - |
| Cell nominal capacity: | 2.5Ah |
| Maximum Voltage: | 4.2V |
| Nominal Voltage: | 3.6V |
| Minimum Voltage: | 2.5V |
| Maximum output current: | 100A for less than 1 second |
| Maximum nominal output current: | 20A |
| Maximum charging current: | 4A |
| Maximum Cell Temperature (discharging) | 60°C |
| Maximum Cell Temperature (charging) | 45°C |
| Cell chemistry: | LiNiCoAlO2 [NCA] |

## Cell Configuration

The accumulator system consists of 720 battery cells with 30 series groups of 24 cells connected in parallel. Within those parallel groupings of cells, sets of 8 are packaged in what we are calling "submodules" in a 1s8p configuration from Energus Power Solutions (part number Li8P25RT). This packaging consists of a UL 94 V-0 rated plastic encasement, internal fusing, built-in temperature sensing, and 8mm threaded high voltage path connections. Three of these submodules are then connected in parallel via aluminum busbars. This leads us to a full accumulator with a 30s3p configuration of submodules

.

The busbars connecting the submodules will be attached via the 8mm bolts threaded into the internal threads that come attached to the copper within. To ensure positive locking, a tab washer will be installed between the busbar and the bolt head, bending around each to prevent rotation.

Figure 2: Close-up of module

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_003.png)

Figure 3: Overhead of accumulator showing layout of cell and connections

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_004.png)

The accumulator is separated into 5 isolated battery sections, each containing 6 series connections. Each battery section has a peak voltage and energy capacity of 25.2 V and 5.8 MJ, respectively. The sections of the accumulator are physically separated by the steel internal walls, and the batteries themselves are physically separated by the non-conductive, UL 94 V-0 rated plastic enclosures.

Internal cell fusing is included in the Energus Power Solutions package, with 32 fuses included in each 1s8p package (2 fuses on each cell end). The fuses are made of nickel wire and are welded straight to the cells and copper conductor, deeming them non-resettable. The fuse blow curve is shown in Figure 4, and the fuses are depicted in Figure 5.

Figure 4: Graph of current rating for the internal fuses inside the Energus package

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_005.png)

Figure 5: Simplified render of welded nickel wire fuse connecting cell to copper busbar

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_006.png)

Using these "submodules" as we call them would simplify the design and expedite the manufacturing process. In addition, their packs used Samsung 18650-25R cells, which were already a top cell candidate in our initial cell tables. Because of the ease of packaging, availability of technical support, and performance of the battery, the Energus 8-cell module with Samsung 18650 cells was chosen as the optimal battery.

## Cell Temperature Monitoring

Each grouping of 8 cells in the Energus submodule has a 4-point temperature sensor built in, which sit on the negative pole of the 2 adjacent cells, see figure 6. The output of all 4 temperature sensors gets fed into a 2-wire system as the maximum temperature reading between them. This allows us to sense the temperature of all the cells in each submodule without quadrupling the amount of wires.

All these outputs are connected to the Orion BMS through a custom Thermistor Expansion Module, which we had to design ourselves because of the unique voltage temperature curve as seen in figure 7. The sensor is a temperature-variable voltage shunt reference, acting as a Zener diode whose voltage depends on temperature. By taking the voltage drop measured across and referencing that against the temperature-voltage response curve in figure 7, we will know the highest temperature sensed in the module.

Figure 6: Placement of the 4 temperature sensors within the Energus submodule

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_007.png)

Figure 7: Temperature-Voltage response of internal Energus submodule sensors

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_008.png)

## Battery Management System Selection

The battery management system (BMS) for an electric vehicle can vary immensely depending on which manufacturer and model you decide to design around. A complete list of which BMS systems we looked can be found in Table B-2. One of the major factors that drove our decision was whether the BMS had a centralized topology. A centralized topology means that all of the voltage and thermistor tap information is processed within a single BMS. This is beneficial since you will only have two possible points of connection failure and do not need to design, manufacture individual cell PCBs in order to process the information before sending it to the BMS. Many other factors were considered, including whether it could communicate over CAN, how many cells it could monitor both with voltage and temperature, and whether it was isolated from its voltage taps.

The BMS utilized in our design is the Orion BMS from Ewert Energy Systems. This BMS is commercially available and designed specifically for electric and hybrid vehicles. It supports sets of 12 cells up to 108 battery cells or a variety of different battery chemistries. Since we have 30 series groups to monitor, we had to acquire a BMS with a 36 cell or above configuration. It is designed to work in high noise environments and in harsh temperatures ranging from -40 to 80 degrees Celsius. The BMS can read cell voltages from .5 to 5 volts. The accumulator pack consists of lithium ion cells, the maximum cell open circuit voltage limit is set to 4.2 volt and minimum open circuit voltage limit set to 3 volts. Measurement resolution is 1.5mV. The ADC within the AMS has a 12-bit resolution with a ±10mV accuracy rating. If the voltages get near the limits it opens the accumulator insulation relays (AIRs). The temperature limit is set to be 60 C and if this temperature is exceeded it opens the AIRs. All the sense wires are electrically and magnetically isolated by the BMS. In the case that an error is detected and the BMS needs to open AIR's, it switches the internal relay which connects to the internal shutdown circuit. Galvanic isolation between the tractive system and the grounded low voltage system connections occurs within the BMS.

Table 2 BMS Parameters

| Electrical Specification Item | Min. | Typ. | Max | Units |
| - | - | - | - | - |
| Nominal Supply Voltage | 10 | 12 | 16 | Vdc |
| Supply Current - Active |  | 250 |  | mA |
| Supply Current - Sleep |  | 650 |  | uA |
| Operating Temperature | -40 |  | 80 | C |
| Cell Voltage Measuring Range | 0.5 |  | 5.0 | ms |
| Number of Cells Supported in Series | 12 |  | 108 | cells |

## Charging System

## Charging Cart

According the FSAE rule EV8.2.2, any time the accumulator is taken out of the vehicle it must be transported on an accumulator container hand cart equipped with a deadman's braking system. In order to meet this requirement, several routes could be taken. The first would be to source a push cart with a deadman's brake already equipped that could provide enough braking force to stop the cart loaded with the accumulator and high voltage charger. Few companies sell push carts with the option to have a deadman's brake attached and the carts that do are expensive for what you actually get. These carts sell for $800 plus. Because this option would be so expensive, the next route investigated was buying deadman braking casters and attaching them to a push cart. Again, not many companies sell deadman braking casters that are rated to support the weight of our accumulator and charger. The ones that do are sold for at least $200 per caster. By buying a push cart, roughly $200, and two deadman braking casters this method would cost us over $600. Although this is expensive, it's an improvement from buying a push with deadman casters already equipped that couldn't handle the weight. The final route investigated was buying pushcart and creating a deadman's braking system in house. This route would be much more time intensive compared to the first two options but will be much less expensive. Since this is required by rules and will need to be operational for potentially multiple years, we decided to go with the second option of sourcing braking casters, but instead of purchasing a cart, we would fabricate our own.

## Charger

The accumulator will be charged with a PFC 5000 Battery Charger from ElCon, part number TCCH-96-44. During charging, the BMS will be balancing cells by passing small amounts of amperage across the voltage sense wires. The charger will be connected to the accumulator and BMS through an external charge plug that connects the positive and negative terminals of the accumulator before the AIR's. Overvoltage protection is provided by the CAN communication between the charger and the BMS and the BMS disabling the contactors separating the modules. The charger will only become live when connected to the accumulator due to a low voltage interlock loop within the connector. There will also be an emergency shutdown button on the charging cart as a manual failsafe.

Table 31 General charger data

| Charger Type: | ElCon PFC 5000 TCCH-96-44 |
| - | - |
| Maximum charging power: | 5kW |
| Maximum charging voltage: | 130V |
| Maximum charging current: | 44A @ 230 VAC, 20 @ 115VAC |
| Interface with accumulator | CAN-Bus |
| Input voltage: | 230 VAC, 115 VAC |
| Input current: | 20A rms @ 120 VAC / 23 A rms @ 230 VAC |

Figure 8: Charging port that will connect the accumulator to the ElCon charger

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_009.png)

## Cooling System

Based on the thermal models made for the batteries, the cells would exceed their maximum operating temperature of 60° C before the end of the endurance event. Personal experience with 18650 cells in Milwaukee Tool batteries and consulting with our faculty advisor, Glenn Bower, lead us to believe that the heat generation seen in the thermal models may be higher than what would occur in reality, even after taking into account the fact that the thermal models assume adiabatic conditions. If the actual heat generated by the batteries is small enough, a cooling system may not be needed. The thermal models have to be validated against measured data to provide a definitive answer as to whether or not a cooling system is needed. Because the thermal has yet to be validated, a basic air cooling system was designed and packaged into the accumulator. It is easier to design and package a cooling system while the rest of the vehicle is being designed than to wait until the thermal model is validated and changing other components would be difficult. If the validated model shows that a cooling system is not needed, the air cooling system that was designed will not be implemented, freeing up extra space if un-forseen changes need to be made to other components last minute.

## Separation and Connectivity

## Fusing

The main high voltage tractive system current path is protected by one main fuse, a 170M3418 fuse from Bussmann, within the High Voltage Disconnect. Additionally, four smaller, stud-mount 160LET fuses from Bussmann (an Eaton company) protect each of the motor controllers. These smaller fuses connect the negative terminal of each motor controller to the negative terminal distribution busbar of the accumulator.

Table 4 Basic main tractive system fuse data

| Fuse manufacturer and type: | Bussmann, 170M3418 |
| - | - |
| Continuous current rating: | 350A |
| Maximum operating voltage | 550VDC |
| Type of fuse: | High speed |
| I2t rating: | 68500A2s at 660VDC |
| Interrupt Current (maximum current at which the fuse can interrupt the current) | 200kA |

Table 5 Basic motor controller fuse data

| Fuse manufacturer and type: | Bussmann, 160LET Fuse |
| - | - |
| Continuous current rating: | 160A |
| Maximum operating voltage | 150VDC |
| Type of fuse: | High speed |
| I2t rating: | 16000A2s at 240VDC |
| Interrupt Current (maximum current at which the fuse can interrupt the current) | 200kA |

Table 6 Fuse Protection Table

| Location | Wire Size | Wire Ampacity | Fuse type | Fuse rating |
| - | - | - | - | - |
| Aluminum Busbars connecting Cells | 50mm^2 | 350 A | 170M3418 Fuse | 350 A |
| Shielded Copper Cable Accumulator to Motor controller | 16mm^2 | 200 A | 160LET Fuse | 160 A |
| Shielded Copper Cable AIR to HVD | 50mm^2 | 400 A | 170M3418 Fuse | 350 A |
| TE KILOVAC EV200 Contactor | - | 500 A | 170M3418 Fuse | 350 A |
| Cell Voltage Taps to BMS | 22 AWG | 7 A | Orion BMS Internal Fuse | 5 A |

## Accumulator Insulation Relays

The AIRs used are normally open KILOVAC EV200AAANA Contactors rated for 500 amps continuous current from Tyco Electronics. These insulation relays are used between each of the modules and between the negative and positive most battery terminals before the high voltage motor controller distribution busbars.

Table 2 Basic AIR data

| Relay Type: | KILOVAC EV200 |
| - | - |
| Contact arrangement: | 1 Form A (SPST-NO) |
| Continuous DC current rating: | 500A |
| Overload DC current rating: | 2000A for 10sec |
| Maximum operation voltage: | 900VDC |
| Nominal coil voltage: | 12VDC |
| Normal Load switching: | Make and break up to 300A |
| Maximum Load switching | 10 times at 1500A |

## Wiring

Knowing the size of our battery pack, the expected aerodynamics and kinematics of the vehicle, we used our student developed lap simulator to get an accurate estimate of our nominal current draw and how long each maximum current draw would occur. The maximum current from the accumulator occurs during heavy acceleration and high speed when the total vehicle power output is just below the 80 kW limit.

The maximum and nominal current draw from the accumulator at 50% state of charge (108 VDC) with a 20 kW regeneration and an 80 kW power limit are 950 A and 240 A rms, respectively. Current draws of over 800 A only occur for a maximum of 0.5 seconds.

Table 8 Wire data of Coroplast, 50 mm²

| Wire type | Coroplast, Silicone-insulated single-core high-voltage automotive cables, screened - Copper |
| - | - |
| Continuous current rating: | 400 A @ 60°C |
| Cross-sectional area | 50 mm² |
| Maximum operating voltage: | 900VDC |
| Temperature rating: | 180 °C |
| Wire connects the following components: | Accumulator to HVD |

Table 9 Wire data of Coroplast, 16 mm²

| Wire type | Coroplast, Silicone-insulated single-core high-voltage automotive cables, screened - Copper |
| - | - |
| Continuous current rating: | 200 A @ 60°C |
| Cross-sectional area | 16 mm² |
| Maximum operating voltage: | 800VDC |
| Temperature rating: | 180 °C |
| Wire connects the following components: | Accumulator to Motor Controller |

Table 10 Wire data of Raychem, 0.326 mm²

| Wire type | TE Raychem, 55A0111-22-9 |
| - | - |
| Continuous current rating: | 7A |
| Cross-sectional area | 0.326 mm², 22 AWG |
| Maximum operating voltage: | 600VDC |
| Temperature rating: | 150 °C |
| Wire connects the following components: | Cell to BMS, Contactors, and Pre- charge/discharge circuit |

Instead of maintenance plugs our design utilized normal open contactors to separate the different battery sections. The contactors are the same as those used for the AIRs. Inside the Accumulator, all connections are made by aluminum 6061 busbars, positive locking tab washers and head bolts. There is no high voltage cabling internally, just connecting external components (i.e. HVD, motor controllers) to the accumulator.

Figure 9: Render of contactor placement as well as high voltage busbar layout

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_010.png)

## Overall Accumulator

## Electrical Parameters

The accumulator pack consists of 720 lithium polymer battery cells, arranged in a parallel-series configuration. Twenty-four cells are connected directly in parallel, and thirty of these sets are then connected in series. Each module of the accumulator contains 6 series connections, and is separated from the others by high voltage contactors.

Table 11 Main accumulator parameters

| Maximum Voltage: | 126VDC |
| - | - |
| Nominal Voltage: | 108VDC |
| Minimum Voltage: | 75VDC |
| Maximum output current: | 1080A for 10 sec |
| Maximum nominal current: | 480A |
| Maximum charging current: | 96A |
| Total numbers of cells: | 720 |
| Cell configuration: | 30s24p |
| Total Capacity: | 23.3 MJ, 6.48 kWh |
| Number of cell stacks < 120VDC | 5 |

## Physical Parameters

The accumulator container consists of a welded, bent 4130 sheet steel lower chassis (0.05" thick) with welded internal walls (0.04" thick) that break it up into 5 equal compartments. The cover is also made of welded, bent 4130 sheet steel (0.04" thick). The accumulator is internally broken up into the lower section, where the cells are housed, and an upper section, which houses the low voltage components that interact with the accumulator (contactors, BMS, AIR's, etc.). This barrier is made with a 0.5" thick sheet of polycarbonate that insulated and isolates one half from the other. In the upper section, there is a portion that is dedicated to power distribution, which is protected from the rest of the low voltage components by a polycarbonate wall. All aforementioned materials meet UL94 V-0 standards. Describe the concept of the container, show how the cells are mounted, use CAD-Renderings, show data regarding materials used, etc.

Figure 10: Cross-section of accumulator showing compartmentalization

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_011.png)

To ensure adequate cooling, holes in the sides of the lower chassis are laser-cut to align with the cooling holes on the Energus submodules. Air will be forced in through the lower chassis and up through and out of the upper section of the accumulator by 3 92mmx92mm fans.

## Location in Vehicle

In the vehicle, the accumulator is mounted directly behind the driver and firewall. The driver side impact structure extends all the way to the rear of the monocoque to protect the accumulator. The accumulator is rigidly attached to the monocoque and rear tubular spaceframe by welded on mounts. In all there are 10 mounts, each with 5/16-24 steel bolts going through them. These mounts are capable of withstanding 20 kN of force in all directions, which are detailed in the Structural Equivalency Spreadsheet (SES).

Figure11: Accumulator container position

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_012.png)

Figure 12: Accumulator mount point locations

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_013.png)

## Analysis

## Finite Element Analysis

Many of the accumulator's structural components were required to withstand a significant amount of force [6]. In order to verify that our vehicle would be able to withstand the required forces, parts were modeled in solidworks and subjected to the required loads. This allowed our team to test and iterate design without the high cost and time involved in destructive physical testing.

The mounts are required to withstand 20 kN in any direction, and due to the weight of our accumulator, we are required to have at least 10 mounts. The rules also state that for steel components, 300 MPa is considered failing at weld locations and 365 MPa is considered to be failing in the body of the part.

In the interest of prototyping numerous designs, initial testing was performed on a percomponent basis. This allowed the team to gain a general idea of what would work and what would fail. As each iteration converged on a singular design, we moved to Solidworks simulation for forces applied in an assembly. This allowed a more realistic representation for the magnitude of stresses present in our parts.

Early designs were based on minimum required size for the mount, as the significance of the mounting system was initially underestimated. These were modeled as simple sheet metal parts. The sheet metal thickness was increased until it was apparent that the benefit of doing so would not be substantial enough to make the part pass. In Figure 13, any visible color is experiencing a stress greater than 300 MPa, while any material in red is experiencing 365 MPa or greater, and is therefore considered to be failing. This showed that a small sheet metal part would very likely be inadequate for the needs of the accumulator.

Figure 13: A 20 kN load is applied in the downward direction to our initial mount idea, with welded edges set to be fixed for the simulation.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_014.png)

We still desired to use a bent sheet metal part. This would be easiest to manufacture, because one of our sponsors would be able to bend the part for us, leaving welding as the only remaining operation to be performed. The next mount we considered was a flattened pyramid with a welded tube insert placed through the center to allow a stronger location for the bolt to be placed. We realized that this part would need to allow air through it in some locations, in order to allow the cells to pull in air for cooling. Because of this, we placed slots in the mount which were parallel with the load paths.

This part, shown in figure 14, showed promise for meeting our needs due to the general shape of its construction. However, the part needed to be made of thicker sheet material. Increasing the sheet thickness meant increasing the bend radius. This increase in bend radius increased how far the outermost edge was away from the accumulator. Due to our space constraints within the monocoque, we were not able to increase the size of the part to the degree necessary to meet our required load cases.

Figure 14: Vented gusset mount. This mount allowed loads to be transferred into the accumulator at the internal walls or the edges of the accumulator, distributing the force into members which could support the forces required.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_015.png)

The continual failure in supporting the required forces led to the decision to begin modeling the mount as a solid part, to be manufactured on a 3-axis CNC mill or with a waterjet. This allowed more freedom of design, and so the first workable 20kN mount was created. This mount used more traditional gussets, spreading the load across a large area of the accumulator. Figure 15, shown below, shows how the "butterfly" mount has gussets which spread out the applied load. This piece is also highly manufacturable, as it is only two setups on a waterjet.

Figure 15: Butterfly mount with a 20 kN downward force applied.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_016.png)

The mounts would be used for six of our 10 required mount locations. From here, mounts to the frame tubes and to the rear of the accumulator could be designed. These mounts will be 3 axis CNC machined parts, as they would need to be coped to sit flush with the frame tubes. The frame mounts will be capable of supporting much higher loads without having to extend their gussets over a large area. Figure 16 demonstrates where the mounts will sit relative to the accumulator. These mounts have been weight optimized by having sections removed.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_017.png)

.

Figure 16: Rear accumulator mounts. Highlighted in blue are the mounts which will attach to the frame tubes.

These mounts were then modeled in an assembly, shown in figure 17, to simulate more realistic loading. All components are constrained by not being able to penetrate through each other. The ends of the tubes are fixed and the edges where welds will be are bonded to the adjacent part. The accumulator half of the mount is bolted to assembly. The 20 kN load is then applied to the accumulator portion of the mount, while rollers/sliders guide the mount in the direction the accumulator would move it.

Figure 17: An example of an assembly modeled in a SolidWorks static study.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_018.png)

Figure 18: A downward 20 kN load is applied to the lower rear mount assembly.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_019.png)

This more realistic method of modeling in an assembly shows that our parts will succeed in their required load cases. This simulation and continuous iteration heavily drove the design process for the mounting system, The images of how our mounts meet each load case will allow us to prove that our vehicle will pass technical inspection at competition.

Along with the FEA on the mounts we ran studies on the accumulator chassis and cover. These tests utilized the points on where the mounts would attach to the lower chassis. To simulate the acceleration that is required by the rules, the mass of the accumulator gathered by compiling a list of every component that would go in and on the accumulator. The final mass of the system is approximately 65 kg. This mass was then taken and multiplied by the acceleration of gravity (9.81 m/s^2) and multiplied by the correct factor of 40 or 20 depending on which area the test was being conducted on. For the lateral and longitudinal directions a distributed force of 25.6 kN was applied and for the vertical direction a force of 12.8 kN was applied.

## Cooling

## Calculations

In order to have accurate inputs for the thermal model of the battery, multiple physical properties had to be measured. The mass of the Samsung 18650 cell was measured to be 44 grams and the density was calculated to be 2.574e-6 kg/mm3. To calculate the heat capacity of the cells, a simple calorimeter test was conducted. First, a known amount of room temperature water was poured into a well-insulated container. Then, a single Samsung 18650 cell was placed into an ice bath for an hour to ensure it reached a uniform temperature of 0° Celsius. The battery was then quickly removed from the ice bath and placed into the room temperature water while recording the water temperature. The temperature data from the warm water can be seen in Figure 19.

Figure 19: Calorimeter test data for a single Samsung 18650 cell initially soaking in an ice bath. The 44 gram battery caused the 156 grams of water to decrease in temperature by 1.11° Celsius.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_020.png)

By taking the difference between the initial room temperature water and the lowest temperature the water reached, the total heat transferred from the water could be calculated. Knowing that the heat transferred from the water must equal the heat that entered the battery, the heat capacity of the cell could be calculated. Based on the test results, the specific heat of one Samsung 18650 cell is 963.3 J/kg-K. The formulas used for this calculation can be found in Figure B-1 in Appendix B.

The first model that was calculated was a simple 0D numerical model of the Samsung 18650 cell which was easy to understand and implement. The model treated the battery cell as a lumped thermal capacitance under adiabatic conditions. Not only did this simplify the problem, it provided a good baseline to validate the internal thermal properties of the battery. The specific heat of the Samsung cell was 963.3 J/kg-K, measured using the calorimeter test mentioned before. The internal resistance from the Samsung 18650 data sheet is 30 mΩ [7]. The heat generation within the battery was assumed to be exclusively due to ohmic heating. The current vs time trace shown in Figure 20 was developed by another team member using an endurance lap simulation and was used as the battery load. By squaring the current at each time step and multiplying by the internal resistance, the heat generated could be determined.

Figure 20: Simulated current vs time for a single endurance lap with a 40kW power limit at the Lincoln FSAE competition

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_021.png)

## Thermal Modeling

The physical cell parameters were implemented into a Heun numerical model that was written in MATLAB to solve for cell temperature vs time. Using a time step of 1 ms, the model goes through the simulated endurance current trace and calculates the change in temperature from the previous time step. The resulting cell temperature vs time can be seen in Figure 21. Based on the initial thermal model setup, each cell in the accumulator would increase by 6.1° Celsius over the course of one endurance lap if no heat was dissipated. The car is expected to complete 14 laps over the course of the entire endurance event, which would result in the pack temperature raising by 85.4° C, which far surpasses the cell's maximum operating temperature of 60° C.

## Cell Temperature vs Time

Figure 21: Cell temperature vs time for a single lithium ion 18650 cell through the single endurance lap current simulation. The model uses a numerical method implemented in MATLAB and assumes the cell to be adiabatic.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_022.png)

Because there is a lot of mass in the accumulator in addition to the battery cells themselves, the heat generated through ohmic heating can dissipate into that mass which would decrease the cell temperatures. In order to investigate this effect further, a more complex 3D thermal model had to be constructed. Using Thermal Desktop, a single cell model was first created using the same parameters from the 0D single cell numerical model. The single cell model was then used to create the full Energus module model. Using a CAD model of the Energus pack, the amount of copper and plastic in the pack was estimated. The thermal contact resistance between the battery cells and the copper was assumed to be negligible, while the thermal contact resistance between the copper and plastic was estimated to be 600 K/W-m2 based on typical thermal contact resistance in metal-plastic interfaces [8]. Figure 22 shows the final Energus module temperature distribution after one endurance lap under adiabatic conditions. The cell temperature increased by 7° C over one lap, which would result in the battery cells increasing in temperature by 98° C over the course of the endurance event.

Node

Figure 22: Final conditions for the full Energus module using the 18560 cells from the single cell model. The entire Energus module was modeled to be adiabatic which resulted in a temperature rise of 7 degrees C.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_023.png)

## Appendix A:

## Relevant FSAE Rules

## Table A-1 Relevant FSAE Structural Accumulator Rules and Regulations

| Description | Rule Number |
| - | - |
| If the accumulator container(s) is not easily accessible during Electrical Tech Inspection, detailed pictures of the internals taken during assembly have to be provided. However, at the end of the event the tech inspectors reserve the right to check any accumulators to ensure that the rules are adhered to | EV3.2.3 |
| Each accumulator container must be removable from the car while still remaining rules compliant. | EV3.2.4 |
| If the container is made from an electrically conductive material, then the poles of the accumulator segment(s) and/or cells must be isolated from the inner wall of the accumulator container with an insulating material that is rated for the maximum tractive system voltage. All conductive surfaces on the outside of the container must have a low-resistance connection to the GLV system ground, see EV4.3. Special care must be taken to ensure that conductive penetrations, such as mounting hardware, are adequately protected against puncturing the insulating barrier | EV3.3.1 |
| Each segment must be electrically insulated by the use of suitable material between the segments in the container and on top of the segment to prevent arc flashes caused by inter segment contact or by parts/tools accidentally falling into the container during maintenance for example. Air is not considered to be a suitable insulation material in this case. | EV3.3.4 |
| The Accumulator Isolation Relays (AIRs) and the main fuse must be separated with an electrically insulated and fireproof material to UL94-V0 from the rest of the accumulator. Air is not considered to be a suitable insulation material in this case | EV3.3.5 |
| If the tractive system connectors to the accumulator containers can be removed without the use of tools, then a pilot contact/interlock line must be implemented which activates the shutdown circuit and opens the AIRs whenever the connector is removed. | EV3.3.6 |
| The container material must be fire resistant according to UL94-V0, FAR25 or equivalent. | EV3.4.3 |

| All accumulator containers must be designed to withstand forces from deceleration. Teams have the option to use the design guidelines in rule EV3.4.6 or analyze the accumulator through the "Alternative Frame Rules" process. Design of the Accumulator container must be documented in the SES or SRCF. Documentation includes materials used, drawings/images, fastener locations, cell/segment weight and cell/segment position. | EV3.4.5 |
| - | - |
| Accumulator containers must be constructed of sheet/plate steel or aluminum in accordance with EV3.4.6, which dictates wall thicknesses of 1.25 mm stainless, 2.3 mm stainless, and 0.9 mm stainless. Please see rules at fsaeonline.com for full details. | EV3.4.6 |
| The accumulator design guidelines are intended to generate a structure that does not fail the following accelerations: a. 40g in the longitudinal direction (forward/aft) b. 40g in the lateral (left/right) c. 20g vertical (up/down) direction | EV3.4.6 |

## Table A-2 Relevant FSAE Charging Rules and Regulations

| Description | Rule Number |
| - | - |
| The charging shutdown circuit when charging consists of at least the charger shutdown button, the insulation monitoring device (IMD) and the accumulator management system (AMS). | EV5.8.1 |
| Accumulator must be removed for charging and transported on accumulator container hand cart. Must have a label with team name and Electrical System Office phone number. | EV8.2.2, EV8.2.3 |
| All chargers must either be accredited to a recognized standard e.g. CE or where built by the team they must be built to high standards and conform to all electrical requirements for the vehicle tractive system. | EV8.3.2 |
| Charger must incorporate an interlock to ensure correct connection and an E-stop button (minimum 25mm diameter.) | EV8.3.3 |
| The charger connector must incorporate an interlock such that neither side of the connector become live unless it is correctly connected to the accumulator. | EV8.3.3 |
| HV charging leads must be orange | EV8.3.4 |
| When charging, the AMS must be live and must be able to turn off the charger in the event that a fault is detected. | EV8.3.5 |

The hand cart must have a brake such that it can only be released using a dead man's switch, i.e. the brake is always on except when someone releases it by pushing a handle for example.

EV8.4.2

## Table A-3 Relevant FSAE Accumulator Electrical Rules and Regulations

| Description | Rule Number |
| - | - |
| The maximum permitted voltage that may occur between any two electrical connections is different between the competitions allowing electric vehicles. 300 VDC. | EV1.1.2 |
| The entire tractive and GLV system must be completely galvanically separated. The border between tractive and GLV system is the galvanic isolation between both systems. Therefore, some components, such as the motor controller, may be part of both systems. | EV1.2.7 |
| All components in the tractive system must be rated for the maximum tractive system voltage | EV1.2.8 |
| The GLV system must be powered up using a specified procedure before it is possible to activate the tractive system, see EV4.10. Furthermore, a failure causing the GLV system to shut down must immediately deactivate the tractive system as well | EV1.2.10 |
| The maximum power drawn from the battery must not exceed 80kW. This will be checked by evaluating the Energy Meter data. | EV2.2.1 |
| A violation is defined as using more than 80kW or exceeding the specified voltage for more than 100ms continuously or using more than 80kW or exceeding the specified voltage, after a moving average over 500ms is applied. | EV2.2.4 |
| Regenerating energy is allowed and unrestricted but only when the vehicle speed is > 5kph. It is not allowed at vehicle speeds <= 5kph. | EV2.2.7 |
| All types of accumulators except molten salt and thermal batteries are allowed. | EV3.1.1 |
| If spare accumulators are to be used then they all have to be of the same size, weight and type as those that are replaced. Spare accumulator packs have to be presented at Electrical Tech Inspection. | EV3.2.2 |
| Every accumulator container must contain at least one fuse and at least two accumulator isolation relays, see EV3.5 and EV6.1. | EV3.3.2 |

| Maintenance plugs, additional contactors or similar measures have to be taken to allow electrical separation of the internal cell segments such that the separated cell segments contain a maximum static voltage of less than 120VDC and a maximum energy of 6MJ. The separation must affect both poles of the segment. | EV3.3.3 |
| - | - |
| This separation method must be used whenever the accumulator containers are opened for maintenance and whenever accumulator segments are removed from the container. | EV3.3.3 |
| Contacting / interconnecting the single cells by soldering in the high current path is prohibited. Soldering wires to cells for the voltage monitoring input of the AMS is allowed, since these wires are not part of the high current path | EV3.3.7 |
| Every wire used in an accumulator container, no matter whether it is part of the GLV or tractive system, must be rated to the maximum tractive system voltage. | EV3.3.8 |
| Each accumulator container must have a prominent indicator, such as an LED that will illuminate whenever a voltage greater than 60V DC is present at the vehicle side of the AIRs. | EV3.3.9 |
| The voltage being present at the connectors must directly control the indicator using hard wired electronics (no software control is permitted). Activating the indicator with the control signal which closes the AIRs is not sufficient. | EV3.3.10 |
| The accumulator voltage indicator must always work, e.g. even if the container is disconnected from the GLVS or removed from the car and carried around. | EV3.3.11 |

## Appendix B:

## Decision Matrices and Informative Calculations

Table B-1: Battery cells that were considered for using in the accumulator.

1

1

.

| Masufacture Hame |  | Hominal Yoltage (Y) |  | Capacity (A"b) Peak Discharge (A) | Weight (g) |  | Eaergy (W"b) Specific Eaergy ("h / g) | Specific Power (/g) |
| - | - | - | - | - | - | - | - | - |
| A123 | AMP20M1HD-A P | 3.3 | 20 | 363 | 436 | 66 | 0.133064516 | 2.415120968 |
| Battery Space | 604490 Battery | 3.7 | 2.1 | 40 | 46 | 7.77 | 0.168913043 | 3.217391304 |
| Battery Space | 803496 Battery | 3.7 | 2.2 | 55 | 53 | 8.14 | 0.153584306 | 3.839622642 |
| EMB | LP9245150HD | 3.7 | 5.4 | 111 | 111 | 19.98 | 0.18 | 3.7 |
| EMB | LP1042126HD | 3.7 | 5 | 100 | 100 | 18.5 | 0.185 | 3.7 |
| GB battery | GB5750HP-1S | 3.7 | 5.75 | 345 | 121 | 21.275 | 0.175826446 | 10.54358678 |
| GB battery | GB7700S-1S | 3.7 | 7.7 | 115.5 | 142 | 28.49 | 0.200633803 | 3.009507042 |
| GB battery | GB10000S-1S | 3.7 | 10 | 150 | 185 | 37 | 0.2 | 3 |
| GB battery | GB6250HP-1S | 3.7 | 6.25 | 375 | 128 | 23.125 | 0.180664063 | 10.83984375 |
| GB battery | GB2200XL-1S | 3.7 | 2.2 | 88 | 47 | 8.14 | 0.173191489 | 6.927659574 |
| GB battery | GB2700XL-1S | 3.7 | 2.7 | 108 | 57.5 | 9.99 | 0.17373913 | 6.349565217 |
| GB battery | GB3250HP-1S | 3.7 | 3.3 | 195 | 70 | 12.21 | 0.174428571 | 10.30714286 |
| GB battery | GB3500XL-1S | 3.7 | 3.5 | 140 | 73 | 12.95 | 0.17739726 | 7.095890411 |
| GB battery | GB4000XL-1S | 3.7 | 4 | 160 | 82.5 | 14.8 | 0.179393939 | 7.175757576 |
| GB battery | GB4500XL-1S | 3.7 | 4.5 | 180 | 95 | 16.65 | 0.175263158 | 7.010526316 |
|  | high power tech 885089AHP-4100 | 3.7 | 4.1 | 61.5 | 77.3 | 15.17 | 0.196248383 | 2.343725744 |
| high power tech 9250140CP-7000 |  | 3.7 | 7 | 105 | 131.8 | 25.9 | 0.196509863 | 2.347647951 |
| LG | 18650 HG2 | 3.6 | 3 | 35 | 47 | 10.8 | 0.229787234 | 2.680851064 |
| LiPol | LPHD9449135 | 3.7 | 5.8 | 522 | 125 | 21.46 | 0.17168 | 15.4512 |
| LiPol | LPHD8245150 | 3.7 | 5 | 450 | 116.6 | 18.5 | 0.158662093 | 14.27958834 |
| LiPol | LPHD1542126 | 3.7 | 6.5 | 650 | 151 | 24.05 | 0.159271523 | 15.92715232 |
| Melasta | SLPB9864155 | 3.7 | 10 | 200 | 218 | 37 | 0.169724771 | 3.394495413 |
| Melasta | SLPBA875175 | 3.7 | 15 | 225 | 302.5 | 55.5 | 0.183471074 | 2.752066116 |
| Melasta | SLPB7785186 | 3.7 | 12.5 | 187.5 | 262 | 46.25 | 0.176526718 | 2.647900763 |
| Melasta | SLPB8070170 | 3.7 | 10 | 150 | 206 | 37 | 0.17961165 | 2.634174757 |
| Melasta | LPA545135 | 3.7 | 6.1 | 183 | 135 | 22.57 | 0.167185185 | 5.015555556 |
| Melasta | SLPB3145180 | 3.7 | 7.05 | 176.25 | 159 | 26.085 | 0.164056604 | 4.101415094 |
| Melasta | SLPB9342126 | 3.7 | 5 | 125 | 113 | 18.5 | 0.163716814 | 4.092920354 |
| Melasta | LP8534106 | 3.7 | 2.6 | 52 | 64 | 9.62 | 0.1503125 | 3.00625 |
| Melasta | LPA745150 | 3.7 | 6.9 | 276 | 160 | 25.53 | 0.1595625 | 6.3825 |
| Melasta | LP8045135 | 3.7 | 4 |  |  |  |  |  |
| Melasta | SLPBB142126 | 3.7 | 6.3 | 120 | 96 | 14.8 | 0.154166667 0.18 | 4.625 2.7 |
| Melasta | SLPB7685186 | 3.7 | 12.5 | 94.5 187.5 | 129.5 257 | 23.31 46.25 | 0.179961089 | 2.699416342 |
| Melasta | SLPB8763124 | 3.7 | 7.5 | 112.5 | 151 | 27.75 | 0.183774834 | 2.756622517 |
| Melasta | SLPBA790215 | 3.7 | 24 | 336 | 454 | 88.8 | 0.195534714 | 2.738325991 |
| NXE (LiCo) | NXEC6400/100-13 | 3.7 | 6.4 | 1280 | 147.9 | 23.68 | 0.160108181 | 32.02163624 |
| Orion | Carbon Pro | 3.7 | 7.2 | 720 | 145 | 26.64 | 0.183724138 | 18.37241379 |
| PDBattery | High Charge Custo | 3.7 | 10 | 450 | 240 | 37 | 0.154166667 | 6.9375 |
| Samsung | Lithium 18650 | 3.6 | 1.5 | 23 | 45 | 5.4 | 0.12 | 1.84 3.288888889 |
| Tenergy Tenergy | 8059156 Battery | 3.7 | 8 | 160 | 180 | 29.6 | 0.164444444 0.148 | 3.7 |
|  | 5745135 Battery | 3.7 | 3 | 75 | 75 | 11.1 |  |  |
|  | Nano-tech round c 703564 Battery | 3.7 3.7 | 1.2 1.1 | 27.5 18 | 23 28 | 4.44 4.07 | 0.193043478 0.145357143 | 3.633928571 2.895652174 |
| Turnigy |  | 3.7 | 5 | 100 | 114 | 18.5 | 0.162280702 | 3.245614035 |
| Tcnergy Turnigy | Single Cell 20C |  |  |  |  | 22.2 | 0.155244755 | 20.18181818 |
| Turnigy | Single Cell 40C | 3.7 | 5 | 200 | 130 | 18.5 | 0.142307692 | 5.692307692 |
| Turnigy Turnigy | Nano-tech A-SPEC Nano-tech hardcas | 3.7 3.7 | 6 5.6 | 780 728 | 143 152 | 20.72 | 0.136315789 | 17.72105263 |
| Turnigy | Nano-tech hardcas | 3.7 | 5 | 500 | 148 |  | 0.125 | 12.5 |
| Turningy | Nano-tech ultimate | 3.7 | 6.4 | 576 | 170 | 18.5 23.68 | 0.139294118 | 12.53647059 |
| ZIPPY |  |  |  |  |  | 22.94 |  | 5.126256983 |
|  | Flightmax | 3.7 | 6.2 | 248 | 179 |  | 0.128156425 |  |

Table B-2: Battery management system decision matrix.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_024.png)

Figure B-1: Equations used for calculating the specific heat of lithium ion batteries using a data from a calorimeter test.

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_025.png)

```
m_accumulator = 64.3 [kg] 'mass of accumulator" m_charger = 14 [kg] "mass of charger" m_total = m_charger + m_accumulator "total mass' g = 9.81 [m/s^2] "constant of gravity" v_i = 3.1 [m/s] 'average walking velocity" v_f = 0 [m/s] "final velocity" DELTA_x = 0.5 [m] "stopping distance' v_f^2 = v_i^2 + 2*accel*DELTA_x "equation of motion" F_x = m_total*accel "force of cart" F_wheel = F_x/2 "force of one wheel" mu = 1.15 "coefficient of friction, rubber on rubber" r = 6*convert(in,m)/2 "radius of caster" M_o = F_wheel*r "moment on caster" 0 ≡ mu*F_brake*r - M_o "brake force" DELTA_L = .01 [m] "spring defelection' F_spring = F_brake "spring force" F_spring = k*DELTA_L "spring rate"
```

Figure B-2: Equations used for calculating the brake force required to stop the charging in 0.5 [m] with spring deflection of 0.01 [m].

## Appendix C:

## Component Datasheets

## Samsung INR18650-25R Technical Data

The Samsung INR18650-25R cells are covered in Cells.

| Type | Type | Spec. | Typical INR18650-25R |
| - | - | - | - |
| Chemistry |  | NCA | NCA |
| Dimension (mm) | Diameter | 18.33 ± 0.07 | 18.33 ± 0.07 |
| Dimension (mm) | Height | 64.85 ± 0.15 | 64.85 ± 0.15 |
| Weight (g) | Weight (g) | Max. 45.0 | 43.8 |
| Initial IR (mΩ AC 1kHz) | Initial IR (mΩ AC 1kHz) | ≤ 18 | 13.20 ± 2 |
| Initial IR (mΩ DC (10A-1A)) | Initial IR (mΩ DC (10A-1A)) | ≤ 30 | 22.15 ± 2 |
| Nominal Voltage (V) | Nominal Voltage (V) | 3.6 | 3.64 |
| Charge Method (100mA cut-off) | Charge Method (100mA cut-off) | CC-CV (4.2±0.05V) | CC-CV (4.2±0.05V) |
| Charge Time | Standard (min), 0.5C | 180min | 134min |
| Charge Time | Rapid (min), 4A | 60min | 55min |
| Charge Current | Standard current (A) | 1.25 | 1.25 |
| Charge Current | Max. current (A) | 4.0 | 4.0 |
| Discharge | End voltage (V) | 2.5 | 2.5 |
| Discharge | Max. cont. current (A) | 20 | 20 |
| Discharge | Max. momentary pulse (A, <1sec) | 100 | 100 |
| Rated discharge Capacity | Standard (mAh) (0.2C) | 2,500 | 2.560 |
| Rated discharge Capacity | rated (mAh) (10A) | 2,450 | 2.539 |

[Full datasheet may be found here.](https://www.powerstream.com/p/INR18650-25R-datasheet.pdf)

## Energus Power Solutions Li8P25RT Technical Data

The Energus Power Solutions Li8P25RT is covered in Cells.

| Parameter | Comment | Min. | Typ. | Max. | Unit |
| - | - | - | - | - | - |
| Battery voltage | Allowed range | 2.50 | 3.60 | 4.20 | V |
| Battery capacity | 20A discharge to 2.5 V | 19.5 | 20.4 |  | Ah |
| Battery capacity | 20A discharge to 2.5 V | 70.2 | 73.4 |  | Wh |
| Battery capacity | 200A discharge to 2.5 V | 18.5 | 19.5 |  | Ah |
| Fast charge current | Forced air cooling |  | 一 | 40 | A |
| Fast charge current | No cooling, in a pack |  | 1 | 30 | A |
| Fast charge current | 10 sec. pulse, 50% SOC |  | 一 | 240 | A |
| Discharge current | Forced air cooling |  | 1 | 240 | A |
| Discharge current | No cooling, in a pack |  | 一 | 120 | A |
| Discharge current | 10 sec. pulse, fuse limited |  |  | 360 | A |
| Initial internal impedance | 1kHz after rated charge |  | 2.7 | 3.0 | mΩ |
| Internal fuse rating | Holding current |  |  | 360 | A |
| Working temperature | Discharge | -20 | 25 | 60 | ℃ |
| Working temperature | Charge | 0 | 25 | 45 | ℃ |
| Dimensions | ±0.5 mm |  | 39×69.5×87 |  | mm |
| Weight | Without fasteners |  | 0.427 | 0.429 | kg |

[Full datasheet may be found here.](https://www.energusps.com/shop/product/li8pt-li-ion-building-block-with-temp-sensor-3-6v-18c-37)

## Orion Battery Management System Technical Data

The Orion BMS is covered in Battery Management System.

| Specification Item | Min | Typ | Max | Units |
| - | - | - | - | - |
| Supply Voltage | 8 |  | 16 | Vdc |
| Supply Current—Active |  | 250 |  | mA |
| Supply Current—Sleep (Rev. D & E) |  |  |  | uA |
| Operating Temperature | -40 |  | 80 | C |
| Sampling Rate for Current Sensor |  | 8 |  | mS |
| Sampling Rate for Cell Voltages |  | 30 | 50 | mS |
| Isolation Between Cell Taps and Chassis / 12v Supply | 2.5 |  |  | kVrms |
| Isolation Between Cells 36-37, 72-73, 108-109, & 144-145 | 2.5 |  |  | kVrms |
| Digital Output Voltage (Open Drain) |  |  | 30 | V |
| Digital Output Sink Current (Rev. D & newer) |  |  | 175 | mA |
| Cell Voltage Measurement Range | 0.5 |  | 5 | V |
| Cell Voltage Measurement Error (over 1-5v range) |  |  | 0.25 | % |
| Cell Balancing Current |  |  | 200 | mA |
| Cell Current (Operating) |  | 5 |  | mA |
| Cell Current (Sleep) |  |  |  |  |
| Thermistor Accuracy |  |  |  | C |
| Cell Voltage Reporting Resolution |  | 1.5 |  | mV |

[Full datasheet may be found here.](https://www.orionbms.com/downloads/documents/orionbms_specifications.pdf)

## Coroplast High Voltage Wiring Technical Data

The Coroplast 50mm 2 and 16mm 2 cable is covered in Wiring

Derating: Threshold value curves of screened copper high-voltage cables

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_026.png)

[Full datasheet may be found here.](http://www.coroplast.de/fileadmin/user_upload/images/kabel-leitungen/coroplast_kabel_und_leitungen_en.pdf)

## TE Raychem 22 AWG Accumulator Low Voltage Wiring Technical Data

The Raychem 22 AWG low voltage wiring is covered in Wiring.

| TABLEI.CONSTRUCTIONDETAILS - PART NUMBER 1/ | TABLEI.CONSTRUCTIONDETAILS - WRE SIZE - (AWG) | TABLEI.CONSTRUCTIONDETAILS - (number x AWG) CONDUCTOR STRANDING | TABLEI.CONSTRUCTIONDETAILS - DIAMETEROF - CONDUCTOR STRANDED (in.) - MINIMUM | TABLEI.CONSTRUCTIONDETAILS - DIAMETEROF - CONDUCTOR STRANDED (in.) - MAXIMUM | TABLEI.CONSTRUCTIONDETAILS - FINISHED WIRE - RESISTANCE MAXIMUM AT 20°C (ohms/1000 ft.) | TABLEI.CONSTRUCTIONDETAILS - FINISHED WIRE - DIAMETER (in.) | TABLEI.CONSTRUCTIONDETAILS - FINISHED WIRE - (lbs/1000 ft.) MAXIMUM WEIGHT |
| - | - | - | - | - | - | - | - |
| 55A0111-30-* | 30 | 7 x 38 | .011 | .013 | 108.4 | .024 ± .002 | .66 |
| 55A0111-28-* | 28 | 7 x 36 | .014 | .016 | 68.6 | .027 ± .002 | .91 |
| 55A0111-26-* | 26 | 19 x 38 | .018 | .020 | 41.3 | .032 ± .002 | 1.4 |
| 55A0111-24-* | 24 | 19 x 36 | .023 | .025 | 26.2 | .037 ± .002 | 2.0 |
| 55A0111-22-* | 22 | 19 X 34 | .029 | .031 | 16.2 | .043 ± .002 | 2.8 |
| 55A0111-20-* | 20 | 19 x 32 | .037 | .039 | 9.88 | .050 ± .002 | 4.3 |
| 55A0111-18-* | 18 | 19 x 30 | .046 | .049 | 6.23 | .060 ± .002 | 6.5 |
| 55A0111-16-* | 16 | 19 x 29 | .052 | .055 | 4.81 | .068 ± .002 | 8.3 |
| 55A0111-14-* | 14 | 19 x 27 | .065 | .069 | 3.06 | .085 ± .003 | 13.0 |
| 55A0111-12-* | 12 | 37 x 28 | .084 | .089 | 2.02 | .103 ± .003 | 19.7 |
| 55A0111-10-* | 10 | 37 x 26 | 106 | .113 | 1.26 | .128 ± .006 | 31.8 |
| 55A0111- 8-* | 8 | 133 x 29 | .158 | .173 | .701 | .188 ± .008 | 58.8 |

[Full datasheet may be found here.](http://www.mouser.com/ds/2/418/NG_CD_55A0111_R-681624.pdf)

## TE EV200AAANA Accumulator Insulation Relay Technical Data

The accumulator isolation relays are covered in Accumulator Insulation Relays.

## Performance Data

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_027.png)

[Full datasheet may be found here.](http://www.te.com/usa-en/product-1618002-7.html)

## Eaton Bussman 170M3418 Main Tractive System Fuse Technical Data

The Bussman 170M3418 tractive system fuse is covered in Fusing.

| Electrical Characteristics | Electrical Characteristics - Rated Current RMS-Amps | Electrical Characteristics - (z) (z) | Electrical Characteristics - (z) (z) | Electrical Characteristics - Losses at Rated | Ordering Information - -B/- Visual Indicator | Ordering Information - -BKN/- Type K Indicator for Micro | Ordering Information - -G/- Visual Indicator | Ordering Information - -GKN/- Type K Indicator for Micro | Ordering Information - Carton Qty. | Ordering Information - Carton Weight (kg) | Curves - BIF # |
| - | - | - | - | - | - | - | - | - | - | - | - |
|  | Size | Pre-arc | Clearing at 660V | Current |  |  |  |  |  |  |  |
|  | 40 | 40 | 270 | 9 | 170M3408 | 170M3458 | 170M3508 170M3509 | 170M3558 170M3559 | (-B/-) 10 (-G/-) | 2.40 |  |
|  | 50 | 77 | 515 | 11 | 170M3409 | 170M3459 |  | 10 | (-B/-) 10 (-G/-) | 2.40 |  |
|  | 63 | 115 | 770 | 14 | 170M3410 | 170M3460 | 170M3510 | 170M3560 | (-B/-) 10 (-G/-) | 2.40 |  |
|  | 80 | 185 | 1250 | 18 | 170M3411 | 170M3461 | 170M3511 | 170M3561 |  | 2.40 |  |
|  | 100 | 360 | 2450 | 21 | 170M3412 | 170M3462 | 170M3512 | 170M3562 |  | 2.40 |  |
|  | 125 | 550 | 3700 | 26 | 170M3413 | 170M3463 | 170M3513 | 170M3563 |  | 2.40 | 2.40 |
|  | 160 | 1100 | 7500 | 30 | 170M3414 | 170M3464 | 170M3514 | 170M3564 |  | 2.40 |  |
|  | 200 1* | 2200 | 15000 | 35 | 170M3415 | 170M3465 | 170M3515 | 170M3565 |  | 2.40 |  |
|  | 250 | 4200 | 28500 | 40 | 170M3416 | 170M3466 | 170M3516 | 170M3566 |  | 2.40 | 17056314 |
|  | 315 | 7000 | 46500 | 50 | 170M3417 | 170M3467 | 170M3517 | 170M3567 | 6 (-BKN/-) | 2.40 |  |
|  | 350 | 10000 | 68500 | 55 | 170M3418 | 170M3468 | 170M3518 | 170M3568 | 6 (-BKN/-) | 2.40 | 1.62 |
|  | 400 | 15000 | 105000 | 60 | 170M3419 | 170M3469 | 170M3519 | 170M3569 |  | 2.40 |  |
|  | 450 | 21000 | 140000 | 65 | 170M3420 | 170M3470 | 170M3520 | 170M3570 |  | 2.40 |  |
|  | 500 | 27000 | 180000 | 70 | 170M3421 | 170M3471 | 170M3521 | 170M3571 | 6 (-GKN/-) | 2.40 |  |
|  | 550 | 34000 | 230000 | 75 | 170M3422 | 170M3472 | 170M3522 | 170M3572 | 6 (-GKN/-) | 2.40 | 1.62 |
|  | 630 | 48500 | 325000 | 80 | 170M3423 | 170M3473 | 170M3523 | 170M3573 |  | 2.40 |  |

![Image](Wisconsin%20Racing%20WR-217e%20-%20HV%20Accumulator%20Design%20Report_files/img_028.png)

[Full datasheet may be found here.](http://www.mouser.com/ds/2/87/51b3f0c2-01da-47b6-888a-1f0a2c504108-182178.pdf)

## Eaton Bussmann 160LET Motor Controller Fuse Technical Data

The Bussman 160LET motor controller fuses are covered in Fusing.

| Catalog - numbers | Type | Rated - current - RMS-amps | Pt (A2 sec) - Pre-arc | Pt (A2 sec) - Clearing - at 120V | Pt (A2 sec) - Clearing - at 240V | Watts - loss |
| - | - | - | - | - | - | - |
| 6LCT |  | 6 | 2 | 6 | 9 | 1.0 |
| 10LCT |  | 10 | 3.8 | 12 | 22 | 2.5 |
| 12LCT | LCT | 12 | 7 | 22 | 32 | 2.5 |
| 16LCT |  | 16 | 20 | 50 | 100 | 2.5 |
| 20LCT |  | 20 | 25 | 80 | 160 | 4.0 |
| 25LET |  | 25 | 18 | 120 | 250 | 4.0 |
| 32LET |  | 32 | 32 | 200 | 450 | 5.0 |
| 35LET |  | 35 | 50 | 320 | 600 | 5.0 |
| 50LET |  | 50 | 100 | 500 | 1400 | 7.0 |
| 63LET | LET | 63 | 180 | 1100 | 2200 | 9.0 |
| 80LET |  | 80 | 300 | 1900 | 3800 | 10.0 |
| 100LET |  | 100 | 600 | 3800 | 7500 | 10.0 |
| 125LET |  | 125 | 600 | 3800 | 7500 | 16.0 |
| 160LET |  | 160 | 1100 | 7000 | 16000 | 20.0 |

[Full datasheet may be found here.](http://www.cooperindustries.com/content/dam/public/bussmann/Electrical/Resources/Catalogs/bus-ele-cat-1007-06-hsf-bs88.pdf)

## ElCon PFC 5000 5kW 96V 44A Battery Charger Technical Data

The Elcon PFC 5000 charger is covered in Charging.

## Specifications

| Spec Model | Ouput Voltage -Nominal | Ouput Voltage -Maximum | Output Current -Maximum 230vac | Output Current -Maximum 115vac |
| - | - | - | - | - |
| TCCH-48-80 | 48V | 66V | 80A | 38A |
| TCCH-60-70 | 60V | 82V | 70A | 30A |
| TCCH-72-56 | 72V | 96V | 56A | 26A |
| TCCH-84-50 | 84V | 112V | 50A | 22A |
| TCCH-96-44 | 96V | 130V | 44A | 20A |
| TCCH-120-36 | 120V | 168V | 36A | 15A |
| TCCH-144-30 | 144V | 192V | 30A | 13A |
| TCCH-168-24 | 168V | 233V | 24A | 12A |
| TCCH-216-20 | 216V | 289V | 20A | 8A |
| TCCH-288-15 | 288V | 389V | 15A | 7.5A |
| TCCH-312-14 | 312V | 417V | 14A | 7A |

Note: red = in stock, black = special order.

Technical Features

| AC Input Voltage Range | AC85V~AC265V |
| - | - |
| AC Input Frequency | 45~65 Hz |
| AC Power Factor | ≥0.98 |
| Full Load Efficiency | ≥93 |
| Mechanical Shock & Vibration Resistance Level | Conformance to SAEJ1378 Standard |
| EnvironmentalEnclosure | IP46 |
| Operating Temperature | -40℃+55℃ |
| Storage Temperature | -40℃+100℃ |
| Mechanical Dimensions | 365mm×352mm×139mm |
| Net Weight | 13.80kg |

[Full datasheet may be found here.](http://www.elconchargers.com/catalog/item/7344653/7638130.htm)

## References

- [1] 2015, "Formula E: New timeline for electric car battery." from batterybro.com.
- [2] J. M. Melillo, T. C. Richmond, and G. W. Yohe, " Climate Change Impacts in the United States," The Third National Climate Assessment. U.S. Global Change Research Program., 2014.
- [3] 2015, "Delft DUT15." from racecar-engineering.com.
- [4] Ma, Y. and Teng, H., "Comparative Study of Thermal Characteristics of Lithiumion Batteries for Vehicle Applications," SAE Technical Paper 2011-01-0668, 2011, doi:10.4271/2011-01-0668.
- [5] Giese, R. and Walsh, W., "A Least-Cost Method for Prioritizing Battery Research," SAE Technical Paper, 1983, doi:10.4271/830221.
- [6] 2017-18 Formula SAE® Rules - September 2, 2016 Rev A
- [7] Samsung, "Introduction of INR18650-25R" Samsung SDI, Oct. 2013.
- [8] Oke, S. A., Oyekunle, A. A., Salau, T. A. O., et. al. "Estimation of Thermal Contact Resistance in Metal-Plastic interface of Semiconducting Electronic Devices" Int. J. Nanoelectronics and Materials 2 No.1 (2009)
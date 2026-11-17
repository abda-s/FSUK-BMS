<!-- Converted from FST Lisboa - BMS for Formula Student (Guedes Thesis).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_001.png)

## Battery Management System for Formula Student

## Miguel Ângelo da Silva Guedes Nº 55224

Dissertation to obtain the Master's Degree in

## Electrical and Computer Engineering

## Jury

President: Prof. Marcelino Santos

Chairman: Prof. António Serralheiro

Advisor: Prof. Moisés Piedade

Co-Advisor: Prof. Francisco Alegria

## Acknowledgements

One name on a page of this document is not enough to really thank for the help I've received through this journey. The order of the names presented here doesn't mean any preference, as I'm deeply thankful to all of them.

I'll start by thanking all the people that I have worked with during the project presented in this document, as well to all the members from the Projecto FST current team who have accompanied me in all the ups and downs we had, and to the previous teams, who always were an inspiration.

To my advisor, Moisés Piedade, who embraced this idea and supported me the best way he could, like he always supported the Projecto FST team.

To my friends in the Electronics team members from Projecto FST, David Tempero, Miguel Silva and Pedro Oliveira, as well as to Rui Andrade from the previous team, for your friendship, support and cooperation, even when a fire extinguisher was required.

To Paulo Quental for your help and in the design and construction of the battery, has well as for the company and support in the late dark evenings.

To André Cereja, Team leader of the ProjectoFST, for his support when choosing this path, as well as when things went according to Murphy's Law.

To Luís Monteiro and Ricardo Santos for their help with the construction of the L supports for the modules presented here.

To Pina dos Santos, for his patience and help soldering and constructing PCBs; Marli Gomes, Manuel dos Santos and Agostinho Fernandes for providing the tools, materials and access for the equipment required on the development of this work.

To Carlos Brito, for his help and comprehension whether we needed to move a power supply, a fridge or a cleaning team and replacement of the fire extinguishers.

To my friends Bruno Jacinto, Carlos Lavadinho, Ivo Monteiro, João Gil, Nuno Pereira, Ana Rita Silva, Ricardo Oliveira, Paulo Pereira and Ricardo Pascoal, for accompanying me through these amazing years in the late nights working, in the late nights partying, in brainstorming sessions or in leisure session, a big, thank you.

To my Co-Advisor, Francisco Alegria, for his support in reviewing this documents;

To Professor Leonel Sousa, for his help with the acquisition of the battery cells used in this project.

To all my friends, not mentioned here, whose paths crossed mine during this journey.

Last, but not in any way least, to my parents António Guedes and Eulália Moringa, for their amazing efforts and sacrifices to support me during these years; to my brother, Diogo Guedes who has always been there for me whenever I needed; to my girlfriend Joana Durão, for your love, patience and encouragement; a Big, Big thank you!! Thank you for being part of my life, your love and dedication that made me the person I am today, even when I deprived you of my attention and affection.

## Resumo

O objectivo desta tese é projectar, construir e testar um Sistema de Gestão da Bateria para o mais recente protótipo desenhado pela equipa Projecto Formula Student Técnico (Projecto FST), o FST04e. Este será um veículo movido a energia eléctrica projectado para participar em corridas de Formula Student, onde as equipas competem entre si num ambiente de engenharia. O protótipo terá um sistema de propulsão composto por um motor eléctrico, um controlador de potência e uma bateria de 153V - 50Ah composta por 240 células Lítio fosfato de ferro (LiFePO4).

O sistema a ser desenvolvido tem uma arquitectura distribuída composta por uma placa Mestre e várias placas Escravo, comunicando através de um barramento CAN. O módulo Mestre lida com todas as comunicações entre as placas Escravo e sistema eléctrico do carro; armazena todas as informações numa memória flash; determina vários parâmetros da bateria, como o estado de carga (SOC); acciona o sistema de refrigeração a ar e gere os relés de activação do sistema. Garante ainda que todas as condições para operar o carro com segurança são cumpridas. As placas Escravo monitorizam diversos parâmetros das células, como a tensão e a temperatura, e enviam os mesmos ao módulo Mestre. Uma vez que a bateria será descarregada quase na sua totalidade durante uma corrida, foi decidido não implementar, por enquanto, qualquer tipo de sistema activo para equilibrar a carga das células, dado o tempo necessário para equilibrar as células e o peso adicional deste sistema. Desta forma, a complexidade e o custo do sistema são reduzidos, sendo o equilíbrio feito passivamente e apenas durante o carregamento da bateria.

Dado o tipo de veículo e competição, deverão ser cumpridos certos requisitos em termos de capacidade do sistema e gestão de projecto. Por um lado, o sistema deve ser muito fiável e capaz de suportar um ambiente hostil, ou seja, fortes vibrações mecânicas, temperaturas elevadas, derrame de líquidos e não ser vúlneravel a interferência electromagnética. Por outro lado deve ser funcional, leve e barato.

Palavras-Chave: Sistema de Gestão da Bateria, BMS, Lítio, CAN-Bus, Formula Student, Veículo Eléctrico

## Abstract

The purpose of this thesis is to design, build and test a Battery Management System (BMS) for the latest prototype designed by the Projecto Formula Student Técnico team (Projecto FST), the FST04e. This will be a Battery Electric Vehicle (BEV) designed to participate in Formula Student events where teams compete against each other in a real world, engineering environment. The prototype will have an electric drive train composed by an electric motor, a power controller and a 153V - 50Ah battery composed by 240 Lithium-Iron-Phosphate (LiFePO4) cells.

The system being developed is a distributed BMS composed by one Master board and several Slave boards communicating through a CAN bus. The Master module handles all the communications between the Slave modules and the car's electrical system, stores all the information on a flash memory, estimates several parameters of the battery - such as the State-Of-Charge - triggers the air cooling system and manages the master relays operation. It assures that all the conditions to safely operate the car are met. The Slave modules monitor several cell parameters - like cell voltage and temperature - and report them to the Master module. Since the battery will be almost completely drained during the competition it was decided not to implement, for now, any type of active cell balancing system, given the time these systems usually take to balance the cells, and the added weight of these. This way, the complexity and cost of the system is reduced.

Given the type of vehicle (and competition), certain requirements are set in terms of both system capabilities and project management. In one hand the system must be very reliable and be able to support a harsh environment, namely vibration, heat, liquids and electromagnetic interference, and on the other hand it must be lightweight, cheap and user-friendly.

Keywords: Battery Management System, BMS, Lithium, CAN-Bus, Formula Student, Electric Vehicle

## Contents

| Acknowledgements ........................................................................................................................... iii | Acknowledgements ........................................................................................................................... iii |
| - | - |
| Resumo ............................................................................................................................................. v | Resumo ............................................................................................................................................. v |
| Abstract ............................................................................................................................................ vii | Abstract ............................................................................................................................................ vii |
| Contents ............................................................................................................................................ix | Contents ............................................................................................................................................ix |
| List of Tables ................................................................................................................................... xiii | List of Tables ................................................................................................................................... xiii |
| List of Figures ...................................................................................................................................xv | List of Figures ...................................................................................................................................xv |
| List of Abbreviations ....................................................................................................................... xvii | List of Abbreviations ....................................................................................................................... xvii |
| 1 Introduction ................................................................................................................................ | 1 Introduction ................................................................................................................................ |
|  | 1 1.1. Project Scope and Objectives ......................................................................................... 2 |
|  | 1.2. State of the art ................................................................................................................ 3 |
|  | 1.3. System definition ............................................................................................................ 3 |
|  | 1.4. Structure of the thesis ..................................................................................................... 4 |
| 2. Specifications and System Architecture ...................................................................................... 5 | 2. Specifications and System Architecture ...................................................................................... 5 |
|  | 2.1. Overview and specifications ........................................................................................... 5 |
|  | 2.2. Battery Parameters......................................................................................................... 6 |
|  | 2.2.1. Cell and Battery voltages ............................................................................................ 6 |
|  | 2.2.2. Charge or Capacity ..................................................................................................... 7 |
|  | 2.2.3. State-Of-Charge ......................................................................................................... 7 |
|  | 2.2.4. Specific Energy ........................................................................................................... 7 |
|  | 2.2.5. Energy Density ........................................................................................................... 8 |
|  | 2.2.6. Specific Power ............................................................................................................ 8 |
|  | 2.3. Battery Technologies ...................................................................................................... 9 |
|  | 2.3.1. Lead-Acid Batteries .................................................................................................... 9 |
|  | 2.3.2. Nickel based batteries................................................................................................. 9 |
|  | 2.3.3. Lithium based batteries ............................................................................................. 10 |
| 2.4. Cell Balancing .............................................................................................................. 15 | 2.4. Cell Balancing .............................................................................................................. 15 |
|  | 2.4.1. Dissipative balancing ................................................................................................ 15 |
|  | 2.4.2. Non-dissipative balancing ......................................................................................... 16 |
|  | 2.5. BMS architectures ........................................................................................................ |
| 17 | 17 |
|  | 2.5.1. Centralized BMS ....................................................................................................... 17 2.5.2. Distributed BMS ........................................................................................................ 18 |
|  | 2.5.3. Modular BMS ............................................................................................................ 20 |

| 2.6. | Cell configuration .......................................................................................................... 20 |
| - | - |
| 2.7. CAN Bus | ...................................................................................................................... 21 |
| 2.8. Connections and Geometry .......................................................................................... | 22 |
| 2.9. Pre-charge Circuit ........................................................................................................ | 25 |
| 2.10. Discharge Circuit .......................................................................................................... | 26 |
| 2.11. Fusing .......................................................................................................................... | 27 |
| 2.12. Current Sensor ............................................................................................................. | 28 |
| 2.13. Accumulator Insulation Relays ...................................................................................... | 30 |
| 2.14. Tractive-System-Active-Light ........................................................................................ | 30 |
| 2.15. Ready-To-Drive-Sound ................................................................................................. | 31 |
| 2.16. Cooling ......................................................................................................................... | 31 |
| 2.17. ESS architecture .......................................................................................................... | 33 |
| 3. Slave Module ............................................................................................................................ | 35 |
| 3.1. Architecture .................................................................................................................. | 35 |
| 3.2. DC/DC Converter ......................................................................................................... | 36 |
| 3.3. PIC microcontroller ....................................................................................................... | 36 |
| 3.4. Balancing Load............................................................................................................. | 37 |
| 3.5. Sensors ........................................................................................................................ | 39 |
| 3.5.1. Cell voltage measurement ........................................................................................ | 39 |
| 3.5.2. Temperature sensor ................................................................................................. | 39 |
| 3.5.3. Balancing Current ..................................................................................................... | 40 |
| 3.6. CAN-bus interface | ........................................................................................................ 40 |
| 3.7. Printed Circuit Board .................................................................................................... | 41 |
| 3.8. Software ....................................................................................................................... | 43 |
| 3.8.1. Normal Mode ............................................................................................................ | 44 |
| 3.8.2. Alert Mode ................................................................................................................ | 44 |
| 3.8.3. Critical Mode ............................................................................................................ 3.8.4. Charging | 44 ................................................................................................................... 45 |
| 4. Module .......................................................................................................................... |  |
| Master | 47 |
| 4.1. Overview ...................................................................................................................... | 47 |
| 4.2. dsPIC FST Module ....................................................................................................... | 47 |
| 4.3. I/O Shield Hardware ..................................................................................................... | 48 |
| 4.3.1. Relay driver | .............................................................................................................. 49 |

|  | 4.3.2. Fan Control ............................................................................................................... 50 |
| - | - |
| 4.3.3. Ready-To-Drive-Sound | ............................................................................................. 52 |
| 4.3.4. Data logging | ............................................................................................................. 52 |
| 4.3.5. Start Switch | .............................................................................................................. 53 |
| 4.4. Printed Circuit Board | .................................................................................................... 54 |
| 4.5. Software | ....................................................................................................................... 56 |
| 4.5.1. Timer | interruption...................................................................................................... 56 |
| 4.5.2. CAN message interruption | ........................................................................................ 57 |
| 4.5.3. Start Switch interruption | ............................................................................................ 58 |
| 4.5.4. Charging | ................................................................................................................... 58 |
| 5. Test and Implementation | .......................................................................................................... 59 |
| 5.1. Test | .............................................................................................................................. 59 |
| 5.2. Implementation | ............................................................................................................. 60 |
| 6. Conclusions | .............................................................................................................................. 65 |
|  | ................................................................................................................ 65 |
| 6.1. Cost analysis 6.2. Future work | .................................................................................................................. 67 |
| Bibliography | .................................................................................................................................... 69 |
| Appendix A ...................................................................................................................................... | 71 |
| Appendix B | ...................................................................................................................................... 75 |
| B.1 Message arbitration ......................................................................................................... B.2 Error handling | 75 .................................................................................................................. 75 |
| B.3 Message format | ............................................................................................................... 75 |
| B.4 Bit Appendix C ...................................................................................................................................... | timming....................................................................................................................... 76 79 |
| Appendix D | ...................................................................................................................................... 81 |
| Appendix E ...................................................................................................................................... | 83 |
| Appendix F ...................................................................................................................................... | 85 |
| F.1 Electrical Schematics ....................................................................................................... | 85 |
| F.2 Aluminium connectors and support mounts ...................................................................... | 86 |
| F.3 BMS Slave Parameters .................................................................................................... | 87 |
| F.4 BMS FST04e CAN Specification dsPIC FST V1.3 Schematics | ...................................................................................... 88 |
| Appendix G | ..................................................................................................................................... 97 |
|  | ........................................................................................... 97 |
| G.1 |  |

| G.2 BMS Master I/O Shield Schematics ................................................................................. 98 |
| - |
| Appendix H ...................................................................................................................................... 99 |
| H.1 Slave Modules Voltage and Resistance Measurments ..................................................... 99 |
| H.2 Slave Modules Voltage and Temperature measurements validation ............................... 101 |

## List of Tables

| table 2.1 - System parameters .................................................................................................... 6 |
| - |
| table 2.2 - Cell characteristics ................................................................................................... 14 |
| table 2.3 - Electrical resistance of the cell connections .............................................................. 24 |
| table 2.4 - Dissipated power at 230A ......................................................................................... 25 |
| table 2.5 - Dissipated power at 500A ......................................................................................... 25 |
| table 2.6 - Pre-charge over time ................................................................................................ 26 |
| table 2.7 - Discharge over time ................................................................................................. 27 |
| table 5.1 - Maximum measurement deviations .......................................................................... 61 |
| table 6.1 - Slave Module cost breakdown .................................................................................. 66 |
| table 6.2 - Master Module cost, in a 50 unit production .............................................................. 66 |
| table A.1 - FST04e Specifications ............................................................................................. 72 |
| table B.1 - Slaves CAN Baudrate Registers .............................................................................. 77 |
| table B.2 - Master CAN Baudrate Registers .............................................................................. 77 |
| table D.1 - Agnimotors 95-R Specifications ............................................................................... 81 |
| table F.1 - Slave Parameters .................................................................................................... 87 |
| table H.1 - Slave modules voltage and resistance measurements ........................................... 100 |
| table H.2 - Slave Modules Voltage and Temperature measurements validation ........................ 102 |

## List of Figures

| figure 1.1 - Typical EV propulsion | ...................................................................................... 1 |
| - | - |
| figure 1.2 - FST04e Design | ................................................................................................ 2 |
| figure 2.1 - FST04e propulsion architecture ........................................................................ | 5 |
| figure 2.2 - Ragone plot for Lead Acid and Nickel Cadmium Traction Batteries | ................... 8 |
| figure 2.3 - 2 nd Gen Toyota Prius NiHM battery | ................................................................ 10 |
| figure 2.4 - Tenergy 18650 Li-ion cell ............................................................................... | 11 |
| figure 2.5 - Kokam Cell for RC models | ............................................................................. 12 |
| figure 2.6 - Example of a laptop battery fire | ...................................................................... 13 |
| figure 2.7 - China Headway 38120S cell | .......................................................................... 14 |
| figure 2.8 - Example of an extremely imbalanced battery.................................................. | 15 |
| figure 2.9 - Non-dissipative cell balancing techniques: (a) Cell-to-Battery; (b) Battery-to-Cell; (c) Cell-to-Cell .................................................................. | 16 |
| figure 2.10 - Centralized BMS .......................................................................................... | 18 |
| figure 2.11 - Distributed BMS | ........................................................................................... 19 |
| figure 2.12 - Distributed BMS with serial communications................................................. | 19 |
| figure 2.13 - Modular BMS ............................................................................................... | 20 |
| figure 2.14 - Cell distribution inside the container | ............................................................. 21 |
| figure 2.15 - Cell group, trapezoidal shape ....................................................................... | 22 |
| figure 2.16 - Cell group, linear shape ............................................................................... | 23 |
| figure 2.17 - Cell column assembly .................................................................................. | 23 |
| figure 2.18 - Column assemble inside container ............................................................... | 24 |
| figure 2.19 - Pre-Charge circuit schematics | ...................................................................... 26 |
| figure 2.20 - Discharge circuit schematics | ........................................................................ 27 |
| figure 2.21 - Siemens SITOR semiconductor fuse | ............................................................ 28 |
| figure 2.22 - rect() function used in the ZOH model | .......................................................... 29 |
| figure 2.23 - ZOH signal reconstruction ............................................................................ | 29 |
| figure 2.24 - Current sensor schematics | ........................................................................... 30 |
| figure 2.25 - RTDS Wiring ................................................................................................ | 31 |
| figure 2.26 - Thermal analysis of the Headway 38120S cells at 10C discharge | ................. 32 |
| figure 2.27 - FloWorks CFD simulations | ........................................................................... 33 |
| figure 2.28 - ESS architecture .......................................................................................... | 33 |
| figure 3.1 - Slave Module Architecture.............................................................................. | 35 |
| figure 3.2 - DC/DC converter schematics ......................................................................... | 36 |
| figure 3.3 - PIC18F2480 Schematics ................................................................................ | 37 |
| figure 3.4 - Balancing Circuit Schematics | ......................................................................... 38 |
| figure 3.5 - TMP20 temperature sensor Schematics | ......................................................... 40 |
| figure 3.6 - CAN transceiver Schematics | .......................................................................... 41 |
| figure 3.7 - PCB drawings, top and bottom layers | ............................................................. 41 |
| figure 3.8 - PCB Structure | ................................................................................................ 42 |

| figure 3.9 - Assembled Slave module ............................................................................... | 42 |
| - | - |
| figure 3.10 - Top and Side view of a 5 cell module with the slave BMS installed | ............... 43 |
| figure 3.11 - Program flow | ................................................................................................ 45 |
| figure 4.1 - Master BMS Architecture | ............................................................................... 47 |
| figure 4.2 - dsPIC FST module | ......................................................................................... 48 |
| figure 4.3 - Relay Drivers Schematics | .............................................................................. 49 |
| figure 4.4 - AIR supply connector ..................................................................................... | 49 |
| figure 4.5 - Schematic overview of the car's shutdown system, FSE rules, 2011 ............... | 50 |
| figure 4.6 - FAN speed control and measurement schematics .......................................... | 51 |
| figure 4.7 - Reversed driver input/output | .......................................................................... 51 |
| figure 4.8 - FAN expansion connector .............................................................................. | 51 |
| figure 4.9 - RTDS Schematics .......................................................................................... | 52 |
| figure 4.10 - SD data logger schematics ........................................................................... | 53 |
| figure 4.11 - Start Switch Circuit Schematics .................................................................... | 54 |
| figure 4.12 - I/O Shield PCB layout................................................................................... | 54 |
| figure 4.13 - PCB Structure .............................................................................................. | 55 |
| figure 4.14 - PCB Tri-dimensional view ............................................................................ | 56 |
| figure 5.1 - BMS Slave Module V1.1 ................................................................................ | 59 |
| figure 5.2 - Charging test | ................................................................................................. 59 |
| figure 5.3 - PCBs before assembling ................................................................................ | 60 |
| figure 5.4 - Assembled Modules, top and bottom layers | ................................................... 61 |
| figure 5.5 - Assembled Cell Groups.................................................................................. | 62 |
| figure 5.6 - Glass-Fibre-Reinforced-Plastic Structure | ........................................................ 62 |
| figure 5.7 - Assembled Columns ...................................................................................... | 62 |
| figure 5.8 - Assembled Battery | ......................................................................................... 63 |
| figure A.1 - The FST04e on the AutoCross Event, FSE2011 ............................................ | 73 |
| figure A.2 - The Projecto FST team | .................................................................................. 73 |
| figure A.3 - The FST04e at the FSS2011 event ................................................................ | 74 |
| figure B.1 - CAN 2.0B data frame | ..................................................................................... 76 |
| figure B.2 - A CAN bit and Its Segments .......................................................................... | 76 |
| figure C.1 - 5 Cell group connector, trapezoidal shaped | ................................................... 79 |
| figure C.2 - 5 Cell group connector, linear shaped ............................................................ | 79 |
| figure C.3 - Cell Blocks interconnector ............................................................................. | 79 |
| figure D.1 - Agnimotors 95-R Power and Torque curves | ................................................... 81 |
| figure E.1 - Siemens Fuse Characteristic curve ................................................................ | 83 |
| figure F.1 - Slave Modules Full Schematics ...................................................................... | 85 |
| figure F.2 - L shaped BMS connector, minus terminal | ...................................................... 86 |
| figure F.3 - L shaped BMS connector, Plus terminal | ......................................................... 86 |
| figure G.1 - dsPIC FST Schematics Schematics | ................................................................................. 97 |
| figure G.2 - I/O Shield | ................................................................................... 98 |

## List of Abbreviations

A/D

Analogue to Digital

AIR

Accumulator Insulation Relay

BEV

Battery Electric Vehicle

BMS

Battery Management System

CAN

Controller Area Network

CMM

Cell Management Module

CMS

Cell Management System

DOD

Depth of Discharge

dsPIC

digital signal Peripheral Interface Controller

EEPROM Electronically Erasable Programable Read-Only-Memory

ESS

Energy Storage System

EV

Electric Vehicle

FSE

Formula Student Electric

FST

Formula Student Técnico

GFRP

Glass-Fibre-Reinforced-Plastic

HV

High Voltage

HVD

High Voltage Disconnect

I 2 C

IMD

Inter-Integrated Circuit

Insulation Monitoring Device

IMechE Institute of Mechanical Engineers

LIN

Local Interconnect Network

MIPS

Millions of Instructions Per Second

PCB

Printed Circuit Board

RS-232 Recommended Standard 232

RS-485 Recommended Standard 485

RTDS

Ready-To-Drive-Sound

SAE

Society of Automotive Engineers

SOC

State of Charge

SPI

Serial Peripheral Interface

TSAL

Tractive-System-Active-Light

VDI

Verein Deutscher Ingenieure

## 1 Introduction

In the automotive industry, the Electric Vehicle has always been seen has a poor alternative to internal combustion powered vehicles due to its low range, long charging times and high cost. Given the current economic downturn and global climate changes, the search for cheaper and cleaner means of transport has increased its popularity massively, which has cleared the way for researchers around the world to improve and develop technologies used in this vehicles.

The typical architecture of an EV consists on an energy storage unit, an electric motor and a power converter, which transfers the energy, stored to the electric motor (figure 1.1). On this work, we will focus mainly on the first one, the energy storage unit, which is typically the heaviest, the most expensive and the most dangerous component on an electric vehicle.

figure 1.1 - Typical EV propulsion

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_002.png)

With the current development in battery technology, mainly with Lithium, some of the downsides of electric vehicles have been improved substantially, with shorter charging times and longer ranges. While this technology has many advantages concerning weight, power and energy densities and maximum discharge currents, it is also a dangerous technology, which can be seen on numerous cases of exploding laptops and mobile phones equipped with Lithium batteries. Therefore, it is imperative to monitor the conditions of battery, to ensure that all the cells are working within the normal functioning parameters, assuring the safety of the battery and its users. The Battery Management Systems fulfil this purpose, typically monitoring every cell voltage and temperatures to ensure the safety requirements are met. Another purpose for the BMS is to ensure the voltage of every cell is above the minimum working voltages, to ensure the cell integrity. This is especially important on Lithium cells, since the cell becomes permanently damaged if its voltage drops below a certain value and will need replacement. In addition, it is important to ensure that when charging, every cell is charged at the same level, which is a very important factor when considering the size of an automotive battery, and the amount of cells that compose it.

The objective of this work is to design and implement a Battery Management System from scratch and apply it on a battery designed to fit a racing car, which will compete in Formula Student series. It focuses not only the development of the BMS, but also the Battery itself where the system is implemented, since the development of this was done at the same time.

## 1.1. Project Scope and Objectives

This work is primarily aimed at a particular prototype vehicle (figure 1.2), built at Instituto Superior Técnico (IST) to participate in Formula Student competitions. These competitions, organized by the Society of Automotive Engineers (SAE) and other engineers societies (IMechE, VDI, others), are held every year in different countries, not as part of a world championship, but as individual events, each one with its own character and challenges. In these events, teams of students compete with their prototypes in many different ways, from the dynamic performance of the vehicles on track to the way they manage their team. More information about Formula Student and the team from IST - Projecto FST, can be found in Appendix A.

MAV

figure 1.2 - FST04e Design

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_003.png)

Developing the system for a Formula Student prototype sets certain requirements in terms of both system capabilities and project management. In one hand, the system must be able to sustain a harsh environment, namely vibration, heat, liquids and electromagnetic interference, and on the other hand, it must be lightweight, cheap and user-friendly.

The main objectives for this work were to develop a system that:

- was able to function under harsh conditions;
- was able to monitor the voltage and temperature of each cell, or group of cells in a battery:
- o Voltage reading range: 1.8V to 4.0V
- o Maximum Voltage reading error: ±0.05V;
- o Temperature reading range: -20ºC to 80ºC
- o Maximum Temperature reading error: ±5ºC
- balanced the voltage between cells;
- o Maximum accepted Voltage difference between balanced cells: 0.01V
- determined the State-Of-Charge of the battery;
- controlled the battery activation, cooling system, pre-charge and discharge circuits;

- guarantied the safety of the vehicle users, as well as the battery integrity;
- was easy to assemble;
- worked independently of the energy capacity of the battery
- o Has to withstand at least 50Ah
- had a low cost;

This system was designed to be implemented on the battery of the FST04e which was designed from scratch by the team members, which means the packaging was also a major concern of the system.

## 1.2. State of the art

Thanks to the consumer electronics industry, there has been a constant evolution in battery technologies and management systems. With the popularity of portable devices, such has laptops, netbooks, tablet pcs and cell phones, growing every day, the battery life has become one the key decision factors for the buyers, which means the manufacturers invest a lot in the research of better technologies for their batteries.

Most of the batteries available on portable devices on today's market are lithium derived which offers better power and energy densities, being the most popular the Lithium Cobalt Oxide (LiCoO2) battery, largely used in most of today's portable electronic gadgets. The downside of these technologies is the fact that they are highly intolerable if they are over charged, over discharged, or exposed to high temperatures. Here it becomes essential for manufacturers to monitor the batteries condition permanently, to avoid any malfunctioning resulting in fire or explosion, as there are several documented cases of laptops and mobile phones whose batteries suddenly burst in to flames, or even exploded.

Thanks to the grown popularity of electric vehicles, some manufacturers turned their attention to this market, developing integrated circuits for larger batteries. The major companies with products already available on the market are Microchip and ATMEL, booth with fully developed and serializable ICs, which allow the control of a number of cells. These also offer communications with other devices, making them relatively easy to integrate a custom developed BMS. Other manufacturers develop not only the ICs but offer their customers fully developed solutions, which can be custom built for each individual battery. One of the most established companies is Elithion [2], who develops their own ICs, sells fully developed modules and offers consulting services.

## 1.3. System definition

This work consists on the development and assembly of several components to monitor and manage the battery. The main components are the Cell Management Modules (also called slave modules), the Master Module, and several peripheral devices such as cooling fans, relays and precharge and discharge resistors.

The Cell Management Modules consist on a PCB with a microcontroller and a set of sensors whose main job is to monitor a cell pack to which they are connected. It is required to have one module per cell pack, therefore it must be compact, reliable, have low power consumption and a low cost. The main battery on this EV will have 48 of these connected to the Master Module.

The Master module communicates with all the cell management modules and the vehicle electronic system. Its main functions are monitoring the battery condition, activate the cooling system and manage the relays according to the driver's request and battery conditions. There is only one master module required for this type of BMS. The Master module uses two independent CAN bus working at 1Mbit.s -1 for the communications, one for the vehicle electronics and the other for a dedicated battery network for the communications with the Cell Management modules.

## 1.4. Structure of the thesis

This work is divided in six chapters.

In chapter 2 the specifications of the system will be presented, as well as the architecture of the vehicle and the battery, with all the components that were developed for the implementation of the system.

In chapter 3 the BMS Slave Modules architecture and components will be explained, has well as the software developed to monitor the battery

In chapter 4 the BMS Master Module is presented with its main components and developed hardware.

In chapter 5 the implemented system will be demonstrated along with the conducted bench tests, as well as the expected results.

Finally, in chapter 6, conclusions are drawn regarding the design and implementation of the system in the vehicle, along with the cost estimations and future work.

## 2. Specifications and System Architecture

In this chapter several aspects of the Energy Storage System will be analysed, as well as its integration with the vehicles system and its architectures.

## 2.1. Overview and specifications

The first step towards the development of this electric vehicle was a MATLAB model made in [1] that estimated the energy required to complete the 22km endurance race at Formula SAE events. It was required to have a good estimation of the cars weight, power and torque in order to have a reliable model, which meant all the main components had to be defined early in the design.

In [1], several types of motors and batteries were compared to see which best fitted a racing vehicle, built with a very limited budget. It was decided to use Brushed Permanent Magnet Direct Current motors, which have a very high power density at a low cost, and are simple to control, meaning that the motor controllers available on the market also have a low cost.

For the Energy Storage System it was decided to use lithium technology, in one of its safest and cheapest forms, Lithium-Iron-Phosphate (LiFePO4), a technology that has better power and energy densities compared to Lead-Acid and Nickel based batteries, while keeping a cost just over these. To determine the capacity of the Energy Storage System, a MATLAB model was developed which was based on the drivers demand on the previous prototype.

The propulsion system (figure 2.1) is composed mainly by 3 components: the Energy Storage System (also known as High Voltage Accumulator), the Motor controller and the Electric Motors which are two brushed Permanent Magnet Direct Current (PMDC) motors connected to the same sprocket, electrically connected in series (for the purposes of this work, these units are considered the equivalent of one single Motor, since they are connected in series).

figure 2.1 - FST04e propulsion architecture

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_004.png)

The energy is stored in one accumulator located behind the driver seat, and transferred to the motors using one student built motor controller. Power is transferred to the wheels through a chain connected to a mechanical differential. This is a simple and reliable solution, which is what the team was aiming for in the first EV.

The system main parameters are described in table 2.1.

table 2.1 - System parameters

| System Parameters: | System Parameters: |
| - | - |
| Maximum Tractive System voltage [V] | 175,2V |
| Nominal Tractive System voltage [V] | 153,6V |
| Maximum Continuous Discharge Current [A] | 500A |
| Control System Voltage [V] | 12,8V |
| Motor Type | Brushed Permanent Magnet DC motor |
| Total number of motors | 2 |
| Maximum combined motor power [kW] | 60kW |
| Accumulator Capacity [kWh] | 7,7kWh |

The FSE rules to which this vehicle complies, state that any system with a voltage above 40V DC is considered the vehicles High Voltage system; therefore, the tractive system is considered and named the HV circuit on this vehicle.

## 2.2. Battery Parameters

When designing a battery for any application, there are several parameters that must be taken into account, in order to assure that the best technology for the desired application is used.

## 2.2.1. Cell and Battery voltages

Nominal Cell voltage is defined has the voltage produced by a cell when there is no load connected to it and its charge is about 80% of its capacity. Cell voltage depends on its charge, but this behaviour depends on the technology used. Also, this may drop considerably under heavy discharge, due to its internal resistance, according to (2.1):

<!-- formula-not-decoded -->

where 𝐸 is the cell nominal voltage, 𝐼 is the drained current and 𝑅𝑖 is the cell's internal resistance, which depends on the working temperature and cell charge.

Battery voltage is defined as the total voltage of a set of batteries connected in series.

## 2.2.2. Charge or Capacity

The electric charge that a battery can supply is one of the most crucial parameters. The SI unit for this is the Coulomb, the charge when one Amp flows for one second. However, this unit is inconveniently small. Instead the Amp-hour is used: 1A flowing for one hour. The capacity of a battery might be, e.g., 10Amp-hours. This means it can provide 1A for 10 hours, or 2A for 5 hours or, in theory, 10A for 1 hour. However, in practice, it does not work out like this for most batteries.

It is usually the case that while a battery may be able to provide 1A for 10 hours, but if 10 Amps are drawn from it, it will last less than one hour. The capacity of the large batteries used in electric vehicles (traction batteries) is usually quoted for a 5 hour discharge. However, if the current is drawn of more slowly, e.g., in 20 hours, the capacity rises to about 11Ah. This change in capacity occurs because of unwanted side reactions inside the cell. The effect is most noticeable in the lead acid battery, but it occurs in all types. It is very important to be able to accurately predict the effects of this phenomenon, when considering battery modelling.

To express charging and discharging rates, the most widely used terminology in the battery world is the "C rating", which consists in assigning the capacity of the battery, in Ah, to a constant C. If, e.g., the manufacturer of a 3.2V, 10Ah battery claims the maximum discharge rate is 15C peak, it means the battery allows peak discharges at 15x10A=150A. The same applies to the charging rates, where, e.g., a 0.3C charging rate means charging at a current of 0.3x10A=3A.

The total energy stored in the battery is expressed in kWh and is equal to the product of battery voltage by its capacity, in Ah.

## 2.2.3. State-Of-Charge

The State-Of-Charge (SOC) is the percentage of charge still left on the battery. It can be estimated dividing the depleted charge (in Ah) with the battery capacity, though this depends largely on the discharge rate, since, as previously mentioned, the battery capacity is lower if the discharge rate is very high.

There are several mechanisms to improve this estimation, which, depending on the battery technology, can provide very accurate estimations. The simplest way is through the battery voltage, though in some technologies this is not possible since the voltage remains the same between 80% and 20% of the battery charge.

The most sophisticated methods analyse the discharge rates and the voltage drop when discharging to estimate the depleted capacity more accurately, and considering the aging effects as well, since batteries typically loose capacity over time and charge/discharge cycles.

## 2.2.4. Specific Energy

The Specific energy is the amount of electrical energy stored for every kilogram of battery mass. It has units of Wh.kg -1 . Once the energy capacity of the battery needed in a vehicle is known (Wh) it can be divided by the specific energy (Wh.kg -1 ) to give a first approximation of the battery mass.

Specific energies quoted can be no more than a guide, because as previously seen, the energy stored in a battery varies considerably with factors such as temperature and discharge rate.

## 2.2.5. Energy Density

Energy density is the amount of electrical energy stored per cubic metre of battery volume. It normally has units of Wh.m -3 . It is also an important parameter as the energy capacity of the battery (Wh) can be divided by the battery's energy density (Wh.m -3 ) to show the volume of battery required. Alternatively if a known volume is available for batteries, the volume (m 3 ) can be multiplied by the batteries energy density (Wh.m -3 ) to give a first approximation of how much electrical energy can be made available.

The battery volume may well have a considerable impact on vehicle design.

## 2.2.6. Specific Power

Specific power is the amount of power obtained per kilogram of battery. It is a highly variable and rather anomalous quantity, since the power given out by the battery depends far more upon the load connected to it than the battery itself.

Although batteries do have a maximum power, it is not sensible to operate them at anywhere near this maximum power for more than a few seconds, as they will not last long and would operate very inefficiently. The normal units are W.kg -1 . Some batteries have a very good specific energy, but have low specific power, which means they store a lot of energy, but can only give it out slowly. In electric vehicle terms, they can drive the vehicle very slowly over a long distance. High specific power normally results in lower specific energy for any particular type of battery. This is because taking the energy out of a battery quickly, i.e. at high power, reduces the energy available. This difference in change of specific power with specific energy for different battery types is very important, and it is helpful to compare them. This is often done using a graph of specific power against specific energy, which is known as a Ragone plot. Logarithmic scales are used, as the power drawn from a battery can vary greatly in different applications. A Ragone plot for a good quality lead acid traction battery, and a similar NiCad battery, is shown in figure 2.2 [25].

figure 2.2 - Ragone plot for Lead Acid and Nickel Cadmium Traction Batteries

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_005.png)

It can be seen that, for both batteries, as the specific power increases the specific energy is reduced. In the power range 1 to 100 W.kg -1 the NiCad battery shows slightly less change. However, above about 100 W.kg -1 the NiCad battery falls much faster than the lead acid. Ragone plots like the one in figure 2.2 are used to compare energy sources of all types. In this case we should conclude that, ignoring other factors such as cost, the NiCad battery performs better if power densities of less than 100 W.kg -1 are required. However, at higher values, up to 250 W.kg -1 or more, then the lead acid begins to become more attractive.

## 2.3. Battery Technologies

There are many different types of batteries used in electric vehicles, all with their advantages and disadvantages. A lot of electric vehicles still use Lead-acid batteries, even though nowadays the most prominent technologies are Nickel and Lithium based. The choice for the used technology depends a lot on the application since some are more suited for performance and others have a lower cost.

## 2.3.1. Lead-Acid Batteries

Lead-Acid batteries are very popular with EVs. It is a very mature and safe technology at a low cost, it is suited for vehicles working in industrial environments. They are used in a wide range of vehicles from forklifts to compact passenger vehicles, were the performance is not important and it is imperative to keep the cost low, not only on the purchase, but also on the maintenance. It is very easy to monitor the state of charge of these batteries since it is proportional to its voltage, and they are very tolerant to over-charge and over-discharge. The problem of this technology is its low durability, long charge time and low output current. Gel Batteries and Valve Regulated Lead-Acid (VRLA) are two variants of lead-acid that better suit electric vehicles, with higher discharge currents and higher capacities, but these come at a much higher cost.

## 2.3.2. Nickel based batteries

Nickel based batteries are mainly divided in Nickel-Cadmium (NiCd) and Nickel-Metal-Hydrate (NiMH). Nickel cadmium batteries have been widely used in many appliances, including use in electric vehicles.

The NiCd battery has advantages of high specific power, a long life cycle (up to 2500 cycles), a wide range of operating temperatures (from -40◦C to+80◦C), low self-discharge and good long-term storage. This is because the battery is a very stable system, with equivalent reactions to the selfdischarge of the lead acid battery only taking place very slowly. The NiCd batteries can be purchased in a wide range of sizes and shapes, though they are not easy to obtain in the larger sizes required for electric vehicles, being their main market portable tools and electronic equipment. They are also very robust both mechanically and electrically and can be recharged within an hour and up to 60% capacity in 20 minutes. On the negative side, the operating voltage of each cell is only about 1.2V, so 10 cells are needed in to form a 12V battery, compared to 6 cells for lead acid. This partly explains the higher cost of this type of battery. A further problem is that the cost of cadmium is several times higher than the cost of lead, and that this is not likely to change. Cadmium is also environmentally harmful and carcinogenic.

The nickel metal hydride (NiMH) battery was introduced commercially in the last decade of the 20th century. It has a similar performance to the NiCd battery, being the main difference that in the NiMH battery the negative electrode uses hydrogen, absorbed in a metal hydride, which makes it free from cadmium, a considerable advantage. An interesting feature of this battery type is that the negative electrode behaves exactly like a fuel cell. The reaction at the positive electrode is the same as for the nickel cadmium cell; the nickel oxyhydroxide becomes nickel hydroxide during discharge. At the negative electrode hydrogen is released from the metal to which it was temporarily attached, and reacts, producing water and electrons. The metals that are used to hold the hydrogen are alloys, whose formulation is usually proprietary. The principle of their operation is exactly the same as in the metal hydride hydrogen stores used in conjunction with fuel cells. The basic principle is a reversible reaction in which hydrogen is bonded to the metal, and then released as free hydrogen when required. For this to work the cell must be sealed, as an important driver in the absorption/desorption process is the pressure of the hydrogen gas, which is maintained at a fairly constant value. A further important point about the sealing is that the hydrogen-absorbing alloys will be damaged if air is allowed into the cell. This is because they will react with the air, and other molecules will occupy the sites used to store the hydrogen.

The best example of a vehicle using this type of batteries is the Toyota Prius[3], which is a hybrid vehicle combining a petrol engine with an electric motor, which is used to power the car in urban environments (figure 2.3).

figure 2.3 - 2 nd Gen Toyota Prius NiHM battery

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_006.png)

This air-cooled battery has 38 modules of NiHM cells combined in series with an output voltage of 273.6V and a capacity of 6.5Ah, weighting just 53.3kg. The cells are provided by Panasonic, the world's largest supplier of Nickel-based battery cells, and are never charged to more than 60% of their capacity, to extend the battery lifespan. The cost of its replacement is around USD 5000$00.

## 2.3.3. Lithium based batteries

Since the late 1980s rechargeable lithium cells have come onto the market. They offer greatly increased energy density in comparison with other rechargeable batteries, though at increased cost. It is a well-established feature of nowadays laptop computers and mobile phones that lithium rechargeable batteries are specified, rather than the lower cost NiCad or NiHM cells. Today there are several different types of lithium batteries available on the market and the number of electric vehicles using these is constantly growing as the cost of the technology decreases.

The most popular technologies within electric vehicles are Lithium-ion (Li-Ion), Lithium-ion Polymer (Li-Po) and Lithium-Iron-Phosphate (LiFePO4).

Lithium-ion (Li-ion) is a family of batteries using lithium ions (Li + ) to carry the electric charges between the battery poles. It is the most popular technology within lithium batteries as it was the first commercially available at a reasonable cost. It is used in most portable devices such as laptops and mobile phones, since it delivers greater autonomy and more stable voltage output and it is lighter than most technologies. Its cost is higher when compared with conventional Nickel based batteries, but its gains in performance and autonomy made this technology very popular, which helps reducing its cost. The most used chemistry for the cathode is Lithium Cobalt Oxide (LiCoO2) due to its lifespan and lower cost, but there are other chemistries such as Lithium Manganese Oxide (LiMn2O4) and Lithium Nickel Cobalt Manganese (Li(NiCoMn)O4) which are better for specific applications.

These are available on the market in several forms, from small cylindrical (figure 2.4) typically used in laptops, to large prismatic cells typically employed in automotive batteries. These can be made according to the customer request to deliver either more power or store more energy.

figure 2.4 - Tenergy 18650 Li-ion cell

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_007.png)

There are a few issues with lithium, since this is an instable compound when in contact with air or water, or when their voltage or temperature exceed their limits and therefore, constant monitoring of these values is required if the battery is to be considered safe. Also, lithium cells are not tolerant to deep discharges and become permanently damaged if its voltage drops to near zero values, with the cells showing loss of capacity, or inability to hold any charge; therefore, given the cost of the cells, a system should be used to assure over discharge never occurs. This is where Battery Management Systems became popular, in order to prevent over charge or over discharge of any cell.

In recent years, several electric vehicles emerged using Li-Ion cells on their energy storage systems, like the Tesla Roadster [4], Nissan Leaf and the Chevrolet Volt. The most revolutionary was the Tesla Roadster which has a liquid cooled, 375V, 20KWh battery that uses 6800 cylindrical shaped Li-Ion cells, measuring 18 x 65mm (d x l) and weighting just over 50g each, making it very similar to the typical AA battery. The cells are specially made for Tesla and feature several protection systems that are not typically found in commercially available cells, such as a positive temperature coefficient (PTC) current limiting device which protects the battery, the Current Interrupt Device (CID) which releases pressure in the cell if it overheats, and a steel case structure that provides structural rigidity and strength. The complete assemble pack weights 450Kg, and it represents an engineering breakthrough since when it was launched it was one of the largest Li-ion available on a commercial vehicle, showing the world that it was possible to have a green sports car, with a high performance and a driving range of nearly 400km.

The Nissan Leaf aims to be an utilitarian and accessible car, with four doors and a large boot, that can be used every-day, with a range up to 250km. It has a 24KWh Laminated Li-Ion battery placed on the undercarriage, just below the living compartment, making it possible to use just air to cool the battery. The cells are very thin prismatic shaped and assembled in groups of 4 in parallel, with the complete battery being composed by 48 of these groups connected in series. Nissan claims this is the first Lithium powered to break the 400$/KWh barrier (the Tesla is over 700$/KWh) but some automakers don't believe this value, while others justify this with the simplicity of the battery, claiming that the air cooling isn't enough if the battery is to last a minimum of 8 years. Still, this is currently the most affordable Lithium powered electric vehicle on the market and it is selling fairly well, according to the manufacturer.

Lithium Polymer (Li-Po, or Li-Pol) is a very recent technology, but this type of batteries is quickly gaining popularity amongst portable devices, electric vehicles, and especially in the Radio Controlled Hobbyist world where the high power density delivered by these batteries is much appreciated (figure 2.5). They deliver more power than conventional Li-ion batteries, store more energy and weight less than these, making them ideal for small, light and powerful radio controlled vehicles.

figure 2.5 - Kokam Cell for RC models

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_008.png)

These batteries are also well known for its dangerous characteristics, since Li-Po cells explode or burst into flames if they over-charge or over-heat; some will also explode if physically damaged, since the lithium is very unstable when in contact with air. Still, this technology is gaining popularity very fast in the portable device market and because of this it is getting safer and cheaper, though several cases of exploding laptops and mobile phones having been registered (figure 2.6).

figure 2.6 - Example of a laptop battery fire

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_009.png)

Because of this, battery manufacturers have invested a lot in new materials and manufacturing processes and they have been successful in making this technology safer, being SKinovation [5] one of the most successful companies; Advanced Battery Management Systems also have a very important role in keeping Energy Storage Systems safe and with this type of batteries it is very important to monitor the voltage and temperature of as much cells as possible.

With these breakthroughs it becomes possible to use this technology in electric vehicles, making way for longer driving ranges and more powerful and lighter drivetrains, with the cost dropping every day.

Lithium Iron-Phosphate (LiFePO4) has also appeared in recent decade as an alternative type if Li-Ion batteries using an Iron Phosphate Cathode. It is the only type of battery chemistry that is considered intrinsically safe, i.e., it can resist extreme over-charges, high operating temperatures and be physically damaged without exploding or incinerate.

These batteries have a high abundance of iron, and use a carbon based cathode, making them much cheaper than Lithium-Cobalt Oxide batteries while having a higher lifespan than most Lithium based cells. Since they are virtually incombustible, manufacturers can create cells with very large capacities, reaching beyond 100Ah in a 3.2V cell. This makes this technology very well suited for electric vehicles, since they deliver a lot of power and have a lifespan that is 5x to 10x higher than normal LiCoO2 batteries, reason why they are currently being used in most electric motorbikes available on the market, equipped with lithium batteries. The low cost also contributes for its popularity amongst these vehicles, since the batteries are typically small, and therefore a small number of cells are required, which means the required BMS only needs to monitor a small set of batteries.

For this application it was decided to use Lithium-Iron-Phosphate technology, due to its intrinsically safe characteristics, good power and energy densities and low cost. The cells are from China Headway, model 38120S (figure 2.7).

figure 2.7 - China Headway 38120S cell

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_010.png)

The main characteristics of these cells are on table 2.2.

table 2.2 - Cell characteristics

| Parameter | Value |
| - | - |
| Nominal Voltage [V] | 3,2V |
| Maximum Voltage [V] | 3,65V |
| Minimum Voltage [V] | 2,0V |
| Normal Capacity [mAh] | 10000mAh |
| Maximum Continuous Discharge Rate [C] | 10C |
| Maximum Charge Rate [C] | 3C |
| Working Temperature Range (Charging) [ºC] | 0~45ºC |
| Working Temperature Range (Discharging) [ºC] | -20~60ºC |
| Lifetime [Cycles] | 3000 |
| Weight [Kg] | 0.307Kg |
| Specific Power [W/Kg] | 850 |
| Specific Energy [Wh/Kg] | 105 |
| Shape | Cylindrical |
| Dimensions (diameter x length) [mm] | 38x120 (38x134.5 with fittings) |
| Connection type | M6 screws on both cylinder tops |
| Cost p/ cell (exc. tax+shipment, 11/2010 ) [$] | USD 15$00 |

Due to the cost of these technologies and their lack of tolerance for voltage and temperature values outside the range, a Battery Management System (BMS) becomes a crucial part of any Energy Storage System using these technologies, not only to keep the battery operating within the desired ranges, but also to assure the safety of its users.

## 2.4. Cell Balancing

One of the main functions of a Battery Management System is to assure the cells are balanced, i.e., that the voltage of every cell is approximately at the same level. This is extremely important for the health of the battery since if one cell drops below its voltage limits, not only it will be permanently damaged, but it can compromise the performance and behaviour of adjacent cells, which might become damaged as well.

Cell imbalance is derived of many factors. The most important one is the internal resistance, which is always different from cell to cell; the temperature also has a considerable effect on this since cells in the interior of a battery pack usually have worse cooling conditions, which influences the cell internal resistance.

figure 2.8 - Example of an extremely imbalanced battery

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_011.png)

The imbalance may occur in both directions, i.e., there may be cells with either very low voltages, as well as cells with voltages above the safe operation limits (figure 2.8), which generally occurs in unsupervised charges, and might lead to potentially dangerous situations if lithium based batteries are used.

The balancing processes mainly actuate on the charging, allowing the cells to be fully charged, while assuring they stop charging as soon as they reach the desired voltage. The ideal solution would be to completely disconnect charged cells on the pack and replace them with a direct connection, but this implies the application of several bypass circuits, which have to be big enough to handle the currents at stake. Therefore, other solutions should be used.

To address this issue, a Battery Management System is usually installed in order to monitor and balances the cells. There are two types of balancing which will be discussed in this section: Dissipative and Non-dissipative.

## 2.4.1. Dissipative balancing

The most used balancing type is the Dissipative balancing, also known as Passive Balancing since it uses simple passive components to adjust the voltage levels. The most common is to use a resistor that dissipates electric energy into heat in order to lower the voltage of the most charged cells.

The major disadvantage of this solution is that with high currents, the generated heat may affect surround cells, or even the battery management system itself. Also, it is not very environmentally correct to waste energy, but it is less harmful to waste energy in heat than in the production and recycling of more batteries.

## 2.4.2. Non-dissipative balancing

Non dissipative balancing (also known as Active Balancing) consists on transferring energy from the most charged cells to the ones with lower voltage. In theory, this method is better since it doesn't waste energy, therefore it is more efficient. However, in practice, the additional components required to do this make the system more complex, less reliable and, in most cases, heavier and with a bigger volume.

Active balancing is usually made with one of three techniques (figure 2.9):

- Cell-to-Battery: energy is transferred from the most charged cell to the entire battery;
- Battery-to-Cell: energy is transferred from the entire battery to the cell with the less charge;
- Cell-to-Cell: energy is transferred between adjacent cells;

figure 2.9 - Non-dissipative cell balancing techniques: (a) Cell-to-Battery; (b) Battery-to-Cell; (c) Cell-to-Cell

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_012.png)

The first one, Cell-to-Battery, uses isolated DC/DC converters from Low Voltage to High Voltage to balance the cells. There are some losses in the converters, but it is the most efficient of the three methodologies seen here. The supplied currents depend on the size of the converter, but these are usually very small, leading to very small balancing currents. The system becomes faster as more cells become charged.

The second one, Battery-to-Cell, uses DC/DC converters from High Voltage to Low Voltage, which are typically less efficient but easily allow higher currents, and use switched outputs to every cell. This takes up a lot of room in a battery pack since it is required to have a lot of wires from the converter to the cells, plus the converter itself, even more if the desired balancing currents are high since bigger cables will be required. Still, this method allows a faster balancing, even with less efficiency.

The third one, Cell-to-Cell, uses small converters to transfer energy between adjacent cells, from the one with the higher voltage to the one with the lower voltage. This is a low efficient solution, with very small balancing currents, making this very slow. The advantage is that the used components are small, and the architecture itself allows this to be integrated on the BMS, without requiring complex wiring to be installed. This type of balancing is presented in several "On-chip" Battery Management integrated circuits, given the low currents, and it is also found in centralized management systems (see section 2.5)

Non-dissipative balancing does present benefits in vehicles that are used for short distances and left stopped for long periods of time, since the energy transferring process can balance the cells and improve the driving range of the vehicle, since most Battery Management Systems will deactivate the vehicle when one cell reaches the low voltage limit, leaving energy on the remaining cells that could be used for travelling.

Given the complexity, cost and weight of this systems, it was decided not to implement this in the development of this work, since this is a racing prototype and not a commercial vehicle, therefore such a system would not be able to balance the cells fast enough before the battery was completely drained, not justifying the investment.

Several EVs available on the market abuse the term "Active Balancing", since they are dissipative balancing systems that use passive components to dissipate energy during most of the charging, to keep the cells in balance throughout the process, thus calling this active balance. In these cases, the term "Active Balancing" is abused for marketing purposes, since the balancing system uses passive elements to dissipate energy, instead of transferring it.

## 2.5. BMS architectures

There are several possible architectures for a Battery Management System. The main ones are the Centralized, the Distributed and the Modular, each of them with its set of advantages and disadvantages, which will be explained in this section.

## 2.5.1. Centralized BMS

The Centralized system (figure 2.10) is one of the most used architectures, consisting in having only one control module that monitors every cell or cell group in the battery. There is at least one wire from every cell to the BMS in order to connect both poles of every cell.

figure 2.10 - Centralized BMS

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_013.png)

This is a simple and cheap solution, very popular with small batteries. Usually there's only one PCB with all the wiring for the cells and for the temperature sensors, so if the battery has a large of cells, the wiring will be very complex. In some battery management systems there isn't even a microcontroller or any other digital monitoring device, only analogue electronics which manage the charge making them very cheap. But the lack of digital control makes it hard to configure and integrate with any information system or vehicle electronics, which might lead to potentially dangerous situations due to the lack of monitoring.

This type of BMS is widely used in electric bikes since typically these have small batteries, where the wiring is not a big problem, and there are no complex vehicle electronics systems.

## 2.5.2. Distributed BMS

Distributed systems (figure 2.11) are composed by several nodes, typically divided in a master and slave modules, communicating with a specific protocol.

The slave modules are dedicated circuits connected to a cell or cell group, from which its power is supplied. A set of sensors monitors the cell conditions to ensure all the parameters are within the manufacturer specification, and sends this information to the master module. In addition, the modules usually include a power dissipation element, which is responsible for eliminating the excessive energy flow when the cell is charged.

figure 2.11 - Distributed BMS

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_014.png)

The master module is responsible for managing the operations on the battery like the activation or deactivation of its poles, SOC estimation and integration with vehicle information systems. Several communications protocols can be used for the master-slaves link, being the most popular SPI, I2C, RS-232, RS-485, LIN and CAN Bus, with the latest being the chosen for this work due to its reliability, robustness and simplicity. For more information see Appendix B.

Some systems use serializable communications (figure 2.12) so that there is only one wire running through the battery, but there is a constant reliability problem, with the communication being compromised if one of the modules fails, or a wire becomes loose or broken.

figure 2.12 - Distributed BMS with serial communications

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_015.png)

The advantage of distributed battery management systems is that the wiring is very simple and the resulting system is very reliable, and simple to install, making this more suited for large batteries. On the downside, its cost is higher than centralized systems since there are more modules installed.

## 2.5.3. Modular BMS

The last analysed architecture is the Modular BMS (figure 2.13), which is a mixture of the architectures previously seen. It combines a centralized module that monitors a set of cells, which then communicate with each other. Typically there is also a control module connected to this communication bus which controls the peripheral devices such as relays and the cooling system.

figure 2.13 - Modular BMS

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_016.png)

This architecture is slightly cheaper than a distributed system and has a less complex wiring harness compared to a fully centralized system, but the wiring is still fairly complex and if one module fails, a large cell number might be at risk.

These are the main types of architectures generically found in most batteries, tough there are other types of systems which are custom built for very particular solutions. It is up to the developers to choose one of these architectures, or a mix of these, depending on what the application demands.

The architecture chosen for this work is the distributed system, which allows a better control and monitoring of each cell and has a simple wiring harness composed only by the cables for the CAN bus and 5V supply, making it better suited for a first implementation of such system.

## 2.6. Cell configuration

From the MATLAB model of the battery developed in [1], the determined capacity required for this prototype was 50Ah at a voltage of 144V, which corresponded to the selected electric motor nominal voltage. As seen in 2.3 the selected cells have a capacity of 10Ah at 3.2V each, therefore the minimum amount of cells required to obtain the desired capacity is 225 cells.

A lot of time has been spent working with the chassis team members to decide the better place and geometry for the accumulator. The final decision was to keep all the cells inside one container, located behind the driver's seat in a lower central position, keeping the car's centre of gravity very close to the vehicle centre and the ground for improved dynamics.

The next task was to distribute the cells inside the container. Being the cells cylindrically shaped with a diameter of 38mm and 120mm long (plus fittings), it was decided to distribute them in four columns, with the cells placed transversely to the car, spaced 4mm from each other. In order to compensate for the voltage drops in the connections and cables, and for geometrical reasons, it was decided to increase the cell number from 225 to 240. The cells are connected in identical groups of 5 cells to obtain groups of 50Ah, which are then connected in series, making the resulting system a 153.2V battery, with a 48s5p configuration (48 series, 5 parallel).

figure 2.14 - Cell distribution inside the container

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_017.png)

In figure 2.14 is shown the cell distribution, with 225 cells. This geometry was revised in order to have 240 cells, displaced in a slightly shorter length has it will be shown further in this document.

## 2.7. CAN Bus

As previously mentioned, it is very important to assure that the communications are very reliable, guaranteeing the messages are correctly delivered while working in harsh conditions, with vibrations, high temperatures and Electromagnetic Noise, typically seen on road and racing cars.

For this work it was decided to use CAN bus, a communication protocol developed specifically for the automotive industry by Bosch Gmbh [6] in the 80s that quickly became the industry standard communication protocol. The CAN communication protocol is a Carrier Sense Multiple Access/Collision Detection (CSMA/CD) protocol. This means that every node on the network must monitor the bus for a period of no activity before trying to send a message on the bus (Carrier Sense). Also, once this period of no activity occurs, every node on the bus has an equal opportunity to transmit a message (Multiple Access). As for the Collision Detection, if two nodes on the network start transmitting at the same time, the nodes will detect the collision and take the appropriate action. In the CAN protocol, a non-destructive bitwise arbitration method is utilized, which means that messages will remain intact after arbitration, even if collisions are detected. All this arbitration takes place without corruption or delay of the higher priority message (the node transmitting the highest priority message will continue and the others will wait).

Another important characteristic of this protocol is that it is a broadcast or message-based type of protocol, which means that all the nodes receive all the messages (in opposition to an address-based type of protocol), and for specific node addressing to be accomplished, local message filtering must be used. This means that upon receiving a message, each node decides if the message is kept for further processing or immediately discarded. The protocol guarantees that messages are accepted by either all nodes or none of them, implementing for this several mechanisms to ensure data consistency, error handling and error confinement.

This protocol is used in the communication between the slaves and master modules, as well as in the communications between the master module and the vehicle electronic system. More details on the CAN protocol can be found in Appendix B.

## 2.8. Connections and Geometry

The connections between the cells have a very important role on the ESS, since it influences the behaviour of the vehicle in many different ways. If the connections are under dimensioned, it will lead to high thermal losses; if they are over dimensioned the ESS will be heavier, which means more weight to be dragged and more energy required. It is therefore extremely important to choose the right materials with the right size.

The first step is to define the shape and how the connections will be made; we wanted a modular, easy to manufacture and easy to assemble system, so it was decided to assemble the cells in individual groups of 5 cells. Keeping in mind the weight distribution and space requirements for all the devices required for the battery, each of the four cell columns was divided in twelve groups of 5 cells, with eleven of these assembled in a trapezoidal shape, and the remaining one linearly distributed - see figure 2.15 and figure 2.16. Between every cell there is a 4mm gap to allow any cell expansion and provide better cooling.

figure 2.15 - Cell group, trapezoidal shape

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_018.png)

figure 2.16 - Cell group, linear shape

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_019.png)

Even though the most used material for electric conductors is copper, it was decided to use Aluminium, AL2024, which has an electric resistivity of almost 3 times higher than copper (Cu Resistivity: 17.8nΩ.m; AL2024 resistivity: 4.8nΩ.m), but with less than 1/3 of the weight (Cu density: 8.94g.cm -3 ; AL2024 density: 2.78g.cm -3 ). This means more material has to be used when applying aluminium instead of copper, but this allows a better heat dissipation and higher mechanical robustness, achieved with less weight than using copper.

In order to withstand the high discharge currents the cells provide, it was decided to use 3mm thick aluminium plates, with an average cross section of 96mm 2 . See Appendix C for more details.

The cell groups were then assembled in groups of 12 (11 trapezoidal, 1 linear) in a Glass-FiberReinforced-Plastic (GFRP) structure and connected electrically in series using aluminium bars with the same 3mm, 96mm 2 cross-section., with M6x15mm screws holding the cells and the aluminium connectors - see figure 2.17. The resistivity of this connecting bar is determined on table 2.3, with the label "Type 1".

figure 2.17 - Cell column assembly

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_020.png)

The Energy Storage System is composed by four of these columns connected in series, using the same aluminium previously referred (figure 2.18), whose resistance is determined in table 2.3 with the labels "Type 2" and "Type 3", with the "Type 2" being used in the connection between the 1 st and 2 nd , 3 rd and 4 th columns, and the "Type 3" between the 2 nd and the 3 rd .

figure 2.18 - Column assemble inside container

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_021.png)

The electrical resistance of the connections were determined using the material resistivity, cross section and distance between the connecting points, given by the following equation:

<!-- formula-not-decoded -->

where 𝜌 is the material electrical resistivity, L is the distance and S is the cross section.

table 2.3 - Electrical resistance of the cell connections

| Connection | Distance between connecting points (mm) | Thickness (mm) | With (mm) | Cross Section (mm 2 ) | Resistance (Ohm) |
| - | - | - | - | - | - |
| Type 1 | 40 | 3 | 32 | 96 | 2,00E-05 |
| Type 2 | 60 | 3 | 32 | 96 | 3,00E-05 |
| Type 3 | 366 | 3 | 32 | 96 | 1,83E-04 |

To determine the voltage drop in the connections and dissipated energy, we first needed to estimate the currents that will cross them. The nominal discharge current is 230A, corresponding to the motors nominal current (Appendix D), and the accumulator maximum discharge is 10C, corresponding to 500A. The voltage drop (Vd) and dissipated power (Pd) are determined by the following equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The results for the 230A and 500A discharge rates can be seen on table 2.4 and table 2.5 respectively.

table 2.4 - Dissipated power at 230A

| Connection | Resistance (Ohm) | Voltage Drop [V] | Dissipated Power [W] |
| - | - | - | - |
| Type 1 | 2,00E-05 | 0,00460 | 1,058 |
| Type 2 | 3,00E-05 | 0,00690 | 1,587 |
| Type 3 | 1,83E-04 | 0,04209 | 9,681 |

table 2.5 - Dissipated power at 500A

| Connection | Resistance (Ohm) | Voltage Drop [V] | Dissipated Power [W] |
| - | - | - | - |
| Type 1 | 2,00E-05 | 0,01000 | 5,000 |
| Type 2 | 3,00E-05 | 0,01500 | 7,500 |
| Type 3 | 1,83E-04 | 0,09150 | 45,750 |

The values for the 500A discharge showed that there would be high losses due to thermal dissipation, but this discharge rate only occurs in very small periods of time, therefore it was not a significant problem.

## 2.9. Pre-charge Circuit

In order to safely close the relays on the Energy Storage System to allow a safe start of the vehicle without damaging the motor controller, the FSE rules state that a Pre-charge Circuit must be installed on the battery, in order to charge the capacitors on the Motor Controllers.

The pre-charge circuit consists on a resistor connected in series with a normally opened relay, connected in parallel with the positive AIR (see figure 2.19). The relay is actuated by the BMS when the HV system is connected, activating the negative AIR and the pre-charge relay for about 5 seconds, until the HV system voltage is over 90% of the accumulator current voltage (157.8V when fully charged). Then, the Positive AIR is connected and the pre-charge relay is disconnected. This happens every time the tractive system is activated.

figure 2.19 - Pre-Charge circuit schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_022.png)

The currents, voltage and power (I, V and P) on the circuit were calculated considering the capacity of the self-developed controller of 13.12 mF, using the following equations:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where 𝑉0 is the voltage at t=0, R is the resistor value and C the controller capacitance.

After several iterations, the chosen resistor value was 150Ω, rated at 100W. The results for the Voltage, Current and Power over time are on table 2.6.

table 2.6 - Pre-charge over time

| Time [s] | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| - | - | - | - | - | - | - | - |
| I [A] | 1,17 | 0,70 | 0,42 | 0,25 | 0,15 | 0,09 | 0,06 |
| Vc [V] | 0,00 | 69,84 | 111,85 | 137,13 | 152,33 | 161,48 | 166,9878 |
| P [W] | 204,87 | 74,15 | 26,84 | 9,71 | 3,52 | 1,27 | 0,46 |

The used resistor has a power rating of 100W but it is able to withstand almost 3 times the rated power for about 20s without any deterioration, so it can handle the initial 200W peak Power. The relay is from Tyco electronics, T9A series, with a 12V coil, able to withstand up to 30A.

## 2.10. Discharge Circuit

When the vehicle is turned off, the relays on the ESS are opened, and the motor controller stops sending power to the wheels. This means that the capacitors on the motor controller stay charged, since there is nowhere for the current to flow. Therefore, a discharge circuit should exist in order to discharges the capacitors, so that the vehicle can be safely operated without danger to its operators.

The FSE rules states that the circuit should be connected in such way that whenever all circuits (LV and HV) are off the circuit is permanently activated, discharging the capacitors. This is achieved by a circuit with a resistor connected to the HV terminals, with a normally closed relay in series (figure 2.20). The relay is actuated by the BMS when the HV system is connected, interrupting the discharge circuit, and lowering the voltage below 40V in less than 5s, as stated in the rules.

figure 2.20 - Discharge circuit schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_023.png)

To estimate the worst case scenario, we considered the maximum accumulator voltage, 175.3V, and used the same equations for current, voltage and power as in the pre-charge section. The resistor and relay are equal to those used in the pre-charge circuit, since the discharge operation is the opposite of the pre-charge, and therefore it should behave very similarly.

The results are on table 2.7.

table 2.7 - Discharge over time

| Time [s] | 0 | 1 | 2 | 3 | 4 | 5 |
| - | - | - | - | - | - | - |
| I [A] | 175,30 | 105,46 | 63,45 | 38,17 | 22,97 | 13,82 |
| Vc [V] | 1,17 | 0,70 | 0,42 | 0,25 | 0,15 | 0,09 |
| P [W] | 204,87 | 74,15 | 26,84 | 9,71 | 3,52 | 1,27 |

The maximum discharge is near 200W which the resistor and the relay are able to withstand without sustaining any damage.

## 2.11. Fusing

Fusing is also an important protection system in any kind of battery, providing protection not only to the battery users, but also to the battery itself and the surrounding components.

For this application, the system consisted in one high power fuse installed between the positive pole of the cell association and the positive Accumulator Insulation Relay, assuring that there was no voltage present on the accumulator terminals if the fuse was broken, providing protection to the battery users.

Since this is a racing vehicle, the weight plays a very important part on the vehicle performance, and therefore, all the components should be as light as possible. For this, it was decided to use a Semiconductor Fuse type, providing high levels of protection and fast actuation.

The selected fuse is a Siemens SITOR 3NE8 731-1(figure 2.21), rated at 315A.

figure 2.21 - Siemens SITOR semiconductor fuse

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_024.png)

This fuse rating was chosen according to the HV cables current ratings (copper, 70mm 2 ) and to withstand the current peaks that flow from the battery to the motors, which can be as high as 750A, for a few milliseconds. More information regarding this fuse can be found in Appendix E.

## 2.12. Current Sensor

The easiest way to estimate the State Of Charge of a Lithium-based battery is called the Coulombian counting [26], and consists on integrating the current over time (2.8), to determine the charge used, and dividing this with the battery capacity 𝐶𝑡𝑜𝑡𝑎𝑙.

<!-- formula-not-decoded -->

The integration of the current can be done using analogue electronics, but this would be harder to integrate with the digital control on the system, as well as a more noise-biased system. Instead, this is done electronically with a current sensor, on which periodic measurements are made. The result is then determined using a zero Order Hold (ZOH) model which converts a discrete-time signal to a continuous-time signal (2.9).

<!-- formula-not-decoded -->

where () rect is a rectangular function as in figure 2.22, ] [n x is the sample sequence and T is the time between samples.

figure 2.22 - rect() function used in the ZOH model

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_025.png)

An example of a signal reconstruction can be seen on figure 2.23, where the blue signal represents the discrete signal and the black line the reconstructed

fft)

figure 2.23 - ZOH signal reconstruction

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_026.png)

For every measurement (sample), the model considers that there aren't any changes over the next period T , maintaining its value for that period of time (a zero order function).

The current measurement was made with a Closed Loop Hall Effect sensor, the CSNS300 from Honeywell [7] which is able to measure currents up to ±600A. To measure properly, it needs a symmetric power supply of ±12V with a current output of 300mA; therefore, it was decided to use a DC/DC converter just for this sensor, since the current output required was higher than the rest of the components in the system, thus the need to apply a bigger converter. The component used for this was the TEN 8-2422WI from TRACO POWER [8], an 8W DC/DC converter which supplies a fixed output of ±12V with a maximum current of ±333mA, from a 9-36VDC power supply (figure 2.24).

Since the sensor output is a current proportional to the measuring value, a 10Ω resistor had to be placed between the output and the common, to transform the current signal to a voltage that can be measured by the microcontroller in the Master Module (see section 4.2).

figure 2.24 - Current sensor schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_027.png)

The sensor was placed inside the battery container, with the HV negative pole cable crossing it before the AIR. The DC/DC converter and the output resistor were placed on a perforated PCB apart from the BMS Master Module, due to the space constrictions inside the container.

## 2.13. Accumulator Insulation Relays

The function of the AIRs is to assure there is no voltage present on the battery terminals when the system is disconnected. It consists in two relays, one in each pole. This is a safety feature that is mandatory by the FSE rules, which state these have to be normally opened and should only be closed when a set of safety requirements are met.

The relays are from Tyco Electronics, the EV200 series [9], a standard in the electric vehicle business. They can stand currents up to 500A continuous and interrupt the circuit with 2000A crossing it, at 320VDC. The coils have a 12V power supply which has dedicated connections on the accumulator, meaning the power can be controlled from another point in the vehicle.

There are a total of 5 shutdown point in the vehicle that allow any user to cut the power supply of these relays, plus an insulation monitoring device which can also open these if an insulation between the HV and LV system occurs, as stated by the FSE rules.

## 2.14. Tractive-System-Active-Light

The Tractive-System-Active-Light is a device that warns surrounding people that the vehicles Tractive system is active and the vehicle may move at any time. Electric vehicles typically don't make any noise when stationary; therefore the use of such device is mandatory by the FSE rules, which also states it has to be placed on a clearly visible place, on the highest point of the car.

This device was supplied from SIEMENS, SIRIUS series, model 8WD42 20-5BB. It is a 24V red blinking element which can be seen from any point around the car. It is activated by the BMS if the voltage outside the accumulator container is above 40VDC or if the AIRs are activated. The circuit was developed by a colleague from the Projecto FST electronics team, Miguel Silva, and incorporates a galvanically isolated DC/DC converter that pumps the voltage supply to 24V, a voltage comparator to identify when the HV voltage is above 40V RMS, and a 9V battery that supplies the circuit if the low voltage circuit is off.

This increases the safety of the vehicle, since it will warn operators is High Voltage is present outside the container, even with all the control systems turned off.

## 2.15. Ready-To-Drive-Sound

The Ready-to-Drive-Sound is a mandatory device whose function is to warn surrounding people that the vehicle has been started and is ready to drive. Electric vehicles typically don't make any significant noise when they are activated, other than relays being closed, and therefore the use of such device is mandatory by the FSE rules.

The sound is produced by an acoustic signal transformer from Siemens, model 3SB19 02-2BN, producing a sound pressure of 80dB at a distance of 10cm. It produces a loud intermittent signal for 6 seconds (2s interval) when the tractive system is activated, through the pre-charge phase until the AIR are both activated. The control of the RTDS is made in the BMS Master module.

figure 2.25 - RTDS Wiring

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_028.png)

The acoustic transformer needs a 24V power supply; therefore a voltage booster is required since the vehicle LV system works at 12V. The voltage booster is integrated in the BMS Master module (figure 2.25), and together with the acoustic device have a power consumption bellow 100mA.

The speaker itself was placed outside the container, on a high position in the vehicle, where the sound is better reproduced.

## 2.16. Cooling

Cooling is also an important part of big electric vehicle batteries, especially if they are subjected to very high rates of discharge, since high currents mean high dissipation losses on the cells internal resistances. To study this effect on the cells, thermal and CFD analysis were conducted, to see what type of cooling would be required.

The Thermal Analysis was made in collaboration with two Portuguese companies, "AutoSil" [10] and "Ventura Rodrigues Consultadoria Engenharia" [11], with the first providing the facilities and high discharge test benches, and the second providing the Thermal Imager, the Fluke Ti9 [12]. Several test where conducted with discharge rates rating from 5C to 10C (figure 2.26) for long periods of time, where it registered the evolution of the temperature over time.

figure 2.26 - Thermal analysis of the Headway 38120S cells at 10C discharge

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_029.png)

The maximum measured temperature was of 85ºC, with an ambient temperature of 25ºC, but this was in an extreme discharge at a constant 10C discharge rate for over 5 minutes.

CFD analyses where then conducted by the Projecto FST team member, Henrique Cunha, using the FloWorks [13] software suite, with several driving profiles and different cooling types and combinations, to determine which solution would better fit this application. It was decided to use aircooling, since it is a lighter and simpler solution than liquid cooling, on which the team has no experience, thus avoiding potentially dangerous situations with conductive liquids in contact with batteries. The results of the thermal analysis were also used to validate the CFD studies, where it was concluded the model was good approximation.

From these, it was concluded that a four 80mm fan solution would suffice, as long as the airflow capacity of these is above 60CFM (Cubic Feet per Minute), with two of these placed on a lower position on the sides of the battery forcing air in, and the other two placed on a high position in the back, extracting air from the battery (figure 2.27).

figure 2.27 - FloWorks CFD simulations

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_030.png)

The chosen fans were from Delta Electronics, model QFR0812DE-F00, which measured 80x80x38mm, and had a maximum air flow of 105CFM, when supplied at 12V. These may seem over-dimensioned, but the speed of these is controlled by the Battery Management System, thus working at a lower regime in normal operation while allowing the system to pump up the cooling if the battery becomes hotter.

## 2.17. ESS architecture

On figure 2.28 there is an overview of the ESS architecture, with the all the components that are part of the Energy Storage System.

figure 2.28 - ESS architecture

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_031.png)

The only components placed outside the container were the discharge circuit (resistor and relay), the TSAL and the RTDS, both placed in high positions in the car. There are connectors for these devices on the accumulator container, to facilitate maintenance and assembling.

## 3. Slave Module

These modules are responsible for monitoring the cells groups in the battery, measuring the voltage, temperature and balancing current and transmitting these to the Master module. The hardware for these modules should fulfil a set of requirements with respect to its dimensions, electric isolation, and thermal conductivity.

First, the PCB had to be very thin in order to fit the gaps between the cells; Power should be supplied by the monitored cells; the module must be able to operate in the entire voltage range of a cell, meaning it must work between 2V and 3,65V; a communication system had to be implemented that would guarantee a reliable message exchange and allowed galvanic insulation between the module supply (HV) and the control system (LV); the module must also be able to measure the cell voltage and temperature and, being this a passive system, it should include a power dissipating module to discharge the cell when it is required to. The first step was to define the communication protocol, then the components and finally design the circuit. This process required some iteration since every decision for a component affects the whole system.

Another goal for the slave modules was the possibility to be used with different battery technologies, so that it can be implemented in other vehicles using different battery technologies with a simple reconfiguration of its parameters, a goal that was successfully achieved.

## 3.1. Architecture

The slave modules have a simple design consisting on a microcontroller, with voltage and temperature measurements, a load element that provides the balancing for each cell, a power supply element that supplies a voltage reference and a transceiver to handle the communications (figure 3.1).

figure 3.1 - Slave Module Architecture

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_032.png)

The first stage is the DC/DC converter which provides the supply to the microcontroller, sensors and communications transceiver. The microcontroller reads the voltage directly from the cell supply and the temperature through a sensor installed on the PCB. This also controls the balancing load, being able to activate/deactivate this, and measuring the current flow through this.

The final stage is the communications, which are made with a dedicated transceiver which has already built in galvanic isolation.

## 3.2. DC/DC Converter

In order to have a power supply for the transceiver, it was decided to use a step-up voltage regulator, supplying a fixed voltage of 5V from the cell voltage, which ranges from 2.0V to 3.65V.

For this it was chosen the LM2621 [14] from National Semiconductor, which is able to supply a steady output of 5V from an input between 1.6V and 5.5V, and has a low cost and small package (figure 3.2),.

figure 3.2 - DC/DC converter schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_033.png)

The passive components were selected according to the manufacturer instructions on the component datasheet with only some small changes, given that some of the components are not available on the market at competitive prices. This resulted in very small changes in the output - 4.9V instead of 5V. Since the microcontroller is also be supplied by this converter and this voltage is used as a reference for the A/D converter (see section 3.3), this value was carefully analysed on every module.

## 3.3. PIC microcontroller

There are many microcontrollers available on the market, from different manufacturers, which are suited for this type of application. It was decided to use a microcontroller from Microchip because the required tools to program products of this maker are available on the labs on which this work was developed, and it is the same used in on the vehicle electronic system on all prototypes built by the Projecto FST team and therefore there is a good knowledge base about these microcontrollers.

The main requirements for the microcontroller are CAN compatibility, at least 3 analogue inputs, one PWM output, a low cost, a small package and works with a supply voltage from 1.8V to 5.5V. The PIC18F2480 [15] meets this requirements, has a low cost and a small package (QFN 28pin), making it suited for this system.

figure 3.3 - PIC18F2480 Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_034.png)

This 8-bit micro controller is the central component in the Slave Modules, to which every device is connected. It has a 16MHz SMD crystal connected to assure synchronism and a 1Mbit.s -1 CAN Bus speed, filtering capacitors and a Programming connector, allowing the modules to be connected to any programmer or debugger from Microchip, such as the PicKit3 or the ICD2, using the MPLAB software.

## 3.4. Balancing Load

The process of balancing the battery requires that some cells stop charging before other. Since they are connected in series with very large connections, it is not possible to disconnect a cell from the others in the pack when they are charged.

The solution used in this work was to use a balancing load which is connected in parallel with the cell which diverts the current flow from the cell to the load. This way it is possible to maintain the cell voltage when the charging current is low or simply slow down the charge when a cell group is charging faster than the remaining.

The first step was to define the balancing current, i.e., the current to be diverted from the cell to a balancing load. The higher this current is, the faster is the balancing, allowing faster charges with higher charging rates. The problem is that this method uses loads to dissipate the energy, so the higher the current, higher is the generated heat. Since there is not much room for large dissipating areas, the dissipated current could be very high. Along the development of these modules, several versions were built, with different resistor values and different dispositions, in order to determine the solution that best fitted the application. It was determined that the balancing current should be around 2A.

The used load is composed by 20 SMD resistors, size 3210, with a resistance of 33Ω connected in parallel, each rated at 0,5W. The result is a 1,65Ω resistor, diverting up to 2.13A at 3,65V (8W), capable of dissipating a maximum of 10W continuously. These are displaced on the PCB far from the rest of the components, since the heat generated by these could influence the microcontroller or the sensors behaviour.

The load is connected with a MOSFET to the microcontroller (figure 3.4), the BSP030 [17] from NXP, which is able to withstand up to 5A continuous, has a very low cost and comes in a compact SOT-223 footprint.

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_035.png)

33

figure 3.4 - Balancing Circuit Schematics

The MOSFET is controlled by the microcontroller using a Pulse-Width-Modulated signal, which means it is possible to control the balancing current by controlling the duty cycle of the PWM signal. The frequency of this is important to guaranty the load is linearly controlled at several duty cycles, since the objective was to provide a load control that can range from 1% to 100%. The determined frequency was 3,906 kHz, which is high enough for the system to work as it was designed, but it is also low enough not to stress either the components in the circuit, or the cell itself.

Also in the balancing circuit is a 0.1Ω resistor, which is used to measure the balancing current, and will be discussed in the next section (3.5), making the total load resistance Ω = 75 . 1 L R , thus the making the maximum balancing current 2.08A at 3.65V cell charge.

## 3.5. Sensors

There are 3 different measures made is each slave module which measure the cell voltage, cell temperature and balancing current. The measurement consists in a voltage for all three sensors, which is measured and converted by the 10-bit ADC on the microcontroller.

All the sensors are checked periodically with dedicated routines, which will be analysed in section 3.8 of this document.

## 3.5.1. Cell voltage measurement

The voltage is measured directly on the microcontroller, using the 10 bit A/D converter with the 4.9V supply from the DC/DC converter as a voltage reference, making the measurement range from 0V to 4.9V. The voltage is obtained using (3.1).

<!-- formula-not-decoded -->

where ADCR is the result of the ADC measurement (from 0 to 1023), REF V is the ADC voltage reference, which in this application is the 4.9V supply from the DC/DC converter, and 10 2 is the ADC resolution (10bit) resulting in 1024 possible values.

Since the ADC module on this microcontroller has a capacitive device to make the data acquisition and keep the value to be read during the conversion, the acquisition and conversion times have to be properly set, to have a correct measurement. Also, the microcontroller is in an environment with a lot of electromagnetic noise, which may corrupt the measurement, as can the current bursts from the drivers demand; therefore, in order to have a more accurate measure, 30 consecutive samples are taken from the ADC channel, from which the average value is then calculated and used as a measure.

## 3.5.2. Temperature sensor

The temperature sensor used is the TMP20 [16] from Texas Instruments, which has a measuring range of -55ºC to 130ºC on a supply voltage from 2.7V to 5.5V, and comes in a SC-70 5 pin package.

It is placed on the ground plane, near the minus terminal of the battery in order to measure the temperature of the cell more accurately.

The temperature is obtained from the sensor output voltage measurement, using (3.2) to obtain the result in [ºC], as stated in [16].

<!-- formula-not-decoded -->

where 𝑉𝑡𝑒𝑚𝑝 is the output voltage from the sensor (figure 3.5), and the other constant values are as stated in the component datasheet.

figure 3.5 - TMP20 temperature sensor Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_036.png)

Before applying (3.2), the voltage has to be measured. This is done using the same sampling methodology as previously described, since any noise on the microcontroller supply can cause a wrong measure.

## 3.5.3. Balancing Current

The measurement of the balancing load is important to determine the cells SOC, as well as to check if the balancing circuit is working properly. This should be a non-intrusive circuit.

To measure the current in the balancing load, there is a 0,1Ω SMD resistor connected in series with the load, on which the voltage drop is measured. It has a maximum power dissipation of 0,5W. Applying Ohm's law (3.3), when crossed by a current of 2A, the voltage drop on its terminal is 𝑉𝑑𝑟𝑜𝑝 = 0.2𝑉.

<!-- formula-not-decoded -->

Given the 10bit resolution from the ADC in the microcontroller, the minimum voltage the microcontroller is able to read is 5mV, therefore it is possible to read the balancing current with a 50mA resolution, which is enough for this application.

## 3.6. CAN-bus interface

For the communications it was decided to use CAN bus, since it is a very reliable protocol, easy to implement, and it is compatible with the vehicle electronics system.

This communication protocol requires a microcontroller which supports it, and a transceiver to adjust the voltage levels. See Appendix B for more information about the protocol. The chosen transceiver was the ISO1050 [18] from Texas Instruments which supports a 1Mbit/s link and it is optically isolated, fulfilling the requirements.

figure 3.6 - CAN transceiver Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_037.png)

Since this transceiver is optically isolated, it needs two independent supply sources, one on the TTL side (connected to the microcontroller), and the other the CAN side (connected to the CAN network). The problem is the supply voltage, which has to be between 3.3V and 6V on both sides. Given the nominal cell voltage is 3.2V it is not possible to power the transceiver directly from the cell. Therefore a step-up power converter is needed to supply this device, which is one of the main reasons the device described in section 3.2 was installed, to supply a steady voltage source to the TTL side of the transceiver. The CAN network has a 5V supply line provided by the Master module, which is capable of delivering power to all 48 nodes in the network.

The CAN register configurations required on the microcontroller are defined in Appendix B, section B.4.

## 3.7. Printed Circuit Board

One of the main requirements for the system is the space taken by the module. This should be placed as close to the cells as possible, while not disturbing the cell cooling.

Given the cell distribution, the best way to displace the module is using the gaps between the cells, placing the PCB alongside the cells. This lead to a PCB measuring 15x134mm (W x L) which the same length as the cells and wide enough so that it fits the interstitial spaces left by the cells.

figure 3.7 - PCB drawings, top and bottom layers

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_038.png)

The result is a two layered PCB (figure 3.7) with all the control and monitoring components on the top layer and the balancing load, current sensor and CAN transceiver on the bottom layer. There is an heat dissipation zone on the left, the positive pole, where the balancing resistors are installed, which is cleared of components on the top layer. This zone has several Vias from one side to the other in order to carry the heat from the bottom layer to the top, for better dissipation. A better view of the several zones in the PCB is on figure 3.8.

figure 3.8 - PCB Structure

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_039.png)

The resulting module in figure 3.9 is one of 65 built for this application where the layers are made in copper, 0.7μm each, with a 1.6mm thick FR-4 Glass-fibre core.

figure 3.9 - Assembled Slave module

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_040.png)

This way, it is possible to place the module inside the 5 cell groups, using 1mm aluminium Lshaped pieces to connect the cell group to the module, creating a good mechanical fixation system that also is an excellent electrical and thermal conductor. The L-Shaped connectors are asymmetrical, with the one for the right side, the negative pole, being very short, and the one for the positive side being very long. Since the heat dissipation area is on the positive side and the resistors used to dissipate the energy are low profile SMD type, size 3210, the connector is placed on top of the resistors, in order to dissipate the heat from the resistors to the aluminium metal that connects the five cell groups. An electrically non-conductive thermal pad is placed between the resistors and the L connector in order to allow a better heat dissipation without short-circuiting the resistors.

figure 3.10 - Top and Side view of a 5 cell module with the slave BMS installed

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_041.png)

Full schematics of the circuit and drawings of the aluminium L-shaped connecting elements are available on Appendix C.

## 3.8. Software

The software on the slave modules has been designed for an easy reconfiguration of the cell parameters and to guarantee the reliability of the system. The software also plays a very important part on the efficiency of the module, since it is where the power management is configured. This is extremely important, since the standby system consumption should be as low as possible, to assure the self-discharge rate of the battery.

The programming was done using the MPLAB suite from Microchip, with the C18 compiler, linker and assembler for C programming language, with the code divided in several files designated for each function of the modules.

With reliability and easiness of configuration in mind, all the parameters are stored in the microcontroller EEPROM, assuring any configurations made are kept if the system crashes. These are fixed values that are not changed during normal program execution, just when a CAN message is received to do so. When the execution begins, the program read this value from the EEPROM and stores them in local variables for faster access; these variables are updated whenever a reconfiguration is made. A list of all parameters is on Appendix F, table F.1.

After the initialization, the program enters the sleep mode, where it stays until an interruption occurs. There are two types of interruption in the program: a timer interruption and a CAN message interruption. The CAN message interruption occurs whenever a CAN message is received only if the received message is from the master module, since the microcontroller CAN module is configured this way. In every CAN message, there is a field that identifies the destination module, so if a module receives a message which is not destined to himself, it ignores the message and returns to sleep mode; if the message is for the receiving module, it will handle it accordingly and return to sleep afterwards. When a timer interruption occurs, the program will react according to its operating mode. There are four basic operation modes: Normal, Alert, Critical and Charging, which will be further discussed.

## 3.8.1. Normal Mode

In normal mode the microprocessor timer 0 is configured to wake up every 4 seconds with a timer interruption and launch a function to check the cell conditions.

This function reads the value from all the sensors and analyses the data read. If every value is within the expected normal values, the program returns to sleep, and no messages are sent to the master. If any value is outside the normal operating ranges, a message is sent to the CAN network to inform the Master Module of the occurrence: if a current is measured, but the load is turned off, a module mal-function is reported; if either the voltage or the temperature is outside the normal working ranges, the program is set in Alert mode, a message is sent to the Master Module reporting the situation and the timer 0 is reconfigured for 2 seconds periods, so that the situation is monitored more frequently.

The voltage and temperature of a cell never change value too rapidly therefore the 4 s period is enough to monitor the changes in the cell.

## 3.8.2. Alert Mode

If a voltage or temperature outside the normal range is measured, the program is set in alert mode. This is divided in four categories: high voltage, low voltage, high temperature and low temperature.

The program deals with the alert according to its category. If a low voltage, low temperature or high temperature is detected, the program sends messages continuously to the Master, advising this to shut down the battery. If a high voltage is measured, the program activates the balancing load at 75% of its dissipation capacity to lower this, while sending messages to the Master. The current is also measured to check if it is within the expected values, and if it is not, the Master is informed.

The sensors are measured every time the timer interruption is ran and if the values return to normal conditions, the operating mode is set back in normal; else, if the readings reach critical levels, the operation mode is set in Critical mode, the timer 0 is set for 1s periods and a message are sent to the Master module.

## 3.8.3. Critical Mode

If a critical value is detected, the vehicle should be immediately shut down, as there is imminent risk of permanently damage the battery which might result in injuries if a cell explodes.

This also works in a similar fashion from the Alert mode, in the sense that of a critically low voltage, or a critically low temperature or a critically high temperature is detected, a message is sent to the Master advising this to shut down the vehicle. If a critically high voltage is measure, the balancing load is set to 100% of its balancing capacity, to lower the voltage, and messages are sent to the master module so that it shuts the car down.

As the sensors continue to be measured, if the values return to non-critical values the program is set back in alert mode, working as previously described.

## 3.8.4. Charging

The charging mode operates as the three previous modes. The main difference is that when charging, any CAN message received with a current flow value, is processed as a current input.

This is only important on for the SOC determination, since this is also calculated for every cell block installed, to improve the SOC estimation.

An overview of the program flow is in figure 3.11.

figure 3.11 - Program flow

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_042.png)

Each module also determines its own SOC by means of Coulomb counting and voltage adjustment. Each time the Master module reads the current flow out of the battery, it broadcasts a CAN message to all the modules with that current value, so that these can estimate the used charge using a zero-order hold method, as described in chapter 2, section 2.12. Furthermore, each module has stored values for the state of charge corresponding to some voltage levels, which improves the estimation of the state of charge.

The watchdog feature is used, to assure the system recovers if it crashes. It consists on a timer causing the reboot of the system if the prescaler values are reached; therefore, whenever a timer interruption to read the sensors is launched, it also resets the watchdog timer. If the program execution freezes, the system will reboot after a few seconds.

The resulting program with all of its features has 7773 single-word instructions, out of the 8192 available on the program memory of the microcontroller, using the version 3.4 of the standard C18 compiler and MPLAB v8.70.

## 4. Master Module

## 4.1. Overview

The Master Module is one of the most important components in the system. It manages all the communications with the slave modules and the car electronic system, controls the cooling system and all the safety devices mentioned on chapter 0, measures the current in and out of the battery, stores data from the battery in a flash card and activates the Accumulator Insulation Relays, precharge and discharge circuits (figure 4.1).

Therefore, this module requires a good processing power, and several I/O functions.

figure 4.1 - Master BMS Architecture

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_043.png)

It was decided to use an already developed module that has been intensively tested and is widely used in the vehicle electronics system, the dsPIC FST Module - see 4.2. Then, a shield is coupled to the module that has the Input and Output connectors and drivers, and other devices - see 4.3.

## 4.2. dsPIC FST Module

The dsPIC FST Module was designed by Professor Moisés Piedade, at Instituto Superior Técnico, to be a multifunctional and versatile system, with special care to electromagnetic compatibility and analogue and digital signals mixing on the same PCB. Victor de Almeida [15] revised this module to be applied on Projecto FST vehicles, and since then it has been used in most of the electronic systems developed for it.

figure 4.2 - dsPIC FST module

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_044.png)

The core of this module is its microcontroller: a dsPIC30F6012A from Microchip [20]; this 16-bit microcontroller features CAN (2 channels), I 2 C, SPI and RS-232 communication protocols, 16 A/D ports, PWM and input capture modules, and a processing power that can reach 30MIPS (Millions of Instructions Per Second).

Since this module was designed to be implemented on automotive vehicles, it was design to be supplied by a 12V system; therefore it was essential to use a power converter, not only to adjust the output voltage, but also to filter electric noise on the supply system. The microcontroller works at 5V, so this was the voltage required for the output. Since the module is a base system to which can be added several expansion systems, it also has to provide power to these, therefore requiring a good power capacity. In addition it must have a high input tolerance since the vehicle battery voltage may float. The LM2676-5.0 was chosen for this purpose, since it provides a 5V constant supply from an input that can be between 8V and 40V, and supply up to 3A with an efficiency of 88%.

Another important feature of this module is the existence of two independent CAN communication buses, since this application requires the use of both lines. The configuration required for this to work with the vehicle electronics and the Slave modules discussed previously are in Appendix B, section B.4.

This module is currently used in several works developed under the supervision or in collaboration with Professor Moisés Piedade at the IST Electronics department since it is a good base system that can be used in very different applications, with the advantage of having all the ports from the microcontroller available to use. There are currently some works being developed with this module using new 32-bit microcontrollers from Microchip® that share the same footprint, and can be installed on the same PCB, but the voltage regulator has to be adjusted for this, since these microcontrollers typically work at 3.3V.

## 4.3. I/O Shield Hardware

In order to provide direct access to microcontroller in the dsPIC FST module and to integrate all the components required for the control of the several devices, a shield was developed for this system which incorporated all the connectors and drivers for the devices it manages, a slot for a SD memory card and power regulators for the SD card and the RTDS (Ready-To-Drive-Sound).

## 4.3.1. Relay driver

Four drivers control the relays for the positive and negative AIR, pre-charge circuit, and discharge circuits. Each of these is composed by a BSP030 MOSFET [17] connected between the ground circuit and the negative supply of the relays coils, breaking the power supply to these, and a 1N4007 Diode placed in parallel with the relay coils (figure 4.3).

figure 4.3 - Relay Drivers Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_045.png)

The MOSFETs are digitally controlled by the microcontroller in the dsPIC FST module, allowing this to process all available information and decide autonomously if the accumulator is ready to be activated when the driver presses the start button.

The relays connect to the system using small 2-pin connectors, which are able to handle the inrush current of the Accumulator Insulation Relays, keeping the connections simple with the power distribution made in the PCB.

figure 4.4 - AIR supply connector

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_046.png)

The power for these relays has a different source from the Master Module to which it is connected (figure 4.4). This is for safety reasons, since the power for these systems has a circuit with a total of 5 shutdown buttons and switches, where 3 of them are Emergency Mushroom buttons, one placed on the cockpit and the other two on each side of the car, at the same level has the drivers head (figure 4.5).

figure 4.5 - Schematic overview of the car's shutdown system, FSE rules, 2011

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_047.png)

This is mandatory by the FSE rules committee for improved safety, since the users have to be able to shut down the vehicle's tractive system if the Master Module freezes, or one of the relay drivers is short-circuited. There are also other safety devices on the circuit which are not discussed in this work since they are not a part of development of either the Battery Management System, or the Battery itself.

## 4.3.2. Fan Control

As mentioned in section 2.16, cooling represents an important part of the battery, not only to improve performance, but also to increase the battery lifespan. Therefore it is very important to control and monitor the cooling system, to assure this is working properly.

The microcontroller in the dsPIC FST module has built-in functions that allow an easy control and monitoring of the fan speeds, such as the PWM and Input Capture modules which allow the control and speed monitoring respectively. The used fans have a 4-wire system, with two used for the power supply (12V, 1.07A), one for speed control (PWM signal from 30Hz to 300kHz) and the other for speed measurement (Square wave with 4 impulses per revolution). There are four headers on the I/O shield, each with 4-pin connections for the fans, with the power distribution being made in the PCB, and dedicated lines for the speed control and measurement. Since the cooling system is designed to have all the fans working at the same speed, and these are all identical, it was decided to use only one PWM output from the microcontroller that is connected to all the fans with a driver in between, assuring that the current drain from the microcontroller is low. The driver uses the same MOSFET as previously described in section 4.3.1, in order to maintain the cost low (figure 4.6)

figure 4.6 - FAN speed control and measurement schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_048.png)

With this type of connection, it is required to pay attention to the duty cycle of the PWM, as the output from the driver will be the reverse of the input, since there is a pull-up on the output. Therefore, if the desired fan speed is 80%, the PWM should be 100%-80%=20% (figure 4.7).

figure 4.7 - Reversed driver input/output

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_049.png)

This also provides safety for the cooling system, since the fans will spin at the maximum speed if the master module freezes, since the PWM output will be a digital Low level, making the output of the driver a high level making the fans spin at the maximum speed. This is a characteristic of these fans and it is not guaranteed to work with fans from different manufacturers.

There is also a small 2-pin connector (figure 4.8) that allows the cooling system to be expanded, since it allows other fans to be connected if it is required.

figure 4.8 - FAN expansion connector

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_050.png)

The speed measurement is made individually for each fan, using the Input Compare functions of the dsPIC30F6012A. This module stores in a buffer the value read on a timer register of the microcontroller whenever a change of level on the input occurs. The speed can be determined using two consecutive instances on that buffer, and the time unit used by the buffer. The program can be configured to call a routine that determines the fan speed, dividing the frequency by 4, since the fan speed output changes level 4 times per revolution.

The Fans accept a PWM signal in a wide range of frequencies; therefore the value defined for the frequency is not very important, as long as it is between 30Hz and 300kHz. The used value for the frequency was 1kHz for energy saving and timer configuration reasons.

## 4.3.3. Ready-To-Drive-Sound

The implementation of the RTDS has already been discussed in section 2.15, consisting on a sound reproduction device from Siemens, model 3SB19 02-2BN, which works at 24V and has a power consumption of 10mA. Therefore, a power converter should be installed that transforms the 12V supply into a 24V output. The component used for this effect is the IE1224S from "XP Power", which has a low cost, 4-pin SIP package and provides a 24V, 42mA output, fulfilling the power requirements for the sound device. The control is made by the microcontroller using the same MOSFET driver as previously described in section 4.3.1, in order to maintain the cost down (figure 4.9).

figure 4.9 - RTDS Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_051.png)

The select converter has all the components built inside the SIP package, making this very easy to implement on the circuit. The only external devices are two tantalum capacitors to filter the input and output of the converter, which are 15μF SMD mounted capacitors, in a 3210 package. The acoustic transformer is connected to the circuit using a 2-pin connector.

## 4.3.4. Data logging

Data logging is an important feature for this system, since it provides not only information regarding the modules conditions, but also information about the power requirements of this type of vehicle, to help the development of future vehicles.

To provide easy access to the data stored, it was decided to use a Flash memory card, specifically a SD card; Microchip provides the required libraries that had to be modified in order to work with fast memory cards, which was done with the help from Projecto FST team member Miguel Silva. A characteristic of flash memory devices is that they require a 3.3V power supply. The component used for this effect was the MCP1703-3.3 from Microchip, a low cost LDO regulator in a SOT23-3 package, which has an output of 250mA. Also, since the SD card communicates with the microcontroller using an SPI bus, voltage dividers were placed in the SPI lines from the microcontroller (figure 4.10).

figure 4.10 - SD data logger schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_052.png)

The values for the resistors in the voltage divider were chosen considering the impedance of the SD card inputs, in order to obtain a value as close to 3.3V as possible. This is a simple and cost effective solution, since it does not required the use of dedicated buffers with voltage level adjustment.

Two capacitors were also installed on the voltage regulator, to filter any noise on the input or output. These are the same tantalum capacitors used in the DC/DC converter in the previous section, for cost reasons.

## 4.3.5. Start Switch

In order to activate the vehicle, a start switch was installed on the cockpit that allows the driver to command this operation. The switch has a two colour LED built-in which is used to tell the driver if the vehicle is ready to be started, pre-charging, or ready to drive.

On the shield there is a 4-wire connector where two of them are connected to the switch terminals, and the other two control the built-in LED (figure 4.11). The switch connections consist in having one terminal connected to the 5V supply and the other to the microcontroller, making use of the external interruption module. This way, whenever the driver presses the switch, an interruption routine is launched in the program that verifies if all the safety conditions are met and starts the activation of the battery, which consists in sounding the RTDS, activate the Negative pole AIR, activate the Pre-Charge circuit and Discharge circuit and, after the 5s pre-charge, activate the Positive pole AIR at the same time it deactivates the pre-charge circuit. There is also a Low Pass filter connected to the microcontroller input to filter any noise coming from the switch, and a timer was also implemented to check if the switch is pressed for more than 1.5s, avoiding accidental or electric noise derived activations of the system.

figure 4.11 - Start Switch Circuit Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_053.png)

The LED element is connected to two outputs of the microcontroller and has a current limiting resistor, allowing the current to flow in both ways and tough the microcontroller itself. The LED is turned off if the conditions to safely operate the car are not met; when the car is ready to be activated, it turns green; once the start switch is pressed and the pre-charge phase begins, it blinks green in 1s periods; finally, when the car is fully activated and ready to drive, it turns blue.

## 4.4. Printed Circuit Board

The main objectives when designing the PCB for the I/O shield were to keep the size of the board as close as possible to the size of the dsPIC module; having the SD card support in an accessible zone; keep the system simple and easy to assemble on the dsPIC module and in the battery, making it easy to replace either the dsPIC module or the shield itself; and have a low cost.

The components were chosen with the cost effectiveness in mind, e.g., with the drivers all use the same MOSFET for all the drivers, and low cost connectors. The result is a one layered PCB measuring 100x90mm, just slightly longer than the dsPIC module, but much wider to accommodate the SD card (figure 4.12).

figure 4.12 - I/O Shield PCB layout

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_054.png)

The fans control and connectors are also installed outside the dsPIC module perimeter, to facilitate the installation on the battery. All the passive components used are SMDs size 1608, except for some tantalum capacitors as previously referred. The several zones in which the PCB is structured are on described on figure 4.13.

figure 4.13 - PCB Structure

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_055.png)

The PCB has all the copper connections in one layer, mixing Surface Mount Devices with through-hole components and connectors. The majority of the components are installed on the copper surface, which is facing down towards the dsPIC module. The IDC connectors that are assembled on the pin headers from the dsPIC module are also surface mount single line female headers, as is the programming connector. The SD Card holder is also surface mount, though it requires holes for positioning. The rest of the connectors is placed on the opposing layer, using the through-hole properties to connect to the pads on the copper surface (figure 4.14).

figure 4.14 - PCB Tri-dimensional view

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_056.png)

There are some connections made with bounding wire, avoiding the use of two separate copper layers, thus reducing the cost.

There are two programming connectors on the shield, one that connects to the dsPIC module itself and the other that goes into a connector on the battery container, to allow easy access and reprogramming of the Master Module.

## 4.5. Software

As seen in the Slave modules analysis, the software plays one of the most important parts in the system, being essential for the system to work as desired. The Master system has to be in control of several systems connected to it, plus the two CAN buses, where one is for the control of the Slave modules. It is also required to define priorities for the devices, since the role played in the safety of the battery and its users is different for every device and therefore, the most important should be given a higher priority in the information processing. This is made possible by the microcontroller in the dsPIC module, which allows a priority definition in its interruptions.

The program execution is similar to the Slave modules, in the sense that it starts by initializing every module, entering the sleep mode afterwards where it will remain until an interruption occurs which can be caused by either a timer, a CAN message, or the Start Switch.

## 4.5.1. Timer interruption

There are two timers working in during the program execution, both that launch interruptions when the preconfigured time passes.

The first one, timer 4, is configured to launch an interruption every 50ms. This is to measure the current flow out of the battery in 50ms periods, information that is broadcasted to all the Slave Modules and used to process the SOC of the battery. This is calculated with the same ZOH model described in section 2.12, and the value is stored in the first position of the microcontroller EEPROM. This has a low priority since it does not compromise the safety of the system if a value is not read

The other timer, timer 5, is configured to wake up the microcontroller every 100ms and send a query to a Slave module for the readings of its sensors, to check if everything is ok with the module. Every time the interruption occurs, a different slave module is requested, taking a total of 4.8s to pool all the modules. Since every Slave module only reads its sensors every 4s, this time is enough to guarantee the readings are from different time instances. If an answer is not received in the 100ms period between queries, another is sent to the same module, since it may just be message collision case, or a message that was not read properly. The system tries a maximum of three times and if no message is received, it is set in Alert mode, moving on to the next module. If during the next round the module is still not replying, a CAN message is sent to the vehicle data information bus to warn the driver of the occurrence, and lets him decide whether to shut down the vehicle or keep running. If the same occurs to 3 modules simultaneously, the Master deactivates the battery to assure its integrity, warning the driver through CAN Messages to the dashboard.

The cooling system is also check on every 48 interruptions, making the fan speed to be measured every time the system checks all the slave modules. If the speed doesn't match the value set on the PWM, a message is sent to the vehicle information bus, reporting a cooling malfunction. If the system detects more than 2 fans stopped, it will deactivate the relays, regardless of the temperature inside the battery.

## 4.5.2. CAN message interruption

Whenever the microcontroller receives a CAN message on any of its 2 channels, an interruption is launched that awakes the microcontroller from its sleep mode. The channels are for communication with the vehicle electronics and with the BMS Slave modules, therefore making messages received in this second channel a high priority interruption and the messages in the first one with lower priority.

If an alert occurs in any of the slave modules, a message is automatically sent to the CAN bus for the Master to process, which will than act accordingly to the alert. If a low voltage alert is sent, the Master immediately deactivates de vehicle, to preserve the battery integrity. The same happens if the alert if with a low or high temperature warning and if a high voltage alert occurs without the car being charged. If the car is being charged, when a high voltage alert is sent, the system sends information to the information bus, so that if a charger is connected, to the CAN network, it lowers the charging current. If the voltage arises to critical values, the accumulator relays are opened, shutting down the charge. Any of these events is recorded in the SD card for posterior analysis.

When a query is sent to the slave modules, the system also wakes up with this interruption when the reply is received, with a message handling function dealing with the received information accordingly.

Messages received from the vehicle data bus can either be to shut down the system or a request for information. Other components in the vehicle may detect abnormal situations that may put the safety of the vehicle and its occupier at risk, thus sending that information to the vehicle electronics system. If this information is received by the BMS it immediately deactivates the relays, turning the power in the vehicle off. The BMS may also be queried for information regarding the SOC, and room temperature of the battery.

## 4.5.3. Start Switch interruption

The accumulator is activated through a push-button on the cockpit that connects directly to the battery and launches a low priority interruption when pressed.

When the interruption is launched, the system checks if it was really a start request or if it was electrical noise. The implemented method to check this was with a timer and a counter, making sure the pilot pressed the start switch intentionally. If the car is to be started, the pilot has to press the button for 1.5s, with the system verifying every 100ms if the button is being pressed. If the pilot releases the button in the 1.5s period, the vehicle will not start; else it will begin the start sequence.

This sequence consists in checking if all the fans are working, or if there any pending messages with alerts. If all these conditions are met, the system proceeds to active the negative pole AIR and the Pre-charge circuit, deactivates the discharge circuit, sounds the RTDS 3 times in 2 second periods, and activates the positive pole AIR after the 5s pre-charge is completed. The stage of the start sequence is also shown to the driver through the LED on the switch, as described in 4.3.5.

## 4.5.4. Charging

When the system is charging, a message to activate the relays should be sent through the system information bus to set the Master in charging mode.

By doing so, the system knows that it should expect the cells to enter alert modes, so that it won't shut down the battery. The system also changes the timer 5 interruption to be launched every 20ms instead of 100ms, making sure in can monitor the cells if they are in alert mode. The voltage of every cell is monitored permanently throughout the charging process and if any cell voltage is 5% higher than the lowest cell voltage in the battery, the balancing load is activated at 50% and it stays that way until the voltage is difference is below 2%. If the difference increases to 10%, the load is set at 75%, until it drops below 5%, where it is set to 50% again. The Slave module overcomes these settings if an alert occurs in the module.

This way, the system is kept in balance during the charge process, without the occurrence of cells with much higher or lower voltage than the rest of the cells.

The program also includes a watchdog timer that work as described in section 3.8, assuring that if the program execution freezes, it will reboot the microcontroller, which will open the accumulator insulation relays, thus deactivating the vehicle.

## 5. Test and Implementation

Since this is a critical component of one of the vehicles most important systems, it underwent several tests, for different time periods, to assure the reliability of the components.

The implementation of such system had to be carefully designed and planned since working with live batteries is dangerous.

Conducted test were also carefully planned ahead to minimalize the risk of accidents in the process, since there was no previous experience in working in this type of material.

## 5.1. Test

Several tests were made throughout the project phases. A total of 3 prototypes of the BMS Slave mode were designed, built and tested (figure 5.1) until the production version was ready.

figure 5.1 - BMS Slave Module V1.1

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_057.png)

In the early stages of development the tests were conducted using power supplies to simulate the cells. Later, after many tests, the trials were conducted using the cells to power the circuit, and several charges and discharges were made (figure 5.2).

figure 5.2 - Charging test

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_058.png)

These tests were also made to analyse the balancing circuit behaviour, mainly concerning the heat dissipation. Tests were conducted with a controlled charge with the cells at 4.0V, well above their healthy limits, with a current of 2.28A, all wasted in the resistors. The test showed the heat is well conducted through the aluminium connectors and on to the cells, with the PCB reaching 120ºC on the balancing load area. This is an effect that is not very desirable, but these tests were conducted in non-ventilated conditions and with the balancing load at its maximum power. The module was able to work correctly under those conditions, only with slight temperature deviations since the PCB temperature raised slightly, influencing the reading.

In these tests, it also possible to see that the temperature reading is influenced by the dissipation of energy in the connectors, since the reading is made in the PCB itself. The maximum registered temperature difference was 4ºC, when the cells were at 35º and the measured temperature was 31ºC, at a room temperature of 22ºC. This was considered within the project tolerance specifications.

## 5.2. Implementation

The system as it was designed requires 48 slave modules to monitor each of the 48 groups of 5 cells. Plus it was decided to build the Low Voltage battery using 4 of the same LiFePO4 cells, which also needed monitoring, thus making 52 the total number of modules required.

Therefore, in order to assure that there were spare parts available, a total of 65 modules were built, with the PCBs (figure 5.3) being ordered from PCBCart, in china, and the components from Digikey and Farnell.

figure 5.3 - PCBs before assembling

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_059.png)

The modules were all soldered by hand at the IST labs in INESC-ID and TagusPark, using precision tools and soldering stations (figure 5.4).

figure 5.4 - Assembled Modules, top and bottom layers

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_060.png)

The first tests conducted consisted in measuring the electrical resistance of the dissipative element and the voltage of the DC-DC converter output, when the input voltage is 1.8V and 4V, using a bench multimeter and a power supply to simulate the cell voltage. Each module was measured individually and the result of these measurements is on table H.1.

From the measurements conducted in this test, the average output voltage from the DC-DC converter was 4.9V, and the average electrical resistance of the balancing device is 1.69Ω.

The next step was an individual test of every function of each slave module, using the same source code modified for testing purposes only. This consisted in making periodic measurements of the voltage and temperatures, and activating the dissipative element with a PWM signal at a duty cycle of 50%. The voltage measurements were made using a power supply at 1.8V and 4.0V, while the room temperature was 22ºC, measured with the bench multimeters available on the lab. The purpose of these measurements was not only to check if every module was working correctly, but also to estimate the maximum deviations in the measurements made

The information was sent through the CAN bus, and the information was read by a USB-CAN converter that transmitted the information from the CAN bus to a PC that logged the measurements.

The results for the maximum deviations on the measurements are on table 5.1 and the measurements for each module are on Appendix H, table H.2.

table 5.1 - Maximum measurement deviations

| Maximum deviations: | Maximum deviations: |
| - | - |
| dV@1.8V | 0.027 [V] |
| dV@1.8V | 0.05 [V] |
| dT@1.8V | 2.25 |
| dT@4.0V | 2.48 |

The modules were then programmed with the production source code, a unique Serial Number and a default CAN ID corresponding to the number of the cell group in the battery. Finally, they were assembled in the cell groups, with special attention to the distances between the cells and the components in the modules (figure 5.5), applying a thermal pad in the screws heads assuring that if a cell touches it, there is no risk of short circuit.

figure 5.5 - Assembled Cell Groups

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_061.png)

The groups were assembled in columns composed with 12 modules bolted on 2 GFRP structures using (figure 5.6) M6x15mm Allen screws, replacing the ones holding the cells in the group where they meet the GFRP structure (figure 5.7).

figure 5.6 - Glass-Fibre-Reinforced-Plastic Structure

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_062.png)

figure 5.7 - Assembled Columns

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_063.png)

The columns were then assembled in the accumulator container along with the other system components (figure 5.8). The container consists on a steel frame with L-profiled steel bars welded together and using 1mm thick aluminium covers bolted to the structure.

figure 5.8 - Assembled Battery

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_064.png)

The battery was assembled on the vehicle, and the testing phase began, were the system worked as it was designed to.

## 6. Conclusions

In this work it was presented the design and implementation of a functioning Battery Management System on a racing vehicle, which was done successfully. The design of this system was done at the same time as the design of the battery itself, as well as the vehicle where it was applied.

The conception of the vehicle and its drivetrain was a process that took about 1 year, with the project being presented to a jury composed by members of the automotive industry in the Formula Student UK 2010 event, achieving the 1 st place in the competition against concepts from other universities. The battery design and implementation started in September 2010, with the completed system being presented to the public in July of 2011, when the test phase began. Some initial reliability issues were raised in the early testing stages and therefore there was not time to develop functionalities such as the aging effects analysis and improve the SOC estimation, which were not considered as important as having the car ready in time.

It was also concluded that the packaging is one of the most important aspects when designing a battery, since the whole design has to be made with assembling in mind since batteries cannot be turned off, and therefore there is a constant risk when working with them. The batteries should be carefully analysed prior to design and assembly, since it is very common to see cells where the outer shell is made of conductive materials and, in most cases, connected to a potential in the cell different from any of its poles, thus making it very easy to short-circuit a battery if a connection is made between one of its poles and the cell shell.

All of the targeted operating and measuring ranges were met, obtaining a system capable of measuring voltages with an error below of 0.05V and temperatures with an error of nearly 2.5ºC, worse case scenario.

This first Battery Management System developed by the Projecto FST team was successfully implemented on the FST04e racing vehicle, which has competed two Formula Student events were it was possible to see that the system works as it was designed to.

## 6.1. Cost analysis

Since this system was designed from the start to be produced in large quantities, the cost was one of the main criteria when choosing the components for the developed modules.

The costs presented in for the modules produced are on table 6.1, which are the costs as ordered for the production of 65 modules, with the order being made from Farnell and Digikey. The PCB was manufactured by PCBCart, one of Chinas leading PCB manufacturers, and the cost presented here includes the tooling for the PCB manufacturing.

table 6.1 - Slave Module cost breakdown

| Name | Description | Manufacturer | Part Number | Qty | Unit Cost | Total Cost |
| - | - | - | - | - | - | - |
| U1 | pic18F2480 | Microchip | PIC18F2480-I/ML | 65 | 3,65 € | 237,46 € |
| XTAL | 16MHz Crystal | ABRACON | ABM8G-16.000MHZ-18- D2Y-T | 65 | 0,89 € | 57,76 € |
| U3 | Temperature Sensor | Texas | TMP20 | 65 | 0,70 € | 45,21 € |
| Thermal Pad | Thermal Pad - 406.40mm x 203.20mm | Bergquist | GP1500R-0.010-02-0816 | 1 | 18,36 € | 18,36 € |
| U5 | MOSFET | NXP | BSP030,115 | 65 | 0,53 € | 34,45 € |
| ICD2 | Header 5Way Vertical | Molex | 53047-0510 | 65 | 0,36 € | 23,40 € |
| U2 | Isolated Can Transceiver | Texas | ISO1050DUBR | 65 | 3,27 € | 212,55 € |
| U4 | DC/DC Voltage booster | National | LM2621 | 65 | 1,11 € | 72,15 € |
| L1 | Coil, 4.7uH | Murata | LQH32CN4R7M33L | 65 | 0,24 € | 15,60 € |
| D1 | Schottky Diode, 70V, 0.5A | ON SEMICONDUCTOR | MMSD701T1G | 65 | 0,13 € | 8,39 € |
| R1, R2 | Resistor 1K0, 0603 | VISHAY DRALORIC | CRCW06031K00FKEA | 150 | 0,02 € | 3,15 € |
| R3 | Resistor 510R, 0603 | VISHAY DRALORIC | CRCW0603510RFKEA | 100 | 0,02 € | 2,10 € |
| R4 | Resistor 200K, 0603 | MULTICOMP | MC 0.063W 0603 1% 200K | 100 | 0,04 € | 3,60 € |
| R5 | Resistor 150K, 0603 | MULTICOMP | MC 0.063W 0603 5% 150K | 100 | 0,01 € | 0,50 € |
| R6 | Resistor 51K, 0603 | VISHAY DRALORIC | CRCW060351K0FKEA | 100 | 0,02 € | 2,10 € |
| RON | Resistor 10K, 0603 | VISHAY DRALORIC | CRCW060310K0JNEA | 100 | 0,02 € | 1,90 € |
| RLxx | Resistor 33R0, 500mW, 1206 | MULTICOMP | MCHP06W2F330JT5E | 1300 | 0,02 € | 23,40 € |
| RIL | Resistor 0R1, 500mW, 1206 | YAGEO | RL1206FR-7W0R1L | 100 | 0,18 € | 18,20 € |
| LED | LED, SMD, GREEN | AVAGO | HSMG-C190 | 65 | 0,07 € | 4,49 € |
| C1 | Capacitor, 15uF, Tantalum, 1206 | AVX | TPSA156K006R1500 | 100 | 0,15 € | 15,10 € |
| C2 | Capacitor, 33uF, Tantalum, 1206 | AVX | TLJS336M010R1500 | 100 | 0,30 € | 30,00 € |
| C3, C7, C8, C9, C12 | Capacitor 0,1uF, Ceramic, 0603 | MULTICOMP | MCCA000256 | 300 | 0,01 € | 2,40 € |
| C4 | Capacitor 1nF, Ceramic, 0603 | MULTICOMP | MCCA000224 | 100 | 0,01 € | 0,80 € |
| C5, C6 | Capacitor 22pF, Ceramic, 0603 | MULTICOMP | MCCA000196 | 200 | 0,01 € | 1,60 € |
| C11 | Capacitor 39pF, Ceramic, 0603 | KEMET | C0603C390J1GACTU | 100 | 0,03 € | 3,10 € |
| CAN Connector | HEADER, SQUARE PIN, 2.54MM, 4WAY | MULTICOMP | MC34633 | 70 | 0,35 € | 24,50 € |
| CAN Cable | CRIMP HOUSING, 2.54MM, 4WAY | MULTICOMP | MC34485 | 70 | 0,16 € | 11,27 € |
| CAN Cable pin | CRIMP PIN, 22-26AWG | MULTICOMP | 2218T | 300 | 0,06 € | 17,70 € |
| PCB | Slave Board PCB | PCB Cart | BMS | 65 | 2,03 € | 131,76 € |
|  |  |  |  | Total Cost / Module | Total Cost / Module | 1.022,99 € 15,74 € |

The cost for the Master Module is shown in table 6.2, considering a 50 unit production since the estimated cost in [19] for the dsPIC module is €33.05, in a 50 unit production. The solution presented in this work is not the most cost effective, since in a mass production scenario it would justify the unification of both Master Module and the Shield used for input and output control. Despite this, the cost is still lower that most products currently on the market.

table 6.2 - Master Module cost, in a 50 unit production

| Description | Qty | Total Cost |
| - | - | - |
| dsPIC Module [19] | 1 | 33,05 € |
| I/O Shield PCB, 1 Layer | 1 | 2,26 € |
| Header, 2 | 8 | 1,42 € |
| Header, 4 | 8 | 2.88 € |
| Header, 5 | 1 | 0,46 € |
| IDC 5pin, Fem | 1 | 0,86 € |
| IDC 20 pin, Fem | 2 | 3,56 € |
| IDC 16 pin, Fem | 2 | 3,08 € |
| SD Card Socket | 1 | 1,67 € |
| BSP030 MOSFET | 6 | 3,18 € |
| XP Power IE1224S | 1 | 4,78 € |
| Diode 1N4007 | 4 | 0,16 € |
| MCP1703 voltage regulator | 1 | 0,37 € |
| SMD Resistors | 13 | 0,65 € |
| SMD Capacitors | 5 | 0,75 € |
|  |  | 59,16 € |

These costs do not consider the labour involved in the module assemble, neither in the CAN harness production.

If the vehicle was produced in mass production, e.g., 1000 cars per year, the production of slave modules will be at least 48000 units per year, given that every battery requires 48 modules, and the production of master modules would be 1000 units per year. This would bring the cost down to 2 3 � of the costs presented here.

## 6.2. Future work

As in any first functioning prototype, there is a lot of room for improvements in this work to make it simpler to produce, easier to use and more cost effective.

The first one is the choice of the microcontrollers. On the slaves modules, it should be used a microcontroller with much more program memory, since these modules could have much more functions built in which were not applied due to the misjudgement of memory requirements. The PCB is already prepared to receive the PIC18F25K80, which was launched by Microchip while this project was being developed and wasn't available on the market at the time of construction. This microcontroller costs about half of the one used in the project, has more than twice the memory and built in voltage references.

The use of another microcontroller would also allow the use of a CAN bootloader, which means it would be possible to reprogram the modules while mounted on the batteries, instead of disassembling the whole battery to reprogram every slave module.

For the Master module, the 32bit version of the dsPIC FST module should be used, giving the system a higher computing power, capable of faster operations which would allow the implementation of more complex and precise control systems that could provide a better estimations of the several parameters, like the SOC. This would also allow the implementation of a small ftp server to provide a better way to store and access data. Also, to provide better access to the data, a Wi-Fi or Ethernet link could be implemented, allowing easy access to any authorized computer with a network interface.

A Real-Time clock should also be implemented, to allow better analysis of the aging effects of the battery, as well as a temperature sensor on the master module to measure the room temperature of the accumulator container.

A supervising system should be implemented that communicates with the Master module, in order to check if it is working properly. This should attempt to restart the master module and either control the Accumulator Insulation Relays, or be connected to the vehicle information system to warn the driver of a mal-function on the battery. This is a safety feature that is not mandatory by the competition rules, but it is a standard in the Electric Automotive industry and therefore it should be implemented in future versions of the system.

Power Measuring Module should be designed to measure the current and the voltage in a separate system, communicating through isolated LIN or CAN Bus with the BMS. This would provide an easier way to measure the amount of energy spent, as well as the conditions of the AIR, while being completely isolated from the BMS control module, thus avoiding electric noises, and different voltage references issues.

## Bibliography

- [1] Gabriel Rodrigues, "Modelação e Simulação de um Formula Student Eléctrico", IST, Lisboa, Outubro de 2009
- [2] Elithion LLC, Li-Ion BMS Solutions, http://liionbms.com/, accessed 03-10-2011
- [3] Toyota Motors, http://www.toyota.com/prius-hybrid/, accessed 07-10-2011
- [4] Tesla Motors, http://www.teslamotors.com/roadster, accessed 06-10-2011
- [5] SK innovation, http://eng.skinnovation.com/, accessed 07-10-2011
- [6] Bosch Gmbh, http://www.bosch.com, accessed 17-10-2011
- [7] [Honeywell CSNS300 Current Sensor datasheet, accessed 18-10-2011, http://www.honeywellsensor.com.cn/prodinfo/sensor\_current/datasheet/CSNS300M\_CHN.pdf](http://www.honeywell-sensor.com.cn/prodinfo/sensor_current/datasheet/CSNS300M_CHN.pdf)
- [8] TRACO POWER TEN 8WI series datasheet, accessed 18-10-2011, http://www.tracopower.com/products/ten8wi.pdf
- [9] Tyco Electronics EV200, accessed 18-10-2011, http://relays.te.com/datasheets/ev200.pdf
- [10] AutoSil, Grupo A.A. Silva, accessed 18-10-2011, http://www.autosil.pt/
- [11] Ventura Rodrigues Consultadoria Engenharia LDA, accessed 18-10-2011, http://www.venturarodrigues.pt/
- [12] Fluke Ti9 Thermal Imager, accessed 18-10-2011, http://www.fluke.com/fluke/uken/ThermalCameras/Fluke-Ti9.htm?PID=56189
- [13] Solidworks FloWorks, accessed 18-10-2011, http://www.solidworks.com/sw/products/cfdflow-analysis-software.htm
- [14] National Semiconductor Inc., LM2621 datasheet, accessed 09-10-2011 http://www.national.com/pf/LM/LM2621.html#Overview
- [15] Microchip Technology Inc., PIC18F2480 Datasheet , accessed 09-10-2011, http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en020612#
- [16] Texas Instruments Inc., TMP-20 datasheet, accessed 09-10-2011, http://www.ti.com/product/tmp20&amp;lpos=Middle\_Container&amp;lid=Alternative\_Devices
- [17] NXP Semiconductors Inc., BSP030 datasheet, accessed 09-10-2011, http://www.nxp.com/#/pip/pip=[pip=BSP030]|pp=[t=pip,i=BSP030]
- [18] [Texas Instruments Inc.,ISO1050 CAN transceiver datasheet, accessed 09-10-2011 http://www.ti.com/ww/en/analog/iso1050/index.shtml?DCMP=A\_Signal%20Chain\_ICP\_Inter face\_Leadership&amp;CMP=KNC-GoogleTI&amp;247SEM](http://www.ti.com/ww/en/analog/iso1050/index.shtml?DCMP=A_Signal%20Chain_ICP_Interface_Leadership&CMP=KNC-GoogleTI&247SEM)
- [19] Victor de Almeida, "Volante Electrónico para o FST", IST, Lisboa, Outubro de 2009
- [20] Microchip Technology Inc., dsPIC30F6012A datasheet, accessed 18-09-2011, http://www.microchip.com/wwwproducts/Devices.aspx?dDocName=en024764
- [21] Formula Student Electric, http:// www.formulastudentelectric.com, accessed 09-10-2011
- [22] DUT Racing, TU Delft, http://dutracing.nl/?lang=en, accessed 09-10-2011
- [23] Formula Student Spain, http://www.formulastudent.es/, accessed 09-10-2011
- [24] Formula Student, http://www.formulastudent.com, accessed 09-10-2011

- [25] M. Broussely, G.Pistoia, "Industrial Applications of Batteries - From Cars to Aerospace and Energy Storage", ELSEVIER, 2007
- [26] Valer Pop, Henk Jan Bergveld, Dmitry Danilov, Paul P. L. Regtien, Peter H. L. Notten, "Battery Management Systems - Accurate State-Of-Charge Indication for Battery-Powered Applications", Springer, 2008

## Appendix A

## Formula Student and Projecto FST

In this appendix, a short introduction to the Formula Student competitions can be found, as well as some insight on the team Projecto FST and the vehicle FST04e.

## A.1 Formula Student

Adapted from What is Formula Student? at formulastudent.com:

Started in the United States by SAE in 1981, the Formula SAE programme was considered to be very worthwhile in providing students with excellent learning opportunities and practical skills. In europe the IMechE accepted the management of the European venture in a partnership with SAE. Formula Student (the name given to the event held in England) is different from Formula SAE in that it is designed to be a progressive learning exercise throughout the different classes. However, the same rules are used for both Formula Student and Formula SAE (with some minor changes).

Formula student provides the students with a real-life exercise in design and manufacture and the business elements of automotive engineering. It teaches them all about team working, under pressure and to tight timescales. It demands total commitment, lots of late nights, and many frustrations and challenges along the way, but the result is the development of highly talented young engineers.

For the purpose of the competition, the students are to assume that a manufacturing firm has engaged them to produce a prototype car for evaluation. The intended sales market is the non-professional weekend autocross or sprint racer. Therefore, the car must have very high performance in terms of its acceleration, braking, and handling qualities. The car must be low in cost, easy to maintain, and reliable. In addition, the car's marketability is enhanced by other factors such as aesthetics, comfort and use of common parts. The challenge to the team is to design and fabricate a prototype car that best meets these objectives. Each design is compared and judged with other competing designs to determine the best overall car.

The teams have their work judged by Industry specialists and demonstrate the performance of the car. It is not simply the fastest car that wins, students have to balance speed with safety, reliability, cost and good handling qualities.

## A.2 Projecto FST

The team from IST is formed by students of both mechanical and electronics engineering. It has already successfully delivered 4 prototype vehicles, from which 2 are still in the active. This work is aimed at the latest built prototype, the FST04e, whose main technical specifications can be found in table A.1.

table A.1 - FST04e Specifications

| General dimensions |  |
| - | - |
| Overall Length Overall Width Overall Height Wheelbase Track Weight with 68 kg driver | 2954 mm 1451 mm 1269 mm 1650 mm 1230 mm (front) 1200 mm (back) 161 kg (front) 175 kg (back) |
| Frame |  |
| Construction Material | Tubular Space Frame AISI 4140 Steel |
| Tractive System |  |
| Manufacturer / Model No. of motors Motor Driven Wheels Type of motors Max RPM Max Torque Max Power Type of motor controller Accumulator Cell Technology Accumulator Cell Configuration Accumulator Voltage when fully charged Accumulator Capacity | Agnimotors 95-R 2 Rear wheels through chain and sprocket Brushed Permanent Magnet DC 6000 60Nm p/ motor 60KW Student built, MOSFET, high frequency PWM LiFePO4 48s5p 175.2V 7,68 KWh |
| Drivetrain |  |
| Differential type Drive Ratio | Torsen FSAE 012000, 4:1 TBR 5.8:1 |
| Suspension |  |
| Suspension type | Double unequal length A-arm, Pull-rod actuated - front, Push-rod actuated - Read |
| Wheels |  |
| Wheels Tyres | 7.2x13", 3 pc Aluminium Rims Avon 195x89 R13 Slicks |
| Body |  |
| Bodywork Seat | Carbon fibre, 3 piece (Nose, Left, Right) Carbon fibre |

So far, this prototype has competed in two events in 2011, in Germany and Spain. Formula Student Electric [21] is the German event and it was created especially for electric vehicles with a huge support from some car manufacturers and automotive related companies in Germany such as Audi BMW, Bosch, Daimler and Siemens, who pressured the VDI (the German Engineers Association) to create the event as a spin-off from the Formula Student Germany, the biggest competition of this type in Europe with more than 100 teams attending this year's event, in August at the Hockenheim circuit. From these teams, 31 where competing with Electric Vehicles, being Projecto FST one of them. After many sleepless nights and many unforeseen problems, the team managed to stay in 13 th overall, with a lot of positive judge reviews for the simplicity and functionality of the powertrain, as well as high praises to the amount of self-developed electronic systems - such as the BMS - especially being develop by such a small number of team elements.

figure A.1 - The FST04e on the AutoCross Event, FSE2011

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_065.png)

This was a very positive result for the team, as it was the first electric vehicle developed by the 17 element team with a very small budget supplied mostly by sponsoring companies (figure A.2). The wining team on this event was from the Technical University of Delft, DUT Racing [22] which is composed by 107 elements and has a very high budget supplied mostly by the university itself.

figure A.2 - The Projecto FST team

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_066.png)

In September 2011, the team participated on the recently created Spanish event, Formula Student Spain 69[23] which was organized by the Spanish Society of Automotive Engineers, STA, and was held in the Circuit de Catalunya, in Barcelona, for the second consecutive year.

This event is also becoming very interesting for teams all around the world since it offers track and weather conditions like no other European event, the participating fees are lower, and it follows the German event set of rules, the most strict and safe on the competition.

figure A.3 - The FST04e at the FSS2011 event

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_067.png)

This event whet particularly well for the Projecto FST team, achieving the 1 st place in both Cost and Business presentation events, and 2 nd place overall, even though the car was running at a very limited pace with a damaged motor controller. The mechanical part of the FST04e was also very high praised by the judges at the event with the chassis and suspension showing excellent performance on the dynamic events.

The next step for the team is continuing testing and development on the FST04e to participate in the Formula Student event, in the United Kingdom in 2012. The team is also currently designing the next prototype, the FST05 which will have an electric drivetrain as well, and will probably feature a Carbon-Fibre-Reinforced Plastic monocoque chassis similar to the ones used in Formula 1 and the first ever built in Portugal for racing purposes.

## Appendix B CAN bus protocol

In this appendix an introductory explanation of the CAN-bus protocol can be found and also the method to compute the CAN-bus controlling hardware registers configuration values.

## B.1 Message arbitration

In order to support a non-destructive bitwise arbitration it is first necessary to define the logic states as dominant or recessive and also have each node monitoring the state of the bus. The CAN protocol defines the logic bit 0 as the dominant bit and the logic bit 1 as the recessive bit. A dominant bit always prevails over a recessive bit in what concerns arbitration, which translates in the lowest Message Identifier (fields used for arbitration) values having the highest priority. In this way if two nodes are trying to transmit a message at the same time, and since they monitor the bus to check if the voltage level they are sending is actually appearing on the bus, when a recessive bit appears in the lowest priority message the monitored state of the bus will be dominant. Here, the node transmitting the lowest priority message loses the arbitration and, as it notices the loss, it stops transmitting. Meanwhile the message sent by the higher priority node wasn't corrupted and it is continued until the end. The losing node keeps monitoring the bus waiting for a period of no activity to send its message.

## B.2 Error handling

The nodes on a CAN network have the ability to detect fault conditions and change their behaviour accordingly, implementing in this way fault confinement in the bus. There are five error conditions that relate to errors in CRC calculation, failure to acknowledge, bad message format, bit monitoring and bit stuffing. The number and type of error conditions define in which of three states a node is in. These can be error active, with the node being in full working condition while it's transmitting and receiving error counters do not reach 128, error passive, being active but with differences in the way it flags errors until its error counters reach 255 from which it goes on the bus-off state and cannot send or receive messages. This way error confinement is achieved and no faulty CAN node is able to "eat" the entire network's bandwidth.

## B.3 Message format

In figure B.1 the format of a CAN data frame can be found.

figure B.1 - CAN 2.0B data frame

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_068.png)

## B.4 Bit timming

To configure the CAN controller for the network's operating speed proper configuration of the bit timing is needed. Each bit in the CAN-bus is divided 4 segments: the synchronization segment, the propagation segment, the phase 1 segment and the phase 2 segments, as can be seen in figure B.2. The synchronization segment is always 1 bit long and exists for clock synchronization. The propagation segment allows delays in the bus to be compensated, and the phase 1 and 2 segments are configured to have the sampling point in the right place.

figure B.2 - A CAN bit and Its Segments

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_069.png)

The time one symbol takes is divided in time quantas, and depending on the desired speed for the bus, the number of time quantas (TQ) that fit inside a CAN bit varies. This means that in a CAN network the bit rate is the same for all the nodes (the symbol time is the same), what is different, according to the controller's clock (𝐹𝑜𝑠𝑐), is the number of time quantas that each bit is understood to have. Likewise the registers for each one of the segments are configured accordingly and making sure that the sampling point is between 60% and 70% of the whole bit time. There are also registers synchronization jump width and baudrate prescaler (BRP) are used for adjustments to the bus clock and as a clock prescaler respectively. The computation of the register values defined for each module starts by defining the speed wanted on the bus. In this case:

<!-- formula-not-decoded -->

and then using the CAN-bus controller equation the PIC2480 datasheet:

<!-- formula-not-decoded -->

which, having 𝐹𝑜𝑠𝑐 = 16𝑀𝐻𝑧 and 𝐵𝑅𝑃 = 0, results in 𝑇𝑄 = 0.125𝜇𝑠.

From here, the time quantas are divided by the 4 segments, having in mind where the sampling point is. The Nominal bit rate is determined by:

<!-- formula-not-decoded -->

In order to have the sampling point at 75%, the values used in these segments for the Slave modules are on table B.1.

table B.1 - Slaves CAN Baudrate Registers

| Register | Value |
| - | - |
| Sync Segment | 1 |
| Propagation Segment | 3 |
| Phase Buffer Segment 1 | 2 |
| Phase Buffer Segment 1 | 2 |

The Master Module CAN buses work in a similar way to the Slave modules, with the time equations being the same. The main difference is the oscillator frequency, which is 𝐹𝑜𝑠𝑐 = 20𝑀𝐻𝑧, resulting in different time quantas.

This both CAN channels are configured to work at 1Mbit.s -1 with a sampling point at 70%, resulting in the segment values on table B.2.

table B.2 - Master CAN Baudrate Registers

| Register | Value |
| - | - |
| Sync Segment | 1 |
| Propagation Segment | 1 |
| Phase Buffer Segment 1 | 5 |
| Phase Buffer Segment 1 | 3 |

This was heavily tested on both communication buses to assure the reliability of the communication in the Master-Slaves and Master-Vehicle electronics links.

## Appendix C

## Cell block connectors

116

figure C.1 - 5 Cell group connector, trapezoidal shaped

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_070.png)

figure C.2 - 5 Cell group connector, linear shaped

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_071.png)

74

figure C.3 - Cell Blocks interconnector

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_072.png)

## Appendix D

## Agnimotors 95-R

table D.1 - Agnimotors 95-R Specifications

| rpm/V | max. V | A cont. @48V | cont. output power@48V | max | cont. output | max. power for |
| - | - | - | - | - | - | - |
| rpm/V | max. V |  |  | rpm | power | 5sec |
| 71rpm/V | 84V | 230A | 9.5kW | 6000rpm | 16kW@78V | 30kW |

## 71RPM/VOLT AT 72V

95-turn armature (re inforced version only) Recomended for'Sporting'applications only, such as a motorcycle or speedboat

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_073.png)

Amps

figure D.1 - Agnimotors 95-R Power and Torque curves

## Appendix E

## Accumulator Fusing - Siemens 3NE8 731-1

## BETA Protecting SITOR Semiconductor Fuses

## SITOR, LV HRC design

Series 3NE8 72.-1, 3NE8 731-1

Size:

Rated voltage:

Operational class:

Rated current:

000

690 V AC/700 V DC acc. to UL

aR

80 ... 315 A

## Time/current characteristic curves diagram

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_074.png)

## Correction factor kA for breaking t²t value

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_075.png)

4/42

Siemens ET B1 AO - 2009, Characteristic curves for fuses

figure E.1 - Siemens Fuse Characteristic curve

© Siemens AG 2009 © Siemens AG 2009

4

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_076.png)

## Peak arc voltage

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_077.png)

## Appendix F BMS Slave Modules

## F.1 Electrical Schematics

figure F.1 - Slave Modules Full Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_078.png)

## F.2 Aluminium connectors and support mounts

figure F.2 - L shaped BMS connector, minus terminal

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_079.png)

10

figure F.3 - L shaped BMS connector, Plus terminal

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_080.png)

## F.3 BMS Slave Parameters

table F.1 - Slave Parameters

| Name/Category | Default Value | Description |
| - | - | - |
| Firmware Info |  |  |
| FIRMWARE_V_H FIRMWARE_V_L | 1 1 | Firmware Version, HIGH Firmware Version, LOW |
| Serial Number Info |  |  |
| CMM_SN | FSTBMS01M001 | Cell Management Module Serial Number |
| CAN Parameters |  |  |
| CAN_MASTER_ID D_CAN_ID | 0 1 | Default CAN Master ID Default Slave CAN ID |
| Cell Parameters |  |  |
| D_V_MAX | 763 (3.65V) | Maximum Voltage allowed |
| D_V_MAX_H | 794 (3.8V) | Critical High Voltage Value |
| D_V_MAX_L | 742 (3.55V) | Safe Voltage High Limit |
| D_V_LOW | 418 (2.0V) | Lowest Voltage allowed |
| D_V_LOW_H | 460 (2.2V) | Lowest Voltage Recommended |
| D_V_LOW_L | 376 (1.8V) | Critical Lowest Voltage |
| D_T_MAX | 241 (60ºC) | Maximum Temperature allowed |
| D_T_MAX_H | 217 (70ºC) | Critical Temperature |
| D_T_MAX_L | 254 (55ºC) | Safe Temperature High Limit |
| D_T_LOW | 389 (0ºC) | Lowest Temperature allowed |
| D_T_LOW_H | 377 (5ºC) | Safe Lowest Temperature |
| D_T_LOW_L | 401 (-5ºC) | Critical Lowest Temperature allowed |
| D_I_SAMPLE_TIME | 50 (50ms) | Sample time ms for current drain measurement |
| D_SOC | 100 (100%) | Default SOC is 100% |
| D_QC | 50000000 (50Ah) | Default current capacity is 50Ah (SOC 100%) |
| D_QN | 500000 (50Ah) | Default nominal capacity is 50Ah, divided by 100 (100%) |
| D_V_SOC_100 | 700 (3.4V) | Default Voltage at which the battery charge is 100% |
| D_V_SOC_5 | 470 (2.3V) | Default Voltage at which the battery charge is 5% |
| Load Settings |  |  |
| D_LOAD_VAL | 767 (75%) | Duty cycle for load |
| D_LOAD_VAL_H | 1023 (100%) | Duty cycle for load in Critical situations |

- F.4 BMS FST04e CAN Specification

Message Code PONG 0x07 ACK 0x0F UNKOWN\_COMAND 0x08

PING - 0x10

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | PING |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

QUERY

GET\_SLAVE\_ID - 0x11

QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_SLAVE_ID |
| Data[1]: | CAN_MASTER_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ V\_MAX - 0x12

QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_MAX |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ V\_MAX\_H - 0x13 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_MAX_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ V\_MAX\_L - 0x14 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_MAX_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | PONG |
| Data[1]: | - |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 2 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_SLAVE_ID |
| Data[1]: | CAN _ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_MAX |
| Data[1]: | V_MAX |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_MAX_H |
| Data[1]: | V_MAX_H |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_MAX_L |
| Data[1]: | V_MAX_L |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ V\_LOW - 0x15 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_LOW |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ V\_LOW\_H - 0x16 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_LOW_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ V\_LOW\_L - 0x17 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_LOW_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ T\_MAX - 0x18

## QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_T_MAX |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ T\_MAX\_H - 0x19 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_T_MAX_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_T\_MAX\_L - 0x1A QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_T_MAX_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_LOW |
| Data[1]: | V_LOW |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_LOW_H |
| Data[1]: | V_LOW_H |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_LOW_L |
| Data[1]: | V_LOW_L |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_T_MAX |
| Data[1]: | T_MAX |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_T_MAX_H |
| Data[1]: | T_MAX_H |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_T_MAX_L |
| Data[1]: | T_MAX_L |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ T\_LOW - 0x1B QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_T_LOW |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ T\_LOW\_H - 0x1C QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_T_ LOW_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_T\_LOW\_L - 0x1D QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_T_LOW_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ LOAD\_VAL - 0x1E

## QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_LOAD_VAL |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ LOAD\_VAL\_H - 0x1F QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_LOAD_VAL_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ MAX\_IL - 0x20 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_MAX_IL |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_T_ LOW |
| Data[1]: | T_ LOW |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_T_LOW_H |
| Data[1]: | T_LOW_H |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_T_LOW_L |
| Data[1]: | T_LOW_L |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_LOAD_VAL |
| Data[1]: | LOAD_VAL |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_LOAD_VAL_H |
| Data[1]: | LOAD_VAL_H |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_MAX_IL |
| Data[1]: | MAX_IL |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ I\_SAMP\_TIME- 0x21 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_ I_SAMP_TIME |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ SOC - 0x22 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_SOC |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ QC - 0x23 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_QC |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_ QN - 0x24

## QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_QN |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_V\_SOC\_100 - 0x25 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_SOC_100 |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

GET\_V\_SOC\_5 - 0x26 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | GET_V_SOC_5 |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_ I_SAMP_TIME |
| Data[1]: | SOC |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_SOC |
| Data[1]: | SOC |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_QC |
| Data[1]: | QC[0:15] |
| Data[2]: | QC[16:31] |
| Data[3]: | - |
| DLC: | 6 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_QN |
| Data[1]: | QN[0:15] |
| Data[2]: | QN[16:31] |
| Data[3]: | - |
| DLC: | 6 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_SOC_100 |
| Data[1]: | V_SOC_100 |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_V_SOC_5 |
| Data[1]: | V_SOC_5 |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

REFRESH\_EEPROM - 0x30 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | REFRESH_EEPROM |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

SET\_SLAVE\_ID - 0x31 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_SLAVE_ID |
| Data[1]: | SLAVE_ID |
| Data[2]: | SLAVE_ID (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ V\_MAX - 0x32 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_V_MAX |
| Data[1]: | SLAVE_ID |
| Data[2]: | V_MAX (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ V\_MAX\_H - 0x33

## QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_V_MAX_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | V_MAX_H (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ V\_MAX\_L - 0x34 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_V_MAX_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | V_MAX_L (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ V\_LOW - 0x35

QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_V_LOW |
| Data[1]: | SLAVE_ID |
| Data[2]: | V_LOW (new) |
| Data[3]: | - |
| DLC: | 6 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | REFRESH_EEPROM |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID (new) |
| - | - |
| Data[0]: | SET_SLAVE_ID |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_V_MAX |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_V_MAX_H |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_V_MAX_L |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_V_LOW |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

SET\_ V\_LOW\_H - 0x36 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_V_LOW_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | V_LOW_H (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ V\_LOW\_L - 0x37 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_V_LOW_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | V_LOW_L (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ T\_MAX - 0x38 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_T_MAX |
| Data[1]: | SLAVE_ID |
| Data[2]: | T_MAX (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ T\_MAX\_H - 0x39 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_T_MAX_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | T_MAX_H (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_T\_MAX\_L - 0x3A QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_T_MAX_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | T_MAX_L (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ T\_LOW - 0x3B

QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_T_LOW |
| Data[1]: | SLAVE_ID |
| Data[2]: | T_LOW (new) |
| Data[3]: | - |
| DLC: | 6 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_V_LOW_H |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_V_LOW_L |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | GET_T_MAX |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_T_MAX_H |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_T_MAX_L |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_T_ LOW |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

SET\_ T\_LOW\_H - 0x3C QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_T_ LOW_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | T_LOW_H (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_T\_LOW\_L - 0x3D QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_T_LOW_L |
| Data[1]: | SLAVE_ID |
| Data[2]: | T_LOW_L (new) |
| Data[3]: | - |
| DLC: | 4 |

SET\_ LOAD\_VAL - 0x3E QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_LOAD_VAL |
| Data[1]: | SLAVE_ID |
| Data[2]: | LOAD_VAL (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ LOAD\_VAL\_H - 0x3F QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_LOAD_VAL_H |
| Data[1]: | SLAVE_ID |
| Data[2]: | LOAD_VAL_H (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ MAX\_IL - 0x40 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_MAX_IL |
| Data[1]: | SLAVE_ID |
| Data[2]: | MAX_IL (new) |
| Data[3]: | - |
| DLC: | 6 |

SET\_ SOC - 0x41 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_SOC |
| Data[1]: | SLAVE_ID |
| Data[2]: | SOC (new) |
| Data[3]: | - |
| DLC: | 6 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_T_LOW_H |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_T_LOW_L |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_LOAD_VAL |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_LOAD_VAL_H |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_MAX_IL |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_SOC |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

READ\_VBAT - 0x50 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | READ_VBAT |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

READ\_TEMP - 0x51 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | READ_TEMP |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

READ\_IL - 0x52 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | READ_IL |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

READ\_ LOAD\_STATUS - 0x53 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | READ_LOAD_STATUS |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

READ\_SENSORS - 0x54 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | READ_SENSORS |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

SET\_LOAD - 0x60 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_LOAD |
| Data[1]: | SLAVE_ID |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | READ_VBAT |
| Data[1]: | VBAT |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | READ_TEMP |
| Data[1]: | VTEMP |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | READ_IL |
| Data[1]: | IL |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | READ_LOAD_STATUS |
| Data[1]: | LOAD_STATUS |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | READ_ SENSORS |
| Data[1]: | VBAT |
| Data[2]: | VTEMP |
| Data[3]: | IL |
| DLC: | 8 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_LOAD |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

SET\_LOAD\_VALUE - 0x61 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_LOAD_VALUE |
| Data[1]: | SLAVE_ID |
| Data[2]: | LOAD_VAL |
| Data[3]: | - |
| DLC: | 6 |

SET\_CHARGING- 0x65 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | SET_CHARGING |
| Data[1]: | CAN_MASTER_ID &#124;&#124; SLAVE_ID |
| Data[2]: | 1 (on) / 0 (off) |
| Data[3]: | - |
| DLC: | 6 |

CURRENT FLOW - 0x66 QUERY

| ID: | CAN_MASTER_ID |
| - | - |
| Data[0]: | CURRENT_FLOW |
| Data[1]: | CAN_MASTER_ID &#124;&#124; SLAVE_ID |
| Data[2]: | Current flow |
| Data[3]: | - |
| DLC: | 6 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_LOAD_VALUE |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | SET_CHARGING |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

ANSWER

| ID: | CAN_ID |
| - | - |
| Data[0]: | CURRENT_FLOW |
| Data[1]: | ACK |
| Data[2]: | - |
| Data[3]: | - |
| DLC: | 4 |

## Appendix G

## BMS Master Module

## G.1 dsPIC FST V1.3 Schematics

figure G.1 - dsPIC FST Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_081.png)

## G.2 BMS Master I/O Shield Schematics

figure G.2 - I/O Shield Schematics

![Image](FST%20Lisboa%20-%20BMS%20for%20Formula%20Student%20%28Guedes%20Thesis%29_files/img_082.png)

## Appendix H BMS Slave Modules Test

## H.1 Slave Modules Voltage and Resistance Measurments

| Board no. | CAN Id. | Vref @ 1.8V [V] | Vref @ 4.0V [V] | RL [Ω] | Vref (AVG) |
| - | - | - | - | - | - |
| 1 | 1 | 4.87 | 4.92 | 1.68 | 4.895 |
| 2 | 2 | 4.85 | 4.89 | 1.69 | 4.87 |
| 3 | 3 | 4.84 | 4.89 | 1.7 | 4.865 |
| 4 | 4 | 4.85 | 4.89 | 1.68 | 4.87 |
| 5 | 5 | 4.86 | 4.91 | 1.67 | 4.885 |
| 6 | 6 | 4.89 | 4.92 | 1.68 | 4.905 |
| 7 | 7 | 4.89 | 4.92 | 1.69 | 4.905 |
| 8 | 8 | 4.85 | 4.89 | 1.68 | 4.87 |
| 9 | 9 | 4.86 | 4.87 | 1.69 | 4.865 |
| 10 | 10 | 4.89 | 4.92 | 1.69 | 4.905 |
| 11 | 11 | 4.86 | 4.92 | 1.69 | 4.89 |
| 12 | 12 | 4.87 | 4.9 | 1.69 | 4.885 |
| 13 | 13 | 4.88 | 4.94 | 1.69 | 4.91 |
| 14 | 14 | 4.87 | 4.93 | 1.69 | 4.9 |
| 15 | 15 | 4.89 | 4.91 | 1.69 | 4.9 |
| 16 | 16 | 4.92 | 4.99 | 1.69 | 4.955 |
| 17 | 17 | 4.9 | 4.94 | 1.69 | 4.92 |
| 18 | 18 | 4.9 | 4.93 | 1.69 | 4.915 |
| 19 | 19 | 4.9 | 4.91 | 1.7 | 4.905 |
| 20 | 20 | 4.87 | 4.89 | 1.68 | 4.88 |
| 21 | 21 | 4.88 | 4.93 | 1.69 | 4.905 |
| 22 | 22 | 4.91 | 4.98 | 1.69 | 4.945 |
| 23 | 23 | 4.91 | 4.91 | 1.69 | 4.91 |
| 24 | 24 | 4.85 | 4.88 | 1.67 | 4.865 |
| 25 | 25 | 4.88 | 4.93 | 1.69 | 4.905 |
| 26 | 26 | 4.91 | 4.93 | 1.68 | 4.92 |
| 27 | 27 | 4.88 | 4.95 | 1.69 | 4.915 |
| 28 | 28 | 4.85 | 4.9 | 1.69 | 4.875 |
| 29 | 29 | 4.91 | 4.94 | 1.68 | 4.925 |
| 30 | 30 | 4.82 | 4.87 | 1.67 | 4.845 |
| 31 | 31 | 4.82 | 4.86 | 1.69 | 4.84 |
| 32 | 32 | 4.88 | 4.93 | 1.68 | 4.905 |
| 33 | 33 | 4.9 | 4.93 | 1.69 | 4.915 |
| 34 | 34 | 4.85 | 4.88 | 1.68 | 4.865 |
| 35 | 35 | 4.85 | 4.9 | 1.69 | 4.875 |
| 36 | 36 | 4.92 | 4.98 | 1.69 | 4.95 |
| 37 | 37 | 4.9 | 4.95 | 1.7 | 4.925 |
| 38 | 38 | 4.87 | 4.9 | 1.69 | 4.885 |

table H.1 - Slave modules voltage and resistance measurements

| 39 | 39 | 4.89 | 4.97 | 1.69 | 4.93 |
| - | - | - | - | - | - |
| 40 | 4.89 | 4.94 | 1.69 | 4.915 | 40 |
| 41 | 4.83 | 4.88 | 1.69 | 4.855 | 41 |
| 42 | 4.83 | 4.86 | 1.69 | 4.845 | 42 |
| 43 | 4.85 | 4.88 | 1.68 | 4.865 | 43 |
| 44 | 4.87 | 4.9 | 1.68 | 4.885 | 44 |
| 45 | 4.87 | 4.94 | 1.69 | 4.905 | 45 |
| 46 | 4.96 | 4.99 | 1.69 | 4.975 | 46 |
| 47 | 4.89 | 4.89 | 1.69 | 4.89 | 47 |
| 48 | 4.86 | 4.89 | 1.69 | 4.875 | 48 |
| 49 | 4.92 | 4.95 | 1.7 | 4.935 | 49 |
| 50 | 4.87 | 4.91 | 1.69 | 4.89 | 50 |
| 51 | 4.92 | 4.92 | 1.69 | 4.92 | 51 |
| 52 | 4.88 | 4.9 | 1.69 | 4.89 | 52 |
| 53 | 4.89 | 4.92 | 1.69 | 4.905 | 53 |
| 54 | 4.95 | 4.96 | 1.69 | 4.955 | 54 |
| 55 | 4.95 | 4.96 | 1.69 | 4.955 | 55 |
| 56 | 4.88 | 4.9 | 1.69 | 4.89 | 56 |
| 57 | 4.89 | 4.93 | 1.69 | 4.91 | 57 |
| 58 | 4.86 | 4.9 | 1.69 | 4.88 | 58 |
| 59 | 4.89 | 4.92 | 1.69 | 4.905 | 59 |
| 60 | 4.95 | 4.96 | 1.69 | 4.955 | 60 |
| 61 | 4.95 | 4.96 | 1.69 | 4.955 | 61 |
| 62 | 4.87 | 4.9 | 1.7 | 4.885 | 62 |
| 63 | 4.87 | 4.94 | 1.68 | 4.905 | 63 |
| 64 64 | 4.96 | 4.99 | 1.68 | 4.975 |  |
| 65 65 | 4.89 | 4.89 | 1.69 |  | 4.89 |

## Average values:

- Vref @ 1.8V = 4.88V
- Vref @ 4.0V = 4.92V
- Vref = 4.90V
- RL = 1.69Ω

H.2 Slave Modules Voltage and Temperature measurements validation

| Board no. | ID_CAN | Voltage @ 1.8V | Temp @ 1.8 | Voltage @ 4.0V | Temp @ 4.0 |
| - | - | - | - | - | - |
| 1 | 1 | 1.803 | 22.12 | 4.005 | 22.16 |
| 2 | 2 | 1.812 | 21.35 | 4.026 | 21.19 |
| 3 | 3 | 1.814 | 21.24 | 4.029 | 21.32 |
| 4 | 4 | 1.811 | 21.41 | 4.026 | 21.18 |
| 5 | 5 | 1.806 | 22.04 | 4.013 | 21.90 |
| 6 | 6 | 1.799 | 22.33 | 3.996 | 22.12 |
| 7 | 7 | 1.799 | 22.14 | 3.996 | 22.54 |
| 8 | 8 | 1.812 | 21.39 | 4.025 | 21.19 |
| 9 | 9 | 1.814 | 21.23 | 4.030 | 21.22 |
| 10 | 10 | 1.799 | 22.59 | 3.996 | 22.15 |
| 11 | 11 | 1.804 | 21.93 | 4.009 | 21.73 |
| 12 | 12 | 1.806 | 21.78 | 4.013 | 22.02 |
| 13 | 13 | 1.796 | 22.45 | 3.992 | 22.37 |
| 14 | 14 | 1.801 | 22.17 | 4.001 | 21.97 |
| 15 | 15 | 1.801 | 22.06 | 4.000 | 22.29 |
| 16 | 16 | 1.781 | 23.84 | 3.956 | 23.72 |
| 17 | 17 | 1.793 | 22.95 | 3.984 | 22.73 |
| 18 | 18 | 1.795 | 22.55 | 3.988 | 22.44 |
| 19 | 19 | 1.798 | 22.29 | 3.997 | 22.35 |
| 20 | 20 | 1.808 | 21.58 | 4.017 | 21.59 |
| 21 | 21 | 1.798 | 22.55 | 3.996 | 22.14 |
| 22 | 22 | 1.784 | 23.33 | 3.964 | 23.52 |
| 23 | 23 | 1.797 | 22.51 | 3.993 | 22.61 |
| 24 | 24 | 1.813 | 21.18 | 4.030 | 21.10 |
| 25 | 25 | 1.798 | 22.46 | 3.996 | 22.19 |
| 26 | 26 | 1.793 | 22.99 | 3.984 | 22.70 |
| 27 | 27 | 1.795 | 22.45 | 3.989 | 22.63 |
| 28 | 28 | 1.809 | 21.56 | 4.021 | 21.28 |
| 29 | 29 | 1.791 | 22.97 | 3.980 | 22.81 |
| 30 | 30 | 1.821 | 20.57 | 4.046 | 20.72 |
| 31 | 31 | 1.823 | 20.68 | 4.050 | 20.69 |
| 32 | 32 | 1.799 | 22.60 | 3.997 | 22.58 |
| 33 | 33 | 1.795 | 22.48 | 3.988 | 22.56 |
| 34 | 34 | 1.814 | 21.36 | 4.029 | 21.14 |
| 35 | 35 | 1.810 | 21.76 | 4.021 | 21.35 |
| 36 | 36 | 1.782 | 23.45 | 3.960 | 23.55 |
| 37 | 37 | 1.791 | 22.66 | 3.980 | 22.75 |
| 38 | 38 | 1.806 | 21.55 | 4.013 | 21.78 |
| 39 | 39 | 1.790 | 22.99 | 3.976 | 22.82 |
| 40 | 40 | 1.795 | 22.46 | 3.988 | 22.81 |
| 41 | 41 | 1.817 | 20.87 | 4.037 | 20.98 |
| 42 | 42 | 1.821 | 20.53 | 4.046 | 20.70 |

table H.2 - Slave Modules Voltage and Temperature measurements validation

| 43 | 43 | 1.813 | 21.32 | 4.029 | 21.14 |
| - | - | - | - | - | - |
| 44 | 1.806 | 21.86 | 4.013 | 21.58 | 44 |
| 45 | 1.798 | 22.32 | 3.996 | 22.49 | 45 |
| 46 | 1.773 | 24.25 | 3.940 | 24.37 | 46 |
| 47 | 1.804 | 21.75 | 4.008 | 22.07 | 47 |
| 48 | 1.809 | 21.49 | 4.021 | 21.27 | 48 |
| 49 | 1.787 | 23.26 | 3.972 | 23.29 | 49 |
| 50 | 1.804 | 21.87 | 4.009 | 22.12 | 50 |
| 51 | 1.793 | 22.97 | 3.984 | 22.65 | 51 |
| 52 | 1.804 | 21.78 | 4.008 | 22.02 | 52 |
| 53 | 1.799 | 22.58 | 3.997 | 22.41 | 53 |
| 54 | 1.780 | 23.84 | 3.956 | 23.52 | 54 |
| 55 | 1.780 | 23.91 | 3.957 | 23.63 | 55 |
| 56 | 1.804 | 21.94 | 4.009 | 22.17 | 56 |
| 57 | 1.797 | 22.27 | 3.992 | 22.28 | 57 |
| 58 | 1.808 | 21.54 | 4.017 | 21.82 | 58 |
| 59 | 1.798 | 22.12 | 3.997 | 22.27 | 59 |
| 60 | 1.780 | 23.56 | 3.956 | 23.48 | 60 |
| 61 | 1.781 | 23.49 | 3.956 | 23.61 | 61 |
| 62 | 1.806 | 21.92 | 4.013 | 21.89 | 62 |
| 63 | 1.799 | 22.12 | 3.996 | 22.29 | 63 |
| 64 | 1.773 | 24.11 | 3.940 | 24.48 | 64 |
| 65 | 1.805 | 21.84 | 4.008 | 21.98 | 65 |

## Maximum deviations:

- dV@1.8V=0.027V
- dV@4.0V=0.05V
- dT@1.8V=2.25ºC
- dT@4.0V=2.48ºC
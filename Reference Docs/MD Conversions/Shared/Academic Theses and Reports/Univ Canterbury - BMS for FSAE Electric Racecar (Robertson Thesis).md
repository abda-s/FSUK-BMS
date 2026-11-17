<!-- Converted from Univ Canterbury - BMS for FSAE Electric Racecar (Robertson Thesis).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

## [University of Canterbury](https://www.canterbury.ac.nz/)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_001.png)

## Master's Thesis

## Design and Development of a Battery Management System for a Formula-SAE Electric Racecar

Author:

Ben Robertson

Supervisor:

Paul Gaynor

A thesis submitted in fulfillment of the requirements for the degree of Master's of Engineering

in the

Department of Electrical and Computer Engineering

"To finish first, you must first finish."

## Abstract

University of Canterbury Motorsport (UCM) is a student run club from Christchurch, New Zealand that designs and builds race cars to compete in the international FormulaSAE competition. In 2023, University of Canterbury Motorsport won the Formula SAE Australasia competition with a car that departed significantly from the team's previous vehicle designs.

Since 2016, University of Canterbury Motorsport has built EVs, with incremental improvements each year. The 2023 car, named UCM23, featured the team's first custom designed Battery Management System (BMS), a critical sub-system in the car's high voltage battery pack.

The author was responsible for overall technical direction of the UCM23 programme and developed a completely new BMS for the car. This BMS was designed to comply with Formula SAE rules to ensure the safe operation of the car. In addition, features to strategically manage the vehicle's efficiency and improve ease of operation were developed.

UCM23's battery pack is constructed from Sony/Murata VTC5A cells, of a cylindrical 18650 form factor. These cells are assembled to form UCM23's battery pack, in a 96s5p configuration. This pack is 403V at full charge, with 4.5kWh of energy storage.

UCM23's battery pack is monitored by eight BMS modules, that report via a CAN bus to a control unit. Each BMS module manages 12 series connected cells. These modules are designed around the LTC6811 Battery Management IC (BMIC), providing the analogue front end. The voltage of each series connection and the temperature of the respective cells is measured by the BMS. These measurements provide immediate information on the health of each cell, and are used to trigger a shutdown of the car if a voltage or temperature exceeds hard operating limits. Over time, these measurements are used to determine the overall State of Health (SoH) and State of Charge (SoC) of the battery pack.

Development of UCM23's BMS was divided into two phases, prior to and following the 2023 Formula-SAE Australasia competition. Prior to the competition, development was aimed at establishing reliability of the essential functionality required by the competition rules. Following the competition, a significant portion of the system's software was rewritten, learning from the initial implementation, and aimed to ease implementation of more advanced algorithms. During this latter phase, a SoH algorithm was developed and more advanced SoC algorithms were implemented.

Testing prior to the competition yielded positive results. Calibrated cell voltage measurements recorded by the BMS exhibited no more than 1mV deviation from manual measurements. Calibrated BMS temperature measurements matched manual measurements recorded while charging the battery pack and deviated by less than a degree over a 15 degree temperature rise. Critical functionality required by the competition rules was proven at this stage, including all fault conditions that shutdown the car. During the competition the system performed as expected, with all measurements from the BMS reporting to the car's Vehicle Control Unit (VCU), and charging functionality enabling charging to occur between events. This allowed the team to confidently focus on standard operation of the car.

Following the competition, development of new software algorithms yielded a range of results. A Coulomb counting method for SoC estimation proved to reliably indicate the SoC under driving conditions. The initial implementation of an Equivalent Circuit Model (ECM) SoC estimation technique failed to accurately identify the internal resistance of the battery pack's cells under driving conditions. However, it was concluded that identification of internal resistance under driving conditions was not necessary, and assuming a constant internal resistance resulted in the ECM SoC method producing an estimate that closely followed one produced by the Coulomb counting method, with a maximum and mean difference between them of 5.3% and 2.1% respectively.

The BMS developed in this thesis is now being utilised by the 2024 UCM team. It has been adapted to work with a different battery pack configuration without significant difficulty, showing the versatility of the design and its suitability to the Formula-SAE application.

## Acknowledgements

Thank you to my supervisor Associate Professor Dr Paul Gaynor. Your unwavering support and enthusiasm for UCM over many years has been amazing, and your insights into this project have proved extremely valuable.

To all the staff at the University of Canterbury that have helped our team over the last ten years, thank you for your continued support and guidance.

Deep gratitude goes to everyone in University of Canterbury Motorsport for your dedication and passion. Without you all, UCM23 would not have seen the success it did. I am confident that working with you will be a forever lasting highlight of my career. Despite the the occasional blunder along the way, we produced an incredible car that caught the eyes of everyone around it. Special thanks goes to Clark for your persistence and dedication.

Thanks to all the UCM alumni for setting the bar high, allowing us to reach UCM's 10th year in triumph. Special mention to the 21 and 35 teams for being great friends coming into UCM.

Thanks Dad!

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_002.png)

2023 University of Canterbury Motorsport team at Calder Park, Melbourne.

## Table of Contents

| Abstract . | . . | . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . ii |
| - | - | - | - |
| Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . | Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . | Acknowledgements . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . iv |
| Table of Contents . . . . . . . . . . . . . . . . . . . . . . . . | Table of Contents . . . . . . . . . . . . . . . . . . . . . . . . | Table of Contents . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . viii |
| List of Figures . . . . . . . . . . . . . . . . . . . . . . . . . . | List of Figures . . . . . . . . . . . . . . . . . . . . . . . . . . | List of Figures . . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . xii |
| List of Tables . . . . . . . . . . . . . . . . . . . . . . . . | List of Tables . . . . . . . . . . . . . . . . . . . . . . . . | List of Tables . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . xiii |
| Glossary of Terms . . . . . . . . . . . . . . . . . . | Glossary of Terms . . . . . . . . . . . . . . . . . . | . . . | . . . . . . . . . . . . . xvi |
| 1 Introduction | 1 Introduction | 1 Introduction | 1 |
| 1.1 |  | Formula-SAE/Formula Student . . . . . . . . . . | . . . . . . . . . . . . . 1 |
|  | 1.2 | University of Canterbury Motorsport . . . . . . . | . . . . . . . . . . . . . 3 |
|  | 1.3 | UCM23 . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 4 |
|  | 1.3.1 | Project Motivation . . . . . . . . . . . . . | . . . . . . . . . . . . . 4 |
|  | 1.3.2 | Design Philosophy and Vehicle Concept . . | . . . . . . . . . . . . . 5 |
|  | 1.4 | Thesis Overview . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 6 |
| 2 | Background Electric Vehicle | Tractive |  |
|  |  |  | 7 |
| 2.1 | 2.1.1 | System . . . . . . . . Motors . . . . . . . . . . . . . . . . . . . . | 7 . . . . . . . . . . . . . 7 |
|  | 2.1.2 | Motor Controllers . . . . . . . . . . . . . . | . . . . . . . . . . . . . 8 |
|  | 2.1.3 | Battery Packs | 8 |
| 2.2 |  | . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . |
|  | 2.2.1 | Lithium-ion Cells . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 9 9 |
|  | 2.2.2 Physical | Electrochemistry . . . . . . . . . . . . . . Construction . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . 10 |
|  | 2.2.3 | Safety . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 10 |
|  | 2.2.4 | Nominal Operation . . . . . . . . . . . . . | . . . . . . . . . . . . . 11 |
|  | 2.2.5 | Necessity of a Battery Management System | . . . . . . . . . . . . 12 |
| 2.3 | BMS | Theory . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 13 |
|  | 2.3.1 | Centralised Architecture . . . . . . . . . . | . . . . . . . . . . . . . 14 |
|  | 2.3.2 | Distributed Architecture . . . . . . . . . . | . . . . . . . . . . . . . 15 |
|  | 2.3.3 | Modular/Hybrid Architecture . . . . . . . | . . . . . . . . . . . . . 16 |
|  | 2.3.4 | Cell Balancing Methods . . . . . . . . . . | . . . . . . . . . . . . . 17 |
| 2.4 | FSAE | Vehicle Theory . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 17 |
|  | 2.4.1 | Inverter | 18 |
|  | Shutdown 2.4.2 | Circuit . . . . . . . . . . . . . . | . . . . . . . . . . . . . 17 |
| 2.5 |  | Precharge & Discharge . . . . . . | . . . . . . . . . . . . . |
|  | CAN | . . . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 19 20 |
|  | 2.5.1 CAN 2.5.2 | Frames . . . . . . . . . . . . . . . . Arbitration . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . . . . . . . . . 20 |

| 2.6 UCM23 Accumulator Design . . . . . . . . . . . . . . . . | 2.6 UCM23 Accumulator Design . . . . . . . . . . . . . . . . |
| - | - |
| 2.6.1 | . . . Cell Configuration . . . . . . . . . . . . . . . . . . . . . . . . . . 21 |
| 2.6.2 . . . | Packaging . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22 |
| System Concept | Design 24 |
| 3.1 AMS . | Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24 |
| 3.1.1 | Minimum Viable Product . . . . . . . . . . . . . . . . . . . . . . 24 |
| 3.1.2 | Stretch Goal Features . . . . . . . . . . . . . . . . . . . . . . . . . 25 |
| 3.2 Selection | of Architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 |
| 3.2.1 | Selection Criteria . . . . . . . . . . . . . . . . . . . . . . . . . . . 26 |
| 3.2.2 | Applying Selection Criteria . . . . . . . . . . . . . . . . . . . . . 27 |
| 3.2.3 | Resulting Considerations for Modular Architecture . . . . . . . . 29 |
| 3.3 Vehicle . | Integration . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31 |
| 3.3.1 | AMS Master and IO . . . . . . . . . . . . . . . . . . . . . . . . . 31 |
| 3.3.2 | Current Sensor . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 |
| 3.3.3 . . | Fault Latch . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32 |
| 3.3.4 | Charging Interface . . . 33 |
|  | . . . . . . . . . . . . . . . . . . . . . . . |
| 3.4 Summary | of System Design . . . . . . . . . . . . . . . . . . . . . . . . . 33 |
| Hardware | Design 35 |
| 4.1 Design Tools and Workflows | . . . . . . . . . . . . . . . . . . . . . . . . . 35 |
| 4.2 AMS | Module Electronics Unit . . . . . . . . . . . . . . . . . . . . . . . . 36 |
| 4.2.1 | Requirements . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36 |
| 4.2.2 | Block Diagram of AMS Module . . . . . . . . . . . . . . . . . . . 36 |
| 4.2.3 | Battery Management IC . . . . . . . . . . . . . . . . . . . . . . . 37 |
| 4.2.4 | Micro-controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38 |
| 4.2.5 | Temperature Monitoring . . . . . . . . . . . . . . . . . . . . . . . 39 |
| 4.2.6 . | Power Supply . . . . . . . . . . . . . . . . . . . . . . . . . . . . 41 |
| 4.2.7 . | Isolated CAN . . . . . . . . . . . . . . . . . . . . . . . . . . . . 42 |
| 4.2.8 . | PCB Layout . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44 |
| 4.3 Cell . | Carrier Unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44 |
| 4.3.1 | Passive Discharge Circuit . . . . . . . . . . . . . . . . . . . . . . 45 |
| 4.4 Accumulator Motherboard | . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 |
| 4.4.1 | Secondary CAN Controller . . . . . . . . . . . . . . . . . . . . . . 49 |
| 4.5 Accumulator | IO Isolation . . . . . . . . . . . . . . . . . . . . . . . . . . . 49 |
| 4.5.1 | Power Isolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 |
| 4.5.2 4.5.3 Fault Flag Isolation Software Development | CAN Isolation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50 . . . . . . . . . . . . . . . . . . . . |

| 5.1 | Firmware Development for ESP32 . . . . | . . . . . . . . . . . . . . . . . . 51 |
| - | - | - |
| 5.2 | System Level Implementation . . . . . . | . . . . . . . . . . . . . . . . . . 51 |
|  | 5.2.1 AMS CAN bus . . . . . . . . . . Prototyping and Assembly | . . . . . . . . . . . . . . . . . . 53 |
| 5.3 | 5.2.2 Vehicle CAN bus . . . . . . . . . | . . . . . . . . . . . . . . . . . . 56 |
|  | Executive Functions . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 57 |
|  | 5.3.1 Common . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 57 |
|  | 5.3.2 Modules . . . . . . . . . . . . . . Motherboard . | . . . . . . . . . . . . . . . . . . 58 |
|  | 5.3.3 . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 58 |
| 5.4 | Algorithms . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 59 |
|  | 5.4.1 Charge . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 59 |
|  | 5.4.2 Balancing . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 61 |
|  | 5.4.3 State of Charge Estimation . . . | . . . . . . . . . . . . . . . . . . 63 |
|  | 5.4.4 Temperature Monitoring . . . . . | . . . . . . . . . . . . . . . . . . 64 |
|  | 5.4.5 Fault Detection . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 65 |
| 5.5 | User Interface . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 66 |
|  | 5.5.1 Layout . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 67 |
|  | Preliminary Work | 68 |
| 6 6.1 | . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 68 |
| 6.2 | First Module Prototype . . . . . . . . . | . . . . . . . . . . . . . . . . . . 69 |
|  | 6.2.1 Software Development Process . . | . . . . . . . . . . . . . . . . . . 70 |
|  | 6.2.2 Design Flaws and Corrections . . | . . . . . . . . . . . . . . . . . . 71 |
| 6.3 | Motherboard and IO PCBs . . . . . . . | . . . . . . . . . . . . . . . . . . 72 |
|  | 6.3.1 Design Flaws and Corrections . . | . . . . . . . . . . . . . . . . . . 72 |
|  | 6.3.2 Software Development . . . . . . | . . . . . . . . . . . . . . . . . . 73 |
| 6.4 | Assembly . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 73 |
|  | 6.4.1 AMS Module PCBs . . . . . . . . | . . . . . . . . . . . . . . . . . . 73 |
|  | 6.4.2 Accumulator Segments . . . . . . Accumulator | . . . . . . . . . . . . . . . . . . 74 Motherboard |
|  | 6.4.3 Observation Deck with | . . . . . . . . . 75 |
| 7 | Pre-Competition Results | 76 |
| 7.1 7.2 7.3 7.4 8 | Measurements . . . . . . . . . . . . . . . Fault Detection . . . . . . . . . . . . . . Communications . . . . . . . . . . . . . Cell Balancing . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . . . . . 76 . . . . . . . . . . . . . . . . . . 77 . . . . . . . . . . . . . . . . . . 79 . . . . . . . . . . . . . . . . . . |
|  |  | 80 |
| 7.5 | Charging . . . . . . . . . . . . . . . . . . | 79 . . . . . . . . . . . . . . . . . . |
|  | Post-Competition Development | 82 |
| 8.1 | Module Power Efficiency . . . . . . . . . | . . . . . . . . . . . . . . . . . . 82 |
|  | 8.1.1 Investigation of avenues | 83 |
|  | for development | . . . . . . . . . . . . . . |

|  | 8.1.2 | Changes Implemented . . . . . . . . . . . . . | . . . . . . . . . . . 86 |
| - | - | - | - |
| 8.2 | State of Charge Estimation | . . . . . . . . . . . . . . | . . . . . . . . . . . 87 |
|  | 8.2.1 | Shortcomings of Open Circuit Voltage method | . . . . . . . . . . . 87 |
|  | 8.2.2 | Equivalent Circuit Model . . . . . . . . . . . . | . . . . . . . . . . . 87 |
|  | 8.2.3 | Coulomb Counting and State of Health Estimation | . . . . . . . . 94 |
| 8.3 | End of | Discharge Derating . . . . . . . . . . . . . . . | . . . . . . . . . . . 101 |
|  | 8.3.1 | End of Discharge Derating Results . . . . . . | . . . . . . . . . . . 103 |
| 8.4 | Range | Estimation . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . 104 |
|  | 8.4.1 | Calculating energy consumption rate . . . . . | . . . . . . . . . . . 105 |
|  | 8.4.2 | Forward projection . . . . . . . . . . . . . . . | . . . . . . . . . . . 105 |
|  | 8.4.3 | Range Estimation Results . . . . . . . . . . . | . . . . . . . . . . . 106 |
| 8.5 | Software Implementation . | . . . . . . . . . . . . . . . | . . . . . . . . . . . 106 |
|  | 8.5.1 | OTA Firmware Upload . . . . . . . . . . . . . | . . . . . . . . . . . 106 |
|  | 8.5.2 | Migrating to an RTOS . . . . . . . . . . . . . | . . . . . . . . . . . 107 |
|  | 8.5.3 | Design . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . 108 |
|  | 8.5.4 | Diagnostic Logging . . . . . . . . . . . . . . . | . . . . . . . . . . . 109 |
| 9 Conclusions | 9 Conclusions | 9 Conclusions | 110 |
| 9.1 | Review of Architecture . | . . . . . . . . . . . . . . . . | . . . . . . . . . . . 110 |
| 9.2 | Review of Hardware | . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . 111 |
| 9.3 | Review of Algorithms . | . . . . . . . . . . . . . . . . . | . . . . . . . . . . . 111 |
| 9.4 | Recommendations . . | . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . 111 |
| Appendix A FSAE AMS Rules | Appendix A FSAE AMS Rules | Appendix A FSAE AMS Rules | 113 |
| Appendix B AMS Module Schematics | Appendix B AMS Module Schematics | Appendix B AMS Module Schematics | 116 |
| Appendix C Motherboard Schematic | Appendix C Motherboard Schematic | Appendix C Motherboard Schematic | 120 |
| Appendix D Accumulator IO Schematic | Appendix D Accumulator IO Schematic | Appendix D Accumulator IO Schematic | 121 |
| Appendix E UCM23 FSAE Australasia 2023 | Appendix E UCM23 FSAE Australasia 2023 | Appendix E UCM23 FSAE Australasia 2023 | 122 |
| Appendix F General Recommendations For FSAE Teams | Appendix F General Recommendations For FSAE Teams | Appendix F General Recommendations For FSAE Teams | 126 |
| References | References | References | 128 |

## List of Figures

| 1.1 | UCM FSAE cars built since founding . . . . . . . . . . . . . . . . . . . . | 3 |
| - | - | - |
| 1.2 | UCM23 being setup for an autocross practice session. . . . . . . . . . . . | 4 |
| 2.1 | Diagram of UCM23's Tractive System . . . . . . . . . . . . . . . . . . . . | 7 |
| 2.2 | AMK DD5-14-10-POW Motors used by UCM23. . . . . . . . . . . . . . . | 7 |
| 2.3 | Illustration of common Li-ion cell form factors [19]. . . . . . . . . . . . . | 10 |
| 2.4 | Discharge curve for Sony VTC5A cells used in UCM23 [22]. . . . . . . . | 11 |
| 2.5 | Diagram depicting the limited usable capacity of poorly balanced cells [26]. | 12 |
| 2.6 | Diagram of centralised BMS architecture. . . . . . . . . . . . . . . . . . . | 14 |
| 2.7 | Diagram of distributed BMS architecture. . . . . . . . . . . . . . . . . . | 15 |
| 2.8 | Diagram of modular BMS architecture. . . . . . . . . . . . . . . . . . . . | 16 |
| 2.9 | Diagram of precharge and discharge system. . . . . . . . . . . . . . . . . | 18 |
| 2.10 | Diagram showing the relationship between CAN hardware, ISO 11898, and the layers of the OSI model [36]. . . . . . . . . . . . . . . . . . . . . . . . | 19 |
| 2.11 | Enepaq "blocks" product picture [22]. . . . . . . . . . . . . . . . . . . . . | 21 |
| 2.12 | Exploded diagram of UCM23's accumulator. . . . . . . . . . . . . . . . . | 22 |
| 2.13 | Illustration of a UCM23 accumulator segment. . . . . . . . . . . . . . . . | 23 |
| 2.14 | Illustration of UCM23's accumulator "observation deck" . . . . . . . . . . | 23 |
| 3.1 | Diagram of AMS hardware concept . . . . . . . . . . . . . . . . . . . . . | 33 |
| 4.1 | Block diagram of AMS module electronics unit. . . . . . . . . . . . . . . | 37 |
| 4.2 | Comparison of ESP32 packages. . . . . . . . . . . . . . . . . . . . . . . . | 38 |
| 4.3 | Portion of the Espressif ESP32 DevKit Schematic showing the automatic bootloader circuit [44]. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 39 |
| 4.4 | Enepaq's example test circuit for reading a temperature sensor [22]. . . . | 40 |
| 4.5 | Block diagram of AMS module power supply circuit. . . . . . . . . . . . | 41 |
| 4.6 | TI WEBENCH's buck converter circuit reference design for the AMS mod- ule PCB. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 42 |
| 4.7 | TJA1052i Block diagram form manufacturer data sheet [48]. . . . . . . . | 43 |
| 4.8 | Section of the AMS module schematic showing the isolated CAN transceiver. | 43 |
| 4.9 | AMS module PCB layout. . . . . . . . . . . . . . . . . . . . . . . . . . . | 44 |
| 4.10 | Passive balancing current bypass portion of cell carrier PCB schematic. . | 45 |
| 4.11 | Cell carrier PCB layout and 3D model. . . . . . . . . . . . . . . . . . . . | 47 |
| 4.12 4.13 | Block diagram of Accumulator Motherboard PCB. . . . . . . . . . . . . . Portion of Accumulator Motherboard schematic showing the standalone SPI CAN controller . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 48 49 |

| 4.14 | Render of the Accumulator Motherboard and Accumulator IO Isolation PCB. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 49 |
| - | - | - |
| 5.1 | Diagram of AMS data structures relating to the AMS CAN bus. . . . . . | 52 |
| 5.2 | Diagram of motherboard data structures relating to the vehicle CAN bus. | 52 |
| 5.3 | Diagram of AMS module firmware functions. . . . . . . . . . . . . . . . . | 53 |
| 5.4 | Diagram of AMS motherboard functions. . . . . . . . . . . . . . . . . . . | 53 |
| 5.5 | AMS CAN network layer diagram. . . . . . . . . . . . . . . . . . . . . . | 55 |
| 5.6 | Qualitative example of current and voltage over time during CC-CV charging. | 60 |
| 5.7 | Charging algorithm, logic flow diagram. . . . . . . . . . . . . . . . . . . . | 61 |
| 5.8 | Balancing algorithm controller segment, logic flow diagram. . . . . . . . . | 62 |
| 5.9 | Balancing algorithm functional segment, logic flow diagram. . . . . . . . | 62 |
| 5.10 | Discharge characteristic curve for 1x5P Enepaq VTC5A at 5C [22]. . . . | 63 |
| 5.11 | Piece-wise transfer function approximating Enepaq's 1C discharge charac- teristic curve. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 64 |
| 5.12 | Approximate linear transfer function from ADC values to temperature values, and Enepaq provided LUT values [22]. . . . . . . . . . . . . . . . | 64 |
| 5.13 | AMS User Interface version 1 layout. . . . . . . . . . . . . . . . . . . . . | 67 |
| 6.1 | CAD screenshots taken during accumulator packaging design process. (a) Near final segment design. (b) Final segment design inside accumulator container concept model with excess space for observation deck. . . . . . | 68 |
| 6.2 | Photos of mock-up cell carrier and observation deck. (a) 3D printed proto- type of a cell carrier unit and Enepaq cell blocks. (b) Pathfinder prototype observation deck sub-assembly. . . . . . . . . . . . . . . . . . . . . . . . . | 68 |
| 6.3 | Photos of accumulator mock-ups. (a) First accumulator mock-up, prior to observation deck design. (b) Final accumulator mock-up with observation deck size finalised. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 69 |
| 6.4 | AMS Module prototype at various stages in prototype testing. (a) One cell block connected. (b) Displaying data over the UI, with 4 spare cell blocks. (c) 12 spare cell blocks connected and with full shrouding, while reporting to the UI. (d) Full prototype module with shrouding and lid attached for the adjacent module. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 69 |
| 6.5 | First prototype of accumulator motherboard and accumulator IO PCBs. . | 72 |
| 6.6 | All eight final AMS module PCBs. . . . . . . . . . . . . . . . . . . . . . | 73 |
| 6.7 | A UCM23 accumulator module (half a segment) being assembled. . . . . | 74 |
| 6.8 | All UCM23 accumulator segments fully assembled. . . . . . . . . . . . . | 75 |
| 6.9 | UCM23 accumulator's observation deck fully assembled. . . . . . . . . . | 75 |

| 7.1 | Plot of AMS measured temperature and Thermocouple probe measured temperature, while charging UCM23's accumulator. . . . . . . . . . . . . | 76 |
| - | - | - |
| 7.2 | Plots showing data recorded with UCM23 while tripping an AMS over- temperature fault. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 77 |
| 7.3 | Plots showing data recorded with UCM23 while tripping an AMS under- voltage fault. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| 7.4 | AMS fault light visible in the cockpit of UCM23 during testing of the AMS fault detection system. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 78 |
| 7.5 | Logged AMS CAN lost message counter of 20 minutes of driving. . . . . | 79 |
| 7.6 | Comparison of measured voltage imbalance over 20 charge cycles with cell balancing enabled and disabled on a prototype AMS module. . . . . . . . | 79 |
| 7.7 | Comparison of minimum and maximum cell voltages in an AMS module prototype, testing cell balancing functionality. . . . . . . . . . . . . . . . | 80 |
| 7.8 | Plot of voltage and current while charging UCM23's accumulator. . . . . | 81 |
| 8.1 | Apparent lower voltage at 12th cell of the AMS module first prototype. . | 82 |
| 8.2 | Measurements to determine buck converter efficiency prior to attempted improvements of standby time. . . . . . . . . . . . . . . . . . . . . . . . . | 83 |
| 8.3 | LMR16006 efficiency plot from its datasheet [55]. . . . . . . . . . . . . . | 84 |
| 8.4 | Lithium-ion cell Equivalent Circuit Model (ECM) from literature [27]. . . | 88 |
| 8.5 | Simplified lithium-ion equivalent circuit model considered for UCM AMS. | 88 |
| 8.6 | Logic diagram of Equivalent Circuit Model (ECM) based State of Charge (SoC) estimation. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 89 |
| 8.7 | Current profile for the proof of concept test of the Equivalent Circuit Model (ECM) State of Charge (SoC) estimation algorithm. . . . . . . . . . . . . | 90 |
| 8.8 | Output of the linear regression Equivalent Circuit Model (ECM) proof of concept test. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 90 |
| 8.9 | Equivalent Circuit Model IR identified via LLS plotted against Coulomb Counting SoC while charging UCM23's accumulator. . . . . . . . . . . . | 91 |
| 8.10 | Plots of internal resistance identification with LLS regression, typical for charging and driving conditions. . . . . . . . . . . . . . . . . . . . . . . . | 91 |
| 8.11 | Plots showing a 100s long filter applied to voltage and current values to estimate internal resistance during driving conditions. . . . . . . . . . . . | 92 |
| 8.12 | Plot of Equivalent Circuit Model (ECM) based State of Charge (SoC) estimation, logged while driving UCM23. . . . . . . . . . . . . . . . . . . | 93 |
| 8.13 | Logic diagram for Qmax determination during charging. . . . . . . . . . . | 95 |
| 8.14 | Output of the linear regression Qmax proof of concept test. . . . . . . . . | 96 |
| 8.15 | Diagram of the iterative Coulomb counting algorithm, utilising an esti- mated Qmax. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 97 |

| 8.16 | Plot showing Coulomb Counting ∆Q and accumulator current output. . . | 97 |
| - | - | - |
| 8.17 | Plot showing Coulomb Counting based SoC estimate in relation to "open circuit" voltage based SoC. . . . . . . . . . . . . . . . . . . . . . . . . . . | 98 |
| 8.18 | Plotted output of the Qmax algorithm during charging of UCM23's accu- mulator. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 98 |
| 8.19 | Plot of the Qmax estimation algorithm, recorded during charging, showing the impact of insufficient internal resistance estimates. . . . . . . . . . . | 99 |
| 8.20 | Plotted output of the Qmax algorithm during charging of UCM23's accu- mulator after fixing ECM SoC estimation. . . . . . . . . . . . . . . . . . | 100 |
| 8.21 | Plotted output of the Qmax algorithm counting only start and end points under open circuit conditions. . . . . . . . . . . . . . . . . . . . . . . . . | 100 |
| 8.22 | Plots showing the determination of the current limit to prevent voltage sag below the cutoff voltage, recorded UCM23's VCU while driving. . . . . . | 103 |
| 8.23 | Plots showing the operation of current limiting as part of the end of dis- charge de-rating system, recorded by UCM23's VCU while driving. . . . | 104 |
| 8.24 | Plot showing range estimated in relation to distance driven. . . . . . . . | 106 |
| 8.25 | Final AMS User Interface (UI) displaying the output of improved SoC estimation algorithms. . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 109 |
| 9.1 | Values reported by the AMS, displayed on UCM23's dash during final testing before the competition. . . . . . . . . . . . . . . . . . . . . . . . . | 110 |
| E.1 | Photos from the final test sessions in Melbourne. . . . . . . . . . . . . . . | 122 |
| E.2 | Photos from milestones in UCM23's tech inspection process at FSAE. . . | 122 |
| E.3 | Photos of UCM23 competing in the skid-pad event. . . . . . . . . . . . . | 123 |
| E.4 | UCM23 in line for the acceleration event. . . . . . . . . . . . . . . . . . . | 123 |
| E.5 | UCM23's accumulator on its transport kart "the stance kart". . . . . . . . | 123 |
| E.6 | UCM23 and a jubilant team after completing the endurance event, ending the 2023 FSAE Australasia competition. . . . . . . . . . . . . . . . . . . | 125 |
| F.1 | UCM23 pictured at UCM's test site, during a test session validating im- proved AMS algorithms. . . . . . . . . . . . . . . . . . . . . . . . . . . . | 127 |

## List of Tables

| 1.1 | FSAE Points Structure . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 1 |
| - | - | - |
| 2.1 | Standard CAN frame bit format. . . . . . . . . . . . . . . . . . . . . . . | 20 |
| 3.1 | Decision matrix for selection of AMS architecture . . . . . . . . . . . . . | 27 |
| 4.1 | Candidate micro-controller families for the AMS module design. . . . . . | 38 |
| 5.1 | Example of cell voltage CAN frames from AMS modules. . . . . . . . . . | 55 |
| 5.2 | Polling CAN frame to AMS modules. . . . . . . . . . . . . . . . . . . . . | 56 |
| 5.3 | Accumulator data CAN frame to AMS modules. . . . . . . . . . . . . . . | 56 |
| 5.4 | Accumulator status CAN frame to vehicle. . . . . . . . . . . . . . . . . . | 57 |
| 5.5 | Format of status word in accumulator's CAN frame to the vehicle. . . . . | 57 |
| 5.6 | Accumulator command CAN frame from vehicle or charge controller to accumulator. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 57 |
| 7.1 | Comparison of cell voltage measurements with prototype AMS module and a high precision multimeter at low SoC. . . . . . . . . . . . . . . . . . . . | 76 |
| 8.1 | AMS module power consumption and buck converter efficiency in various configurations. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 85 |

## Glossary of Terms

AC Alternating Current.

Accumulator The battery pack in an F-SAE car.

ADC Analogue to Digital Converter.

AIR Accumulator Isolation Relay.

AMS Accumulator Management System.

BMIC Battery Management IC.

BMS Battery Management System.

BoM Bill of Materials.

BSPD Brake System Plausibility Device.

CAN Controller Area Network.

CC-CV Constant Current-Constant Voltage.

COTS Commercial Off The Shelf.

DC Direct Current.

ECM Equivalent Circuit Model.

EDA Electronic Design Automation.

EMI Electromagnetic Interference.

ESR Equivalent Series Resistance.

EV Electric Vehicle.

FET Field Effect Transistor.

FSAE Formula-SAE.

FYP Final Year Project.

GLV Grounded Low Voltage.

HV High Voltage.

HVIL High Voltage Interlock.

I2C Inter-Integrated Circuit.

IC Integrated Circuit.

ICE Internal Combustion Engine.

IDE Integrated Development Environment.

IMD Insulation Monitoring Device.

IO Input/Output.

IR Internal Resistance.

LLS Linear Least Squares.

LV Low Voltage.

MAC Medium Access Control.

MCU Micro-Controller Unit.

MVP Minimum Viable Product.

OCV Open Circuit Voltage.

OEM Original Equipment Manufacturer.

OTA Over the Air.

PCB Printed Circuit Board.

PDOC Precharge &amp; Discharge Over Current.

PMSM Permanent Magnet Synchronous Motors.

RTOS Real Time Operating System.

RX Receive.

SAE Society of Automotive Engineers.

SoC State of Charge.

SoH State of Health.

SPI Serial Peripheral Interface.

SPIFFS SPI Flash File System.

TS Tractive System.

TX Transmit.

UART Universal Asynchronous Receiver-Transmitter.

UCM University of Canterbury Motorsport.

UI User Interface.

VCU Vehicle Control Unit.

## Chapter 1: Introduction

## 1.1 Formula-SAE/Formula Student

FSAE is an international competition administered by SAE (Society of Automotive Engineers) International. The competition is renowned for providing a unique learning experience for tertiary students to develop, technical, management, financial and marketing skills relevant to a professional engineering environment.

With its inaugural competition held in the United States in 1981 with four teams competing, FSAE now sees over 800 teams in the combined EV &amp; ICE world rankings [1]. FSAE runs in multiple competitions each year, organised by respective SAE regional chapters.

The premise of FSAE is for students to form a team acting as a company building a prototype open wheel car with intent to enter serial production to distribute to a briefed target market. The competition is points based, comprised of dynamic and static events. Dynamic events aim to test the real-world holistic performance of the vehicle. Static events test the team as an organisation to match the premise of the competition; quality of engineering workflows, programme management, handling of product data for manufacturing, cost effectiveness, and business strategy. The FSAE points structure is given in Table 1.1.

Table 1.1: FSAE Points Structure

| Static Event Points | Static Event Points |
| - | - |
| Business Presentation | 75 |
| Cost | 100 |
| Engineering Design | 150 |
| Dynamic Event Points | Dynamic Event Points |
| Acceleration | 100 |
| Skid Pad | 75 |
| Autocross | 125 |
| Efficiency | 100 |
| Endurance | 275 |
| Total | 1000 |

The business presentation follows the premise of the team as a company aiming to bring their prototype car to a target market. The target market is elaborated in the event brief each year. The overall premise remains the same, but each year there are unique requirements the team must incorporate into their business model. The team must pitch their fictional business to a panel of investors. They are judged on their understanding of the target market and their strategy to enter that market; customer acquisition costs, manufacturing strategy and distribution strategy.

For the cost event, the team submits a report which accounts for all the materials and processes involved in mass manufacturing the car. These material and process costs are taken from tables provided by the FSAE organisers to directly compare between teams. Points are allocated based on the total cost of their vehicle (lower cost being more points) and the accuracy of their report. During the competition itself, the team must front to the costing judges to defend any inconsistencies between the cost report and car as it sits. The cost event tests the team's ability to professionally organise their product data and make cost-conscious design choices.

Engineering design is the highest points static event. This event requires the team to present the workflows they have developed that build into a cohesive engineering programme. Significant judgement is placed on the team's ability to close the loop in their engineering design choices through first principles analysis and practical validation of analysis methods and results.

The acceleration event is a 75m straight course, timed from a standing start. The fastest team receives full points.

The skid pad event tests the car's ability to produce lateral force in a steady state cornering condition. The car completes two rotations each of two linked 15.25m diameter circles, ideally building to maximum cornering speed during the first rotation and holding steady state during the second rotation. The skid pad time is the averaged time for the second rotation of each circle. The skid pad event aims to evaluate how well a car "handles" by demonstrating how well set-up the car is to carry speed through a corner in isolation from it's ability to enter and exit the corner.

Autocross is one lap from a standing start, of a tight circuit track that is designed for average speeds around 40km/h with a length of approximately 800m.

The efficiency event measures how much energy the car uses during the endurance event. For EVs this is determined by an energy meter provided by the event organisers.

The endurance event consists of multiple laps on an autocross style track totalling 22km with a driver swap at half way. The endurance event evaluates the durability and reliability of the car, and is worth the largest share of the competition points.

## 1.2 University of Canterbury Motorsport

University of Canterbury Motorsport, herein called UCM, was founded in 2013 to compete in FSAE Australasia. Figure 1.1 shows all of the FSAE cars UCM has built from 2013 to 2023. UCM's first cars were Internal Combustion Engine (ICE) cars with steel spaceframe construction. In 2015 the team transitioned to building carbon fibre monocoque chassis cars. In 2016 UCM built its first EV, UCM16 (Figure 1.1(d)).

Figure 1.1: UCM FSAE cars built since founding

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_003.png)

UCM16 was an ambitious undertaking, implementing an independent 4-wheel-drive quadmotor system in a newly designed car. It is typical for a team's first EV to be a single motor adaptation of a previous car. The development of the electrical systems in UCM16 was a Masters project carried out by Matt Barham [2]. UCM16's EV systems set numerous design norms that have persisted throughout UCM's EVs to-date.

UCM has a flat management structure that aims to create the highly collaborative environment necessary for designing a well integrated vehicle. The quality of integration between sub-systems is often a direct reflection of the effectiveness of collaboration between the respective engineers responsible for those sub-systems. To develop this environment, UCM runs a small scale internal FSAE competition where teams of 2-5 members design and build radio-control cars with limited materials and processes. Each year, UCM's core engineering design team nominally consists of at least four Final Year Project (FYP) teams. The team is managed by the Team Principal and the Technical Director.

## 1.3 UCM23

## 1.3.1 Project Motivation

Conceptual design work for UCM23 began immediately following the 2022 FSAE Australasia competition. This competition saw the UCM21 car suffer from several electrical reliability issues resulting in a performance detriment and failure to complete the endurance event.

Since UCM's first EV, there has been a trend of UCM EV's increasing in complexity and compounding technical debt, as some systems are re-engineered with compromises to interface with existing systems. In addition, UCM cars were increasing in weight as vehicle concepts favoured increasing power and excessive energy storage.

These trends were identified as hindering the team's overall performance in FSAE competitions. The high-power, four-wheel-drive concept was consistently overstretching the resources of the team with significant opportunity costs. The team was stuck in a trend of improvement through addition of complexity, without a balanced consideration of programme risk that accounted for all events. This often included a complete disregard for costing and efficiency points. UCM23, shown in Figure 1.2 was envisioned to subvert this trend.

Figure 1.2: UCM23 being setup for an autocross practice session.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_004.png)

The Battery Management System (BMS) is a critical system in an EV and mandated by the FSAE rules. For several years UCM used an off-the-shelf BMS solution, the Elithion Lithiumate Pro [3]. While this solution persisted through multiple cars, and allowed the team to establish a knowledge base around other aspects of building an FSAE EV, the flaws of the system were starting to increasingly stand-out as being the next logical step for a concerted effort to improve vehicle reliability. Hence, the development of a custom solution fell within the higher level project objectives for the UCM23 car.

## 1.3.2 Design Philosophy and Vehicle Concept

UCM23 was directed to be a light-weight concept with conservative implementation. Twowheel-drive was favoured over UCM's traditional four-wheel-drive approach. This was done to reduce mass, decrease the required effort to implement effective vehicle dynamics algorithms, and simplify the high voltage system.

A wing-less aerodynamic package focused on under-car aerodynamics. Neglecting wings reduced mass and drag, improving efficiency performance. This approach recognises the opportunity cost of implementing a large number of aerodynamic devices. This cost being a lack of experimental validation, detrimental to the design event. A focus on "simple" implementation with validation studies allows the team to improve on historical performances.

UCM23's LV system concept is a full redesign, with the previous cars' LV system as a reference for detailed circuit implementations. The purpose of this concept is to eliminate technical debt in the form of fragmented sub-systems, where interfaces between sub-systems have been formed inconsistently as new sub-systems have been added or retrofitted. The result of this concept is a reduction in the number of PCBs and fewer distinct physical packages, allowing for greater accessibility, which aids debugging and testing.

UCM23's chassis concept was aimed at increasing accessibility of the car's internals while aesthetically integrating air-cooling ducts. To this end, while not the subject of this thesis, the author created concept models of the chassis and ducts as a combined unit for a visually cohesive concept. The integrated ducting concept incorporated accessibility, as the cooling ducts doubled as removable bodywork for a large open rear section of the chassis. This accessibility aided packaging of the EV systems and enabled airflow through the battery pack.

The battery pack is downsized from previous cars in capacity, from 8.8kWh in UCM21 to 4.5kWh. In addition to a change in cell type, this resulted in a 45% reduction in cell mass. This change was enabled through numerical simulation of energy requirements and validated by UCM21's endurance energy usage. The configuration of UCM23's accumulator is 96s5p with Sony/Murata VTC5A cells.

## 1.4 Thesis Overview

In the FSAE rules, a car's battery pack is called the "accumulator" due to it being a generic term for energy storage, as the rules allow battery cells and super capacitors (EV.6.1.1 [4]). Herein this thesis will refer to the car's battery pack as the accumulator.

In typical applications, battery packs with series cell connections require a BMS to monitor the immediate state of charge and state of health of the overall battery for safety, and maintain the state of charge balance of the cells as they go through multiple charge and discharge cycles. The FSAE rules require all accumulators have such a system (EV.8.3 [4]), which they call the Accumulator Management System (AMS). For the remainder of this thesis, when discussing these systems in general applications, the term BMS will be used. For discussions of systems implemented for FSAE, the term AMS will be used.

This thesis details the development of an AMS for the UCM23 car. All development identified in this thesis was carried out by the author unless specifically indicated otherwise. Background on EV and battery technology is given to motivate the necessity of an AMS from first principles. The generation of high level requirements is explored, as they pertain to the FSAE rules and the UCM team's needs. A review of common BMS design norms is given to contextualise the AMS design and implementation.

Later chapters give a detailed specific description of hardware design for the AMS electronics. This will move down in abstraction levels, from block-diagram concept, through design and analysis, to schematics, layouts, and assembly. Design iterations leading to the final implemented PCBs that form the AMS are explained.

Description of the software design is split between AMS core functionality and "accessory features" such as user-interface design and integration with other vehicle systems. Descriptions of core functionality focuses on block-diagram abstraction levels, explaining the implementation of algorithms.

The final implementation of the AMS prior to the 2023 FSAE competition is presented and with results to validate its expected functionality. Further work following the FSAE competition is detailed, centred on implementing improvements to the AMS's State of Charge (SoC) estimation.

## Chapter 2: Background

This chapter outlines the operating principles of an EV, focused on the Tractive System (TS). This leads into a discussion of High Voltage (HV) battery packs, motivating the necessity of a BMS for their safe operation. Given this motivation, theory around common BMS design trends is investigated to provide context to the design decisions made in further chapters.

## 2.1 Electric Vehicle Tractive System

As a parallel to ICE cars, the Tractive System (TS) of an EV can be thought of as the equivalent to the engine and fuel tank, the tractive system stores energy and propels the car. A typical EV tractive system comprises three components: Motor(s), Motor Controller(s), and Battery Pack (or alternative energy storage). Figure 2.1 shows a diagram of UCM23's tractive system.

Figure 2.1: Diagram of UCM23's Tractive System

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_005.png)

## 2.1.1 Motors

Electric motors work on the principle of electromagnetism, that a current flowing through a conductor produces a proportional magnetic field. Flowing current through conductors in a specific arrangement, a rotating magnetic field is generated, forcing rotational motion of an associated rotor. Types of electric motors diverge in physical layout of components, the methods through which they produce magnetic fields, and how they achieve the required arrangement of current [5].

Figure 2.2: AMK DD5-14-10-POW Motors used by UCM23.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_006.png)

UCM23's motors are AC Permanent Magnet Synchronous Motors (PMSM) from AMK (DD5-14-10-POW) [6], one is shown in Figure 2.2. Three-phase AC current flowing into the motor's stator windings produces the required rotating magnetic field. In contrast, a DC motor utilises brushes to mechanically switch current into the motor's rotor. The use of AC is advantageous in EV applications due to the lower susceptibility to wear, relying on electronic switching rather than mechanical brushes [7]. Permanent magnet rotors allow for high power density and high torque to inertia ratio [8], desirable for a high performance application like FSAE. The use of a permanent magnet rotor is what enables the "synchronous" operation of the motor, where the rotor is locked rotationally with the magnetic field produced by current through the stator windings.

## 2.1.2 Motor Controllers

EVs require a motor controller to provide appropriate power from the battery pack to the motor(s), according to requests from the driver. While brushed motors are still used for their technological maturity, motors utilising electrically switched commutation are becoming increasingly prevalent for EV motors due to their higher performance and lower mechanical wear [7]. For these motors, the motor controller is called an "inverter" which is the name given to a power electronics device that converts DC to AC [9, 5]. UCM23 utilises two AMK KW26-S5-FSE-4Q inverter units [10], which produce the variable frequency three-phase AC required by the AMK PMSMs.

## 2.1.3 Battery Packs

An EV's battery pack stores tractive energy in electrochemical cells. OEM packs differ in a wide range of ways, the most significant being cell chemistry and cell form factor [11].

In the current state-of-the-art, Lithium-ion cells are the predominant cell chemistry utilised by EV OEMs [12]. Early notable "modern" EVs, such as the General Motors EV1, utilised Lead-acid and NiMH (Nickel-Metal Hydride) battery chemistries [13]. Use of Li-ion cells became predominant as they matured, with typical specific energies increasing from 98Wh/kg in 1990[14] to 300Wh/kg in 2023[15].

"Lithium-ion" is a broad term encapsulating multiple chemistries utilising a Lithiummetal-oxide cathode. Common Li-ion chemistries include:

- Lithium Cobalt Oxide (LCO)
- Lithium Manganese Oxide (LMO)
- Lithium Iron Phosphate (LFP)

- Lithium Nickel Cobalt Manganese Oxide (NMC/NCM)
- Lithium Nickel Cobalt Aluminium Oxide (NCA)
- Lithium Titanate (LTO)

NMC Li-ion cells account for the biggest share of EV packs at 58% as of 2020 [16]. While NMC cells offer higher energy density, LFPs are a viable alternative for lower performance EVs due to their lower cost. Notably in the Chinese market, Tesla equips the low-spec Model 3 with an LFP based pack [16].

Battery cells come in different form factors which can influence how they are incorporated into a design and affect performance. The most common form factors are prismatic, pouch, and cylindrical.

## 2.2 Lithium-ion Cells

## 2.2.1 Electrochemistry

Electrochemical cells work on the basis of paired reduction-oxidation (redox) reactions [17]. A reduction reaction is one that takes in an electron, conversely an oxidation reaction gives off an electron.

In a Li-ion cell, the positive electrode (cathode) of the cell undergoes a reduction reaction. In this reaction, a free electron and a positive Lithium ion are consumed, maintaining the charge balance of the reaction. At the negative electrode (anode) an oxidation reaction occurs, producing a free electron and a positive Lithium ion. The free electrons and Lithium ions given off in the anode reaction are consumed in the cathode reaction. These reactions will simultaneously occur if there is a current path for the electrons to flow from the negative to the positive cell terminal, and there are sufficient lithium atoms to be ionised at the anode for subsequent de-ionisation in the cathode [18]. The reactions of a Li-ion cell are easily reversible [17], allowing a cell to be recharged by applying a charge current. Between the anode and cathode is an electrolyte, the purpose of which is to be a medium through which Li + can flow between electrodes. The electrolyte does not take part in either electrode reaction.

The following two chemical equations are the electrode reactions in an LFP Li-ion cell.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 2.2.2 Physical Construction

It was previously mentioned that individual battery cells are constructed in multiple common form-factors, however, they have the same fundamental constituents; a cathode, anode, electrolyte, separator, and mechanical containment [17]. In normal conditions, the cathode and anode are the only components contributing to the electrochemical functionality of the cell. The separator provides electrical insulation between the electrodes, preventing a short circuit within the cell.

Figure 2.3: Illustration of common Li-ion cell form factors [19].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_007.png)

## 2.2.3 Safety

As in any energy storage system, Lithium-ion cells require safeguards to prevent uncontrolled energy release. The primary risk condition for Li-ion cells is a "thermal runaway" condition [20]. Thermal runaway is a positive feedback loop, beginning with initial cell damage causing an internal short circuit between the electrodes. This short allows the discharge reactions to occur at an unbounded rate. Being exothermic reactions, the resulting heat further damages the cell's separator, exasperating the internal short circuit. This leads to the unbounded discharge reactions spreading, resulting in complete discharge and physical destruction of the cell.

The damage required to initiate a thermal runaway can be triggered by mechanical damage (crushing or puncturing), excessive temperature, and electrical over-stressing. Electrical over-stressing can be caused by an external short circuit of the cell, or more significantly by overcharging the cell [21]. In the case of over-charging, the cell experiences a significant increase in joule heating, in other words it begins to act as an electrical heating element that is thermally dissipating energy rather than storing it.

Safe battery pack design is achieved through layers of hazard avoidance and mitigation. Avoidance of hazardous conditions is achieved through active and passive systems, such as a Battery Management System and cell protective-fusing respectively. Mitigation is achieved through passive features in the pack's design, such as segmentation of the battery pack, over-pressure relief vents and thermal insulation.

## 2.2.4 Nominal Operation

## Units and Nomenclature

Battery capacity is commonly given in energy units of W h or charge units of Ah, each being more useful given context. The W h unit of energy can be directly converted to the equivalent base unit Joules (J). The W h is commonly used in the context where the load is maintaining a constant power, hence increasing current draw over time to keep power constant as the battery terminal voltage decreases. Conversely, the Ah unit is more common when a load is effectively at a constant current, decreasing in power as the battery terminal voltage decreases. An Ah is a unit of charge that can be directly converted to the equivalent base unit Coulombs (C). This conversion is given in Equation 2.1.

<!-- formula-not-decoded -->

A "C" value 1 is a common method of describing charge and discharge current [18]. C values normalise a current according to a cell's capacity. For example a 2, 000mAh cell, has a 1C discharge rate of 2, 000mA. For the same cell, 10C discharge would be 20, 000mA. The same 20, 000mA load on a 20, 000mAh cell would be a 1C load current [18].

## Charge-Voltage Relationship

Ideally, a cell's voltage will relate to its SoC by a nominal characteristic curve, for example Figure 2.4 shows a characteristic relationship for the Sony VTC5A cells used in UCM23. The characteristic of actual voltage at the cell terminal varies dependant on the load due to internal resistance causing an additional voltage drop. Figure 2.4 shows this relationship with a continuous 1C load discharging a cell.

Figure 2.4: Discharge curve for Sony VTC5A cells used in UCM23 [22].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_008.png)

1 not to be confused with the symbol for the unit Coulombs

## Internal Resistance and Voltage Sag

As with any non-ideal electrical component, Li-ion cells have some resistance. The resistance of a cell is commonly called "internal resistance" [23]. When a load current is drawn from a cell, the voltage at the terminals will decrease proportionally. This phenomenon is commonly called voltage sag. Voltage sag is a combination of the linear ohmic voltage drop over the cell's internal resistance and various non-linear effects. Internal resistance varies across a cell's SoC range [24, 18, 23].

## 2.2.5 Necessity of a Battery Management System

## Balancing

When cells are assembled in a battery pack, small variances in each cell's characteristics will manifest in each cell having a State of Charge (SoC) that becomes increasingly different from other cells over numerous charge/discharge cycles. This condition is called charge imbalance. Limiting the degree of imbalance between cells in a battery pack is an essential function of a BMS [13]. Consider an exaggerated case, one cell could become almost fully discharged while all other cells are at around 50% SoC. This condition negates use of almost half the battery pack's energy, as the pack must stop sourcing current to safeguard the fully discharged cell. The described case is extreme, and should only potentially occur with the absence of a BMS maintaining SoC balance. As shown in Figure 2.5, a failure to maintain balance of series connected cells can limit the usable capacity of the battery pack [25, 20].

Figure 2.5: Diagram depicting the limited usable capacity of poorly balanced cells [26].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_009.png)

Figure 2.5 shows the individual SoC of four series connected cells. The first cell has the lowest SoC, and hence limits how much further the battery pack can be discharged. Despite three of the cells being able to accept further charge, as a battery pack they cannot be charged higher because the third cell is already fully charged. This illustrates how imbalanced cells limit the usable charge range of a battery pack.

## State of Charge Estimation

The potential energy stored in a cell is not a directly measurable quantity, and must be inferred indirectly from other directly measurable quantities such as voltage and current. This is called State of Charge (SoC) estimation, for which there are many techniques available [27, 28]. To ensure the energy storage potential of a battery pack is utilised effectively, a BMS is required to perform SoC estimation. In the context of an EV this enables features critical to its usability, such as estimated charge times and vehicle range.

## Safeguarding

As established, maintaining Li-ion cells within safe operating conditions is essential to prevent uncontrolled energy release. The highest probability of a hazardous condition developing is during charging or discharging of cells, while they are subject to thermal loading. A reasonable Li-ion battery pack design must include some means of monitoring voltages, currents, and temperatures of its cells, and a means to cut off the load should any of these measurements go beyond safe limits. This is the most fundamental role of a BMS.

## 2.3 BMS Theory

There is no universal definition for a BMS, however, one will typically fulfil the following functions: [29, 20]

- Measurements
- Charge current control
- Cell balancing
- Estimation of battery SoC and State of Health (SoH)
- Alarms to protect from unsafe operation
- Diagnostics and fault handling
- Thermal management
- Networking with rest of vehicle
- Data storage

A broad distinction between BMS designs can be made by their architecture. BMS architecture describes how the system physically interfaces with the battery pack's cells. The three commonly defined architectures are centralised, distributed and modular [30, 31]. Each architecture includes trade-offs heavily associated with the context of their implementation.

## 2.3.1 Centralised Architecture

A centralised BMS architecture, is implemented as a monolithic unit whereby the entire system is usually implemented on a single PCB. All monitored cells are connected to the BMS unit via a wiring harness, that gives the BMS access to the terminals of each cell 2 in the pack.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_010.png)

Series Connected Cells of Full Battery Pack

Figure 2.6: Diagram of centralised BMS architecture.

## Design &amp; Development Implications

Centralised architecture allows the electronics design to be decoupled from the physical design of the battery pack. Its physical integration is a matter of designing a wiring harness to connect the BMS unit to the pack's cells. Being a single unit, the need to implement communications between sub-units is avoided at the architectural level. This creates a reduction in software complexity relative to other architectures.

A centralised BMS potentially needs to accommodate large numbers of cells. Designing measurement electronics and a PCB to handle large voltage potentials can result in complex and expensive electronics and a large and complex PCB layout, in relative terms. Such a design is also costly to iterate as it implements the design in a consolidated manner.

## Use-case Implications

Centralised systems lack flexibility in implementation. A centralised BMS can be infeasible for a large battery pack, as any centralised design is limited in the number of cells it can manage.

A centralised system is easiest to implement in a battery pack where the BMS was not integrated in the mechanical design. Typically, centralised systems are implemented in products that have a low degree of vertical-integration. This is typical of a prototype or low volume product. An advantage to this lack of integration is interchangeability.

2 In the context of a BMS monitoring a cell, this means a single series connection. It can refer to an individual cell or a parallel-connected group of cells such as the 1S5P Enepaq blocks used in UCM23.

## 2.3.2 Distributed Architecture

A distributed BMS architecture monitors each cell via a standalone circuit, typically with a separate electronics unit and PCB per cell. The "cell-units" report measurements to a master unit via a galvanically-isolated communication method.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_011.png)

Series Connected Cells of Full Battery Pack

Figure 2.7: Diagram of distributed BMS architecture.

## Design &amp; Development Implications

The BMS's cell-units must be considered in the mechanical design of the cell assemblies. Hence, the physical packaging design of a battery pack is coupled with the BMS's design. This comes at the advantage of not requiring a large wiring harness as with a centralised design [25, 20].

Many identical cell-units form the full system, lending towards rapid iterative development. Testing can be carried out with small numbers of cell-units and then expanded with increasing levels of design maturity. This comes at the cost of assembling and testing a large number of cell-units to assemble the finished system.

A significant engineering-effort cost is implementing a galvanically-isolated communication channel from the cell-units to the BMS master. This introduces software complexity, relative to a centralised system.

## Use-case Implications

A distributed BMS is highly flexible. The size of the battery pack is effectively "unlimited" , the system only requires enough cell-units. In reality there will be limitations, resulting from communication between the cell-units and the master unit. Using a daisy-chain or bus style communication method, minimal wiring is required. Distributed systems have a low degree of interchangeability, and are typically implemented in a highly verticallyintegrated environment. This gives control over the BMS and mechanical pack design.

## 2.3.3 Modular/Hybrid Architecture

A modular BMS architecture can be thought of as a hybrid of a centralised and distributed design. There are multiple BMS module units communicating to a master-unit as in a distributed system. In contrast to a distributed system, each of these units manages multiple cells (identified as a module).

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_012.png)

Modularised Series Connected Cells of Full Battery Pack

Figure 2.8: Diagram of modular BMS architecture.

## Design &amp; Development Implications

A modular BMS architecture requires the BMS's electronics design to be integrated with the battery pack's mechanical packaging. However, it allows for a highly modular approach to the mechanical packaging design [30].

This architecture compromises between the consolidation of a centralised system and numerous but simple units of a distributed system. Each unit of a modular design manages a portion of the pack's cells, meaning it can be tested and iterated in isolation without the full system Bill of Materials (BoM) cost. When the full system is being implemented, fewer BMS module units require assembly and testing compared to a distributed system.

## Use-case Implications

The modular architecture largely shares use-case implications with a distributed system, allowing for flexibility in the overall pack design as the system is only limited in its ability to manage the pack by the throughput of the communication channel between the modules and the master unit.

As with a distributed system, a modular system does not require a complex BMS wiring harness, only requiring a communications channel between modules and the master. The modular system similarly has a low degree of interchangeability, lending itself toward implementation in a vertically integrated product.

## 2.3.4 Cell Balancing Methods

Cell balancing is the process of ensuring the SoC of cells in a battery pack do not differ by more than an appropriate amount [32].

Cell balancing methods are broadly categorised as active or passive. Passive cell balancing thermally dissipates excess energy from the most charged cells, where-as active balancing redistributes energy from the most charged cells to the least charged. Passive cell balancing is a simpler lower cost approach, where-as active balancing methods offer greater efficiency and speed [33, 34].

## 2.4 FSAE Vehicle Theory

## 2.4.1 Shutdown Circuit

FSAE rules require a system called the "shutdown circuit" . In the EV industry, the equivalent of this system would be a High Voltage Interlock (HVIL) circuit. The shutdown circuit consists of series connected devices, each of which can be considered a switch. When any device opens the circuit, current cannot flow, allowing any shutdown circuit device to independently disable the car.

FSAE rules require contactors at both the positive and negative terminals of the accumulator, each called an Accumulator Isolation Relay (AIR). These must be located within the accumulator's housing such that if the AIRs are open, no HV is present at the accumulator's HV output. The AIRs are normally open, and are closed by means of an LV input that powers the electromagnet to close the HV contacts. This LV input must be powered from the end of the car's shutdown circuit. Hence, should any device in the shutdown circuit open, current cannot flow to AIRs and they will revert to their normally open state, inhibiting HV from being present outside the accumulator. Should any shutdown circuit device open while the car is diving, power from the accumulator will cease and the car will coast to a stop.

Reading the voltage at any point in the shutdown circuit will indicate if all up-stream devices are closed, or if at least one is open. Reading the current drawn through the shutdown circuit can indicate if the AIRs are presently engaged. With zero current flow in the shutdown circuit, it can be assumed both AIRs are disengaged.

## 2.4.2 Inverter Precharge &amp; Discharge

HV inverters have large capacitors on their DC input to reduce peak input current demands from the battery. Should the accumulator's HV output be connected directly to the inverter from an initial un-powered state, the low series resistance of the inverter's input capacitor will cause a large inrush current. That is, the un-charged inverter input capacitance behaves as an effective short circuit equivalent, causing instantaneous short circuit current draw from the accumulator. Only once the voltage across the input capacitance rises with charge, does the accumulator current fall.

A large in-rush current can cause damage to cells, AIRs, and the inverter, leading to potentially unsafe operation. FSAE rules accordingly require a precharge system to prevent this condition. A precharge system works by having an additional relay that temporarily switches in a series resistor to limit in-rush current. The negative AIR and precharge relay are engaged first, instantaneous current at this point results from the accumulator's voltage and the precharge resistance. The voltage across the inverter's input capacitance will rise accordingly for the associated RC time constant. After an appropriate number of time constants, such that the inverter capacitor voltage is essentially equal to the Tractive System (TS) voltage, the precharge relay is disengaged and the positive AIR is engaged.

There must be a complimentary system to discharge the inverter's capacitance when the vehicle is shutdown, this is the discharge system. Neglecting inclusion of a discharge system can lead to potential shock hazards, as full TS voltage will remain across the inverter's input terminals after the TS has been active. In UCM23 a normally on FET is used, thus the default un-powered state is to discharge the capacitance through the discharge resistor. The FET is turned off through hardware logic, disabling discharge, only when there is verification of the AIRs being engaged. This is done by measuring the AIR's holding current drawn through the shutdown circuit. The precharge and discharge system are shown in Figure 2.9. These are distinct systems within the car, the precharge system is located in the accumulator, and discharge is located near the inverter.

Figure 2.9: Diagram of precharge and discharge system.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_013.png)

## 2.5 CAN

Controller Area Network (CAN) is a communication protocol developed by Bosch GmbH in the 1980s, common in automotive applications. In terms of the ISO OSI model, the original protocol developed by Bosch describes a data link layer, and a portion of the physical layer, neglecting a Physical Medium Attachment (PMA) sub-layer. The PMA sub-layer converts between physical signals (voltages, currents, frequencies, etc) and digital logic signals (high/low) [35, 36].

CAN is now specified by the ISO 11898 series of standards. ISO 11898-1 specifies the scope of Bosch's original protocol that neglected a PMA. A CAN controller, commonly included as a micro-controller peripheral, implements ISO 11898-1. ISO 11898-2 specifies a PMA sub-layer for CAN. ISO 11898-2 is implemented by a CAN transceiver, this is a device that converts between the Transmit (TX) and Receive (RX) digital logic signals of a CAN controller, and the physical voltages on the CAN bus wires [37]. ISO 11898-2 is a differential two-wire standard that supports bus speeds up to 1Mbit/s and is the most commonly implemented PMA for CAN [35]. Figure 2.10 shows the relationship between these standards, as related to the OSI model.

Figure 2.10: Diagram showing the relationship between CAN hardware, ISO 11898, and the layers of the OSI model [36].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_014.png)

The differential two-wire physical medium of ISO 11898-2 gives CAN suitability for communications in rugged Electromagnetic Interference (EMI) environments, by the nature of common mode noise rejection at the transceiver. Signals are encoded as the difference in voltage present on the two CAN wires. This is in contrast to a single ended signal which would reference a fixed ground potential. Hence, noise caused by EMI impacts both CAN wires and is hence subtracted out at the transceiver.

## 2.5.1 CAN Frames

There are four types of CAN frame: Data, Remote, Error, and Overload. Data frames carry a maximum 8 byte payload. Remote frames simply request another device to send a data frame with a corresponding ID. Error frames are transmitted when a device detects an error while transmitting or receiving another frame. Overload frames are transmitted by a device to pause the bus to give it time until the next incoming frame.

Table 2.1: Standard CAN frame bit format.

| 11(+1) | 6 | 0 - 64 | 16 | 2 | 7 |
| - | - | - | - | - | - |
| ID/Arbitration | Control | Payload Bytes | CRC | ACK | End of Frame |

## 2.5.2 Arbitration

CAN's Medium Access Control (MAC) uses priority based arbitration to avoid conflicts. This is achieved by physically encoding bits in a dominant and recessive state, with logic low as dominant and logic high as recessive. Any device driving the bus to the dominant state will override any devices attempting to transmit a recessive bit. In terms of boolean logic, the CAN bus can be considered an AND of all devices transmission, whereby the bus will be logic high (recessive) only when all devices are transmitting so.

All devices on the bus operate with synchronised bit timing, based on an internal clock. To correct timing drift between devices, a start bit is transmitted allowing devices to synchronise on the rising edge and begin transmission if they have a frame to send. The transmission of frame IDs from each device serves as arbitration. When a device attempts to put the bus into the recessive state for a logic high bit, it will be overridden by any devices driving the bus to the dominant state. When a device detects that it has lost this conflict it will cease transmission. By this method, the remaining winner transmission will have the lowest value frame ID of all that attempted to transmit.

## 2.6 UCM23 Accumulator Design

The UCM23 accumulator design was carried out by the author in parallel with preliminary AMS design work. Details around the physical packaging design iterations are out of scope for this thesis. However, the final implementation is presented as background relevant to the AMS design. In some instances requirements flow from the electronics of the AMS, imposing physical packaging constrains and vice-versa.

## 2.6.1 Cell Configuration

UCM23's Accumulator consists of 480 cells, in a 96 series 5 parallel (96S5P) arrangement. The cells are Sony/Murata VTC5A (US18650VTC5A product code), these are cells of the common 18650 cylindrical form factor. Several cells were considered but the final selection was limited by those available from the team's preferred supplier "Enepaq" [38].

Determination of cell configuration followed a process of; first, constructing a numerical simulation of the proposed car to determine the energy required. This simulation was carried out for an "ideal" maximum performance endurance run. Secondly, iteration of potential series-parallel combinations of available cells determined the lowest mass configuration that allows the motors to operate at their maximum rated power, while storing the minimum viable energy for a full power endurance event. Thirdly, consideration was given to the relationship between cell mass, and vehicle efficiency. In-short the greater the total vehicle mass, the less efficient it is, hence, requiring more energy, adding required cell mass. Consequently, further configurations were iterated on, whereby the car would store less energy, improving the car's overall efficiency in the initial energy requirements simulation by the reduction in weight of the proposed accumulator configuration.

As mentioned previously, UCM uses Enepaq as a preferred cell supplier. From a technical perspective, this is primarily to outsource the process of welding individual 18650 cells. In-house cell welding incurs additional complications within the FSAE rules, in testing that the welded link can act as effective fuses. Given negative experiences of the UCM team in 2016, demonstrating the quality sensitivity of the process [2], out-sourcing cellwelding has become an institutional norm. Enepaq supplies 18650 cells in pre-assembled parallel connected "blocks" as shown in Figure 2.11. Enepaq's blocks feature built in temperature sensors that comply with FSAE rule EV.8.5 whereby the maximum cell temperature within the block is read through a 2-pin connector.

Figure 2.11: Enepaq "blocks" product picture [22].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_015.png)

## 2.6.2 Packaging

Packaging design is heavily influenced by the competition rules, in addition to the desired outcome of minimising the physical volume the accumulator occupies in the car, and consideration for air-cooling. Per the FSAE rules, the accumulator is divided into segments each no greater than 120V and 6MJ. Accumulator segments are connected with "maintenance plugs" that can by readily removed while carrying out work on the accumulator, reducing the risks associated with high voltage exposure. Each segment must be divided by structural walls and insulation.

Figure 2.12: Exploded diagram of UCM23's accumulator.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_016.png)

UCM23's accumulator is divided into four identical segments, each 100V maximum 24S5P. The selection of overall cell configuration as discussed prior, was influenced by the desire to give suitable numbers for even divisions into accumulator segments. The number of series connections 3 in an accumulator segment was influenced by the number of cells monitored by each AMS module. This will be explained in coming chapters. Each AMS module is capable of monitoring 12 series cells, with two AMS modules in each accumulator segment.

As shown in Figure 2.12, where the maintenance plugs of each accumulator segment occupy horizontal space within the accumulator, there is free space underneath. This allows for placement of captive nuts within the accumulator for mounting to the chassis, negating the need for external mounting tabs that would add to the accumulator's footprint.

3 Each series connection is one 5P Enepaq block

Figure 2.13 illustrates a single accumulator segment. With its lid removed it is possible to see the two PCBs that make the cell-carrier system. Not visible, under the lid, is mounted two AMS module PCBs that connect to the respective cell-carrier PCBs.

Figure 2.13: Illustration of a UCM23 accumulator segment.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_017.png)

The final significant aspect of UCM23's accumulator packaging is the so called "observation deck" 4 , illustrated in Figure 2.14, this is a sub-assembly which contains the components that manage the electrical connection between the internal terminals of the accumulator and the DC output connector. The observation deck also mounts supervisory/controlling electronics on several PCBs. Of which, those relating to the AMS will be expanded on in the following chapters.

Figure 2.14: Illustration of UCM23's accumulator "observation deck".

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_018.png)

4 "observation deck" is an internal UCM term, and a homage to Tesla's equivalent sub-assembly called the "penthouse"

## Chapter 3: System Concept Design

This chapter explores the high-level concept design of the AMS. First, the AMS system requirements are outlined. These requirements are split between those required for a minimum viable product prior to the 2023 FSAE competition, and those that extend the functionality of the AMS for the benefit of future UCM teams. This leads to reasoning through selecting an appropriate architecture for the AMS. Given the selected architecture, a discussion of resultant concept choices is presented. This discussion serves as background to their detailed implementation, in coming chapters. This chapter concludes with an overview of the full concept design that informs detailed hardware and software design.

## 3.1 AMS Requirements

The requirements for the AMS implementation this thesis explores can be broadly separated into those required by the FSAE rules, and additional requirements to realise a fully featured Battery Management System by modern EV standards. The FSAE rules inform a minimum viable product, that the author must implement prior to the FSAE competition, and hence took priority. The development process was carried out with the primary goal of realising the earliest possible Minimum Viable Product (MVP).

## 3.1.1 Minimum Viable Product

The MVP must prevent cells from sustaining any form of damage in the course of normal operation. EV.8.3, EV.8.4 and EV.8.5 in the 2023 rules [4] directly outlines the minimum AMS requirements. These rules are given in Appendix A, and are summarised as follows:

## · AMS Functionality

- Voltage and temperature must be monitored whenever the tractive system is enabled.
- Galvanic isolation is required between accumulator segments.
- Cell balancing is prohibited when the tractive system is disabled.
- If temperature or voltage measurements are outside allowable ranges, the AMS must disable the tractive system.

## · Voltage Measurement

- The voltage of each cell 1 must be measured.
- Allowable cell voltage range must correspond with the cell's datasheet.
- Voltage sensing wires to the AMS must have over-current protection.

## · Temperature Measurement

- The temperature of critical points inside the accumulator must be measured.
- The maximum allowable temperature is 60℃ or the datasheet stated limit, whichever is lower.
- Cell temperatures must be taken from contact with the conductor on the negative terminal, no more than 10mm from the terminal. 2
- A minimum of 20% of cells are required to be monitored. The monitored cells must be equally distributed. Every cell should be monitored.

In addition to the requirements generated by the rules, there are requirements to allow for normal operation of the car.

The AMS must have some means of cell-balancing to ensure sufficiently equal SoC between all cells in the accumulator to allow the full capacity of the pack to be utilised in normal operation. The AMS must be capable of communicating to a charger to control charging current. There must be a user-interface to allow for an operator to monitor the accumulator while it charges. The AMS must communicate key information on the state of the accumulator to the rest of the vehicle's systems: Accumulator SoC, maximum cell temperature and minimum cell voltage.

## 3.1.2 Stretch Goal Features

Stretch goal features pertain to improvements post competition that facilitate a smooth technology handover to future UCM teams. This means treating the developed AMS as an out-of-the-box product to implement within a new accumulator. The most critical feature, is SoC estimation that can inform accurate vehicle range estimation. This will allow future teams to design lower mass accumulators, with confidence in running the endurance event length. AMS stretch goal requirements are as follows:

1 Or parallel group of cells such as an Enepaq block

2 Heavily summarised. The internal temperature sensors of Enepaq block satisfy EV.8.5

- Investigation and implementation of SoC estimation through "Coulomb counting" or a related method [28][20].
- Investigation of methods and implementation of SoH estimation [20].
- Automatic limiting of Tractive System (TS) current at low SoC to prevent premature shutdown.

## 3.2 Selection of Architecture

BMS Architecture lies at an intersection between physical packaging and electronics. Some electrical designs can be implemented in differing ways as to realise different architectures. Whereas some electrical designs lend themselves to specific architectures, as the physical packaging of that architecture creates unique electrical design constraints.

Cell balancing methods must be considered in selection of an architecture. For instance a distributed architecture would not be conducive to an active balancing method, as the additional wiring required negates the advantages provided by a distributed architecture.

## 3.2.1 Selection Criteria

The foremost objective for the development of UCM23's AMS is achieving a mature implementation prior to the 2023 competition. This means the system should be tested fully integrated into the vehicle, with full rules compliance while the vehicle is tested in a competition-like manner. The following is a breakdown of factors that maximise the probability of meeting this objective:

- Maximised Development Agility (Ease of testing and iteration)
- Minimised Manufacturing Complexity
- Minimised Packaging/Assembly Complexity
- Minimised Software Complexity

Maximising development agility recognises the importance of iterative development. Early prototypes are likely to include flaws and oversights. The pace at which these can be identified, corrected and re-tested will have an impact of the robustness of the final design. Judgement on the development agility for each architecture is made subject to the resources and capabilities available to UCM. This criteria is considered to be the most important of those listed, and partially incorporates those subsequently listed.

Manufacturing complexity has an impact of the overall pace of development, even considered in isolation to design iteration. The complexity and quantity of each required electronics system and PCB impacts lead-times, and the need for a "non-standard" BoM items increases the risk of procurement issues. Satisfying this criteria would be an architecture that requires a low number of boards to be manufactured, each with a small BoM, without items of high procurement risk and reasonable cost.

Packaging/Assembly complexity considers the suitability of an architecture for integration into the UCM (and more broadly FSAE style) accumulator. Assembly complexity is judged on the amount of manual assembly work required to install the AMS into the accumulator, with emphasis on repeated actions that could compound susceptibility to quality related issues. Examples of such actions would be multiple connections being made in a specific order where the assembler is required to track each connection for numerous solder or crimp joints.

Software complexity has the least variability between architectures, as the high-level algorithms remain the same. Difference in complexity stems from variance in lowerlevel functionality that collects the data used by the higher-level algorithms. The level of software complexity is thus considered according to the amount of communications required between BMS-units, and the number of distinct code-bases required.

## 3.2.2 Applying Selection Criteria

The decision matrix shown in Table 3.1 gives a summary of the decision to design UCM23's AMS with a modular architecture. Each category was rated on a scale of 1-5 to give an overall mean favourability rating for each architecture. It must be emphasised the summary this matrix gives is subjective within the context of the resources and capabilities available to UCM. Ultimately, it is not to say that one is architecture is objectively better, but best suited to UCM's application.

Table 3.1: Decision matrix for selection of AMS architecture

|  | Development Agility | Manufacturing Complexity | Assembly Complexity | Software Complexity | Overall Rating |
| - | - | - | - | - | - |
| Centralised | 1-Highly Undesirable | 3-Moderate | 2-Undesirable | 4-Desirable | 2.5-Moderate |
| Distributed | 3-Moderate | 2-Undesirable | 1-Highly Undesirable | 2-Undesirable | 2-Undesirable |
| Modular | 4-Desirable | 4-Desirable | 5-Highly Desirable | 3-Moderate | 4-Desirable |

## Development Agility

Distributed and Modular architectures offer the highest degree of development agility. Due to comprising multiple units, small scale development can be carried out. Units can be iterated individually or in small batches, without a full-scale system required. Although, this assumes that design maturity will scale to a full system. This assumption is easier to make for a modular system relative to a distributed one. The reason being, the scale increase is lower for a modular system. For instance a modular system can go from one or two units in testing, to eight or ten units in a full system. Whereas a distributed system must scale to one unit per series cell, in the UCM accumulator this would be 96 units. As a result, small scale testing becomes less valid in building design maturity for a distributed system.

## Manufacturing Complexity

A centralised system has the highest degree of manufacturing complexity. Despite only being a single unit, the system will feature a high part count and will have a relatively large PCB size resulting from the need to separate sections for galvanic isolation between accumulator segments.

A distributed system has a low level of individual BMS-unit complexity, however with a large number of units required for a full system it is deemed to have a moderate degree of complexity.

A modular system has the lowest degree of complexity, with a moderate part count per BMS module unit, and a moderate number of units. Its manufacturing complexity sits as a compromise between a distributed and a centralised system.

## Packaging/Assembly Complexity

The mechanical packaging design of UCM23's accumulator was carried out by the author in parallel with selecting an AMS architecture. This allowed strong emphasis to be placed on this selection criteria.

The FSAE rules require accumulators to be divided into removable segments, this requirement aligns with an AMS architecture that has multiple units that can be packaged into each segment. Hence a centralised architecture is least suited.

A modular architecture is best suited towards the assembly complexity criteria, as the AMS modules can be designed to integrate into the mechanical packaging of accumulator segments, with the only connection between them being a communication channel. A modular system is able to leverage the parallel workflow between AMS development and accumulator mechanical design.

## Software Complexity

A centralised system has the lowest degree of software complexity as all of the cell data is collected in one unit and all of the processing can be carried out on a single microcontroller.

A distributed architecture has the highest degree of software complexity, introducing the need to handle communications and associated error handling. While this is also true for a modular architecture, the difference is the availability of various options for an Integrated Circuit (IC) specifically designed to measure voltages of groups of cells. This can decrease software complexity for a modular system. The ability to perform processing on each module of a modular system, decouples the complexity of communications between boards and their functionality.

## 3.2.3 Resulting Considerations for Modular Architecture

With a modular architecture selected, the system is defined to a greater degree. Further decisions must be made to fully define the system within the bounds of a modular architecture. An overview of relevant decision making is given for the remainder of this chapter. All of these concept decisions are heavily influenced by the objective of mature implementation prior to the 2023 competition. As such, choices that de-risk and expedite timelines are universally favoured.

## Measurement Method

Cell voltage measurements are to be carried out by a dedicated battery management IC. Battery management ICs offer a solution that essentially abstracts cell voltage measurement circuitry into a standalone component, with the significant benefit of de-risking compared to a custom designed measurement circuit.

## Cell Balancing

Passive cell balancing will be implemented. This approach will utilise a current bypass, whereby cells can be selectively discharged through a parallel connected load resistor. An active balancing approach does not give significant benefit for a Li-ion pack, such as UCM23's. Li-ion cells usually accumulate less than 0.1% unbalance per charge cycle, which is manageable through current bypass alone without any significant detriment to electrical efficiency [32]. Hence the additional complexity of active charge redistribution circuits is not justified.

## Data Processing &amp; Communications

There is a choice in the degree to which data processing should be centralised/modularised. This decision is coupled with the selection of a communications method. Battery management ICs, often feature built-in communication interfaces that support galvanically isolated daisy chain communications. For instance, the LTC6811 IC ultimately used, supports Analogue Device's isoSPI [39]. Utilising such a built in interface, would ideally remove the need for a micro-controller on each module, as the battery management ICs of each could daisy-chain communications directly to one master micro-controller.

However, this approach introduces significant design inter-dependence, as the communications channel is coupled with the chosen battery management IC. By introducing a micro-controller on each module, greater flexibility is offered, essential within the limited development time-frame. A galvanically isolated CAN bus will be used, whereby each micro-controller acts as a buffer between the CAN bus and battery management ICs. The CAN bus' functionality is not reliant on the choice of battery management IC or microcontroller, hence decreasing component inter-dependence within the AMS module design. Designs of the AMS modules and master unit are decoupled, as the exchange of data between them is enabled through software on both ends. Overall, this approach places a greater emphasis on embedding functionality through software rather than hardware.

## Module Powering

There is a choice to be made regarding how each module is powered. The circuitry of each module must be referenced to the module's negative most cell terminal. A common external supply could be provided to each module, with the supply galvanically isolated at each board. Alternatively each module could power itself from the cells it is monitoring. The later approach is favoured, as it is a more standard design and referenced in the LTC6811 datasheet [39]. It comes with an advantage of each module functioning independently at all times.

## Physical Design

The physical design of the AMS pertains to how each AMS module connects to cells of an accumulator segment. Each AMS module is divided into two electronic systems, to decouple aspects of the electronics that are anticipated to require iteration. These systems are the "Cell Carrier System" and "AMS Module Electronics System" .

The cell carrier system forms part of the structure for mounting the Enepaq blocks and their busbars. This system contains the passive cell balancing resistors and FETs, as this circuit is not expected to require significant iterative changes. It provides thermal contact with the mass of cells to better dissipate thermal energy when balancing.

The AMS module electronics system implements the remaining circuitry. It is responsible for performing measurements, processing and communication. It is mounted in the lid of the accumulator segment. For each accumulator segment there are two AMS modules, each comprising a cell carrier and AMS module electronics.

The selection of this layout is determined by the availability of battery management ICs capable of handling different numbers of cells. As such the AMS layout was iterated in conjunction with the accumulator cell configuration to give an appropriate cell configuration that could be divided into identical segments while fully utilising the number of channels on a readily available battery management IC. The result was eight AMS modules each handling 12 cell connections, for the 96s5p accumulator.

## 3.3 Vehicle Integration

## 3.3.1 AMS Master and IO

The need to process data from all AMS modules necessitates a "master" processing unit. This device acts as a buffer between the AMS modules and the vehicle-wide data bus. Data from all AMS modules is processed into critical information that reflects the state of the whole accumulator. The accumulator also requires a device to enable/disable the AIRs. This functionality is incorporated into the AMS Master. Given this unit performs tasks pertaining to the whole accumulator, it is hence named the "Accumulator Motherboard" .

The Accumulator Motherboard utilises the vehicle's CAN bus to communicate with devices external to the accumulator. The AMS broadcasts CAN messages communicating the state of the accumulator. CAN messages are received from the Vehicle Control Unit (VCU) requesting the Accumulator Motherboard to enable the accumulator's HV output.

FSAE rules (EV.7.5) [4] call for galvanic isolation between Tractive System (TS) and Grounded Low Voltage (GLV) components. Galvanic isolation is the condition whereby a signal can pass between distinct circuits without the flow of current between them. The signal is passed between circuits without the circuits referencing a common ground. Subject to the rating of the galvanic isolation method, signals can be passed between circuits that have large potential differences in their grounds. EV.7.5.5 gives requirements for physical separation of GLV and TS components when located in the same housing. Hence, a signal isolation device as the Input/Output (IO) between the accumulator and the rest of the vehicle eases compliance with EV.7.5.5 as there will be no GLV systems present in the accumulator housing 3 .

## 3.3.2 Current Sensor

The FSAE rules (EV.8.7) [4] call for a system called the Brake System Plausibility Device (BSPD): "The vehicle must have a standalone non-programmable circuit to check for simultaneous braking and high power output. " The threshold for "high power" is 5kW. To determine if this condition is met there must be a non-programmable circuit that outputs a signal dependant on measured current flow from the accumulator to the inverter.

Additional to the requirement of the BSPD, the AMS requires a method to measure the current flow from the accumulator. Common methods of SoC estimation rely on a combination of open circuit voltage and current, to track energy flow during charge/discharge. Over time, this data allows SoH estimation.

These two use cases lead to a unified current sensor design, with outputs to satisfy its dual use. The current sensor unit was designed by another member of the UCM team, and utilised a hall effect current transducer. The transducer selected for this design was an LEM HAIS 100-P [40].

## 3.3.3 Fault Latch

Previously mentioned, per the FSAE rules, the AMS requires the capability to shut down the vehicle's TS. The car has a "shutdown circuit" where the current to enable the accumulator's HV contactors (AIRs) flows. The shutdown circuit consists of series devices that can open the circuit to cut current flow to the contactors. When the contactors lose power they open, preventing HV being present at the accumulator's HV output, disabling the car.

3 Apart from the GLV connection required to the Insulation Monitoring Device (IMD)

The rules dictate that when the AMS triggers a shutdown, the shutdown circuit must be latched in the open state until manually reset. This functionality of latching open the shutdown circuit is required for other devices in the car. These devices are the Insulation Monitoring Device (IMD), Precharge &amp; Discharge Over Current (PDOC), and BSPD. Each must open the shutdown circuit independently, but circuitry can be included on one PCB.

The described circuit and PCB is the "Fault Latch System" , which accepts digital logic inputs from the AMS, BSPD, IMD and PDOC to trigger a shutdown. When one of these inputs triggers a shutdown the fault latch will open the shutdown circuit until manually reset.

## 3.3.4 Charging Interface

When the accumulator is connected to a charger, it requires a user-interface for an operator to monitor the state of the accumulator while it charges. A device is required to emulate the vehicle's fault latch and shutdown circuit to allow the HV output to be enabled for charging to occur.

## 3.4 Summary of System Design

Figure 3.1: Diagram of AMS hardware concept

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_019.png)

Figure 3.1 shows the hardware concept for the UCM23 AMS, as a combined illustration of how elements interface with each other and their physical location relative to the accumulator container and the accumulator modules.

Each accumulator segment, of which there are four, contains two modules. Each module contains 12 cell "blocks" , and a cell carrier unit breaks out the cell connections to a respective AMS module unit. The AMS CAN bus connects all eight AMS modules to the Accumulator Motherboard.

The Accumulator Motherboard interfaces with the vehicle systems via the accumulator IO PCB connecting to the vehicle wide CAN bus, and outputs alarm flags to the fault latch. The alarm flags from the accumulator are the PDOC, IMD and AMS flags. These flags are inputs to the fault latch circuit, external to the accumulator. Should any alarm flag be triggered the fault latch will open the shutdown circuit to cause the car's HV to disengage.

The precharge system within the accumulator is commanded by digital logic signals from the Accumulator Motherboard according to CAN messages from the vehicle CAN bus. Also from the vehicle CAN bus, measurements are received from the current sensor measuring the accumulator's output current. This sensor is located external to the accumulator due to its role in the BSPD system.

## Chapter 4: Hardware Design

This chapter details the hardware design for the UCM23 AMS. This begins with an outline of all the electronics systems that comprise the system concept detailed in Chapter 3. A general workflow for the design process is presented. For each electronics system the process is further elaborated; beginning with requirements, followed by a block diagram, component selection, circuit design, concluding with schematic capture and PCB layout.

The following electronics systems were designed by the author:

- AMS Module
- Cell Carrier
- Accumulator Motherboard
- Accumulator IO
- Precharge

## 4.1 Design Tools and Workflows

All PCB designs were completed with the open-source Electronic Design Automation (EDA) software package KiCAD. KiCAD was primarily chosen due to the author's prior familiarity. Ultimately the choice of software package does not significantly impact the quality of design, given reasonable fitness of a software's capabilities for the task. Different software options vary in details but broadly follow an established workflow. Effectiveness executing a workflow has the largest impact on the quality of a design.

The majority of electronics systems designed must negotiate packaging requirements, and vice-versa with some packaging requirements being dictated by PCB layout. Often there is an iterative convergence between the surrounding mechanical packaging and the PCB layout. Mechanical design of the accumulator was completed in the mechanical CAD package, SolidWorks. SolidWorks allows for the importation of STEP files, an ISO specified file format to exchange 3D models. STEP files can be thought of as the CAD equivalent of a PDF. KiCAD allows exporting STEP files with a 3D model of a PCB populated with its components. By importing these into SolidWorks, packaging design and PCB layout can be iterated in parallel to converge their respective designs.

Best practice is followed in the design process to minimise the impacts of noise and reduce the probability of issues relating to power supply quality. Each of the PCBs designed, except for the Cell Carrier, are four layer designs. Their stack-up from top to bottom is: signal, ground, power, signal. This stack-up provides low impedance power and ground paths for all components. For power supply related circuits, stitching vias are used to provide low impedance paths to the power and ground planes.

## 4.2 AMS Module Electronics Unit

## 4.2.1 Requirements

The requirements for the AMS module electronics unit hardware are generated from the overall system design detailed in Chapter 3. These requirements are as follows:

- Read voltages of 12 cells
- Read temperatures of 12 Enepaq blocks
- Capable of selecting cells to discharge for balancing
- Galvanic isolated CAN interface
- Operable as a standalone unit for development and debugging

## 4.2.2 Block Diagram of AMS Module

Figure 4.1 shows a block diagram of the AMS module electronics unit. Distinct elements of the system are shown, illustrating their relationship to each-other and their interface with a respective cell carrier unit.

The buck converter powers all other elements of the module unit design. The Battery Management IC acts as the interface between the Micro-Controller Unit (MCU) and the cells of the module, communicating with it via SPI. The USB interface allows the MCU to be programmed and monitored for debugging purposes. The isolated CAN transceiver provides an interface for the unit to communicate with the accumulator motherboard. The DC-DC isolation transformer provides a galvanically isolated power supply for the bus facing side of the CAN transceiver. This allows multiple module units at different ground potentials to communicate on the same CAN bus.

Figure 4.1: Block diagram of AMS module electronics unit.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_020.png)

## 4.2.3 Battery Management IC

A Battery Management IC (BMIC) is a component designed to measure cell voltages specifically for a BMS application. Use of a BMIC is a common choice for implementing a modular BMS [20]. Broadly speaking, a BMIC will consist of multiple high-precision Analogue to Digital Converter (ADC) channels rated to high voltages. For instance a BMIC measuring the voltages of 12 cells, with a maximum cell voltage of 4.2V must be rated to a voltage greater than 4.2V × 12 = 50V plus some factor of safety.

BMICs will have a digital interface to transfer data, such as SPI, I2C or UART. BMICs are available from a range of notable IC vendors including: Analog Devices 1 , STMicroelectronics, and Texas Instruments.

The LTC6811 was selected [39], due to the desirability of the LTC68xx family having a high-popularity in established designs leading to high availability of design and implementation resources. Within the LTC68xx family the LTC6811 was chosen for its suitable cell count and higher stock availability.

1 Acquired and now supplies the former products of Linear Technologies and Maxim Integrated

## 4.2.4 Micro-controller

As discussed in Section 3.2.3, the AMS modules each include a local MCU to perform tasks on a per-module basis. This decouples the BMIC functionality from the means of communication between units. A list of candidate MCU families with built-in CAN controllers is given in Table 4.1. Families/product lines of MCUs are given, as there is an extremely wide range within a given product line such that there is often a suitable product for an application within each. Hence, broad judgements of a product line can offer useful distinction in selecting an appropriate MCU.

Table 4.1: Candidate micro-controller families for the AMS module design.

| Name | Documentation Clarity | Familiarity |
| - | - | - |
| ESP32 | High | High |
| STM32 | Moderate | Moderate |
| PIC32 | Moderate | Low |

The ESP32 family was selected, primarily due to the authors familiarity with the platform, expediting implementation time. However, there are independent reasons the ESP32 was deemed superior in this application. Being marketed for IoT applications, the ESP-32 has a built in WiFi peripheral [41]. This opens the possibility of enabling Over the Air (OTA) firmware flashing, which is desirable for software development purposes given the inaccessibility of the modules when assembled into the complete accumulator. The final reason for selecting the ESP32 is its availability in a surface mount module form-factor [41]. This lies between a standalone IC and development-board. This package consists of the MCU, Flash, Oscillator and WiFi antenna, easing implementation over a standalone IC, while not as cumbersome as a development-board. Figure 4.2 shows a comparison between available form-factors for the ESP32, where the development-board would typically be used in a bread-board prototype and the standalone IC would be utilised in a mass-produced product. The ESP32 module provides an easy to integrate solution for product development such as this.

Figure 4.2: Comparison of ESP32 packages.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_021.png)

## USB Programming &amp; Serial Debugging

Espressif maintains a tool called Esptool.py "a Python-based, open source, platform independent utility to communicate with the ROM bootloader in Espressif SoCs" [42]. The ESP32's bootloader supports program flashing via UART (serial TX/RX pins). The documentation states that pulling GPIO-0 low, while the ESP32 resets, will place the ESP32 into UART flashing mode. To automate this, Esptool asserts the DTR and RTS on common USB to UART chips such that these pins can be used to trigger the Enable (reset) and GPIO-0 (bootmode selection) pins on the ESP32 [43]. The commonly used CH340 USB to Serial chip was chosen for this application. Figure 4.3 shows the recommended circuit to connect DTR and RTS of the CH340 to the ESP32 module, necessary to ignore operating system triggered functions of DTR and RTS. In normal operation, the CH340 allows a user to send/receive serial data over a USB connection, commonly plain text to monitor the running program's status.

1

0

Figure 4.3: Portion of the Espressif ESP32 DevKit Schematic showing the automatic bootloader circuit [44].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_022.png)

## 4.2.5 Temperature Monitoring

The temperature of all 12 Enepaq blocks in the module are to be monitored. Each Enepaq block has a 2 pin interface for reading its internal temperature sensors. The datasheet states "it acts as a zener diode, whose voltage drop depends on temperature. It requires a pull-up resistor (680Ω) to operate at cell voltage level" [22]. Hence the AMS module must provide a reference voltage to pull-up to, and read the voltage drop across each 2-pin interface. Figure 4.4 illustrates this. While this example shows the temperature sensor powered by the cell, this does not have to be the case, as stated "Temperature sensor is galvanically isolated from cell terminals and signal can be safely read with separate circuit" [22].

Figure 4.4: Enepaq's example test circuit for reading a temperature sensor [22].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_023.png)

A 3.3V regulator is used to provide a switchable reference voltage for the temperature sense pins to be pulled up to. The SPX3819M5-L-3-3 was chosen as a readily available common part. The 3.3V level was chosen for this purpose as it is within the range of "cell voltage" as stated by Enepaq and is a common IC operating voltage. All temperature sensors are referenced to a common ground, and their positive input pulled-up to the 3.3V output of the regulator. Hence, the voltage drop across each sensor can be measured with an ADC referenced to the common ground.

To measure the 12 temperature dependant voltages, a dedicated ADC IC such as the ADS114S0 was initially considered. Such an IC boasts high accuracy, however it was deemed a prohibitively expensive BoM item, being approximately 2/3 the cost of the BMIC, the most expensive item. The central advantage of using a dedicated ADC chip over the internal ADCs of the ESP32 is higher sampling rate. Neither of which are significant towards this application. The FSAE rules do not specify a minimum sampling rate, it must only be within reason to effectively determine if the car needs to shutdown due to an over-temperature cell. Hence, the shortcomings of the ESP32's internal ADC relative precision can be sufficiently compensated for through software filtering.

## 4.2.6 Power Supply

From the concept design discussed in Section 3.2.3, each AMS module unit is powered from the group of cells that it manages. To achieve this, a buck converter is used to step down total module voltage to an intermediate voltage that can then be regulated to appropriate levels for the different functions of the PCB. Cell voltages range from 2.8V-4.2V, thus the expected input voltage to the AMS module will be 33.6V-50.4V. The voltages required by the unit's systems are 5V and 3.3V. For final regulation to these power rails, the ubiquitous AMS1117 low dropout voltage regulator is used [45]. The AMS1117 requires an input more than 1.5V higher than its desired output voltage. Hence, the buck converter must step down an input voltage in the range of 33.6V-50.4V to an output close but no-less-than 6.5V. A block diagram of this implementation is shown in Figure 4.5.

Figure 4.5: Block diagram of AMS module power supply circuit.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_024.png)

A requirement of 0.5A was set for the maximum current the buck converter's output would need to source. This was driven by the ESP32's expected maximum current draw. The datasheet for the ESP32-WROOM-32D module used, states an average current draw of 80mA [46]. However as stated in the datasheet of the ESP32 IC the ESP32-module contains, current draw can be as high as 240mA with all wireless functionality enabled [47]. Both datasheets recommend a supply circuit capable of sourcing up to 500mA. No factor of safety was added as this recommendation was considered highly conservative given previous experience with the ESP32. No overhead was added for the other circuit elements, as their expected current draw was significantly lower and within the overhead above the expected 240mA maximum for the ESP32. The LTC6811's datasheet states a typical input current of 100µA [39]. The TJA1052i CAN transceiver is expected to draw a maximum of 76mA, when it is driving the bus in the dominant state [48].

Figure 4.6: TI WEBENCH's buck converter circuit reference design for the AMS module PCB.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_025.png)

Selection of a buck-converter IC and feedback circuit was aided by Texas Instrument's WEBENCH Power designer tool [49]. With selection parameters set to Vin = 26 - 52V and Vout = 7V @0.5A the recommended design shown in Figure 4.6 was given. This recommended design was implemented as is, with some equivalent components substituted according to availability with consideration for similar capacitor Equivalent Series Resistance (ESR).

## 4.2.7 Isolated CAN

The ESP32 MCU has a built-in CAN controller. To provide the physical layer interface, a CAN transceiver is required. Galvanically-isolated devices are a common use-case for CAN. As such, dedicated isolation transceivers are available. The TJA1052i by NXP Semiconductors was chosen for this purpose [48]. "The TJA1052i is specifically targeted at Electric Vehicles (EV) and Hybrid Electric Vehicles (HEV), where galvanic isolation barriers are needed between the high- and low-voltage parts" [48].

Shown in Figure 4.7 is a block diagram of the TJA1052i. Evidently, a separate isolated power supply is needed for the bus side VDD and GND. The MCU side of the transceiver shares GND and VDD with the MCU. Hence, an isolated supply must be generated.

Figure 4.7: TJA1052i Block diagram form manufacturer data sheet [48].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_026.png)

An isolated supply is generated by an isolated DC/DC converter. A B0305S-1W is used [50]. According to NPX's application notes for the TJA1052i "The device is able to operate from 5V down to 3.3V on the primary side that allows connecting 3V and 5V microcontrollers. The secondary side needs to be supplied out of 5V for the CAN transceiver. " [51]. Given the primary side is provided the same power supply as the ESP32 MCU, and the transceiver side must be supplied with 5V, the B0305S-1W was chosen as it steps up a 3.3V input to an isolated 5V output. The isolated 5V output powers the transceiver side of the TJA1052i with sufficient power rating. The maximum current draw for the transceiver side is 70mA according to the TJA1052i datasheet [48], hence a maximum power consuption of 5V × 70mA = 350mW . This is within the 1W rating of the B0305S-1W. Figure 4.8 shows the section of the final schematic relevant to what has been described.

Figure 4.8: Section of the AMS module schematic showing the isolated CAN transceiver.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_027.png)

## 4.2.8 PCB Layout

Finished schematics for the AMS Module PCB are given in Appendix B. From this schematic the board layout was designed as shown in Figure 4.9. The PCB layout is largely dictated by the location of the connectors to the cell carrier board (highlighted in Figure 4.9), spaced accordingly to achieve the most effective routing on the cell carrier board from the connectors to each cell.

Figure 4.9: AMS module PCB layout.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_028.png)

## 4.3 Cell Carrier Unit

Design of the cell carrier electronics system is significantly influenced by its physical role in connecting the Enepaq blocks to the AMS module. Apart from its role in providing electrical connections between the AMS module and the cells, it contains the passive discharge circuit for each cell used in the cell balancing process.

## 4.3.1 Passive Discharge Circuit

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_029.png)

260mA @ 3.6V passive cell balancing current.

Figure 4.10: Passive balancing current bypass portion of cell carrier PCB schematic.

Shown in Figure 4.10 is an instance of the current bypass circuit for cell balancing, for which there is an instance per cell (12 per board). C(n) is the positive terminal of the nth cell and C(n - 1) is the negative terminal of the nth cell, which is also the positive terminal of the n - 1th cell. The total bypass resistance is 13.9Ω split between 3.9Ω and 10Ω resistors, such that the cell voltage measurement is between the two. This is a design recommendation given in the BMIC datasheet [39]. This allows the cell voltage measurements to indirectly measure the bypass current, by utilising the voltage drop across the 3.9Ω resistor. This feature enables the AMS software to verify the circuit is functioning, by checking that the cell voltage measurement drops the expected amount when taking a measurement while the bypass FET is enabled. As calculated in Equation 4.1 the bypass current for a full charge cell will be 302mA, thus there will be a 1.17V drop across the top resistor calculated in Equation 4.2.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The FET gate when pulled to the C(n) level will inhibit conduction, and pulled low to the C(n-1) level will enable conduction. The gate is pulled high through a 10kΩ pull-up resistor to default the circuit to inhibit current bypass. The S(n) net-label corresponds to a pin on the LTC6811 BMIC. The LTC6811 has internal circuitry for passive discharge circuits, that can be commanded in software to selectively short the S(n) pin to the C(1 - n) pin. As per the LTC6811 datasheet, a 3.3kΩ series gate protection resistor is included.

The bypass resistance is specified according to a recommendation from the LTC6811 datasheet; a 5% SoC imbalance should be corrected in less than 5 hours [39]. Given the desire to potentially test a range of balancing algorithms, a faster time of 5% SoC correction in 2.5 hours was chosen. Given cell balancing is a closed loop control system, the accuracy of the resistor values is not a significant factor. The 5P Enepaq blocks of UCM23's accumulator are each 13Ah [22], hence per Equation 4.3 and Equation 4.4 requiring a 13.9Ω bypass resistance.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The remainder of the cell carrier board is simply a set of traces breaking out the Enepaq block terminals and temperature monitoring points to headers for the AMS Module PCB to connect to. Surface mount fuses are included at the end of each voltage measurement trace at the end nearest the cell terminals. Shown in Figure 4.11 is the PCB layout and 3D model (note the copper busbars reside on the under-side of the PCB carrying the tractive current, and brass inserts soldered to the PCB take the compressive load of the bolt).

Figure 4.11: Cell carrier PCB layout and 3D model.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_030.png)

## 4.4 Accumulator Motherboard

Figure 4.12: Block diagram of Accumulator Motherboard PCB.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_031.png)

To maximise coherency with the AMS Module design, the Accumulator Motherboard, as shown in Figure 4.12, utilises an ESP32, additionally allowing the WiFi based userinterface that will be covered in Chapter 5. A 5V power rail is supplied from the Accumulator IO PCB, from this a 3.3V power rail is supplied via an AMS1117 LDO Regulator.

The ESP32 MCU sends/receives GPIO level logic flags to/from the precharge PCB to request the accumulator HV to be enabled and receive the status of the shutdown circuit entering the precharge PCB. The HV enable flag to the precharge PCB is set according to CAN messages on the vehicle bus from the VCU, and shutdown circuit status is communicated to the VCU via CAN.

The AMS alarm is an LV level logic flag triggered by the MCU to request the vehicle to shutdown per the FSAE AMS rules. There is an additional flag called the POC (Precharge Over-current) driven by a temperature sensor on the precharge PCB, as required by the FSAE Australasia rules addendum. Both alarm flags pass through the galvanic isolation barrier on the accumulator IO PCB to the fault latch circuit located outside the accumulator.

## 4.4.1 Secondary CAN Controller

Two CAN controllers are required to interface with the vehicle CAN bus and the AMS CAN bus. The vehicle CAN bus is interfaced via a galvanic isolation barrier on the accumulator IO PCB. The ESP32 has a single built-in CAN controller, used for the vehicle bus, requiring an external CAN controller for the AMS bus. The MCP2515 is a CAN controller IC with an SPI interface. The MCP2515 was chosen for its high availability, low-cost compared to alternatives and commonality with established UCM electronics systems.

C8

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_032.png)

√

Figure 4.13: Portion of Accumulator Motherboard schematic showing the standalone SPI CAN controller

## 4.5 Accumulator IO Isolation

Shown in Figure 4.14 is a 3D model of the accumulator motherboard and accumulator IO PCB. The space available for the IO board in the accumulator's housing (Figure 2.14) affected the hardware design. The PCB schematic is given in Appendix D.

Figure 4.14: Render of the Accumulator Motherboard and Accumulator IO Isolation PCB.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_033.png)

## 4.5.1 Power Isolation

GLV (chassis grounded) power is supplied to the accumulator, which is then passed through a step-down isolation transformer. A CRE1S1205SC is utilised, being the only component found that met the voltage step down and isolation requirements, with adequate availability. With a rated isolation of 1kV DC [52], it exceeds the 400V maximum of the accumulator it would guard against during an insulation failure between the HV and GLV. The voltage input range of 10.8-13.2V allows for an unregulated input from the vehicle's GLV which can vary according to the LV battery's SoC. Given no circuit within the accumulator requires more than 5V, a step down isolation transformer was opted for to reduce wasted energy through a voltage regulator that would otherwise be required to regulate down to at least 5V from ∼12V.

Grounded and isolated 3.3V power rails are required for the rest of the PCB. On the chassis ground side an AMS1117-3.3 is used and on the isolated side a CAT6219-330 is used for its smaller footprint enabled by the lower current output required.

## 4.5.2 CAN Isolation

The CAN controller built-in to the MCU on the accumulator motherboard has MCU logic level RX/TX lines going to the IO PCB, to then pass through galvanic isolation to a transceiver on the GLV side. The ISO7721 from Texas Instruments is used to provide galvanic isolation. The CAN transceiver utilised is the SN65HVD230, a ubiquitous CAN transceiver used on all other in-house designed PCBs of the car. The combination of the ISO7721 and SN65HVD230 is functionally equivalent to the TJA1052i isolated CAN transceiver on the AMS modules, however the combination of the two ICs over one was favoured to enable a PCB layout with the limited available space.

## 4.5.3 Fault Flag Isolation

Galvanic isolation of the fault flag signals (POC and AMS) is provided by an ISO7220. The signals entering and exiting the ISO7220 are each buffered through a TL331 comparator to perform a logic-level shift. Being an open-drain output, the logic level of the output is a result of a pull-up to the desired level. The fault signals entering the IO board from the motherboard are at isolated LV level (5V), which are shifted to 3.3V entering the ISO7220. Exiting the ISO7220 the signals are shifted to vehicle GLV level. A low resistance pull-up is used to ensure signals correctly interact with the fault latch PCB, which has a high resistance pull-down on its fault flag inputs. This allows the low resistance pull-up to essentially override the high resistance pull down.

## Chapter 5: Software Development

## 5.1 Firmware Development for ESP32

PlatformIO is an Integrated Development Environment (IDE) for embedded systems development offered as an extension to the popular editor VScode [53]. It automates tool-chain setup and library management.

All firmware written for the UCM23 AMS was built on the ESP32 Arduino Framework. The Arduino framework was created to simplify firmware development for ATmega microcontrollers used on Arduino's boards. It abstracts low level hardware interaction into simple functions. Espressif, the company behind ESP32, maintains a version of the Arduino framework for their micro-controllers. The framework is built on C++. This allows C++ firmware to be written in a way that is cross platform, or highly adaptable to different micro-controllers that have a corresponding version of the Arduino framework.

Espressif offers an alternative lower-level framework called ESP-IDF (Integrated Development Framework). ESP-IDF is built from the ground up for their MCUs with its key advantage being more control of ESP specific functionality. While ESP-IDF was considered, due to the short time-frame prior to the 2023 competition and the author's lack of familiarity with the framework, it was not deemed to provide a significant benefit to the end product to justify the timeline risk associated with learning the framework.

## 5.2 System Level Implementation

The AMS runs two distinct firmware programs, one for the motherboard and one for the modules. Each module executes an instance of identical firmware.

Figure 5.1 shows how the AMS CAN bus is used to exchange data between the programs running on the modules and the motherboard. Variables are listed in boxes representing C structs. Individual variables and structs are colour coded to indicate their respective sender/receiver on the bus, with green being sent to the modules from the motherboard, and blue sent from modules to the motherboard. All measured values on the modules are transmitted to the motherboard, where they are further processed. Values describing the state of all the modules are transmitted from the motherboard to all the modules.

Motherboard

Figure 5.1: Diagram of AMS data structures relating to the AMS CAN bus.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_034.png)

Figure 5.2 shows the structure of data within the motherboard as it relates to the vehicle wide CAN bus, external to the accumulator. Similar to the previous diagram, variables are organised into structs and colour coded. Red values are those received from the vehicle CAN bus and orange values are sent to the vehicle CAN bus.

Figure 5.2: Diagram of motherboard data structures relating to the vehicle CAN bus.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_035.png)

Figure 5.3 and Figure 5.4 show the high level interaction between elements within the AMS module and motherboard programs respectively. For both of these diagrams, the green and blue boxes represent the data structures of their respective programs, given previously.

Figure 5.3: Diagram of AMS module firmware functions.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_036.png)

Figure 5.4: Diagram of AMS motherboard functions.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_037.png)

## 5.2.1 AMS CAN bus

The following discussion of the AMS CAN bus architecture is given in terms of the ISO OSI model, which is an architecture level model through which to describe communication systems in common terms. CAN's structure within this model was previously explained in Chapter 2.

## Data Link Layer

At a hardware level, CAN implements CSMA/CD (Carrier Sense Multiple Access with Collision Detection) to handle multiple devices attempting to concurrently transmit messages, Medium Access Control (MAC). Hardware arbitration allows the bus to have multiple devices, where each device transmitting/receiving specific messages blindly and is not programmed with an awareness for all devices that will be accessing the bus. In other words, no software based MAC is required.

## Network Layer

A software based network layer can be as simple as periodically adding messages to the send queue to be handled by the hardware data link layer. However, the AMS CAN bus does not primarily rely on MAC in the data link layer. Given the AMS bus is only accessed by AMS devices, a layer of indirect software MAC is implemented in the form of polling from the motherboard to the modules. Each AMS module transmits messages, only in response to a request from the motherboard. This allows the motherboard's software complete control over the state of the bus, adding flexibility to more effectively use the bus' throughput. To this end, the software based network layer handles, what frames to send and when, including managing CAN frame IDs, this is shown in Figure 5.5.

The AMS bus uses standard CAN frames, which have 11-bit IDs. CAN IDs are formatted as follows, where the upper 4 bits give the sending device's number, and the lower 4 give the type of data the frame contains.

```
CAN_ID = (device_ID << 7) | data_type
```

The device number is 0 for the motherboard, and 1 to 8 for the modules. The data types are enumerated as follows:

1. Reserved / Motherboard Polling
2. Cell Voltages 1
3. Cell Voltages 2
4. Cell Voltages 3
5. Cell Temperatures 1
6. Cell Temperatures 2
7. Cell Temperatures 3
8. Cell Discharge
9. Fault Code

Figure 5.5: AMS CAN network layer diagram.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_038.png)

## Transport Layer

The transport layer is responsible for organising data into 8 byte payloads for the CAN frames managed by the network layer. All cell voltages and temperatures are represented in the application as unsigned 16 bit integers with units 0.1mV and 0.1℃ respectively. Each 16bit value is split into a high and low byte, for 12 cells this results in 24 bytes of cell voltage data organised into the 3 voltage data CAN frames as shown in Table 5.1. The same applies for the 3 temperature data frames, just considering Vn \_ HI/LO as Tn \_ HI/LO.

Table 5.1: Example of cell voltage CAN frames from AMS modules.

Bytes

...

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| - | - | - | - | - | - | - | - |
| V0 _ HI | V0 _ LO | V1 _ HI | V1 _ LO | V2 _ HI | V2 _ LO | V3 _ HI | V3 _ LO |

Bytes

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| - | - | - | - | - | - | - | - |
| V8 _ HI | V8 _ LO | V9 _ HI | V9 _ LO | V10 _ HI | V10 _ LO | V11 _ HI | V11 _ LO |

Cell balancing discharge data is stored as a boolean value per cell. This is trivially formatted in a single CAN frame whereby the first 12 bits of the payload each represent a respective cell.

The motherboard's network layer transmits a polling frame to request data from each module. The format of this frame is given in Table 5.2. module \_ ID is the number of the module being addressed. active \_ ACK is a flag which indicates the last data request from that module was received. request \_ OTA triggers the module to enter WiFi update mode to allow new firmware to be uploaded over WiFi. Table 5.3 gives the format of the frame which transmits full accumulator data to all the modules.

Table 5.2: Polling CAN frame to AMS modules.

## Bytes

Table 5.3: Accumulator data CAN frame to AMS modules.

| 0 | 1 | 2 |
| - | - | - |
| module _ ID | active _ ACK | request _ OTA |

## Bytes

| 0 | 1 | 2 | 3 | 4 |
| - | - | - | - | - |
| Vmed _ HI | Vmed _ LO | current _ HI | current _ LO | temperature _ calibration |

## 5.2.2 Vehicle CAN bus

## Network Layer

Given a lack of control of all devices on the vehicle's CAN bus, a simple blind network layer is implemented whereby frames to send are placed into the send queue for the CAN hardware data link layer to manage.

Only one CAN frame is sent by the AMS to the rest of the vehicle, the accumulator status frame. This contains all data relevant to the vehicle's operation, required by the VCU, or for display to the driver. However this CAN bus is also used when charging the accumulator. While charging, the accumulator is removed from the vehicle, as required by the FSAE rules. Hence its IO is connected to a charge controller unit, which substitutes the vehicle's shutdown circuit and CAN commands. The accumulator command frame has a byte only sent by the charge controller, if this byte is received the motherboard switches to sending charger command frames instead of accumulator status frames. The charger command frames contain values generated by the charging algorithm.

## Transport Layer

Table 5.4 gives the data format in the status CAN frame transmitted by the accumulator. Table 5.6 gives the format of the CAN frame the accumulator expects from the car's VCU or the charger controller PCB. This CAN frame has the primary purpose of requesting the accumulator to precharge/disengage the HV output.

Table 5.4: Accumulator status CAN frame to vehicle.

## Bytes

Table 5.5: Format of status word in accumulator's CAN frame to the vehicle.

| 0 | 1 | 2 - 3 | 4 | 5 | 6 - 7 |
| - | - | - | - | - | - |
| Status _ Word | SoC | voltage | avg_ temp | max _ temp | min _ voltage |

## Status Word Bits (MSB to LSB)

Table 5.6: Accumulator command CAN frame from vehicle or charge controller to accumulator.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| - | - | - | - | - | - | - | - |
| Precharge _ Complete | Shutdown _ Circuit _ Powered | - | - - |  | - | - | - |

## Bytes

| 0 | 1 |
| - | - |
| HV _ request | charger _ connected |

## 5.3 Executive Functions

Executive functions are considered to be the aspects of the program that address core functionality. The highest level actions considered executive functions are basic calculations and manipulation of data that facilitate higher level algorithms.

## 5.3.1 Common

## Function Timing

Both programs utilise paced loops to trigger all executive and algorithm functions, however freeRTOS is utilised by some libraries. Paced loops are implemented with the Arduino Ticker library, which allows a Ticker object to be instantiated that is initialised with a function callback and a minimum time between each call. Multiple Ticker instances can exist, given sufficient time to execute each paced function.

## Handling ESP32 CAN Controller

The Arduino framework for ESP32 is built on the ESP-IDF framework and as such ESPIDF drivers for CAN are accessible, however they are called TWAI (Two-Wire Automotive Interface) in all Espressif documentation [54].

## 5.3.2 Modules

## Provisioning Unit IDs

The desire to run identical firmware of each AMS module means the ID of each device can't be hard-coded into the firmware binary and must be provisioned at runtime. To accomplish this, the Espressif Arduino "preferences.h" library is used. This library abstract Espressif's NVS (non-volatile storage) API which stores key-value pairs in a dedicated partition of the ESP32's flash storage.

On startup, the AMS module firmware checks the NVS for an existing ID. If an ID is not found it is assumed the device is being programmed for the first time, and prompts the user to enter an ID number via the serial terminal. The entered ID is then loaded into NVS, and will be found and used for all subsequent executions of the firmware.

## Handling LTC6811

A simple driver was written for the LTC6811 that interfaces with the moduleData structure, previously shown in Figure 5.1. This driver is written with the Arduino "spi.h" library to implement the data transfer protocol detailed in the LTC6811 datasheet [39]. Paced functions read all 12 cell voltages to the moduleData struct, and command cell discharging according to the boolean array in the moduleData struct. Hence, this struct acts as the interface between the LTC6811 driver and the rest of the program.

This driver is written low-weight for this application, allowing it to be easily understood and modified within the AMS module code. It is not designed with an interoperable interface for use as a library.

## 5.3.3 Motherboard

## Handling SPI CAN Controller

An Arduino library is used which abstracts the functionality of the MCP2515, with data structures for CAN frames and functions to trigger loading/unloading frames from the send/receive registers. This library's CAN frame structs are handled by the CAN network layer, and the send and receive polling functions are called by the transport layer.

## Handling User Interface

The User Interface (UI) is WiFi based. The accumulator motherboard acts as a WiFi access point and web-server, while the UI acts as a web client. A WebSocket channel is established to transmit data between the client (UI) and server (firmware). A WebSocket is a two way communication protocol distinct from HTTP, which serves web page content. HTTP is only capable of serving data in response to a request from a client. In a pure HTTP application, there is no way for a server to update data sent to a client, and relies on the client polling the server for new data. WebSockets are a two way protocol that address this shortcoming of HTTP, they allow a client and server to transmit data to the other without request. A handshake between a client and server is established via HTTP to open a WebSocket channel.

Two libraries are used to add HTTP and WebSocket functionality on top of the ESP Arduino framework's WiFi driver. There is a sequence of packets defined in plain text comma separated values, that encode all the data to send to the UI. The data-rate of WebSockets is not a significant constraint, hence this approach is taken to aid debugging, having data readable in a debug console while developing the UI. A paced function formats the next packet in the sequence and triggers it to send. Each execution of the function iterates to the next packet in the sequence and eventually loops back to the first. On initialisation of the WebSocket library, a function callback is set for an event such as an incoming packet. This function can parse incoming packets from the UI accordingly.

## 5.4 Algorithms

## 5.4.1 Charge

The charge algorithm has access to all accumulator data, and outputs a charge current request, charge voltage limit, and balancing enable/disable signal. This combination of current request and voltage limit, is called Constant Current-Constant Voltage (CC-CV). In CC-CV charging, a constant current is supplied until the voltage limit is reached, at which point that voltage is held while the charge current falls exponentially. Figure 5.6 shows an example of this.

The Brusa NLG-513 is the CC-CV charger owned by the UCM team. This unit is capable of supplying 3.3kW, for the 4.49kWh accumulator this gives a maximum charge rate of 0.73C. Enepaq's maximum rated fast charge current is 30A [22], corresponding to a 2.3C maximum. Hence, the maximum available charge current is well within the the VTC5A cell's limits. A nominal 13A charge current was chosen to give a 1C charge rate, with ideally balanced cells this should give a one hour charge time.

Figure 5.6: Qualitative example of current and voltage over time during CC-CV charging.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_039.png)

While charging, there is a voltage drop across the cell's internal resistance causing a voltage rise at the cell terminals. This is the charging equivalent effect of voltage sag during discharge. The internal resistance of each cell will vary slightly, and by each cell's SoC. This is shown in Equation 5.1, where Vterminal is the measured cell voltage while charging, and VOCV is the Open Circuit Voltage (OCV) of the cell. Given the voltage rise will vary between cells, attempting cell balancing while a charge current is applied could cause false balancing to occur. For this reason the charge algorithm must interact with the balancing algorithm to determine when to balance and if charge current should be limited.

<!-- formula-not-decoded -->

Two negotiation points are given where the balancing algorithm will determine if the charge must be paused or limited. The first point is when the minimum cell voltage measurement reaches the nominal cell voltage of 3.6V . This point is chosen as it is the middle of the cell charge curve, hence giving the most linear relationship between voltage and SoC to correct relatively large imbalances. The second point is when the maximum cell voltage measurement exceeds 4.1V , 100mV prior to the maximum voltage. This point is chosen to allow for accurate final balancing to occur, maximising the accumulators possible charge.

Prior to the first CC-CV requests to the charger, the charge algorithm assesses the minimum cell voltage to determine of the charge should begin at nominal 1C charge, or begin with a slow charge for low starting SoC. The state machine for the charge algorithm is shown in Figure 5.7

Figure 5.7: Charging algorithm, logic flow diagram.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_040.png)

## 5.4.2 Balancing

The balancing algorithm is divided into a controlling state machine, and the functional segment. The controlling state machine runs on the motherboard and handles the enabling/disabling of balancing in coordination with the charge algorithm, this is shown in Figure 5.8. The functional segment runs on each AMS module and controls the current bypass of each cell in the module according to the whole accumulator data provided by the motherboard.

The functional segment outputs a boolean value for each of the 12 cells monitored by a given module, indicating if a cell's current bypass circuit is to be enabled. This is determined through full-accumulator data, targeting equalisation of all cell voltages. This function is continuously run, and its output is conditional on the controller's enabling/disabling of balancing. The algorithm iterates through each cell as shown in Figure 5.9 which gives the logic flow.

As shown by the charging logic in Figure 5.7, during balancing stage 1 the CC-CV charge continues at a current level determined by the balancing algorithm logic shown in Figure 5.8. This charge current is determined such that the theoretical time to charge until the maximum cell voltage reaches the cut-off is equal to the time required to correct the imbalance. The function to calculate this current is given in Equation 5.4, derived by equating Equation 5.2 and Equation 5.3 which estimate the balancing time and charge time respectively. For the UCM AMS, Ibypass in Equation 5.4 is 0.26A.

Figure 5.8: Balancing algorithm controller segment, logic flow diagram.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_041.png)

Figure 5.9: Balancing algorithm functional segment, logic flow diagram.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_042.png)

Equation 5.2 and Equation 5.3 both have the value Qconversion, this a factor to convert a voltage difference to Coulombs of charge. This is ultimately cancelled out in the derivation of Equation 5.4. Hence, Equation 5.2 calculates Coulomb difference between the highest and lowest voltage cells and divides by balancing bypass current to give total time required to balance. Similarly, Equation 5.3 calculates the Coulomb difference between the maximum cell voltage and a fully charged state to give the total time remaining to charge.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 5.4.3 State of Charge Estimation

SoC estimation is implemented using a voltage measurement method. This method estimates SoC according to the relationship given by the cell's discharge characteristic curve. While this method has several drawbacks, it is the simplest method to implement. It also does not rely on Tractive System (TS) current measurement, which was not implemented prior to preliminary vehicle testing.

This method neglects to account for voltage sag resulting from the load current. As such, it won't provide an accurate estimate under driving conditions. However, it will provide an estimate that increases in accuracy the longer the car is at rest. This is an acceptable shortcoming for MVP implementation, as the low voltage cut-off will safeguard the accumulator regardless of any SoC estimation implemented. Shown in Figure 5.10, is a discharge curve given by Enepaq, which relates SoC to terminal voltage under a 5C load. Utilising this curve would result in an overestimate of SoC while the car is at rest. As such, the discharge curve provided by Enepaq for a 1C load (shown in Figure 2.4 in Section 2.2.4) was used, which more closely approximates a zero load charge-voltage relationship. This curve is approximated as a piece-wise function shown in Figure 5.11. The piece-wise transfer function is applied to the lowest measured cell voltage to indicate the SoC of the limiting cell for discharge. The piece-wise approximation is sufficiently accurate for the AMS application as the SoC-voltage relationship is near linear above and below ∼ 20% SoC.

0

Figure 5.10: Discharge characteristic curve for 1x5P Enepaq VTC5A at 5C [22].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_043.png)

Figure 5.11: Piece-wise transfer function approximating Enepaq's 1C discharge characteristic curve.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_044.png)

## 5.4.4 Temperature Monitoring

Temperature monitoring is implemented by reading ADC values, applying a moving average filter, then applying a transfer function from ADC values to temperature values. Enapaq provides a lookup table relating voltage across sensors to temperature. Figure 5.12 shows the transfer function given by Equation 5.5 which approximates the curve of Enepaq's lookup table. This approximation captures the linearity in the accumulator's operating temperature range, from ∼ 10℃ to 60℃. Above 60℃ the car must be disabled, hence accuracy of temperature readings above 60℃ are less critical.

Figure 5.12: Approximate linear transfer function from ADC values to temperature values, and Enepaq provided LUT values [22].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_045.png)

<!-- formula-not-decoded -->

The temperature monitoring function is called at a 5Hz rate. On each call, the temperature ADCs are all read, and values stored in a circular buffer. The circular buffer is five long, and the average value is calculated on every execution of the function. This gives an updated temperature reading at 5Hz, averaging the last second's worth of readings.

An offsetting value Tcalibration is introduced in Equation 5.5 to allow calibration of each module's readings. This value is stored as a preference in flash, as with the module's provisioned ID. In the CAN message broadcast by the accumulator motherboard to all modules, given in Table 5.3, is a byte for temperature calibration. If this value is received as non-zero, the calibration process will execute. For this, five temperate measurements are conducted and averaged. The difference between the result and the calibration value provided is then stored at the Tcalibration value.

## 5.4.5 Fault Detection

The fault detection system runs on each AMS module. Should a fault be detected, an error code is transmitted to the accumulator motherboard. If the accumulator motherboard receives an error code from any module, or a module fails to report data after 5 attempted requests, the motherboard's fault flag output is set to open the shutdown circuit.

The module fault detection function is called at a 5Hz rate, and checks for a series of conditions. Each condition has a corresponding counter. Should a given condition be be met its counter is incremented, otherwise, the counter is decremented. Each counter is limited to a range of 0 to 5. Should a counter reach 5, its corresponding fault code is transmitted. This mechanism is implemented to eliminate false fault detection without impacting true fault detection. Should a fault condition clearly persist, it is acted on within one second. The following is a list of fault conditions.

- Cell over voltage (&gt; 4.2V )
- Cell under voltage (&lt; 2.5V )
- Cell over temperature (&gt; 60℃)
- Unable to conduct measurement

The AMS CAN bus network layer set out in Section 5.2.1 provides a CAN frame for transmitting error codes from the AMS modules to the accumulator motherboard. This CAN frame transmits a single byte error code where each bit corresponds to a fault condition. Comparing to a numerically enumerated approach, this allows for the simultaneous transmission of eight fault conditions in a single byte.

The accumulator motherboard's portion of the fault detection system is executed on each data request to an AMS module, and each data response from a module. A counter exists for each module, the counter is incremented once for every data request, and decremented twice for every data response. In effect, causing the counter to increment on a failed request and decrement on a successful request. Should any module's counter reach 5 it is considered to have failed, meaning the AMS can no longer accurately report the condition of the whole accumulator. This is categorised as a "module reporting fault" .

Immediately on receiving a non-zero module fault code, or a module reporting fault occurs, the accumulator motherboard sets its fault flag GPIO to LOW, triggering a vehicle shutdown by opening the shutdown circuit at the fault latch.

## 5.5 User Interface

The UI must display all cell voltages and temperatures. This is to act as diagnostic information and demonstration of AMS functionality during FSAE tech inspection. High level information for the full accumulator should be displayed, including min/max values of cell voltage and temperature, total accumulator voltage, SoC, charging algorithm targets, and actual charger output.

The UI is written with Electron, an open source framework for developing cross-platform desktop applications. Electron apps are built on at least two core processes, "main" and "renderer" . The renderer is built on front-end web technologies, HTML, CSS, JavaScript, and other in-browser technologies. The main process is built on Node.js which is a crossplatform JavaScript runtime environment that allows the program to interact with native operating system APIs.

## 5.5.1 Layout

Figure 5.13: AMS User Interface version 1 layout.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_046.png)

Shown in Figure 5.13 is the layout of the UI design with panels on the left side for individual cell data, and panels on the right side for full accumulator information and charging information. The layout is designed to provide as much information graphically as possible to ease the ability to quickly determine the state of the accumulator and easily identify any off-nominal condition.

Individual cell data for voltage and temperature is presented in two histograms. The scale of the histograms are indicative of expected ranges; the voltage histogram spans from 2.5V to 4.2V and the temperature histogram spans from 0℃ to 60℃. Red and blue arrow markers are placed on the highest and lowest bars respectively to indicate the maximum and minimum values. To avoid clutter, and easier identification of cell location, the cells shown in these two histograms is one module at a time. Cell balancing is graphically indicated, by an animated orange pulse on a cell voltage bar to indicate the corresponding cell has its current bypass circuit enabled.

## Chapter 6: Prototyping and Assembly

## 6.1 Preliminary Work

Prior to electronics design work, packaging of the system into the accumulator was determined. Sketches and CAD models were used to explore concepts, and 3D printing was heavily utilised to mock-up candidate designs. Figure 6.1, Figure 6.2 and Figure 6.3 show various stages of this phase of work. Various packaging concepts were explored leading to the final design of two AMS modules per accumulator segment with separate boards for the core AMS module electronics and the cell carriers for mounting and passive balancing circuits.

Figure 6.1: CAD screenshots taken during accumulator packaging design process. (a) Near final segment design. (b) Final segment design inside accumulator container concept model with excess space for observation deck.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_047.png)

Figure 6.2: Photos of mock-up cell carrier and observation deck. (a) 3D printed prototype of a cell carrier unit and Enepaq cell blocks. (b) Pathfinder prototype observation deck sub-assembly.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_048.png)

Figure 6.3: Photos of accumulator mock-ups. (a) First accumulator mock-up, prior to observation deck design. (b) Final accumulator mock-up with observation deck size finalised.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_049.png)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_050.png)

## 6.2 First Module Prototype

Preliminary testing was carried out with a single AMS module, using spare cells left over from a previous car. This setup allowed initial module design issues to be resolved as early as possible, and build a mature code base for the executive level functions of the software design. Figure 6.4 shows the incremental development of this preliminary testing setup.

UCM23AMS

100

UCM23AMS

UCM

H

730980

100

(a)

(b)

(c)

Figure 6.4: AMS Module prototype at various stages in prototype testing. (a) One cell block connected. (b) Displaying data over the UI, with 4 spare cell blocks. (c) 12 spare cell blocks connected and with full shrouding, while reporting to the UI. (d) Full prototype module with shrouding and lid attached for the adjacent module.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_051.png)

Module1

As seen in Figure 6.4(a), the prototype module was powered from a bench supply, across where the negative and positive most cells would connect. This allowed the prototype AMS module unit to be powered as if connected to a full module of cells, testing the functionality of the buck converter, as detailed in Section 4.2.6. A single cell block was added to test the voltage reading functionality of the LTC6811. Readings were printed to a serial terminal and verified with a manual multi-meter measurement. Figure 6.4(b) shows this setup expanded with four cell blocks, now testing an early implementation of the WiFi UI. Figure 6.4(c) shows the next prototype module, addressing several issues uncovered in the first. Here, the module is monitoring a full array of 12 cell blocks, and is self powered. Cell balancing was tested with this prototype, validating the cell carrier PCB design.

All preliminary testing was carried out with one module, and no motherboard. Due to the same MCU being used on the motherboard and modules, the software ultimately written for each, derived from the code written for this first prototype. The prototype implemented combined functionality of the module and motherboard, neglecting the AMS CAN bus for later development with multiple modules. This approach allowed all the core AMS functionality to be tested with minimal risk and cost to fix any issue.

## 6.2.1 Software Development Process

Firmware for the prototype module was written with the aim of testing core functionality, this was prioritised such that the central aspects of the design were proven first, so any time-costly issues could be resolved as early as possible. Along with these core aspects, a preliminary data structure was established. The prioritised order for development was as follows

- LTC6811 SPI driver
- Temperature measurement
- Cell balancing algorithm
- AMS CAN bus
- WiFi User Interface

This firmware implementation then served as the basis for the distinct module and motherboard firmware versions. The only completely rewritten aspect was the supporting data structure and AMS CAN bus functionality. The prototype did not test the AMS CAN functionality in its entirety, as laid out in Chapter 5, it only tested the isolated CAN transceiver could send/receive frames as expected.

## 6.2.2 Design Flaws and Corrections

During testing of the prototype module, several design flaws were identified:

- Lack of a pull up resistor on the balancing FETs
- Module powering through 12th cell tap causing apparent voltage reading to decrease
- Lack of in-rush current protection on the LT6811 cell voltage inputs
- Insufficient power input decoupling for the isolated CAN transceiver

The LTC6811 datasheet contains reference designs for cell balancing circuits using external balancing FETs [39]. All of these are intended to be implemented on the same PCB as the BMIC, given the LTC6811 has an internal pull-up at each the control line (Sn) for the gate of the nth cell's FET. Hence, a pull up on each FET gate was absent from the cell carrier PCB's first prototype. As a result, when disconnecting the AMS module PCB the floating gate would randomly allow cell blocks to discharge. This was easily identified by means of the discharge indication LEDs. Figure 4.10 of Chapter 4 shows the circuit with the included pull-up resistor to correct this issue.

The cell carrier connects all the cell voltage measurement points to the AMS module electronics unit. The voltage measurement points come from the passive balancing bypass circuit, such that there is a shunt resistor that will cause an apparent voltage drop proportional to the balancing bypass current. This is to have a means of verifying the circuit's functionality by measuring the voltages while discharging and observing the expected voltage drop. This was explained in Chapter 4. The first prototype module utilised the 12th cell measurement point to provide the positive voltage input for the module's buck converter. As a result, the current drawn from the cells to power the module caused an apparent decrease the 12th cell's voltage as the module's supply current was being drawn through the 12th cell's shunt resistor. To correct this, subsequent versions of the cell carrier system included an additional pin for the module to power directly from the positive most terminal of the 12 cells rather than the voltage measurement point.

While testing with increasing numbers of cells connected, the BMIC would occasionally fail, characterised by a rapid thermal event. This was a result of neglecting the series protection resistors recommended for the BMICs inputs, meant to limit any undesired current transients while connecting cells. Subsequent module PCBs include 100Ω series protection resistors on the cell voltage measurement lines, shown in the final schematic in Appendix B.

Using a USB-CAN debugging tool to test send/receive CAN frames to the module, the module would accumulate CAN errors and enter the bus-off state. The quality of the isolated power input to the TJA1052i CAN transceiver was isolated as the likely cause. This was addressed by the addition of decoupling capacitors at the input to the transceiver and output of the DC-DC converter.

## 6.3 Motherboard and IO PCBs

Figure 6.5: First prototype of accumulator motherboard and accumulator IO PCBs.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_052.png)

Shown in Figure 6.5 is the assembled first prototype of the accumulator motherboard and isolated IO PCBs. These two PCBs had a single design iteration following the prototype, addressing design flaws with no functional changes. Rework was carried out on the first prototype to circumvent its issues to bridge the gap between prototypes, enabling testing of the system to proceed.

## 6.3.1 Design Flaws and Corrections

The prototype IO PCB utilised a CAT6219-330 on both isolated and non-isolated segments of the board to provide a 3.3V power rail. This was chosen due to its availability in a TSOT-23 package, in the standard component stock accessible by the author. The more commonly used AMS1117 regulator in a SOT-223 package did not fit the available board space on the isolated side. However, the CAT6219 only supports input voltages &lt; 6.5V resulting in the CAT6219 on the non-isolated side powered from ∼ 12V GLV to fail. This was remedied by replacing it with an AMS1117, as it is rated to a 15V input. The AMS1117's package does fit within the available space on the non-isolated section of the board. The motherboard prototype had two design mistakes; it omitted a pull up resistor on the CAN controller's MISO SPI line, and the chip select line was from a pin on the ESP32 that didn't support logic output.

## 6.3.2 Software Development

Firmware for the accumulator motherboard forked from the code base written for the module prototype, and the primary aspect of this code base retained for the accumulator motherboard was handling the WiFi UI. The foremost additions were implemented and tested as follows:

1. Handling the additional SPI CAN controller
2. Full-accumulator data structure
3. AMS CAN bus
4. Balancing controller
5. Charge controller

## 6.4 Assembly

## 6.4.1 AMS Module PCBs

Shown in Figure 6.6 is all eight assembled AMS module PCBs ready for installation in the accumulator. All PCBs were manufactured externally, but assembled in-house using equipment in the University of Canterbury's surface mount technology lab. The KiCAD interactive HTML BoM plugin was utilised to aid component placement without the need for silkscreen component designation. Following assembly of each PCB, the quality of solder joints to the LTC6811 BMIC was inspected under a microscope. This was to ensure no bridges were formed that could cause a short circuit, or any dry (lacking solder) pins that could cause faulty cell voltage readings.

Figure 6.6: All eight final AMS module PCBs.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_053.png)

## 6.4.2 Accumulator Segments

Accumulator modules were assembled individually, bolting 1x5p Enepaq blocks to a total of eight cell carrier PCBs. One such module is shown in Figure 6.7. Pairs of modules were joined to form accumulator segments. Two AMS module PCBs are installed in the lid of each accumulator segment. The header pins on the AMS module PCBs interface with header sockets on the cell carrier PCB when the segment lid is pushed down and bolted in position. All four accumulator segments are shown in Figure 6.8.

Figure 6.7: A UCM23 accumulator module (half a segment) being assembled.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_054.png)

Figure 6.8: All UCM23 accumulator segments fully assembled.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_055.png)

## 6.4.3 Observation Deck with Accumulator Motherboard

Figure 6.9 shows the so called "observation deck" installed in the accumulator, containing the Accumulator Motherboard, IO PCB, Precharge PCB, Insulation Monitoring Device (IMD), AIRs and tractive fuse.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_056.png)

1. LV Connector to the rest of the car, on the Accumulator lO PCB
2. HV Output to the TS (Tractive System)
3. Positive AIR(Accumulator Isolation Relay)
5. Accumulator motherboard
5. 34 Negative AIR
6. Precharge relay on the Precharge PCB
7. Gauge indicating voltage present at the HV output
8. Tractive fuse
9. IMD (Insulation Monitoring Device)

Figure 6.9: UCM23 accumulator's observation deck fully assembled.

## Chapter 7: Pre-Competition Results

Development on UCM23's AMS was divided into pre-competition and post-competition phases. The pre-competition phase was aimed primarily at hardware development, and building reliability with the simplest software implementation to satisfy the minimum functional requirements for the competition. This chapter provides results to validate the AMS's functionality at this stage of development.

## 7.1 Measurements

Figure 7.1 shows results validating the accuracy of AMS temperature measurements. Temperature rise while charging the accumulator is shown. A K-type thermocouple probe was installed in the centre of the accumulator to provide a baseline comparison. Table 7.1 compares measurements with the prototype AMS module, with 6 cells being compared to measurements taken with a high precision bench multimeter (HP3468A).

Figure 7.1: Plot of AMS measured temperature and Thermocouple probe measured temperature, while charging UCM23's accumulator.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_057.png)

Table 7.1: Comparison of cell voltage measurements with prototype AMS module and a high precision multimeter at low SoC.

| Cell | AMS Voltage (V) | Multimeter Voltage (V) | ∆ (mV) |
| - | - | - | - |
| 1 | 3.3984 | 3.3865 | 11.9 |
| 2 | 3.3902 | 3.3785 | 11.7 |
| 3 | 3.3880 | 3.3763 | 11.7 |
| 4 | 3.3975 | 3.3855 | 12 |
| 5 | 3.3932 | 3.3813 | 11.9 |
| 6 | 3.3987 | 3.3869 | 11.8 |

## 7.2 Fault Detection

Figure 7.2 and Figure 7.3 show AMS fault cases being tested under driving conditions. For both of these tests, the under-voltage and over-temperature thresholds were adjusted to purposefully trigger a fault. Figure 7.2 shows the maximum temperature threshold set at 15℃ (normally 60℃). When the AMS maximum temperature rises beyond the cut-off level, the car shuts down. Logged data shows the inverter's ready state signal, part of its CAN status message, becomes zero. This indicates there is no-longer an HV input to the inverter. This is similarly shown for the under-voltage fault case in Figure 7.3, with a threshold set at 3.8V. Accelerator pedal position is included in both plots to illustrate that driving is completely inhibited when fault conditions occur. Figure 7.4 shows the AMS fault light visible after the car shutdown while testing the fault conditions. This light directly indicates the fault latch system has opened the shutdown circuit.

Figure 7.2: Plots showing data recorded with UCM23 while tripping an AMS over-temperature fault.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_058.png)

Figure 7.3: Plots showing data recorded with UCM23 while tripping an AMS under-voltage fault.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_059.png)

Figure 7.4: AMS fault light visible in the cockpit of UCM23 during testing of the AMS fault detection system.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_060.png)

## 7.3 Communications

Figure 7.5 shows AMS diagnostic data logged under driving conditions. The data provided shows the highest AMS module communication error counter. This shows that no more that one message is missed consecutively on the AMS CAN bus by any of the modules.

Figure 7.5: Logged AMS CAN lost message counter of 20 minutes of driving.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_061.png)

## 7.4 Cell Balancing

Figure 7.6 shows the results of a test conducted with a prototype AMS module, consisting of 12 series-connected Enepaq cell-blocks. The module was subjected to 10 charge/discharge cycles without cell balancing enabled. The difference between minimum and maximum cell voltage was logged with ±1mV precision by the AMS module electronics unit at the end each charge. This test was not able to show a perceptible increase of imbalance over its duration. This result serves to validate the choice of passive cell balancing over active cell balancing.

Figure 7.6: Comparison of measured voltage imbalance over 20 charge cycles with cell balancing enabled and disabled on a prototype AMS module.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_062.png)

Figure 7.7 shows the minimum and maximum cell voltages of the same prototype AMS module, while testing the cell balancing algorithm. This data is logged by the AMS module electronics unit to ±1mV precision. To create the initial imbalance condition, with the AMS module electronics unit removed, random cell balancing control header pins were temporarily connected to their respective negative cell terminals allowing them to discharge and create an imbalanced condition. The AMS module electronics unit was then reinstalled with the cell balancing algorithm enabled. This test demonstrates the cell balancing algorithm controlling each of the 12 passive balancing discharge circuits on the cell carrier unit. At the start of the test, the maximum cell voltage is ∼ 65mV higher than the minimum cell voltage. Over time, the maximum cell voltage can be see decreasing until it is within 10mV of the minimum cell voltage.

Figure 7.7: Comparison of minimum and maximum cell voltages in an AMS module prototype, testing cell balancing functionality.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_063.png)

## 7.5 Charging

Figure 7.8 shows data logged while charging UCM23's accumulator. This data is logged in the AMS from values sent via CAN by the Brusa NLG-513 charger. Current values are to the nearest 10mA and voltage to the nearest 100mV . Total accumulator voltage can be seen rising steadily during the constant current phase of charging, and holding near constant during the constant voltage phase of charging in the final 20 minutes while charge current reduces to near zero.

Figure 7.8: Plot of voltage and current while charging UCM23's accumulator.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_064.png)

## Chapter 8: Post-Competition Development

This chapter details further development made to the AMS following the 2023 FSAE Australasia competition. The UCM team's experience at this competition is recalled in Appendix E. Further development was centred around creating algorithms that extend the utility of the AMS for future teams.

## 8.1 Module Power Efficiency

With AMS modules being self powering from the monitored cells, they will discharge the accumulator over time on standby. Their power efficiency while in standby will determine how long they can sit in this state, without a required charge.

Power consumption in normal operation was determined at the prototype stage. Previously mentioned in Chapter 6, a design flaw in the first module prototype resulted in the voltage of the positive most cell appearing lower. This was caused by the module drawing its current through a series 3.9Ω resistor on the cell's voltage measurement line. However, this allowed an indirect means to estimate the current drawn by the module. This voltage drop is shown in Figure 8.1 and the module current draw is hence calculated in Equation 8.2.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 8.1: Apparent lower voltage at 12th cell of the AMS module first prototype.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_065.png)

The calculated current draw of 46.0mA is also corroborated with the module powered from a bench supply, reading 0.04A. The nominal power consumption for the prototype AMS module is hence, 12 × 3.42V × 46.0mA = 1.89W . Enepaq's 1x5p VTC5A blocks are quoted as 46.8W h giving the expected discharge time of 46.8 × 12/1.89 = 297h or 12 days.

## 8.1.1 Investigation of avenues for development

A 12 day standby time is not desirable, typically a commercial BMS will have standby times in the order of months. To determine a path to improving this, the contributing factors need to be identified. This led to a split consideration of the efficiency of the buck converter, and the power consumption of the module downstream of the buck converter. Hence, determining the efficiency of the buck converter was necessary to place proportionate significance on both factors. Should the buck converter be highly inefficient, improvements to the power consumption of the downstream elements would not be valuable. Conversely, efficiency improvements to an already efficient buck converter would not be valuable.

## Determining Buck Converter Efficiency

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_066.png)

Figure 8.2: Measurements to determine buck converter efficiency prior to attempted improvements of standby time.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_067.png)

Figure 8.2 show the measurements performed to determine the buck converter efficiency. Figure 8.2(a) corroborates the calculated current draw at 40V calculated previously in Equation 8.2 as 46.0mA. The buck converter output voltage was measured at 6.41V . Shown in Figure 8.2(b) the buck converter is bypassed and the module is powered by the bench supply at the output of the buck converter. Supplying the measured 6.41V the module draws 160mA. From these measurements, calculated in Equation 8.5, the buck converter efficiency in this condition is 56%. It is necessary to note that this measurement applies only to this power level, as a buck converter's efficiency will depend on its operating conditions.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## Efficiency vs Output Current (fSW= 0.7 MHz, VOUT= 3.3 V)

Output Current (mA)

Figure 8.3: LMR16006 efficiency plot from its datasheet [55].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_068.png)

Shown in Figure 8.3 is a plot of efficiency for the LMR16006 buck converter IC [55]. While this plot shows a lower Vin than supplied to an AMS module, it does show the efficiency varies by ∼ 15%. Hence it is postulated the buck converter efficiency varies similarly across the output current range at higher Vin. This assumption is tested in the course of improving standby time.

From the initial measurements, the power consumption of the module's circuity is unexpectedly high and the buck converter's efficiency poor. Firstly, efforts are made to reduce the power consumption of the module's electronics following the buck converter. Based on the efficacy of these efforts, the necessity of implementing a more efficient buck converter, better suited to low power consumption was determined. The measurements shown in Figure 8.2 were repeated for differing software and hardware configurations. The results of these tests are given in Table 8.1.

Table 8.1: AMS module power consumption and buck converter efficiency in various configurations.

|  | Iout(mA) | Iin(mA) | ηbuck | Standby Days |
| - | - | - | - | - |
| Unchanged Prototype | 160 | 46.0 | 56% | 12 |
| WiFi Disabled | 86.3 | 17.5 | 78% | 33 |
| ESP32 Sleep | 48.3 | 9.59 | 79% | 60 |
| TJA1052i Removed | 31.0 | 6.32 | 77% | 91 |
| B0305S Removed | 17.9 | 3.47 | 81% | 166 |

## WiFi Disabled

The original prototype for which power consumption measurements were conducted in Figure 8.2, ran the prototype software configuration. This configuration was testing the AMS module standalone, with the ESP32's WiFi peripheral active to communicate with the UI. The more matured full-system implementation utilises the AMS CAN bus, meaning the WiFi on an AMS module remains inactive. This already leads to an improvement in standby time from 12 to 33 days.

Noteworthy is the significant improvement in the buck converter's efficiency at this reduced power consumption. All subsequent measurements give a buck converter efficiency ∼ 80%. This improved efficiency is a result of the ECO mode function for this buck converter. The datasheet states: "The LMR16006 operates in ECO mode at light load currents to improve efficiency by reducing switching and gate drive losses. The LMR16006 is designed so that if the output voltage is within regulation and the peak switch current at the end of any switching cycle is below the sleep current threshold, IINDUCT OR ≤ 80mA, the device enters ECO mode. "[55].

## ESP32 Sleep Mode

Current draw was tested with the ESP32 MCU running a modified firmware that placed it into deep sleep mode following initialisation of the module. The impact of power consumption in this mode proved to be significant, leading to an almost 2x improvement in calculated standby time from 33 to 60 days.

The ESP32's sleep mode was tested with the intention of introducing a feature that can place the MCU into the sleep mode after a certain time period since receiving a polling CAN message from the AMS motherboard. Waking the MCU can be triggered by an external GPIO interrupt, hence the intention of utilising CAN RX to trigger a wake-up.

## CAN Transceiver and Isolation Transformer

Measurements were conducted with the TJA1052i isolated CAN transceiver removed, and the B0305S-1W removed, for the purpose of determining how significantly each impacts power consumption, despite their lack of avenues for optimisation.

The CAN transceiver is responsible for 17mA current draw. This is near consistent with its datasheet which state while in the recessive transmit state IDD1 = 5.6mA and IDD2 = 10mA. While the TJA1052i does feature a standby mode, the datasheet claims this does not significantly reduce quiescent current draw [48]. The standby enable pin on the TJA1052 is also referenced to the bus side ground, and hence can not be controlled by the MCU without the addition of another signal isolation IC.

Removing the B0305S-1W showed it has a quiescent current draw of 13mA. Similarly, this does not lend itself to a self-evident design change, however it does highlight the combination of CAN transceiver and DC-DC isolation transformer as the next point of clear consideration for further efforts to improve the AMS module's standby time.

## 8.1.2 Changes Implemented

The sleep mode feature described above was implemented. If an AMS module does not receive a CAN message from the Accumulator Motherboard within 60 seconds of the most recent message, the MCU will enter a deep-sleep, with a GPIO interrupt configured as the wake-up source. This GPIO pin is jumped to the CAN RX pin. While the pin already used for CAN RX could be used as the interrupt GPIO, it is jumped to a second GPIO pin on the MCU dedicated to the wake-up to avoid conflict with the MCU's CAN controller. This was deemed simpler and thus less error prone than de-initialising and initialising the CAN controller on sleep and wake respectively.

Prior to implementation of ESP32 sleep mode, from a full charge the accumulator's SoC fell ∼ 23% over a one week period. Following implementation SoC fell ∼ 12% over the same period. This closely matches the expected standby times.

## 8.2 State of Charge Estimation

State of Charge (SoC) estimation is critical in the fitness of an AMS to its role in an FSAE car. The FSAE endurance event ultimately dictates the capacity, and hence mass, of the accumulator. In the UCM23 car, the accumulator accounts for ∼ 23% of the car's mass without the driver. Reducing the mass of an accumulator design has a significant impact on over-all vehicle mass. The importance of minimised mass for an FSAE car cannot be understated, as it brings performance and efficiency benefits. Ultimately, reducing the mass of an accumulator design requires an increasing degree of confidence in SoC estimation and the capability to manage SoC such that the accumulator isn't prematurely depleted before the end of the endurance event.

## 8.2.1 Shortcomings of Open Circuit Voltage method

The Open Circuit Voltage (OCV) method of SoC estimation was implemented prior to competition. The OCV method is unable to provide estimation during and immediately following discharge, due to the impacts of voltage sag and settling. During operation, the measured accumulator voltage is not open circuit, and hence only provides a qualitative indication of SoC. The OCV method is only able to provide an SoC estimate after the cells have been in a resting state for sufficient time. For Li-ion cells this settling time can be in the order of hours [56].

## 8.2.2 Equivalent Circuit Model

An Equivalent Circuit Model (ECM) addresses the shortcomings of the OCV method. An ECM method is reviewed in [27], from which a simplified implementation was considered for the UCM AMS. The ECM from literature shown in Figure 8.4 provides Rd and Rc to model the cell's internal resistance under discharge and charge loads respectively. Capacitance C, in combination with the terminal resistance Rb, models the settling behaviour of the cell.

The simplified model used in the UCM AMS is shown in Figure 8.5, and mathematically represented in Equation 8.6. This model includes a voltage source Voc, representing open circuit cell voltage as a function of SoC, and a series internal resistance Rinternal. This simplification was deemed adequate as a proof of concept for the viability of an ECM based SoC estimation. It describes the static behaviour of voltage sag under steady state current conditions, without the complicating dynamics of settling effects which would require additional complexity to identify. This allowed a relatively simple implementation that could be compared to other SoC estimation methods to conclude if further development was justifiable.

Figure 8.4: Lithium-ion cell Equivalent Circuit Model (ECM) from literature [27].

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_069.png)

Figure 8.5: Simplified lithium-ion equivalent circuit model considered for UCM AMS.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_070.png)

<!-- formula-not-decoded -->

It is necessary to identify the Rinternal parameter of this model. An ideal constant value for Rinternal could be assumed, however in reality Rinternal will vary throughout a cell's SoC range as it discharges. Logically, if multiple data points can be gathered at different values of I and resulting Vterminal, then a regression line can be fitted to approximate VOC and Rinternal. Linear Least Squares (LLS) can be applied to generate this line of best fit. This must done over a time period short enough that VOC and Rinternal can be assumed as constant, yet long enough to capture wide variation in the measured values. A time span for each estimation of 60 seconds was chosen, with measurements taken in 5 second intervals.

The logic for the implemented algorithm is shown in Figure 8.6. Given sufficient variation of I is required for LLS to approximate values of VOC and Rinternal, the viability of the 12 data points is checked. The algorithm checks for an I variation of at least 3A, otherwise LLS is bypassed. 3A was chosen as a compromise between capturing high quality data sets with clear variation and frequency of valid data sets. This was limited by the typical charge current of ∼ 10A, and the intent to command charge current variation for this purpose without significantly slowing the charge. Additionally an R2 value is calculated and used to reject data sets when R2 &lt; 0. For every data set where LLS does not occur or is rejected, for each of the values Vterminal(i) and I(i), VOC(i) is calculated using the most recent estimate of Rinternal. Then the mean of the VOC(i) values is calculated to go in the place of the VOC value that would otherwise be produced by the LLS calculation. Hence, prior to any estimation of Rinternal the ECM algorithm falls back to an OCV based SoC estimate.

Figure 8.6: Logic diagram of Equivalent Circuit Model (ECM) based State of Charge (SoC) estimation.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_071.png)

## Proof of concept

As a proof of concept for the functionality of the linear regression model, a Python script was written to process manually collected data. This was done in a manner to mimic the algorithm shown in Figure 8.6. The cell's OCV prior to the test was noted to compare with the output of the algorithm. A spare cell brick was charged via a bench power supply to control charge current, with voltage and current measured at intervals of 5 seconds. The cell was allowed to begin charging at 1A for 30s prior to the starting of recording, after which the charge current was ramped over 30s to 4A then ramped back to 1A over the remaining 30s, as shown in Figure 8.7. The recorded data points are shown in Figure 8.8 with the regression line calculated by the Python script, which output an internal resistance estimate of 9.6mΩ and OCV of 3477mV . The cell's measured OCV prior to the test was 3.45V .

Figure 8.7: Current profile for the proof of concept test of the Equivalent Circuit Model (ECM) State of Charge (SoC) estimation algorithm.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_072.png)

Figure 8.8: Output of the linear regression Equivalent Circuit Model (ECM) proof of concept test.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_073.png)

## Equivalent Circuit Model Results

Figure 8.9 shows IR plotted against estimated SoC, while charging UCM23's accumulator. These IR values were identified by the Linear Least Squares (LLS) regression method. This data shows a mean internal resistance of 7.8mΩ. This value is close to that identified by a source stating the DC internal resistance for a single VTC5A cell is 40mΩ [57], for the 5p configuration of UCM23's cell-blocks this would equate to 8mΩ. For the first half of the datapoints the IR identified remains relatively constant. Later in the charge, however, variation in the IR estimate begins to occur. This is likely due to decreasing charge current resulting in lower quality input to the LLS stage, and increased impact of dynamic effects on the data being input to the LLS stage.

Figure 8.9: Equivalent Circuit Model IR identified via LLS plotted against Coulomb Counting SoC while charging UCM23's accumulator.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_074.png)

Figure 8.10: Plots of internal resistance identification with LLS regression, typical for charging and driving conditions.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_075.png)

Figure 8.10 shows two datasets input to the IR identification LLS stage. These plots compare driving and charging conditions, and are datasets typical for their respective conditions. While charging, IR can be identified with this technique, as changes in current levels are purposely introduced to aid the collection of valid data points. This is shown in Figure 8.10(a), where the increasing charge current shows a clear relationship to the increase in measured terminal voltage. In contrast Figure 8.10(b), captured under driving conditions, does not clearly show a relationship that allows for a valid IR estimate to be produced. This is due to driving conditions drawing current with little variation except for short spikes, which results in dynamic effects on the measured terminal voltage and not the static effects which the simplified model captures.

Figure 8.11 shows an alternative method of identifying IR under driving conditions utilising filtered voltage and current values and an estimate of open circuit cell voltage from the Coulomb Counting system that is introduced later. Clear spikes are visible as current and voltage sag decrease, approaching a division by zero condition. This is plotted on shared axes with the IR identified by the LLS technique. Evidently, the LLS technique is not able to produce a valid IR estimate under driving conditions, as was shown by Figure 8.10.

Figure 8.11: Plots showing a 100s long filter applied to voltage and current values to estimate internal resistance during driving conditions.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_076.png)

Figure 8.12 shows a plot of various SoC estimates relating to the ECM system, logged while driving UCM23. The "Open Circuit" Voltage (OCV) SoC is produced by direct conversion from measured cell voltage, as detailed in Chapter 5. This data shows the ineffectiveness of the OCV method for SoC estimation under load due to voltage sag.

The Coulomb Counting SoC, introduced later, is considered the most true SoC estimate to compare to. This is because it shows no erratic variations while also agreeing with OCV SoC after voltage sag subsides.

The IR LLS ECM SoC is the estimate produced by the ECM SoC algorithm using the IR identified by the LLS technique. As expected, this estimate is poor compared the the baseline Coulomb counting SoC. This is owing to the low accuracy IR estimates generated by the LLS technique, as shown previously.

A separate ECM SoC estimation was included which can be programmed with a fixed IR value. This is shown in Figure 8.12 as IR Constant ECM SoC. The result of this estimate follows the Coulomb counting baseline better than the previously mentioned estimate. However, due to the ECM being a static model of a dynamic system, it struggles to produce a matching estimate under transient conditions, as visible in the 200-400s and 1,200-1,600 time ranges.

Figure 8.12: Plot of Equivalent Circuit Model (ECM) based State of Charge (SoC) estimation, logged while driving UCM23.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_077.png)

## 8.2.3 Coulomb Counting and State of Health Estimation

Coulomb counting is an SoC estimation method which works over time, integrating current flow from/to the battery pack. Equation 8.7 shows this in its simplest form, working over discrete time-steps of ∆t. Qmax is the total charge capacity of the pack, hence the change of charge over the total charge capacity in the time-step give the change in SoC. Henceforth, all Q terms are measured in units of Coulomb (C) which is an ampere-second.

<!-- formula-not-decoded -->

Shortcomings of this direct approach to SoC estimation with coulomb counting are the unknown initial condition of SoC(0), and the assumption that Qmax is unchanging over the lifetime of a battery. While the initial condition could be manually determined, and an ideal Qmax assumed, this is potentially inadequate. As the actual Qmax of the cells reduces over the cell's lifetime and measurement errors accumulate, the Coulomb Counting SoC estimation will drift over time.

## Qmax / State of Health Estimation

Qmax is determined while charging, it is a condition controlled by the AMS, allowing high quality data to be utilised in the process. Determining Qmax allows an indication of the accumulator's SoH by comparing the determined Qmax with the theoretical capacity of the cells Qideal, this is described in Equation 8.8. For UCM23 Qideal is 13Ah × 3600s/h = 46, 800C [22].

<!-- formula-not-decoded -->

Qmax is determined by tracking the change in SoC using the ECM method, while Coulomb counting current flow into the accumulator. The initial SoC condition and Qmax can be determined from these data points. Equation 8.9 describes a relationship, where Q∆ is the number of Coulombs counted since the start of the charge and SoCECM is the SoC determined via the ECM method (0 to 1.0 scale). Using this relationship, LLS is applied to find a best fitting value of Qmax.

<!-- formula-not-decoded -->

Given this system requires accurate SoC estimates by the ECM method, periodic variations in the commanded charge current are introduced, allowing the ECM method to work.

Qmax is stored in non-volatile memory and re-calculated on every charge. The logic flow for this algorithm is shown in Figure 8.13 which is initiated every time the accumulator is connected to its charger. Noteworthy, is the algorithm only updates Qmax if more than 10, 000C enters the accumulator, which equates to approximately 10, 000/46, 800 = 0.21SoC increase.

Figure 8.13: Logic diagram for Qmax determination during charging.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_078.png)

A proof of concept test was conducted, with a similar setup to the prior ECM test, to show the Qmax determination method. A cell was charged with constant current, such that ∆Q would be a direct multiple of the charge current and time in seconds since the start of the charge. An ECM SoC value was estimated using an assumed constant internal resistance. Figure 8.14 shows points plotted from the raw data, and a regression line generated by a Python script to emulate the algorithm running on the AMS. The regression line has a gradient of 537.66 Coulombs per %SoC, giving a Qmax estimate of 53, 766C or 14.9Ah. Comparing to the cell's stated capacity of 13Ah this is high, however within reason considering the tested cell was previously unused.

Figure 8.14: Output of the linear regression Qmax proof of concept test.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_079.png)

## Coulomb Counting Continued

When the AMS boots, the stored Qmax value and OCV SoC estimation are used to determine Q(0). This is described in Equation 8.10, where the OCV SoC estimate is multiplied by Qmax to give Q(0). With the initial condition determined, a loop is entered with an iteration every 1 second. In each iteration, Q(t) is calculated, which is the remaining charge in the accumulator. Equation 8.11 gives this calculation, where the current value I is subtracted from the previous iteration's Q(t). This is followed by the calculation given in Equation 8.12, which converts Q(t) to an SoC value by dividing by Qmax. The described logic is shown in Figure 8.15.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Figure 8.15: Diagram of the iterative Coulomb counting algorithm, utilising an estimated Qmax.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_080.png)

## Coulomb Counting Results

Figure 8.16 shows data recorded while driving UCM23, plotting measured Tractive System (TS) current and corresponding Coulomb Count (∆Q) since the start of the session. Figure 8.17 shows a plot over the same time period. It compares Coulomb Counting SoC and SoC estimated directly from measured minimum cell voltage. The impact of voltage sag can be seen on the voltage based estimation. When the car is at rest, the minimum cell voltage is allowed time to settle and rises resulting in the voltage based SoC approaching the Coulomb Counting SoC.

Figure 8.16: Plot showing Coulomb Counting ∆Q and accumulator current output.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_081.png)

Figure 8.17: Plot showing Coulomb Counting based SoC estimate in relation to "open circuit" voltage based SoC.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_082.png)

## Qmax Identification / State of Health Estimation Results

Figure 8.18 shows a plot of datapoints collected by the AMS while charging UCM23's accumulator. These datapoints are the input to the SoH algorithm. The regression line shown is the algorithm's output, which gives a Qmax of 49, 648 Coulombs or 13.8Ah. This is above the stated capacity listed in the Enepaq datasheet of 13Ah [22]. Reasons for this will be explored. Critically, this plot shows the relationship between ECM SoC and ∆Q is clearly linear as expected.

Figure 8.18: Plotted output of the Qmax algorithm during charging of UCM23's accumulator.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_083.png)

During the charging session shown in Figure 8.18, it was noticed the ECM system was only identifying the IR at the start of the charge. This was due to a lack of significant current variation at subsequent points. A software bug was preventing the purposeful charge current variation, required by the ECM system for identifying IR. Figure 8.19 shows the next charge, prior to this issue being fixed. During this charge, at ∼ 40% SoC the charger was turned off and back on. This allowed the ECM system to identify a lower IR than it did at the start of the charge and hence estimate a higher SoC resulting in a lower Qmax estimate of 44, 502 Coulombs over the whole charge.

Figure 8.19: Plot of the Qmax estimation algorithm, recorded during charging, showing the impact of insufficient internal resistance estimates.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_084.png)

The software bug was corrected for the next charge. During this charge the ECM system was able to identify IR throughout the charge when current variation occurred. Figure 8.20 shows the datapoints input to the SoH algorithm during this charge. Larger deviation from the regression line is observed, owing to the ECM system producing IR estimates of variable accuracy, and hence variable accuracy SoC estimates.

Figure 8.20: Plotted output of the Qmax algorithm during charging of UCM23's accumulator after fixing ECM SoC estimation.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_085.png)

To eliminate the accuracy of the ECM SoC estimation as factor in the accuracy of the SoH system, a test was performed utilising SoC determined by OCV. This is shown in Figure 8.21 where the two datapoints were collected after allowing the voltage to settle for 10 minutes. This test yielded the closest uninterrupted Qmax estimate to the capacity quoted by Enepaq, but also showed the accuracy of the ECM system was not primarily at fault for the over estimation of capacity. The most likely cause of this is an over estimation of charge current, and less likely but still possible is that the actual capacity is higher than quoted.

Figure 8.21: Plotted output of the Qmax algorithm counting only start and end points under open circuit conditions.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_086.png)

## 8.3 End of Discharge Derating

At low SoC levels the accumulator's minimum cell voltage will eventually cause the car to shutdown when the AMS outputs a low cell voltage fault. This will occur even if there is some remaining charge, due to voltage sag. The range of the car can be maximised if the current draw at low SoC is limited to prevent voltage sag from bringing the terminal voltage below the minimum cell voltage cut off prematurely.

An algorithm was hence envisioned that utilises the ECM employed in SoC estimation to set a current limit. The current limit is obtained by solving for Ilimit in Equation 8.13, with Vcutoff as the minimum allowable cell voltage. It was initially intended to utilise VOC and Rinternal values produced by the ECM system. However, results showing low accuracy outputs from the ECM system led to a design change. VOC is determined from the Coulomb counting SoC estimate, by applying the reverse of the OCV SoC conversion. Rinternal is set at a constant value of 10mΩ, based on results previously mentioned.

<!-- formula-not-decoded -->

The calculated Ilimit value is communicated via CAN to the car's VCU. The VCU then limits torque commands to the motors, to keep the measured DC current below this value. A combination of two methods were implemented to achieve this.

The first method is a proportional-integral controller, with the proportional and integral elements described in Equation 8.14 and Equation 8.15 respectively. Both controller outputs are clamped in a range from 0 to 1, this prevents the controllers from commanding more torque than requested by the driver when the measured current is below the limit, and prevents negative torque when the measured current overshoots the limit.

For the proportional controller (Equation 8.14), the value αp is a configurable threshold to set the controller's target as a proportion of the current limit. When current is bellow the target the output will be clamped at 1, not attempting to limit current. Above the target the output will reduce to zero as the measured value approaches the current limit.

<!-- formula-not-decoded -->

For the integral controller (Equation 8.15), an αi value is included to configure the controller's target. Over increasing time with current measured below the target, the output will increase towards 1. Conversely, over increasing time above the target, the output will reduce to zero. For this controller, clamping the output in the range of 0 to 1, also prevents excess wind-up. This essentially sets a maximum time window which it integrates over.

<!-- formula-not-decoded -->

The second method of current limiting is a linear approximation of the relationship between inverter input current and requested torque. This is used to set a torque limit. This is described in Equation 8.16, where τrated is the maximum rated torque of the motors and Irated is the maximum rated DC input current of the inverter.

<!-- formula-not-decoded -->

The combination of these two methods in shown in Equation 8.17, which describes how torque requests to the motors are calculated by combining τlimit with throttle pedal position αpedal and the controller outputs Up and Ui. τmax represents either the maximum rated motor torque or a lower value set in the VCU's configuration.

<!-- formula-not-decoded -->

An alternative method for calculating a torque limit was considered, by equating electrical and mechanical power. An electrical power limit could be calculated by Equation 8.18. This could then be considered equal to mechanical power PM . Using Equation 8.19, the mechanical power limit could be divided by the motor's measured rotational velocity to determine a torque limit. On further consideration this method was not implemented, as it was flawed at low speed. For any given maximum mechanical power, as rotational velocity approached zero, the torque limit would approach infinity.

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## 8.3.1 End of Discharge Derating Results

For testing the end of discharge de-rating system, the target cutoff voltage was set as a parameter in UCM23's VCU. Hence this value can be adjusted and transmitted via CAN to the AMS. This is shown occurring in Figure 8.22, where the cutoff was set at 3.5V and then adjusted to 3.7V . When the cutoff voltage is adjusted, the current limit can be seen adjusting accordingly.

Figure 8.22: Plots showing the determination of the current limit to prevent voltage sag below the cutoff voltage, recorded UCM23's VCU while driving.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_087.png)

For the first portion of this testing session, it is observed the TS current is not impacted by the current limit. However with the cutoff voltage set higher the measured current draw becomes limited by this system. Over time in this condition the current limit decreases and voltage sag reduces. Eventually the current limit becomes too low for the car to continue driving. Figure 8.23 shows the latter portion of this test session showing the operation of the current limiting system.

Figure 8.23: Plots showing the operation of current limiting as part of the end of discharge de-rating system, recorded by UCM23's VCU while driving.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_088.png)

## 8.4 Range Estimation

The car's VCU calculates distance travelled by integrating wheel speed, and communicates this to the AMS via CAN messages. Utilising known distance travelled and the Coulomb counting technique, an estimate of remaining range of travel is produced.

The method to produce a range estimate is divided into two functional elements: calculation of historical energy consumption rate, and extrapolation based on immediate SoC and historical consumption rate.

## 8.4.1 Calculating energy consumption rate

Historical energy consumption rate is calculated in a loop as follows where the difference in values from the previous iteration are calculated to give the difference over the time period, set at 10 seconds intervals, this is described in Equation 8.20. If the car travels less than 100m in this period the current iteration is skipped.

<!-- formula-not-decoded -->

∆Q is a value of charge in Coulombs, however this is not directly used. The rate of energy consumption is most applicable, not charge consumption. Under a constant driving load, the current draw will vary. However the power consumption will remain constant. Hence the use of Equation 8.21 to convert charge in Coulombs to energy in Joules. This assumes the variation in the accumulator voltage over this time period is small enough to consider it constant.

<!-- formula-not-decoded -->

As driving loads are not constant, varying between iterations, a moving average filter is used. While a longer iteration interval could be used instead of a moving average filter, this would result in a slower response to a change in driving pattern. The final calculation step is described in Equation 8.22, which calculates the mean distance travelled for energy consumed over the previous 10 iterations.

<!-- formula-not-decoded -->

## 8.4.2 Forward projection

The charge remaining is similarly converted to Joules by multiplying percentage SoC based on Coulomb counting by the Qmax and nominal accumulator voltage. Multiplying remaining energy in the pack by the distance per unit energy average, gives the remaining range estimate.

## 8.4.3 Range Estimation Results

Figure 8.24 shows data logged while driving UCM23, validating the range estimation system. The first 200s can be seen estimating a high value due to utilising a default energy usage value. After this time the system was able to calculate the energy usage within this time and estimate the remaining range. From the data shown in Figure 8.24, the decrease in estimated range is a close match to the distance driven over the same time, indicating the system is working as intended.

Figure 8.24: Plot showing range estimated in relation to distance driven.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_089.png)

## 8.5 Software Implementation

Major changes were made to the AMS code base during further development, the most central being implementation of FreeRTOS to manage tasks. This was done to improve the future-proof the code base and aid the implementation of the improved algorithm's explained previously. Over the Air (OTA) firmware upload to AMS modules and motherboard was also added to aid in this and further development.

## 8.5.1 OTA Firmware Upload

The ESP32 Arduino framework includes libraries to handle the ESP32's internal SPI Flash File System (SPIFFS), and flash firmware binaries stored on the file system. In combination with the web server library and WiFi functionality already in use to communicate with the AMS UI the ability to flash new firmware binaries to the accumulator motherboard and the AMS modules via the UI was added.

To update motherboard firmware, the UI has an HTTP POST request file upload form to select and submit a firmware binary. When this request is received by the motherboard's web-server library, the uploaded binary is written to the file system, flashed, and rebooted.

Uploading AMS module firmware works slightly differently. Similarly, it starts with an upload form in the AMS UI, uploading a firmware binary to the motherboard and writing to its flash file system. The motherboard transmits a CAN message on the AMS CAN bus, indicating to all modules that a new firmware file is available. Receiving this, the modules enable their WiFi functionality and connect to the motherboard's WiFi network that's ordinarily used by the UI. The motherboard serves the firmware binary over HTTP to the modules. Each module downloads the binary to its flash file system, updates and reboots into normal operation.

## 8.5.2 Migrating to an RTOS

Traditional code execution runs in a sequential manner, one action after another. This is how most of the software executed on the AMS is currently structured. This is done with paced loops, where functions are executed in turn with a minimum interval between a given function's last execution. While simple, as the requirement to handle more actions increases, handling a greater number of actions requires more forward planning in their implementation. This is where a Real Time Operating System (RTOS) becomes useful to use.

An RTOS abstracts low level functionality that allows "tasks" to be executed in a manner that is pseudo-concurrent. FreeRTOS is an open source RTOS popular in embedded system, and has cross-platform compatibility with a wide range of micro-controller families, including ESP32. FreeRTOS implements a round-robin scheduler relying on hardware interrupts from an MCU's internal timer peripheral to rapidly switch between all tasks requiring execution. While other abstractions and functionalities are provided, this is the core functionality.

Each "task" is a function that can be written as if it is an independent program, meaning consideration for other tasks don't have to be made in terms of how it is written, for instance time delays can be used within a task that will only pause execution of code within that task but not others. An exception to this isolated perspective, would be accessing shared resources like a GPIO or serial communication. Hence, FreeRTOS provides mutexes to prevent conflicts between tasks accessing shared resources [58].

An important benefit of migrating the firmware to an RTOS is being able to leverage the dual core architecture of the ESP32. Tasks will be automatically assigned by FreeRTOS to one of two cores, allowing elements of the code base not inter-dependant to run with true concurrency. This is especially valuable for the accumulator motherboard.

## 8.5.3 Design

Migrating to the use of FreeRTOS constituted large changes to the existing code base, during which more consistent object oriented design principles were followed. Centrally, adhering to the principle of abstraction, where each algorithm or key functionality is contained within a dedicated class that has only the necessary interface methods publicly accessible.

To improve extend-ability and maintainability of the code base, common object oriented design patterns were implemented as much as possible where appropriate. Design patterns are common approaches to problems in software design, that have evolved over time through iteration. The advantage of implementing design patterns is to skip over this iteration as a design pattern ideally addresses common issues that arise when iterating on a given problem from first principles. From the introduction to [59], a highly regarded book on object oriented design patterns: "They help designers reuse successful designs by basing new designs on prior experience. A designer who is familiar with such patterns can apply them immediately to design problems without having to rediscover them. "

The accumulator motherboard firmware consists of several distinct objects that perform core AMS functionality and higher level algorithms such as the algorithms the make up the SoC estimation system. Each of these objects are to operate as independently as possible, however most need to access outputs of others. To organise these objects, the "singleton" design pattern is utilised, whereby a single globally declared instance of a top level object is implemented. Within the top level object are declarations of algorithm and core-functional objects which can be thought of as sub-programs. This allows each sub-program to access the top level object and it's constituent member sub-programs.

## 8.5.4 Diagnostic Logging

For the purposes of testing newly developed algorithms, additional CAN frames from the accumulator motherboard to the vehicle CAN bus were added, transmitting all relevant values for logging in the car's VCU. To avoid sending excessive data to the VCU and log data during charging, internal AMS logging was added. CSV logs of the outputs of the SoH and ECM SoC algorithms were added to allow the inputs to be plotted. To resolve teething issues associated with the migration to FreeRTOS crash logs were also added. The crash log and CSV algorithm logs are stored in the AMS motherboard ESP32's SPIFFS file system, to be downloaded via the AMS UI.

Additional information was added to the user interface to monitor the outputs of the algorithms developed in this chapter that are relevant/observable during charging when the UI is used. This is shown in Figure 8.25.

Figure 8.25: Final AMS User Interface (UI) displaying the output of improved SoC estimation algorithms.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_090.png)

## Chapter 9: Conclusions

By mid November 2023, the AMS design detailed in this thesis was developed to a mature reliable system, and implemented in the UCM23 car being shipped to Melbourne for the 2023 FSAE Australasia competition. Figure 9.1 shows the car's dash display during testing in late October, with voltage and temperature values reported by the AMS. During this time various software bugs in the AMS were addressed. This proved extremely valuable testing time as an assembly error led to a gearbox failure on the 3rd of November, with testing resumed on the 14th of November. Over the following week, back to back endurance testing was carried out to maximise the chance of identifying any remaining reliability issues. Validation of the systems implemented at this point are provided in Chapter 7. On November 20th, 2023 UCM23 was freighted to Australia. Appendix E details the experience with UCM23 at the competition. Further development following the FSAE competition extended the functionality of the system, with improved SoC estimation. This development is detailed in Chapter 8.

Figure 9.1: Values reported by the AMS, displayed on UCM23's dash during final testing before the competition.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_091.png)

## 9.1 Review of Architecture

The modular architecture selected for the AMS design proved to be effective. Compared to previous years cars that the author was involved with, there was a significant improvement in the ease of assembling and testing the accumulator. By comparison, the cell carrier concept eliminated connection reliability related issues between the AMS and cells, including temperature monitoring connections.

The UCM24 team has begun adapting the design for a different accumulator configuration. The modular architecture has proved effective for this. Relying on CAN for communication between AMS has proved useful for debugging given the team's familiarity with the protocol due to it's extensive use in automotive applications.

## 9.2 Review of Hardware

The hardware design for the AMS has proved to be a robust design, however there is room for improvement in eliminating stand-by power consumption. This is owing to the choice of CAN for communication between AMS modules and the Accumulator Motherboard. Possible solutions to this will be given in Section 9.4. Use of the ESP32-C6 series could have eliminated significant complexity in the Accumulator Motherboard design, as it has two internal CAN controllers [60]. This would have removed the need for the SPI CAN controller.

## 9.3 Review of Algorithms

Estimating SoC via Coulomb Counting proved to be the most effective technique, and took the least development effort of any improvement made after the FSAE competition. However, open circuit voltage SoC estimation is viable for a first implementation, as it provides a valid estimate prior to driving and allows for a qualitative assessment of SoC after sitting at rest for a short period.

While the ECM system was able to identify IR during charging, the SoC estimates the ECM system produced were of minimal value, especially considering the development effort.

The SoH algorithm functions as expected. However, further development work is required to validate the accuracy of its results. Early results are promising, estimating a charge capacity consistently over multiple charges with the resulting capacity estimate being used by the Coulomb counting system's SoC estimation.

## 9.4 Recommendations

Implementing a modular BMS architecture is highly recommended for an FSAE accumulator. The modular architecture enables easy access to accumulator segments, allowing them to be integrated into the accumulator with minimal effort. This approach only requires installation of the CAN bus connections and maintenance connectors once a segment is placed in the accumulator container.

Utilising CAN does result in high standby current draw, however this approach is still recommended due to its BMIC agnostic approach. It fully decouples module design from motherboard design. That is, a module design with any BMIC or MCU can work with a given motherboard design so long as the software on both ends is written with an agreed CAN frame format. Additionally, the wide availability of CAN controller and transceiver ICs makes implementation of a CAN based design low cost and low effort, enabling rapid implementation. CAN systems are common in FSAE and this familiarity is an advantage of using a CAN based modular architecture.

To accommodate the high standby current of a CAN design, it is recommended to explore a design that has a means of disabling the input to the buck converter when the module is not being used. A possible means of doing this would be to have a signal line alongside the CAN bus which switches an optically isolated FET (a Photo-FET Optocoupler would be well suited for this). Alternatively, module power could be provided by the low-voltage system feed through DC-DC isolation transformers at each module.

Developing a code-base utilising a Real Time Operating System is recommended. This significantly reduces the design effort required to enable multiple concurrent algorithms. However, it is recommended to prioritise a basic implementation first that focuses on the MVP implementation.

Appendix F provides general recommendations beyond the scope of this thesis for FSAE teams.

## Appendix A: FSAE AMS Rules

Where appropriate, the proceeding list will present these rules verbatim. However, some rules are reworded to assist readers unfamiliar with other sections of the rules that are referenced.

## EV.8.3 - AMS Functionality Rules

EV.8.3.1 An Accumulator Management System must monitor the Accumulator Voltage and Temperature when the: Tractive System is Active, or the Accumulator is connected to a Charger.

EV.8.3.2 The AMS must have galvanic isolation at every segment to segment boundary, as approved in the ESF.

Context: An accumulator must be divided into segments no greater than 120V and 6MJ.

EV.8.3.3 Cell balancing is not permitted when the Shutdown Circuit is Open.

Context: The shutdown circuit is a car-wide system which allows/inhibits the HV output of the accumulator.

## EV.8.3.4 The AMS must monitor for:

- a. Voltage values outside the allowable range
- b. Voltage sense Overcurrent Protection device(s) blown or tripped
- c. Temperature values outside the allowable range
- d. Missing or interrupted voltage or temperature measurements
- e. A fault in the AMS

EV.8.3.5 If the AMS detects one or more of the conditions of EV.8.3.4 above, the AMS must: Open the Shutdown Circuit, and turn on the AMS Indicator Light.

Context: Opening the shutdown circuit will inhibit the HV output of the accumulator, disabling the car from driving.

EV.8.3.6 The AMS Indicator Light must be: Red, Visible to the driver, Marked "AMS" .

## EV.8.4 - Voltage Measurement Rules

EV.8.4.1 The AMS must measure the cell voltage of every cell. When single cells are directly connected in parallel, only one voltage measurement is needed.

Context: As in UCM23, a single ENEPAQ block consisting of parallel cells counts as "one cell" in the context of the AMS's voltage measurements.

EV.8.4.2 Cell Voltage levels must remain inside the allowed minimum and maximum cell voltage levels stated in the cell data sheet. Measurement accuracy must be considered.

EV.8.4.3 All voltage sense wires to the AMS must have Overcurrent Protection, or meet requirements for no Overcurrent Protection.

EV.8.4.4 When used, Overcurrent Protection for the AMS voltage sense wires must meet the following:

a. The Overcurrent Protection must occur in the conductor, wire or PCB trace which is directly connected to the cell tab.

b. The voltage rating of the Overcurrent Protection must be equal to or greater than the smaller of: The sum of the cell voltages sensed by the AMS board, or the sum of the cell voltages sensed between galvanic isolation boundaries on the cell board/AMS.

EV.8.4.5 Overcurrent Protection is not required on a voltage sense wire if all three of the following conditions are met: AMS is a distributed AMS system (one cell measurement per board), Sense wire length is &lt; 25 mm, AMS board has Overcurrent Protection.

Context: Overcurrent protection rules are written broadly to account for teams using Commercial Off The Shelf (COTS) BMS units with differing typologies.

## EV.8.5 - Accumulator Temperature Measurement Rules

EV.8.5.1 The AMS must measure the temperatures of critical points of the Accumulator.

EV.8.5.2 Temperatures (considering measurement accuracy) must remain below the lower of the two: The maximum cell temperature limit stated in the cell data sheet, or 60°C.

EV.8.5.3 Cell temperatures must be measured at the negative terminal of the respective cell.

EV.8.5.4 The temperature sensor used must be in direct contact with one of: The negative terminal itself, or the negative terminal busbar less than 10 mm away from the cell terminal.

EV.8.5.5 For lithium based cells, the temperature of a minimum of 20% of the cells must be monitored by the AMS. The monitored cells must be equally distributed inside the Accumulator Container. Every cell temperature should be monitored.

EV.8.5.6 Multiple cells may be monitored with one temperature sensor, if EV.8.5 is met for all cells sensed by the sensor.

EV.8.5.7 Temperature sensors must have appropriate electrical isolation that meets one of the two: Between the sensor and cell, or in the sensing circuit. The isolation must consider both GLV/TS isolation as well as common mode voltages between sense locations.

## Appendix B: AMS Module Schematics

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_092.png)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_093.png)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_094.png)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_095.png)

## Appendix C: Motherboard Schematic

X

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_096.png)

## Appendix D: Accumulator IO Schematic

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_097.png)

## Appendix E: UCM23 FSAE Australasia 2023

During the final week prior to the competition maximum emphasis was placed on testing time, building confidence in all the electrical systems and making setup changes in the warmer climate. Figure E.1 shows these testing sessions.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_098.png)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_099.png)

- (a) Team members enthusiastically checking car setup notes. (b) Swapping drivers during an en-
- durance test.

Figure E.1: Photos from the final test sessions in Melbourne.

## Tech Inspection

FSAE Australasia 2023 opened on the 14th of December, with the first day of tech inspection. By the afternoon of the 15th UCM23 had passed all stages of electrical tech inspection, and all mechanical stages except brake test. The following morning, UCM23 passed the brake test, the final tech inspection stage granting entry to the dynamic events. Figure E.2 shows various milestones of the tech inspection process.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_100.png)

Figure E.2: Photos from milestones in UCM23's tech inspection process at FSAE.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_101.png)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_102.png)

## First Dynamic Event Day

The skid-pad and acceleration events were held on the first day of dynamic events. Figure E.3 shows UCM23 competing in the skid-pad event, where it placed 3rd. This was followed by the acceleration event, with UCM23 shown in line for the event in Figure E.4. The accumulator was charged between events and can be seen on it's transportation kart in Figure E.5.

Figure E.3: Photos of UCM23 competing in the skid-pad event.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_103.png)

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_104.png)

Figure E.4: UCM23 in line for the acceleration event.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_105.png)

Figure E.5: UCM23's accumulator on its transport kart "the stance kart".

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_106.png)

## Second Dynamic Event Day

The second day of dynamic events had autocross scheduled in the morning and endurance in the afternoon. ICE events were scheduled between the two EV events to ensure teams had sufficient charging time. This would prove extremely valuable, as a previously not encountered electrical fault occurred with the car which required debugging and resolution.

With the electrical issue resolved, UCM23 immediately proceeded to the endurance event. The endurance event doubles as the efficiency event. So, considering the standing amongst the competition at that time, UCM opted to drive the full endurance in a manner to maximise efficiency. Completing the full length of the endurance event is a momentous occasion for any team. This was no exception for UCM, especially after UCM21's AMS triggered shutdown meters before the finish line in the previous year.

## Results

UCM23 attained 1st place overall in the EV class. For individual events, UCM achieved several podium results, placing 2nd in efficiency, 3rd in skid pad, 3rd in engineering design, and 3rd in endurance. As of writing, UCM sits 3rd in the FSAE EV world rankings as calculated by FS-world [1]. Figure E.6 shows the team with the car after completing the endurance event.

Figure E.6: UCM23 and a jubilant team after completing the endurance event, ending the 2023 FSAE Australasia competition.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_107.png)

## Appendix F: General Recommendations For FSAE Teams

This appendix is a subjective set of recommendations the author would give to a new FSAE team, or teams intending to switch to EV.

If you do not finish all of the events, you will not place well overall. It is difficult to understate the value of simplicity for achieving a reliable car. This applies at all levels of abstraction, from vehicle concept down to individual PCBs and components. This requires buy-in from everyone working on the design at each level. A healthy degree of scepticism on the success of a first implementation is required in combination with a confidence that sufficient testing and development time can overcome any initial issues.

Avoid design by committee. Productive and inclusive discussion for considering the right course of action is always a required, and these discussions must happen through the lens of maximising the probability of achieving high level objectives. However, clear direction is necessary and no perfect choices can be made. Failing to clearly move forward invalidates the effectiveness of any discussion. With excessive deliberation/analysis, eventually the difference in the effectiveness of two paths becomes outweighed by the lost opportunity to learn along the way of any of the available paths.

Establish high level goals early that align with your team's strength and current standing. Every team is different, and the goals must reflect your team's position and experience. Some examples of questions to ask when determining these are as follows. Is this the team's first or nth EV? Is the team comprised of students that have been heavily involved in prior years? Should development iterate on details from the previous car, targeting optimisation in the last few percent, or is a high-level reconsideration of the concept required? UCM23, shown in Figure F.1, is an example of the latter, focused large concept changes from previous years and with conservative implementation of detailed design.

The accumulator is the most significant "single" point of failure for an EV. While the accumulator is often considered an electrical part of the car, its mechanical design is crucial. A lot of electronics inevitably ends up in the accumulator to satisfy the FSAE rules, and how all of that is packaged into the accumulator container is often just as crucial to reliability as the electronics themselves. Consider how easily each electrical component can be accessed for trouble-shooting, as it will be unavoidable. Friction in the process of working through teething issues will prolong the process.

Figure F.1: UCM23 pictured at UCM's test site, during a test session validating improved AMS algorithms.

![Image](Univ%20Canterbury%20-%20BMS%20for%20FSAE%20Electric%20Racecar%20%28Robertson%20Thesis%29_files/img_108.png)

## References

- [1] Formula Student Germany GmbH. Formula Student - World Ranking Lists. [Online]. Available: https://fs-world.org/
- [2] M. Barham, "Design and development of the electrical systems in an electric formula SAE race car, " Master's thesis, University of Canterbury, 2017. [Online]. Available: https://ir.canterbury.ac.nz/items/cccfaa91-16e9-43dc-83cb-20fee49bb4c8
- [3] Elithion Inc, "Lithiumate Lithium-ion BMS Professional distributed Li-ion Battery Management System, " 2024. [Online]. Available: https://elithion.com/lithiumate. php
- [4] SAE International, "Formula SAE Rules 2023, " 2022. [Online]. Available: https://www.fsaeonline.com/cdsweb/gen/DocumentResources.aspx
- [5] A. Hughes, "Electric Motors and Drives: Fundamentals, Types and Applications". Elsevier Science &amp; Technology, 2005.
- [6] AMK, "motor data sheet DD5-14-10-POW - 18600-B5 - Formula Student, " 2018. [Online]. Available: https://www.amk-motion.com/amk-dokucd/dokucd/de/conten t/resources/pdf-dateien/fse/motor \_ data \_ sheet \_ a2370dd \_ dd5.pdf
- [7] Y. Gao, M. Ehsani, S. E. Gay, and A. Emadi, "Modern Electric, Hybrid Electric, and Fuel Cell Vehicles: Fundamentals, Theory, and Design". Boca Raton : CRC Press, 2005.
- [8] W. Xu, Permanent Magnet Synchronous Machines and Drives: Flux Weakening Advanced Control Techniques. Taylor &amp; Francis eBooks, 2023.
- [9] N. Mohan, T. Undeland, and W. Robbins, "Power Electronics: Converters, Applications, and Design". John Wiley &amp; Sons, Inc., 1995, ch. 1.
- [10] AMK, "AMK RACING KIT 4 wheel drive "Formula Student Electric" , " 2020. [Online]. Available: https://www.amk-motion.com/amk-dokucd/dokucd/en/conten t/resources/pdf-dateien/fse/r25/pdk \_ 205481 \_ kw26-s5-fse-4q\_ en \_ 2020-44 \_ .pdf
- [11] M. Gutiérrez and I. Careaga, "Which format do the major battery cell manufacturers bet on? prismatic, cylindrical or pouch?" 2022. [Online]. Available: https://cicenerg igune.com/en/blog/format-battery-cell-manufacturers-prismatic-cylindrical-pouch

- [12] "Electric vehicle (ev) battery market size, share &amp; industry analysis, by battery type (lithium-ion, lead acid, nickel metal hydride, and others), by vehicle type (battery electric vehicles, plug-in hybrid electric vehicles, and hybrid electric vehicles), and regional forecasts, 2024-2032, " 2024. [Online]. Available: https://www.fortunebusin essinsights.com/industry-reports/electric-vehicle-battery-market-101700
- [13] J. A. Sanguesa, V. Torres-Sanz, P. Garrido, F. J. Martinez, and J. M. Marquez-Barja, "A Review on Electric Vehicles: Technologies and Challenges, " Smart Cities, vol. 4, no. 1, pp. 372-404, 2021. [Online]. Available: https: //www.mdpi.com/2624-6511/4/1/22
- [14] M. Waseem, M. Ahmad, A. Parveen, and M. Suhaib, "Battery technologies and functionality of battery management system for EVs: Current status, key challenges, and future prospectives, " Journal of Power Sources, vol. 580, p. 233349, 2023. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S037 8775323007255
- [15] I. Dumé, "Lithium-ion batteries break energy density record, " Physics World, 2023.
- [16] R. M. Salgado, F. Danzi, J. E. Oliveira, A. El-Azab, P. P. Camanho, and M. H. Braga, "The Latest Trends in Electric Vehicles Batteries, " Molecules, vol. 26, no. 11, 2021. [Online]. Available: https://www.mdpi.com/1420-3049/26/11/3188
- [17] S. Dhameja, "Electric Vehicle Battery Systems". ScienceDirect, 2001.
- [18] J. Larminie and J. Lowry, Electric Vehicle Technology Explained. John Wiley &amp; Sons, Incorporated, 2012, pp. 30-31, 51.
- [19] H. Löbberding, S. Wessel, C. Offermanns, M. Kehrer, J. Rother, H. Heimes, and A. Kampker, "From cell to battery system in bevs: Analysis of system packing efficiency and cell types, " World Electric Vehicle Journal, vol. 11, no. 4, 2020. [Online]. Available: https://www.mdpi.com/2032-6653/11/4/77
- [20] D. Andrea, Battery management systems for large lithium-ion battery packs. Artech House, 2010, pp. 51, 64, 88-97.
- [21] S. Shahid and M. Agelin-Chaab, "A review of thermal runaway prevention and mitigation strategies for lithium-ion batteries, " Energy Conversion and Management: X, vol. 16, p. 100310, 2022. [Online]. Available: https: //doi.org/10.1016/j.ecmx.2022.100310

- [22] ENEPAQ, "Li-ion building block with Sony/Murata VTC5A datasheet, " 2023. [Online]. Available: https://enepaq.com/wp-content/uploads/2023/09/VTC5A-Son y-Murata-Li-ion-Battery-Module-With-Temperature-Sensor-Datasheet-Tesla-Bat tery-Sponsorship-Formula-SAE-Electric-Formula-Student-Battery-Pack.pdf
- [23] S. Yang, X. Liu, S. Li, and C. Zhang, Advanced Battery Management System for Electric Vehicles. Springer, 2023.
- [24] W. Waag, S. Käbitz, and D. U. Sauer, "Experimental investigation of the lithium-ion battery impedance characteristic at various conditions and aging states and its influence on the application, " Applied Energy, vol. 102, pp. 885-897, 2013, special Issue on Advances in sustainable biofuel production and use - XIX International Symposium on Alcohol Fuels - ISAF. [Online]. Available: https://doi.org/10.1016/j.apenergy.2012.09.030
- [25] D. W. Gao, Energy Storage for Sustainable Microgrid. Elsevier Science &amp; Technology, 2015, pp. 99-105.
- [26] Y. Cao, Y. Zhang, and C. Gu, Automated and Electric Vehicle: Design, Informatics and Sustainability. Springer, 2023, p. 35.
- [27] J. Chiasson and B. Vairamohan, "Estimating the state of charge of a battery, " IEEE Transactions on Control Systems Technology, vol. 13, no. 3, pp. 465-470, 2005.
- [28] W. -Y. Chang, M. Brünig, and E. Di Nardo, "The State of Charge Estimating Methods for Battery: A Review, " International Scholarly Research Notices, vol. 2013, 2013. [Online]. Available: https://doi.org/10.1155/2013/953792
- [29] L. Lu, X. Han, J. Li, J. Hua, and M. Ouyang, "A review on the key issues for lithium-ion battery management in electric vehicles, " Journal of Power Sources, vol. 226, pp. 272-288, 2013. [Online]. Available: https: //www.sciencedirect.com/science/article/pii/S0378775312016163
- [30] G. Vykunta Rao, M. Aruna Bharathi, S. Kumar, B. Murali, and V. Vykunta Rao, "Modular battery management system architecture for commercial vehicle applications, " Materials Today: Proceedings, vol. 92, pp. 1538-1543, 2023, 2nd International Conference on Multifunctional Materials. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S2214785323033953
- [31] G. Pistoia, Lithium-Ion Batteries - Advances and Applications. Elsevier, 2014, pp. 129-132, 136-138.

- [32] Y. Barsukov, "Battery Cell Balancing: What to Balance and How, " Technical Report; Texas Instruments, 2023. [Online]. Available: https://www.ti.com/downloa d/trng/docs/seminar/Topic%202%20-%20Battery%20Cell%20Balancing%20-%20 What%20to%20Balance%20and%20How.pdf
- [33] U. K. Das, P. Shrivastava, K. S. Tey, M. Y. I. Bin Idris, S. Mekhilef, E. Jamei, M. Seyedmahmoudian, and A. Stojcevski, "Advancement of lithiumion battery cells voltage equalization techniques: A review, " Renewable and Sustainable Energy Reviews, vol. 134, 2020. [Online]. Available: https: //www.scopus.com/inward/record.uri?eid=2-s2.0-85090402533&amp;doi=10.1016%2fj.r ser.2020.110227&amp;partnerID=40&amp;md5=af562f7decd9c8441dad5b34f3743cbd
- [34] W. Liu, T. Placke, and K. Chau, "Overview of batteries and battery management for electric vehicles, " Energy Reports, vol. 8, pp. 4058-4084, 2022. [Online]. Available: https://www.sciencedirect.com/science/article/pii/S2352484722005716
- [35] M. D. Natale, H. Zeng, P. Giusto, and A. Ghosal, Understanding and Using the Controller Area Network Communication Protocol. Springer, 2012.
- [36] P. Richards, "A CAN Physical Layer Discussion, " Microchip Technology Inc., Tech. Rep., 2002. [Online]. Available: https://ww1.microchip.com/downloads/en/appno tes/00228a.pdf
- [37] I. 11898-2" , "Road vehicles - Controller area network (CAN) - Part 2: High-speed physical medium attachment (PMA) sublayer, ISO 11898-2:2024, " International Organization for Standardization, Geneva, Standard, 2024. [Online]. Available: https://www.iso.org/obp/ui/en/#iso:std:85120:en
- [38] ENEPAQ, "Battery modules, " 2024. [Online]. Available: https://enepaq.com/produ ct-category/battery-modules/
- [39] Analog Devices, "LTC6811-1/LTC6811-2: 12-Cell Battery Stack Monitors Data Sheet (Rev.C). " [Online]. Available: https://www.analog.com/media/en/technica l-documentation/data-sheets/LTC6811-1-6811-2.pdf
- [40] LEM, "Current Transducer HAIS 50 .. 400-P HAIS 50 .. 150-TP, " 2014. [Online]. Available: https://www.lem.com/sites/default/files/products \_ datasheets/hais \_ 50 \_ 400-p\_ and \_ 50 \_ 150-tp.pdf
- [41] Espressif, "ESP32, " 2024. [Online]. Available: https://www.espressif.com/en/produ cts/socs/esp32

- [42] Espressif, "Esptool.py Documentation, " 2024. [Online]. Available: https: //docs.espressif.com/projects/esptool/en/latest/esp32/
- [43] Espressif, "Esptool.py Documentation - Boot Mode Selection, " 2024. [Online]. Available: https://docs.espressif.com/projects/esptool/en/latest/esp32/advanced-t opics/boot-mode-selection.html
- [44] Espressif, "ESP32 \_ DevKitc \_ V4, " 2018. [Online]. Available: https://dl.espressif.c om/dl/schematics/esp32 \_ devkitc \_ v4-sch-20180607a.pdf
- [45] Advanced Monolithic Systems, "AMS1117 1A Low Dropout Voltage Regulator. " [Online]. Available: http://www.advanced-monolithic.com/pdf/ds1117.pdf
- [46] Espressif, "ESP32-WROOM-32D &amp; ESP32-WROOM-32U Datasheet, " 2023. [Online]. Available: https://www.espressif.com/sites/default/files/documentation/e sp32-wroom-32d \_ esp32-wroom-32u \_ datasheet \_ en.pdf
- [47] Espressif, "ESP32 Series Datasheet, " 2024. [Online]. Available: https://www.espres sif.com/sites/default/files/documentation/esp32 \_ datasheet \_ en.pdf
- [48] NXP Semiconductors, "TJA1052i Galvanically isolated high-speed CAN transceiver Product data sheet. " 2018. [Online]. Available: https://www.nxp.com/docs/en/da ta-sheet/TJA1052I.pdf
- [49] Texas Instruments, "WEBENCH-CIRCUIT-DESIGNER. " [Online]. Available: https://www.ti.com/tool/WEBENCH-CIRCUIT-DESIGNER
- [50] MORNSUN, "DC/DC Converter B \_ S-1WR3 Series. " [Online]. Available: https: //www.mornsun-power.com/html/pdf/B0305S-1WR3.html
- [51] Frank Schade and Matthias Muth, "Application Hints - TJA1052i Galvanic Isolated High Speed CAN Transceiver, " 2014. [Online]. Available: https://www.nxp.com/do cs/en/supporting-information/AH1301 \_ Application \_ Hints \_ TJA1052i.pdf
- [52] Murata Power Solutios, "CRE1 | Datasheet | Isolated 1W Single Output Isolated DC-DC Converters | Murata Power Solutions. " [Online]. Available: https://www.murata.com/products/productdata/8807029407774/kdc-cre1.pdf
- [53] PlatformIO, "What is PlatformIO?" 2024. [Online]. Available: https://docs.platfor mio.org/en/latest/what-is-platformio.html
- [54] Espressif, "ESP-IDF Programming Guide - Two-Wire Automotive Interface (TWAI), " 2024. [Online]. Available: https://docs.espressif.com/projects/esp-idf/e n/stable/esp32/api-reference/peripherals/twai.html

- [55] Texas Instruments, "LMR16006 SIMPLE SWITCHER 60 V 0.6 A Buck Regulators With High Efficiency ECO Mode datasheet, " 2014. [Online]. Available: https://www.ti.com/lit/ds/symlink/lmr16006.pdf
- [56] M. Messing, T. Shoa, and S. Habibi, "Lithium-Ion Battery Relaxation Effects, " Cadex Electronics and McMaster University, Tech. Rep., 2004. [Online]. Available: https://www.cadex.com/\_ content/li-Ion \_ battery\_ relaxation.pdf
- [57] "Sony US18650VTC5A 2600mAh (Green), " 2024. [Online]. Available: https: //lygte-info.dk/review/batteries2012/Sony%20US18650VTC5A%202600mAh%20 (Green)%20UK.html
- [58] R. Barry, "Mastering the FreeRTOS Real Time Kernel". Real Time Engineers Ltd, 2016.
- [59] E. Gamma, J. Vlissides, R. Helm, and R. Johnson, Design patterns : elements of reusable object-oriented software. Addison-Wesley, 1994.
- [60] Espressif, "ESP32-C6 Series Datasheet, " 2024. [Online]. Available: https://www.es pressif.com/sites/default/files/documentation/esp32-c6 \_ datasheet \_ en.pdf
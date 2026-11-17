<!-- Converted from FEUP Porto - BMS for FS Electric Vehicle (Teixeira Thesis 2024).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

## FACULDADE DE ENGENHARIA DA UNIVERSIDADE DO PORTO

## Development of a Battery management system for electric vehicles applied to formula student

Francisco Oliveira Amorim Plácido Teixeira

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_001.png)

Master in Eletrical and Computer Engeneering

Supervisor: Prof. Agostinho Afonso da Rocha

## Resumo

Esta dissertação explora o projeto e implementação de um Sistema de Gestão de Bateria (BMS) para o veículo elétrico (VE) da Formula Student FEUP (FSFEUP), abordando o crescente relevo global em soluções de transporte sustentáveis e a crescente proeminência dos VEs no desporto automóvel. O projeto é motivado pela necessidade de melhorar o desempenho, eficiência e segurança de carros de corrida elétricos, particularmente no contexto da competição Formula Student.

Utilizando uma abordagem de engenharia de sistemas baseada em modelos de simulação (MBSE) com recurso ao MATLAB como principal ferramenta de projeto, este trabalho centra-se no desenvolvimento de um BMS que não só é adaptado aos requisitos únicos do VE da FSFEUP e às regras da FS, como também apresenta características de uma solução descentralizada, versátil, fiável e escalável, tornando-o adaptável a futuros projetos da FSFEUP.

Este projeto inicia-se com uma investigação abrangente sobre as tecnologias de gestão de baterias existentes e as soluções disponíveis. Um objetivo principal é abordar e ultrapassar as limitações apresentadas pelo BMS comercial standard atualmente utilizado pela equipa. O trabalho desenvolvido foca-se em vários avanços: estimação precisa do Estado de Carga (SOC), um modelo de bateria híbrido versátil, adaptável a diferentes células e facilitado por uma interface de utilizador (IU) personalizada para parametrização automática, mecanismos de controlo de balanceamento de células mais precisos em comparação com a solução atual, limites de controlo de corrente dinâmicos adaptáveis aos variados cenários encontrados em eventos da Formula Student, um sistema completo de diagnóstico do veículo que oferece informações mais detalhadas em comparação com o BMS existente, e uma IU intuitiva que permite aos utilizadores adaptar os parâmetros do BMS e as condições ambientais específicas.

Além destes avanços técnicos, esta dissertação realça o cumprimento bem-sucedido dos objetivos do projeto e do produto, em alinhamento com os requisitos SYS2 definidos. Sáo também dadas recomendações para futuras pesquisas e desenvolvimentos no campo da tecnologia BMS, particularmente no contexto da continuação deste projeto.

Palavras-Chave: Sistema de gestão de bateria, Formula Student, Veículo elétrico, Baterias de iões de lítio, Engenharia de sistemas, Modelo de bateria

## Abstract

This dissertation explores the design and implementation of a Battery Management System (BMS) for the Formula Student FEUP (FSFEUP) electric vehicle (EV), addressing the growing global emphasis on sustainable transportation solutions and the increasing prominence of EVs in motorsport. The project is motivated by the need to enhance the performance, efficiency, and safety of electric race cars, particularly within the context of the Formula Student competition.

Employing a model based systems engineering (MBSE) approach with MATLAB as the primary tool for design and simulation, this work focuses on developing a BMS that is not only tailored to the unique requirements of the FSFEUP EV and FS rules, but also presents characteristics of a decentralized, versatile, reliable, and scalable solution, making it adaptable to future FSFEUP designs.

This project commences with a comprehensive investigation into existing battery management technologies and available solutions. A primary objective is to address and overcome the limitations presented by the team's current off-the-shelf BMS. The work developed focuses on several key advancements: accurate State of Charge (SOC) estimation, a versatile hybrid battery model adaptable to different cells facilitated by a custom-developed user interface (UI) for automatic parameterization, precise cell balancing control mechanisms compared to the current solution, dynamic current control limits adaptable to the varied scenarios encountered in Formula Student events, a complete vehicle diagnostics system offering deeper insights compared to the existing BMS, and a user-friendly UI allowing users to adapt BMS parameters and specific environmental conditions.

In addition to these technical achievements, this dissertation underscores the successful fulfillment of project and product objectives, in alignment with the SYS2 requirements defined. It also provides valuable insights and recommendations for future research and development in the field of BMS technology, particularly within the context of the continuation of this project.

Key Words: Battery management system, Formula Student, Electric Vehicle, Lithium Ion Batteries, System Engineering, Battery Model

## United Nations' Sustainable Development Goals (SDGs)

In 2015, all United Nations Member States adopted the 2030 Agenda for Sustainable Development, a plan to address global challenges and promote sustainable practices worldwide [1]. At the core of this agenda are the 17 Sustainable Development Goals (SDGs), which call for collective action to eradicate poverty, protect the planet, and ensure prosperity for all by 2030. This thesis aligns with several of these goals through its focus on developing a BMS for electric vehicles.

A BMS is essential for the safe and efficient operation of electric vehicles, contributing significantly to multiple SDGs:

SDG 7: Affordable and Clean Energy - By improving the performance and lifespan of batteries in electric vehicles, this research promotes the use of clean energy sources in the transportation sector, reducing greenhouse gas emissions and contributing to a more sustainable energy system.

SDG 11: Sustainable Cities and Communities - Efficient BMS technologies are crucial for the widespread adoption of electric vehicles, which can significantly improve air quality and reduce noise pollution in urban areas. This project supports the transition to sustainable transportation, making cities and communities healthier and more habitable.

SDG 12: Responsible Consumption and Production - The focus on extending battery lifespan and optimizing battery usage through advanced BMS algorithms aligns with the principles of responsible consumption and production. By maximizing resource utilization and minimizing waste, this project contributes to a more circular and sustainable economy.

SDG 13: Climate Action - The transportation sector is a major source of greenhouse gas emissions. By enabling the development and adoption of electric vehicles, efficient BMS technologies directly support climate action goals and help mitigate the adverse effects of climate change.

Table 1 summarizes the project's contribution to the SDGs.The table details how the project addresses specific targets within each relevant SDG, showcasing its impact across several areas.

Table 1: Contribution of the Project to SDGs

| SDG | Target | How this project impacts: |
| - | - | - |
| 7 | 7.1 | Enhances access to affordable and clean energy by developing a BMS that boosts electric vehicle performance and efficiency. |
| 7 | 7.2 | Supports the shift to renewable energy in transportation by facilitating electric vehicle adoption with improved battery management. |
| 7 | 7.3 | Increases energy efficiency in transport through optimized battery usage and extended lifespan via innovative BMS algorithms. |
| 7 | 7.a | Fosters international collaboration on clean energy by advancing BMS tech- nologies for electric vehicles. |
| 11 | 11.2 | Improves access to reliable and eco-friendly transport by enhancing electric vehicle performance, which contributes to road safety and broader availabil- ity. |
| 12 | 12.2 | Promotes efficient natural resource use by extending battery life through en- hanced management and efficiency. |
| 12 | 12.5 | Aids battery recycling efforts by providing data that supports effective recy- cling practices through longer-lasting batteries. |
| 12 | 12.a | Supports advancements in sustainable production and consumption with cutting-edge battery management technology. |
| 13 | 13.1 | Builds resilience to climate extremes by ensuring battery systems perform reliably in diverse conditions. |
| 13 | 13.2 | Contributes to climate resilience strategies by offering data on battery tech- nologies that help reduce carbon footprints. |
| 13 | 13.3 | Enhances understanding of sustainable energy by showcasing the impact of BMS technology on climate change mitigation and energy efficiency. |

.

## Acknowledgments

I would like to begin by expressing my gratitude to my supervisor, Professor Agostinho Afonso da Rocha, for his continuous availability and support throughout this work.

I also extend my sincere gratitude to Xelerate for providing all the necessary conditions for this project, particularly to Daniel Magalhães, my supervisor at the company, for his patience, invaluable guidance, and prior work on the subject.

A heartfelt thank you goes to my parents, Ana and Artur, and to my siblings, Zé, João, and Pipa, for their patience and support not only during this phase of the dissertation but throughout my entire journey.

Finally, I must also thank the rest of my family and friends who have been present throughout this journey.

To all of you, A big thank you!

Francisco Teixeira

" Life is the most brutal endurance sport of all time! "

David Goggins

## Contents

| 1 Introduction | 1 Introduction | 1 Introduction | 1 |
| - | - | - | - |
| 1.1 | Problem and Context definition . | . . . . . . . . . . . . | . . . . . . . . . . . . . . 1 |
|  | 1.1.1 | Formula Student FEUP context . . . . . . . . | . . . . . . . . . . . . . . 2 |
|  | 1.1.2 | Xelerate digitalcar context . . . . . . . . . . . | . . . . . . . . . . . . . . 3 |
| 1.2 | Project scope | . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 4 |
| 1.3 | Product objectives . . | . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 4 |
| 1.4 | Structure of the thesis . . | . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 5 |
| 2 State of the art | 2 State of the art | 2 State of the art | 7 |
| 2.1 | Historical background . . . | . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 7 |
| 2.2 | Battery fundamentals . . | . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 8 |
|  | 2.2.1 | Batteries characteristics . . . . . . . . . . . . | . . . . . . . . . . . . . . 8 |
|  | 2.2.2 | Battery parameters . . . . . . . . . . . . . | . . . . . . . . . . . . . . 10 |
| 2.3 | . . Battery management system (BMS) | . . . . . . . . . . | . . . . . . . . . . . . . . 11 |
|  | 2.3.1 | Lithium-Ion (Li-Ion) BMS . . . . . . . . . . . | . . . . . . . . . . . . . . 12 |
|  | 2.3.2 | BMS components and functions . . . . . . . . | . . . . . . . . . . . . . . 13 |
| 2.4 | BMS topology . . . | . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 14 |
|  | 2.4.1 | Distributed topology . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 15 |
|  | 2.4.2 | Non-distributed topology . . . . . . . . . . . . | . . . . . . . . . . . . . . 15 |
|  | 2.4.3 | Hybrid architecture . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 17 |
|  | 2.4.4 | Topologies comparison . . . . . . . . . . . . . | . . . . . . . . . . . . . . 18 |
| 2.5 | BMS features . . | . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 18 |
| 2.6 | Cell balancing . . . . . . . . . . . | . . . . . . . . . . . | . . . . . . . . . . . . . . 19 |
|  | 2.6.1 | Passive balance method . . . . . . . Active balance method . . . . . . . . . . . . . | 20 . . . . . . . . . . . . . . |
|  | 2.6.2 |  | 21 |
|  | 2.6.3 | Methods comparison . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 23 |
|  | 2.6.4 | Balancing control variable . . . . . . . . . . . | . . . . . . . . . . . . . . 23 |
| 2.7 | State estimation methods . | . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 25 |
|  | 2.7.1 | State of Charge (SOC) estimation . . . . . . . | . . . . . . . . . . . . . . 26 |
|  | 2.7.2 | State of Health (SOH) estimation . . . . . . . | . . . . . . . . . . . . . . 29 |
|  | 2.7.3 | Battery model . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 32 |
| 2.8 | Charging and discharging control . . | . . . . . . . . . . | . . . . . . . . . . . . . . 36 |
|  | 2.8.1 | Charging control . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 37 |
|  | 2.8.2 | Discharging control . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 37 |
|  | 2.8.3 | Advanced Control Methods . . . . . . . . . . | . . . . . . . . . . . . . . 38 |
| 2.9 | Fault diagnosis . . | . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 38 |
|  | 2.9.1 | Fault parameters . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 39 |
|  | 2.9.2 | Fault methods . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . . 40 |

|  | 2.10 Integrated circuits (ICs) market | . . . . . . . . . . . . . . | . . . . . . . . . . . . . 40 |
| - | - | - | - |
|  | 2.11 BMS within formula student . | . . . . . . . . . . . . . . | . . . . . . . . . . . . . 41 |
|  | 2.12 Final remarks . | . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 42 |
| 3 | Methodology and Proposed solution description | Methodology and Proposed solution description | 43 |
| 3.1 | Methodology . . . . . | . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 43 |
|  | 3.1.1 | Automotive SPICE (ASPICE) . . . . . . . . . . | . . . . . . . . . . . . . 43 |
|  | 3.1.2 | Tools . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 47 |
|  | 3.2 Previous | BMS analysis . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 48 |
| 3.3 | New BMS configuration . | . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 49 |
| 4 Battery | Modelling and Simulation | Modelling and Simulation | 51 |
|  | Battery modelling | Battery modelling |  |
|  | 4.1 | . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 51 |
|  | 4.1.1 | Simulink battery block parametrization . . . . . | . . . . . . . . . . . . . 51 |
|  | 4.1.2 | Battery model description . . . . . . . . . . . . | . . . . . . . . . . . . . 59 |
|  | 4.2 User | Interface (UI) for battery parametrization . . . . . . | . . . . . . . . . . . . . 68 |
|  | 4.2.1 | UI inputs . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 68 |
|  | 4.2.2 | UI outputs . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 68 |
|  | 4.2.3 | Final remarks . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 70 |
| 5 | Model based simulation | Model based simulation | 72 |
| 5.1 | Model based architecture . | . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 72 |
| 5.2 | BMS slave block . . | . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 72 |
| 5.3 | BMS master block . . . | . . . . . . . . . . . | . . . . . . . . . . . . . 73 |
|  | . . . . . . | . . . . . . |  |
|  | 5.3.1 | Cell power loss representation . . . . . . . . . . | . . . . . . . . . . . . . 73 |
|  | 5.3.2 5.3.3 | Battery model block . . . . . . . . . . . . . . . Critical Voltage and Temperature Calculation Blocks | 74 . . . . . . . . . . . 76 |
|  | 5.3.4 | Cell balancing command control . . . . . . . . . | . . . . . . . . . . . . . 77 |
|  | 5.3.5 | Internal resistance estimation . . . . . . . . . . . | . . . . . . . . . . . . . 83 |
|  | 5.3.6 | Current control algorithm . . . . . . . . . . . . | . . . . . . . . . . . . . 83 |
|  | 5.3.7 | Fault Diagnosis . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 91 |
|  | 5.3.8 | Communication Block . . . . . . . . . . . . . . | . . . . . . . . . . . . . 93 |
| 5.4 | User | Interface . . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 94 |
| 5.5 | Final remarks . . . . . . . | . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 95 |
| Conclusions | Work | Work |  |
| 6 | and Future | and Future | 96 |
|  | 6.1 | Satisfaction of objectives . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 96 |
|  | 6.2 Future work . . | . . . . . . . . . . . . . . . . . . . . . . | . . . . . . . . . . . . . 97 |
| A | Cell Datasheet | Cell Datasheet | 104 |

## List of Figures

| 1.1 | Chart points distribution of formula student events . . . . . . . . . . . . . . . . | . 3 |
| - | - | - |
| 1.2 | FSFEUP 2024 team members . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 4 |
| 1.3 | FSFEUP01 car, team´s first ever prototype . . . . . . . . . . . . . . . . . . . . | . 4 |
| 2.1 | Annual demand forecast for EVs . . . . . . . . . . . . . . . . . . . . . . . . . | . 8 |
| 2.2 | Basic structure of a Li-ion cell and representation of the electrochemical reactions occurring during discharge and charge . . . . . . . . . . . . . . . . . . . . . . | . 9 |
| 2.3 | Comparison of characteristics of different batteries chemistries . . . . . . . . . | . 10 |
| 2.4 | General architecture of an electric vehicle . . . . . . . . . . . . . . . . . . . . | . 11 |
| 2.5 | Li-ion cell formats:(a) cylindrical, (b) prismatic, and, (c) pouch . . . . . . . . . | . 12 |
| 2.6 | Li-ion chemistries and respective specific capacity . . . . . . . . . . . . . . . . | . 12 |
| 2.7 | Generic TSAC block diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 13 |
| 2.8 | BMS different topologies . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 14 |
| 2.9 | Control networks of BMS topologies:(a) centralized; (b) decentralized (modular and master-slave topologies), and (c) distributed . . . . . . . . . . . . . . . . . | . 15 |
| 2.10 | Distributed BMS topology adapted . . . . . . . . . . . . . . . . . . . . . . . . | . 15 |
| 2.11 | Centralized BMS topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 16 |
| 2.12 | Modular BMS topology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 17 |
| 2.13 | Master Slave BMS topology . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 17 |
| 2.14 | FST hybrid BMS architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 18 |
| 2.15 | BMS main functionalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 19 |
| 2.16 | Causes of cell unbalance and effect on performance . . . . . . . . . . . . . . . | . 19 |
| 2.17 | The impact of the SOC imbalance on 4-cell battery pack during charging and discharging scenarios . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 20 |
| 2.18 | Resume diagram of cell balancing topologies based on the electronic component used . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 20 |
| 2.19 | Switched shunt resistor passive balancing circuit . . . . . . . . . . . . . . . . . | . 21 |
| 2.20 | Fixed shunt resistor passive balancing circuit . . . . . . . . . . . . . . . . . . | . 21 |
| 2.21 | Fixed shunt resistor passive balancing circuit with the Zener diode . . . . . . . | . 21 |
| 2.22 | Active topologies from left to right: double tiered switch capacitor, multi-inductor, single winding transformer, and Buck-Boost converter . . . . . . . . . . . . . | . 23 |
| 2.23 | SOC and SOH effects of a battery . . . . . . . . . . . . . . . . . . . . . . . . | . 25 |
| 2.24 | Flowchart of OCV-SOC estimation method . . . . . . . . . . . . . . . . . . . | . 27 |
| 2.25 | Typical OCV-SOC curve . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 27 |
| 2.26 | Diagram of SOC estimation method based on battery model with filter appliance | 27 |
| 2.27 | Neural network for SOC estimation . . . . . . . . . . . . . . . . . . . . . . . | . 29 |
| 2.28 | Cycle characteristics from Molicel model INR-18650-P28A with different current discharge conditions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . 30 |

| 2.29 | Battery voltage dynamics under charge/discharge current pulses . . . . . . . | . . 31 |
| - | - | - |
| 2.30 | Different types of battery models . . . . . . . . . . . . . . . . . . . . . . . . | . . 32 |
| 2.31 | (a) - Rint model; (b) - Thevenin model; (c) - DP model . . . . . . . . . . . . | . . 35 |
| 2.32 | Conceptual illustration of the Kibam . . . . . . . . . . . . . . . . . . . . . . | . . 35 |
| 2.33 | Hybrid model fusing Kibam and Rint model | . . 36 |
| 2.34 | . . . . . . . . . . . . . . . . . . CC-CV charging characteristics of Molicel model INR-18650-P28A cell at differ- ent C-rates . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . 37 |
| 2.35 | A schematic of fault diagnosis in the BMS . . . . . . . . . . . . . . . . . . . | . . 39 |
| 3.1 | V-model process for BMS development . . . . . . . . . . . . . . . . . . . . | . . 44 |
| 3.2 | System architecture of the TSAC internal and external interactions . . . . . . | . . 46 |
| 3.3 | TSAC (a) and Orion BMS block diagram (b) in the FSFEUP01 vehicle . . . . | . . 48 |
| 3.4 | Orion BMS SWOT analysis . . . . . . . . . . . . . . . . . . . . . . . . . . | . . 50 |
| 3.5 | Proposed BMS architecture . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . 50 |
| 4.1 | Datasheet battery block from Simulink . . . . . . . . . . . . . . . . . . . . . | . . 51 |
| 4.2 | Battery model used by the Simulink battery block . . . . . . . . . . . . . . . | . . 52 |
| 4.3 | Discharge rate characteristics graph from cell datasheet . . . . . . . . . . . . | . . 53 |
| 4.4 | Heuristic flowchart for the electric model parametrization process . . . . . . | . . 54 |
| 4.5 | Comparison of fitting plot and the plot extracted from datasheet . . . . . . . | . . 55 |
| 4.6 | Comparison of the plotted datasheet curve and the Simulink simulation curve discharge with 2.8 A . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | - . . 56 |
| 4.7 | Discharge rate characteristics graph from Matlab with C=2.8 Ah . . . . . . . | . . 57 |
| 4.8 | Discharge rate characteristics graph from Matlab with C=2.846 Ah . . . . . . | . . 58 |
| 4.9 | CC-CV charging current calculation . . . . . . . . . . . . . . . . . . . . . . | . . 58 |
| 4.10 | CC-CV charge characteristics from Matlab . . . . . . . . . . . . . . . . . . | . . 59 |
| 4.11 | CC-CV charge characteristics adapted from from cell datasheet . . . . . . . . | . . 59 |
| 4.12 | Hybrid battery model representation . . . . . . . . . . . . . . . . . . . . . . | . . 59 |
| 4.13 | Kibam model simulation results . . . . . . . . . . . . . . . . . . . . . . . . | . . 61 |
| 4.14 | Kibam model simulation results obtained from the experiment . . . . . . . . | . . 61 |
| 4.15 | Heuristic flowchart for the Kibam model parametrization process . . . . . . . | . . 62 |
| 4.16 | Sampled values and the resulting curve fitting by the Voc function . . . . . . . | . . 64 |
| 4.17 | Comparison of Hybrid Model and Datasheet for various discharge currents . . rate characteristics of Hybrid model with available SOC=0% as | . . 65 |
| 4.18 | Discharge stop- page condition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . 66 |
| 4.19 | Difference of error between stopping by voltage and SOC . . . . . . . . . . . | . . 67 |
| 4.20 | User interface in work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | . . 70 |
| 5.1 | Simulink block modeling the relationship between cell current and temperature | . 74 |
| 5.2 | Demonstration of current influence on temperature during a discharge test . . | . . 74 |
| 5.3 | Battery model block implemented in Simulink for the lowest SOC cell . . . . | . . 75 |
| 5.4 | Sampled values and the resulting curve fitting by the SOCinit function . . . . . | . . 76 |
| 5.5 | Maximum and Minimum Value Blocks for Voltage (a) and Temperature (b) . . | . . 77 . . |
| 5.6 5.7 | Cell Balance Control Block (a) and Flowchart (b) . . . . . . . . . . . . . . Comparative analysis during -6 A constant current charging: (a) Voltage compar- ison of cells with different Rint, (b) SOC comparison of cells with different Rint, and (c) Balance command comparison between the proposed control method the commercial BMS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 78 79 |

| 5.8 | Comparative analysis during -2.8 A constant current charging: (a) Voltage com- parison of cells with different Rint, (b) SOC comparison of cells with different Rint, and (c) Balance command comparison between the proposed control method and the commercial BMS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 80 |
| - | - | - |
| 5.9 | Comparative analysis during -0.5 A constant current charging: (a) Voltage com- parison of cells with different Rint, (b) SOC comparison of cells with different Rint, and (c) Balance command comparison between the proposed control method and the commercial BMS. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 80 |
| 5.10 | Passive balance circuit of the cell, adapted from Figure 2.19 . . . . . . . . . . . | 81 |
| 5.11 | First balancing test: (a) Delta SOC and balance command. (b) Max SOC and min cell SOC during charging (c) Voltage of the cell and current of balance. . . . . . | 82 |
| 5.12 | Second balancing test: (a) Delta SOC and balance command. (b) Max SOC and min cell SOC during charging. (c) Voltage of the cell and current of balance. . . . | 82 |
| 5.13 | Current control with voltage algorithm: (a) Open circuit voltage (V), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh). . . . . | 84 |
| 5.14 | Current control with temperature algorithm: (a) Temperature (ºC), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh). . . . . | 85 |
| 5.15 | Current control with voltage algorithm and temperature influence: (a) Tempera- ture (ºC), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 86 |
| 5.16 | Current control with DeltaSOC algorithm for endurance events: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) Charge extracted during dis- charge (mAh). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 87 |
| 5.17 | Current control with DeltaSOC algorithm for acceleration events: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) Charge extracted during dis- charge (mAh). . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 87 |
| 5.18 | Current control with all control algorithms: (a) Current limit (A) and Fault sig- nal values; (b) Control parameters: DeltaSOC (%), Open circuit voltage (V), and Temperature (ºC); (c) Charge extracted during discharge (mAh). . . . . . . . . . | 88 |
| 5.19 | Current control with voltage algorithm: (a) Open circuit voltage (V), Current limit (A), and Fault signal values; (b) SOC of the battery pack (%). . . . . . . . . . . . | 89 |
| 5.20 | Current control with temperature algorithm: (a) Temperature (ºC), Current limit (A), and Fault signal values; (b) SOC of the battery pack(%). . . . . . . . . . . . | 89 |
| 5.21 | Current control with voltage algorithm and temperature influence: (a) Temperature (ºC), Current limit (A), and Fault signal values; (b) SOC of the battery pack(%). . | 90 |
| 5.22 | Current control with DeltaSOC algorithm: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) SOC of the battery pack (%). . . . . . . . . . . . . . | 90 |
| 5.23 | Current control with DeltaSOC algorithm: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) SOC of the battery pack (%). . . . . . . . . . . . . . | 91 |
| 5.24 | Current control with all control algorithms: (a) Current limit (A) and Fault sig- nal values; (b) Control parameters: DeltaSOC (%), Open circuit voltage (V), and pack (%). . . . . . . . . . . . . . . . | 92 |
| 5.25 | Temperature (ºC); (c) SOC of the battery . BMS Communication diagram . . . . . . . . . . . . . . . . . . . . . . . . . . . | 94 |
| 5.26 | User interface during (a) discharge and (b) charge scenarios. . . . . . . . . . . . | 95 |
| A.1 | Molicel model INR-18650-P28A . . . . . . . . . . . . . . . . . . . . . . . . . . | 104 |

## List of Tables

| 1 | Contribution of the Project to SDGs . . . . . . . . . . . . . . . . . . . . . . . . | iv |
| - | - | - |
| 2.1 | Comparison of BMS Topologies . . . . . . . . . . . . . . . . . . . . . . . . . . | 18 |
| 2.2 | Comparison of cell balancing methods . . . . . . . . . . . . . . . . . . . . . . . | 23 |
| 2.3 | Comparison of balancing control variables . . . . . . . . . . . . . . . . . . . . . | 25 |
| 2.4 | Comparison of SOC estimation methods . . . . . . . . . . . . . . . . . . . . . . | 29 |
| 2.5 | Comparison of SOH estimation methods . . . . . . . . . . . . . . . . . . . . . . | 32 |
| 2.6 | Comparison of BMS ICs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 41 |
| 2.7 | Comparison of BMS systems across different universities . . . . . . . . . . . . . | 42 |
| 3.1 | Summary of SYS2 requirements for BMS development . . . . . . . . . . . . . . | 45 |
| 4.1 | Molicel model INR-18650-P28A datasheet cell characteristics . . . . . . . . . . | 53 |
| 4.2 | Coefficients obtained in the fitting of Equation 4.7 . . . . . . . . . . . . . . . . . | 55 |
| 4.3 | Errors between curves presented in 4.5 . . . . . . . . . . . . . . . . . . . . . . . | 55 |
| 4.4 | Errors between curves presented in 4.6 . . . . . . . . . . . . . . . . . . . . . . . | 56 |
| 4.5 | Comparison of charge extracted of the block used in the Simulink discharge sim- ulation, with C=2.8 Ah, with the values extracted from the datasheet . . . . . . . | 57 |
| 4.6 | Comparison of charge extracted of the block used in the Simulink discharge sim- ulation with C=2.846 Ah with the values extracted from the datasheet . . . . . . | 58 |
| 4.7 | Parameters for the Kibam . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 61 |
| 4.8 | Comparison of discharge time of the block used in the Simulink simulation and the Kibam model parameterized with the values extracted from the datasheet . . . | 62 |
| 4.9 | Relative errors in discharge times of the Simulink block and Kibam model com- pared to the datasheet . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| 4.10 | Goodness of Fit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 63 |
| 4.11 | Coefficients obtained in the fitting of 4.16 . . . . . . . . . . . . . . . . . . . . . | 64 |
| 4.12 | Comparison of charge extracted of the hybrid model with stopping condition of Vout=2.5 V with the datasheet values . . . . . . . . . . . . . . . . . . . . . . . . | 65 |
| 4.13 | Comparison of relative error between the hybrid model and datasheet values pre- sented in Table 4.12 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 66 |
| 4.14 | Comparison of charge extracted of the Hybrid model with stopping condition of available SOC=0% with the values extracted from the datasheet . . . . . . . . . | 67 |
| 4.15 | Comparison of relative error between the Hybrid model and Datasheet values pre- sented in Table 4.14 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . | 67 |
| 5.1 | Goodness of fit presented in Figure 5.4 . . . . . . . . . . . . . . . . . . . . . . . | 76 |
| 5.2 | Coefficients obtained in the fitting of function 5.2 . . . . . . . . . . . . . . . . . | 76 |
| 5.3 | Summary of fault and warning thresholds . . . . . . . . . . . . . . . . . . . . . | 93 |

## Abreviations and Symbols

AC

Alternating Current

Adj R-sq Adjusted R-square

AKF

Adaptive Kalman Filter

Ah Ampere-hour

AMS

Accumulator Management System

As Ampere second

ASPICE Automotive SPICE

BMS

Battery Management System

CAN

Controller Area Network

CC

Constant Current

CC-CV Constant Current-Constant Voltage

CPF

Cubature Particle Filter

CV

Constant Voltage

D-APF Double-Scale Dual Adaptive Particle Filter

DCM Discontinuous Current Mode

DoD

Depth of Discharge

DP

Dual Polarization

D-PF

Double-Scale Dual Particle Filter

EKF

Extended Kalman Filter

EOL

End of Life

EV

Electric Vehicle

FEUP

Faculdade de Engenharia da Universidade do Porto

FS

Formula Student

FSAE

Formula Student of Automotive Engineers

FSFEUP Formula Student FEUP

FSG

Formula Student Germany

FSUK

Formula Student UK

HMI

Human-Machine Interface

IC

Integrated Circuit

KF

Kalman Filter

Kibam Kinetic Battery Model

LiCoO2 Lithium Cobalt Oxide

Li-ion Lithium-ion

LiMnNiCo Lithium Manganese Nickel Cobalt

Li-poly Lithium Polymer

Li4Ti5O12 Lithium Titanate

MBSE Model-Based Systems Engineering

MPC Model Predictive Control

| NiCd | Nickel Cadmium |
| - | - |
| NiMH | Nickel-Metal Hydride |
| NTC | Negative Temperature Coefficient |
| OCV | Open Circuit Voltage |
| PCB | Printed Circuit Board |
| PF | Particle Filter |
| PI | Proportional-Integral |
| R&D | Research and Development |
| Rint | Internal Resistance |
| RMSE | Root Mean Square Error |
| SDGs | Sustainable Development Goals |
| SOC | State of Charge |
| SOE | State of Energy |
| SOH | State of Health |
| SOP | State of Power |
| SOS | State of Safety |
| SPKF | Sigma Point Kalman Filter |
| SSE | Sum of Squared Errors |
| SWOT | Strengths, Weaknesses, Opportunities, and Threats |
| TSAC | Tractive System Accumulator Container |
| UI | User Interface |
| UKF | Unscented Kalman Filter |
| VE | Veiculo Elétrico |
| Vnom | Nominal Voltage |
| Voc | Voltage open circuit |
| WTA | Weighted Temperature Averaging |
| XDC | Xelerate Digitalcar |
| ZEBRA | Molten Salt |
| Zn-Air | Zinc-Air |

## Chapter 1

## Introduction

This chapter introduces the thesis, outlining the mission and objectives of the project within the defined scope. It also provides the context in which the project was developed, detailing the involvement of Formula Student (FS) and the partnership with Xelerate, where this thesis was conducted. Lastly, the overall structure of the thesis document is presented, detailing the organization and content of each chapter.

## 1.1 Problem and Context definition

In recent years, the development and widespread adoption of electric vehicles (EVs) has gained significant attention due to their potential to mitigate environmental concerns and reduce dependency on fossil fuels, due to the use of electrical energy to operate motors [2]. Within this context, the battery is the main component of an electric vehicle, as it dictates its performance, range, and overall safety. Therefore, the development of Battery Management System (BMS) technologies has been emerging as an area of research to enhance the efficiency of EV batteries, thereby making their adoption a convincing option for drivers compared to traditional combustion alternatives.

Within this landscape, the FS competition stands as a unique platform that not only promotes innovation of automotive technologies but also serves as a testing ground for young engineers to demonstrate their technical analysis, engineering design, and manufacturing skills whilst having to meet a strict deadline and rules compliance [3].

This thesis is driven by a mission to advance sustainable mobility and technological innovation in the automotive sector, with a specific focus on electric vehicles and efficient battery management. By searching into the development of an advanced and intelligent BMS, the goal is to optimize the reliability of EVs, contributing to a cleaner and more eco-conscious transportation future. The aim is to develop a versatile, scalable, robust, and reliable BMS to be applied to FSFEUP vehicles.

The central problem of this thesis is to investigate how can a developed BMS be competitively advantageous for the FSFEUP team when compared to the current solution of buying a commercial one. This will set up the decision of whether it is worthwhile to develop a custom BMS prototype in the future, or if opting for an off-the-shelf BMS is a more suitable approach for the team's needs.

## 1.1.1 Formula Student FEUP context

Founded in July 2021, Formula Student FEUP (FSFEUP) embarked on a journey driven by a group of ambitious engineers with a clear mission: "to foster students' self-development, by providing them with the chance to be part of something bigger together, by developing Formula Student-spec prototypes - resulting in career-ready people" [4].

The team is composed of around 60 students (Figure 1.2) from different engineering branches (mechanical, electronic, informatics, and other courses), composing the 8 departments of the team [5]:

- Powertrain: "Responsible for the Accumulator, Transmission, and Cooling Traction System subsystems"
- Chassis and Aerodynamics: "Responsible for the Chassis, Aerodynamics and Driver Interface subsystems"
- Vehicle dynamics: "Responsible for the Suspension Geometry and Kinematics subsystems, Control, Lap Time Simulation, and Testing"
- Suspension: "Responsible for Wheel Assembly, Vibration, Wind Arms, Braking and Steering subsystems"
- Autonomous systems: "Responsible for the State Estimation, Planning and Control, Perception and Simulation and Infrastructure subsystems"
- Electronics and software: "Responsible for low voltage subsystems, software, traction system, and traction system accumulator"
- Research and Development: "Responsible for creating the connecting infrastructure between students, academia and companies - through the development of master's and bachelor's thesis"
- Operations: "Responsible for the Sponsors, Marketing and Logistics subsystems"

This thesis is not only related to the department of Electronics and Software but also to the recently developed Research and Development (R&amp;D) department.

The Formula Student competitions are divided in two categories: dynamic and static events.

Dynamic events are designed to test the performance of the prototype vehicle, assessing its capabilities across a range of challenges. These challenges include Endurance (250 points) where the vehicle must demonstrate its durability over a long-distance course, Efficiency (100 points), which evaluates the vehicle's energy consumption and overall efficiency, Skid Pad (50 points), testing the vehicle's handling and cornering abilities, Autocross (100 points), a timed event requiring agility and precision in navigating a course, and Acceleration (50 points), which measures the vehicle's speed and acceleration performance [4, 6].

On the other hand, static events focus on evaluating the team behind the prototype. Judges, often experts from economics, the automotive industry, and esteemed competitions like Formula 1, evaluate various aspects of the team's work. This includes the Business Presentation (75 points), where teams showcase their understanding of the market and their business plan, the Engineering Design event (150 points), which assesses the technical prowess and innovation of the vehicle's design, and the Cost Report (100 points), where teams must demonstrate their ability to manage project finances effectively [4, 6].

Figure 1.1 illustrates a chart with the points distribution of the various FS events, highlighting the weight of the Endurance event.

Figure 1.1: Chart points distribution of formula student events

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_002.png)

The team's first-ever prototype, FSFEUP01 (Figure1.3), marked a significant milestone at the beginning of their history. From 2021 to 2023, FSFEUP01 underwent rigorous testing and validation, competing in renowned events such as Formula Student UK (FSUK) and Formula Student Germany (FSG). These competitions provided opportunities for the team to showcase its engineering expertise and gain insights into the competition landscape. From their participation in their first 5 events (2022 and 2023), they managed to collect 6 awards.

In the upcoming cycle, from 2023 to 2025, the team's focus will be on the FSFEUP02 prototype development, centered on autonomous driving technology, and it will begin with the participation of static events only.

## 1.1.2 Xelerate digitalcar context

Xelerate Digitalcar (XDC), powered by AVL Software and Functions GmbH (AVL), stands at the forefront of mobility technology, offering cutting-edge solutions for development, simulation, and testing in the automotive industry and beyond. With a focus on sustainability and innovation, XDC envisions a future where technology fosters greener, safer, and more efficient mobility solutions.

Figure 1.2: FSFEUP 2024 team members from [5]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_003.png)

Figure 1.3: FSFEUP01 car, team´s first ever prototype from [4]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_004.png)

The collaboration and sponsorship between XDC and FSFEUP reflect a shared commitment to driving sustainable innovation in the automotive sector. This partnership underscores the significance of developing advanced technologies, such as BMS, to address the evolving needs of EVs.

This BMS project collaboration is planned to continue over the next two years, progressing through different stages. This first year focuses on researching and simulating the proposed solution, while the second year aims to physically verify and produce a quick validation prototype. The third and final year will conclude the project with the development of a final prototype, ready to be integrated into the vehicle.

## 1.2 Project scope

The project will begin with a research stage, starting with the definition of a conceptual solution. Drawing on insights from a review of the state-of-the-art BMS technology, the project will identify and evaluate potential solutions, selecting those best suited to the project's needs and constraints.

The project will progress to system definition and design, taking into account the system requirements. Leveraging a model based systems engineering (MBSE) approach, a BMS will be developed and tested with the help of Matlab software.

The project will include the development of a user interface (UI) to perform configurations and monitor battery cells. This interface will enable users to adjust system parameters and monitor key metrics of the system.

## 1.3 Product objectives

The objectives of this research are defined to address the team's specific challenges and needs, with the aim of improving the overall performance of the BMS. These objectives will serve as a guideline in evaluating the existing state-of-art solutions proposed.

One of the main objectives is to create a BMS solution that manifests as a reliable system for the FSFEUP team. The goal is to deliver a BMS that is adapted to the team's needs and ensures consistent performance under the demanding conditions of competitive racing.

Building upon past experiences, one of the defined objectives is to reduce system complexity compared to its predecessor. The team aims to implement a decentralized BMS architecture, which is further discussed in Section 2.4.2.1, to simplify cable management and minimize potential points of failure.

Anticipating the dynamic landscape of electric vehicle technologies and the recurrent need to innovate in the world of FS competitions, the project focuses on delivering a BMS with scalability and versatility. This involves creating a system that not only meets current requirements but also being future-proof so that can it be adapted to future changes, such as battery configuration.

Having a balance between performance and cost is imperative to the project's objectives. By optimizing resources and re-utilizing the benefits of the current solution, the goal is to create a BMS that aligns with cost considerations while delivering the quality and efficiency demanded by the team. The aim is to achieve a cost-benefit equilibrium, considering the financial constraints of the team.

Another important objective is to prioritize safety within the FS FEUP team by including safety features in the BMS. The intention is to ensure the well-being and protection of both the team and the electric vehicle system, by having a rigorous diagnosis of the battery.

## 1.4 Structure of the thesis

The following document is structured into six chapters, as described next.

Chapter 1 introduces the thesis, outlining the project's mission, objectives, and scope. It provides the context of the project, detailing the involvement of Formula Student and the collaboration with Xelerate.

Chapter 2 delves into the state of the art of batteries and BMS technologies. It explores the historical development of batteries and BMS, showcasing the growing importance of these technologies in electrical transportation. The chapter begins by covering fundamental concepts related to batteries, including their characteristics, parameters, and various chemistries. It provides a comprehensive overview of BMS functions, components, and topologies, discussing the advantages and disadvantages of different approaches. Furthermore, the chapter explores advanced BMS features such as cell balancing, state estimation methods, charging and discharging control, fault diagnosis, and integrating integrated circuits. It concludes by examining the application of BMS within Formula Student, demonstrating real-world examples and the most common approaches.

Chapter 3 details the methodology employed in the development of this project. It introduces the Automotive SPICE (ASPICE) framework, a set of guidelines for ensuring quality and efficiency in automotive software development, and details the steps of requirements gathering and system architecture definition. The chapter also describes the tools utilized in the project, including MATLAB and its various toolboxes. It presents a comprehensive analysis of the previous BMS used by FSFEUP, identifying its strengths, weaknesses, opportunities, and threats. Based on this analysis, the chapter outlines the proposed new BMS configuration, detailing its architecture, components, and functionalities.

Chapter 4 focuses on battery modeling and simulation. It describes the process of parameterizing the battery model used in Simulink, a simulation environment within MATLAB. The chapter explores the characterization of the Simulink datasheet battery block, which utilizes manufacturer data to accurately represent battery characteristics. It also details the development of the hybrid battery model, combining the Kinetic Battery Model with an electrical circuit model. The chapter presents simulation results obtained from various tests and experiments, validating the accuracy and effectiveness of the hybrid model parameterization. Additionally, it introduces a user interface developed to automate the battery model parameterization process.

Chapter 5 elaborates on the model-based architecture used for the BMS. It provides detailed descriptions of the functionalities implemented in both the BMS Slave and Master blocks. The chapter covers various aspects of the BMS, including cell power loss representation, battery model integration, critical voltage and temperature calculation, cell balancing control, internal resistance estimation, current control algorithms, fault diagnosis, and communication of BMS with different systems. It also presents a user interface developed for simulating different configurations and scenarios, allowing for testing and analysis of the BMS performance.

Chapter 6 concludes the thesis by summarizing the main findings and contributions of the research. It evaluates the outcomes of the BMS development process, highlighting the compliance with requirements and highlighting the improvements achieved when compared to commercial BMS. The chapter also discusses potential future work, suggesting directions for further research and development in BMS technology and its application in Formula Student vehicles.

## Chapter 2

## State of the art

This chapter presents a comprehensive overview of the current state of research regarding EVs and BMS. It begins by tracing the historical development of BMS, highlighting the increasing complexity of these systems as battery technology has advanced. The chapter then delves into the fundamental principles of batteries, exploring their characteristics, parameters, and various chemistries. It provides a detailed examination of BMS functions, components, and topologies, discussing the trade-offs between different approaches. The chapter further explores advanced BMS features such as cell balancing and state estimation methods for determining critical parameters like State of Charge and State of Health. Additionally, it covers charging and discharging control strategies, fault diagnosis techniques, and a market review of integrated circuits used in BMS design. The chapter concludes by examining the specific application of BMS within Formula Student, showcasing real-world examples and common approaches in this competitive field.

## 2.1 Historical background

The progression of rechargeable battery technology has always been closely linked with the evolution of BMS. During the late 19th and early 20th centuries, lead-acid batteries were widely used, necessitating simple voltage regulation to control and avoid overcharging, and subsequent battery damage [7].

In the 1960s, the emergence of nickel-cadmium (NiCd) batteries demanded more intricate management techniques due to their specific charging and discharging requirements. This era marked the early conceptualization of BMS through the implementation of overcharge protection mechanisms.

The early 1990s introduced a significant advancement with the commercial release of lithiumion batteries. These batteries, offering higher energy densities, required sophisticated management systems to mitigate risks such as overcharging and thermal runaway. This period was critical in the development of more complex systems managing and controlling the battery.

Entering the 21st century, the popularity of electric vehicles, as illustrated in Figure 2.1, and the need for efficient renewable energy storage solutions significantly elevated the role of BMS.

Recently, modern BMS has evolved to a wide range of functionalities, including cell balancing, battery state estimation, fault diagnostics, and seamless system communication, and are indispensable across various applications, from electric vehicles and portable electronic devices to large-scale energy storage systems [7].

Figure 2.1: Annual demand forecast for EVs, from [8]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_005.png)

## 2.2 Battery fundamentals

Batteries are a conjunction of basic elements called cells. These cells can be connected in series or parallel to achieve the desired voltage and power capacity of a battery pack [9]. A typical cell consists of two electrodes - a cathode (positive electrode) and an anode (negative electrode) - an electrolyte, and a separator [9, 10, 11]. The electrode is the fundamental component where electrochemical reactions occur. The potential difference between the cathode and anode determines the cell voltage. During discharge, oxidation occurs at the anode, releasing electrons to the external circuit, while reduction occurs at the cathode, accepting electrons. The electrolyte facilitates ionic conductivity between the electrodes, while the separator prevents direct contact between the electrodes, avoiding short circuits [10, 11]. The reverse processes occur during charging, with oxidation at the cathode and reduction at the anode. Figure 2.2 illustrates a schematic of a lithiumion (Li-ion) cell, depicting its basic structure and the electrochemical reactions that occur during both discharge and charge cycles. In the diagram, the movement of electrons and ions is shown, highlighting the flow of electrons through the external circuit and the migration of ions within the cell.

## 2.2.1 Batteries characteristics

Batteries have several essential characteristics that define their performance and suitability for various applications.

Figure 2.2: Basic structure of a Li-ion cell and representation of the electrochemical reactions occurring during discharge and charge, from [10]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_006.png)

One of the main characteristics is the capacity (C), which represents the total amount of charge a battery can store, typically measured in ampere-hours (Ah). This value indicates how long a battery can provide a specific current before becoming fully discharged [12].

Nominal voltage (VN) refers to the standard voltage level provided by a battery under normal operating conditions. It is the theoretical voltage value of a battery, calculated by multiplying the number of cells connected in series by the theoretical voltage of each individual cell [9].

The open-circuit voltage (VOC) refers to the voltage across the battery terminals when no external load is connected, after the needed rest to accurately reflect the battery´s state of charge (SOC) and other conditions [9].

Internal resistance (Rint) is a property of the battery that affects its ability to deliver current. It causes a voltage drop within the battery when a current flows, impacting the efficiency and heating of the battery during operation. This resistance is typically quite low, usually in the range of tens of milli-ohms, and is generally provided by the manufacturer [9, 12].

Specific energy, expressed in watt-hours per kilogram (Wh/kg), denotes the amount of energy a battery can store per unit mass at a certain discharge current.

Specific power, expressed in watts per kilogram (W/kg), represents the total power a battery can provide per unit of mass for a given discharge rate [9].

Energy density refers to the amount of energy stored per unit volume, measured in watt-hours per liter (Wh/L).

The memory effect is a phenomenon observed in some rechargeable batteries where they tend to "remember" the point of partial discharge if not fully discharged before recharging. This can lead to a reduced effective capacity over time, commonly associated with NiCd and nickel-metal hydride (NiMH) batteries.

There are several batteries chemistries, with the most commonly employed in EVs being leadacid, NiCd, NiMH, lithium-ion (Li-ion), lithium polymer (Li-poly), zinc-air (Zn-Air), and molten salt (ZEBRA) [9, 10, 13, 14]. Among these, Li-ion batteries are the most prevalent due to their high energy density, long cycle life, and decreasing cost, as demonstrated in Figure 2.3.

Figure 2.3: Comparison of characteristics of different batteries chemistries, from [13]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_007.png)

## 2.2.2 Battery parameters

The state of charge (SOC) is a parameter that describes the amount of energy remaining in a battery. SOC is defined as the ratio of the available charge to the maximum possible charge that the battery can hold [15, 16]. Mathematically, SOC can be expressed as:

<!-- formula-not-decoded -->

where Qavailable is the charge currently available in the battery, and Qrated is the rated capacity of the battery [15], and it is often presented in percentage values.

Depth of Discharge (DOD) refers to the percentage of the total nominal energy stored in a cell or battery that has been withdrawn or utilized. It is essentially the complement to SOC, which indicates the percentage of available energy remaining in the battery.

State of Health (SOH) represents the overall condition of a battery relative to its initial state, as mathematically expressed in equation 2.2:

<!-- formula-not-decoded -->

where Qaged is the current capacity, and Qnew is the nominal capacity at the beginning of life [17].

This relationship is often expressed as a percentage, where a new battery has an SOH of 100%, and it is considered to have reached the end of its life at an SOH of 0% [9, 18]. Generally, a battery is considered to have reached the end of its useful life when its capacity or maximum deliverable power drops to 80% of the nominal value under reference conditions.

Life cycle denotes the total number of charge-discharge cycles a battery can undergo before its capacity diminishes significantly.

## 2.3 Battery management system (BMS)

During the research, it was noted that there is not a unique and single definition of a BMS, as most of them are different due to their specific requirements and applications [19]. The BMS, while often unseen by its users, plays an indispensable role in the safe and optimized operation of the battery. In essence, a BMS serves as the guardian of the battery, prioritizing its protection and ensuring user safety [20]. The main functions of the BMS will further be scrutinized in the following sections of the chapter. Still, its main duties are the following: monitor the battery and measure its key parameters (current, voltage, and temperature), protect the battery, estimate the state of the battery, maximize its performance, and communicate with the user and external devices. These essential functions can be achieved through a variety of methods and varying levels of complexity, thereby determining the level of intelligence and sophistication inherent in the BMS.

In the specific application for electric vehicles, the necessity of a robust BMS arises as the battery plays an indispensable role in the vehicle, due to the EVs being powered by them. The BMS not only serves as a protector of the battery, extending its lifetime but also has the role of interconnecting the battery with other systems and components in the vehicle, such as the charger and electronic control unit [17]. This can be visualized in the general architecture of an EV presented in Figure 2.4.

Figure 2.4: General architecture of an electric vehicle

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_008.png)

Beyond powering the vehicle, the battery dictates the EVs autonomy and range. Here, the BMS steps in, as it is the system that provides to the driver with all the information needed for a safe driving experience. The BMS optimizes the battery's overall performance by monitoring crucial parameters, protecting the battery from fault scenarios, and controlling its charge balance [7].

## 2.3.1 Lithium-Ion (Li-Ion) BMS

Li-Ion cells, introduced by Sony in Japan in 1991, are widely used in the fields of computer and mobile technologies, and in the last decade have been highly adopted by the automobile industry, with companies such as Nissan and Tesla [9]. This type of rechargeable cells has the highest energy density, minimal memory effect, and low self-discharge rate in the cell market, making them the most promising to be applied in electric vehicles when compared to others [2]. These characteristics offer the EV a wide range of autonomy and enhance its acceleration capabilities while having a compact occupation within the tractive system accumulator container (TSAC). The Li-Ion cell is available in the following format: cylindrical, prismatic, and pouch, as seen in Figure 2.5, and there are several chemistries types, such as LiCoO2 - Standard lithium-cobaltoxide, LiMnNiCo - Lithium manganese nickel cobalt, Li4Ti5O12 - Lithium titanate, etc. Figure 2.6 presents the different operating voltage characteristics of Li-ion cells related to their specific capacity.

Figure 2.5: Li-ion cell formats:(a) cylindrical, (b) prismatic, and, (c) pouch, from [21]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_009.png)

Figure 2.6: Li-ion chemistries and respective specific capacity, from [2]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_010.png)

However, this battery presents certain disadvantages. The process of charging and discharging requires careful and intricate management to ensure safety and prolong battery lifespan. Overdischarging can significantly reduce battery cycles (typically around 1000 cycles) while overcharging may lead to overheating. This not only risks irreparable damage but also poses potential hazards such as fires or explosions, endangering end-users safety [9].

This necessity for careful and intricate management underscores the heightened requirement for a BMS. A Li-Ion BMS, citing the book from [19], must at the very least and in order of importance, do the following:

- "Prevent the voltage of any cell from exceeding a limit, by stopping the charging current, or requesting that it be stopped. This is a safety issue for all Li-Ion cells."
- "Prevent the temperature of any cell from exceeding a limit by stopping the battery current directly, requesting that it be stopped, or requesting cooling. This is a safety issue for Li-Ion cells that are prone to thermal runaway."

- "Prevent the voltage of any cell from dropping below a limit by stopping the discharging current or requesting that it be stopped."
- "Prevent the charging current from exceeding a limit (which varies with cell voltage, cell temperature, and previous level of current) by requesting that the current be reduced or stopped, or by stopping the current directly."
- "Prevent the discharging current from exceeding a limit, as described in the previous point."

As mentioned above, the BMS is crucial during the charging and discharging of a Li-ion battery, as it is the system that keeps the battery working within its safe operating area (SOA), preventing the battery from exceeding its voltage, current, and temperature limits. In sum, when compared to other cell chemistries, Li-Ion requires accurate management in order to provide safety and protection to the battery, emphasizing the essential need of having a "brain" controlling the operation [12].

Figure 2.7 presents a high-level diagram of the Tractive System Accumulator Container (TSAC). The diagram illustrates the integration of a Li-ion battery pack with essential components such as the fuse, charger, load, and thermal system. The BMS is central to this setup, overseeing balancing, monitoring, and data management. Additionally, the diagram highlights the data links connection to the logging and telemetry units.

Figure 2.7: Generic TSAC block diagram, from [22]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_011.png)

## 2.3.2 BMS components and functions

As previously mentioned, the BMS can vary in levels of complexity, ranging from a highly intelligent and sophisticated system to a more basic and straightforward one. This reflects not only on its functionalities but also on the amount and type of components used in the design and development of the system. In general and essentially, the BMS is composed of two main components: the monitoring module, which measures the crucial parameters of the battery, and the control module, the one responsible for the computation and communication [23].

The monitor module is responsible for gathering data from the battery pack and cells, and commonly measures: cell voltage (and consequently the pack voltage by adding the voltage of cells in series), cell temperature, and current of the pack. Although this measurement function can be accomplished in several ways due to the wide range of hardware components available in the market, this is a paramount function common to all BMS since the rest of the functionalities depend on this. The control module, normally represented by a Printed Circuit Board (PCB), is where the rest of the functionalities are integrated, and it is also where the BMSs distinguish themselves in terms of levels of complexity. In essence, this control module is responsible for the computation of the system, typically providing functionalities such as diagnostics, management, control, and state estimation of the battery. Additionally, it ensures the necessary communication between various vehicle components and the user, usually through a Human-Machine Interface (HMI). This control module features will be discussed in depth in Section 2.5.

## 2.4 BMS topology

Control system architecture refers to the structural design and organizational framework that governs the operation and interaction of various components within a control system. [24]. Similarly to its definition, the research made on BMS topologies in existing literature has revealed a spectrum of definitions. In this thesis, the definition of BMS topology is based on the relationship between the main components of the system (the monitoring module and the control module) and how they are disposed of in the system [23]. Firstly, a distinction is made between the distributed and non-distributed topologies. Non-distributed are further divided into centralized and decentralized architectures, with this last one including master-slave and modular approaches [22], as illustrated in Figure 2.8.

Figure 2.8: BMS different topologies

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_012.png)

Figure 2.9, presents the three main BMS control network topologies and illustrates the interaction between the system nodes. The centralized network features a single control unit managing all the other nodes, while the decentralized network shows multiple sub-nodes acquiring data and communicating with a single master node. The distributed topology depicts a network where each node communicates with multiple others.

Figure 2.9: Control networks of BMS topologies:(a) centralized; (b) decentralized (modular and master-slave topologies), and (c) distributed, adapted from [25]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_013.png)

## 2.4.1 Distributed topology

The distributed (from the dictionary "shared or spread out") BMS is an architecture where the electronics (cell boards) are directly placed on the cells being measured. These cell boards are responsible for the monitoring and control of the cells, and communicate with each other through wires, having a distributed control over the system [19]. Additionally, there is a possibility of having a controller that handles the communication and computation of the multiple distributed intelligence spread across the cells, in cases of more complex implementations, as seen in Figure 2.10. The colors in the diagram relate to the functions of the BMS, with yellow representing functionalities exclusive to the monitor module, blue representing functionalities exclusive to the control module, and green representing a module that performs both functionalities.

Figure 2.10: Distributed BMS topology, adapted from [19]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_014.png)

This approach presents several advantages, with the most notable being the greater functionality and precise control over the system due to having more than one control node. Adding to this, this topology has a reduced wiring need due to the cell boards being connected in a daisy chain manner and also presents significant scalability and expansion versatility [12, 19]. However, this topology presents an increased cost when compared to the others, due to each cell board having its own electronic components. Furthermore, this system can be complex in terms of handling several communication ports [19].

## 2.4.2 Non-distributed topology

In the non-distributed topology, opposite to what we have in the previous one, the control is allocated to one single module, making it the master module of the system. The following architectures differ from each other based on the relationship between the master module and the measurement module.

## 2.4.2.1 Centralized architecture

Centralized, in the context of system management, means that control is executed by a single authority or managed from one central location. In the realm of BMS, this concept is applied similarly, where the entire system is operated by a single module, as seen in Figure 2.11. This module is responsible for both the measure and control functions of the system, unifying these functions into a single module.

Figure 2.11: Centralized BMS topology, adapted from [19]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_015.png)

A centralized BMS offers several advantages. It is a compact solution and tends to be cheaper due to fewer components and a simpler design, leading to lower overall costs when compared to the others [19]. The system's low complexity also means it requires less maintenance, making it easier to manage in the long term. However, there are some disadvantages to this approach. A centralized BMS requires long cabling, which can increase the risk of misconnections, and it has limited scalability, making it less flexible for future battery configuration expansion. Additionally, as stated by the team, managing a large volume of components in a single area can be challenging and may impact the overall spatial efficiency of the system.

## 2.4.2.2 Decentralized architectures

Decentralized architecture, in opposition to the previous, has an architecture composed by multiple modules, in which one of them is considered the master controlling the rest of the modules. In this perspective, and as seen in Figure 2.8, the distributed topology may also be considered a decentralized architecture.

Modular architecture In the modular topology, several identical modules are connected to the batteries in the pack acting as measuring devices, with one of them being assigned as the master of the system, as illustrated in Figure 2.12. This master module is responsible not only for the data acquisition as the others but also for managing all the other modules and communicating with the rest of the systems [19].

This modular approach presents several advantages. Mainly, it enhances reliability, as in the event of a master module failure, the system can transfer control to another module. Additionally, this approach provides great scalability, making it straightforward to add more modules as needed for battery expansion. However, these benefits come with certain drawbacks. The increased reliability also brings higher control complexity to the system in terms of managing the master attribution. Furthermore, this approach tends to be more expensive than centralized systems due to the need for additional hardware and components [19].

Figure 2.12: Modular BMS topology, adapted from [19]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_016.png)

Master slave architecture The Master slave topology is very similar to the modular one, with the main difference being that this topology separates measurement and control functions on the modules. The slave modules are assigned exclusively to data acquisition, as the master module is in charge of all the computation and communication [19]. This topology is illustrated in Figure 2.13.

Figure 2.13: Master Slave BMS topology, adapted from [19]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_017.png)

This topology has most of the advantages and disadvantages of the modular topology, with the particular decrease of reliability, due to the system having one master exclusively and not being able to adapt the system in the event of control failure. On the other hand, due to this, it makes the solution less complex in terms of control and module management.

## 2.4.3 Hybrid architecture

This is a very abstract architecture, with high adaptability to specific needs and requirements, due to the combination of features of the previous topologies. With that comes the gathering of both advantages and disadvantages of the topologies mentioned above, with the external complexity of unifying more than one control architecture approach. An example of this hybrid adoption is the FST team's BMS. The work presented in [26] is based on a combination of master-slave and distributed topology, as seen in Figure 2.14.

Figure 2.14: FST hybrid BMS architecture, from [26]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_018.png)

## 2.4.4 Topologies comparison

The choice of topology is a crucial decision since it affects important parameters, such as cost, reliability, complexity, and scalability [19]. Table 2.1 summarizes the main characteristics to be considered in the overall choice of solution, presenting the overall strengths and weaknesses of each topology based on the referred parameters above.

Table 2.1: Comparison of BMS Topologies, adapted from [19]

| BMS Topology | Reliability | Scalability | Electronics Cost | Complexity |
| - | - | - | - | - |
| Distributed Centralized Modular Master Slave | High Medium High Medium | High Low High High | High Low Medium Medium | High Low High Medium |

## 2.5 BMS features

As mentioned before, there are several features that a BMS may have besides its measurement functionality. In this section, an overview is made of the main techniques and estimations features of an advanced BMS. Firstly, a review of cell balancing is made, scrutinizing the causes of cell unbalance and the main techniques to control the balance of the battery. Moreover, the main state estimation features, including, state of charge, state of health, and battery model are analyzed. The section proceeds to cover the main methods for controlling the current limits for both the charge and discharge processes and concludes with a review of fault diagnosis common parameters and methods utilized in BMS technology. Figure 2.15 summarizes the main functionalities of a BMS, showcasing the diversity of tasks and processes inherent to the BMS.

Figure 2.15: BMS main functionalities, adapted from [22]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_019.png)

## 2.6 Cell balancing

Although each cell is designed to be identical, manufacturing variations and chemical disparities can lead to subtle differences in their behavior [27, 28]. These distinctions become more pronounced over time due to diverse operating conditions and aging, significantly impacting the overall battery performance. Moreover, while not a direct cause, temperature gradients within a battery pack can aggravate cell unbalance. Cell behaviors, like self-discharge and efficiency, vary with temperature and this difference in internal temperatures among cells leads to unbalances. Higher temperatures also speed up degradation, causing cells to degrade at different rates [20]. Issues like limited usable capacity or potential cell damage may arise if these differences are not addressed. Figure 2.16 illustrates the factors producing pack inconsistency, reflecting on unbalanced operation, consequently affecting the pack performance [28].

Figure 2.16: Causes of cell unbalance and effect on performance, from [28]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_020.png)

To mitigate such risks, it is essential to implement a process known as cell balancing. This essential function, controlled by the BMS, ensures the maximization of usable capacity of the battery, by maintaining the battery pack in a balanced state. In figure 2.17 is visible the impact of cell unbalance in both charging and discharging scenarios, highlighting the impact of significant differences in SOC among cells. This unbalance not only reduces the overall battery capacity, due to the waste but also introduces the risk of premature aging and potential damage to individual cells.

Figure 2.17: The impact of the SOC imbalance on 4-cell battery pack during charging and discharging scenarios, from [29]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_021.png)

There are two main methods of cell balancing: passive balancing, also known as dissipative, and active balancing, also referred to as non-dissipative method. These methods differ in their approach to balancing. In the passive method, balance is achieved by dissipating energy from cells with higher charge, while in the active method, energy is transferred from cells with higher SOC to those with lower SOC [30]. Figure 2.18 shows the different passive and active balancing topologies based on the electronic component used for the balancing.

Figure 2.18: Resume diagram of cell balancing topologies based on the electronic component used

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_022.png)

## 2.6.1 Passive balance method

The passive method uses shunt resistors to dissipate the extra charge of the cells with higher SOC aiming to match those with lower SOC [31]. Among these methods, switched shunt resistor is the most common technique. In this approach, each cell is paired with a balancing resistor and a switch, commonly a MOSFET due to control simplicity, which is connected to the cell, as shown in Figure 2.19. The balancing resistors redistribute charge among cells, promoting balance [32]. In terms of the complexity of control, this is a favorable approach since it only requires the control of the switch to start and stop balancing. Some BMS integrated circuits (IC) offer direct control over these balancing switches, with integrated switches available in certain advanced IC designs [28].

Figure 2.19: Switched shunt resistor passive balancing circuit, from [32]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_023.png)

Another dissipative method involves the use of fixed resistors that are continuously connected to the cells, as seen in Figure 2.20. While this method allows the pack to naturally balance over time, as higher voltage cells experience greater resistor currents, it comes with inherent drawbacks. The fixed resistors lead to continuous losses, even when the pack is fully balanced, making it a less favorable option. Additionally, fixed shunt resistor balancing can also incorporate Zener diodes (Figure 2.21) to deactivate the balancing process once the cells reach a specific voltage, thereby reducing unnecessary energy dissipation [20, 32]. Both of these approaches lack control over the balancing state and conditions, as they employ a continuous and fixed balancing process.

Figure 2.20: Fixed shunt resistor passive balancing circuit, from [32]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_024.png)

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_025.png)

## 2.6.2 Active balance method

The active balancing method offers a wide range of solutions and can be categorized into four distinct groups: capacitor-based, inductor-based, transformer-based, and converter-based systems. Each group utilizes different electronic components to achieve cell balancing, offering unique advantages and disadvantages depending on the specific application and requirements.

Figure 2.21: Fixed shunt resistor passive balancing circuit with the Zener diode, from [32]

## 2.6.2.1 Capacitor based

In this method, capacitors redistribute energy between neighboring cells or from the battery pack to individual cells, effectively achieving cell balancing [28]. All implementations share a common principle: a capacitor is charged when connected in parallel with a higher voltage cell and discharged when connected in parallel with a lower voltage cell, absorbing the difference in energy between cells [33]. There are several capacitor based topologies, with the most common being the double tiered switched capacitors and single switched capacitor [28].

## 2.6.2.2 Inductor based

Inductor based balancing methods use inductors to transfer energy between cells. This approach relies on inductive coupling to move energy from cells with higher SOC to those with lower SOC. Common implementations include single inductor systems, which use one inductor to manage multiple cells, and multi-inductor systems, which employ individual inductors for each cell pair [34]. These methods are favored for their efficiency and speed but are often more complex and costly due to the need for multiple inductors and sophisticated control mechanisms [28].

## 2.6.2.3 Transformer based

Transformer based methods use transformers to facilitate energy transfer between cells. By leveraging the properties of transformers, energy is moved from cells with higher SOC to those with lower SOC, promoting balance. This can be achieved through various topologies, such as single transformers managing multiple cells or multi-winding transformers for more complex arrangements. While these methods are efficient and fast, they tend to be more expensive and complicated due to the intricate nature of transformer design and control [28, 34].

## 2.6.2.4 Common converter based

Converter based balancing methods employ DC-DC converters to manage energy distribution among cells. These converters adjust voltage and current levels to transfer energy from higher SOC cells to lower SOC cells effectively [28]. Several converters, such as Buck-Boost, Cuk, flyback, full-bridge, and quasi-resonant converters, can be used to transfer power between adjacent cells [28, 33]. Converter based methods are known for their precision and efficiency, though they come with increased complexity and cost due to the advanced control systems and components required [28, 30].

Figure 2.22 presents the circuitry of some of the commonly employed active topologies. The figure illustrates the balancing circuits of double tiered switch capacitor, multi-inductor, a single winding transformer, and a Buck-Boost converter.

Figure 2.22: Active topologies from left to right: double tiered switch capacitor, multi-inductor, single winding transformer, and Buck-Boost converter, adapted from [33, 34]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_026.png)

## 2.6.3 Methods comparison

Table 2.2 summarizes the comparison between the active and passive cell balancing methods, highlighting the advantages and disadvantages of each method based on key selection criteria, including cost, control complexity, size, and balancing speed.

Table 2.2: Comparison of cell balancing methods, adapted from [17, 28, 30, 35]

| Method | Total Cost | Complexity | System volume | Balancing speed |
| - | - | - | - | - |
| Passive balancing |  |  |  |  |
| Fixed resistors | Low | Low | Compact Compact | Low |
| Switched resistors | Low | Medium |  | High |
| Active balancing |  |  |  |  |
| Capacitor based | Medium | High | Large | Low |
| Inductor based | Medium | High | Large | Very high |
| Transformer based | High | High | Large | High |
| Converter based | High | High | Large | High |

To conclude this comparison, passive balancing, more specifically the switched shunt resistor, stands as a promising technique to be applied when compared with the active methods, since it presents crucial factors such as lower cost, reduced complexity control, compact size, and efficient balancing speed.

## 2.6.4 Balancing control variable

State variables have a great impact on the control of the balance of EV batteries. The correct state variable choice can make the balancing algorithm simpler and more effective, taking in consideration the needs of the solution. The most common state variables for balancing control in EV batteries include terminal voltage, battery capacity, and SOC [17].

## 2.6.4.1 Terminal voltage based control

Voltage based balancing systems aim to maintain the same cell voltage across the battery pack. This approach involves identifying the maximum and minimum cell voltages and determining their respective positions within the series connected battery string. Although constructing voltage based systems is relatively simple, this method often results in complex control mechanisms for multi cell batteries. Due to the uneven internal resistances of cells, voltage based balancing can lead to over equalization or under equalization, showcasing poor accuracy in reflecting the system inconsistencies. Despite these challenges, voltage based balancing offers fast sampling speeds [17, 36].

## 2.6.4.2 Battery capacity based control

Balancing based on battery capacity focuses on ensuring that the capacity of each cell is equalized to reflect system inconsistencies accurately. This method theoretically maximizes the available capacity of the battery string. However, it requires complex and precise calculations, making it challenging to implement in real time [36]. Capacity based control methods are known for their accurate reflection of system inconsistencies but suffer from poor real time performance and are difficult to measure directly due to the complicated calculation methods involved [17].

## 2.6.4.3 SOC based control

SOC based balancing aims to equalize the cells with maximum and minimum SOC in the battery pack. While this method can theoretically maximize the available capacity of the battery string, it necessitates accurate SOC estimation for each cell, resulting in a large amount of calculation [17, 36]. Despite its challenges, SOC based control accurately reflects system inconsistencies and can characterize the system's status effectively.

## 2.6.4.4 Comparison of balancing control variables

When selecting the variables, factors like the connection between the target variable and SOC, the ease of obtaining the target variable, accuracy in measuring it, and the time delay in updating it need to be considered. Table 2.3 summarizes the key aspects to be regarded when selecting the control variable for a balancing system. These aspects include the ease of obtaining the variable, determined by the complexity involved in measuring or estimating the parameter; the precision, reflecting the degree to which the balancing variable accurately represents the system's inconsistencies; and the real time performance, indicating the variable's reliability and effectiveness under real time operational conditions.

The table illustrates that both SOC and voltage variables align well with the necessary criteria for balancing control, with SOC having the distinct advantage of precisely representing the system's inconsistencies, such as the uneven internal resistance of cells. Further discussion on this topic, based on simulation tests, is provided in Section 5.3.4.1.

Table 2.3: Comparison of balancing control variables, adapted from [17, 36]

| Control Variable | Ease of Obtaining Variable | Precision | Real time Performance |
| - | - | - | - |
| Terminal voltage Battery capacity State of Charge | High Low | Low | Moderate Low Moderate |
|  |  | High |  |
|  | Moderate | High |  |

## 2.7 State estimation methods

As mentioned before, one of the paramount features of the BMS is to provide an accurate estimation of the current state of the battery. Studies made revealed several state estimation techniques to evaluate the battery pack condition [20], with the most commonly employed being: SOC, SOH, state of power (SOP), state of energy (SOE), and state of safety (SOS) [17]. Figure 2.23 illustrates the impact of SOC and SOH during the life cycle of a battery, highlighting the increase of SOC with higher battery voltage and the decline as the battery drains. On the other hand, SOH decreases as the number of charge and discharge cycles rises [7].

2

Figure 2.23: SOC and SOH effects of a battery, from [7]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_027.png)

Apart from this estimation method, since Li-ion batteries present highly nonlinear dynamics [17], it is crucial to control and predict the battery behavior and response in any conditions of usage [9, 17]. To achieve this, BMS relies on battery models to accurately represent the battery´s performance.

The next sections will focus exclusively on the SOC and SOH estimation methods, defining the concept and presenting the several methods in which they can be obtained. Moreover, different battery model types are defined, analyzing which model is the most promising to be applied based on the needs.

## 2.7.1 State of Charge (SOC) estimation

Despite its straightforward definition presented before, since the SOC is associated with the internal charge concentration within the battery, it cannot be directly measured [16]. Therefore, it is essential to develop estimation methods that rely on measurable parameters of the battery, such as voltage, temperature, and current [15, 16].

Below are presented the most common SOC estimation methods, each presenting its advantages and limitations, making it suitable for specific applications and conditions.

## 2.7.1.1 Coulomb Counting

This method, also known as the Ampere-hour (Ah) counting method, is the most extensively used method for SOC estimation [15, 16], and as the name states, is based on the principle of coulombic counting. To calculate the SOC value, this method uses the integration of the charge and discharge current flowing in the cell, as seen in equation 2.3:

<!-- formula-not-decoded -->

where, SOC(t0) is the initial SOC, η represents the coulombic efficiency, Cn represents rated cell capacity, and I(t) is the instantaneous current of the battery, assuming negative values for charging and positive in discharging [15, 16]. η is obtained by the ratio of the charge delivered from the electrode during discharging to the charge stored on the electrode during charging [37]. Despite its common use in BMS due to its simplicity and implementation convenience, it faces two notable drawbacks. It requires precise initial SOC, often challenging due to battery aging, and is vulnerable to current measurement errors, especially with fluctuating loads or high temperatures [38].

## 2.7.1.2 Open circuit voltage (OCV)

The OCV method relies on the relationship between the SOC and the battery's open circuit voltage. After the battery has rested for a sufficient period, the terminal voltage stabilizes to the OCV, which can be mapped to the SOC using a predefined OCV-SOC curve, as shown in Figure 2.25, or lookup table [15, 17, 39]. Figure 2.24 illustrates the flowchart process of this method.

This method provides accurate SOC estimation when the battery is at rest but is impractical during active operation due to the need for long rest periods. To overcome this limitation, it's often combined with other methods that can handle dynamic loads, ensuring more accurate SOC estimation across varied operating conditions [17].

## 2.7.1.3 Battery model based

Recently, there has been significant progress in developing real-time diagnostic algorithms for estimating the SOC using battery models [15, 16]. These techniques model the battery dynamics as nonlinear systems and utilize real-time parameter identification and adaptation methods. The estimation method, from [15]

Figure 2.24: Flowchart of OCV-SOC

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_028.png)

process involves mapping the Open Circuit Voltage (OCV) to the SOC, with continuous updates to the parameters to accurately capture both the static and dynamic properties of the battery [16, 38]. The reliability of this estimation highly depends on the model's accuracy. A detailed discussion of various battery models can be found in Section 2.7.3.

## 2.7.1.4 Adaptive filters

To enhance the accuracy and robustness of battery SOC estimation while minimizing the impact of noise on the battery model, the application of adaptive filtering algorithms from modern control theory offers an alternative estimation method [38]. Figure 2.26 illustrates the process of applying filters to the battery model in order to obtain SOC [40].

Figure 2.26: Diagram of SOC estimation method based on battery model with filter appliance, from [40]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_029.png)

There are several adaptive filters, with the most commonly employed presented below.

Kalman Filter The Kalman filter (KF) is an optimal estimation algorithm that uses a series of measurements observed over time to estimate unknown variables and is widely recognized as an optimal state estimator and an intelligent tool for linear systems [16, 38]. One of the most appealing features of the Kalman filter is its self-correcting capability during operation, which allows it to accommodate significant variations [38, 41]. The Kalman filter operates using a linear state space model that involves predicting the current state based on the previous state and updating the current state with new measurements to converge toward the true value. There are several variations of the Kalman filter, each presenting unique features, such as the Extended Kalman Filter (EKF), Adaptive Kalman Filter (AKF), Unscented Kalman Filter (UKF), Sigma Point Kalman Filter (SPKF), and others [38].

Figure 2.25: Typical OCV-SOC curve

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_030.png)

Particle Filter The Particle Filter (PF) algorithm is a state estimation technique that approximates the probability density function of a non-linear system using the Monte Carlo simulation method. This algorithm has been effectively applied in battery SOC estimation due to its ability to handle non-linearities and non-Gaussian noise. Notable advancements in PF algorithms include the Cubature Particle Filter (CPF), the Double-Scale Dual Particle Filter (D-PF), and the Double-Scale Dual Adaptive Particle Filter (D-APF). Despite its advantages, the PF method is computationally intensive [38].

## 2.7.1.5 Neural Networks

Neural networks are computational models inspired by the human brain's structure and function, capable of learning and storing information through interconnected neurons, or weights. These networks, organized in layers, process input parameters through hidden layers to produce output estimates, as seen in Figure 2.27 [15, 38, 41].

In the context of SOC estimation, neural networks effectively model the nonlinear relationships within battery systems, enhancing prediction accuracy by learning from historical data and adapting to new information, with the main drawback being they require a large amount of training data and computational power [41].

## 2.7.1.6 Comparison of SOC Estimation Methods

The selection of the SOC estimation method for a BMS appliance has to take into consideration several factors, such as ease of implementation, accuracy of estimation, real-time application, and computational cost. Table 2.4 summarizes the key aspects of the discussed SOC estimation methods based on these key factors.

This table illustrates that each SOC estimation method has its strengths and weaknesses. Coulomb counting is simple and suitable for real-time applications but suffers from accuracy issues due to cumulative errors. The OCV method provides high accuracy when the battery is resting but is impractical for real-time use. Battery model-based methods and Kalman filters offer a good balance between accuracy and real-time application, though they require more complex implementation. Particle filters and neural networks provide the highest accuracy and robustness, especially in handling nonlinearities and noise. However, they demand significant computational resources and are more complex to implement.

Figure 2.27: Neural network for SOC estimation, from [41]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_031.png)

Table 2.4: Comparison of SOC estimation methods, adapted from [15, 16, 38, 41, 42, 43]

| Method | Ease of implementation | Accuracy | Real time application | Computational Cost |
| - | - | - | - | - |
| Coulomb Counting OCV Method Battery Model Based Kalman Filter Particle Filter Neural Networks | High Moderate Moderate Moderate Low Low | Low High (at rest) High High High Very High | Yes No Yes Yes Yes Yes | Low Low Moderate Moderate Very High Very High |

## 2.7.2 State of Health (SOH) estimation

Similar to SOC, the SOH parameter cannot be directly measured and is typically assessed by monitoring changes in capacity, internal resistance, self-discharge rate, and power density [16]. The most commonly employed methods for obtaining the SOH of the cell are outlined below.

## 2.7.2.1 Charge/Discharge cycle count

The most empirical approach to obtain the SOH parameter is by keeping track of the number of charge/discharge cycles the battery has undergone [17, 44]. Each life cycle represents one complete charge and discharge of the battery [9]. This method assumes that the SOH degrades predictably with each cycle. However, the actual degradation can vary based on usage conditions, such as different current discharges, as seen in Figure 2.28, and battery chemistry, making this method less precise without additional data.

Figure 2.28: Cycle characteristics from Molicel model INR-18650-P28A with different current discharge conditions

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_032.png)

## 2.7.2.2 Capacity measurement

The driving range of EVs is predominantly determined by the battery capacity, making capacity measurement a widely used method for estimating the SOH. The process begins by fully charging the battery according to a specified charging procedure. Once fully charged, the battery is then fully discharged at a fixed rate until it reaches the end-of-discharge point, which is typically defined by a cut-off voltage threshold [17, 18]. The battery capacity is then determined by calculating the discharge capacity in Ah [17]. The SOH is subsequently obtained by calculating the ratio between the current capacity and the nominal capacity of the battery, as seen in 2.2.

Despite its simplicity and accuracy, this method has a significant drawback: it cannot be applied when the battery is subjected to dynamic current loads, as is common in EV applications. As a result, capacity measurement is typically used in laboratory settings for estimating the battery's capacity under controlled conditions [17].

## 2.7.2.3 Internal resistance measurement

One of the most common and efficient approaches to obtaining the SOH is by measuring or estimating the internal resistance value of the cell, as the evolution of a battery's life is significantly influenced by the increase in internal resistance and the corresponding loss of capacity. This method assesses the battery's resistance to current flow, which directly impacts its voltage drop during operation [18, 44]. A common approach involves applying current pulses and observing the voltage response, following Ohm's law to calculate the internal resistance:

<!-- formula-not-decoded -->

where ∆U is the voltage drop, and ∆I is the change in current [17]. This technique can track resistance degradation over the battery's life by measuring resistance at different states of charge (SOC) and temperatures. Figure 2.29 illustrates an example of applying pulse discharge and charge currents in order to observe the voltage drop.

Figure 2.29: Battery voltage dynamics under charge/discharge current pulses, from [17]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_033.png)

Studies have shown that while SOC has minimal effect on resistance growth, temperature significantly influences resistance increase, thereby affecting battery life [17, 18, 44].

## 2.7.2.4 Battery model based

Similar to SOC estimation, battery models are commonly used to gain valuable insights into the SOH of the battery. While experimental methods, like some of those described previously, can provide rich degradation information and accurate SOH estimation, online, real-time, and reliable acquisition of battery health state is more desirable for BMS. Battery model based estimation methods can offer this advantage by utilizing capacity, resistance, and other parameters estimation [18, 44].

By combining real-time data with advanced computational techniques, battery model-based estimation methods provide a robust and accurate approach to SOH estimation, making them a critical component of effective BMS design, as it will be presented in Section 2.7.3 [44].

As described in SOC estimation methods, the same adaptive filters can be applied to improve the battery model accuracy of SOH estimation.

## 2.7.2.5 Comparison of SOH Estimation Methods

The selection of SOH estimation methods depends on various factors including ease of implementation, accuracy, applicability in real-time, and computational cost. Table 2.5 summarizes these key aspects for the discussed SOH estimation methods.

Table 2.5: Comparison of SOH estimation methods, adapted from [17, 18, 44]

| Method | Ease of implementation | Accuracy | Real time application | Computational Cost |
| - | - | - | - | - |
| Cycle Counting Capacity Measurement Rint Measurement Battery Model Based | High Moderate Moderate Moderate | Low High High High | No No Yes Yes | Low Moderate Moderate Moderate |

The table highlights the distinct advantages and limitations of each approach. Cycle counting is straightforward and easy to implement, making it accessible but less accurate for real-time applications. Capacity measurement is precise but unsuitable for dynamic conditions, limiting its practical use to controlled environments such as BMS. Internal resistance measurement strikes a balance, offering reliable real-time data and moderate implementation complexity. Battery modelbased methods, while relatively complex and computationally demanding, provide the highest accuracy and are well-suited for real-time BMS applications, offering comprehensive insight into battery health.

## 2.7.3 Battery model

Battery models are (mathematical) representations of the behavior and characteristics of batteries, crucial for BMS, particularly in estimating the SOC and SOH parameters. A reliable battery model allows the BMS to manage charging and discharging processes effectively, preventing overcharging or deep discharging, and extending the battery's overall lifespan.

Figure 2.30 illustrates the variety of battery models, that can be classified into several types, such as electrochemical, empirical, mathematical, stochastic, electrical, analytical, and hybrid models.

Figure 2.30: Different types of battery models, adapted from [9]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_034.png)

## 2.7.3.1 Electrochemical Models

Electrochemical models are based on the mathematical description of the chemical reactions occurring within the battery cells, providing high accuracy but at the cost of complexity [23]. An example is the DualFoil model, which requires around 50 specific battery parameters and extensive simulation time, making it impractical for real-time BMS applications [9].

## 2.7.3.2 Empirical Models

Empirical models are simpler to configure and apply but lack precision. Notable examples include Peukert's Law, which models discharge behavior using empirical parameters. This model is traduced by the following equation:

<!-- formula-not-decoded -->

where C is the battery-rated capacity, and L represents the expected discharge time of the battery following a certain constant current, I [9, 16]. The parameter α varies with different temperatures and currents, making it necessary to estimate through laboratory tests with the battery [9].

Despite their simplicity and ease of implementation, these models are unsuitable for applications requiring high accuracy and variable currents, such as BMS in EVs [9].

## 2.7.3.3 Stochastic Models

Stochastic models provide a qualitative description of battery behavior under variable currents but lack quantitative accuracy. An example is the Markov chain-based model, which describes battery behavior using probabilistic states [16].

These models are less effective for precise BMS applications due to their abstract nature, as they only provide relative lifetime comparisons. Additionally, it only considers the recovery effect and does not account for the impact of discharge and charge current intensity, which is crucial for BMS application [9].

## 2.7.3.4 Mathematical Models

Mathematical models define battery voltage as a function of charge/discharge current and SOC, minimizing an objective function relating reference voltage to simulated voltage. Examples include the Shepherd, Unnewehr Universal, and Nernst models [9]. Both terminal voltage, Vout, and OCV, Voc, can be estimated using these models, as seen in the following equations:

## · Shepherd Model

Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

## · Universal Unnewehr Model

Thus,

## · Nernst Model

Thus,

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where, Vout represents the output voltage, Rs is the series resistance, and E0, k, k1, k2, and k3 are constants used to adjust the model to match the real output voltage [16].

Another mathematical model was proposed in [9, 16, 45], and consists in the following equation:

<!-- formula-not-decoded -->

where Voc and kV1 represent the OCV and SOC of the battery, respectively.

These models, although precise, require highly accurate reference data.

## 2.7.3.5 Electrical Models

Electrical models recreate battery dynamics using equivalent electrical circuits. They offer intuitive understanding for electrical engineers and can simulate open-circuit voltage, terminal voltage, dynamic response, and self-discharge [9, 30]. The most commonly used models are:

- Rint model: Consists of a voltage source in series with a resistance.
- Thevenin model: Adds a parallel RC branch in series with the Rint model.
- Dual Polarization (DP) model: Further extends the Thevenin model by adding an additional parallel RC branch in series with the first.

Figure 2.31 demonstrates the electrical circuit of these models.

However, they struggle to represent non-linear behaviors, such as current intensity effects.

## 2.7.3.6 Analytical Models

Analytical models, such as the Kinetic Battery Model (Kibam) or Rakhmatov and Vrudhula's diffusion model, use physical analogies and differential equations to describe battery behavior. These models can account for recovery and current intensity effects but require precise parameter estimation and are complex to implement [9, 16].

Figure 2.31: (a) - Rint model; (b) - Thevenin model; (c) - DP model, from [30]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_035.png)

Kibam model The Kibam, introduced by Manwell and McGowan in 1993, provides an intuitive approach to representing the internal dynamics of a battery [9, 16, 46]. It conceptualizes the battery charge into two components: available charge (y1(t)) and bound charge (y2(t)). The available charge directly supplies the load, while the bound charge transfers to the available charge through a constant conductance valve (K), depending on the height differences (h1(t) and h2(t)) of the two charge components [46], as seen in Figure 2.32.

Figure 2.32: Conceptual illustration of the Kibam, adapted from [46]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_036.png)

The system's behavior is described by the following differential equations [9, 47, 48]:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

When the battery is in use, the available charge decreases, increasing the height difference between the two tanks, and causing the bound charge to flow into the available charge tank until equilibrium is restored. This model effectively represents the recovery effect, where the available charge increases during rest periods due to the transfer from the bound charge. The model also accounts for the impact of discharge current intensity, as higher current demands deplete the available charge more quickly. Due to its capabilities, the Kibam is an excellent candidate for BMS. However, its implementation requires solving differential equations in a circuit simulator and estimating several parameters, which can be complex and challenging [9, 47].

## 2.7.3.7 Hybrid Models

Hybrid models combine elements of various models to leverage their strengths while minimizing weaknesses. An example of this approach is the model combination of the Kibam with an electrical circuit model, or Rint model, providing comprehensive and accurate battery behavior representation, as presented in [9, 46, 47]. Figure 2.33 illustrates the coupling of both these models.

Figure 2.33: Hybrid model fusing Kibam and Rint model, from [46]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_037.png)

In this hybrid model, the Kibam model is coupled with an electrical circuit to receive data on the battery's SOC and calculate the terminal voltage. The mathematical block representing the Kibam model is connected to an electrical circuit that provides information on the charge current. This integration allows the model to capture non-linear dynamic effects and predict the usage time of individual cells and the entire battery pack with high precision under various charging and discharging conditions. This model is computationally efficient and suitable for BMS applications but requires extensive parameter estimation, as mentioned before in the Kibam description [9].

## 2.8 Charging and discharging control

In the case of Li-ion batteries utilized in EVs, it is imperative to control the charging and discharging mechanism to provide maximum efficiency and safety in conjunction with battery durability. Management leads to optimal utilization of energy, protection of such capacity from degrading, and avoids restrictive phenomena such as thermal runaway or overcharging, which can lead to severe safety issues. For a Formula Student BMS, this control is even more critical due to the varying events and discharging scenarios that the batteries undergo, therefore requiring precise and adaptive management to maintain optimal equilibrium between performance and safety.

## 2.8.1 Charging control

The charging process must be carefully controlled to avoid overcharging, which can degrade the battery and pose safety risks. Traditionally, the method recommended for charging Li-ion batteries is the Constant Current-Constant Voltage (CC-CV) technique [2, 19, 22, 49].

- Constant Current (CC) Phase: The battery is charged with a constant current until the voltage reaches a predetermined threshold. This allows for efficient energy transfer and rapid charging.
- Constant Voltage (CV) Phase: Once the voltage threshold is reached, the charging mode switches to constant voltage. During this phase, the voltage remains constant while the current gradually decreases as the battery reaches full charge. This phase ensures the battery is fully charged without exceeding safe voltage levels.

Figure 2.34 demonstrates the process of CC-CV charging

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_038.png)

Figure 2.34: CC-CV charging characteristics of Molicel model INR-18650-P28A cell at different C-rates

To enhance the precision of the CC-CV method, a Proportional-Integral (PI) controller is often employed. The PI controller adjusts the current and voltage in real-time based on the battery's state, ensuring stable and efficient charging. This control method helps eliminate the memory effect, which can hinder battery performance over time [2].

## 2.8.2 Discharging control

Discharging control is equally important to prevent over-discharging, which can lead to irreversible damage to the battery cells and significantly reduce battery lifespan. One of the common discharging control method for lithium-ion batteries is the Discontinuous Current Mode (DCM) [2, 50].

In DCM, the discharge current is meticulously controlled and periodically interrupted to allow the battery to rest. This helps manage the heat generated during discharging and reduces stress on the battery cells. The BMS monitors the battery's state of charge (SOC), temperature, and discharge current to adjust the discharging rate accordingly. By implementing DCM, the BMS can prevent deep discharges, which are detrimental to the battery's health, and ensure a balanced load distribution among the cells [50]. Other advanced control methods are presented below.

## 2.8.3 Advanced Control Methods

To further enhance charging and discharging processes, advanced control algorithms and techniques are employed:

Adaptive Control Systems These systems adjust charging and discharging parameters in realtime based on the battery's condition and environmental factors, optimizing charging efficiency and improving battery longevity.

Machine Learning Algorithms By analyzing historical data and learning from patterns, machine learning algorithms can predict optimal charging and discharging profiles, adapting to the battery's aging process and usage patterns.

Model Predictive Control (MPC) MPC uses mathematical models to predict future battery states and optimize control actions, handling multiple constraints and objectives for robust control of complex battery systems.

## 2.9 Fault diagnosis

BMS is one of the key enabling technologies that can help in improving the efficiency and lifetime of Li-ion batteries particularly those that are deployed in EVs. The identification of faults on BMS is critical to ensure that accurate and precise locations of the faults, which may endanger the safety of the battery or affect its efficiency, are detected immediately. For a Formula Student BMS, fault detection is a priority, not only to enhance the safety of both the driver and the vehicle but also due to the constant demanding nature of the FS events, which tend to push the car to its limits.

Several types of faults in Li-ion battery systems include overcharge, overdischarge, overheat, under heat, short-circuiting, thermal runaway, and some types of sensor failure [51, 52]. Figure 2.35 demonstrates an example of the fault diagnosis mechanism in the BMS.

It can lead to a drastic risk of threat to the life of the owners and other users, reduction in efficiency, and shortcomings in battery power. These faults are crucial to be known while designing the control system and most importantly the BMS ought to be designed with a very complex fault analysis mechanism to identify the fault and rectify it as early as possible. Effective fault diagnosis ensures optimal battery performance, enhances safety, and extends the overall life of the battery system [51, 53].

Figure 2.35: A schematic of fault diagnosis in the BMS, from [52]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_039.png)

## 2.9.1 Fault parameters

Following are described some of the most often utilized types of faults in BMS.

Overcharge and Overdischarge A basic BMS should continuously monitor voltage and current values, ensuring that they are maintained within their Safe Operating Area (SOA) to prevent overcharging and overdischarging. Overcharging can lead to excessive voltage, causing thermal runaway and potential explosion hazards. Overdischarge, on the other hand, can result in irreversible damage to the battery cells and significantly reduce the battery's lifespan.

Overheating and Underheating Maintaining the battery within an optimal temperature range is crucial. Overheating can accelerate battery degradation and lead to thermal runaway, while underheating can reduce the battery's efficiency and capacity.

Short Circuit Detection Short circuits can cause immediate and severe damage to the battery system, leading to potential fires or explosions. The BMS must detect and isolate short circuits quickly to prevent catastrophic failures [7, 51].

Thermal Runaway Thermal runway is a safety threat that results in a natural discharge of energy where the battery temperature rises. This can occur due to overstressing or overcharging of the battery, short-circuiting among other issues [7].

Sensor Faults Accurate data from sensors is vital for the BMS to function correctly. Sensor faults can lead to incorrect assessments of the battery's state, resulting in improper management and potential safety risks.

SOC and SOH Faults Monitoring and maintaining these estimated values within desired intervals is crucial to prevent undesirable faults. Typically, most EV batteries maintain the SOC

between 20% and 80%, while cells reaching 80% of their SOH need to be replaced due to their end of useful life, as mentioned before

## 2.9.2 Fault methods

In order to detect these faults, there are several employed methods, such as direct sensing, model based methods, and data-driven methods [2, 22].

Direct Sensing This approach involves the use of sensors to quantify physical parameters like voltage, current, and temperature. Anything that deviates from the expected standard is a likely indication of a fault. Nonetheless, it is normally difficult to differentiate between the deviations that are caused by a fault and random fluctuations [2].

Model Based Methods These methods involve the use of battery system mathematical models in assessing the expected behavior of the battery system. Larger differences between predicted and actual behavior suggest that faults occurred. Although accurate, these models may become hard to manage, requiring extensive computational power [52].

Data Driven Methods Machine learning algorithms and statistical methods analyze historical data to identify anomalies. These techniques can detect complex faults that might be missed by other methods but require large amounts of high quality data [52].

Depending on the nature and severity of the fault, the BMS may adjust the system's operation to minimize the impact, such as reducing the load on a weak cell, or it may shut down the system to prevent further damage. The ultimate goal is to protect the battery and the system while minimizing disruption to the application [53].

## 2.10 Integrated circuits (ICs) market

The choice of ICs for BMS applications is critical because not only does it have a direct impact on performance, but also due to compliance with system requirements. Key criteria for selecting a BMS IC include high accuracy measurements, fast communication interfaces, cost-effectiveness, suitable operating temperature and voltage ranges, integrated passive balancing capabilities, compact size, and high scalability for various system configurations.

Table 2.6 compares some of the most common BMS ICs available in the market based on these parameters.

Each IC has unique strengths and is suited for different applications. For instance, the BQ76940 and ISL94203 are well-suited for consumer electronics and power tools due to their low cost and integrated passive balancing capabilities. On the other hand, the LTC6804-2 and ISL78600 are ideal for automotive and industrial applications where high accuracy and robust communication interfaces are crucial.

Table 2.6: Comparison of BMS ICs [54]

| Integrated circuit | BQ76940 | MAX14921 | LTC6804-2 | ISL94203 |  |  | ISL78600 | BQ7961x Family |  |  |  |
| - | - | - | - | - | - | - | - | - | - | - | - |
| Cell Count | 9 to 15 | 12 |  | 16 |  | 3-8 |  | 12/14/16 |  | 12 |  |
| Voltage Accuracy | 25mV | ±1.2mV |  | ±0.5mV |  | ±30mV |  | ±1.5mV |  | ±1.5mV |  |
| Communication | I2C | SPI |  | SPI |  | I2C |  | SPI, UART |  | SPI |  |
| Voltage Limits (per cell) | 2V to 5V | 1.7V 5.5V | to | 0V to 5V |  | 0.5V 4.8V | to | 2.7V 4.5V | to | 0.3V to 5V | 0.3V to 5V |
| Temperature Limits (Operat- | -40°C to | -40°C | to | -40°C | to | -40°C | to | -40°C | to | -40°C | to |
| ing) | 85°C | 125°C |  | 85°C |  | 85°C |  | 125°C |  | 105°C |  |
| Cost | Moderate | High |  | Moderate |  | Low |  | Low |  | High |  |
| Passive Balancing Integrated | Yes | Yes |  | Yes |  | Yes |  | Yes |  | Yes |  |
| Size | Small | Medium |  | Medium |  | Small |  | Medium |  | Medium |  |
| Scalability | Medium | High |  | High |  | Low |  | High |  | High |  |

The BQ7961x Family stands out for its high scalability ("up to 64 devices can be connected in the daisy chain"), making it suitable for a wide range of applications from electric vehicles to industrial battery packs. Its combination of high accuracy, integrated passive balancing, and SPI daisy-chain communication interface ensures reliable and efficient battery management.

## 2.11 BMS within formula student

To gain a deeper understanding of the current BMS solutions adopted by some of the most highly regarded Formula Student teams, an analysis of their BMS selections was conducted. This analysis highlights the diverse approaches and technologies employed by different teams, as presented in Table 2.7. The table presents a comparison of the BMS systems used by various universities, showcasing key aspects such as battery configuration, maximum voltage, balancing techniques, and communication protocols. This comparative study provides valuable insights into the design choices and technical specifications that define each team's BMS.

The analysis reveals that Distributed and Master Slave topology is a common architecture approach, with this last one being implemented in the most recent vehicles. In terms of manufacturing, the majority of teams have chosen to develop their own BMS rather than using commercial options. This factor is influenced by the fact that many of these teams have been part of the Formula Student community for several years and have accumulated significant expertise. Opting for a custom-made BMS aligns with the teams' aspirations of achieving higher performance levels in the future, and having a solution tailored to their specific needs. Regarding cell balancing, it is evident that the passive method is preferred. This choice is primarily due to the lower cost and reduced complexity associated with passive balancing, as detailed in the section 2.6.

Table 2.7: Comparison of BMS systems across different universities, adapted from [26]

| University | TU Lis- bon | ETH Zürich | UAS Augsburg | ETSEIB Barcelona | FEUP | NTNU | Karlsruhe IT |
| - | - | - | - | - | - | - | - |
| Team | Projecto FST | AMZ Racing | StarkStrom Augsburg | ETSEIB MotorSp | FSFEUP | Revolve NTNU | KA Rac- ing |
| Vehicle | FST-04e | Grimsel | Elinor | CAT07e | FSFEUP01 | Lyra | Kit23 |
| Year | 2011 | 2014 | 2014 | 2014 | 2019 | 2023 | 2023 |
| Batt. Config. | 48s5p | 112s4p | 96s3p | 140s2p (2x70s2p) | 120s5p | unk | unk |
| Max Volt (V) | 175.2 | 470 | 403.2 | 588 | 432 | 600 | 532 |
| Cap (Ah) | 50 | 15.6 | 18.75 | 12.7 | 30 | unk | unk |
| Cell Chem. | LiFePO4 | unk | LiCoO2 | LiCoO2 | LiFePO4 | unk | LiPo |
| Cell Type | Cylindrical | Pouch | unk | Pouch | Pouch | unk | unk |
| Model | Seld De- veloped | Self De- veloped | Li-BMS v3 | Elithion Lithumate TM pro | Orion BMS | Self De- veloped | Self de- veloped |
| Topology | Dist. | Dist. | Cent., Mod. or Dist. | Dist. | Cent | Master- slave | Master- slave |
| Balancing Current Sensor | Passive Hall Ef- | Passive Shunt re- | Passive Shunt re- | Passive Hall Ef- | Passive Hall Ef- | Passive Shunt re- | Passive IVT-S 300 |
| Internal Bus(es) | fect CAN | sistor 4xCAN | sistor CAN, USB, | fect CAN | fect CAN, isoSPI | sistor isoSPI | CAN |
|  |  |  | Ethernet,RS- 232, I 2 C |  | CAN |  |  |
| External Bus(es) | CAN | CAN | CAN, RS- 232 | CAN, RS- 232 |  | CAN-FD | CAN |
| Cost (C) | 1100 | 1500 | unk | 4200 | 2000 | unk | unk |

## 2.12 Final remarks

This chapter has presented a comprehensive overview of the current state of the art in battery and BMS technology. Key insights include the advantages of a master slave topology for its balance of cost, complexity, and scalability, making it suitable for the project's requirements. For cell balancing, the switched shunt resistor passive method emerged as the most promising option due to its simplicity, cost-effectiveness, and suitability for Formula Student application needs. The importance of accurate battery modeling, particularly for precise SOC estimation and insights into SOH, was emphasized, with the hybrid model presented in Section 2.7.3.7 being promise due to its ability to capture non-linear dynamic effects and the recovery effect. This model will enable the implementation of advanced controls and fault diagnosis under various charging and discharging scenarios. The chapter also underscored the necessity of comprehensive fault diagnosis mechanisms and precise control over charging and discharging currents. The review of ICs in the market provided valuable information on their features and capabilities, highlighting the importance of considering factors such as accuracy, cost, size, and scalability in system design. Finally, the examination of BMS implementations in top FS teams offered practical insights into real-world applications and design choices in this competitive field, serving as a foundation for the subsequent chapters and guiding the development of a BMS tailored for FS EVs.

## Chapter 3

## Methodology and Proposed solution description

This chapter will begin describing the methodologies used in the preparation and development stage, describing the system engineering framework and the tools utilized during the thesis. Secondly, an analysis of the current commercial BMS will be made, to recognize the main strengths, weaknesses, opportunities, and threats this solution provides to the team. Parallel to this description, the BMS solution that will be presented and developed in this thesis is described last. This includes the selection of the most promising technologies and approaches from the study of the state of the art and the corresponding system architecture.

## 3.1 Methodology

The following section will cover the system engineering framework methodology that served as a base for the project development. It begins by describing the Automotive SPICE (ASPICE) approach and its main principles, such as requirements and definition of system architecture. Secondly, the V-model process, a standard of ASPICE, is characterized, by referring to its several stages. The section concludes by characterizing the Model-Based Systems Engineering (MBSE) approach, which served as the cornerstone of the development process. It details the specific benefits of adopting this methodology, particularly for the initial development of a complex system such as the BMS.

## 3.1.1 Automotive SPICE (ASPICE)

The development of this project is fundamentally based on system engineering principles and the ASPICE framework. System engineering provides a structured approach to product development, ensuring that all stakeholder needs are systematically addressed and validated throughout the development process [55]. ASPICE, on the other hand, offers a comprehensive process assessment model for the automotive industry, focusing on software, hardware, and systems engineering practices [56].

## 3.1.1.1 V-model process

The V-model process is a standard in the automotive industry that ensures systematic development and validation of systems. It is a graphical representation of a system's development life cycle, illustrating the relationships between each development phase and its associated testing phase [56]. This approach is essential for developing complex systems like BMS, ensuring that each requirement is validated and verified at every stage [22, 57, 58].

A key principle of the V-model, and a core rule of the ASPICE framework, is the integration rule. This rule mandates that integration testing should not proceed until the components to be integrated have been individually unit-tested. This sequential approach ensures that individual components are functioning correctly before they are combined, minimizing the risk of compounding errors during integration.

Figure 3.1 exemplifies a V-model for the BMS development process, showcasing the verification/validation interaction between the several layers of both sides of the model.

Figure 3.1: V-model process for BMS development, from [22]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_040.png)

## 3.1.1.2 Needs and requirements analysis

The ASPICE framework begins with an elicitation of needs and requirements from the stakeholder, which in this case was FSFEUP. This initial step was fundamental in understanding the team's necessities and constraints, ensuring that the proposed solution aligns with their expectations. This gathering process is referred to in ASPICE as SYS.1, and for this work, the requirements raised were based on these three references: FSFEUP needs and requirements, FS rules [6], and also current commercial BMS specifications [59].

Once the stakeholder needs are clearly defined, the next step is to derive specific system requirements from these needs. This process is referred to as SYS.2 and it involves translating high-level stakeholder requirements into detailed, actionable system requirements [56]. These requirements serve as a sketch for the design and development phases, ensuring that the system fulfills all identified needs and performs with alignment between stakeholder expectations.

Table 3.1 summarizes the main SYS.2 requirements obtained from the SYS.1 elicitation, structuring the requirement description, priority, and its origin.

Table 3.1: Summary of SYS2 requirements for BMS development

| SYS.2-ID | Requirement Description | Priority | SYS.1-Decompose |
| - | - | - | - |
| SYS.2-01 | The BMS must measure each cell volt- age that is connected in series. | High | FS Rule |
| SYS.2-02 | The BMS must measure the tempera- ture of at least 30% of the cells equally distributed in the battery pack to a limit of 60ºC. | High | FS Rule |
| SYS.2-03 | The BMS must estimate the SOC of the battery pack. | High | Commercial BMS Speci- fication |
| SYS.2-04 | The BMS must measure the battery pack current. | High | FS rules |
| SYS.2-05 | The BMS must monitor the critical cell unbalance and initiate balancing when needed | High | Commercial BMS Speci- fication |
| SYS.2-06 | The BMS shall communicate with the vehicle's ECU using the CAN protocol. | High | FSFEUP Requirement |
| SYS.2-07 | The BMS must have a UI to perform battery configurations. | Medium | FSFEUP Requirement |
| SYS.2-08 | The BMS must have a UI to display rel- evant information such as battery SOC, pack voltage, average temperature, and pack current. | Medium | FSFEUP Requirement |
| SYS.2-09 | The BMS must disconnect the Tractive System via the Shut Down Circuit in the event of critical cell voltage, cell temperature, or pack current | High | FS Rule |
| SYS.2-10 | The BMS must light up the "AMS" light in the cockpit in the event of the BMS opening the SDC. | High | FS Rule |
| SYS.2-11 | The BMS must be adaptable for differ- ent battery configurations. | High | FSFEUP Requirement |
| SYS.2-12 | The BMS must be adaptable for differ- ent cells. | Medium | FSFEUP Requirement |
| SYS.2-13 | The BMS must communicate to the ECU the charging and discharging cur- rent limit. | High | Commercial BMS Speci- fication |
| SYS.2-14 | The BMS must diagnose over/under voltage, over/under current, over/under temperature, and the health of the pack. | High | Commercial BMS Speci- fication |

## 3.1.1.3 System architectural design

The project definition cycle culminates in the design of the system architecture. This architecture was developed to thoroughly understand the interactions not only between the internal components of the BMS but also the external interactions with other systems such as the battery, ECU, charger, and other vehicle components. This architectural design process is referred to as SYS.3 in the ASPICE framework [56]. Figure 3.2 illustrates the two highest levels of the system architecture developed. In Figure 3.2a, the main relevant interactions between the TSAC and other vehicle components that have a direct or indirect relationship with the BMS are represented. On the other side, Figure 3.2b illustrates the main interactions within the TSAC that have relevance to the BMS operation.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_041.png)

(a) High-level system architecture of TSAC interactions with other vehicle systems

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_042.png)

- (b) High-level system architecture of interactions within the TSAC

Figure 3.2: System architecture of the TSAC internal and external interactions

By mapping out these interactions, we ensure a comprehensive approach that addresses both internal system coherence and external compatibility, thereby facilitating an integrated BMS solution.

## 3.1.1.4 Model Based System Engineering (MBSE)

MBSE is an advanced approach in systems engineering that formalizes the application of modeling principles, methods, languages, and tools to support the entire lifecycle of complex, interdisciplinary systems. While the practice of MBSE is still progressing, it is expected to become a standard practice in systems engineering, embracing various application domains beyond hardware and software systems [55].

While testing BMS on actual batteries can be effective in some situations, utilizing MBSE presents valuable advantages in terms of reducing costs, minimizing test duration, ensuring reproducibility, and mainly enhancing safety due to not risking real-world system operation [22]. This approach is particularly advantageous for large battery systems undergoing rigorous operating conditions or fault scenarios, especially in the BMS development for the FSFEUP team as it goes through the initial stages of development.

MBSE allows for a structured and systematic management of the complexities inherent in battery systems. Through comprehensive simulation and system analysis, MBSE significantly reduces the reliance on physical prototypes, thereby speeding up the development process. It also enhances requirement traceability, ensuring all system components align with specified requirements and function as intended [22].

## 3.1.2 Tools

To facilitate the development process of this thesis, several tools were employed, each serving a distinct purpose.

Matlab was the primary tool used, not only for programming scripts but also for various tasks using apps such as:

- Simulink, a block diagram environment used for model-based design, was utilized to run simulations and test various control algorithms. This environment allows for the modeling, simulation, and analysis of dynamic systems, making it an essential tool for validating the behavior of control systems in the project
- System Composer, an app developed to enable the specification and analysis of architectures for MBSE and software architecture modeling, was used for an initial system architecture design to have a more comprehensive overview of the interactions between BMS and other systems, as seen in Figure 3.2
- Requirements Toolbox allows users to link and validate requirements within Simulink or Matlab. It was utilized to link system architecture with requirements documented in the Requirements Editor.

- App Designer was utilized for creating two user interfaces. One is to simplify the battery model parametrization process, while the other permits the user to configure and test different scenarios, analyzing the response of the BMS.
- Curve Fitting App allows users to fit curves and surfaces to data interactively, providing tools for data exploration, model selection, and goodness-of-fit analysis.

Other tools were used such as Miro for brainstorming sessions and diagram development allowing for collaborative idea generation. PlotDigitizer, an online data extraction tool, was utilized for extracting necessary data from cell datasheet, aiding in accurate parametrization and validation of battery models.

## 3.2 Previous BMS analysis

To gain a deeper understanding of the current BMS setup in the FSFEUP01 vehicle, a thorough analysis and discussion were conducted with the team. This aimed to identify the primary issues arising from the FSFEUP01 performance and to explore potential opportunities for improvement. Figure 3.3a shows the TSAC as installed in the vehicle highlighting the various key components relevant to the BMS operation, such as temperature sense cables and acquisition board, voltage sense cables, and the Hall effect sensor. Figure 3.3b presents a block diagram of the commercial Orion BMS, illustrating the connections between the centralized BMS block, the battery pack, and other components like the charger, DC load, and current sensor.

Figure 3.3: TSAC (a) and Orion BMS block diagram (b) in the FSFEUP01 vehicle

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_043.png)

The Orion BMS, as a commercial solution, offers both strengths and challenges relevant to the team's needs. A SWOT analysis was conducted, focusing on maintaining and reinforcing strengths and opportunities while aiming to eliminate or reduce weaknesses and threats. The analysis is summarized below.

Strengths The Orion BMS is recognized for its reliability, ensuring consistent performance under various conditions while providing precise cell voltage measurements. Additionally, this solution offers great compatibility with different Li ion cells, providing adaptability to the usage of different cells. Moreover, it offers a fixed-cost solution, which simplifies budgeting and financial planning of the team. Utilizing a centralized topology, this enhances a compact architecture, as previously mentioned.

Weaknesses A centralized topology also presents the disadvantage of limited scalability, as it restricts the expansion of the battery configuration, in this case to a maximum of 180 cells in series. Additionally, the system exhibits a suboptimal balancing control algorithm (voltage-based), causing the system to enter the balancing state more frequently than necessary. This limitation was highlighted by the team and led to thermal problems, with excessive balancing generating undesirable temperature increases. The team also reported high complexity in the assembly of the BMS in the vehicle. Furthermore, the system lacks versatility in adapting its controls to different usage conditions.

Opportunities On the opportunities side, there is potential to develop a scalable solution design, providing a future-proof system that can adapt to various configurations and cell types. Furthermore, implementing advanced control algorithms, such as improved cell balancing control and sophisticated current control calculations, could enable the system to handle different usage scenarios effectively, providing versatility. Enhancing fault diagnosis capabilities and improving the estimation of the SOC, providing a more accurate alternative to the current coulomb counting technique employed by the commercial system.

Threats The main threat lies in the potential alteration of the rules of the FS competition. Since the selection of the Orion BMS was based on its compliance with current regulations, future changes may pose challenges that the BMS software might not be able to address. Additionally, any modifications to these rules could necessitate significant updates or even replacements to ensure continued compliance and functionality.

Figure 3.4 illustrates the summary of the SWOT analysis made of the commercial Orion BMS.

## 3.3 New BMS configuration

The proposed solution utilizes a master slave architecture, with multiple slave modules connected via daisy chain communication to the master module. The slave modules are tasked with acquiring cell voltages and the temperatures of critical cells using NTC thermistor sensors. Each slave module also integrates a cell balancing circuit, specifically employing switched shunt passive balancing. This method is chosen for its low complexity and reduced cost, as it is already integrated into most ICs.

Figure 3.4: Orion BMS SWOT analysis

| Strengths | Weaknesses |
| - | - |
| .Reliability .Fixed cost .Accurate measurement .Compatability .Compact | .Low scalability .Poor balancing control .High assembly complexity .Low versatility |
| Opportunities | Threats |
| .Scalable architecture .Improve control algortihms .Improve fault diagnosis .Improve SOC estimation .Increase versatility | .Competition rules alteration |

The master module is responsible for the current acquisition, achieved through the use of a Hall effect sensor and a conditioning circuit to amplify and filter the sensor signal. This proposal leverages the existing sensor from the FSFEUP01 system, providing cost savings and ensuring backward compatibility between versions 01 and 02.

Additionally, the master module handles the computation of all control algorithms described in Chapter 6, as well as the communication between internal systems, slave modules, and external systems such as the ECU (via CAN) and the latching PCB. The latching PCB manages both the shutdown circuit and the accumulator management system (AMS) cockpit light, which activates when the shutdown circuit is triggered by the BMS. This PCB receives a digital signal from the BMS, operating as follows: a 5V signal indicates normal operation while switching to 0V signifies a critical fault requiring the vehicle to enter a safe state.

Figure 3.5 illustrates the high level architecture of the proposed BMS and its primary interactions with the battery ECU and latching PCB.

Figure 3.5: Proposed BMS architecture

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_044.png)

## Chapter 4

## Battery Modelling and Simulation

This chapter describes the entire process of parametrization of the battery model. Firstly, it is described the process of parametrizing the battery model used in Simulink, using a block named Datasheet Battery. Following this, the hybrid battery model was parameterized in stages, starting with the Kibam model, then parametrizing the electric part of the model, and concluding with tests with the complete model. The chapter concludes with an explanation of the UI developed to automate the parametrization process of the hybrid battery model.

## 4.1 Battery modelling

The purpose of simulating is to analyze the behavior of the battery and test the implementation of different controls. Matlab offers advanced software for technical computing and system design, featuring an extensive library for various applications.

## 4.1.1 Simulink battery block parametrization

To represent the cell in current use by the team, the Datasheet Battery block, illustrated in Figure 4.1, from the Powertrain Blockset library, was utilized. This block allows for the accurate representation of battery characteristics by utilizing manufacturer data.

Figure 4.1: Datasheet battery block from Simulink [60]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_045.png)

This block uses lookup tables for the open circuit voltage, Em, and internal resistance, Rint, to determine the battery output voltage. These lookup tables are functions of the state of charge (4.1) and battery temperature (4.2), characterizing the battery performance at various operating points:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

The block calculates the battery output voltage, VT , using the following equation:

<!-- formula-not-decoded -->

which can be represented by the circuit presented in Figure 4.2:

Figure 4.2: Battery model used by the Simulink battery block

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_046.png)

For SOC update, the block utilizes the coulomb counting method as seen in the equation:

<!-- formula-not-decoded -->

where SOC0 and Capbatt represent the initial SOC and capacity of the battery respectively. The variable Ibatt represents the current flowing from the battery, where a positive current indicates battery discharge and a negative current indicates battery charge.

In this work, the Molicel model INR-18650-P28A was used as a reference due to its application in the FSFEUP02 prototype. In Table 4.1 are the detailed specifications of the cell present in its datasheet.

For parameterization matters, the curve fitting app available on Matlab was not the most viable option due to the block usage of lookup table array to represent the battery output voltage. In figure 4.3, the discharge rate characteristics of the cell, as provided in the datasheet, is illustrated. This graph allows for the extraction of data on the battery's voltage relative to the charge extracted, using five different constant discharge currents: 0.56A, 2.8A, 10A, 20A, and 30A.

As seen in equation 4.1, the block relates the OCV lookup table data with a lookup table of SOC breakpoints of the same length. The process of parametrizing this array began with extracting the nominal current (2.8A) discharge curve data from the datasheet using PlotDigitizer, which was then transferred to the Matlab workspace. The charge extracted (mAh) was converted into SOC (%) in order to have the same variables used by the simulink block to perform the parametrization, For this conversion the following equation were used:

Table 4.1: Molicel model INR-18650-P28A datasheet cell characteristics

|  |  |  |
| - | - | - |
| Cell Characteristics | Cell Characteristics | Cell Characteristics |
| Capacity | Typical Minimum | 2800 mAh 10.3 Wh 2600 mAh 9.56 Wh |
| Cell Voltage | Nominal Charge Discharge | 3.6 V 4.2 V 2.5 V |
| Charge Current | Standard Maximum | 2.8 A 6.0 A |
| Charge Time | Standard | 1.5 hour |
| Discharge Current | Maximum | 35 A |
| Internal Resistance | AC (1 KHz) DC (10A/1s) | 20 mΩ (Max) 20 mΩ (Max) |
| Ambient Temperature | Charge Discharge | 0°C to 60°C -40°C to 60°C |
| Energy Density | Volumetric Gravimetric | 610 Wh/l 220 Wh/kg |

Figure 4.3: Discharge rate characteristics graph from cell datasheet

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_047.png)

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

For the cell capacity (Ah) it was used the typical capacity value of the cell presented in the datasheet (Table 4.1), 2.8Ah. Function 4.7, presented in the following works [16, 45], was used in the parametrization process of the voltage array as it presented optimal results when compared to other mathematical equations [16].

<!-- formula-not-decoded -->

In this equation, kV1 represents the SOC, and the coefficients a, b, c, d, e and f are determined through curve fitting to match the experimental data.

A parametrization function was developed in order to approximate the voltage over SOC set of data extracted from the datasheet to equation 4.7. Initially, predefined parameters a, b, c, d, e and f are set. In each iteration, the electric model generates voltages using the current parameters introduced as test conditions. The objective function calculates the error as the standard deviation of the differences between simulated and reference voltages. Additionally, it computes the mean relative error to ensure accuracy across varying voltage levels.

The parameters are then adjusted in the parametrization function to minimize this error. If the error improves, the parameters are slightly modified using a random variation function. If the error does not improve, larger adjustments are made, and the parameters revert to their previous values.

The function iterates, adjusting parameters until the error falls below a set threshold or the maximum number of iterations is reached. Once the error is minimized, the function outputs the optimized parameters. Figure 4.4 illustrates a flowchart of the heuristic process described above.

Figure 4.4: Heuristic flowchart for the electric model parametrization process

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_048.png)

Table 4.2 demonstrates the coefficients a, b, c, d, e and f obtained from the parametrization process.

Table 4.2: Coefficients obtained in the fitting of Equation 4.7

| Coefficients |
| - |
| a = -0.3451 b = 0.0992 c = 6.3473 × 10-7 d = -4.0329 × 10-5 e = 0.0044 f = 3.4137 |

In figure 4.5 can be visualized the precise parametrization between the function 4.7 with the parameters found and the datasheet 2.8 A constant discharge curve.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_049.png)

Capacity(mAh)

Figure 4.5: Comparison of fitting plot and the plot extracted from datasheet

To precisely conclude the accuracy of the parametrization, the point to point error between the curves was made, and Table 4.3 presents the obtained results:

Table 4.3: Errors between curves presented in 4.5

| Errors |
| - |
| Max error = 2.0690% |
| Mean error = 0.1468% |
| Standard deviation = 0.3355% |

In order to obtain the desired value to be used in Datasheet Battery block, the open circuit voltage table data, the equation 4.3 was used this time in the following format:

<!-- formula-not-decoded -->

where VT was the output voltage obtained from the parametrization of equation 4.7. The value used for Ibatt was 2.8 A since it was the curve of reference in the process, and for Rint it was used the max internal resistance value present in the datasheet 4.1, 20 mΩ since there is no other value of reference.

The parameterized block was then tested in Simulink to visualize its preciseness and Figure 4.6 shows the comparison between the datasheet curve extracted and the output voltage given by the block in the simulation.

Figure 4.6: Comparison of the plotted datasheet curve and the Simulink simulation curve - discharge with 2.8 A

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_050.png)

The results were satisfactory for cell simulation wise, with the errors between the curves being presented in Table 4.4:

Table 4.4: Errors between curves presented in 4.6

| Errors |
| - |
| Max error = 15.9939% |
| Mean error = 1.4635% |
| Standard deviation = 2.3025% |

Other discharge currents were then tested, to have a more detailed comparison between the Datasheet graph, Figure 4.3, and the Simulink block. The results obtained by the block can be seen in Figure 4.7.

In Simulink, the use of a lookup table for simulation introduces certain limitations. Even though the stoppage condition was made at 2.5 V as done in the Datasheet, the model is unable to stop precisely at 2.5 V during high current scenarios, even with a very small sample time in the simulation, as seen in Figure 4.7. For comparison wise, Table 4.5 shows the difference between the charge extracted values from the cell datasheet and the charge extracted of the Simulink block, using 2.8 Ah as cell capacity in the block.

Figure 4.7: Discharge rate characteristics graph from Matlab with C=2.8 Ah

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_051.png)

Table 4.5: Comparison of charge extracted of the block used in the Simulink discharge simulation, with C=2.8 Ah, with the values extracted from the datasheet

| Current (A) | Datasheet charge extracted (mAh) | Simulink block charge extracted (mAh) |
| - | - | - |
| 0.56 | 2846.53 | 2800 |
| 2.8 | 2728.53 | 2800 |
| 10 | 2728.53 | 2800 |
| 20 | 2772.68 | 2800 |
| 30 | 2728.53 | 2800 |

The overall results were satisfactory, obtaining a relative mean error between charge extracted values of 0.65%. Nevertheless, after analyzing the results and the 0.56 A discharge characteristics curve, it was noted that the charge extracted, 2.846 mAh, was higher than 2.8 Ah. Given that the cell has a capacity of 2.8 Ah, it would be impossible to reach those values. Therefore, a new simulation was conducted in Simulink with C=2.846 Ah. Figure 4.8 presents the new results obtained.

It is noted that the curves are now stopping closer to 2.5 V at higher discharge currents and Table 4.6 presents the difference between the charge extracted values from the cell datasheet and charge extracted of the Simulink block, using 2.846 Ah as cell capacity in the block.

The new results demonstrated a reduced relative mean error between the charge extracted values compared to the previous simulation that used 2.8 Ah as the cell capacity. This updated simulation resulted in a relative mean error of 0.47%.

The CC-CV charging scenario was also implemented in Simulink, aiming not only to compare the block simulation response to that presented in the datasheet but also to facilitate further tests on charging current control. In order to recreate this, the control presented in Figure 4.9 was implemented, where Cell Volt was the output voltage of the battery block and 4.201 was the value Table 4.6: Comparison of charge extracted of the block used in the Simulink discharge simulation with C=2.846 Ah with the values extracted from the datasheet used as the maximum cell voltage limit. This maximum cell voltage value was calculated using equation 4.3. The Ibatt value was set to -0.05 A, which corresponds to the minimum current value reached at the end of the CV charging cycle. The internal resistance, Rint, was 20 mΩ, and the open-circuit voltage, Em, was set to the maximum cell voltage limit of 4.2 V. Kp was initialized with the value 50, 1/Rint, but was then tuned to 18 after some tests, in order to reduce noise that was occurring in the CV curve.

Figure 4.8: Discharge rate characteristics graph from Matlab with C=2.846 Ah

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_052.png)

| Current (A) | Datasheet charge extracted (mAh) | Simulink block charge extracted (mAh) |
| - | - | - |
| 0.56 | 2846.53 | 2846 |
| 2.8 | 2728.53 | 2846 |
| 10 | 2728.53 | 2846 |
| 20 | 2772.68 | 2839.51 |
| 30 | 2728.53 | 2833.33 |

Figure 4.9: CC-CV charging current calculation

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_053.png)

Figure 4.10 and Figure 4.11 demonstrate the charging characteristics at 1C (2.8 A) obtained from the simulink and cell datasheet, respectively.

Both figures indicate a similar duration for the CC phase, followed by the CV phase, and the overall charging time in both graphs is nearly identical, further validating the simulation model's effectiveness in replicating the actual cell performance during charging.

Figure 4.10: CC-CV charge characteristics from Matlab

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_054.png)

## 4.1.2 Battery model description

The hybrid battery model based on the coupling of Kibam and the electric model was selected for its several advantages presented previously in Section 2.7.3.7. Figure 4.12 illustrates the hybrid model, representing the interactions between both models.

Figure 4.12: Hybrid battery model representation, adapted from [46]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_055.png)

The following sections present the parametrization of the hybrid battery model to be applied, starting with an initial validation of the Kibam model by comparing results with established references. The section then proceeds to the parametrization of both Kibam and the electric model, concluding with the results of the parameterized hybrid model.

## 4.1.2.1 Kibam model characterization

In order to simulate the Kibam model, the system of equations 4.9, adapted from [9], was utilized.

Figure 4.11: CC-CV charge characteristics adapted from from cell datasheet

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_056.png)

<!-- formula-not-decoded -->

With y1,0 = y1 (t0), y2,0 = y2 (t0) and y0 = y1,0 + y2,0, where y1 (t0) an y2 (t0) represent the quantity of liquid stored in tank 1 and 2, respectively, at the initial time, t0 [9]. The k' constant is obtained from:

<!-- formula-not-decoded -->

where k represents the valve conductivity between tank 1 and tank 2, and the variables c1 and c2 represent the capacity of tank 1 and 2, correspondingly.

In order to obtain the SOC (%) of both tanks, the following equations, adapted from [9], were utilized:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

where C represents the cell total capacity in Ampere second (As). As mentioned in Chapter 2 and seen in Figure 4.12, the SOC of tank 1 and 2 represent the available and bound SOC, respectively. The available SOC being the charge that is readily available for immediate use, while the bound SOC represents the charge that is initially not available for discharge but can gradually move into tank 1.

In order to validate this system of equations and the mathematical transcription of the model, following simulations were made in order to compare the response of the model with some test experiments made in the cited reference.

In the experiment made in [9], a battery with a capacity of 1Ah was used. It was subjected to a discharge current of 3A (3C) for a duration of 500 seconds. Following this period, the discharge current was turned off, allowing the battery to rest for 500 seconds. After this resting period, the battery was once again subjected to a discharge current of 3C for another 500 seconds. The same parameters from the reference were used for this simulation, and can be seen in Table 4.7.

The variables h1 and h2, as seen in Figure 4.12, represent the liquid height in tanks 1 and 2, and can be obtained by the equations 4.13 and 4.14, respectively:

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Table 4.7: Parameters for the Kibam, from [9]

| Parameters | Symbolic Variable | Value |
| - | - | - |
| Total battery capacity (in As) | C | 3600 |
| Capacity of tank 1 | c1 | 0.3 |
| Capacity of tank 2 | c2 | 0.7 |
| Diffusion constant | k′ | 0.005 |
| Initial height in tank 1 | h1(0) | 3600 |
| Initial height in tank 2 | h2(0) | 3600 |

Figures 4.13 and 4.14 illustrate the results of the experiment presented in [9] and the results obtained, respectively. These figures demonstrate identical results, thereby validating the use of the equations to represent Kibam.

Figure 4.13: Kibam model simulation results, from [9]

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_057.png)

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_058.png)

Figure 4.14: Kibam model simulation results obtained from the experiment

## 4.1.2.2 Kibam model parametrization

This next section is dedicated to explaining the process of the Kibam model parametrization. The searched variables of the system of equations 4.9 were parameters k and c1. The value of c2 was not subject to parametrization, since the capacity of tank 2 can be obtained with equation 4.15.

<!-- formula-not-decoded -->

The following heuristic, seen in Figure 4.15, was used for the process of searching for the desired values.

The parameterization function implements the parametrization process for the Kibam model by optimizing the parameters k and c1. The code begins by initializing variables, including discharge times from the cell datasheet and initial guesses for the parameters k and c1. It then simulates the discharge process for the various currents presented in the datasheet, using the Kibam model. The Objective function compares the simulated discharge times to those in the datasheet, calculating a cost based on the mean relative error and standard deviation. An optimization loop iteratively adjusts the values of k and c1 to minimize this cost, using a function based on the derivative analysis of the error. The loop continues until the cost falls below a predefined threshold or the maximum number of iterations is reached.

Figure 4.15: Heuristic flowchart for the Kibam model parametrization process

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_059.png)

After an extensive search, the parameters c1 and k that satisfied the desired cost were determined to be c1 = 0.956 and k = 0.00001. Table 4.8 presents a comparative analysis of the discharge times derived from the datasheet, the Simulink block, and the Kibam model, simulating the five discharge currents specified in the datasheet.

Table 4.8: Comparison of discharge time of the block used in the Simulink simulation and the Kibam model parameterized with the values extracted from the datasheet

| Current (A) | Datasheet discharge time (s) | Simulink block discharge time (s) | Kibam model discharge time (s) |
| - | - | - | - |
| 0.56 | 18299.1 | 18800 | 18105 |
| 2.8 | 3508.02 | 4000 | 3549 |
| 10 | 982.27 | 1040 | 985 |
| 20 | 499.082 | 520 | 491 |
| 30 | 327.424 | 340 | 328 |

Table 4.9 presents a comparison of the relative errors in discharge times for the Simulink block and the Kibam model, relative to the datasheet values.

The table highlights the accuracy of the Kibam model in predicting the discharge times for various currents. The average relative error for the Kibam model stands at 0.86%, demonstrating its high fidelity in replicating the datasheet discharge characteristics. In contrast, the Simulink block exhibits higher errors, particularly at 2.8 A where the error reaches 14.02%. This greater error is again attributed to the limitation of the lookup table to stop at a predefined condition. In this case, the stopping condition was defined as the SOC of the cell reaching zero.

Table 4.9: Relative errors in discharge times of the Simulink block and Kibam model compared to the datasheet

| Current (A) | Simulink block relative error (%) | Kibam model relative error (%) |
| - | - | - |
| 0.56 | 2.74 | 1.06 |
| 2.8 | 14.02 | 1.17 |
| 10 | 5.88 | 0.28 |
| 20 | 4.19 | 1.62 |
| 30 | 3.84 | 0.18 |

## 4.1.2.3 Electric model parametrization

To parametrize the electric model, the following equation 4.16 was utilized:

<!-- formula-not-decoded -->

Note the difference from the previous equation 4.7, since this time the aim is to parametrize an equation that relates the open circuit voltage in order of the SOC value received from the Kibam model, here also represented by kV1.

The curve fitting application was employed to perform this parametrization. Data from the 0.56A discharge curve, extracted from the datasheet, was used since this test is conducted with the lowest current and, thus, is the most representative of the open circuit response of the cell. The output voltage data was adapted to open circuit voltage by applying equation 4.8, where the values of Ibatt and Rint were 0.56 A and 20 mΩ, respectively. Figure 4.16 illustrates the sampled values extracted from the datasheet alongside the fitted Voc function utilized. Table 4.10 presents the goodness of fit metrics, which include the sum of squared errors (SSE), the coefficient of determination (R-square), the adjusted R-square (Adj R-sq), and the root mean square error (RMSE).

Table 4.10: Goodness of Fit

| Metric | Value |
| - | - |
| SSE | 0.0134 0.9985 0.9984 0.0118 |
| R-square |  |
| Adj R-sq |  |
| RMSE |  |

The curve fitting process allows for the determination of the coefficients a, b, c, d, e and f of equation 4.16 with a precision of 96%. The slight deviation in the fitting curve for SOC values near zero is noted, however, this error is negligible as the discharge of the cell is never conducted below 5%, as required by the team. The coefficients obtained are presented in Table 4.11.

Figure 4.16: Sampled values and the resulting curve fitting by the Voc function

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_060.png)

Table 4.11: Coefficients obtained in the fitting of 4.16

| Coefficients |
| - |
| a = -0.1501 b = 0.1697 c = 2.1877 × 10-7 d = -2.2205 × 10-14 e = 0.0062 f = 3.3720 |

## 4.1.2.4 Hybrid model results

This section presents the results obtained from the integration of the previously parameterized Kibam and Electric models into the proposed Hybrid model. In order to validate the comparison between the fully parameterized model and the experimental data available on the datasheet of the cell, the following discharge tests were conducted.

The first test conducted on the hybrid model was the discharging with the five different constant currents presented in the datasheet (0.56 A, 2.8 A, 10 A, 20 A, and 30 A), with the stoppage condition being the output voltage of the cell reaching its minimum limit value of 2.5 V. Figure 4.17 illustrates the individual overlap of both discharge rate characteristics curves obtained from the hybrid model and the ones presented in the datasheet, Figure 4.3.

In order to compare the results presented in Figure 4.17, Table 4.12 demonstrates the comparison of charge extracted values from the datasheet with the obtained results from the discharging tests of the hybrid model. This comparison highlights the differences in charge extraction under various constant current discharge tests.

Figure 4.17: Comparison of Hybrid Model and Datasheet for various discharge currents

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_061.png)

Table 4.12: Comparison of charge extracted of the hybrid model with stopping condition of Vout=2.5 V with the datasheet values

| Current (A) | Datasheet charge extracted (mAh) | Hybrid model charge extracted (mAh) |
| - | - | - |
| 0.56 | 2846.53 | 2941.87 |
| 2.8 | 2728.53 | 2874.67 |
| 10 | 2728.53 | 2813.89 |
| 20 | 2772.68 | 2755.56 |
| 30 | 2728.53 | 2666.67 |

Table 4.13 presents the relative error between the hybrid model's charge extraction values and the datasheet values as shown in Table 4.12.

The overall results of these tests presented an average relative error of 2.94%, demonstrating a close agreement between the hybrid model and the datasheet values when the stopping condition of the discharge was the cell minimum voltage limit.

Table 4.13: Comparison of relative error between the hybrid model and datasheet values presented in Table 4.12

| Current (A) | Relative Error (%) |
| - | - |
| 0.56 | 3.35 |
| 2.8 | 5.35 |
| 10 | 3.13 |
| 20 | 0.62 |
| 30 | 2.27 |

The next test conducted followed a similar methodology to the previous one, with the key difference being that this time the stoppage condition was defined by the available SOC, specifically when the SOC of tank1 reached zero. This new test aims to evaluate the accuracy of the model in estimating the SOC during the discharging process since SOC will be a paramount parameter in the control implemented by the BMS, as it will be demonstrated in Chapter 5.

Figure 4.18 illustrates the results obtained from the different constant current discharges of the Hybrid model for this new test.

Figure 4.18: Discharge rate characteristics of Hybrid model with available SOC=0% as stoppage condition

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_062.png)

Table 4.14 presents the comparison between the datasheet and the hybrid model with respect to the charge extracted during the various constant current discharge tests.

Table 4.15 summarizes the accuracy of this discharge scenario with the Hybrid model, showcasing the relative error between each discharge current test.

The results obtained underscore the accuracy of the Hybrid Model in estimating the SOC in comparison to the charge extracted during the cell's discharge. The analysis reveals an average relative error of 0.86%, thereby demonstrating the model's precision in replicating the battery's discharge behavior.

Table 4.14: Comparison of charge extracted of the Hybrid model with stopping condition of available SOC=0% with the values extracted from the datasheet

| Current (A) | Datasheet charge extracted (mAh) | Hybrid model charge extracted (mAh) |
| - | - | - |
| 0.56 | 2846.53 | 2816.33 |
| 2.8 | 2728.53 | 2760.33 |
| 10 | 2728.53 | 2736.11 |
| 20 | 2772.68 | 2727.78 |
| 30 | 2728.53 | 2733.33 |

Table 4.15: Comparison of relative error between the Hybrid model and Datasheet values presented in Table 4.14

| Current (A) | Relative Error (%) |
| - | - |
| 0.56 | 1.06 |
| 2.8 | 1.17 |
| 10 | 0.28 |
| 20 | 1.62 |
| 30 | 0.17 |

This reduction of error, from the test stopping by Vout=2.5 V to this where the stoppage condition is set to SOC=0%, was expected and is explained based on the error present on the fitting produced by Matlab, as seen in Figure 4.16. To better understand the deviation of overall preciseness between the two tests, Figure 4.19 illustrates the difference of error between stopping by voltage and SOC variable.

Figure 4.19: Difference of error between stopping by voltage and SOC

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_063.png)

## 4.2 User Interface (UI) for battery parametrization

Since the whole process of parametrizing the battery model adopted is extensive and of complex understanding, a UI was developed in Matlab App Designer to automate the process of parametrization of the hybrid model. The code behind the UI is based on the parametrization codes developed previously and presented in the heuristics 4.4 and 4.15.

## 4.2.1 UI inputs

In order to utilize this UI the user needs to introduce the following inputs:

- Internal Resistance of the cell (in Ohms)
- Maximum cell capacity (in Ah)
- Maximum and minimum voltage limit (in Volts)
- Nominal voltage (in Volts)
- Maximum current limit (in Amperes)
- Charge extracted at maximum current (in mAh)
- Maximum cost desired for the fitting (in %)
- Maximum number of iterations permitted for the running of the parametrization codes
- Battery configuration: number of cells in series and parallel
- Vout(SOC) data about the discharge of the cell preferably obtained with the minimum current presented in the datasheet
- The minimum current (in Amperes) value used to obtain this Vout(SOC) data
- The charge extracted (mAh) in this discharge scenario with minimum current

The Vout(SOC) discharge data should be related to the one with the minimum current available in the datasheet since it is the closest to representing the open circuit scenario. Either way, these values are transformed into Voc(SOC) points, by adding Rint*I, since it is the data desired for the electric model parametrization function. The UI requests voltage values, Vout, at specific SOC points: 0%, 20%, 40%, 60%, 80%, and 100%.

## 4.2.2 UI outputs

After the UI is correctly filled with the inputs mentioned above the user can then proceed to click on the "Parametrize" button. The UI will run its code, performing the discharge in the same conditions mentioned as the data introduced, until the max iterations are reached or the parameters are found inside the desired max cost defined.

In both scenarios of reaching the maximum iterations or obtaining the desired parameters within the cost desired, the UI will present the following outputs:

- Maximum voltage estimated (in Volts), obtained by multiplying the maximum voltage limit by the number of cells in series of the configuration
- Minimum voltage estimated (in Volts), obtained by multiplying the minimum voltage limit by the number of cells in series of the configuration
- Maximum current estimated (in Amperes), obtained by multiplying the max current limit by the number of cells in parallel of the configuration
- Estimated charge extracted value (in mAh) from the model in the discharge scenario
- Estimated time of discharge of the cell (in seconds), if the user also desires to compare this value with the expected, even though the discharge time of the cell is not a required input of the UI
- The found parameters of the recent search for both electric (a, b, c, d, e and f ) and Kibam model (c1,k)
- The average standard deviation and average relative error (both in %) between the voltage curve outputted by the model and the voltage points of data introduced
- The relative error (in %) between the estimated charge extracted value (in mAh) of the model and the charge extracted value introduced in the UI
- A graph presenting the estimated Vout(SOC) curve of the battery model (with the battery parameters outputted) and the Vout(SOC) points of the data introduced by the user.

The graph provides a user-friendly visualization of the parameterized hybrid model's accuracy by comparing it to the input datasheet data. If the parameter search does not yield satisfactory results within the desired cost constraints, the user can re-initiate the optimization process by adjusting the maximum number of iterations and clicking the "Parametrize" button again.

Figure 4.20 demonstrates the UI in operation, illustrating all the previous descriptions.

Figure 4.20: User interface in work

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_064.png)

## 4.2.3 Final remarks

The UI developed offers a comprehensive solution to the complexities involved in the hybrid model parameterization process. By automating this process, the UI significantly reduces user effort and enhances the accuracy and efficiency of battery parameterization.

One of the primary advantages of this UI is its user-friendly approach. The extensive and often intricate process of parametrizing a battery model is streamlined, allowing users to input essential data directly from the cell datasheet. This reduces the complexity and technical expertise required, making the tool accessible to a broader range of users.

Furthermore, the UI permits the battery model to adapt to different cells, providing futureproofing for the solution. This ensures that the system can easily accommodate changes in the battery cell type, complying with requirement SYS.2-12.

In addition to its flexibility, the UI enhances reliability by allowing users to input experimental data obtained from actual cell experiments. This feature is particularly valuable for validating the battery model against real-world performance, ensuring that the parameters generated are accurate and applicable. The ability to use experimental data also means that the UI can adapt to variations and discrepancies that may not be covered by standard datasheet values.

Moreover, the UI proves to be a valuable tool for ongoing maintenance and optimization. As batteries undergo usage cycles and experience changes in performance characteristics, the ability to re-parametrize the model ensures that the battery management system remains accurate and efficient over time.

Overall, the UI developed for battery parametrization demonstrates significant advancements in ease of use, flexibility, and reliability. By automating complex processes and providing tools for ongoing adaptation, it supports robust and efficient battery management, aligning with the project's objectives and user needs.

## Chapter 5

## Model based simulation

This chapter details all the model based simulation blocks of the system architecture defined, focusing on the roles and interactions of the BMS slave and master blocks. Firstly, the BMS system architecture is introduced, and the slave functionalities are described. The chapter proceeds to detail the BMS master block controls and algorithms implemented, including cell power loss representation, battery model integration, critical voltage and temperature calculation, cell balancing control, internal resistance estimation, current control algorithms, fault diagnosis, and communication between different components. The chapter concludes with the UI developed for simulating different configurations and scenarios, allowing for comprehensive testing and analysis of the BMS and battery performance.

## 5.1 Model based architecture

The system architecture base of the MBSE, illustrated in 3.5, will be detailed in the following sections, from the functionalities of the slave module to the control blocks and algorithms implemented in the master module. As battery representation in the Simulink environment, it was utilized the block parameterized in 4.1.1, to analyze the expected behavior and perform tests accordingly.

## 5.2 BMS slave block

The slave module is connected to the battery pack in order to obtain two essential parameters: voltage of all cells and temperature of at least 30% of the cells equally distributed within the pack [6]. Both these measurements are defined rules for the BMS in the competition, making them mandatory requirements to be met, complying with requirements SYS.2-01 and SYS.2-02. The slave IC is responsible for measuring the cell's voltage, while an external temperature sensor is responsible for the temperature acquisition. This measurements are then communicated to the master module. The slave module also includes support for the internal passive cell balance, commanded by the master control, detailed in 5.3.4.

## 5.3 BMS master block

This section provides a comprehensive detail of the functionalities implemented and tested in the master module of the BMS. The master module, as mentioned previously, monitors and processes data from the slave modules, which handle cell voltage and temperature measurements. Additionally, the master is responsible for processing the current value transmitted by the current sensor through the usage of a conditioning circuit, as illustrated in the system architecture, fulfilling requirement SYS.2-04. The master functionalities will be described and discussed in the following sections

## 5.3.1 Cell power loss representation

Temperature is highly influential in battery performance, especially Li-ion batteries. Everything that happens inside of the battery is thermo-electrochemical, so the power we get out of the battery depends a lot on the ambient conditions. In order to have control over the influence of temperature on current, and vice versa, this block was developed.

The logic of this block is based on performing a Weighted Temperature Averaging (WTA) process. The room temperature is used as an input and is adjusted based on the power losses generated within the cell during charging, discharging, and balancing.

The block calculates the power losses produced in the cell due to internal resistance and balancing currents, integrating these losses into the ambient temperature to derive the cell temperature. The calculation of losses is as follows:

<!-- formula-not-decoded -->

where Rint and Rbalance represent the cell internal resistance and cell balance resistor, respectively. Figure 5.10 illustrates this circuit for a better understanding. The resistance of the cell balancing MOSFET utilized was despised for power loss calculations. The Icell and Ibalance denote the current flowing in the cell and the balancing current, respectively. It is important to note that this block is not for estimation but rather for representation, ensuring that the simulated relationship between current and temperature reflects on real-world scenarios. The value k was adjusted differently for both charge and discharge scenarios to achieve this representation, however, it was not derived from a detailed parametrization process.

This approach ensures that the cell temperature is influenced by both the ambient temperature and the heat generated due to high current values, causing the temperature to rise. Conversely, it accounts for the decrease in temperature as the current reduces over time. Figure 5.1 illustrates the implemented WTA block in Simulink to represent this influential relation between current and temperature in the cell.

One of the reasons this block was developed was due to the team problem in the FSFEUP01 of unexpected temperature raises during charging specially when the balancing occured, which could be prevented if the losses were considered. This thermal considerarion will also be utilized in the calculations of charge and discharge current limits presented in 5.3.6.

Figure 5.1: Simulink block modeling the relationship between cell current and temperature

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_065.png)

Figure 5.2 demonstrates the relationship between current and temperature during a discharge cycle. For this test the following parameters were used: Room temperature = 25ºC and k = 0.35.

Figure 5.2: Demonstration of current influence on temperature during a discharge test

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_066.png)

This test demonstrates the impact of current reduction on temperature stabilization when a certain temperature limit is reached. In this specific case, the temperature limit was set at 55°C. Upon reaching this threshold, the current is reduced to prevent further temperature increase. As depicted in the graph, this reduction in current results in the stabilization of the temperature. During the discharge process, a fault occurred, causing the current to drop to 0 A. Following this fault, we can observe a gradual decrease in temperature, eventually returning to ambient room temperature.

## 5.3.2 Battery model block

To represent the battery behavior under dynamic conditions and have an accurate SOC estimation, the hybrid model presented in 2.7.3.7 and parameterized in 4.1.2 was employed. This hybrid model integrates the advantages of electrochemical and equivalent circuit models, offering a comprehensive representation of the battery's performance. As previously mentioned, this model requires both the current value flowing through the cell and the initial SOC of the cell as input parameters, in addition to the model parameters and the cell's internal resistance and capacity, to function effectively.

This block was utilized for cells with both initial maximum and minimum SOC to enable further control implementations. These controls are based on the cells at the extremes, as they represent the operational boundaries. The SOC of the battery pack is determined by the cell with the minimum SOC, rather than the average SOC of all cells since the battery pack's usable capacity is limited by the cell with the lowest SOC, as this cell will be the first to reach the discharge limit and thus terminate the operation of the entire pack. Therefore, to meet the requirements and minimize computational effort, only the battery model blocks for the cells with the minimum, presented in Figure 5.3, and maximum SOC were utilized. This approach ensures compliance with the SOC requirements (SYS.2-03) while reducing unnecessary computational load by avoiding the modeling of all individual cells.

Figure 5.3: Battery model block implemented in Simulink for the lowest SOC cell

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_067.png)

It is important to note that the SOC transmitted from the Kibam model to the electric model is that of Tank 1, as it represents the available SOC of the cell.

## 5.3.2.1 Initial SOC function

As explained above, the battery model requires two essential input values: initial SOC and current of the cell. The cell current value is continuously measured. However, to automate the input of the initial SOC value (seen in Figure 5.3 as SOCinicial), this function was created. This function estimates the initial maximum and minimum SOC by reading the OCV of all cells and identifying the extreme values. Once identified, these values are applied to a sigmoidal SOCinit(Voc) function to obtain the SOC of those cells. The Matlab curve fitting app was again utilized to parametrize the following sigmoidal function:

<!-- formula-not-decoded -->

Figure 5.4 illustrates the sampled values extracted from the datasheet alongside the fitted SOCinit function utilized.

Figure 5.4: Sampled values and the resulting curve fitting by the SOCinit function

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_068.png)

Table 5.1 presents the goodness of fit metrics, as previously described in 4.1.2.3.

Table 5.1: Goodness of fit presented in Figure 5.4

| Metric | Value |
| - | - |
| SSE | 41.1161 0.9987 0.9986 1.3089 |
| R-square |  |
| Adj R-sq |  |
| RMSE |  |

The curve fitting process allows for the determination of the coefficients a, b, and c of equation 5.2 with a precision of 96%, and are presented in Table 5.2.

Table 5.2: Coefficients obtained in the fitting of function 5.2

| Coefficients |
| - |
| a = 108.7827 b = 4.50 c = 3.6491 |

This function allows the user to initialize the vehicle without manually inputting the initial SOC of the battery, achieving this by enabling the BMS to perform an OCV reading at the initial stage of usage.

## 5.3.3 Critical Voltage and Temperature Calculation Blocks

Two blocks are employed in order to identify the maximum and minimum values of both cell's voltage and temperature, received from the slave module, as these extreme values are valuable parameters for both control implementations and fault diagnosis. In the voltage block, apart from the maximum and minimum value, it is also calculated the Pack voltage by adding the voltage of cells connected in series, as illustrated in Figure 5.5a. The temperature block is identical but calculates the average temperature instead, as demonstrated in Figure 5.5b. Both pack voltage and average temperature are requirements imposed by the team's needs.

Figure 5.5: Maximum and Minimum Value Blocks for Voltage (a) and Temperature (b)

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_069.png)

## 5.3.4 Cell balancing command control

This block is responsible for controlling the cell balance command sent to the slave module. It analyzes the DeltaSOC, the difference between the maximum and minimum SOC across the cells, to ensure it falls within the defined limits for cell unbalance, therefore complying with requirement SYS.2-05.

The control process begins by reading the minimum and maximum SOC values from the cells. If the maximum SOC is greater than the setpointstartbalance, set to 85, the system proceeds to calculate the DeltaSOC. If the balance command is active, equal to 1, the system checks if the DeltaSOC is less than setpointfinish, set to 2, which is the interval desired for DeltaSOC. If true, the balancing is stopped by setting the balance command to 0. Conversely, if the balance command is not active, the system checks if the DeltaSOC exceeds the setpointstart, set to 5. If true, the balancing is initiated by setting the balance command to 1, otherwise the balance command stays equal to 0.

The flowchart in Figure 5.6b details this decision-making process on the balancing control, with Figure 5.6a illustrating the implemented block in Simulink demonstrating the inputs and outputs described above.

In Figure 5.6a can also be seen the input of the VehicleState, which assumes the values of 0 and 1 for the discharging and charging process, respectively. This input is needed since the balance only occurs during the charge mode. DeltaSOC is also outputted from the block for diagnostic purposes as excessive unbalance could lead to prolonged balancing durations.

Figure 5.6: Cell Balance Control Block (a) and Flowchart (b)

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_070.png)

## 5.3.4.1 Cell balancing tests

Different simulations were made on this balancing control, analyzing not only its response under different test conditions but also its performance compared to the balance control implemented on Orion BMS. The commercial BMS balance control is based merely on the voltage difference, DeltaVolt, between the cells [59]. Upon discussion with the team, it was confirmed that the DeltaVolt configured in the BMS to initiate balancing was set to 10 mV, as recommended by the BMS distributor.

The first test involved having all cells with the same initial SOC (0%) but different internal resistances: while most of the cells had an Rint equal to 0.02 Ω, one specific cell was imposed to have a higher Rint value of 0.03 Ω. This test was conducted with two main goals: to observe the balancing control upon a recurrent real-world scenario of Rint disparities and compare the implemented balance control with the one disposed in Orion BMS. Important to note that this initial test was to only analyze the balancing control so balancing was not performed. For this initial test, three different constant charging currents were utilized: -6 A, -2.8 A, and -0.5 A.

The -6A constant current discharging results are presented in Figure 5.7. Figure 5.7a demonstrates the difference of voltage between the cells with different Rint, while Figure 5.7b demonstrates the same SOC between those cells during the whole charging period. In Figure 5.7c, we can compare the balance control commands of both the proposed control implemented and the commercial BMS, with 1 and 0 representing the control for balancing to initiate and finish, respectively.

The charging stopped after 1523 seconds due to reaching a fault limit of the maximum voltage permitted to the cell, and the battery ended the charging with a SOC of 89.92%. We can visualize

1600

Figure 5.7: Comparative analysis during -6 A constant current charging: (a) Voltage comparison of cells with different Rint, (b) SOC comparison of cells with different Rint, and (c) Balance command comparison between the proposed control method and the commercial BMS.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_071.png)

that after the charging stopped, and the current was set to 0 A (OCV), the voltage of the cells was the same, highlighting the fact that balance was not needed. This voltage difference was exclusively caused by the different Rint of the cells. This difference in internal resistance did not affect the SOC of the cells, which remained the same throughout the charging process, as expected. As there was no SOC difference between the cells, the implemented balance control remained inactive for the entire charge cycle.

The second test conducted was similar to the previous with the only difference being the constant charge current used, this time being -2.8 A. The objective of the simulation was the same but tested with a reduced current to analyze the expected reduction of the voltage difference between the cells with different Rint. The results are presented in Figure 5.8.

In this case, the charging had a duration of 3548 seconds before being stopped by the same fault limit that occurred in the first test, and the battery ended up with a SOC of 97.7%. We can visualize similar results to the previous test, with the expected reduction of DeltaVolt. Despite the reduction, the DeltaVolt remained greater than 10 mV, leading the control implemented by the Orion BMS to still enter the balancing state, while the balance control proposed remained inactive since DeltaSOC is equal to zero.

Figure 5.9 presents the results of this last test conducted with a constant charge current of -0.5 A.

The battery pack reached full SOC (100%) after 20 337 seconds, at which point the charging process was terminated. It is noted that the DeltaVolt remained under 10 mV, as expected due to the low charge current. This reduction led to both controls not sending commands to start balancing, as seen in Figure 5.9c.

Figure 5.8: Comparative analysis during -2.8 A constant current charging: (a) Voltage comparison of cells with different Rint, (b) SOC comparison of cells with different Rint, and (c) Balance command comparison between the proposed control method and the commercial BMS.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_072.png)

Figure 5.9: Comparative analysis during -0.5 A constant current charging: (a) Voltage comparison of cells with different Rint, (b) SOC comparison of cells with different Rint, and (c) Balance command comparison between the proposed control method and the commercial BMS.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_073.png)

We can conclude from this test that SOC is a more reliable variable for the balancing control than voltage, as previously mentioned in Table 2.3. This greater precision of the SOC variable is related to its capacity to interpret the system's inconsistencies, such as Rint disparities across the battery pack.

This second test was conducted under conditions similar to the previous one. Almost all cells had an Rint equal to 0.02 Ω, with one specific cell imposed to have a higher Rint value of 0.03 Ω. The main difference in this test was that the cell with the higher Rint started with an initial SOC different from zero, unlike the rest of the cells, to analyze not only the implemented balance control but also observe the system's response during the balancing state. The CC-CV charging method, previously implemented and demonstrated in Figure 4.9, was used for charging the battery. The main goals were to analyze the performance of the proposed balance control and to validate the hypothesis that balancing should start later rather than sooner to reduce balancing time. This approach justifies the control logic where balancing begins only after reaching a certain setpointstartbalance value.

This hypothesis is based on the fact that the balancing current, Ibalance, is higher when the voltage of the cell, Vcell, is also higher. The balancing current is obtained with the following equation:

<!-- formula-not-decoded -->

where Rbalance and Rint represent the balance resistor and cell internal resistance, respectively. The resistance of the cell balancing MOSFET was again despised. The passive balancing circuit implemented is presented in Figure 5.10.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_074.png)

Rbalance

Figure 5.10: Passive balance circuit of the cell, adapted from Figure 2.19

In order to validate this hypothesis, two scenarios were simulated. In the first one, the balancing was set to start whenever the DeltaSOC was greater than the setpointstart, and the setpointstartbalance was equaled to zero. The second test is conducted to make the balance start only after the maxSOC reaches the setpointstartbalance value, therefore retarding the balancing process. The balance resistor utilized in the experiment was 10 Ω and 0,02 Ω for the internal resistance of the cell.

Figure 5.11 demonstrates the results obtained from the first balancing test. Figure 5.11a illustrates both DeltaSOC and the balance command sent by the master to the slave. The difference between the maximum and minimum SOC can be visualized in Figure 5.11b. Lastly, Figure 5.11

demonstrates the voltage of the cell with maximum SOC during balancing and its relation with the balancing current.

Figure 5.11: First balancing test: (a) Delta SOC and balance command. (b) Max SOC and min cell SOC during charging (c) Voltage of the cell and current of balance.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_075.png)

We can observe that balancing commenced immediately at the beginning and continued for 2597 seconds until the DeltaSOC reached the desired difference of 2% (setpointfinish).

The second test was done under the same conditions, except that the setpointstartbalance was now equal to 85. Figure 5.12 presents the results obtained from the simulation.

Figure 5.12: Second balancing test: (a) Delta SOC and balance command. (b) Max SOC and min cell SOC during charging. (c) Voltage of the cell and current of balance.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_076.png)

From Figure 5.12c, it is evident that the balancing current was higher, resulting in a balance duration of 2115 seconds. This represents a reduction of 18.56% in balance time compared to the previous test.

This reduction in balancing time comes at a higher cost in terms of power losses, due to the increased balancing current. This underscores the importance of considering the losses incurred during balancing, as discussed in Section 5.3.1.

## 5.3.5 Internal resistance estimation

The implemented battery model allows for the estimation of the internal resistance of the critical cell, defined as the cell with the highest SOC. This estimation is performed using the following equation:

<!-- formula-not-decoded -->

where Vout and Voc(SOC) represent the maximum cell voltage measurement and open circuit voltage estimation of the critical cell, respectively.

As discussed in Section 2.7.2.3, the estimation of internal resistance serves as a simple and accurate method for evaluating the SOH of the battery. Although SOH estimation was not a requirement imposed by the team, given that the health of cells does not degrade significantly within the context of FS cars due to the limited number of cycles they undergo, internal resistance estimation was employed to diagnose and detect the end-of-life (EOL) of a cell. As previously mentioned, the EOL is defined as the point where the SOH drops below 80%. To detect this scenario, the following procedure was implemented: the maximum voltage measured for a cell is 4.2 V (Table 4.1), which corresponds to a SOC of 100% at the end of a charge if the cell has an SOH of 100%. This 4.2 V value is used, subtracting the OCV (Voc) of the cell corresponding to an SOH of 80%, which, according to the datasheet, is 3.9 V. The current value, Icell, used in this calculation is 0.05 A, as specified in the datasheet as the cutoff current at the end of charging. These values are applied to equation 5.4, yielding an internal resistance estimation of 6 Ω. The output of this estimation is directed to the fault diagnosis block, presented in Section 5.3.7. When the Rint estimation reaches this critical value, the system triggers a fault alarm message, indicating that the critical cell needs to be replaced.

## 5.3.6 Current control algorithm

An essential function of the BMS is to determine the current limits for both charging and discharging processes. These calculations are critical, mainly for an FS car, as they enhance safety and improve the vehicle's performance across different types of competition events.

This section presents the implemented algorithm for calculating both charge and discharge current limits. This calculation considers multiple factors, such as temperature, voltage, the difference of SOC between tanks 1 (available charge) and 2 (bound charge) of the battery model, and the fault signal. To manage the charging process, the cell with the maximum SOC is designated as the controlling cell, as it is the most critical to observe. This is because the most charged cell dictates the upper limit of the charging current to prevent overcharging. Conversely, during the discharging process, the cell with the minimum SOC becomes the critical cell, as it dictates the lower limit to prevent excessive discharge. Figure 2.17 illustrates the influence these critical cells exert in both scenarios.

## 5.3.6.1 Discharging current limit

As previously mentioned, the minimum SOC cell commands the discharging process, with the control algorithm being based on several parameters. Each parameter has a specific algorithm, and all were simulated in isolation to observe their individual responses, and are presented below.

Voltage-Based Current Limit Algorithm The most basic algorithm implemented is related to the cell voltage. For this control, the following equation, based on the Rint battery model, was utilized to determine the current value:

<!-- formula-not-decoded -->

where VMinLimit represents the minimum cell voltage limit during discharge, set to 2.5V as indicated in Table 4.1. Voc is the estimated open circuit voltage outputted from the battery model of the minimum SOC cell. This current value is then saturated between 0 and the maximum allowable discharge current, which is 35A per parallel connection in the battery configuration.

Figure 5.13 presents the results obtained from a discharge scenario controlled solely by this voltage algorithm. Figure 5.13a demonstrates the current limit throughout the discharge, as well as the estimated Voc controlling the algorithm and the fault signal. When the fault signal is one, it indicates that everything is functioning correctly; when it is zero, it signifies that a fault has occurred. The charge extracted during the discharge is presented in Figure 5.13b.

Figure 5.13: Current control with voltage algorithm: (a) Open circuit voltage (V), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_077.png)

A fault signal indicating that the battery had reached the 5% discharge limit, a threshold set by the team, was detected. This triggered the system to reduce the current to zero, thereby terminating the discharge process. The total charge extracted at the end of the discharge was 2698 mAh.

Temperature-Based Current Limit Algorithm The next simulation involved a discharge test where the current limit was controlled exclusively by a temperature-based algorithm. This procedure employs a temperature hysteresis mechanism to regulate the current. The control algorithm works by monitoring the maximum cell temperature and the power losses produced in the cell. When the temperature approaches a critical threshold, a corrective action is triggered to reduce the current. Specifically, if the temperature exceeds a defined limit minus a buffer value, the algorithm calculates a reduction in the current to prevent overheating. This reduction increases proportionally with the extent to which the temperature exceeds the threshold. For this test, the initial current limit was set to a maximum value. The control algorithm begins to decrease the current once the temperature exceeds 55°C, ensuring that the cell temperature does not surpass the maximum limit of 60°C. To support the analysis of this temperature control, the previously implemented block representing the power losses was utilized in parallel with this simulation. The constant K value used in the power loss block was set to 0.35, and the proportional controller in the algorithm was set to 2. Figure 5.14 presents the results obtained from the temperature control algorithm.

Figure 5.14: Current control with temperature algorithm: (a) Temperature (ºC), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_078.png)

We can observe that the algorithm does not permit the temperature to exceed its limit while keeping the temperature near the limit by reducing the current as needed. The temperature is kept near the limit in order for the vehicle to maintain its high performance which is crucial when referring to an FS car. The total charge extracted at the end of the discharge was slightly higher than the previous test with a value of 2700 mAh (Figure 5.14b), and the fault causing the current to pass to zero was the same as the previous.

Under the same conditions, another test was conducted using only the voltage algorithm. However, this time the current was factored into the power loss block, with the same constant K value of 0.35. As shown in Figure 5.15, the discharge process resulted in an increase in temperature, eventually reaching the maximum temperature limit of 60°C. This triggered the fault signal associated with the maximum temperature limit, reducing the current to zero.

The charge extracted from the cell was 1556 mAh (Figure 5.15b), representing a significant decrease. This result underscores the importance of incorporating the temperature algorithm, which considers the reciprocal effects of current on temperature.

Figure 5.15: Current control with voltage algorithm and temperature influence: (a) Temperature (ºC), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_079.png)

Delta SOC-Based Current Limit Algorithm The next test focused on controlling the difference between the SOC of tanks 1 and 2 in the Kibam model. This control mechanism optimizes the utilization of bound charge from tank 2 by adjusting the current, thereby managing the decrease in available capacity more effectively. The control algorithm operates by monitoring the difference in SOC between the two tanks. If this difference exceeds a predefined setpoint, the algorithm calculates a corrective action to adjust the current. The corrective action is proportional to the extent by which the SOC difference exceeds the setpoint, ensuring that the bound charge from tank 2 is optimally utilized, and allowing the system to dynamically adjust the current to maintain an optimal balance between the SOC of the two tanks.

The selection of the setpoint depends on the type of competition event the vehicle will undergo. A higher setpoint value, closer to 100, allows the battery to sustain higher current values for a longer duration, enhancing performance during high-demand events. Conversely, a lower setpoint value increases the vehicle's autonomy by reducing the current, which is beneficial for endurance events.

The algorithm also limits the current to a minimum usable value, set to 2.8A, ensuring that the vehicle continues to operate efficiently. The proportional controller utilized in the algorithm to adjust the current was set to 2,5.

The first test using this algorithm was conducted with a setpoint value of 5, simulating an endurance-type event. The objective of this test was to analyze the vehicle's extended performance during discharge. Figure 5.16 presents the results from this simulation. In Figure 5.16a we can analyze the differences in SOC between the tanks, DeltaSOC, and its influence on the current control.

From this simulation, it is evident that the battery lasted significantly longer before reaching its 5% SOC limit, primarily due to the reduction in higher current usage. The charge extracted from the cell was the highest among all the control tests conducted, as expected, with a value of 2713 mAh (Figure 5.16b).

The second test was conducted under the same conditions as the previous one, with the exception of the setpoint being set to 100. As mentioned earlier, this higher setpoint is ideal for acceleration-type events where maximum performance is a priority. It allows the battery to deliver maximum current until it is no longer feasible. This approach is generally safe for the battery and vehicle, as acceleration events, unlike endurance events, are typically of short duration. The results of this simulation are presented in Figure 5.17.

Figure 5.16: Current control with DeltaSOC algorithm for endurance events: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_080.png)

Figure 5.17: Current control with DeltaSOC algorithm for acceleration events: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) Charge extracted during discharge (mAh).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_081.png)

We can observe the delivery of maximum current value for an extended period, leading to a reduction in the charge extracted to 2699 mAh, as illustrated in Figure 5.17b.

Full Control Implementation Finally, Figure 5.18 presents the combined performance of all the control algorithms previously discussed. For this specific test, the parameters used in the individual tests were maintained, with the setpoint for the DeltaSOC control set to 50.

The simulation resulted in a discharge time of 1453 seconds before reaching the 5% fault limit, and a charge extracted of 2709 mAh (Figure 5.18c).

This control implemented for the discharging limit calculation provides versatility in adapting to different FS event conditions while optimizing current usage. Furthermore, this control enhances safety by prioritizing the fault signal in the current control calculation. This approach ensures that the vehicle operates within safe parameters, preventing overheating and over-discharging of the cells, by dynamically adjusting the current limits based on voltage, temperature, and SOC differences of tanks 1 and 2 of the Kibam model.

Figure 5.18: Current control with all control algorithms: (a) Current limit (A) and Fault signal values; (b) Control parameters: DeltaSOC (%), Open circuit voltage (V), and Temperature (ºC); (c) Charge extracted during discharge (mAh).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_082.png)

## 5.3.6.2 Charging current limit

The charging current limit control logic is similar to the discharging control logic but with adjustments to the parameters and limits used. In the charging state, as previously mentioned, the maximum cell voltage manages the control, unlike the discharge control which is commanded by the minimum cell voltage.

Voltage-Based Current Limit Algorithm The initial control algorithm implemented is based on the maximum open circuit voltage estimated. The allowable current is calculated using the following equation, derived from the Rint battery model:

<!-- formula-not-decoded -->

where VMaxLimit represents the maximum cell voltage limit during discharge, set to 4.25V as indicated in Table 4.1 and taking into consideration the 0.05 V tolerance from the manufacturer. Voc is the estimated open circuit voltage outputted from the battery model of the maximum SOC cell. This current value is then saturated between 0 and the maximum allowable charge current (6 A), multiplied by the number of parallel connections in the battery configuration. Rint represents the cell's internal resistance and it was set to the tabled value of 0.02 Ω. Figure 5.19 presents the results obtained from the charging test. Figure 5.19a demonstrates the estimated OCV utilized in the algorithm, and also the calculated maximum current and fault signal. In Figure 5.19b it also presented the SOC of the battery pack during the charging.

Figure 5.19: Current control with voltage algorithm: (a) Open circuit voltage (V), Current limit (A), and Fault signal values; (b) SOC of the battery pack (%).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_083.png)

We can observe that this charging algorithm closely follows the CC-CV method. The charging duration was 2776 seconds before reaching the team's desired end value of 100% SOC in the battery pack, which subsequently triggered the fault signal.

Temperature-Based Current Limit Algorithm The next simulation involved controlling the charging current limit using a temperature-based algorithm. This algorithm employs a temperature hysteresis mechanism to regulate the current, similar to the one presented in the discharging algorithm. The control algorithm monitors the maximum cell temperature and reduces the current as the temperature approaches a critical threshold, preventing overheating.

The algorithm begins to decrease the current once the temperature exceeds 55°C, ensuring it does not surpass the maximum limit of 60°C. The proportional control constant used in the algorithm was set to 2, and the power loss block's constant (K) was initially set to 0.35, as used previously but adjusted to 8 for effective visualization on the charging process. Figures 5.20a and 5.20b depict the results of this temperature control algorithm.

Figure 5.20: Current control with temperature algorithm: (a) Temperature (ºC), Current limit (A), and Fault signal values; (b) SOC of the battery pack(%).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_084.png)

The charging process stopped after 1666 seconds due to reaching the maximum cell voltage, with a final SOC of 95.55%, showing the control was ineffective in achieving the desired fully charged battery.

Under identical conditions, another test was conducted using only the voltage algorithm, with the current also influencing the power loss block (K = 8). The results of this charging simulation are presented in Figure 5.21.

Figure 5.21: Current control with voltage algorithm and temperature influence: (a) Temperature (ºC), Current limit (A), and Fault signal values; (b) SOC of the battery pack(%).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_085.png)

We can observe that the system would enter a safe state after 1153 seconds upon reaching the maximum temperature fault, reducing significantly the SOC of the battery to only 68.25%. This outcome underscores once again the necessity to corroborate the controls, meaning the simple control with voltage parameters would be ineffective.

Delta SOC-Based Current Limit Algorithm As previously explained, one of the algorithms applied is based on controlling the difference between Tanks 1 and 2, referred to as DeltaSOC, in the Kibam model. In the charging scenario, setting a higher setpoint value results in faster charging, while a lower setpoint value leads to a longer charging duration with lower current values. Below are two simulations using this algorithm with setpoints of 60 and 20. In both scenarios, the proportional controller value was set to 2.5, and the minimum current value used in the algorithm was 0.01A. The results obtained from the charging simulation using a higher control setpoint of 60 are presented in Figure 5.22b.

Figure 5.22: Current control with DeltaSOC algorithm: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) SOC of the battery pack (%).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_086.png)

The charging process concluded after reaching the desired 100% SOC of the battery pack, with a total charging duration of 3410 seconds.

Figure 5.23 presents the results obtained from the charging simulation using the DeltaSOC algorithm with a lower setpoint control value of 20.

Figure 5.23: Current control with DeltaSOC algorithm: (a) DeltaSOC (%), Current limit (A), and Fault signal values; (b) SOC of the battery pack (%).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_087.png)

We observe an expected increase in charging duration, resulting in a total charge time of 15,656 seconds before achieving the desired 100% SOC in the battery pack.

This adjustable control algorithm is valuable for the team as it allows them to adapt the charging duration based on their specific needs. If more time is available for charging, they can opt for a longer, safer charging process. Charging with higher currents increases power losses and may necessitate additional cell balancing during the charging process, potentially impacting the cell's lifespan [61]. This flexibility ensures that the battery can be charged in a manner that balances performance with longevity, based on the team's requirements and available time.

Full Control Implementation Figure 5.24 illustrates the results obtained by integrating all three control algorithms. The parameters used in this experiment were consistent with those in previous tests, with the setpoint for the DeltaSOC control algorithm set to 60. Figure 5.24a shows the current control limit and fault signal value, which is triggered when the pack reaches 100% of SOC as seen in Figure 5.24c. The control parameters of the charging simulation are presented in Figure 5.24b.

The charging process lasted for 3670 seconds before the battery was fully charged.

An additional factor influencing the current control limit calculation for the charging process is cell balancing. Whenever the balancing command is activated, the current limit for charging is set to 0 until the balancing process is completed and the command is turned off.

## 5.3.7 Fault Diagnosis

The fault diagnosis system in the BMS is crucial for ensuring the safety performance of the battery pack, vehicle, and most importantly the user. The system continuously monitors several parameters to detect potential faults and trigger appropriate responses.

Critical faults necessitate immediate action to prevent damage to the battery or the vehicle. When a critical fault is detected, the current control signal is set to zero as seen before, and a signal is sent to the latching PCB to open the shutdown circuit and turn on the cockpit light, complying with both SYS.2-9 and SYS.2-10, respectively. The parameters monitored for critical faults implemented in the fault diagnosis include:

Figure 5.24: Current control with all control algorithms: (a) Current limit (A) and Fault signal values; (b) Control parameters: DeltaSOC (%), Open circuit voltage (V), and Temperature (ºC); (c) SOC of the battery pack (%).

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_088.png)

The battery pack's SOC is monitored to ensure it stays within safe and desired limits. The team requires the battery to be fully charged at the end of the charging process, setting the upper limit for this parameter at 100%. For discharging, the team has decided to maintain a lower limit of 5%, ensuring maximum utilization of the battery's performance.

The DeltaSOC, indicating the difference between the SOC of the cells with the minimum and maximum SOC, is observed to prevent severe imbalances. Upon detecting a significant disparity, a fault signal is activated, identifying the affected cells, which facilitates targeted actions such as switching or individually charging/discharging specific cells to efficiently restore balance without excessive balancing durations.

The pack current values are evaluated to prevent overcurrent conditions during both charging and discharging. These limits are determined based on the specifications provided in the cell datasheet, multiplied by the number of parallel connections in the battery configuration.

The cell temperatures are monitored to prevent overheating or excessively low temperatures. These critical temperature thresholds are established based on both the limits specified in the cell datasheet and the 60ºC limit imposed by the rules (SYS.2-02).

Cell voltages are monitored to ensure they remain within safe operational limits as specified in the cell datasheet, also considering the manufacturer's specified accuracy of ±0.05V tolerance.

As previously mentioned, the estimated internal resistance is monitored to identify and detect the end of life of a cell. A threshold value of 6, as explained in Section 5.3.5, was established to indicate when a cell reaches the fault limit of 80% SOH. When this threshold is exceeded, it signifies that the cell needs to be replaced to maintain the overall efficiency of the battery pack.

Lastly, the accuracy of voltage estimation is maintained by comparing the estimated maximum and minimum output voltage of the battery model with the corresponding measured voltages. This procedure primarily ensures the model's precision, contributing to detecting sensor issues or misconnections.

Warning faults serve as early indicators of potential issues, using lower threshold values to provide a warning before a critical fault occurs, allowing for preventive actions to be taken. These faults use the same parameters as the critical faults but with more conservative limits.

Table 5.3 provides a summary of the monitored fault parameters along with their corresponding threshold values.

Table 5.3: Summary of fault and warning thresholds

| Parameter | Warning Threshold | Critical Threshold |
| - | - | - |
| SOC | [15% , 90%] | [5% , 100%] |
| DeltaSOC | 20% | 40% |
| Charging Current | [-5.5 A, Max Balance current (A)] | [-6 A, Max Balance current (A)] |
| Discharging Current | [0 A , 30 A] | [0 A , 35 A] |
| Charging Temperature | [10ºC , 50ºC] | [0ºC , 60ºC] |
| Discharging Temperature | [-10ºC , 50ºC] | [-40ºC , 60ºC] |
| Cell Voltage | [2.8 A , 4 A] | [2.5 A , 4.25 A] |
| Internal Resistance | 3 Ω | 6 Ω |
| Voltage Estimation Accuracy | ±0.3 V | ±0.5 V |

The BMS continuously evaluates these parameters and triggers a fault signal if any critical thresholds are breached, complying with requirement SYS.2-14. This ensures that the system takes immediate action to prevent any potential damage to the battery pack or the vehicle. The warning signals, on the other hand, provide an early indication, allowing for preventive maintenance or corrective actions to be taken before a critical fault occurs.

## 5.3.8 Communication Block

Communication is a fundamental aspect of the BMS, involving both master and slave modules. The master module handles more complex communication, as it interacts not only with the slave module internally but also with external systems such as the ECU and the latching PCB. Each communication channel has distinct purposes and requirements, including specific timing and protocols.

Internally, the communication between the slave and master modules involves the transmission of temperature and voltage data from the slave to the master, as mentioned previously. The master module, in turn, sends wake-up and balance commands to the slave module, ensuring coordinated operation.

For the ECU, the BMS transmits essential required data such as pack voltage, individual cell voltages, average cell temperature, pack SOC, pack current, and the maximum current limit for both charging and discharging (SYS.2-13). Additionally, it includes the transmission of fault and warning alarm reports to ensure profound monitoring. From the ECU, the BMS receives voltage and current values from the DC bus, and also the charging state. These communicated values were only simulated and further real-world tests are needed for validation.

The latching PCB receives the fault diagnosis signal, which triggers a safe state response, as required by the rules [6].

Figure 5.25 presents a block diagram of the communication network of the system.

Figure 5.25: BMS Communication diagram

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_089.png)

## 5.4 User Interface

A UI was developed to configure various parameters such as battery configuration, fulfilling requirement SYS.2-07, and specific simulation conditions. The user can input the desired shunt balance value for balancing and set the room temperature to analyze the system's thermal response. The UI allows real-time monitoring of the simulation and displays requested data from the team: pack voltage, average temperature, current, SOC, and the estimated internal resistance, complying with requirement SYS.2-13. Additionally, it shows the state of the vehicle, indicating whether it is in charging, discharging, balancing, or safe state mode. A graph plotting the SOC of the battery during the simulation is also provided.

Figures 5.26a and 5.26b present two simulation scenarios. Figure 5.26a shows the end of a discharge simulation where the 5% SOC limit was reached, triggering the safe state alert. Figure 5.26b depicts a charging simulation. More detailed simulation configurations are defined within the Simulink file to keep the UI user-friendly for general use.

Figure 5.26: User interface during (a) discharge and (b) charge scenarios.

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_090.png)

## 5.5 Final remarks

Upon the conclusion of the MBSE simulations, several significant improvements were detected. The balancing control implemented adds a major upgrade, as explained in Section 5.3.4.1. Both the implemented controls and those of the commercial BMS were compared in parallel. The implemented control proved to be more effective in reducing the need for balancing. Additionally, it permits the balancing process to be adapted to either an earlier or more delayed stage, depending on the team's needs.

The algorithm developed for the current control limit is also highly advanced, taking into consideration key aspects such as the voltage and temperature of the cells. This algorithm leverages the major advantage of the battery model implemented, which not only provides an accurate SOC estimation but also enhances the overall system control. The current control algorithm allows for adaptable parameters to meet the specific needs of the team for both charging and discharging, providing a versatile solution.

The fault diagnosis system presented is very detailed and comprehensive, monitoring several key parameters. This is particularly noteworthy when compared to the diagnosis capabilities of the commercial BMS, which, according to the manufacturer: "protect cells from over-voltage, under-voltage, over-current, over-temperature, and under-temperature based on the programmed minimum and maximum values in the battery profile" [59].

Overall, the enhancements made to the BMS through these simulations highlight the potential for improved performance, safety, and control reliability.

## Chapter 6

## Conclusions and Future Work

This chapter summarizes key research findings related to the development of a BMS for the FSFEUP EV. It provides an overview of the project results and discusses the extent to which the objectives outlined at the beginning were met. Additionally, this chapter addresses the recommendations for future work.

## 6.1 Satisfaction of objectives

This dissertation detailed the development and simulation of a BMS tailored for an FS EV. Both project and product objectives were successfully achieved.

In terms of project objectives, the comprehensive research conducted in the state-of-the-art review established a foundation for the system architecture definition. A MBSE approach was employed, utilizing MATLAB software for simulation and validation, and to compare the proposed BMS with the current commercial Orion BMS. A UI was developed to enable testing of various battery configurations, BMS specifications, and simulation conditions, providing a valuable tool for both the team and future developers.

Regarding the product objectives, the resulting BMS offers a reliable solution that prioritizes safety through detailed fault diagnostics and adaptability to different events through its current control mechanism. The system's reliability is further underscored by its adherence to the requirements defined by the team, encompassing not only team-specific needs but also FS rules and commercial BMS specifications. The decentralized master-slave topology aligns with the team's preference and the need for a scalable and future-proof solution, adaptable to various configurations. A UI was developed to automate the parameterization of the hybrid battery model, ensuring seamless adaptation to future cell modifications without compromising model accuracy. In terms of cost and performance balance, the system was designed to leverage existing components from the current TSAC architecture, such as the Hall effect sensor and temperature acquisition system, to minimize costs. The BMS was also developed considering the limitations of the BQ79616 IC, a cost-effective component that fulfills the system's needs.

All SYS requirements were simulated and verified throughout the document, except for SYS.206, which, while considered in the design, requires further validation on the physical prototype due to the limitations of simulating the CAN protocol communication with the ECU in the MATLAB environment. Notably, the balancing control requirement (SYS.2-05) demonstrated superior accuracy and precision compared to the Orion BMS, showcasing a significant improvement. The UIs for data analysis and configuration (SYS.2-07 and SYS.2-08) proved valuable for testing various system conditions and parameters. The adaptability to different configurations and cells (SYS.211 and SYS.2-12) was validated through the master-slave topology and the UI for automatic cell parameterization. The charging and discharging current limit (SYS.2-13) showcased adaptability to different FS events, offering a versatile control advantage.

The completion of this dissertation represents an advancement in the field of BMS for EVs, specifically within the FS context. The meticulous research and development process has not only fulfilled but surpassed the initial project goals, demonstrating considerable innovation in areas such as battery modeling, balancing control, and current limits calculation. This research has made a significant contribution to EV technology by establishing a solid framework for future BMS advancements. The successful simulation and validation of the system's performance, in comparison to commercial standards, underscore the viability and potential impact of the proposed solutions.

## 6.2 Future work

Future work could involve refining the SOC estimation by incorporating a Kalman filter, as suggested in the literature. The relationship between current and temperature could be further investigated through laboratory tests to estimate the parameter (k) accurately, enhancing the thermal model of the battery. The parameterization heuristics could be integrated into the BMS to achieve a fully autonomous parameterization process. Additionally, the Initial SOC function developed could be implemented after balancing to recalibrate the maximum and minimum cell SOC values. The fault diagnosis system could be upgraded by comparing values received from the ECU on the DC bus (pack voltage and current) with estimated and measured pack values, ensuring comprehensive validation of BMS accuracy and enhancing the system's ability to detect potential discrepancies or sensor malfunctions. The project's outlined plan for the next two years will involve creating a proof of concept (quick prototype) in the following year, culminating in the development of a final prototype ready for vehicle integration in the subsequent year.

## Bibliography

- [1] United Nations. United nations' sustainable development goals (sdgs). https://sdgs. un.org/goals, 2016. Accessed: 2024-07-26.
- [2] Mahammad A Hannan, Md Murshadul Hoque, Aini Hussain, Yushaizad Yusof, and Pin Jern Ker. State-of-the-art and energy management system of lithium-ion batteries in electric vehicle applications: Issues and recommendations. IEEE Access, 6:19362-19378, 2018. https://doi.org/10.1109/ACCESS.2018.2817655.
- [3] Formula Student website, 2024. https://www.imeche.org/events/ formula-student/about-formula-student Accessed: 14-04-2024.
- [4] FSFEUP website/aboutus, 2024. https://formulastudent.fe.up.pt/pt/ aboutus/ Accessed: 07-04-2024.
- [5] FSFEUP website/team, 2024. https://formulastudent.fe.up.pt/pt/team/ Accessed: 07-04-2024.
- [6] Formula Student Germany. Formula student rules 2024. https://www. formulastudent.de/fsg/rules/, 2024. Accessed: 2024-06-27.
- [7] Battery Management Systems course Monolithic Power Systems, 2024. https://www.monolithicpower.com/en/learning/mpscholar/ battery-management-systems Accessed: 12-06-2024.
- [8] Fazel Mohammadi and Mehrdad Saif. A comprehensive overview of electric vehicle batteries market. e-Prime-Advances in Electrical Engineering, Electronics and Energy, 3:100127, 2023. https://doi.org/10.1016/j.prime.2023.100127.
- [9] Daniel Filipe Pereira Magalhães. Modelo de baterias com aplicação em sistemas de gestão de baterias de veículos elétricos, 2013.
- [10] R Ranjith Kumar, Chokkalingam Bharatiraja, K Udhayakumar, S Devakirubakaran, Sathiya Sekar, and Lucian Mihet-Popa. Advances in batteries, battery modeling, battery management system, battery thermal management, soc, soh, and charge/discharge characteristics in ev applications. IEEE Access, 2023. https://doi.org/10.1109/ACCESS.2023. 3318121.

- [11] Michel Armand, Peter Axmann, Dominic Bresser, Mark Copley, Kristina Edström, Christian Ekberg, Dominique Guyomard, Bernard Lestriez, Petr Novák, Martina Petranikova, et al. Lithium-ion batteries-current state of the art and anticipated developments. Journal of Power Sources, 479:228708, 2020. https://doi.org/10.1016/j.jpowsour. 2020.228708.
- [12] John T Warner. The handbook of lithium-ion battery pack design: chemistry, components, types and terminology. Elsevier, 2024.
- [13] Xiaoli Sun, Zhengguo Li, Xiaolin Wang, and Chengjiang Li. Technology development of electric vehicles: A review. Energies, 13(1):90, 2019. https://doi.org/10.3390/ en13010090.
- [14] MA Hannan, Md Murshadul Hoque, Azah Mohamed, and Afida Ayob. Review of energy storage systems for electric vehicle applications: Issues and challenges. Renewable and Sustainable Energy Reviews, 69:771-789, 2017. https://doi.org/10.1016/j.rser. 2016.11.171.
- [15] Dickson NT How, MA Hannan, MS Hossain Lipu, and Pin Jern Ker. State of charge estimation for lithium-ion batteries using model-based and data-driven methods: A review. IEEE Access, 7:136116-136136, 2019. https://doi.org/10.1109/ACCESS.2019. 2942213.
- [16] Sónia Carina Lopes da Costa. Análise e desenvolvimento de um método de estimação de estado de carga de baterias baseado em filtros de kalman. 2014.
- [17] Shichun Yang, Xinhua Liu, Shen Li, and Cheng Zhang. Advanced Battery Management System for Electric Vehicles. Springer Nature, 2022.
- [18] M Berecibar, I Gandiaga, I Villarreal, N Omar, J Van Mierlo, and P Van den Bossche. Critical review of state of health estimation methods of li-ion batteries for real applications. Renewable and Sustainable Energy Reviews, 56:572-587, 2016. https://doi.org/10.1016/ j.rser.2015.11.042.
- [19] Davide Andrea. Battery management systems for large lithium-ion battery packs. Artech house, 2010.
- [20] Gregory L Plett. Battery management systems, Volume II: Equivalent-circuit methods. Artech House, 2015.
- [21] Berker Bilgin, Pierre Magne, Pawel Malysz, Yinye Yang, Vera Pantelic, Matthias Preindl, Alexandre Korobkine, Weisheng Jiang, Mark Lawford, and Ali Emadi. Making the case for electrified transportation. IEEE Transactions on Transportation electrification, 1(1):4-17, 2015. https://doi.org/10.1109/TTE.2015.2437338.

- [22] Jorge Varela Barreras. Practical methods in li-ion batteries: for simplified modeling, battery electric vehicle design, battery management system testing and balancing system control. 2017.
- [23] Xiaojun Tan, Andrea Vezzini, Yuqian Fan, Neeta Khare, You Xu, and Liangliang Wei. Battery Management System and Its Applications. John Wiley &amp; Sons, 2022.
- [24] Hermann Meissner, Rebecca Ilsen, and Jan C Aurich. Analysis of control architectures in the context of industry 4.0. Procedia cirp, 62:165-169, 2017. https://doi.org/10. 1016/j.procir.2016.06.113.
- [25] Jorge Varela Barreras, Ricardo de Castro, Yihao Wan, and Tomislav Dragicevic. A consensus algorithm for multi-objective battery balancing. Energies, 14(14):4279, 2021. https: //doi.org/10.3390/en14144279.
- [26] Bruno Manuel Baraças dos Santos. Battery management system applied to projecto fst's ev prototype, 2014.
- [27] Zachary Bosire Omariba, Lijun Zhang, and Dongbai Sun. Review of battery cell balancing methodologies for optimizing battery pack performance in electric vehicles. IEEE Access, 7:129335-129352, 2019. https://doi.org/10.1109/ACCESS.2019.2940090.
- [28] Mina Naguib, Phillip Kollmeyer, and Ali Emadi. Lithium-ion battery pack robust state of charge estimation, cell inconsistency, and balancing. IEEE Access, 9:50570-50582, 2021. https://doi.org/10.1109/ACCESS.2021.3068776.
- [29] Muhammad Uzair, Ghulam Abbas, and Saleh Hosain. Characteristics of battery management systems of electric vehicles with consideration of the active and passive cell balancing process. World Electric Vehicle Journal, 12(3):120, 2021. https://doi.org/10.3390/ wevj12030120.
- [30] Maria Mafalda Fernandes Machado. Análise e desenvolvimento de um sistema de equilíbrio de células de iões de lítio baseado num circuito ressonante. 2014.
- [31] Nourallah Ghaeminezhad, Quan Ouyang, Xiaosong Hu, Guotuan Xu, and Zhisheng Wang. Active cell equalization topologies analysis for battery packs: A systematic review. IEEE Transactions on Power Electronics, 36(8):9119-9135, 2021. https://doi.org/10. 1109/TPEL.2021.3052163.
- [32] Sonu Kumar, S Koteswara Rao, Arvind R Singh, Raj Naidoo, et al. Switched-resistor passive balancing of li-ion battery pack and estimation of power limits for battery management system. International Journal of Energy Research, 2023, 2023. https://doi.org/10. 1155/2023/5547603.
- [33] Agostinho Manuel Afonso da Rocha. Conversão de renault twingo em veículo elétrico: Sistema de alimentação. 2013.

- [34] Mohamed Daowd, Noshin Omar, Peter Van Den Bossche, and Joeri Van Mierlo. Passive and active battery balancing comparison based on matlab simulation. In Vehicle Power and Propulsion Conference, pages 1-7. IEEE, 2011. https://doi.org/10.1109/VPPC. 2011.6043010.
- [35] Yasin Izadi and Reza Beiranvand. A comprehensive review of battery and super-capacitor cells voltage-equalizer circuits. IEEE Transactions on Power Electronics, 2023. https: //doi.org/10.1109/TPEL.2023.3310574.
- [36] Md Morshed Alam, Dylan Dah-Chuan Lu, and Ricardo P Aguilera. Review of battery balancing techniques based on structure and control strategy. In 2021 31st Australasian Universities Power Engineering Conference (AUPEC), pages 1-6. IEEE, 2021. https: //doi.org/10.1109/AUPEC52110.2021.9597839.
- [37] Jeong Lee and Jehyuk Won. Enhanced coulomb counting method for soc and soh estimation based on coulombic efficiency. IEEE Access, 11:15449-15459, 2023. https://doi.org/ 10.1109/ACCESS.2023.3244801.
- [38] Ruifeng Zhang, Bizhong Xia, Baohua Li, Libo Cao, Yongzhi Lai, Weiwei Zheng, Huawen Wang, and Wei Wang. State of the art of lithium-ion battery soc estimation for electrical vehicles. Energies, 11(7):1820, 2018. https://doi.org/10.3390/en11071820.
- [39] George S Misyris, Dimitrios I Doukas, Theofilos A Papadopoulos, Dimitris P Labridis, and Vassilios G Agelidis. State-of-charge estimation for li-ion batteries: A more accurate hybrid approach. IEEE Transactions on Energy Conversion, 34(1):109-119, 2018. https:// doi.org/10.1109/TEC.2018.2861994.
- [40] Wenlu Zhou, Yanping Zheng, Zhengjun Pan, and Qiang Lu. Review on the battery model and soc estimation method. Processes, 9(9):1685, 2021. https://doi.org/10.3390/ pr9091685.
- [41] Stefano Floridia. Analysis and development of Battery Management System for electric vehicles. PhD thesis, Politecnico di Torino, 2022.
- [42] José Miguel Branco Marques. Battery management systems (bms) for lithium-ion batteries. Master's thesis, Universidade de Coimbra (Portugal), 2014.
- [43] Jinhao Meng, Mattia Ricco, Guangzhao Luo, Maciej Swierczynski, Daniel-Ioan Stroe, AnaIrina Stroe, and Remus Teodorescu. An overview and comparison of online implementable soc estimation methods for lithium-ion battery. IEEE Transactions on Industry Applications, 54(2):1583-1591, 2017. https://doi.org/10.1109/TIA.2017.2775179.
- [44] Rui Xiong, Linlin Li, and Jinpeng Tian. Towards a smarter battery management system: A critical review on battery state of health monitoring methods. Journal of Power Sources, 405:18-29, 2018. https://doi.org/10.1016/j.jpowsour.2018.10.019.

- [45] Luıs Carlos Vieira Pereira, Adriano da Silva Carvalho, and Armando Luıs Sousa Araújo. Sistema de gestão de baterias de iões de li orientado ao modelo da bateria. Ensaio, 3:1, 2013.
- [46] Masoomeh Karami, Sajad Shahsavari, Eero Immonen, Mohammad-Hashem Haghbayan, and Juha Plosila. An extension of the kinetic battery model for optimal control applications. In 2023 IEEE 32nd International Symposium on Industrial Electronics (ISIE), pages 1-6. IEEE, 2023. https://doi.org/10.1109/ISIE51358.2023.10227986.
- [47] Taesic Kim and Wei Qiao. A hybrid battery model capable of capturing dynamic circuit characteristics and nonlinear capacity effects. IEEE Transactions on Energy Conversion, 26(4):1172-1180, 2011. https://doi.org/10.1109/TEC.2011.2167014.
- [48] Dongdong Chen, Long Xiao, Wenduan Yan, and Yinbiao Guo. A novel hybrid equivalent circuit model for lithium-ion battery considering nonlinear capacity effects. Energy Reports, 7:320-329, 2021. https://doi.org/10.1016/j.egyr.2021.06.051.
- [49] Weixiang Shen, Thanh Tu Vo, and Ajay Kapoor. Charging algorithms of lithium-ion batteries: An overview. In 2012 7th IEEE conference on industrial electronics and applications (ICIEA), pages 1567-1572. IEEE, 2012. https://doi.org/10.1109/ICIEA.2012. 6360973.
- [50] AKM Ahasan Habib, Mohammad Kamrul Hasan, Ghassan F Issa, Dalbir Singh, Shahnewaz Islam, and Taher M Ghazal. Lithium-ion battery management system for electric vehicles: constraints, challenges, and recommendations. Batteries, 9(3):152, 2023. https://doi. org/10.3390/batteries9030152.
- [51] Xiaosong Hu, Kai Zhang, Kailong Liu, Xianke Lin, Satadru Dey, and Simona Onori. Advanced fault diagnosis for lithium-ion battery systems: A review of fault mechanisms, fault features, and diagnosis procedures. IEEE Industrial Electronics Magazine, 14(3):65-91, 2020. https://doi.org/10.1109/MIE.2020.2964814.
- [52] Manh-Kien Tran and Michael Fowler. A review of lithium-ion battery fault diagnostic algorithms: Current progress and future challenges. Algorithms, 13(3):62, 2020. https: //doi.org/10.3390/a13030062.
- [53] Dubravko Miljkovi´c. Fault detection methods: A literature survey. In 2011 Proceedings of the 34th international convention MIPRO, pages 750-755. IEEE, 2011.
- [54] AllDatasheet. Electronic components datasheet database. https://www. alldatasheet.com/, 2024. Accessed: 2024-07-10.
- [55] Ana Luísa Ramos, José Vasconcelos Ferreira, and Jaume Barceló. Model-based systems engineering: An emerging approach for modern systems. IEEE Transactions on Systems,

Man, and Cybernetics, Part C (Applications and Reviews), 42(1):101-111, 2011. https: //doi.org/10.1109/TSMCC.2011.2106495.

- [56] Verband der Automobilindustrie e.V. (VDA). Automotive SPICE® Guidelines: Process assessment using Automotive SPICE in the development of software-based systems. German Association of the Automotive Industry (VDA), 2nd edition, May 2023. Draft version for 2nd edition, May 2023.
- [57] Jorge Varela Barreras, Christian Fleischer, Andreas Elkjaer Christensen, Maciej Swierczynski, Erik Schaltz, Søren Juhl Andreasen, and Dirk Uwe Sauer. An advanced hil simulation battery model for battery management system testing. IEEE Transactions on Industry Applications, 52(6):5086-5099, 2016. https://doi.org/10.1109/TIA.2016.2585539.
- [58] Christian Fleischer, Dirk Uwe Sauer, Jorge Varela Barreras, Erik Schaltz, and Andreas Elkjær Christensen. Development of software and strategies for battery management system testing on hil simulator. In 2016 Eleventh International Conference on Ecological Vehicles and Renewable Energies (EVER), pages 1-12. IEEE, 2016. https://doi.org/10.1109/ EVER.2016.7476438.
- [59] Orion. Orion bms 2 specifications. https://www.orionbms.com/products/ orion-bms-standard/, 2024. Accessed: 2024-06-27.
- [60] MathWorks. Datasheet battery. https://www.mathworks.com/help/autoblks/ ref/datasheetbattery.html. Accessed: 2024-06-26.
- [61] Yang Gao, Jiuchun Jiang, Caiping Zhang, Weige Zhang, Zeyu Ma, and Yan Jiang. Lithiumion battery aging mechanisms and life model under different charging stresses. Journal of Power Sources, 356:103-114, 2017. https://doi.org/10.1016/j.jpowsour. 2017.04.084.

## Appendix A

## Cell Datasheet

| Capacity | Typical Minimum | 2800 mAh 10.3 Wh 2600 mAh 9.56 Wh |
| - | - | - |
| Cell Voltage | Nominal Charge Discharge | 3.6 V 4.2 V 2.5 V |
| Charge Current | Standard Maximum | 2.8 A 6.0 A |
| Charge Time | Standard | 1.5 hr |
| Discharge Current | Maximum | 35 A |
| Internal Resistance | AC (1 KHz) DC (10A/1s) | 20 mΩ (Max) 20 mΩ |
| Ambient Temperature | Charge Discharge | 0°C to 60°C -40°C to 60°C |
| Energy Density | Volumetric Gravimetric | 610 Wh/l 220 Wh/kg |

Figure A.1: Molicel model INR-18650-P28A

![Image](FEUP%20Porto%20-%20BMS%20for%20FS%20Electric%20Vehicle%20%28Teixeira%20Thesis%202024%29_files/img_091.png)
<!-- Converted from Thermal Management - Autonomous Cell Balancing (sszt214).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

[www.ti.com](https://www.ti.com/)

## Technical Article

## Enhance Thermal Management in EVs with Autonomous Cell Balancing

## Sudhir Nagaraj

Cell balancing is important in battery management systems for electric vehicles (EVs) because it helps extend vehicle driving ranges and ensure safe EV battery operation. Cell balancing is also required in order to correct imbalances in the battery itself. All batteries, including those found in EVs, experience unbalancing over time caused by mismatches during manufacturing processes or mismatches in operating conditions, leading to unequal aging between the cells.

A battery can only deliver a charge until its weakest cell has discharged completely, even though other cells may have plenty of charge left. Balancing the cells thus increases battery life by maximizing the capacity of the battery pack and ensuring that all of its energy is available, which in the case of an EV battery extends the driving range. Apart from maximizing battery capacity, cell balancing also ensures safe operation of the battery by preventing cell overcharge and overdischarge, both of which can lead to accelerated cell degradation and create potentially hazardous operating scenarios.

## How cell balancing works

There are two common approaches to cell balancing: active cell balancing and passive cell balancing. Active cell balancing redistributes the charge from a cell, using DC/DC converters to deliver higher capacity to cells with lower capacity. Today, cell manufacturing and sorting have improved significantly to provide cells with very low mismatch within a battery pack. Thus, it is possible to avoid balancing large mismatches in cells at the onset of operation with a large cell-balancing current. Frequent cell balancing with smaller balancing currents can manage any mismatches that develop gradually during operation.

Passive balancing removes charge from cells with more capacity, typically through thermal dissipation, until all cells have the same amount of charge. The key distinction between passive balancing and active balancing is that passive balancing does not distribute energy but rather dissipates energy until all cells with a higher initial charge finally match the cell that had the lowest charge. Passive balancing is a more popular approach given its simplicity and lower cost.

Cell capacity is often denoted by state of charge to explain the level of charge a battery has relative to its capacity. Figure 1 illustrates the differences in cell balancing types.

Figure 1. Battery state of charge in various balancing modes

![Image](Thermal%20Management%20-%20Autonomous%20Cell%20Balancing%20%28sszt214%29_files/img_001.png)

![Image](Thermal%20Management%20-%20Autonomous%20Cell%20Balancing%20%28sszt214%29_files/img_002.png)

![Image](Thermal%20Management%20-%20Autonomous%20Cell%20Balancing%20%28sszt214%29_files/img_003.png)

## Passive cell balancing in EV batteries

Passive balancing removes charge from an overcharged cell by switching in a resistor in parallel to the cell and dissipating energy into that resistor. This energy dissipation results in heat in the cells as well as the switches and resistor used for dissipation. It is vital to maintain the lithium cell temperature as close to room temperature as possible. Failing to do so may lead to thermal runaway, when the rate of internal heat generation exceeds the rate at which the heat can be released.

Lithium cells degrade at a faster rate at elevated temperatures, caused by structural changes and the formation of surface film at the electrodes. Additionally, excessive heat buildup could damage cell-balancing switches and resistors. A typical EV has large number of cells and cell-balancing switches and resistors that are often packed in close proximity, which makes managing the thermal dissipation in a battery and its battery management system during passive balancing a necessity.

## Improving EV battery safety with TI battery monitors and balancers

TI's BQ79616-Q1 performs passive cell balancing by using switches internal to the device. There is thermal dissipation inside of the BQ79616-Q1 during cell balancing because of these switches. Hotspots are on the printed circuit board (PCB) on the device and the balancing resistors. The BQ79616-Q1 provides two thermal management functions to avoid overheating the die and oversee the PCB temperature.

One thermal management function monitors the die temperature, and the other monitors the thermistor temperature. A high die temperature triggers a fault to the microcontroller (MCU), which can pause cell balancing in order to allow the integrated circuit (IC) temperature to drop. Once the IC temperature drops and the fault is clear, the MCU can command the BQ79616-Q1 to resume cell balancing.

With thermistor monitoring, the BQ79616-Q1 automatically pauses balancing if the temperature exceeds a pause threshold. When the temperature falls below a recovery threshold, balancing resumes automatically. The BQ79616-Q1 pauses and resumes cell balancing in this case without any intervention from the MCU. Figure 2 shows temperature monitoring on the device and by the thermistors.

![Image](Thermal%20Management%20-%20Autonomous%20Cell%20Balancing%20%28sszt214%29_files/img_004.png)

[www.ti.com](https://www.ti.com/)

Figure 2. BQ79616-Q1 temperature monitoring locations on the PCB

![Image](Thermal%20Management%20-%20Autonomous%20Cell%20Balancing%20%28sszt214%29_files/img_005.png)

The cell-balancing pause state also freezes all balancing timers and settings, which do resume once the device is out of the pause state. To manage thermal increases caused by external balancing resistors, the BQ79616-Q1 can pause cell balancing on all channels if any of the active thermistors connected to generalpurpose inputs/outputs detect a temperature greater than the set overtemperature cell-balancing threshold. Once overtemperature cell-balancing detection is triggered, the balancing on all enabled channels will resume once all active thermistors detect a temperature below the established recovery threshold.

Autonomous cell balancing helps maximize battery life, a key benefit for EV batteries. The addition of enhanced IC thermal management and fault indication to the MCU, as found in the BQ79616-Q1, enables quick and safe cell balancing in a cost-optimized manner for longer battery operation between chargers and a longer operational life for the EV battery.

## Additional resources

- Watch the training video, "What is Cell Balancing?"
- [Read the technical article, "How active and passive cell balancing works."](https://e2e.ti.com/blogs_/archives/b/fullycharged/archive/2016/10/05/how-active-and-passive-cell-balancing-works)
- Read the Analog Design Journal article, "Cell balancing buys extra run time and battery life."

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2023, Texas Instruments Incorporated
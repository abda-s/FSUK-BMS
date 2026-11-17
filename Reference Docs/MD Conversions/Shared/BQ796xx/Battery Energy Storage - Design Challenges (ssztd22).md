<!-- Converted from Battery Energy Storage - Design Challenges (ssztd22).pdf with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->

[www.ti.com](https://www.ti.com/)

## Technical Article

## 3 major design challenges to solve in battery energy storage systems

## Ryan Tan

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_001.png)

Solar and wind power bring renewable energy to the grid, but the imbalance between supply and demand is a major limitation to maximize their use. Although solar energy is abundantly available at noon, demand is not high enough at that time, so consumers pay more per watt.

Energy storage system (ESS) applications for utility-scale, residential, and commercial and industrial scenarios capture energy from renewable sources such as solar and wind during the day and deliver this stored energy when demand or grid electricity prices are high. By storing energy for use during peak hours, an ESS stabilizes the grid and reduces energy costs.

Design challenges associated with a battery energy storage system (BESS), one of the more popular ESS types, include safe usage; accurate monitoring of battery voltage, temperature and current; and strong balancing capability between cells and packs. Let's look at these challenges in more detail.

## Challenge No. 1: Safety

The first challenge is maintaining battery safety across the entire lifetime of a BESS, which is normally longer than 10 years. BESS applications often use lithium-ion (Li-ion) batteries, specifically lithium iron phosphate (LiFePO4) batteries.

Li-ion batteries are prone to smoke, fire or explosion if the voltage, temperature and current exceed their maximum limitations, making the battery's voltage, temperature and current data monitoring and protections highly important. Therefore, you should consider and analyze the potential for battery faults and battery management system failures.

Figure 1 demonstrates a BESS architecture. TI's Stackable Battery Management Unit Reference Design for Energy Storage Systems depicts a stackable battery management unit (BMU) that uses the BQ79616 to detect issues with redundant data measurement, while the Battery Control Unit Reference Design for Energy Storage Systems shows a battery control unit (BCU) with switches that ensures system safety.

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_002.png)

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_003.png)

Figure 1. BESS architecture

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_004.png)

## Challenge No. 2: Accurate battery monitoring

Accurate battery data ensures safety and maximizes energy. Considering the wide, flat zone of the LiFePO4 charge and discharge curve, tiny cell voltage measurement errors can cause huge remaining capacity errors, making accurate battery voltage and pack current measurements important for accurate state-of-charge estimations. Accurate state-of-charge information is the key to avoiding cell balance by mistake, in which overcharge and overdischarge can ruin the maximum usable battery energy.

Another important measurement is temperature. Most battery fire and explosion accidents are caused by battery thermal runaway.

Figure 2 shows TI's stackable battery management unit reference design, which achieves ±3-mV cell voltage error from -20°C to 65°C using the BQ79616 battery monitor. For residential systems, another alternative is the BQ76972 battery monitor, which can achieve a ±5-mV cell voltage error from -40°C to 85°C. Multiplexer switches expand the temperature measurement channels to ensure the monitoring of each battery cell and power bus connector temperature. The stackable battery reference design reserves extra temperature channels for a diagnostic check of multiplexer switches.

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_005.png)

[www.ti.com](https://www.ti.com/)

Figure 2. Stackable battery management unit reference design

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_006.png)

An accurate and reliable current measurement solution is also necessary for ESS state-of-charge monitoring. The BQ79731-Q1 voltage and current sensor integrates dual 24-bit current-sense analog-to-digital converters, with redundant channels that help ensure system safety and accuracy of current data.

## Challenge No. 3: Balance capability of cells and packs

Battery packs might consume current at different rates because of load variations. These variations cause an imbalance between the packs' remaining energy and lower the maximum useable energy of the whole ESS. The inconsistency between new battery cells and different thermal cooling conditions can also cause an imbalance between different cells, even inside one pack. Passive cell balancing consumes battery energy on resisters and is not suggested for pack-level balancing, since it generates too much power consumption and heats the packs.

Battery pack imbalances worsen over a product's life span, and recall that an ESS can last longer than 10 years. Some packs might age faster than others over 10 years, forcing users to replace the aging packs. Without strong pack level balancing circuits, a worker must charge or discharge the new pack to almost equal the energy to remaining packs in the ESS has. But even that is risky, as it is difficult, expensive and labor consuming.

Battery cell imbalances are also affected by cell capacity. Battery manufacturers are developing larger-capacity battery cells - from 280 Ah to 314 Ah and even 560 Ah - to optimize the dollar-per-kilowatt-hour energy costs of the whole ESS. Packs with larger capacity cells require a larger effective balancing current to make all cells inside the pack provide the same energy continually.

There are several ways to balance the packs. Figure 3 shows one way to charge and discharge packs from a high-voltage bus through the Bidirectional CLLLC Resonant Converter Reference Design for Energy Storage System. By controlling the charge and discharge current, the isolated DC/DC converter can balance the packs to match the remaining capacity or pack voltage. Since both charge and discharge current flow through the bidirectional DC/DC converter, the overall efficiency is low and the power rating of the bidirectional DC/DC converter is large.

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_007.png)

Figure 3. Bidirectional isolated DC/DC converter from the battery pack to the high-voltage bus

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_008.png)

Figure 4. Bidirectional isolated DC/DC converter from the pack to the low-voltage bus

![Image](Battery%20Energy%20Storage%20-%20Design%20Challenges%20%28ssztd22%29_files/img_009.png)

## Conclusion

Safe and reliable battery management systems eliminate the concerns of Li-ion and LiFePO4 battery safety and help extend ESS lifespans with well-designed protections, even under a single device fault situation. Accurate data sensing and pack- and cell-level balancing enable charging and discharging with equal capacity and maximize energy utilization of solar and other renewable energy sources, eventually enabling end users to get safe, stable and low-cost renewable energy.

## Additional resources

- [Read the application brief, "Scaling accurate battery management designs across energy storage systems."](https://www.ti.com/lit/pdf/slvafq7)
- [View the video, "Designing a highly accurate battery energy storage system."](https://www.ti.com/video/6322624020112)
- Explore products and reference designs for battery energy storage systems.

## IMPORTANT NOTICE AND DISCLAIMER

TI PROVIDES TECHNICAL AND RELIABILITY DATA (INCLUDING DATA SHEETS), DESIGN RESOURCES (INCLUDING REFERENCE DESIGNS), APPLICATION OR OTHER DESIGN ADVICE, WEB TOOLS, SAFETY INFORMATION, AND OTHER RESOURCES "AS IS" AND WITH ALL FAULTS, AND DISCLAIMS ALL WARRANTIES, EXPRESS AND IMPLIED, INCLUDING WITHOUT LIMITATION ANY IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE OR NON-INFRINGEMENT OF THIRD PARTY INTELLECTUAL PROPERTY RIGHTS.

These resources are intended for skilled developers designing with TI products. You are solely responsible for (1) selecting the appropriate TI products for your application, (2) designing, validating and testing your application, and (3) ensuring your application meets applicable standards, and any other safety, security, regulatory or other requirements.

These resources are subject to change without notice. TI grants you permission to use these resources only for development of an application that uses the TI products described in the resource. Other reproduction and display of these resources is prohibited. No license is granted to any other TI intellectual property right or to any third party intellectual property right. TI disclaims responsibility for, and you will fully indemnify TI and its representatives against, any claims, damages, costs, losses, and liabilities arising out of your use of these resources.

TI's products are provided subject to TI's Terms of Sale or other applicable terms available either on ti.com or provided in conjunction with such TI products. TI's provision of these resources does not expand or otherwise alter TI's applicable warranties or warranty disclaimers for TI products.

TI objects to and rejects any additional or different terms you may have proposed. IMPORTANT NOTICE

Mailing Address: Texas Instruments, Post Office Box 655303, Dallas, Texas 75265 Copyright © 2024, Texas Instruments Incorporated
# Research Links

Background reading and reference material gathered while researching BMS designs
(other FSAE/Formula Student teams, academic work, and commercial/open-source
master-slave BMS boards) and the STM32 master-board MCU question.

## Academic papers and theses

- [Electronic System Design of a Formula Student Electric Car](https://www.scribd.com/document/988693196/Electronic-System-Design-of-a-Formula-Student-Electric-Car) —
  Scribd copy of the PCCOE Pune conference paper (same one saved locally in
  `Academic Theses and Reports/`).
- [University of Canterbury thesis repository entry](https://ir.canterbury.ac.nz/bitstreams/b6ad9ba0-59d8-4b30-ba9e-07c1dcd51b9f/download) —
  source download link for Ben Robertson's Master's thesis, "Design and
  Development of a Battery Management System for a Formula-SAE Electric
  Racecar" (saved locally in `Academic Theses and Reports/`).
- [Battery Management System Hardware Design for a Student Electric Racing Car (ResearchGate)](https://www.researchgate.net/publication/338614673_Battery_Management_System_Hardware_Design_for_a_Student_Electric_Racing_Car) —
  a different paper describing a control PCB built on an STM32 MCU paired with
  the TI BQ76PL455A-Q1 AFE. Not saved locally — worth reading for a second
  STM32+TI-AFE design example besides our own BQ79616 pairing.

## MCU / host-controller research

- [Google search: "in the BMS master board what is the MCU that they use?"](https://www.google.com/search?q=in+the+BMS+master+board+what+is+the+MCU+that+they+use%3F...) —
  leftover search query from researching what MCU other teams/designs use on
  the master board. Safe to ignore/delete — kept only as a breadcrumb of what
  was being investigated.
- [MaxKgo STM32 MCU-based 30V-150V Smart VESC Master BMS + Slave BMS Kit](https://maxkgo.com/products/maxkgo-stm32mcu-30v-150v-smart-vesc-master-bms-slave-bmskit) —
  commercial master/slave BMS kit, explicitly STM32-based. Product page, not a
  datasheet — doesn't name the exact STM32 part.
- [MaxKgo HV Master Board BMS announcement blog post](https://maxkgo.com/blogs/news/maxkgo-hv-master-board-bms-is-coming) —
  announcement post for MaxKgo's high-voltage master board; same product line
  as above.
- [Google search: "MaxKgo high-voltage BMS, what STM chip used"](https://www.google.com/search?client=firefox-b-d&q=MaxKgo+high-voltage+BMS%2C+what+the+SM+chip+used+here+) —
  follow-up search trying to pin down MaxKgo's exact STM32 part number. Didn't
  resolve to a confirmed part — treat as an open question, not an answer.
- [r4hulrr/stm-32-bms (GitHub)](https://github.com/r4hulrr/stm-32-bms#hardware-design) —
  personal/hobby BMS project using an **STM32F446RET6**, with overcharge/overheat
  protection and cell balancing. Hardware design section is the relevant part.
- [embeddedprojects101: Design a Battery-Powered STM32 Board with USB](https://embeddedprojects101.com/design-a-battery-powered-stm32-board-with-usb/) —
  general STM32 hardware design tutorial (power + USB), not BMS-specific, but
  useful as a basic STM32 board-design reference.
- [JacobParent7/FSAE_LSU_BMS (GitHub)](https://github.com/JacobParent7/FSAE_LSU_BMS) —
  **real FSAE team** (LSU) distributed BMS built around an STM32 MCU paired with
  the **BQ79616/BQ79614/BQ79612** family — the same TI AFE chip family we're
  using. Directly comparable project; worth reading their firmware/schematics.
- [ManchesterStingerMotorsports/g474-bms (GitHub)](https://github.com/ManchesterStingerMotorsports/g474-bms) —
  **real FSAE team** (University of Manchester). Confirms a Formula Student team
  using the **STM32G474RET6** specifically, paired with an ADBMS6822 AFE
  (different AFE than ours, but same MCU family/tier we're considering).

## Commercial off-the-shelf master/slave BMS units (for comparison, not for use)

- [HNGCE 96S HV Master/Slave BMS (LiFePO4, 307.2V 50A)](https://www.hngce.com/sale-45179089-master-slave-bms-high-voltage-bms-hv-bms-96s307-2v-50a-lifepo4-bms-lithium-battery-storage-solution-.html) —
  commercial high-voltage master/slave BMS product listing, energy-storage
  focused (not automotive/motorsport), useful only as a reference for how
  commercial master/slave topologies are marketed.
- [Alibaba: ANT BMS Master/Slave 96S](https://www.alibaba.com/product-detail/ANT-BMS-Master-Slave-BMS-96S_1601548423797.html) —
  another commercial master/slave BMS listing, same category as above.
- [AliExpress BMS listing](https://www.aliexpress.com/item/1005011860097059.html) —
  another commercial BMS product listing (generic marketplace result).

## Open-source BMS projects

- [EnnoidMe/ENNOID-BMS — Datasheet.pdf (GitHub)](https://github.com/EnnoidMe/ENNOID-BMS/blob/master/Datasheet.pdf) —
  open-source modular BMS for up to 400V EV packs, built on LTC68XX AFE chips +
  STM32. Direct link to their datasheet PDF.
- [ennoid.me/bms/gen-1](https://www.ennoid.me/bms/gen-1) —
  project page for the same ENNOID-BMS, "Gen 1" hardware overview.
- [cadlab.io/project/1987/master/files](https://cadlab.io/project/1987/master/files) —
  **confirmed source** of the two Altium exports (schematic + PCB layout, by
  Jason Sylvestre) saved locally in `Community Board Examples/`.
- [imgur.com/a/YxB5EGO](https://imgur.com/a/YxB5EGO) —
  image album, likely the source of the two reference photos/renders saved
  locally in `Community Board Examples/` (a physical board photo and a 3D
  render).

## Note on the saved local files

A few PDFs/images were downloaded from some of the links above without
keeping track of exactly which link they came from (hence the random
filenames they originally had, e.g. `bsb_Y9IdNkuxfA.pdf`). They've been
renamed based on their embedded metadata and sorted into:

- `Academic Theses and Reports/` — full written theses/reports, safe to cite.
- `Community Board Examples/` — other people's schematic/PCB/photo exports,
  useful for design comparison, not vetted or ours. The two Altium exports are
  confirmed from the cadlab.io link above.

(A third file that turned out to be an unrelated, mislabeled arXiv math paper
has since been deleted.)

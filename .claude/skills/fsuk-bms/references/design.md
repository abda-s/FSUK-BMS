# BMS-Master design facts (details and sources: BMS-Master/README.md)

## Schematic structure
- Hierarchical: `Top.SchDoc` holds sheet symbols only. Sheets: MCU_STM32, Power, CAN (one file placed twice: CAN1, CAN2), Stack_Interface, Current_Sense, Connectors (all off-board connectors), Charger, AMS_SDC.
- Project options: net scope Hierarchical, Higher Level Names Take Priority, multichannel designators `$Component_$RoomName` (e.g. `U5_CAN1`).
- Harness only for grouped logic signals between two sheets: `CAN_MCU` (TXD, RXD), `BQ97600_SPI`, `ISENSE_ADC`, `SWD`. Pairs and single signals use ports. Power nets are global power ports (`+12V`, `+6V94`, `+5V`, `+3V3`, `GND`, `+5V_REGBUS`, `GND_REGBUS`).
- Differential pairs end `_P`/`_N` with directives: `CAN_P/N` (CAN sheet), `COMH_P/N`, `ISO_COMH_P/N` (Stack). Top net labels `CAN1_P/N`, `CAN2_P/N`. Compiled pairs: CAN1, CAN2, COMH, ISO_COMH.
- Style: dashed box per block, short title (FontID 5), short notes under it; inputs left, outputs/buses right; every used MCU pin has a stub + net label with the CubeMX name; unused pins no-ERC. 108 logical parts; every R/C has an LCSC code (42 Celestial passives re-imported as EasyEDA parts). Test points TP1-TP20 (Keystone 5015, C2906768): Power TP1-5 (+12V, +6V94, +5V, +3V3, GND), MCU TP6-15 (BQ SPI lines, NFAULT, SPI_RDY, MCU_NRST, BAL_EN_N, CHG_EN, GND), Current_Sense TP16-17 (ISENSE_HI/LO), AMS_SDC TP18 (AMS_OK), CAN TP19-20 (CAN_P/N). Not on crystal nets, TS side, Reg Bus or SWD.
- Compile: no errors; expected warnings = nets with multiple names (hierarchy) and no driving source on the crystal nets.

## Parts and decisions
- MCU STM32G474RET6 LQFP64, 170 MHz. Crystal X1 SCTF SX5A20.000F2010F30G (LCSC C5830635), 5032 SMD, 20 MHz, CL 10 pF, ESR 40 ohm; load caps 12 pF C0G CL05C120JB5NNNC (C26406). gmcrit 0.57 mA/V vs STM32G474 HSE Gm 1.5 mA/V (AN2867, DS12288 Table 41); old HC-49S failed gmcrit. NRST: 10k pull-up, 100 nF (DS12288 Fig. 27), reset button XKB TS-1187A-B-A-B (C318884, pins 1-2/3-4 joined). BOOT0 10k pull-down. Balancing enable switch SSSS811101 on BAL_EN_N (10k pull-up, 100 nF).
- Pins: PA12/PA11 CAN1 TX/RX, PB13/PB12 CAN2 TX/RX, PA13/PA14/PB3 SWD, PA4 BQ_nCS, PA5/6/7 SPI1, PB0 BQ_NFAULT (EXTI0), PB1 BQ_SPI_RDY, PC0/1/2 ISENSE HI/LO/SUPPLY (ADC1 IN6-8, 247.5 cycles), PC6 CHG_EN, PC7 AMS_OK_MCU, PC8 BAL_EN_N. FDCAN 500 kbit/s, SPI1 mode 0 5.3 MHz.
- Power: LV_IN 11-16 V -> 1 A slow fuse 0452001.MRL -> SS34 reverse diode -> SMBJ16A TVS (after the diode) -> buck TPS62933F 6.94 V (R_FBT 76.8k, worst case 6.69-7.21 V, 2x 47 uF; one cap oscillated at 9 V in sim) -> LDOs TLV76150 (+5V, 175 mA) and TLV76133 (+3V3, 58 mA), 2.2 uF in/out (TLV761: C_OUT 1-220 uF, C_IN >= 0.47 uF eff., no max). Power LEDs: red KT-0603R (C2286) on each rail via R39 10k/R40 4.7k/R41 3.3k/R42 1.5k, ~1 mA each (LED1-4).
- CAN: TCAN1042V-Q1 (SOIC-8; v2 TCAN1462V-Q1 if stock), VCC +5V 4.7 uF+100 nF, VIO +3V3 100 nF, STB 0R to GND. Split termination 2x 60.4R 1206 (C57572) + 4.7 nF (C84705), fit only at a bus end; 20 pF bus caps kept equal; TVS PESD2CAN24T-QR (C28933048) at J1.
- Current sensor LEM DHAB S/124 (ch1 +-75 A, ch2 +-500 A, ratiometric 5 V). 12k/18k dividers (x0.6), 22 nF at input, 100 nF at ADC pin, supply monitored on a third channel. ESD PESD5V0L2BT (C46956345) at the input. Firmware fault checks in README (T 11.9, EV 5.8.x).
- Stack: BQ79600-Q1 bridge over SPI, COMH filter + ESD, SM91502ALE transformer (same part as on BMS-Module). COMLP/COMLN unconnected (R29 removed, TI SLUAA16A 1.5). T1 pin 5 (secondary centre-tap) intentionally floating (tying it to LV GND would bridge the TS/LV barrier, EV 1.2.1 / 4.3.1). Isolation acceptance still to ask the ESA.
- Charger: CHG_EN -> 330R -> PC817 pulls REGBUS_STOP (fail-safe: low = charger stops). AMS_SDC: AMS_OK_MCU drives a 12 V AMS_OK output (Q1 level shift, AO3401A Q2, 2K2 out); low opens the SDC.
- Connectors: J1 Micro-Fit 3.0 2x8 RA (LV: power, CAN1, CAN2, AMS_OK, current sensor; pins 15-16 spare), J2 Micro-Fit 2-pin (daisy chain, TS side), J3 RJ12 DS1133-S60BPX (charger Reg Bus, TS side, pins 3/5/6 unused), J4 2x5 1.27 mm SWD. TS/LV segregation per EV 4.3.5, Table 5 spacing.

## Open items (README Progress has the live list)
- TCAN1042VDQ1 (C1544495) stock low (26).
- Confirm Keystone 5015 land pattern.
- Order J3 RJ12 (C77859); v2: COML ring connector, external watchdog TPS3431, SDC readback, heartbeat AMS_OK.
- Bench tests (ripple < 0.4 mV, buck at 9 V, hot-plug), PCB layout, SDC-team and ESA questions, firmware (BQ79600 driver, fault latch, IWDG, ISENSE checks, SoC, balancing, CAN messages).
- Notes on Stack_Interface are the user's reminders, not tasks.

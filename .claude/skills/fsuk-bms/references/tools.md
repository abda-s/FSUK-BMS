# Tools

## LTspice (buck sims, BMS-Master/sim/buck)
- `C:\Users\3adas\AppData\Local\Programs\ADI\LTspice\LTspice.exe -b file.cir` -> `.log` with `.meas`. Always use a timeout; `.save` only needed nodes. TI TPS62933F model is patched (`TPS62933F_LTspice.lib`); it needs a rising VIN ramp. Charts: `sim/buck/charts/make_charts.py`; schematic SVG: `sim/buck/asc2svg.py`. A long run stalled once because the PC slept.

## STM32 (Firmware/BMS-Master)
- CubeMX 6.18.1 `C:\Program Files\STMicroelectronics\STM32Cube\STM32CubeMX`; reference skill `stm32cubemx`. The CLI can't set pins: edit the `.ioc`, check with `config load` + `config saveas`, then `project generate`. Only `USER CODE` blocks survive regeneration.
- CubeIDE headless build: `stm32cubeidec.exe --launcher.suppressErrors -nosplash -application org.eclipse.cdt.managedbuilder.core.headlessbuild -data <ws> -import <proj> -build BMS-Master/Debug`. `Debug/` is git-ignored. Pinout image: `Firmware/docs/make_pinout.py` -> `pinout.svg`. CubeMX login is the user's.

## PDF -> Markdown (tools/pdf2md.py)
- `python tools/pdf2md.py [file|folder] [--force] [--dry-run] [--cpu] [--no-ocr] [--max-mb N] [--postprocess]`. Docling, GPU (CUDA), OCR on (RapidOCR torch backend), output to `Reference Docs/MD Conversions/`, duplicate images removed, short image names, image-only PDFs rendered as pages, keeps Windows awake. Full run of 122 PDFs ~72 min.
- GPU needs `torch 2.14.1+cu126` + `torchvision 0.29.1+cu126` (GTX 1650 4 GB, driver 621); `pip install -U docling` may reinstall CPU torch: check `torch.cuda.is_available()`.
- Docling limits: merged cells spill into the next row, superscripts in cells read as text. Paths can exceed 260 chars: use the `\\?\` prefix (and `\` separators) in helpers.

## OCR book project (E:\Documents\Books\the ocr shit)
- Scanned Erickson & Maksimovic textbook -> searchable PDF. `tools/pipeline.py`: MinerU (GPU) parse, extract 1852 equations, render/score, mathcheck, optional voters (PP-FormulaNet, UniMERNet, LaTeX-OCR in `.venv-voters` torch cu118; GLM-OCR via llama.cpp Vulkan), Gemini tiebreak, review sheets, FINAL.pdf. Result: 1690 accepted, 117 review, 13 kept as scan. Report: `reports/Scanned equation OCR accuracy.md` (voting + 2x bicubic crops; GTX 1650 has no bf16).

## Git and docs
- Line-ending warnings (LF->CRLF) are harmless. Check `git status` and untracked files before committing; build output and run logs (`tools/pdf2md*.log/out`) are ignored.
- Root README explains the project; BMS-Master README sections each end with Sources. Block diagrams are SVG (from Excalidraw, no .excalidraw file). Schematic PDF is exported by the user.

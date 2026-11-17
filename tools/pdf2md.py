"""Convert PDFs to Markdown with Docling, keeping tables and figures.

Output goes to "Reference Docs/MD Conversions/", mirroring the folder layout
of "Reference Docs":
    MD Conversions/<same path>/<name>.md       text and tables (Markdown tables)
    MD Conversions/<same path>/<name>_files/   figures as PNG, linked from the .md

After each conversion:
  - identical images inside one PDF (logos, header bars repeated on every page)
    are kept once and every link points to that one file;
  - if the result has almost no text (scans, vector schematics), every page is
    rendered as a full-page PNG instead, so the .md still shows the content.

Usage (from the repo root):
    python tools/pdf2md.py                       # everything under "Reference Docs"
    python tools/pdf2md.py "Reference Docs/Master/LDO"   # one folder
    python tools/pdf2md.py some/file.pdf         # one file
    python tools/pdf2md.py --dry-run             # list what would be converted
    python tools/pdf2md.py --force               # redo files that already have an up-to-date .md
    python tools/pdf2md.py --no-ocr              # skip OCR (faster; scanned/image pages come out empty)
    python tools/pdf2md.py --max-mb 30           # skip PDFs larger than 30 MB
    python tools/pdf2md.py --cpu                 # run on the CPU (default is the NVIDIA GPU)
    python tools/pdf2md.py --postprocess         # only re-run dedupe + page rendering on existing output

GPU: layout, table and OCR models run on CUDA (OCR through RapidOCR's torch
backend). Needs a CUDA build of PyTorch (torch.cuda.is_available() == True);
on this PC that is torch 2.14.1+cu126 on the GTX 1650 (4 GB).

A PDF is skipped when its .md exists and is newer than the PDF. Failures are
logged and the run continues; a summary is printed at the end and written to
tools/pdf2md.log.

Check important numbers against the PDF: Docling can scramble tables with
merged cells and reads superscripts in cells as normal text.
"""
import argparse
import hashlib
import os
import re
import shutil
import sys
import tempfile
import time
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
REF = ROOT / "Reference Docs"
OUT = REF / "MD Conversions"
LOG = ROOT / "tools" / "pdf2md.log"
HEADER = "<!-- Converted from {name} with Docling (tools/pdf2md.py). Check key numbers against the PDF. -->\n\n"
MIN_TEXT_CHARS = 80   # fewer letters/digits than this (outside image links) = treat as image-only
PAGE_DPI = 150        # page renders for image-only PDFs


def rel(p: Path):
    return p.relative_to(ROOT) if p.is_relative_to(ROOT) else p


def out_paths(pdf: Path):
    """Where the .md and its image folder go for this PDF."""
    if pdf.is_relative_to(REF):
        base = OUT / pdf.relative_to(REF)
    elif pdf.is_relative_to(ROOT):
        base = OUT / "_other" / pdf.relative_to(ROOT)
    else:
        base = OUT / "_other" / pdf.name
    return base.with_suffix(".md"), base.with_name(base.stem + "_files")


def find_pdfs(targets):
    pdfs = []
    for t in targets:
        p = Path(t)
        if not p.is_absolute():
            p = (Path.cwd() / p).resolve()
        if p.is_file() and p.suffix.lower() == ".pdf":
            pdfs.append(p)
        elif p.is_dir():
            pdfs.extend(sorted(q for q in p.rglob("*") if q.suffix.lower() == ".pdf"))
        else:
            print(f"not found: {t}", file=sys.stderr)
    return [p for p in pdfs if not p.is_relative_to(OUT)]


def up_to_date(pdf: Path) -> bool:
    md, _ = out_paths(pdf)
    m = lp(md)
    return m.exists() and m.stat().st_mtime >= pdf.stat().st_mtime


def make_converter(ocr: bool, gpu: bool):
    from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
    from docling.datamodel.base_models import InputFormat
    from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions
    from docling.document_converter import DocumentConverter, PdfFormatOption

    opts = PdfPipelineOptions()
    opts.accelerator_options = AcceleratorOptions(device=AcceleratorDevice.CUDA if gpu else AcceleratorDevice.CPU)
    opts.do_ocr = ocr
    if ocr:
        # torch backend so OCR also runs on the GPU (the onnxruntime build here is CPU-only)
        opts.ocr_options = RapidOcrOptions(backend="torch" if gpu else "onnxruntime")
    opts.do_table_structure = True
    opts.generate_picture_images = True
    opts.images_scale = 2.0  # figures at 144 dpi, readable in the .md
    return DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})


def fix_links(text: str, files_dir: Path) -> str:
    """Docling writes absolute file:/// links; make them relative to the .md."""
    rel_prefix = quote(files_dir.name) + "/"
    for absolute in (files_dir.as_uri() + "/", files_dir.as_posix() + "/", str(files_dir) + "\\"):
        text = text.replace(absolute, rel_prefix)
    # Docling's own URL encoding can differ (e.g. it leaves commas as-is)
    return re.sub(r"file:///[^)\s]*?([^/)\s]+_files/)", r"\1", text)


def lp(p: Path) -> Path:
    """Windows long-path form (\\\\?\\C:\\...), so paths over 260 characters still work."""
    s = str(Path(p).resolve()) if not str(p).startswith("\\\\?\\") else str(p)
    if sys.platform == "win32" and not s.startswith("\\\\?\\"):
        s = "\\\\?\\" + s
    return Path(s)


def dedupe_images(text: str, files_dir: Path):
    """Keep one copy of identical images and give images short names (img_001.png ...).

    Docling names images image_000000_<64-char hash>.png, which pushes deep paths past
    Windows' 260-character limit. Returns (text, duplicates removed)."""
    d = lp(files_dir)
    if not d.exists():
        return text, 0
    seen, removed, k = {}, 0, 0
    for name in sorted(n for n in os.listdir(d) if n.lower().endswith(".png")):
        h = hashlib.sha1((d / name).read_bytes()).hexdigest()
        if h in seen:
            text = text.replace(name, seen[h])
            os.remove(d / name)
            removed += 1
            continue
        k += 1
        new = name if name.startswith(("page_", "img_")) else f"img_{k:03d}.png"
        if new != name:
            os.rename(d / name, d / new)
            text = text.replace(name, new)
        seen[h] = new
    return text, removed


def text_chars(text: str) -> int:
    body = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    body = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", body)
    return len(re.findall(r"[A-Za-z0-9]", body))


def render_pages(pdf: Path, md: Path, files_dir: Path) -> int:
    """Image-only PDF: replace the .md with one full-page PNG per page."""
    import pymupdf

    d = lp(files_dir)
    os.makedirs(d, exist_ok=True)
    for name in os.listdir(d):
        if name.lower().endswith(".png"):
            os.remove(d / name)
    doc = pymupdf.open(pdf)
    parts = [HEADER.format(name=pdf.name),
             "No extractable text in this PDF (scan or vector drawing), so each page is shown as an image.\n\n"]
    for i, page in enumerate(doc, 1):
        name = f"page_{i:03d}.png"
        (d / name).write_bytes(page.get_pixmap(dpi=PAGE_DPI).tobytes("png"))
        parts.append(f"## Page {i}\n\n![Page {i}]({quote(files_dir.name)}/{name})\n\n")
    lp(md).write_text("".join(parts), encoding="utf-8", newline="\n")
    return doc.page_count


def postprocess(pdf: Path, md: Path, files_dir: Path) -> str:
    """Dedupe images, or render pages if the conversion has no real text. Returns a short note."""
    text = lp(md).read_text(encoding="utf-8")
    if text_chars(text) < MIN_TEXT_CHARS:
        n = render_pages(pdf, md, files_dir)
        return f"image-only, {n} pages rendered"
    text, removed = dedupe_images(text, files_dir)
    lp(md).write_text(text, encoding="utf-8", newline="\n")
    return f"{removed} duplicate images removed" if removed else "no duplicates"


def convert(converter, pdf: Path):
    from docling_core.types.doc import ImageRefMode

    result = converter.convert(str(pdf))
    md, files_dir = out_paths(pdf)
    # Docling writes into a short temp folder (its long image names can exceed 260 characters
    # in the real folder); images get short names there, then everything moves into place.
    tmp = Path(tempfile.mkdtemp(prefix="pdf2md_"))
    try:
        tmp_md, tmp_files = tmp / "doc.md", tmp / files_dir.name
        result.document.save_as_markdown(
            tmp_md,
            artifacts_dir=tmp_files,
            image_mode=ImageRefMode.REFERENCED,
            compact_tables=True,
        )
        text = fix_links(tmp_md.read_text(encoding="utf-8"), tmp_files)
        text, _ = dedupe_images(text, tmp_files)
        tmp_md.write_text(HEADER.format(name=pdf.name) + text, encoding="utf-8", newline="\n")
        os.makedirs(lp(md.parent), exist_ok=True)
        if lp(files_dir).exists():
            shutil.rmtree(lp(files_dir))
        if tmp_files.exists():
            shutil.move(str(tmp_files), str(lp(files_dir)))
        shutil.move(str(tmp_md), str(lp(md)))
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    note = postprocess(pdf, md, files_dir)
    d = lp(files_dir)
    n_img = len([n for n in os.listdir(d) if n.lower().endswith(".png")]) if d.exists() else 0
    return md, n_img, note


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("targets", nargs="*", help="PDF files or folders (default: Reference Docs)")
    ap.add_argument("--force", action="store_true", help="convert even if the .md is up to date")
    ap.add_argument("--dry-run", action="store_true", help="only list what would be converted")
    ap.add_argument("--no-ocr", action="store_true", help="skip OCR (faster; image-only pages come out empty)")
    ap.add_argument("--cpu", action="store_true", help="run on the CPU instead of the GPU")
    ap.add_argument("--max-mb", type=float, default=0, help="skip PDFs larger than this (0 = no limit)")
    ap.add_argument("--postprocess", action="store_true", help="only dedupe / render pages on existing output")
    args = ap.parse_args()

    pdfs = find_pdfs(args.targets or [REF])

    if args.postprocess:
        for pdf in pdfs:
            md, files_dir = out_paths(pdf)
            if lp(md).exists():
                print(f"{rel(md)}: {postprocess(pdf, md, files_dir)}")
        return

    todo, skipped = [], []
    for pdf in pdfs:
        size_mb = pdf.stat().st_size / 1e6
        if args.max_mb and size_mb > args.max_mb:
            skipped.append((pdf, f"larger than {args.max_mb} MB ({size_mb:.0f} MB)"))
        elif not args.force and up_to_date(pdf):
            skipped.append((pdf, "up to date"))
        else:
            todo.append(pdf)

    print(f"{len(pdfs)} PDFs found, {len(todo)} to convert, {len(skipped)} skipped")
    if args.dry_run:
        for pdf in todo:
            print("  convert:", rel(pdf))
        for pdf, why in skipped:
            print("  skip   :", rel(pdf), f"({why})")
        return
    if not todo:
        return

    gpu = not args.cpu
    if gpu:
        import torch
        if not torch.cuda.is_available():
            sys.exit(f"CUDA not available (torch {torch.__version__}). Install a CUDA build of PyTorch, or run with --cpu.")
        print(f"GPU: {torch.cuda.get_device_name(0)}, torch {torch.__version__}")
    if sys.platform == "win32":
        # Keep Windows from idle-sleeping during the run (released when the process exits).
        import ctypes
        ctypes.windll.kernel32.SetThreadExecutionState(0x80000000 | 0x00000001)  # ES_CONTINUOUS | ES_SYSTEM_REQUIRED
    converter = make_converter(not args.no_ocr, gpu)

    done, failed = [], []
    t_all = time.time()
    for i, pdf in enumerate(todo, 1):
        t0 = time.time()
        print(f"[{i}/{len(todo)}] {rel(pdf)} ...", flush=True)
        try:
            md, n_img, note = convert(converter, pdf)
            dt = time.time() - t0
            done.append((rel(pdf), dt, n_img, note))
            print(f"    ok, {dt:.0f} s, {n_img} images ({note}) -> {rel(md)}", flush=True)
        except Exception as e:  # keep going on bad PDFs
            failed.append((rel(pdf), repr(e)))
            print(f"    FAILED: {e}", flush=True)

    lines = [f"pdf2md run {time.strftime('%Y-%m-%d %H:%M')}, {time.time() - t_all:.0f} s total",
             f"converted {len(done)}, failed {len(failed)}, skipped {len(skipped)}"]
    lines += [f"ok     {r}  ({dt:.0f} s, {n} images, {note})" for r, dt, n, note in done]
    lines += [f"FAILED {r}  {err}" for r, err in failed]
    LOG.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines[:2]))
    if failed:
        print("failures listed in", rel(LOG))


if __name__ == "__main__":
    main()

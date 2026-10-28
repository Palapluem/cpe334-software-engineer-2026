#!/usr/bin/env python3
"""Build the single bilingual question PDF without leaving LaTeX debris."""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


def main() -> None:
    source = Path(__file__).resolve().parent
    repo = source.parents[2]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, default=source / "output/pdf")
    args = parser.parse_args()
    destination = args.output_dir.resolve()
    if shutil.which("xelatex") is None:
        parser.error("XeLaTeX is required. No fonts or packages are downloaded.")
    scratch = repo / "tmp/pdfs"
    scratch.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="cpe334-mock-", dir=scratch) as work:
        command = [
            "xelatex", "-interaction=nonstopmode", "-halt-on-error",
            "-jobname=CPE334_Midterm_Mock_TH_EN", f"-output-directory={work}", "main.tex",
        ]
        for _ in range(2):
            result = subprocess.run(
                command, cwd=source, text=True,
                stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            if result.returncode:
                raise SystemExit(result.stdout)
        log = (Path(work) / "CPE334_Midterm_Mock_TH_EN.log").read_text(errors="replace")
        bad = re.findall(
            r"^.*(?:Overfull \\[hv]box|Missing character|undefined references).*$",
            log, flags=re.MULTILINE,
        )
        if bad:
            raise SystemExit("\n".join(bad))
        destination.mkdir(parents=True, exist_ok=True)
        output = destination / "CPE334_Midterm_Mock_TH_EN.pdf"
        shutil.copyfile(Path(work) / output.name, output)
    print(output)


if __name__ == "__main__":
    main()

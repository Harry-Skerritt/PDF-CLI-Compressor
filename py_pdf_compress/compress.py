import os
import subprocess
import argparse
import shutil


def getCurrentDir():
    return os.getcwd()


def getPDFsInDir(path):
    return [f for f in os.listdir(path) if f.lower().endswith(".pdf")]


def createOutDir(path):
    out_dir = os.path.join(path, "out")
    os.makedirs(out_dir, exist_ok=True)
    return out_dir


def clearOutDir(out_dir):
    if os.path.exists(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)


def getQuality(in_quality):
    match in_quality:
        case 1:
            return "/screen"
        case 2:
            return "/ebook"
        case 3:
            return "/printer"
        case 4:
            return "/prepress"
        case _:
            raise ValueError("Invalid quality level")


def compress_pdfs(arg_in_qual):
    working_dir = getCurrentDir()
    out_dir = createOutDir(working_dir)
    clearOutDir(out_dir)

    pdf_names = getPDFsInDir(working_dir)
    quality = getQuality(arg_in_qual)

    for pdf in pdf_names:
        in_path = os.path.join(working_dir, pdf)

        if not os.path.isfile(in_path):
            continue

        out_path = os.path.join(out_dir, pdf)

        subprocess.run(
            [
                "gs",
                "-sDEVICE=pdfwrite",
                f"-dPDFSETTINGS={quality}",
                "-dNOPAUSE",
                "-dBATCH",
                f"-sOutputFile={out_path}",
                in_path,
            ],
            check=True,
        )
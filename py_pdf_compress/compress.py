import os
import subprocess
import argparse
import shutil
import sys


def getCurrentDir():
       cwd = os.path.abspath(os.getcwd())
   
       if os.name == "nt":  # Windows
           if cwd.rstrip("\\") in ["C:", "D:", "E:"]:
               sys.exit("Error: Cannot run py-pdf-compress in the root directory of a drive.")
       else:  # macOS / Linux
           if cwd == "/":
               sys.exit("Error: Cannot run py-pdf-compress in the root directory (/).")
   
       return cwd
           
        
def getGhostscriptCmd():
    gs_cmd = shutil.which("gs") or shutil.which("gswin64c")
    if not gs_cmd:
        sys.exit(
            "Error: Ghostscript not found.\n"
            "Install it:\n"
            "  macOS:   brew install ghostscript\n"
            "  Linux:   sudo apt install ghostscript\n"
            "  Windows: choco install ghostscript"
        )
    return gs_cmd

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
    gs_cmd = getGhostscriptCmd()
    
    out_dir = createOutDir(working_dir)
    clearOutDir(out_dir)

    pdf_names = getPDFsInDir(working_dir)
    
    if not pdf_names:
        sys.exit(f"Error: No PDF files found in {working_dir}")
    
    quality = getQuality(arg_in_qual)

    for pdf in pdf_names:
        in_path = os.path.join(working_dir, pdf)

        if not os.path.isfile(in_path):
            continue

        out_path = os.path.join(out_dir, pdf)

        subprocess.run(
            [
                gs_cmd,
                "-sDEVICE=pdfwrite",
                f"-dPDFSETTINGS={quality}",
                "-dNOPAUSE",
                "-dBATCH",
                f"-sOutputFile={out_path}",
                in_path,
            ],
            check=True,
        )
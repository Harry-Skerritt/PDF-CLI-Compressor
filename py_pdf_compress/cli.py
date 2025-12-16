import argparse
from .compress import compress_pdfs

def main():
    parser = argparse.ArgumentParser(
        description="Compress PDFs in current directory"
    )
    parser.add_argument(
        "--quality",
        type=int,
        choices=[1, 2, 3, 4],
        default=2,
        help="Compression quality: 1=screen, 2=ebook (default), 3=printer, 4=prepress",
    )
    
    args = parser.parse_args()
    compress_pdfs(args.quality)

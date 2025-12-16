# PDF-CLI-Compressor
![GitHub License](https://img.shields.io/github/license/Harry-Skerritt/PDF-CLI-Compressor)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Harry-Skerritt/PDF-CLI-Compressor)
![Runs on Mac](https://img.shields.io/badge/Mac-OS?logo=apple&color=%23555555)

---

* This is a quick and dirty CLI PDF compressor written in python.

* Not the neatest or most efficient code, but was written in 30 minutes as I needed to compress some PDFs without uploading them to the internet.

* Uses Ghostscript to operate

## How to Install
**Requires Python3 being installed**

* On MacOS run `brew install ghostscript` to install the ghostscript dependency

* Then put the compress.py file into the directory of pdfs and run `python3 compress.py` (This will run at default compression level of 2)


## Quality Flag
You can use the `--quality` flag to specify the quality of your compressed PDF.
> Example Useage `python3 compress.py --quality 2`

| Quality Tag    | Quality / Size | GhostScript Preset |
| -------------- | ----------------- | --------------- |
| `--quality 1`  | lowest / smallest | /screen         |
| `--quality 2`  | good / small      | /ebook          |
| `--quality 3`  | high / big        | /printer        |
| `--quality 4`  | best / largest    | /prepress       |



## Possible Additions
* Neaten up of the code
* More efficient code
* Make it easier to use

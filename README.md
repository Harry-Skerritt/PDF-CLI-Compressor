# py-pdf-compress
![Made with Python](https://img.shields.io/badge/Python-a?logo=python&label=Made%20With&color=blue&style=for-the-badge)
![PyPi Version](https://img.shields.io/pypi/v/py-pdf-compress?style=for-the-badge)
![PyPI - Downloads](https://img.shields.io/pypi/dm/py-pdf-compress?style=for-the-badge)
![GitHub License](https://img.shields.io/github/license/Harry-Skerritt/PDF-CLI-Compressor?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/Harry-Skerritt/PDF-CLI-Compressor?style=for-the-badge)
<br>
![Runs on Mac](https://img.shields.io/badge/Mac-OS?logo=apple&color=%23555555&style=for-the-badge)
![Runs on Linux](https://img.shields.io/badge/Linux-OS?logo=linux&color=orange&style=for-the-badge)
![Runs on Windows](https://img.shields.io/badge/Windows-OS?logo=windows&color=blue&style=for-the-badge)

---
**Find on [PyPi](https://pypi.org/project/py-pdf-compress/)**

Uses Ghostscript to compress all PDFs within a directory!

*Originally written as a quick tool for personal use, but added to, for ease of use by others*

### Quick Links
* [Install](#Installing-the-Tool)
* [How To Use](#Using-the-tool)
* [Flags](#Flags)


# Installing the Tool
Below are instructions to install *py-pdf-compress* and its dependencies

## Requirements
* Python 3.10+
* Ghostscript


## Installing Ghostscript:
**MacOS**

```bash
brew install ghostscript
```

**Linux**

```bash
sudo apt install ghostscript
```

**Windows**

```bash
choco install ghostscript
```


## Installing py-pdf-compress

This tool can either be installed diretcly from [pypi](#Installing-using-pip) using *pip* or *pip3*, or it can be installed from [GitHub](#Installing-from-GitHub) using **pipx**

### Installing using pip *(recommended)*

To install using pip run the command

```bash
pip install py-pdf-compress
```

To install using pip3 run the command

```bash
pip3 install py-pdf-compress
```

### [How To Use The Tool](#Using-the-tool)

---

### Installing from GitHub *(requires pipx)*
---
#### Installing pipx

**MacOS / Linux**

```bash
brew install pipx
pipx ensurepath
```


**Windows**

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

---
#### Once **pipx** is installed, run:

```bash
pipx install git+https://github.com/Harry-Skerritt/py-pdf-compress.git
```

<br>

# Using the Tool

Once installed, the tool can be used as instructed below!

## Running the Script
Navigate to your directory containing the PDFs you wish to compress using the command line, and run

```bash
py-pdf-compress
```

This will run the script with the standard quality of 2!

### Output
All the compressed files will be located at:```{CURRENT_DIRECTORY}/out```

<br>

## Flags

### Quality Flag
You can use the `--quality` flag to specify the quality of your compressed PDF.

| Quality Tag    | Quality / Size | Ghostscript Preset |
| -------------- | ----------------- | --------------- |
| `--quality 1`  | lowest / smallest | /screen         |
| `--quality 2`  | good / small      | /ebook          |
| `--quality 3`  | high / big        | /printer        |
| `--quality 4`  | best / largest    | /prepress       |

#### Example Useage 

```bash
py-pdf-compress --quality 2
```

<br>

### Quiet Flag
You can use the `-q` or `--quiet` to only output the done message, and supress output

#### Example Useage

```bash
py-pdf-compress --quality 2 -q
```

<br>
<br>

## Possible Additions
* Recursive compression within directories
* Neaten up of the code
* More efficient code
* ~~Make it easier to use~~ **Done** through use of pipx and the command line tool

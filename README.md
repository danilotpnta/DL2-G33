# Improving SAM-Med2D
Official implementation of ['SAM-Med2D'](https://github.com/OpenGVLab/SAM-Med2D).


## Requirements

### Installation
Create a conda environment and install dependencies:

```bash
git clone https://github.com/danilotpnta/DL2-G33
cd DL2-G33

conda create -n dl2-g33 python=3.10
conda activate dl2-g33

pip install -r requirements.txt

```

### Dataset
Download the official [SA-Med2D-20M](https://huggingface.co/datasets/OpenGVLab/SA-Med2D-20M/tree/main) dataset and put the unzip folder under `data/`.
The directory structure should be:
```bash
│DL2-G33/
├──...
├──data/
│   ├──GMAI___SA-Med2D-20M/
├──...
```
### 

Alternatively you can run the following script to download the dataset

```bash
cd src/scripts
python download_data.py
```

To download the dataset from [HaN-Seg](https://zenodo.org/records/7442914#.ZBtfBHbMJaQ) use the following:

```bash
cd src/data
wget https://zenodo.org/records/7442914/files/HaN-Seg.zip
unzip HaN-Seg.zip
```

### Checkpoint
Download the official [sam-med2d_b.pth](https://drive.google.com/file/d/1ARiB5RkSsWmAB_8mqWnwDF8ZKTtFwsjl/view) checkpoint and put the unzip folder under `data/`.
The directory structure should be:
```bash
│DL2-G33/
├──...
├──data/
│   ├──checkpoints/
├──...
```
### 

Alternatively you can run the following script to download the dataset

```bash
cd src/scripts
python download_checkpoint.py
```

## Get Started

### Stuff here
### Stuff here


## Acknowlegment
This repo benefits from [CLIP](https://github.com/openai/CLIP), and the excellent database from [MICCAI2023](https://conferences.miccai.org/). Thanks for their wonderful works.

## Contact
If you have any question about this project, please feel free to contact us

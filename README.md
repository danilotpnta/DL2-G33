# Improving SegVol
Official implementation of ['SegVol'](https://github.com/BAAI-DCAI/SegVol).


## Requirements

### Installation
Create a conda environment and install dependencies:

```bash
git clone https://github.com/danilotpnta/DL2-G33
cd DL2-G33

conda create -n SegVol python=3.10
conda activate SegVol

pip install -r requirements.txt
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html
```

### Dataset
Download the official [M3D-Seg](https://huggingface.co/datasets/GoodBaiBai88/M3D-Seg) dataset and put the unzip folder under `data/`.
The directory structure should be:
```bash
│DL2-G33/
├──...
├──data/
│   ├──GM3D_Seg/
├──...
```

To download the demo-dataset from [Abdomenct-12organ](https://zenodo.org/records/7860267) use the following:
```bash
cd src/data
wget https://zenodo.org/records/7860267/files/FLARE22Train.zip
unzip FLARE22Train.zip
```

### Checkpoint
Download the official [SegVol_v1.pth](https://drive.google.com/drive/folders/1TEJtgctH534Ko5r4i79usJvqmXVuLf54?usp=drive_link) checkpoint and put the unzip folder under `data/`.
The directory structure should be:
```bash
│DL2-G33/
├──...
├──data/
│   ├──checkpoints/
├──...
```
### 


## Get Started

### Stuff here
### Stuff here


## Acknowlegment
This repo benefits from [CLIP](https://github.com/openai/CLIP), and the excellent database from [MICCAI2023](https://conferences.miccai.org/). Thanks for their wonderful works.

## Contact
If you have any question about this project, please feel free to contact us

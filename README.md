# Spectrometer Bead Malfunction Detection

This repo contains the supported code and configuration files to reproduce object detection results of the upcoming journal article "Autonomous Malfunction Detection on Spectrometers Using Deep Convolutional Models" supplied as draft to MDPI. It is based on [mmdetection](https://github.com/open-mmlab/mmdetection).

For the sibling link to the data augmentation repository also used for the data synthesis portion of this project, please refer to [coco-paste-augmentation](https://github.com/anley1/coco-paste-augmentation) which was made for this purpose.

# Video Presentation
<!-- [![Watch the video](youtube_thumbnail.png)](https://www.youtube.com/watch?v=bd3WmD_lNCU) -->
[<img src="youtube_thumbnail.png" width="100%" align="center">](https://youtu.be/bd3WmD_lNCU)


## Updates

***12/10/2021*** M3 repository to update training batch files.


## Results and Models
Available in results/ and slurm_scripts/

**Notes**: 

- **Pre-trained models can be downloaded from [Swin Transformer for ImageNet Classification](https://github.com/microsoft/Swin-Transformer)**.
- Access code for `baidu` is `swin`.

## Usage

### Installation

Please refer to [get_started.md](https://github.com/open-mmlab/mmdetection/blob/master/docs/get_started.md) for installation and dataset preparation.

### Inference
```
# single-gpu testing
python tools/test.py <CONFIG_FILE> <DET_CHECKPOINT_FILE> --eval bbox segm

# multi-gpu testing
tools/dist_test.sh <CONFIG_FILE> <DET_CHECKPOINT_FILE> <GPU_NUM> --eval bbox segm
```

### Training

To train a detector with pre-trained models, run:
```
# single-gpu training
python tools/train.py <CONFIG_FILE> --cfg-options model.pretrained=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments]

# multi-gpu training
tools/dist_train.sh <CONFIG_FILE> <GPU_NUM> --cfg-options model.pretrained=<PRETRAIN_MODEL> [model.backbone.use_checkpoint=True] [other optional arguments] 
```
For example, to train a Cascade Mask R-CNN model with a `Swin-T` backbone and 8 gpus, run:
```
tools/dist_train.sh configs/swin/cascade_mask_rcnn_swin_tiny_patch4_window7_mstrain_480-800_giou_4conv1f_adamw_3x_coco.py 8 --cfg-options model.pretrained=<PRETRAIN_MODEL> 
```

**Note:** `use_checkpoint` is used to save GPU memory. Please refer to [this page](https://pytorch.org/docs/stable/checkpoint.html) for more details.


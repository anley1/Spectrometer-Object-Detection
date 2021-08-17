_base_ = './htc_hrnetv2p_w40_20e_coco_08.py'
# learning policy
lr_config = dict(step=[24, 27])
runner = dict(type='EpochBasedRunner', max_epochs=28)

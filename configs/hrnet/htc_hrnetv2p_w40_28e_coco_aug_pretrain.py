_base_ = './htc_hrnetv2p_w40_20e_coco.py'
# learning policy
lr_config = dict(step=[24, 27])
runner = dict(type='EpochBasedRunner', max_epochs=28)
#load_from = 'freeze/type_3_hrnet_htc_aug_medium_gray/epoch_8.pth'
load_from = 'freeze/type_3_hrnet_pretrain_6hr_real/epoch_28.pth'

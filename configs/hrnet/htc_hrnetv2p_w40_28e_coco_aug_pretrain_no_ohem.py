_base_ = './htc_hrnetv2p_w40_28e_coco_type_5.py'
# learning policy
# lr_config = dict(step=[24, 27])
# runner = dict(type='EpochBasedRunner', max_epochs=30)
#load_from = 'freeze/type_3_hrnet_htc_aug_medium_gray/epoch_8.pth'
load_from = 'freeze/htc_hrnet_aug_large_no_OHEM_56_epoch/epoch_11.pth'
# resume_from = 'freeze/type_5_hrnet_htc_pretrained/epoch_26.pth'

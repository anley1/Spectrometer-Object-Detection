_base_ = './htc_r50_fpn_1x_coco_type_2.py'
# learning policy
lr_config = dict(step=[16, 19])
runner = dict(type='EpochBasedRunner', max_epochs=28)

_base_ = './libra_faster_rcnn_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://resnext101_64x4d',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=64,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        style='pytorch'))

optimizer_config = dict(_delete_=True,
                        grad_clip=dict(max_norm=35.0, norm_type=2))
runner = dict(type='EpochBasedRunner', max_epochs=28)
checkpoint_config = dict(max_keep_ckpts=1)
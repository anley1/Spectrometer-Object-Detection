_base_ = [
    './faster_rcnn_r50_fpn.py',
    '../_base_/datasets/bead_cropped_type_2.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
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

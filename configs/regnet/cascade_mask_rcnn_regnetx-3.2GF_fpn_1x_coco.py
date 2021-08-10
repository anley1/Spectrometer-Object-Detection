_base_ = [
    '../bead/cascade_mask_rcnn_r50_fpn_1x_coco.py',
]
model = dict(
    pretrained='open-mmlab://regnetx_3.2gf',
    backbone=dict(
        _delete_=True,
        type='RegNet',
        arch='regnetx_3.2gf',
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=True,
        style='pytorch'),
    neck=dict(
        type='FPN',
        in_channels=[96, 192, 432, 1008],
        out_channels=256,
        num_outs=5))

optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.00005)

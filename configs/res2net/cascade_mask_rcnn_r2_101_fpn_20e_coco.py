#_base_ = '../cascade_rcnn/cascade_mask_rcnn_r50_fpn_20e_coco.py'
_base_ = '../bead/cascade_mask_rcnn_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://res2net101_v1d_26w_4s',
    backbone=dict(type='Res2Net', depth=101, scales=4, base_width=26))

optimizer_config = dict(_delete_=True,
                        grad_clip=dict(max_norm=35.0, norm_type=2))

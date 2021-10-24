_base_ = './faster_rcnn_hrnet_fpn_1x_coco_type_2_w32.py'
model = dict(
    pretrained='open-mmlab://msra/hrnetv2_w40',
    backbone=dict(
        type='HRNet',
        extra=dict(
            stage2=dict(num_channels=(40, 80)),
            stage3=dict(num_channels=(40, 80, 160)),
            stage4=dict(num_channels=(40, 80, 160, 320)))),
    neck=dict(type='HRFPN', in_channels=[40, 80, 160, 320], out_channels=256))

optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(_delete_=True,
                        grad_clip=dict(max_norm=35.0, norm_type=2))

runner = dict(type='EpochBasedRunner', max_epochs=30)
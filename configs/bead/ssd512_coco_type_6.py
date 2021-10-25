_base_ = 'ssd300_coco_type_6.py'
input_size = 512
model = dict(
    backbone=dict(input_size=input_size),
    bbox_head=dict(
        in_channels=(512, 1024, 512, 256, 256, 256, 256),
        anchor_generator=dict(
            type='SSDAnchorGenerator',
            scale_major=False,
            input_size=input_size,
            basesize_ratio_range=(0.1, 0.9),
            strides=[8, 16, 32, 64, 128, 256, 512],
            ratios=[[2], [2, 3], [2, 3], [2, 3], [2, 3], [2], [2]])))
# dataset settings
dataset_type = 'CocoDataset'
classes = ('beading', 'nebulizer')
data_root = 'data/'
img_norm_cfg = dict(mean=[123.675, 116.28, 103.53], std=[1, 1, 1], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile', to_float32=True),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(
        type='PhotoMetricDistortion',
        brightness_delta=32,
        contrast_range=(0.5, 1.5),
        saturation_range=(0.5, 1.5),
        hue_delta=18),
    dict(
        type='Expand',
        mean=img_norm_cfg['mean'],
        to_rgb=img_norm_cfg['to_rgb'],
        ratio_range=(1, 4)),
    dict(
        type='MinIoURandomCrop',
        min_ious=(0.1, 0.3, 0.5, 0.7, 0.9),
        min_crop_size=0.3),
    dict(type='Resize', img_scale=(300, 300), keep_ratio=False),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(300, 300),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=False),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=8,
    workers_per_gpu=3,
    train=dict(
        _delete_=True,
        type='RepeatDataset',
        times=5,
        dataset=dict(
            type=dataset_type,
            classes = classes,
            ann_file=data_root + 'w_nebulizer_save_6.json',
            img_prefix=data_root + 'w_nebulizer_save_6/',
            pipeline=train_pipeline)),
    val=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'w_nebulizer_test_iter1.json',
        img_prefix=data_root + 'w_nebulizer_save_4/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        classes=classes,
        ann_file=data_root + 'w_nebulizer_test_iter1.json',
        img_prefix=data_root + 'w_nebulizer_save_4/',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric=['bbox'])

checkpoint_config = dict(max_keep_ckpts=1)
runner = dict(type='EpochBasedRunner', max_epochs=56)
# optimizer
optimizer = dict(type='SGD', lr=(2e-3)/8, momentum=0.9, weight_decay=5e-4)
# optimizer_config = dict(_delete_=True)
optimizer_config = dict(_delete_=True,
                        grad_clip=dict(max_norm=35.0, norm_type=2))


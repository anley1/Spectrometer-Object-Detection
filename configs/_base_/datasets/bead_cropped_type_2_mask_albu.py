dataset_type = 'CocoDataset'
classes = ('beading',)
data_root = 'data/bead_cropped_detection/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
albu_train_transforms = [
    dict(
        type='ShiftScaleRotate',
        shift_limit=0.0625,
        scale_limit=0.0,
        rotate_limit=0,
        interpolation=1,
        p=0.5),
    dict(
        type='ToGray',
        always_apply=False,
        p=1.0)
]

albu_test_transforms = [
    dict(
        type='ToGray',
        always_apply=False,
        p=1.0)
]

train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations',
         with_bbox=True,
         with_mask=True,
         poly2mask=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Pad', size_divisor=32),
    dict(
        type='Albu',
        transforms=albu_train_transforms,
        bbox_params=dict(
            type='BboxParams',
            format='pascal_voc',
            label_fields=['gt_labels'],
            min_visibility=0.0,
            filter_lost_elements=True),
        keymap={
            'img': 'image',
            'gt_masks': 'masks',
            'gt_bboxes': 'bboxes'
        },
        update_pad_shape=False,
        skip_img_without_anno=True),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='DefaultFormatBundle'),
    dict(
        type='Collect',
        keys=['img', 'gt_bboxes', 'gt_labels', 'gt_masks'],
        meta_keys=('filename', 'ori_shape', 'img_shape', 'img_norm_cfg',
                   'pad_shape', 'scale_factor'))
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            # dict(
            #     type='Albu',
            #     transforms=albu_test_transforms,
            #     bbox_params=dict(
            #         type='BboxParams',
            #         format='pascal_voc',
            #         label_fields=['gt_labels'],
            #         min_visibility=0.0,
            #         filter_lost_elements=True),
            #     keymap={
            #         'img': 'image',
            #         'gt_masks': 'masks',
            #         'gt_bboxes': 'bboxes'
            #     },
            #     update_pad_shape=False,
            #     skip_img_without_anno=True),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        classes = classes,
        ann_file=data_root + 'traintype2lower.json',
        img_prefix=data_root + 'images/',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        classes = classes,
        ann_file=data_root + 'testtype2lower.json',
        img_prefix=data_root + 'images/',
        pipeline=test_pipeline),
    test=dict(
        type=dataset_type,
        classes = classes,
        ann_file=data_root + 'testtype2lower.json',
        img_prefix=data_root + 'images/',
        pipeline=test_pipeline))
evaluation = dict(interval=1, metric=['bbox', 'segm'])


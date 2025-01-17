_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/bead_cropped.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
checkpoint_config = dict(max_keep_ckpts=4)
# optimizer
optimizer = dict(type='SGD', lr=0.01, momentum=0.9, weight_decay=0.0001)

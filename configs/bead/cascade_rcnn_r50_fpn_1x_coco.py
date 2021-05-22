_base_ = [
    '../_base_/models/cascade_rcnn_r50_fpn.py',
    '../_base_/datasets/bead_cropped.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

checkpoint_config = dict(max_keep_ckpts=4)

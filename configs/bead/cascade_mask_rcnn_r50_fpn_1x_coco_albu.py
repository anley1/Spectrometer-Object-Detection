_base_ = [
    './cascade_mask_rcnn_r50_fpn_focal_loss.py',
    '../_base_/datasets/bead_cropped_mask_albu.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

checkpoint_config = dict(max_keep_ckpts=4)
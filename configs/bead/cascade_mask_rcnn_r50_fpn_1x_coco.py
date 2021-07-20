_base_ = [
    './cascade_mask_rcnn_r50_fpn.py',
    '../_base_/datasets/bead_cropped_type_2_mask_grayscale_scale.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]

_base_ = [
    '../bead/retinanet_r50_fpn.py',
    '../_base_/datasets/bead_cropped_type_2.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
# optimizer
optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)

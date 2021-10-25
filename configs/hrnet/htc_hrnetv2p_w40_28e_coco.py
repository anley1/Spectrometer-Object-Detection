_base_ = './htc_hrnetv2p_w40_20e_coco.py'
# learning policy
lr_config = dict(step=[24, 27])
# runner = dict(type='EpochBasedRunner', max_epochs=28)

# # optimizer_config = dict(_delete_=True)
# optimizer_config = dict(_delete_=True,
#                         grad_clip=dict(max_norm=35.0, norm_type=2))
# checkpoint_config = dict(max_keep_ckpts=1)

lr_config = dict(step=[24, 27])
runner = dict(type='EpochBasedRunner', max_epochs=56)

# optimizer = dict(type='SGD', lr=0.02, momentum=0.9, weight_decay=0.0001)
optimizer = dict(type='SGD', lr=0.0025, momentum=0.9, weight_decay=0.0001) # from before
optimizer_config = dict(_delete_=True,
                        grad_clip=dict(max_norm=35.0, norm_type=2))
checkpoint_config = dict(max_keep_ckpts=1)

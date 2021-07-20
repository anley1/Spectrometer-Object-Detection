from mmdet.apis import init_detector, inference_detector

config_file = 'configs/bead/cascade_mask_rcnn_hrnetv2p_w40_20e_coco.py'
checkpoint_file = 'freeze/cascade_mask_rcnn_hrnetv2p_w40_20e_coco/latest.pth'

device = 'cuda:0'
model = init_detector(config_file, checkpoint_file, device=device)

# Run inference on image
image_path = 'data/Basler_test.tiff'
res = inference_detector(model, image_path)

# show_result_pyplot(model, image_path, res, score_thr=0.3)

# from show_result_pyplot
if hasattr(model, 'module'):
    model = model.module

model.show_result(image_path, res, score_thr=0.3, show=False, win_name='result_out', bbox_color=(72,101,241), text_color=(72,101,241), out_file='result.jpg') 

 


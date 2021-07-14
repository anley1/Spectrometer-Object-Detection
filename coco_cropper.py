# Crop a chamber region based on COCO annotation bbox
import os
import json
import cv2

from pathlib import Path
from typing import List

def crop_bbox(bbox: List[int], img_name):
    """
    bbox in [x, y, width, height] format
    """
    img = cv2.imread(img_name)
    [x,y,w,h] = bbox  # Destructure
    # https://stackoverflow.com/questions/15589517/how-to-crop-an-image-in-opencv-using-python
    cropped = img[y:y+h, x:x+w]
    return cropped


def save_img(img, save_path: str, f_name: str):
    # Save image to the local filesystem
    out_path = os.path.join(save_path, f_name)
    cv2.imwrite(out_path, img)
    print('Saving {}'.format(f_name))


def get_bbox(anno: str):

    with open(anno, 'r') as j_file:
        data = json.load(j_file)

    # Grab first one
    return data['annotations'][0]['bbox']



if __name__ == "__main__":
    anno_file = 'data/bead_basler_cropped_chamber/chamber.json'
    imgs_path = 'data/beading_basler'
    save_path = 'data/beading_basler_cropped/'

    # Create folder if not exists
    Path(save_path).mkdir(parents=True, exist_ok=True)
    bbox = get_bbox(anno_file)  # List[int]

    for img_name in os.listdir(imgs_path):
        img_path = os.path.join(imgs_path, img_name)
        cropped = crop_bbox(bbox, img_path)
        save_img(img=cropped, save_path=save_path, f_name=img_name)

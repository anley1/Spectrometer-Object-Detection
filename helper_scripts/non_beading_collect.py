# From https://jacopodaeli.medium.com/from-video-to-thumbnails-with-python-and-opencv-ce5983cbb76a
import os
import cv2
import shutil
from pathlib import Path
import json


def run_example():
    """Collect all original size images of non-beading from Frames folder"""
    with open('../data/w_nebulizer_test_iter1.json', "r") as f:
        data = json.load(f)

    # Turn to 0-indexing
    for i in range(len(data['categories'])):
        data['categories'][i]['id'] -= 1
        print(data['categories'][i]['name'])

    for i in range(len(data['annotations'])):
        data['annotations'][i]['category_id'] -= 1

    save_path = os.path.join('C:\\Users\\aleye\\Swin-Transformer-Object-Detection\\data\\with_nebulizer',
                             'zero_index_test.json')
    with open(save_path, 'w') as save_file:
        json.dump(data, save_file)







if __name__ == '__main__':
    run_example()

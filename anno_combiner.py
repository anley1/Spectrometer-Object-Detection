# Combine two COCO json annotation files such that the images and
# annotations are in one JSON file.
import os
import argparse
import json
import copy
import shutil

from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser(description='Combine COCO JSON files')
    parser.add_argument('anno_one', help='first annotation file')
    parser.add_argument('dir_one', help='first image directory')
    parser.add_argument('anno_two', help='second annotation file')
    parser.add_argument('dir_two', help='second image directory')
    parser.add_argument('save_dir', help='directory to save all images')
    parser.add_argument('save_name', help='name of new anno file')

    return parser.parse_args()


def combiner(anno_one: str, dir_one: str, anno_two: str, dir_two: str,
             save_dir: str, save_name: str):
    """
    Combine two JSON COCO files
    """

    # Create save_dir if not exists
    Path(save_dir).mkdir(parents=True, exist_ok=True)

    with open(anno_one, 'r') as file1:
        data1 = json.load(file1)

    with open(anno_two, 'r') as file2:
        data2 = json.load(file2)

    # Index to start the second annotations
    max_ind_1 = max([im['id'] for im in data1['images']])
    snd_img = max_ind_1 + 1

    # Change the second images to offset by first image len. Need to update
    # the corresponding annotations in this process
    for ix in range(len(data2['images'])):
        curr = data2['images'][ix]['id']  # current image index
        for jx in range(len(data2['annotations'])):
            if data2['annotations'][jx]['image_id'] == curr:
                data2['annotations'][jx]['image_id'] = snd_img
        data2['images'][ix]['id'] = snd_img
        snd_img += 1

    images = data1['images'] + data2['images']
    annotations = data1['annotations'] + data2['annotations']
    annotations = unique_annos(annotations)

    # copy the first file metadata and add on the other
    new_data = copy.deepcopy(data1)
    new_data['images'] = images
    new_data['annotations'] = annotations

    save_path = os.path.join(save_dir, save_name)
    with open(save_path, 'w') as save_file:
        json.dump(new_data, save_file)


    # Combine all images into one directory (save_dir)
    # https://stackoverflow.com/questions/41826868/moving-all-files-from-one-directory-to-another-using-python
    copy_files(dir_one, save_dir)
    copy_files(dir_two, save_dir)

def unique_annos(annotations):
    """
    Ensure that annotation keys are unique
    """
    uniq = 0
    for ix in range(len(annotations)):
        annotations[ix]['id'] = uniq
        uniq += 1
    return annotations


def copy_files(src_dir, dest_dir):
    """
    Copy all files from src_dir into dest_dir
    """
    for src_file in Path(src_dir).glob('*.*'):
        shutil.copy(src_file, dest_dir)


if __name__ == "__main__":
    args = parse_args()

    combiner(args.anno_one, args.dir_one, args.anno_two, args.dir_two,
             args.save_dir, args.save_name)

    # Manual:
    # combiner(anno_one='data/w_nebulizer_train_iter1.json',
    #          anno_two='data/out_02_pct_w_nebulizer.json',
    #          dir_one='data/w_nebulizer_save_4',
    #          dir_two='data/out_02_pct_w_nebulizer',
    #          save_dir='data/w_nebulizer_save_6',
    #          save_name='w_nebulizer_save_6.json')

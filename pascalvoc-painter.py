import argparse
import os
import xml.etree.ElementTree as ET
import time
import cv2
from tqdm import tqdm
from PIL import Image
import numpy as np

# Main entry function to start the program
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('pascalDirectory', metavar='pascalDirectory', type=str, help='A path to the directory with Pascal VOC XML files')
    parser.add_argument('imageDirectory', metavar='imageDirectory', type=str, help='A path to the directory with images')
    parser.add_argument('saveDirectory', metavar='saveDirectory', type=str, help='A path to the directory to save Pascal boundingbox images to')

    args = parser.parse_args()

    run(args.pascalDirectory, args.imageDirectory, args.saveDirectory)

# Main function responsible for running necessary code
def run(pascal_dir, image_dir, save_dir):
    # Create save directory if it does not exist
    make_dir(save_dir)
    pascal_files = get_pascal_files(pascal_dir)
    parse_pascal_files(pascal_files, image_dir, save_dir)
    # create_label_dirs(parsed_pascal_files.get('labels'), save_dir)
    # pascalvoc_to_images(parsed_pascal_files.get('pascal_data'), save_dir)

# Get all PascalVOC xml files from a specific path
def get_pascal_files(path):
    # Array of dicts with file data
    files = []
    
    # Loop through all files at a certain path
    for file in tqdm(os.listdir(path)):
        # Only consider XML
        if file.endswith('.xml'):
            # Store relevant file data
            files.append({ 'base': path, 'filename': file, 'path': os.path.join(path, file)}) 

    return files

# Parse a specific PascalVOC file to a usable dict format
def parse_pascal_file(file, image_dir):
    xml_path = file.get('path')

    # XML root
    xml = ET.parse(xml_path)

    # Img name corresponding to XML
    img_name = xml.find('filename').text

    # Img path corresponding to XML
    img_path = xml.find('path').text
    
    # Array of individual objects in a single PascalVOC XML file
    objects = [] 

    # A set of labels within a single PascalVOC XML file 
    labels = set()
    
    # Loop through all labeled objects and add to objects/labels
    for i, obj in enumerate(xml.iter('object')):
        # Number each individual object to be able to get multiple objects from one file
        object_number = i + 1 
        object_name = '{}_{}'.format(object_number, img_name)
        object_label = obj.find('name').text 
        object_bndbox = obj.find('bndbox')
        labels.add(object_label)

        objects.append({
            'path': os.path.join(image_dir, img_name), 
            'name': object_name, 
            'xmin': object_bndbox.find('xmin').text,
            'xmax': object_bndbox.find('xmax').text, 
            'ymin': object_bndbox.find('ymin').text, 
            'ymax': object_bndbox.find('ymax').text, 
            'label': object_label
        })
    
    return { 'objects': objects, 'labels': labels }

# Parse all pascal files
def parse_pascal_files(files, image_dir, save_dir):
    pascal_data = []
    labels = set()
    
    # Loop through all PascalVOC XML files and parse them
    for file in tqdm(files, ascii=True, desc="Parsing pascal files"):
        # Each file represents one image with one or more labels/bboxes
        try:
            parses = parse_pascal_file(file, image_dir)

            # Create label directory if it does not exist
            create_label_dirs(parses.get('labels'), save_dir)
            pascalvoc_to_images(parses.get('objects'), save_dir)

            # Merge all object labels
            # labels = labels.union(parses.get('labels'))

            # Merge all pascal data 
            # pascal_data += parses.get('objects')
        except Exception as e:
            # Just error if a single file can't be read
            print('Error reading PascalVOC XML file.')
            print('ERROR:' + str(e))

    # return { 'pascal_data': pascal_data, 'labels': labels }

# Loop through all PascalVOC data and cut an image from each
def pascalvoc_to_images(pascal_data, save_path):
    n = 0
    # Load the original image
    im = Image.open(pascal_data[0].get('path'))
    for item in tqdm(pascal_data, ascii=True, desc="Creating images from pascal data"):
        if n == 0:
            image = paint_image(item, save_path, im)
        else:
            image = paint_image(item, save_path, image)
        n += 1

    try:
        # Save the image to the save_path in the corresponding label folder
        image.save(os.path.join(save_path, pascal_data[0].get('label'),
                                pascal_data[0].get('name')))
    except Exception as  e:
        # Just error if a single image does not save
        print('Error saving cut image')
        print('ERROR: ' + str(e))

# Cut an image from a PascalVOC file data
def paint_image(pascal_data, save_path, im):
    # Create the bndbox to cut from
    bndbox = {'xmin': float(pascal_data.get('xmin')),
              'ymin': float(pascal_data.get('ymin')),
              'xmax': float(pascal_data.get('xmax')),
              'ymax': float(pascal_data.get('ymax'))}

    # Cut a new image from the image using bndbox
    # image = image.crop(bndbox)
    # paint the image with a bounding box
    # First convert to cv2 format from PIL Image object. From:
    # https://stackoverflow.com/questions/23720875/how-to-draw-a-rectangle-
    # around-a-region-of-interest-in-python
    # im is a PIL Image object
    im_arr = np.asarray(im)
    # convert rgb array to opencv's bgr format
    im_arr_bgr = cv2.cvtColor(im_arr, cv2.COLOR_RGB2BGR)
    # pts1 and pts2 are the upper left and bottom right coordinates of the rectangle
    point1 = tuple(np.int0((bndbox['xmin'], bndbox['ymin'])))
    point2 = tuple(np.int0((bndbox['xmax'], bndbox['ymax'])))
    cv2.rectangle(im_arr_bgr, point1, point2,
                  color=(0, 255, 0), thickness=2)
    im_arr = cv2.cvtColor(im_arr_bgr, cv2.COLOR_BGR2RGB)
    # convert back to Image object
    im = Image.fromarray(im_arr)
    return im

# Function to create all label directories 
def create_label_dirs(labels, save_path):
    for label in tqdm(labels, ascii=True, desc="Creating label directories"):
        make_dir(save_path, label)

# Helper function to create a directory if it does not already exists
def make_dir(path, name = ''):
    path = os.path.abspath(os.path.join(path, name))

    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            # Raise if directory can't be made, because image cuts won't be saved.
            print('Error creating directory')
            raise e

# if __name__ == "__main__":
#     # Override argparser
#     run("other_crop/bead_cropped_detection/bead_cropped_detection/Annotations",
#         "other_crop/bead_cropped_detection/bead_cropped_detection/JPEGImages",
#         "save_test")
# other_crop/bead_cropped_detection/bead_cropped_detection/save_images

# if __name__ == "__main__":
#     # Override argparser
#     run("other_crop/bead_detection/Agilent-PascalVOC-export/Annotations",
#         "other_crop/bead_detection/Agilent-PascalVOC-export/JPEGImages",
#         "save_test_bead_cropped")

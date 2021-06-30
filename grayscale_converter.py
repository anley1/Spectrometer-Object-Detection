# Convert a given dataset to grayscale images.

import os
import cv2
ims_path = 'data/bead_cropped_detection/JPEGImages'
save_path = 'data/bead_cropped_detection/Grayscale'
base_save_path = os.path.abspath(save_path)
base_path = os.path.abspath(ims_path)
for im in os.listdir(base_path):
    im_path = os.path.abspath(os.path.join(base_path, im))
    image = cv2.imread(im_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('Original Image', image)
    # cv2.imshow('Gray Image', gray)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    save_path_im = os.path.abspath(os.path.join(base_save_path, im))
    cv2.imwrite(save_path_im, gray)




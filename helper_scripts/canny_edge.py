import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


img = cv.imread(
    '../data/beading_basler_cropped/Basler_acA2440-35um__23336827__20201013_093810717_1.tiff',0)
edges = cv.Canny(img,100,200)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('"Strong" Edge Detect'), plt.xticks([]), plt.yticks([])
plt.show()
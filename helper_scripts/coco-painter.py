# Use altered pycocotools to save annotated ground-truth images

from pycocotools.coco import COCO
import numpy as np
import os
import skimage.io as io
import matplotlib.pyplot as plt
import pylab

pylab.rcParams['figure.figsize'] = (8.0, 10.0)

dataDir = 'bead_cropped_detection'
saveDir = '{}/{}'.format(dataDir, '2020JSON_Painted')


# Helper function to create a directory if it does not already exists
def make_dir(path, name = ''):
    path = os.path.abspath(os.path.join(path, name))

    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except Exception as e:
            # Raise if directory can't be made.
            print('Error creating directory')
            raise e

def run():
    make_dir(saveDir)
    names = ['train', 'test']
    for filename in names:
        annFile = '{}/{}.json'.format(dataDir, filename)
        # initialize COCO api for instance annotations
        coco = COCO(annFile)
        catIds = coco.getCatIds(catNms=['beading'])
        imgIds = coco.getImgIds(catIds=catIds)
        for imgId in imgIds:
            img = coco.loadImgs([imgId])[0]
            I = io.imread('{}/images/{}'.format(dataDir, img['file_name']))

            # load and display instance annotations
            plt.figure()
            plt.imshow(I)
            plt.axis('off')
            annIds = coco.getAnnIds(imgIds=[img['id']], catIds=catIds,
                                    iscrowd=None)
            anns = coco.loadAnns(annIds)
            coco.showAnns(anns, draw_bbox=True)
            plt.savefig('{}/painted-{}'.format(saveDir, img['file_name']),
                        bbox_inches='tight')
            print("painting {} ...".format(img['file_name']))
            plt.close()

        print("complete!")


if __name__ == "__main__":
    run()
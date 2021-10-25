import json
from sklearn.model_selection import train_test_split

# Split the instance segmentation annotations into a training and testing
# set.

with open('../data/w_nebulizer_save_4/w_nebulizer_save_4.json', "r") as f:
    data = json.load(f)


images = data['images']
annotations = data['annotations']

train_set, test_set = train_test_split(images, test_size=0.2)

anno_train = []
for im in train_set:
    id = im['id']
    for ann in annotations:
        if ann['image_id'] == id:
            anno_train.append(ann)

anno_test = []
for im in test_set:
    id = im['id']
    for ann in annotations:
        if ann['image_id'] == id:
            anno_test.append(ann)

# Construct the json files
training = {
    'info': data['info'],
    'licenses': data['licenses'],
    'categories': data['categories'],
    'images': train_set,
    'annotations': anno_train
}

with open("w_nebulizer_train_iter1.json", "w") as out_file:
    json.dump(training, out_file)

testing = {
    'info': data['info'],
    'licenses': data['licenses'],
    'categories': data['categories'],
    'images': test_set,
    'annotations': anno_test
}


# Write filtered to file
with open("w_nebulizer_test_iter1.json", "w") as out_file:
    json.dump(testing, out_file)
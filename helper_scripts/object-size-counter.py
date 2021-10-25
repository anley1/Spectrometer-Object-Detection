import json
from sklearn.model_selection import train_test_split

# Split the instance segmentation annotations into a training and testing
# set.

with open('../data/w_nebulizer_test_iter6.json', "r") as f:
    data = json.load(f)


images = data['images']
annotations = data['annotations']

SMALL = 32*32
MEDIUM = 96*96
# LARGE is above Medium here so not included
small_count = 0
med_count = 0
large_count = 0

for anno in annotations:
    a = anno["area"]
    if a <= SMALL:
        small_count += 1
    elif SMALL < a < MEDIUM:
        med_count += 1
    else:
        large_count += 1

print("small count: " + str(small_count))
print("med count: " + str(med_count))
print("large count: " + str(large_count))

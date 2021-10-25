import json

# Split the beading dataset into Type 1 and Type 2, respectively.
TYPE2 = True

# Filter function to keep Type 2
def keep_type(observation, isannotation=False, type2=True):
    # observation: a dictionary from JSON, for each image
    if isannotation:
        file_name = observation['image_id']
    else:
        # Use filename
        file_name = observation['file_name']
    test_type = file_name.split("vlcsnap-2019")
    decision: bool = True
    if type2:
        if len(test_type) == 1:
            decision = False
        elif len(test_type) > 1:
            # Type 2 images have 2019 in name
            decision = True
        else:
            raise Exception("Failed on keep_type_2")
    else:
        # Type 1, so invert
        decision = not decision
    return decision

names = ["train", "test"]
for filename in names:

    with open("{}.json".format(filename), "r") as f:
        data = json.load(f)

    # Get all images in the JSON
    images = data['images']
    filtered_images = list(filter(lambda obs: keep_type(observation=obs,
                                                        isannotation=False,
                                                        type2=TYPE2),
                                  images))
    # Filter annotations
    annotations = data['annotations']
    filtered_annotations = list(filter(lambda obs: keep_type(observation=obs,
                                                        isannotation=True,
                                                        type2=TYPE2),
                                  annotations))

    # Keep categories and type, these will remain the same.
    filtered = {'images': filtered_images,
                'type': data['type'],
                'annotations': filtered_annotations,
                'categories': data['categories']}

    # Write filtered to file
    with open("{}type2.json".format(filename), "w") as out_file:
        json.dump(filtered, out_file, indent=2)
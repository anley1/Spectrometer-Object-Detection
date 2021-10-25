from PIL import Image
# From: https://stackoverflow.com/questions/47143332/how-to-pixelate-a-square-image-to-256-big-pixels-with-python

# Open Paddington
im_path = '../data/beading_basler_cropped/Basler_acA2440-35um__23336827__20201013_093810717_1.tiff'
img = Image.open(im_path)

# Resize smoothly down to 16x16 pixels
imgSmall = img.resize((16,16),resample=Image.BILINEAR)

# Scale back up using NEAREST to original size
result = imgSmall.resize(img.size,Image.NEAREST)

# Save
result.save('pixelated_for_example.png')
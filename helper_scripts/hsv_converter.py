import cv2
from pathlib import Path

def main():
    src_dir = "../data/bead_combined_type_4"
    dest_dir = "../data/bead_combined_type_4_hsv"

    for src_file in Path(src_dir).glob('*.*'):
        if src_file.name.endswith('.tiff') or src_file.name.endswith('.png'):
            src_im = cv2.imread(str(src_file))
            image = cv2.cvtColor(src_im, cv2.COLOR_BGR2HSV)
            cv2.imwrite(str(Path(dest_dir + '/' + src_file.name)), image)


if __name__ == "__main__":
    main()
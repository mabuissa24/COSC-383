import sys
import numpy as np
import imageio.v2 as iio
from PIL import Image

def magnify(original):  # Magnifies the least significant bit of image specified on command line
    img = iio.imread(original)
    height, width, _ = img.shape
    for r in range(height):
        for c in range(width):
            img[r, c][0] = (img[r, c][0] & 1) * 255
            img[r, c][1] = (img[r, c][1] & 1) * 255
            img[r, c][2] = (img[r, c][2] & 1) * 255
    iio.imwrite(f"{original[7:len(original) - 4]}_magnified.png", img)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Doesn't specify which file to use.")
        exit(1)
    filename = sys.argv[1]
    magnify(filename)

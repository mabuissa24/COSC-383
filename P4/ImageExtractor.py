import sys
import LSBExtractor as LSB

import numpy as np
import imageio.v2 as imageio
if __name__ == "__main__":  # Reads hidden image in specified format
    if len(sys.argv) != 2:
        print("Doesn't specify which file")
        exit(1)
    filename = sys.argv[1]
    height = LSB.readAsInt(LSB.extract(filename, 0, 32))
    width = LSB.readAsInt(LSB.extract(filename, 32, 32))
    image = LSB.readAsImage(LSB.extract(filename, 32, height * width * 24), height, width)



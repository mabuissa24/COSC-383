import sys
import numpy as np
import imageio.v2 as iio
from PIL import Image


def extract(filename, start, length):
    img = iio.imread(filename)
    height, width, _ = img.shape

    chars = []
    roffset = start // width  # Skip as many full rows as we can
    count = width * roffset
    for r in range(roffset, height):
        for c in range(width):
            chars.append(str(img[r,c,0] & 1))
            chars.append(str(img[r,c,1] & 1))
            chars.append(str(img[r,c,2] & 1))
            if count >= start + length:
                break
            count += 3
        if count >= start + length:
            break
    input = "".join(chars)[start % width:start % width + length]
    return input


def readAsInt(LSB):
    return int(LSB, 2)


def readAsText(LSB):
    n = 8
    string = ""
    for i in range(0, len(LSB), n):
        string += chr(int(LSB[i:i + n], 2))
    return string


def readAsImage(LSB, height, width):
    img = np.zeros([height, width, 3], dtype=np.uint8)
    im = Image.fromarray(img)  # convert numpy array to image
    im.save('extracted.png')
    img = iio.imread('extracted.png')
    n = 8
    pixels = []
    for i in range(0, len(LSB), n):
        pixels.append(int(LSB[i:i + n], 2))
    count = 0
    for r in range(height):
        for c in range(width):
            img[r, c][0] = pixels[count]
            img[r, c][1] = pixels[count + 1]
            img[r, c][2] = pixels[count + 2]
            count += 3
    iio.imwrite("extracted.png", img)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Doesn't specify which file, where to start and how much to read.")
        exit(1)
    filename = sys.argv[1]
    start = int(sys.argv[2])
    length = int(sys.argv[3])
    LSB = extract(filename, start, length)
    print(readAsInt(LSB))

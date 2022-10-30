import sys

import numpy as np
import imageio.v2 as imageio
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Doesn't specify which file, where to start and how much to read.")
        exit(1)
    filename = sys.argv[1]
    start = int(sys.argv[2])
    length = int(sys.argv[3])
    img = imageio.imread(filename)
    height, width, _ = img.shape
    print("Height:", height, "Width:", width)

    chars = []
    roffset = start // width  # Skip as many full rows as we can
    count = width * roffset
    for r in range(roffset, height):
        for c in range(width):
            if start <= count:
               chars.append(str(img[r,c,0] & 1))
               chars.append(str(img[r,c,1] & 1))
               chars.append(str(img[r,c,2] & 1))
            if count >= start + length:
                break
            count += 1
        if count >= start + length:
            break
    input = "".join(chars)
    print("input is ", input)

    n = 8
    string = ""
    for i in range(0, len(input), n):
        string += chr(int(input[i:i+n], 2))
    print(string)

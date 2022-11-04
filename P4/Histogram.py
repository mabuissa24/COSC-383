import sys
import imageio.v2 as imageio
import pandas as pd
import matplotlib.pyplot as plt


def get_least_significant_bit(row, column, img):
    return str(str(img[row, column, 0] & 1)+str(img[row, column, 1] & 1)+str(img[row, column, 2] & 1))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Doesn't specify file to use.")
        exit(1)
    filename = sys.argv[1]
    img = imageio.imread(filename)
    height, width, _ = img.shape
    four_square = []
    count = 0
    for r in range(height-1):
        for c in range(width-1):
            a = ""
            a = a + get_least_significant_bit(r, c, img) + get_least_significant_bit(r + 1, c, img)
            a = a + get_least_significant_bit(r, c + 1, img) + get_least_significant_bit(r + 1, c + 1, img)
            four_square.append(a)
    df = pd.DataFrame(four_square, columns=["pixels"])
    df['pixels'].value_counts().plot(kind='bar')
    plt.xticks([])
    plt.show()

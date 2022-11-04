import sys
import LSBExtractor as LSB


if __name__ == "__main__":  # Reads hidden text in specified format
    if len(sys.argv) != 2:
        print("Doesn't specify which file")
        exit(1)
    filename = sys.argv[1]
    length = LSB.readAsInt(LSB.extract(filename, 0, 32))
    text = LSB.readAsText(LSB.extract(filename, 32, length * 8))
    print(text)



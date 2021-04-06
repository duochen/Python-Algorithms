import sys

def find_max(arrays):
    array_length = len(arrays)
    for i in range(0, array_length - 1):
        if (arrays[i] > arrays[i + 1]):
            temp = arrays[i]
            arrays[i] = arrays[i + 1]
            arrays[i + 1] = temp
    maxValue = arrays[array_length - 1]
    return maxValue


def main():
    scores = [60, 50, 95, 80, 70]
    maxValue = find_max(scores)
    print ("Max Value = ", maxValue)

if __name__ == "__main__":
    main()

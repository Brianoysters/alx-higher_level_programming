#!/usr/bin/python3
def summation_arguments(argv):
    y = len(argv) - 1
    if y == 0:
        print("{:d}".format(y))
        return
    else:
        index = 1
        summation = 0
        while index <= y:
            summation += int(argv[index])
            index += 1
        print("{}".format(summation))


if __name__ == "__main__":
    import sys
    summation_arguments(sys.argv)

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arguments = sys.argv
    length = len(arguments) - 1

    if length > 1:
        print("{} arguments:".format(length))
        for index in range(1, length + 1):
            print("{}: {}".format(index, arguments[index]))

    elif length == 0:
        print("{} arguments.".format(length))

    else:
        print("{} argument:".format(length))
        print("{}: {}".format(length, arguments[1]))

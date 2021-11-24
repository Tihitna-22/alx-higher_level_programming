#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    alen = len(sys.argv) - 1
    if alen == 0:
        print("{} arguments.".format(alen))
    elif alen == 1:
        print("{} arguments:".format(alen))
    else:
        print("{} arguments:".format(alen))

    for i in range(alen):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

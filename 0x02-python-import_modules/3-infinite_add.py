#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    alen = len(sys.argv)
    res = 0
    for i in range(1, alen):
     if alen > 1:
        res +=  int(sys.argv[i])
        i += 1
    print(res)

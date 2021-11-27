#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul,div
    import sys
    alen = len(sys.argv)
    if alen != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    oper = sys.argv[2]
    x = int(sys.argv[1])
    y = int(sys.argv[3])
    if oper == "+":
        print("{} {} {} = {}".format(x, oper, y, add(x, y)))
    elif oper == "-":
        print("{} {} {} = {}".format(x, oper, y, sub(x, y)))
    elif oper == "*":
        print("{} {} {} = {}".format(x, oper, y, mul(x, y)))
    elif oper == "/":
        print("{} {} {} = {}".format(x, oper, y, div(x, y)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        quit(1)

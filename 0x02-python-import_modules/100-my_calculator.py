#!/usr/bin/python3

if __name__ == "__main__":
    """The funct manages basic arithmetic operation."""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    opts = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(opts.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    xx = int(sys.argv[1])
    yy = int(sys.argv[3])
    print("{} {} {} = {}".format(xx, sys.argv[2], yy, opts[sys.argv[2]](xx, yy)))

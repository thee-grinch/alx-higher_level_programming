#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    import calculator_1 as cl
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    c = argv[2]

    if c == "+":
        print("{} + {} = {}".format(a, b, cl.add(a, b)))
    elif c == "-":
        print("{} - {} = {}".format(a, b, cl.sub(a, b)))
    elif c == "*":
        print("{} * {} = {}".format(a, b, cl.mul(a, b)))
    elif c == "/":
        print("{} / {} = {}".format(a, b, cl.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

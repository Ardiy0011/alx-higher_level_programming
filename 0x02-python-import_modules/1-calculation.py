#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, (calc.add(a, b))))
    print("{} - {} = {}".format(a, b, (calc.subtract(a, b))))
    print("{} * {} = {}".format(a, b, (calc.multiply(a, b))))
    print("{} / {} = {}".format(a, b, int((calc.divide(a, b)))))

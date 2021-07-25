import sys

def set_ops(a, b, second_arg_is_zero):
    if second_arg_is_zero:
        return [a + b, a - b, a * b, "ERROR (div by zero)", "ERROR (modulo by zero)"]
    else:
        return [a + b, a - b, a * b, a / b, a % b]

def print_ops(result):
    print("Sum:".ljust(15), end='')
    print("{}".format(result[0]))
    print("Difference:".ljust(15), end='')
    print("{}".format(result[1]))
    print("Product:".ljust(15), end='')
    print("{}".format(result[2]))
    print("Quotient:".ljust(15), end='')
    print("{}".format(result[3]))
    print("Remainder:".ljust(15), end='')
    print("{}".format(result[4]))


if __name__ == "__main__":
    usage = "Usage: python operations.py <number1> <number2>\nExample:\n\tpython operations.py 10 3"
    argc = len(sys.argv)
    if argc == 1:
        print(usage)
    elif argc == 2:
        print("InputError: not enough arguments\n")
        print(usage)
    elif argc > 3:
        print("InputError: too many arguments\n")
        print(usage)
    else:
        try:
            a = int(sys.argv[1])
            b = int(sys.argv[2])
            result = set_ops(a, b, b == 0)
            print_ops(result)
        except BaseException:
            print("InputError: only numbers\n")
            print(usage)

from calculator import add, mul, sub, div

operations = \
    {
        '+': add,
        '*': mul,
        '-': sub,
        '/': div,
    }


def main():
    num1 = int(input("What's the first number?: "))
    num2 = int(input("What's the second number?: "))
    for symbol in operations:
        print(symbol)

    operation_simbol = input("Pick an operation from the line above: ")

    print(f"{num1} {operation_simbol} {num2} = {operations[operation_simbol]([num1, num2])}")


if __name__ == '__main__':
    main()
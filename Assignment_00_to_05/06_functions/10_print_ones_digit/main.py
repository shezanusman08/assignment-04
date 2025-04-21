def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)


def print_ones_digit(num):
    print("The ones digit is", num % 10)


if __name__ == '__main__':
    main()
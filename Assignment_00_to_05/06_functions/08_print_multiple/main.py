def main():
    message = input("Please type a message: ") 
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)  

def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

if __name__ == '__main__':
    main()
#     # Test the function with a message and number of repeats
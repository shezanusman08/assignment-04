def main():
    # Example usage
    number = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))
    
    if in_range(number, low, high):
        print(f"{number} is in range!")
    else:
        print(f"{number} is NOT in range!")

def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    if n >= low and n <= high:
        return True

    # We could have also included an else statement, but since we are returning, it's fine without!
    return False

if __name__ == '__main__':
    main()

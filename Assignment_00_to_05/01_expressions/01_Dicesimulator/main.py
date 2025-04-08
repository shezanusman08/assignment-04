

import random

def roll_dice():
    dice1: int = random.randint(1, 6)
    dice2: int = random.randint(1, 6)

    total: int = dice1 + dice2

    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total of two dice is: {total}")

def main():
    diec1: int = 10
    print(f"Dice 1 in main() start as: {diec1}")

    roll_dice()
    roll_dice()
    roll_dice()

    print(f"Dice 1 in main() end as: {diec1}")

if __name__ == "__main__":
    main()

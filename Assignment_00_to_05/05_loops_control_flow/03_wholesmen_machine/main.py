AFFIRMATION:str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation:\n" + AFFIRMATION)

    user_feedback:str= input()  # Getting user input

    while user_feedback != AFFIRMATION: # While the user's input isn't the affirmation
        # Tell the user that they did not type the affirmation correctly
        print("That was not the affirmation.")
        print("Please try again!")
        # Ask the user to type the affirmation again!
        print("Please type the following affirmation:\n" + AFFIRMATION)
        user_feedback:str= input()

    print("That's right! :)")

if __name__ == "__main__":
    main()
     
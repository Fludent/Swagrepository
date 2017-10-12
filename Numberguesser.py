import random



def main():
    print ("This is a guessing game, guess the right number between 1 and 100")
    randomNmb =  random.randint(1, 100)
    found = False

    while not found:
        try:
            guess = int(input("Your guess please: "))
        except ValueError:
            print("Please enter a number.")
            continue
        except NameError:
            print("Please enter a number.")
            continue
        if guess == randomNmb:
            print("You got it!")
            break
        elif guess > 100:
            print("That's not a number between 1 and 100...")
        elif guess > randomNmb:
            print("Guess lower")
        elif guess not in range(1, 100):
            print("That's not a number between 1 and 100...")
        else:
            print("Guess higher")


if __name__ == "__main__":
    main()




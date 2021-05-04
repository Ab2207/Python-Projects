import random

number = random.randint(1,10)
player_name = input("Enter your name: ")
print("Hey, {}. I'm guessing a number between 1 to 10".format(player_name))

number_of_guesses = 0
max_guesses = 5

while number_of_guesses < max_guesses:

    guess_number = int(input("I have the number in mind. Your turn to guess the number: "))
    number_of_guesses += 1
    guesses_left = max_guesses - number_of_guesses

    if guess_number == number:
        print("You've guessed the right number {}".format(number))
        print()
        break

    elif guess_number > 10:
        print("You've guessed a number which is out of range")
        print()

    elif guess_number!= number:
        print("You've guessed the wrong number. You have {} tries left".format(guesses_left))
        print()


if guess_number == number:
    print("You've guessed the number in {} tries.".format(number_of_guesses))
    print()

else:
    print("Sorry, you guessed the wrong number and exhausted the number of tries")
    print()



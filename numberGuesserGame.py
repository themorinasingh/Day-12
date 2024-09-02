from art import art
import random

def number_guessing_game():
    #guessing the random number and printing the game start
    print(art)

    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    computers_guess = random.randrange(1,101)

    #setting up the stage for levels and choosing number of remaining attempts
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    num_attempts = 0

    if level == 'easy':
        num_attempts = 10
        print(f"You get {num_attempts} attempts")
    elif level == 'hard':
        num_attempts = 5
        print(f"You get {num_attempts} attempts")


    while num_attempts > 0:
        player_guess = int(input("Guess the Number: "))

        if player_guess > computers_guess:
            print("Too High \nGuess Again")

        elif player_guess < computers_guess:
            print("Too Low \nGuess Again")
        elif player_guess == computers_guess:
            print("You won the game")
            break

        num_attempts -= 1

        print(f"You have {num_attempts} attempts remaining.")

    play_again = input("Do you wanna play again? y/n").lower()

    if play_again == 'y':
        number_guessing_game()
    else:
        print("Thank For Playing")



number_guessing_game()
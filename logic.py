import random

low = int(input("Give your lower numbers (default 1):") or 1)
high = int(input("Give your higher numbers (default 20):") or 20)

correct_ans = random.randint(low, high)
guess_allowed = 5

def playGame():
    for i in range(guess_allowed):
        try:
            guess = int(input(f"Guess a number between {low} and {high}:"))
            if (i == guess_allowed - 1):
                print("sorry, you are run out of guess. You lost!")
            elif guess == correct_ans:
                print("Congratulations, You are win")
                break
            elif guess < correct_ans:
                print("Correct ans is greater")
            elif guess > correct_ans:
                print("Correct ans is smaller")

        except ValueError:
            print("Invalid input, please eneter a valid number.")

    print('----------------------------------------------------------------')
    print("The Game is End. You can play again!")
    print('----------------------------------------------------------------')
    return playGame()

if __name__ == "__main__":
    print("Welcome to the Number Guessing Game")
    playGame()



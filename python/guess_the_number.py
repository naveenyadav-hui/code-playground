"""A small number guessing game for the terminal."""
import random


def play(low: int = 1, high: int = 100) -> None:
    secret = random.randint(low, high)
    tries = 0
    print(f"I'm thinking of a number between {low} and {high}.")
    while True:
        guess = int(input("Your guess: "))
        tries += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"Got it in {tries} tries.")
            break


if __name__ == "__main__":
    play()

import random
def game(n):
    guess = 0 
    number = random.randint(1,n)
    while guess != number:
        guess = int(input(f"Guess a number between 1 and {n} : "))
        if guess < number:
            print("Guess too low")
        elif guess > number:
            print("Guess too high ")
    print(f"Yay, you have guessed the correct number {number}")
game(10)
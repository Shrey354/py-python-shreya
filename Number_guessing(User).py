import random
def computer_guess(n):
    low = 1
    high = n
    feedback =''
    while feedback != 'c':
        guess = random.randint(low,high)
        feedback = input(f"{guess} L for too low, H for too high, C for correct ").lower()
        if feedback == 'h':
            high =guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Correct!! Computer guessed your number {guess} correctly.")
computer_guess(10)


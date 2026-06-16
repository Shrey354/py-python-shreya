import random
import sys
def game():
    computer = random.choice(['r','s','p'])
    user = input("Enter R for rock, S for scissor , P for paper").lower()
    choices = {'r':'rock','s':'scissor','p':'paper'}
    if user not in ('r','s','p'):
        sys.exit("You must enter R, S or P")
    print(f"Computer chose {choices[computer]} and  User chose {choices[user]}.")
    if user == computer:
        return "It's a tie"
    if user_win(user,computer):
        return "You Won"
    return "You Lost"
    
def user_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True  
print(game())


import sys
print("Welcome to Quiz Game")
def game():
    score = 0 
    query = input("Do you want to play the game? (Yes/No) : ").lower()
    if query == "yes":
        print("Start Playing")
        question1 = input("What is capital city of Nepal: ").lower()
        if question1 == "Kathmandu" :
            print("Correct Answer")
            score +=1
        else:
            print("Incorrect Answer")
        question2 = float(input("What is height of Mount Everest (in meters): "))
        if question2 == 8848.86 :
            print("Correct Answer")
            score +=1
        else:
            print("Incorrect Answer")
        question3 = input("What is full form of CPU: ").lower()
        if question3 == "Central Processing Unit" :
            print("Correct Answer")
            score +=1
        else:
            print("Incorrect Answer")
        question4 = input("What is full form of GPU: ").lower()
        if question4 == "Graphical Processing Unit" :
            print("Correct Answer")
            score +=1
        else:
            print("Incorrect Answer") 
        total = (score/4)*100
        print(f"Your total score is {total} %")
    else:
        sys.exit("Oops!!!")
        
game()




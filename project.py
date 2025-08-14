# WORKFLOW OF GAME:
"""
user input (Rock,Paper,Scissor)
computer input (Rock,Paper,Scissor randomlyy using random keyword)
result print

Case 1: Rock
Rock - Rock = tie
Rock - Paper = Paper
Rock -Scissor = Rock

Case 2: Paper
Paper - Paper = tie
Paper - Rock = Paper
Paper - Scissor = Scissor

Case 3: Scissor
Scissor - Scissor = tie
Scissor - Paper = Scissor
Scissor - Rock = Rock

"""
import random
item_list = ["Rock","Paper","Scissor"]
user_choice = input("enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(item_list)
print(f"user choice = {user_choice},computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both choses same : = match tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("computer wins")
    else :
        print("you win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("you win")
    else:
        print("computer wins")         

elif user_choice == "Scissor":
    if user_choice == "Paper":
        print("you win")
    else:
        print("computer wins")


        


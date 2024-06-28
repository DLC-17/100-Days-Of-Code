import random
def game():
    decision=str(input("Make your choice of Rock Paper or Scissors: "))
    computer=["rock","paper","scissors"]
    computer_choice=random.choice(computer)
    print(computer_choice)
    if decision==computer_choice:
        print("It's a tie")
    elif computer_choice=="rock" and decision=="scissors":
        print("You lose")
    elif computer_choice=="rock" and decision=="paper":
        print("You win")
    elif computer_choice=="paper" and decision=="rock":
        print("You lose")
    elif computer_choice=="paper" and decision=="scissors":
        print("You win")
    elif computer_choice=="scissors" and decision=="rock":
        print("You win")
    elif computer_choice=="scissors" and decision=="paper":
        print("You lose")
game()


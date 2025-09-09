import random
def get_choices(Player_choice,Computer_choice):
    if Player_choice==Computer_choice:
        return "Game is a tie"
    elif Computer_choice=="rock":
        if Player_choice=="scissors":
            return "Rock smashes Scissors! You Lose!!"
        else:
            return "Paper catches Rock! You win"
    elif Computer_choice=="paper":
        if Player_choice=="scissors":
            return "Scissors cuts Paper! You win!!"
        else:
            return "Paper catches Rock! You Lose!!"
    elif Computer_choice=="scissors":
        if Player_choice=="paper":
            return "Scissors cuts Paper! You Lose!!"
        else:
            return "Rock smashes Scissors! You win!!"
while True:
   print("Choose from the following options")
   print("Rock")
   print("Paper")
   print("Scissors")
   Playerchoice=input("Enter the choice:")
   Playerchoice=Playerchoice.lower()
   option=["Rock","Paper","Scissors"]
   Computerchoice=random.choice(option)
   print(f"The computer choice is {Computerchoice}")
   Computerchoice=Computerchoice.lower()
   print(get_choices(Playerchoice,Computerchoice))
   x=input("Do u want to continue the game (Yes/No):")
   if x=="Yes":
       continue
   elif x=="No":
       break
   else:
       print("Your input is Invalid")
       break
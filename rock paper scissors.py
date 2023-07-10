import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

games = [rock, paper, scissors]
option = int(input("pick 0 for rock, 1 for paper and 2 for scissors \n"))
if option >= 3 or option < 0:
    print("invalid number, you lose")
else:
    computer = random.randint(0, 2)
    print("you chose:")
    print(games[option])
    print("computer chose: \n")
    print(games[computer])

if option == computer:
    print("It's a draw")
elif computer == 0 and option == 2:
    print("you lose, try again")
elif option == 0 and computer == 2:
    print("you won. congratulations!!!")
elif option > computer:
    print("you won, congratulations!!!")
elif computer > option:
    print("you lose, try again")
elif option == 0 and computer == 2:
    print("you won. congratulations!!!")

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


import random
choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
draw = [rock, paper, scissors]
if int(choice)>2 or int(choice)<0:
  print("Error: No valid choice available.")
else:  
  print(draw[int(choice)])

  print("Computer chose: ")
  cchoice = random.randint(0,2)
  print(draw[cchoice])

  if int(choice) == cchoice:
    print("Draw")
  elif int(choice) == 0:
    if cchoice == 1:
      print("You loose")
    else:
      print("You win")
  elif int(choice) == 1:
    if cchoice == 2:
      print("You loose")
    else:
      print("You win")
  elif int(choice) == 2:
    if cchoice == 0:
      print("You loose")
    else:
      print("You win")

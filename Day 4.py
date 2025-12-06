# Rock,Paper,Scissors Game
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

random_shape = [rock,paper,scissors]
we_chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if we_chose >= 0 and we_chose <= 2:
    print(random_shape)

random_shape_index = random.randint(0,2)
print(random_shape[random_shape_index])

if we_chose == random_shape_index:
    print("It is a draw!")
elif we_chose == 0 and random_shape_index == 2:
    print("We won!")
elif we_chose == 0 and random_shape_index == 1:
    print("We lost!")
elif we_chose == 1 and random_shape_index == 0:
    print("We won!")
elif we_chose == 1 and random_shape_index == 2:
    print("We lost!")
elif we_chose == 2 and random_shape_index == 0:
    print("We lost!")
elif we_chose == 2 and random_shape_index == 1:
    print("We won!")
else:
    print("Not valid")


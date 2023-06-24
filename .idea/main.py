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

#Need to print the input prompt
print("Welcome to Rock, Paper, Scissors!")
print("Can you beat the computer?")
choice = int(input("What do you chose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))

#Create a list of the different options
choices = [rock, paper, scissors]

#Recieve user input and print their option
print(choices[choice])
#Randomly generate the computer option and print
computer_choice = random.randint(0,2)
print(choices[computer_choice])

#Compare the two options to determine who wins
if choice == computer_choice: 
  print("It's a draw! No winners here.")
elif choice == 0 and computer_choice == 1: 
  print("You loose! HAHAHAHAHA")
elif choice == 0 and computer_choice == 2: 
  print ("How can I lose to a human? :(")
elif choice == 1 and computer_choice == 0: 
  print("You just got lucky. HMPH!")
elif choice == 1 and computer_choice == 2:
  print("The superior brain wins! Human, you will never beat me!")
elif choice == 2 and computer_choice == 0:
  print("Just give up! I will also win against a human! ")
elif choice == 2 and computer_choice == 1: 
  print ("It can't be! How did I lose to you?")
  
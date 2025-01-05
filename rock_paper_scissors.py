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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number, You loose!")
elif user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
else:
    print(scissors)

#computer's turn
print("Computer Chose:\n")
computer_choice = random.randint(0,2)
if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number, You loose!")
elif computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)
#rules of rock paper and scissors
if computer_choice == user_choice:
    print("Match Draw")
elif user_choice== 0 and computer_choice == 1:
    print("You loose!")
elif user_choice== 0 and computer_choice == 2:
    print("You win!")
elif user_choice== 1 and computer_choice == 0:
    print("You win!")
elif user_choice== 1 and computer_choice == 2:
    print("You loose!")
elif user_choice== 2 and computer_choice == 0:
    print("You loose!")
else:
    print("You win!")






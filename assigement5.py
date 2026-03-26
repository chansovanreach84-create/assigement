import random
user_score = 0 
computer_score = 0

choices = ['rock', 'paper', 'scissors']

while True :
    user_input = input("Enter your choice :").strip().lower()
    if user_input == 'quite':
        break
    if user_input not in choices :
        print("Invalid choice, Plese try again!! ")
        continue
    computer = random.choice(choices)
    print(f"Computer choice is :, {computer}")
    if user_input == computer :
        print("No one wins!! ")
    elif (user_input == 'rock' and computer == 'scissors') or\
         (user_input == 'paper' and computer == 'rock') or\
         (user_input == 'scissors' and computer == 'paper'):
        print("user is winer!! , Congratulations.......")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

print(f"Total Scores - You: {user_score}, Computer: {computer_score}")
if user_score > computer_score:
    print("Congratulations! You are the winner of the game......")
else:
    print("Computer is the winner of the game......")
    print("Thank You for playing our game!!")
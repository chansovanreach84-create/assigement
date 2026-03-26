my_number = 7
while True :
    guess = int(input("guess the number Start From(1-100): "))
    if guess == my_number:
        print("Congratulations!! Your guess is correct.")
        break
    elif guess < my_number:
        print("Too low! Try again.")
    elif guess > my_number:
        print("Too high! Try again.")
    else:
        print("Invalid input, Please Guess a number between 1 to 100 .")
        
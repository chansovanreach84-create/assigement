import random

user_score = 0
number_exist = [1,2,3,4,5,6,7,8,9,10,11,12]

while True :
    num1 = random.choice(number_exist)
    num2 = random.choice(number_exist)
    
    user_guess = input(f"What is {num1}*{num2}? : ")
    num1 = int(num1)
    num2 = int(num2)
    answer = int(user_guess)
    if answer == num1 * num2 :
        print("Congratulations!! You are correct.....")
        user_score +=1
    else:
        print("Incorrect answer!! Try again......")
        print("The correct answer is :", num1 * num2)
        print (f"Your total score is : {user_score}")
        break


print("...............Welcome to our restaurant...............")
menu_order = ["coca", "pepse" , "cofe", "tea"]
print("coca : 10$")
print("pepsi : 20$")
print("cofe : 30$")
print("tea : 40$")
total=0
while True:
    
    order_input=input("What kind of these do you want to order :").strip().lower()
    if 'coca' in order_input:
        print("This one is cost : 10$")
        total += 10
    elif 'pepsi' in order_input:
        print("This one is cost : 20$")
        total +=20
    elif 'cofe' in order_input:
        print("This one is cost : 30$")
        total +=30
    elif 'tea' in order_input:
        print("This one is cost : 40$")
        total +=40
    elif 'checkout' in order_input:
        
        print("Thank You For supporting us!! ")
        print(f"Here is your reciept : {total}$")
        break
    elif order_input not in menu_order :
        print("Sorry Sir/Madam , we don't have this one in our menu.......")
        continue
        
        
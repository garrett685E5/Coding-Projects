"""Name: Tiffani Garrett
Problem: Create a pizza menu 
Date: 06/18/2024
Version: 3.12
""" 
#Declare list variables
#Create a list of pizza sizes and valid choices
#Define List variables
#
# 
# pizza_options = ["Large-1", "Medium-2", "Small-3"]
print("Hi! How are you? What size cheese pizza would you like today?")
pizza_choice = int(input("Enter number 1, 2, 3"))
valid_choices = int[1, 2, 3]

#pizza_size = int(input())


#User Input/ Loop Statement
#print("What size cheese pizza do you want?")
#for size in pizza_sizes:
    #print(size)
    #while True:
        #if pizza_choice not in valid_choices:
 #else:
            #break
    

        
#Create a list of pizza toppings and define variables
pizza_toppings = ["Pepperoni", "Sausage", "Olives"]
topping_count = 0
#for statement ( outer statement)
for topping in pizza_toppings:
    #inside while statement
    while True:
        print(f"Do you want {topping}? 1 for Yes, 0 for no:")
        topping_choice = input()
        #conditional statements
        if topping_choice == "1":
            topping_count = topping_count + 1
            break
        elif topping_choice == "0":
            break
        else:
            print("You did not enter a valid choice")
#while statemnt for user quantity         
while True:
    print("How many pizzas would you like?")
    quantity = input()
    if quantity.isdigit():
    	break
else:
    print("Enter a quantity.")
#Define varibales (Assign prices to menu options)               
print("Thank you for your order!")

if pizza_choice == "1":
    p_size = "Large"
    price = 12
if pizza_choice == "2":
    p_size = "Medium"
    price = 9
if pizza_choice == "3":
    p_size = "Small"
    price = 6

print(f"Quantity: {quantity}  Item: {p_size} cheese pizza, - ${(price + topping_count) * int(quantity)}")
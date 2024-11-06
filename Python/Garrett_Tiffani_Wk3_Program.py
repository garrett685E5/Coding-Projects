"""
Name: Tiffani Garrett
Problem: Create a Ticket Price Calculator program that calculates the ticket price for a movie theater based on the age of the customer and the time of the movie.
Date: 06/04/2024
Version: 3.12
"""

#ASSIGN VARIABLES
numA=12 
numB=55
numC= 5

#INPUT
AGE= int(input("How old are you?"))
TIME= int(input("What time is it?"))

#PROCESS AND OUTPUT
if AGE < numA:
    print("Under 12 - $5.")
    if str(AGE < numA) and str(TIME < numC):
        print("(-$2 matinee discount) Total:$3.")
else:
    print("12 and over Total:$10.")
    if str(AGE > numB) or str(AGE== numB) and str(TIME < numC):
        print("(-$2 matinee discount) Total: $8.")
    else:
        print("55 or older- $7.")
        if str(AGE > numB) or str(AGE= numB) and str(TIME < numC):
            print("(-$5 matinee discount) Total: $5.")
    








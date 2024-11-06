"""
Name: Tiffani Garrett
Problem: Create a Simple Library Program to support borrowing of available books and returning of books to make them available. The program needs to provide a menu of options to the user to permit them to (1) display a list of available and borrowed books, (2) borrow a book, (3) return a book, and (4) exit the program. 
Date: 07/09/2024
Version 3.13
""" 
#DECLARE LIST VARIABLES OR OPEN BOOKS AND AN EMPTY CONTAINER LIST THAT WILL BE DEFINED BY THE USER LATER IN PROGRAM.
available_books = ["1984", "THE GREAT GATSBY", "THE ALCHEMIST", "MOBY DICK", "BELOVED", "HARRY POTTER"]
borrowed_books = []
#DECLARE 1ST FUNCTION TO DISPLAY AVAILABLE BOOKS W/ SELECTIVE STATMENTS DISPLAY EITHER OR LISTS
def display_books():
    print ("Available Books:")
    if available_books:
        for book in available_books:
            print(book)
    else:
        print("THERE ARE NO AVAILABLE BOOKS")
    print("YOUR CHECKED OUT BOOKS:")
    if borrowed_books:
        for book in borrowed_books:
            print(book) 
    else:
        print("YOU HAVEN'T CHECKED OUT ANY BOOKS YET")

#DECLARE 2ND FUNCTION TO ADD USER INPUT W/ SELECTIVE STATEMENTS AND FUNCTIONS TO ADD BOOK TO ADD AND REMOVE FROM LISTS
def checkout_book(book_name):
    if book_name in available_books:
        available_books.remove(book_name)
        borrowed_books.append(book_name)
        print(f"YOU CHECKED OUT {book_name}")
    else:
        print (f" {book_name} IS NOT AVAILABLE")
#DECLARE 3RD FUNCTION TO REMOVE USER INPUT FROM BOOK_NAME FROM BORROWED BOOKS LIST AND ADD TO AVAILABLE BOOKS
def return_book (book_name):
    if book_name in borrowed_books:
        borrowed_books.remove(book_name)
        available_books.append(book_name)
        print (f"THANK YOU FOR RETURNING {book_name}!")
    else:
        print(f"NO RECORDS FOUND IN LIBRARY DATABASE UNDER THIS TITLE. PLEASE CHECK TITLE NAME")
#WHILE LOOP TO CONTINUOUSLY DISPLAY MENU OPTIONS AFTER USER MAKES SELECTIVE OPTIONS
while True:
    print("WELCOME TO THE SELF-SERVE LIBRARY!")
    print ("1. DISPLAY LIST OF AVAILABLE AND BORROWED BOOKS")
    print ("2. BORROW A BOOK")
    print ("3. RETURN A BOOK")
    print ("4. EXIT")
#DEFINE VARIABLE FOR USER'S MENU CHOICE
    menu_option = input("CHOOSE FROM THE FOLLOWING FOUR MENU OPTIONS 1-4:")
#SELECTIVE STATEMENTS TO PROCESS A SPECIFIC FUNCTION BASED OFF USER'S OPTION 
    if menu_option == "1":
        display_books()
    elif menu_option == "2":
        choose_book = input("WHAT IS THE NAME OF THE BOOK YOU WOULD LIKE TO CHECK OUT?(TYPE TITLE NAME IN ALL CAPS)")
        checkout_book(choose_book)
    elif menu_option == "3":
        remove_book = input("WHAT IS THE NAME OF THE BOOK YOU WOULD LIKE TO RETURN? (TYPE TITLE NAME IN ALL CAPS)")
        return_book (remove_book)
    #BREAK FROM THE LOOP AND EXIT
    elif menu_option == "4":
        print("YOU CHOSE TO EXIT. THANKS FOR STOPPING BY!")
        break
    else:
        print("INVALID OPTION.")

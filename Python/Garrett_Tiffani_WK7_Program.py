"""
Name: Tiffani Garrett
Problem: Create a Movie Recommendations List Program that provides a menu of options to the user to permit them to (1) add a movie to the list, (2) display the movie recommendations on the list, and (3) exit the program. The program prompts the user to enter their menu choice and a combination of selection and repetition structures should support the processing logic for each of the three menu options.
Date: 06/29/2024
Version 3.13
""" 

#FUNCTION MAIN
def main():
#BREAKPOINT ON LINE 11
    movie_recommendations = []
#STEP OVER UNTIL LINE 23 TO TEST FUNCTIONALITY OF MENU OPTION #1
    while True:
        print("Movie Recommendations")
        print("1. Add a movie to the list")
        print("2. Display the movie recommendations added to list")
        print("3. Exit the program")
 #INPUT FROM USER ASSIGNED TO VARIABLE      
        option = input("Enter between options 1-3")

                                #TEST FUNCTIONALITY OF MENU OPTION #1
        
        if option == "1":
            movie = input("Enter a movie to be added to your recommendations")
            movie_recommendations.append(movie)
            print(f"You added {movie}.")
#ELIF STATEMENT TO PROCESS SECOND OPTION IF NOT FIRST OPTION
        elif option == "2":
            #INNER FOR LOOP TO PROCESSS FOR LOOP TO DISPLAY EACH ELEMENT IN THE LIST FROM USER'S INPUT OR DISPLAY MESSAGE AND BREAK
            if movie_recommendations:
                print("Your movie recommendations:")
                for each in movie_recommendations:
                    print(each)        
            else:
                print("You have no recommendations")
                break
#ELIF STATEMENT TO PROCESS THIRD OPTION IF NOT OPTION #1 OR OPTION #2, DISPLAYS MESSAGE, AND BREAKS WHILE LOOP            
        elif option == "3":
            print("You have exited the program. Thank you!")
            break
#ELSE STATEMENT TO PROCESS ALTERNATIVE CONDITIONAL. IF NOT OPTIONS 1-3, USER CHOSE INVALID CHOICE. DISPLAYS MESSAGE, AND RETURNS TO WHILE LOOP        
        else:
            print("You chose an invalid option. pick between 1-3")   
#END MAIN FUNCTION
if __name__ == "__main__":
    main()

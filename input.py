
name = input('What is your name? ')
age = input("How old are you? ")
try:
    age = int(age)
    birth_year = 2023 - age
    print( name, " , you were born in ", birth_year,".", sep = "")
    number = input("give me a number to divide the age")
    number = int(number)
    print(age/number)
except ValueError :
    print("invalid age. please enter a number")
except ZeroDivisionError:
    print("You cannot divide by zero")
else:
    print("No exceptions were raised")
finally:
    print("Thank you for playing")


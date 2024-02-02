name = "Marcos"
age = 19

try:
    birth_year = 2023 - age
    print(name, ", you were born in", birth_year, ".")
    number = input("Give me a number to divide your age: ")
    number = int(number)
    result = age / number
    print("Result of age divided by", number, "is:", result)
except ValueError:
    print("Invalid age. Please enter a number.")
except ZeroDivisionError:
    print("You cannot divide by zero.")
else:
    print("No exceptions were raised.")
finally:
    print("Thank you for playing.")

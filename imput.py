
name = input("What is your name? ")
age = input("How old are you? ")
age = int(age)
current_year = datetime.now().year
birth_year = current_year - age
print(f"{name}, you were born in {birth_year}.")



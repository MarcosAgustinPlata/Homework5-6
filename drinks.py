try:
    name= input( "What is your name?")
    age= input("How old are you")
    age= int(age)
except ValueError :
    print("Invalid age. Please enter a number.")
else:
    if age < 18 :
        print("You are a minor. You can not play the awesome drinking game.")
    else:
        print("You are an adult. You can play the awesome driking game.")
        print("Have some", random.choice(drinks), "and enjoy the game.")
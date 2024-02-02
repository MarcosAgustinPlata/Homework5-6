import random

lives = 3
while lives > 0:
    print("You have", lives, "lives left.")
    dice = random.randint(1, 6)
    print("You rolled a", dice)
    if dice == 6:
        print("You rolled a 6. You win!")
        break
    else:
        lives -= 1

if lives == 0:
    print("You ran out of lives. Game over.")

print("Thank you for playing. Goodbye")






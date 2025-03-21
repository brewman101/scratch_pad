import random

roll=random.randint(1,6)

print("The computer rolled a " + str(roll))

yourRoll=random.randint(1,6)

print("You rolled a "+str(yourRoll))

if roll==yourRoll:
    print("Game Tied")
elif roll<yourRoll:
    print("You win!")
else:
    print("You lose!")
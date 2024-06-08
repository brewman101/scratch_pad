# https://programming-24.mooc.fi/part-2/4-simple-loops

from math import sqrt
# Write your solution here
while True:
    number=float(input("Please type in a number: "))
    if number==0:
        print("Exiting...")
        break
    if number < 0:
        print("Invalid number")
    else:
        print(sqrt(number))


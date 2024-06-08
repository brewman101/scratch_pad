# Source:  https://programming-24.mooc.fi/part-2/4-simple-loops

# Write your solution here
attempts=0
pin=4321
while True:
    pin_test=int(input("PIN: "))
    attempts=attempts+1
    if pin==pin_test and attempts==1:
        print("Correct! It only took you one single attempt!")
        break
    elif pin==pin_test:
        print(f"Correct! It took you {attempts} attempts")
        break
    else:
        print("Wrong")
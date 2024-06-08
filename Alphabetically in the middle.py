# Write your solution here
# https://programming-24.mooc.fi/part-2/3-combining-conditions

letter1=str(input("1st letter: "))
letter2=str(input("2nd letter: "))
letter3=str(input("3rd letter: "))
if letter1<letter2 and letter1>letter3:
    print(f"The letter in the middle is {letter1}")
if letter1<letter3 and letter1>letter2:
    print(f"The letter in the middle is {letter1}")

elif letter2<letter1 and letter2>letter3:
    print(f"The letter in the middle is {letter2}")
elif letter2<letter3 and letter2>letter1:
    print(f"The letter in the middle is {letter2}")
elif letter3<letter2 and letter3>letter1:
    print(f"The letter in the middle is {letter3}")
elif letter3<letter1 and letter3>letter2:
    print(f"The letter in the middle is {letter3}")


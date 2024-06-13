# Source: https://programming-24.mooc.fi/part-3/3-more-loops
total=1
increment=1
#number=3
number=int(input("Please type in a number: "))
while increment <=number:

    while total <= number:
        print(f"{increment} x {total} = {increment * total}")
        total+=1

    increment=increment+1
    total=1



# Source:  https://programming-24.mooc.fi/part-3/1-loops-with-conditions
number=1
limit=int(input("Upper limit: "))
base=int(input("Base: "))
while number<=limit:
    print(number)
    number=number*base

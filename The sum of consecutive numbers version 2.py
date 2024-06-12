# Source:  https://programming-24.mooc.fi/part-3/1-loops-with-conditions

number=1
limit=int(input("Limit: "))
indicator=1
result="The consecutive sum: 1"
while number<limit:
    number=number+(indicator+1)
    result=(f"{result} + {indicator+1}")
    if number<limit:
        indicator=indicator+1
print(f"{result} = {number}")

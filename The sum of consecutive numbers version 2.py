# Source:  https://programming-24.mooc.fi/part-3/1-loops-with-conditions



number=1
limit=int(input("Limit: "))
indicator=1
result="The consecutive sum: "
while number<limit:
    result=(f"{result} + 
    number=number+(indicator+1)
    if number<limit:
        indicator=indicator+1

print(number)
print(result)
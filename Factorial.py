#  Source:  https://programming-24.mooc.fi/part-3/3-more-loops
number=100
result=1
sum=1
while True:
    number=int(input("Please type in a number: "))
    if number<=0:
        break
    else:
        while result<number:
            sum=sum*(sum+1)
            result=result+1
    print(f"The factorial of the number {number} is {sum}")
print("Thanks and bye!")

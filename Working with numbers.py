# Working with numbers

# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
positive=0
negative=0
increment=0
number=1
sum=0
while number!=0:
    number=int(input("Number: "))
    increment=increment+1
    sum=sum+number
    if number>0:
        positive=positive+1
    elif number<0:
        negative=negative+1
mean=(sum/(increment-1))
print("...the program asks for numbers")
print(f"Numbers typed in {increment-1}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")

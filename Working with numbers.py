# Working with numbers

# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
number=666
increment=0
sum=0
while number!=0:
    number=int(input("Number: "))
    increment=increment+1
    sum=sum+number

mean=(sum/(increment-1))
print("...the program asks for numbers")
print(f"Numbers typed in {increment-1}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")


# Write your solution here
string1=str(input("Please type in a string: "))
character1=string1[1]
character2=string1[-2]
if character1==character2:
    print(f"The second and the second to last characters are {character1}")
else:
    print("The second and the second to last characters are different")
# source: https://programming-24.mooc.fi/part-3/2-working-with-strings
# Write your solution here
string1=str(input("Please type in string 1: "))
string2=str(input("Please type in string 2: "))
string1_length=len(string1)
string2_length=len(string2)
if string1_length==string2_length:
    print("The strings are equally long")
elif string1_length>string2_length:
    print(f"{string1} is longer")
elif string2_length>string1_length:
    print(f"{string2} is longer")
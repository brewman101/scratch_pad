# Source: https://programming-24.mooc.fi/part-2/4-simple-loops

# Write your solution here
password=str(input("Password:"))
while True:
    password2=str(input("Repeat password: "))
    if password==password2:
        print("User account created!")
        break
    else:
        print("They do not match!")

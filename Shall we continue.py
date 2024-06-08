# Let's create a program along the lines of the example above. 
# This program should print out the message "hi" and then ask 
# "Shall we continue?" until the user inputs "no". Then the 
# program should print out "okay then" and finish. Please have 
# a look at the example below.

question="yes"
while question!="no":
    print("hi")
    question=str(input("Shall we continue? "))
print("okay then")

# source: https://programming-24.mooc.fi/part-3/2-working-with-strings

string1=str(input("Please type in a string: "))
string1_length=len(string1)
while string1_length>0:
    print(string1[-1])
    string1_length=string1_length-1
    string1=string1[0:-1]
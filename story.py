# Write your solution here
string=""
word2=""
while True:
    word=str(input("Please type in a word: "))
    if (word=="end") or (word==word2):
        break
    else:
        string=string+" "+word
        word2=word
print(string)
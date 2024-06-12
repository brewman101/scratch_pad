# Source:  https://programming-24.mooc.fi/part-3/2-working-with-strings


# Write your solution here
word=str(input("Please type in a word: "))
character=str(input("Please type in a character: "))
index = word.find(character)
length=len(word)
if index==-1:
    print()
elif length-index==1:
    print(word[index])
elif length-index==2:
    print(word[index]+word[index+1])
elif length-index>=3:
    print(word[index]+word[index+1]+word[index+2])


# Source:  https://programming-24.mooc.fi/part-3/2-working-with-strings


# Write your solution here
word=str(input("Please type in a word: "))
character=str(input("Please type in a character: "))
index = word.find(character)
if index==-1:
    print()
else:
    print(word[index]+word[index+1]+word[index+2])
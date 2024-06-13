# 13.6.2024 - I wasn't able to fix this one.
# There is an infinite loop
# Source:  https://programming-24.mooc.fi/part-3/2-working-with-strings

# Write your solution here
word=str(input("Please type in a word: "))
character=str(input("Please type in a character: "))
index = word.find(character)
length=len(word)


while (index+2)<length:
    index = word.find(character)
    print(word[(index):(index+3)])
    word=word[(index+1):]
    length=len(word)


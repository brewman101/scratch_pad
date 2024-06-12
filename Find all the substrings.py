word=str(input("Please type in a word: "))
character=str(input("Please type in a character: "))
index=word.find(character)
while True:
    if len(word)==0:
        break
    word=word[index:index+2]
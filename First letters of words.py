# Source:  https://programming-24.mooc.fi/part-3/3-more-loops


# define the space 
character="z"
# capture the setence
sentence="Humpty Dumpty sat on a wall"
# Print the first letter
print(sentence[0])

# reference the first space
index=sentence.find(character)
while index !=-1:
    print(sentence[(index+1)])
    # trim the sentence
    sentence=sentence[(index+1):]
    # find the next space
    index=sentence.find(character)


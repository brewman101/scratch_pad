# This is looking for a string in the sentence

sentence=input("Give me a sentence: ")
sentence=sentence.lower()
if "cat" in sentence:
    print("You're talking about cats")
else:
    print("You're note talking about cats")
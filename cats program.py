# This is looking for a string in the sentence

sentence=input("Give me a sentence: ")
sentence=sentence.lower()
if "cat" in sentence:
    print("You're talking about cats")
    index_of_cat=sentence.find("cat")
    print(f"It starts at {index_of_cat}")
else:
    print("You're note talking about cats")
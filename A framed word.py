# Write your solution here
word="python"
#word=str(input("Word: "))
space=" "
word2="*"
length=len(word)/2
if length%2==0:
    length=int(14-length)
    print(length)
    print(word2*30)
    print(f"*{space*length}{word}{space*length} *")
    print(word2*30)
else:
    length=int(14-length)
    print(length)
    print(word2*30)
    print(f"*{space*length}{word}{space*length} *")
    print(word2*30)
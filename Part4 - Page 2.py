# Source: https://programming-24.mooc.fi/part-4/2-more-functions

def line(x: int, y: str):
    if y=="":
        print(x * "*")
    else:
        print(x * y)

def box_of_hashes(z):
    b=0
    while b < z:
        line(10,"#")
        b=b+1

box_of_hashes(5)
print()
box_of_hashes(2)

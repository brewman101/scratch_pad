# Source:  https://programming-24.mooc.fi/part-4/2-more-functions
# Noting this hasn't yet been submitted

# define the function
def line(x, y):
    # if string blank print *s instead
    if y=="":
        print(x * "*")
    # else duplicate string
    else:
        print(x * y)

line(4, "")
# Source:  https://programming-24.mooc.fi/part-3/4-defining-functions 

# Write your solution here
def print_many_times(text, x):
    y=0
    while y<x:
        print(text)
        y=y+1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print_many_times("python", 5)

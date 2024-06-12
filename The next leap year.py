# Source:  https://programming-24.mooc.fi/part-2/4-simple-loops
# Part of the solution
inp_year = int(input("Give year:"))
year = inp_year
leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0

if leap:
   print(f"The next leap year from {year} is {year + 4}")

while not leap:
    year += 1
    leap = year % 4 == 0 and year %100 != 0 or year % 100 == 0 and year % 400 ==0
print(f"The next leap year from {inp_year} is {year}")

print("Test")
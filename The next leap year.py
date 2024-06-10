# Source:  https://programming-24.mooc.fi/part-2/4-simple-loops
# Part of the solution
year = int(input("Year:"))
next_leap_year = year + 1
while True:
    if next_leap_year % 4 == 0 and next_leap_year % 100 == 0:
        if next_leap_year % 400 == 0:
            print(f"The next leap year after {year} is {next_leap_year}") 
            break
        else:
            next_leap_year = next_leap_year + 4
            print(f"The next leap year after {year} is {next_leap_year}")
            break
    elif next_leap_year % 4 == 0:
        print(f"The next leap year after {year} is {next_leap_year}")
        break
    else:
        next_leap_year += 1
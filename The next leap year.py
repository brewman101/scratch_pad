# Source:  https://programming-24.mooc.fi/part-2/4-simple-loops
# Part of the solution
year=int(input("Year: "))
if (year%100==0) and (year%400==0):
    print(f"The next leap year after {year} is {year+4}")
elif (year%4==0) and (year%100!=0):
        print(f"The next leap year after {year} is {year+4}")
elif (year%4==3):
    print(f"The next leap year after {year} is {year+1}")
elif (year%4==2):
    print(f"The next leap year after {year} is {year+2}")
elif (year%4==1):
    print(f"The next leap year after {year} is {year+3}")


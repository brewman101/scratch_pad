# This program shows how to pass variables between functions
# I couldn't get it doing the float conversion and sending back to main



def main():
    # pass to function
    dollars = dollars_to_float(input("How much was the meal? "))
    dollars=float(dollars)
    percent = percent_to_float(input("What percentage would you like to tip? "))
    percent=float(percent)
    percent=percent/100
    tip=dollars*percent
    print(f"Leave ${tip:.2f}")




def dollars_to_float(dollars):
    dollars=dollars.lstrip("$")
    # pass it back
    return dollars

def percent_to_float(percent):
    percent=percent.rstrip("%")
    return percent


main()
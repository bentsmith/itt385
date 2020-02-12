amount = int(input("What amount of cents?"))
cents = amount


def printit(units, unit, val):
    if val == 1:
        print(unit, val)
    elif val > 0:
            print(units, val)


# quarters

quarters = cents // 25
remainder = cents % 25
cents = remainder

# dimes

dimes = cents // 10
remainder = cents % 10
cents = remainder

# nickels

nickels = cents // 5
remainder = cents % 5
cents = remainder

# pennies

pennies = cents

# output

printit("Quarters: ", "Quarter: ", quarters)
printit("Dimes: ", "Dime: ",  dimes)
printit("Nickels: ", "Nickel: ", nickels)
printit("Pennies: ", "Penny", pennies)

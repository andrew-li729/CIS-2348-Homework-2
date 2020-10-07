# Andrew Li
# 1824794

def exact_change(user_total):
    user_total = user_total/100
    num_dollars = user_total // 1
    num_cents = (user_total - num_dollars)

    num_quarters = num_cents // 0.25
    num_cents = num_cents - num_quarters*.25

    num_dimes = num_cents // 0.10
    num_cents = num_cents - num_dimes*.10

    num_nickels = num_cents // 0.05
    num_cents = num_cents - num_nickels*0.05

    num_pennies = num_cents // 0.01
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    total = float(input())
    if total <= 0:
        print("no change")
    else:
        # print(exact_change(total))
        numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(total)
        if numdollars != 0 and numdollars > 1:
            print("{:.0f} dollars".format(numdollars))
        elif numdollars == 1:
            print("{:.0f} dollar".format(numdollars))

        if numquarters != 0 and numquarters > 1:
            print("{:.0f} quarters".format(numquarters))
        elif numquarters == 1:
            print("{:.0f} quarter".format(numquarters))

        if numdimes != 0 and numdimes > 1:
            print("{:.0f} dimes".format(numdimes))
        elif numdimes == 1:
            print("{:.0f} dime".format(numdimes))

        if numnickels != 0 and numnickels > 1:
            print("{:.0f} nickels".format(numnickels))
        elif numnickels == 1:
            print("{:.0f} nickel".format(numnickels))

        if numpennies != 0 and numpennies > 1:
            print("{:.0f} pennies".format(numpennies))
        elif numnickels == 1:
            print("{:.0f} penny".format(numpennies))

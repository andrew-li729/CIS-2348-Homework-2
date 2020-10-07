# Andrew Li
# 1824794

def exact_change(user_total):
    total = user_total
    num_dollars = total//100
    total = total - num_dollars * 100
    # print(total)
    num_quarters = total // 25
    total = total - num_quarters * 25
    num_dimes = total // 10
    total = total - num_dimes * 10
    num_nickels = total // 5
    num_pennies = total - num_nickels * 5

    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


if __name__ == '__main__':
    user_val = float(input())
    if user_val <= 0:
        print("no change")
    else:
        # print(exact_change(user_val))
        numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(user_val)
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
        elif numpennies == 1:
            print("{:.0f} penny".format(numpennies))

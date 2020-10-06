# Andrew Li
# 1824794

def exact_change(user_total):
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




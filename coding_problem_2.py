file = open("inputDates.txt", "r")
months_list = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]

# PART A
date_input = []
while True:
    s = input("Enter date:")
    if s == '-1':
        break
    date_input.append(s)

for date in date_input:
    for month in months_list:
        if date.find(month) != -1:
            month_num = months_list.index(month) + 1
            remove_comma = date.replace(",", "")  # replaces comma in date with nothing
            add_slash = remove_comma.replace(" ", "/")  # replaces spaces with "/"
            replace_month = add_slash.replace(month, str(month_num))  # replaces month name with month number
            print(replace_month)
            print("")

# PART B
for line in file:
    for month in months_list:
        if line.find(month) != -1:
            month_num = months_list.index(month) + 1  # counts which month the loop is on
            remove_comma = line.replace(",", "")  # replaces comma in date with nothing
            add_slash = remove_comma.replace(" ", "/")  # replaces spaces with "/"
            replace_month = add_slash.replace(month, str(month_num))  # replaces month name with month number
            print(replace_month)

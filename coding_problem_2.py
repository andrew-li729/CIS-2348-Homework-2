file = open("inputDates.txt", "r")
months_list = ["January", "February", "March", "April", "May", "June", "July",
               "August", "September", "October", "November", "December"]
for line in file:
    for x in months_list:
        if line.find(x) != -1:
            print(line)

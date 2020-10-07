# Andrew Li
# 1824794
import csv
word_list = []
with open("input1.csv", 'r') as file:  # reads csv file and creates words list from row
    reader = csv.reader(file)
    for row in reader:
        words = row

words2 = []


for i in words:
    if i not in words2:  # makes a list of unique words in words list
        words2.append(i)

for i in range(0, len(words2)):  # iterates through new list
    print(words2[i], words.count(words2[i]))  # counts words on 1st word list based on unique word list

# Andrew Li
# 1824794

string_input = input()
no_spaces = string_input.replace(" ", "")
reversed_string = no_spaces[::-1]

if reversed_string == no_spaces:
    print(string_input, "is a palindrome")
else:
    print(string_input, "is not a palindrome")



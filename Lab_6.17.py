# Andrew Li
# 1824794

password = input()
password_key = {"i": "!",
                "a": "@",
                "m": "M",
                "B": "8",
                "o": "."}

for element in password:
    for key in password_key:
        if key == element:
            password = password.replace(element, password_key[key])

print(password + 'q*s')

special = ["!", "@", "#", "$", "&", "*"]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = str(input("Enter password\n"))


def special_char(word):
    z = 0
    if len(word) > 7:
        for i in special:
            if i in word:
                z += 1
                if z >= 2:
                    return True


def numeric_char(word):
    y = 0
    if len(word) > 7:
        for i in number:
            if i in number:
                y += 1
                if y >= 2:
                    return True


while True:
    if numeric_char(password) and special_char(password):
        print("Strong")
        break
    else:
        print("Weak")
        password = str(input("Enter password\n"))
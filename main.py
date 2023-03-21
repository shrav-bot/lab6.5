# Shravya Sama
def encode(password):  # function that changes the password by adding 3
    updated_pass = []
    for i in password:  # each number in the password is separated
        i = int(i)
        i += 3  # each int is added three
        i = str(i)
        updated_pass.append(i)
    final = ''.join(updated_pass)  # joins the list together back into a string
    return final


# pass1 = input()
# print(encode(pass1))


def menu():  # prints out the menu for the main fucntion
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")


# def decode(password):  # function that decodes the password
#     updated_pass = []  # list to store the final password
#     for i in password:  # iterates through each part of string
#         i = int(i)  # changes each to an int
#         i -= 3
#         i = str(i)  # back to string so it can go in list
#         updated_pass.append(i)  # adds to list
#     final = ''.join(updated_pass)
#     return final
#
#
# pass2 = input()
# print(decode(pass2))

if __name__ == "__main__":
    while True:  # while loop for menu so user van keep entering option
        menu()  # prints menu each time
        inp = int(input("Please enter an option:"))
        if inp == 1:
            password1 = input("Please enter your password to encode:")
            stored_pass = encode(password1)
            print("Your password has been encoded and stored!")  # does not print encoded password, just stores it
        elif inp == 2:  # function from partner
            pass
        elif inp == 3:  # quits the entire
            break


def main():


    def get_password():
        password = input("Password Please: ")
        while len(password) < 3:
            print("Too Small")
            password = input("Password Please: ")
        if len(password) > 10:
            print("Too Large")
            password = input("Password Please: ")


password = input("Password Please: ")
while len(password) < 3:
    print("Too Small")
    password = input("Password Please: ")
if len(password) > 10:
    print("Too Large")
    password = input("Password Please: ")
print( '*' * len(password))
print()
main()
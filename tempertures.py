def main():
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def Fahrenheit_to_Celsius():
    global fahrenheit, celsius
    fahrenheit = float(input("Farenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)


def Celsuis_to_Fahrenheit():
    global celsius, fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32


while choice != "Q":
    if choice == "C":
        Celsuis_to_Fahrenheit()
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        Fahrenheit_to_Celsius()
        print("results: {;.2f} C".format(celsius))
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
main()
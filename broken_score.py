def main():
finished = False
result = 0


def Multiply():
    multiply = number1 * number2


while not finished:
    try:
        number1 = int(input("Enter First Number: "))
        if number1 <= 0:
            print("Invalid Try again")
            number1 = int(input("Enter First Number: "))
        number2 = int(input("Enter Second Number: "))
        if number2 <= 0:
            print("Invalid Try again")
            number2 = int(input("Enter Second Number: "))
        Multiply()
        pass
    except:  number1, number2 <= 0:
        print("Please enter a valid integer.")
print("Valid result is:", result)
main()
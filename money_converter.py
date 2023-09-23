print("This program converts currency")

class CurrencyConverter:
    def __init__(self):
        self.rate = 125

    def convert(self, currency_type, amount):
        if currency_type == "E":
            total = amount * self.rate
            print(f"{total} LEK from {amount} EURO")
        elif currency_type == "L":
            total = amount / self.rate
            print(f"{total:.2f} EURO from {amount} LEK")
        else:
            print("Invalid currency type")

converter = CurrencyConverter()

user_input = input("Type 'E' if you have Euro or 'L' if you have Lek: ")

if user_input == "E":
    euro_input = float(input("Enter the amount in Euro: "))
    converter.convert("E", euro_input)
elif user_input == "L":
    leke_input = float(input("Enter the amount in Lek: "))
    converter.convert("L", leke_input)
else:
    print("Invalid input")






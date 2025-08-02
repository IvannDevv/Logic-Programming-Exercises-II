#Currency Converter
name = input("Enter your name: ")

# 1 PEN = 0.27 USD
# 1 PEN = 0.25 EUR

def conversion_and_greeting(name):
    print(f"Welcome, {name}")

    soles_amount = int(input("Enter the amount in soles you want to convert: "))
    print("Which currency do you want to convert to? Enter the number:")
    print("1. EUR")
    print("2. USD")
    eur_or_usd = int(input())

    #CONVERSION
    if eur_or_usd == 1:
        euros = soles_amount * 0.25
        print(f"{soles_amount} soles in euros are: {euros} EUR")
    elif eur_or_usd == 2:
        dollars = soles_amount * 0.27
        print(f"{soles_amount} soles in dollars are: {dollars} USD")
    else:
        print("Invalid option. Please enter 1 or 2. Try again.")

conversion_and_greeting(name)


#RESTAURANT TIP CALCULATOR

total_account = float(input("Enter the customer's total bill: "))

print("What percentage tip would you like to leave? Select the number of your choice:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. I don't want to leave a tip")

user_response = int(input())

def calculate_tip(total_bill):
    if user_response == 1:
        tip = total_bill * 0.10
        tip = round(tip, 2)
        total_with_tip = tip + total_bill
        print(f"The total tip is S/{tip}")
        print(f"The total bill is S/{total_with_tip}")
    elif user_response == 2:
        tip = total_bill * 0.15
        tip = round(tip, 2)
        total_with_tip = tip + total_bill
        print(f"The total tip is S/{tip}")
        print(f"The total bill is S/{total_with_tip}")
    elif user_response == 3:
        tip = total_bill * 0.20
        tip = round(tip, 2)
        total_with_tip = tip + total_bill
        print(f"The total tip is S/{tip}")
        print(f"The total bill is S/{total_with_tip}")
    elif user_response == 4:
        print("Thank you for your visit")
        print(f"The total bill is S/{total_bill}")

calculate_tip(total_account)
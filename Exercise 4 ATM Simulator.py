#ATM SIMULATOR
name = input("Enter your name: ")
initial_balance = float(input("Enter your initial balance: "))

def atm_simulator(name, balance):
    print(f"Welcome, {name}")

    withdrawal = int(input("How much do you want to withdraw: "))

    if withdrawal > balance:
        print("Error, the amount is greater than your balance")
    elif withdrawal <= balance:
        current_balance = balance - withdrawal
        new_balance = current_balance
        print(f"Your current balance is S/{new_balance}")

atm_simulator(name, initial_balance)
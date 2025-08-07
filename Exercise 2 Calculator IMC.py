#CALCULATOR IMC
print("CALCULADORA IMC")
name = input("Enter your name: ")

def imc_calculator(name):
    print(f"Welcome, {name}")

    weight = int(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))
    imc = weight / height**2

    if imc < 18.5:
        print("Underweight")
        print(f"Your BMI is: {imc:.2f}")
    elif 18.5 <= imc <= 24.9:
        print("Normal weight")
        print(f"Your BMI is: {imc:.2f}")
    elif 25 <= imc <= 29.9:
        print("Overweight")
        print(f"Your BMI is: {imc:.2f}")
    else:
        print("Obesity")
        print(f"Your BMI is: {imc:.2f}")

imc_calculator(name)

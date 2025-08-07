#AGE CLASSIFIER

name = input("Enter your name: ")
age = int(input("Enter your age: "))

def age_classifier(name, age):
    print(f"Welcome, {name}")

    # Classifier
    if age < 13:
        print("You are a child")
    elif 13 <= age <= 17:
        print("You are an adolescent")
    elif 18 <= age <= 59:
        print("You are an adult")
    else:
        print("You are a senior adult")

age_classifier(name, age)
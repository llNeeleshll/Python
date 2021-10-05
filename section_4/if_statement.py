name = input("What is your name?")
age = int(input(f"How old are you, {name}"))

if age >= 18:
    print("You can vote")
else:
    print(f"Come back in {18 - age} years")
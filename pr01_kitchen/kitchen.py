"""This program will ask you about drinks."""
print("Welcome to the kitchen.")
name = input("What's your name?")
print(f"Hi there, {name}!")
drink = input("What will you drink?")
if drink == "tea":
    print("Have a nice tea!")
elif drink == "coffee":
    print("Feeling tired?")
else:
    print("We only serve water.")

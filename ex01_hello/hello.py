"""University and index."""
name = input("What's your name?")
study = input("Where do you study?")
if name and study == "":
    print("Name was not inserted!" and "School was not inserted!")
elif name == "":
    print("Name was not inserted!")
elif study == "":
    print("School was not inserted!")
else:
    print(name + ", welcome to " + study)
mass = float(input("Kui palju sa kaalud?(kg)"))
height = float(input("Mis on sinu pikkus?(m)"))
kehamassiindeks = mass / height ** 2
if kehamassiindeks <= 18.5:
    print(f"{kehamassiindeks}, alakaaluline")
elif kehamassiindeks >= 25.0:
    print(f"{kehamassiindeks}, ülekaaluline")
else:
    print(f"{kehamassiindeks}, normaalkaal")

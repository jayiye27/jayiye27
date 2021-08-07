name = input("Name: ")

if len(name) < 3:
    print("Name must be at least 3 characters, thank you.")
elif len(name) >50:
    print("Name must be a maximum of 50 characters, thank you.")
else:
    print("Name looks good! Thank you!")
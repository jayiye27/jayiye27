known_users = ["Alice", "Barbara", "Claire", "Daniel", "Ethan"]

while True:
    print("Hi! My name is CP")
    name = input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("You are on the system. Would you like to be removed from the system (yes/no)?: ").lower()

        if remove == "yes":
            known_users.remove(name)
        elif remove == "no":
            print("No problem, I didn't want you to leave anyway!")

    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        add_me = input("Would you like to be added to the system (yes/no)?: ").strip().lower()
        if add_me == "yes":
            known_users.append(name)
            print("Great! I added you!")
        elif add_me == "no":
            print("No worries, see you around!")
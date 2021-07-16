name = input("What's your name? ")
print("Hello,", name)

ninjas = int(input("How many ninjas are you attacking? "))

if ninjas > 50:
    print("That's too many", name, "!!")
elif ninjas > 20:
    print("Maybe we can take them down", name, ".")
else:
    print("We can take 'em", name, "!", "Let's do this!")



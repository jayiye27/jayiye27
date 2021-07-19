name = input("What's your name? ")
print("Hello,", name)
print("Imagine you are in a video game. Ninjas are your enemies. How many do you want to defeat?")
print("Will the computer agree with your choice? Let's see!")

ninjas = int(input("How many ninjas are you attacking? "))

if ninjas > 50:
    print("That's too many ninjas", name, "!!")
elif ninjas > 20:
    print("Maybe we can take them down", name, ".")
else:
    print("We can take 'em", name, "!", "Let's do this!")



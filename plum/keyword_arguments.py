def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}!')
    print('Welcome aboard')

#positional arguments
print("Start")
greet_user("Smith", "John")
print("Finish")


print("Start")
greet_user("Smith", last_name="John")
print("Finish")

#keyword arguments
print("Start")
greet_user(last_name="Smith", first_name="John")
print("Finish")


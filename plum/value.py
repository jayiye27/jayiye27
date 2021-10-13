import random

for i in range(3):
    print(random.random())

print("---------------")

for i in range(3):
    print(random.randint(10, 20))

print("---------------")


members = ['John', 'Mary', 'Bob', 'Mosh']
leader = random.choice(members)
print(leader)
print("---------------")

names = ['John', 'Bob', 'Mosh','Sarah', 'Mary']
print(names[2:])
print(names)

print("-----------------")

numbers = [3, 6, 2, 8, 4, 10, 90.5, 1000, 1/2]

max = numbers[0]
min = numbers[2]

for number in numbers:
    if number > max:
        max = number
print(f"Max: {max}")

for number in numbers:
    if number < min:
        min = number

print(f"Min: {min}")

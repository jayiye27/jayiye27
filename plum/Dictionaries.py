customer = {
    "name": 'John Smith',
    "age": 30,
    "is_verified": True
}

customer["name"] = "Jack Smith"

print(customer["name"])
print(customer.get("Name"))

#print(customer["birthdate"])
print(customer.get("birthdate", "Jan 1 1980"))

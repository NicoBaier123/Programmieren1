my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("Name:", my_dict["name"])
print("Age:", my_dict["age"])
print("City:", my_dict["city"])

def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]

doubled_numbers = list(map(double, numbers))

print(doubled_numbers)

# Dictionary
# Dictionaries in Python are collections of key-value pairs. Each key in a dictionary is unique and maps to a value.
# Dictionaries are mutable, meaning they can be modified after they are created.
# Dictionaries are unordered, meaning the order of the key-value pairs is not preserved.
# Dictionaries are defined using curly braces {} and key-value pairs are separated by commas.

# Initial dictionary
person = {
    "name": "Arun",
    "age": 35,
    "city": "Mumbai",
    "email": "arun@example.com"
}

# Accessing values
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Email:", person["email"])

# Modifying values
person["age"] = 40
person["email"] = "arun_updated@example.com"

# Printing the updated dictionary
print("\nAfter modification:")
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
print("Email:", person["email"])

# Methods
# 1. dict.get()
# Using get method
print(person.get("name"))
print(person.get("phone", "Not Available"))

# 2. dict.keys()
# Using keys method
print(person.keys())

# 3. dict.values()
# Using values method
print(person.values())

# 4. dict.items()
# Using items method
print(person.items())

# 5. dict.update()
# Update example
additional_info = {
    "phone": "123-456-7890",
    "occupation": "Engineer"
}
person.update(additional_info)
print(person)

# 6. dict.pop()
# Using pop method
removed_value = person.pop("occupation")
print(removed_value)
print(person)

# 7. dict.popitem()
# Using popitem method
last_item = person.popitem()
print(last_item)
print(person)

# 8. dict.clear()
# Using clear method
person.clear()
print(person)

# Functions
# 1. len(dictionary)
print(len(person))

# 2. key in dictionary
print("age" in person)
print("email" in person)

# 3. dictionary.copy()
person_copy = person.copy()

# 4. dictionary.get(key, default=None)
print(person.get("age"))
print(person.get("email", "Not Available"))

# 5. dictionary.items()
print(person.items())

# 6. dictionary.keys()
print(person.keys())

# 7. dictionary.values()
print(person.values())
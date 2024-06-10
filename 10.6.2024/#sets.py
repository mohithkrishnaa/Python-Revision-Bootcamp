#sets
#Sets in Python are unordered collections of unique elements. They are defined using curly braces {} or the set() function. 
# Sets are useful for storing elements without duplicates and for performing set operations like union, intersection, and difference.

# Creating a set of cars
cars = {"Toyota", "Honda", "Ford"}
print(cars)

# Adding multiple elements
cars.update(["Chevrolet", "Kia"])
print(cars)

# Removing an element using remove() (raises KeyError if element is not found)
cars.remove("Honda")
print(cars)

# Removing an element using discard() (does not raise an error if element is not found)
cars.discard("Toyota")
print(cars)

# Clearing all elements
cars.clear()
print(cars)

#Set Operations
# Creating two sets of cars
sedans = {"Toyota Camry", "Honda Accord", "Ford Fusion"}
suvs = {"Ford Explorer", "Honda CR-V", "Toyota Highlander"}

# Union
union_set = sedans.union(suvs)
print("Union:", union_set)

# Intersection
intersection_set = sedans.intersection(suvs)
print("Intersection:", intersection_set)

# Difference
difference_set = sedans.difference(suvs)
print("Difference:", difference_set)

# Symmetric Difference
symmetric_difference_set = sedans.symmetric_difference(suvs)
print("Symmetric Difference:", symmetric_difference_set)
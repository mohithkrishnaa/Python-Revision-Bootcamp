#Tuples
#Tuples are immutable sequences in Python, meaning their elements cannot be changed once they are created.
#Tuples are defined by enclosing elements in parentheses (()) and elements are separated by commas.
#Tuples are similar to lists, but they are immutable.
#Tuples are faster than lists because they cannot be changed.
#Tuples are used when you want to ensure that the data does not change.
#Example:

# Define tuples 
fruits = ("apple", "banana", "cherry")
vegetables = ("carrot", "broccoli", "spinach")
proteins = ("chicken", "paneer", "fish")

# Accessing elements in the tuple
print("Fruits:")
for fruit in fruits:
    print(fruit)

print("\nVegetables:")
for vegetable in vegetables:
    print(vegetable)

print("\nProteins:")
for protein in proteins:
    print(protein)

# Combining tuples
all_foods = fruits + vegetables + proteins
print("\nAll Foods:")
for food in all_foods:
    print(food)

# Accessing a specific element
print("\nThe first fruit is:", fruits[0]) 
print("The last vegetable is:", vegetables[-1])

# Slicing tuples
print(fruits[1:3])  
print(vegetables[:2]) 
print(proteins[1:])  

# Concatenating tuples
all_foods = fruits + vegetables + proteins
print(all_foods)

# Repeating tuples
repeated_fruits = fruits * 2
print(repeated_fruits)

# Iterating through a tuple
for fruit in fruits:
    print(fruit)

# Getting the length of a tuple
print(len(fruits))  
print(len(all_foods))  

# Nesting tuples
nested_tuple = (fruits, vegetables, proteins)
print(nested_tuple)

# Accessing elements in nested tuples
print(nested_tuple[0][1]) 
print(nested_tuple[2][2])  

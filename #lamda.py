#lamda 
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Using map with a lambda function to square each number
squared_numbers = list(map(lambda x: x * x, numbers))

print(squared_numbers) 

# List of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Using filter with a lambda function to get only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  
#functions
#function without arguement
def greet():
    print("Hello, World!")

greet()

#functions with arguements
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")

#function with return value
def add(a, b):
    return a + b

result = add(3, 4)
print(result)

#funtcions with default values of arguements
def greet(name="World"):
    print(f"Hello, {name}!")

greet()         
greet("Alice")
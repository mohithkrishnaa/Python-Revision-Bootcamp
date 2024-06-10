#lists
#Python Lists is the fundamental data structure that allows you to store a collection of items in a specific order and are just like dynamically sized arrays.
#Lists are defined by placing all the items (elements) inside square brackets [], separated by commas.
#It is a collection which is ordered and changeable. Allows duplicate members.
#Lists are used to store a collection of data, and you can manipulate them by using various methods
#Lists are mutable, meaning that they can be modified after they are created.
#Lists are defined by placing all the items (elements) inside square brackets [], separated by commas.
#Example :
my_list = ["chicken", "paneer", "fish"]
print(my_list)

#Accessing Items :
#You can access the items of a list by referring to the index number.
#Example :
my_list = ["chicken", "paneer", "fish"]
print(my_list[0])
print(my_list[1]) 
print(my_list[2]) 

#Append
#The append method adds an element to the end of the list.
# Initial list of dishes
my_list = ["chicken", "paneer", "fish"]
print(my_list)  

#Insert
#The insert method inserts an element at a specified position.
my_list.insert(1, "tofu")
print(my_list) 

#Remove
#The remove method removes the first occurrence of a specified value.
my_list.remove("paneer")
print(my_list) 

#Copy
#The copy method returns a shallow copy of the list.
my_list_copy = my_list.copy()
print(my_list_copy)  

#Count
#The count method returns the number of occurrences of a specified value.
count_fish = my_list.count("fish")
print(count_fish) 

#Extend
#The extend method extends the list by appending elements from another list.
more_items = ["pasta", "salad"]
my_list.extend(more_items)
print(my_list)  

#Index
#The index method returns the index of the first occurrence of a specified value.
index_fish = my_list.index("fish")
print(index_fish)  

#Sort
#The sort method sorts the list in ascending order by default.
my_list.sort()
print(my_list)  

#reverse
#The reverse method reverses the order of the list.
my_list.reverse()
print(my_list)  

#Clear
#The clear method removes all items from the list.
my_list.clear()
print(my_list)  

#Pop
#The pop method removes and returns the element at a specified position.
my_list = ["chicken", "paneer", "fish"]

# Pop the last element
last_item = my_list.pop()
print(last_item)  
print(my_list)    

# Pop the element at index 0
first_item = my_list.pop(0)
print(first_item)  
print(my_list)     
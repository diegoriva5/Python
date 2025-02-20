# base_dictionary.py

# Create a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}

# Accessing items
print("Name:", my_dict['name'])
print("Age:", my_dict['age'])

# Adding an item
my_dict['email'] = 'john@example.com'
print("Updated dictionary:", my_dict)

# Removing an item
my_dict.pop('age')
print("Dictionary after removing age:", my_dict)

# Loop through dictionary keys
print("Keys in dictionary:")
for key in my_dict:
    print(key)

# Loop through dictionary values
print("Values in dictionary:")
for value in my_dict.values():
    print(value)

# Loop through dictionary items
print("Items in dictionary:")
for key, value in my_dict.items():
    print(key, ":", value)

# Check if a key exists
if 'name' in my_dict:
    print("Name is a key in the dictionary")

# Get the length of the dictionary
print("Length of dictionary:", len(my_dict))

# Clear the dictionary
my_dict.clear()
print("Dictionary after clearing:", my_dict)
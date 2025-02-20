# strings_operations.py

# Concatenation
str1 = "Hello"
str2 = "World"
concatenated = str1 + " " + str2
print("Concatenated String:", concatenated)

# Repetition
repeated = str1 * 3
print("Repeated String:", repeated)

# Slicing
sliced = concatenated[0:5]
print("Sliced String:", sliced)

# Length
length = len(concatenated)
print("Length of String:", length)

# Upper and Lower Case
upper_case = concatenated.upper()
lower_case = concatenated.lower()
print("Upper Case:", upper_case)
print("Lower Case:", lower_case)

# Strip
str_with_spaces = "   Hello World   "
stripped = str_with_spaces.strip()
print("Stripped String:", stripped)

# Replace
replaced = concatenated.replace("World", "Python")
print("Replaced String:", replaced)

# Split
split_str = concatenated.split()
print("Split String:", split_str)

# Join
joined_str = "-".join(split_str)
print("Joined String:", joined_str)

# Find
index = concatenated.find("World")
print("Index of 'World':", index)

# Check if string starts with a specific substring
starts_with = concatenated.startswith("Hello")
print("Starts with 'Hello':", starts_with)

# Check if string ends with a specific substring
ends_with = concatenated.endswith("World")
print("Ends with 'World':", ends_with)
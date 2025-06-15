# String methods
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# String length
length = len(c)
print(length)
# String indexing
first_char = c[0]
last_char = c[-1]
print(first_char)
print(last_char)

# String slicing
first_3_chars = c[:3] # Another way is [0:3]
last_3_chars = c[-3:] # Another way is [-3:len(c)]
print(first_3_chars)
print(last_3_chars)

# String methods
uppercase = c.upper()
lowercase = c.lower()
title_case = c.title()
print(uppercase)
print(lowercase)
print(title_case)

# String replacement
# String replace takes a string and replaces it with another string
replaced = c.replace("Hello", "Hi")
print(replaced)

# String concatenation
concatenated = a + " " + b
print(concatenated)

# String splitting
# String split takes a string and splits it into a list of strings
split_words = c.split(" ")
print(split_words)

# String joining
# String join takes a list of strings to a single string
joined = " ".join(split_words)
print(joined)

print("Hello" in c)  # Check if a substring is present
print("Python" not in c)  # Check if a substring is not present

# String formatting
name = "Ali"
age = 23
formatted_string = f"My name is {name} and I am {age} years old." # Using f-string for formatting
print(formatted_string)

# String comparison
# String comparison is done lexicographically based on ASCII values of characters
str1 = "apple"
str2 = "banana"
print(str1 < str2)  # Lexicographical comparison
print(str1 > str2)  # Lexicographical comparison
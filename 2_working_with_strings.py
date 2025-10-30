
# ----------------------------------------
# . Working with Strings
# ----------------------------------------

# Strings are sequences of characters enclosed in quotes (' ' or " ")
greeting = "Hello" #sring data types
name = "World" #string data types

# ----------------------------------------
# Basic String Operations
# ----------------------------------------

# 1. Concatenation: Combining strings using the + operator
message = greeting + " " + name
print("Concatenated String:", message)  # Output: Hello World

# ----------------------------------------
# 2. String Functions
# ----------------------------------------

phrase = "Python is FUN!"
name = "Olivia"
phrase2 = "SUPERCAGEFRAGILISTICIOUS"
# # Convert all characters to lowercase
print("Lowercase:", phrase.lower())  # Output: python is fun!
print("Name Lowercase:", name.lower())
print("phrase2 Lowercase:", phrase2.lower())

# # Convert all characters to uppercase
print("Uppercase:", phrase.upper())  # Output: PYTHON IS FUN!
print("Name Uppercase:", name.upper())

# # Check if all characters are uppercase
print("Is Uppercase?", phrase.isupper())  # Output: False
print("Is Name Uppercase?", name.isupper())
print ("Is Phrase2 Uppercase?", phrase2.isupper())
# # Find the length of the string
# print("Length of phrase:", len(phrase))  # Output: 14

declaration_of_independence = "When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and Nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation"
print(len(declaration_of_independence))
# # ----------------------------------------
# # 3. Indexing and Slicing
# # ----------------------------------------

chicago_mayor = "Johnson"
#index slicing
print(chicago_mayor[0])
#get the last letter
print(chicago_mayor[-1])
#get the 's' in the string
print(chicago_mayor[4])
#slicing
#get the "son" form the string
print(chicago_mayor[ 4 : ]) #blank is to the end of it
#the first number in slicing is inclusing
#the second number is exclusive
# get the string "John"
print(chicago_mayor[0: 4])
print(chicago_mayor[0: -3])
# get "ohns"
print(chicago_mayor[1:5])
#when we get one character/letter
#its called string indexing
#when we get a chunk of letters
#from a string, its called
# string slicing

# git add .
# git commit -m "string slicing"
# git push origin

phrase3 = "Supercagifragilstic"
#uppercase it
print("Uppercase:", phrase3.upper())
#slice super out of it into a different variable
cut = phrase3[0:5]
print(cut)

# # Indexing: Access characters by position (0-based index)
# print("First character:", phrase[0])  # Output: P
# print("Last character:", phrase[-1])  # Output: !

# # Slicing: Get a range of characters (start inclusive, end exclusive)
# print("Characters 1 to 4:", phrase[1:4])  # Output: yth

# # Example combining everything:
# print("Formatted Example:", (greeting + " " + name + "!").upper())
# # Output: HELLO WORLD!


# # ----------------------------------------
# # 7. Strings: Advanced Concepts
# # ----------------------------------------

# # Creating Strings: use single or double quotes
# greeting1 = 'Hello'
# greeting2 = "Hi there"

# # Printing Strings
# print(greeting1)
# print(greeting2)

# # ----------------------------------------
# # String Methods
# # ----------------------------------------

sentence = "Python is fun to learn"

# # .split(): Splits the string into a list of words
words = sentence.split()
print("Split result:", words)
words2 = sentence.join("")
print(words2)

# # .format(): Allows inserting values into strings using {}
# name = "Marvin"
# age = 35
# intro = "My name is {} and I am {} years old.".format(name, age)
# print(intro)

# # You can also use f-strings (Python 3.6+)
# intro_fstring = f"My name is {name} and I am {age} years old."
# print(intro_fstring)

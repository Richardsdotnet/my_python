print("Your task is to get the total number of characters in a name")
# print(f"The total is {len(input('What is your name? '))}")
# print(f"Your name has a total of {len(input('What is your name?'))} characters!")

print("Welcome to python variables")
name = input("What is your name?\n")
length = len(name)
whiteSpace = name.count(" ")
print(f"The total characters are {length - whiteSpace}")
a = input("a:")
b = input("b:")
c = a
a = b
b = c
print("a = " + a)
print("b = " + b)

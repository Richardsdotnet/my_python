# print("Your task is to get the total number of characters in a name")
# print(f"The total is {len(input('What is your name? '))}")
# print(f"Your name has a total of {len(input('What is your name?'))} characters!")

# print("Welcome to python variables")
# name = input("What is your name?\n")
# length = len(name)
# whiteSpace = name.count(" ")
# print(f"The total characters are {length - whiteSpace}")
# a = input("a:")
# b = input("b:")
# c = a
# a = b
# b = c
# print("a = " + a)
# print("b = " + b)
# print("Welcome to the band name generator")
# name = input("Enter Your Name\n")
# print("HELLO! " + name)
# print("Enter the name of your CITY")
# city = input("City name\n ")
# print("Enter the name of your PET")
# pet = input("Pet name\n ")
# print("The name of your band is  " + city + " " + pet)

# print("Welcome, input two numbers")
# two_digit_number = input("Type a two digit number\n")
# first_num = int(two_digit_number[0])
# second_num = int(two_digit_number[1])
# result = int(first_num + second_num)
# print(f"The sum of the two digits is {result}")

print("Welcome to the weeks calculator")
age = input("Welcome, What is your current Age? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days = years_remaining * 365
weeks = years_remaining * 52
months = years_remaining * 12
print(f"Your have {days} days {weeks} weeks and {months} months left")

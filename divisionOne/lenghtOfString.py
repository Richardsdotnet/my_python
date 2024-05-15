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
# two_digit_number = input("Type a two-digit number\n")
# first_num = int(two_digit_number[0])
# second_num = int(two_digit_number[1])
# result = int(first_num + second_num)
# print(f"The sum of the two digits is {result}")

# age = input("Welcome to Days, weeks and months calculator, What is your current Age?\n ")
# age_as_int = int(age)
# years_remaining = 90 - age_as_int
# days = years_remaining * 365
# weeks = years_remaining * 52
# months = years_remaining * 12
# print(f"Your have {days} days {weeks} weeks and {months} months left")

print("Welcome to the tip calculator")
bill = int(input("What was the total bill?\n"))
tip_as_percent = int(input("What percentage tip would you want to give? 10, 12 or 15?\n"))
number_of_friends = int(input("How many people to split the bill?\n"))
tip_as_percent = tip_as_percent / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / number_of_friends
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")

print("Welcome to the rollercoaster game ")
height = int(input("Enter your height\n"))
if height >= 50:
    print("Have fun riding!!")
else:
    print("You need to grow older to ride")

print("Welcome to the odd and even number game")
number_to_check = int(input("Enter the number to check\n"))
if number_to_check % 2 == 0:
    print(f"{number_to_check} is an even number")
else:
    print(f"{number_to_check} is an odd number")




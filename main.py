# basic user input
# rental_car = input("what car would you like to rent today?")
# print(f"\nLet me see if i can find you a {rental_car.title()}")

# restaurant_seating = input("How may people is in your dinner group?")
# restaurant_seating = int(restaurant_seating)
#
# if restaurant_seating > 8:
#     print(f"\nYou will have to wait a short while for a table of {restaurant_seating}")
# else:
#     print(f"\nYou table of {restaurant_seating} is ready")
#

# # multiple of 10
# num = input("Enter a number to check if its is a multiple of ten: ")
# num = int(num)
#
# if num % 10 == 0:
#     print(f"The number {num} is a multiple of 10")
# else:
#     print(f"The number {num} is not a multiple of 10")

# while loops
# prompt = "\nPlease enter a pizza topping"
# prompt += "\n(enter 'quit' when you are finished,) "
# while True:
#     topping = input(prompt)
#
#     if topping == 'quit':
#         break
#     else:
#         print(f"I will add {topping.title()} on your pizza")

# prompt = "\nPlease enter a your age"
# prompt += "\n(enter '0' when you are finished,) "
# active = True
# while active:
#     age = input(prompt)
#     age = int(age)
#     if age == 0:
#         active = False
#     elif age == 'quit':
#         break
#     elif age < 3:
#         print("The ticket is free")
#     elif age <= 12:
#         print("The ticket is $10")
#     else:
#         print("The ticket is $15")

# using while loop with list
# sandwich_orders = ['ham sandwich', 'bacon sandwich', 'salime sandwich', 'pastrami sandwich',
#                    'pastrami sandwich', 'pastrami sandwich']
#
# finished_sandwiches = []
# print("the deli has run out of pastrami")
#
# while 'pastrami sandwich' in sandwich_orders:
#     sandwich_orders.remove('pastrami sandwich')
# print(sandwich_orders)
#
# while sandwich_orders:
#     sandwich = sandwich_orders.pop()
#     print(f"I made your {sandwich.title()}")
#     finished_sandwiches.append(sandwich)
#
# print("\nList of finished sandwich")
# for sand in finished_sandwiches:
#     print(f"{sand.title()}")
#
# Filling up a dictionary using user input and while loops
# responses = {}
# active = True
#
# while active:
#     name = input("What is your name")
#     dream_vacation = input("If you can visit one place in the world where would you go?")
#     responses[name] = dream_vacation
#     repeat = input("Would you like to pass this poll to someone else (yes or no)?")
#     if repeat == 'no':
#         active = False
# print("-----Result of poll-----")
# for names, place in responses.items():
#     print(f"{names.title()} would like to go to {place.title()}")

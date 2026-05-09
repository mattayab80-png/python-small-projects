# # ce code a pour but de creer le factoriel
# n = int(input("Enter le nombre: "))
# if n < 0:
#     print("Le factoriel des nombres < 0 n'existe pas.")
# else:
#     factoriel = 1
#     for i in range(1, n+1):
#         factoriel *= i
#
#     print(f"Le factoriel de {n} est : {factoriel}")

import random

#Ici apprenons les dictionnaires


# import random
#
# cards = ["3","4","G","r","5","4","D","9"]
#
# random.shuffle(cards)
#
# # print(cards)
#
# low = 1
# high = 30
#
# guess = random.randint(low,high)
# #
# # while True:
# #     users_guess = int(input(f"Pick a number between ( {low} - {high} ): "))
# #     print(guess)
# #     if users_guess < guess:
# #         print("It's too small")
# #     elif users_guess > guess:
# #         print("It's too high")
# #     else:
# #         print(f"Your guess is correct: {guess}")
# #         break
#
# import random
# import string
#
#
# chars = " "+ string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()
#
# random.shuffle(key)
#
# print(f"chars: {chars}")
# print(f"key: {key}")
#
#
# #ENCRYPT
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""
# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]
#
# #print(f"Original message: {plain_text}")
# print(f"Encrypted message: {cipher_text}")
#
# #DECRYPT
#
# cipher_text = input("Enter a message to encrypt: ")
# plain_text= ""
# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]
#
# #print(f"Original message: {plain_text}")
# print(f"Encrypted message: {plain_text}")
#
#
# def happy_birthday(name, age):
#     print(f" Happy birthday to {name} \n Happy birhtday to {name} \n Happy birhtday to you my son \n Happy birthday to you! You are {age} ")
#
#
# happy_birthday("SAM", 20)

#  # Login form
# array = []
# user_name = input("Entrer votre nom d'utilisateur:")
# password = input("Entrer votre mot de passe: ")
# array.append([user_name, password])
# print(f"Your username and password have been saved successfully!!!")
#
# username2 = input("Entrer votre nom d'utilisateur: ")
# password2 = input("Entrer votre mot de passe: ")
#
# if username2 != user_name or password2 != password :
#     print("Your password or username is incorrect!!!")
# else:
#     print("Welcome again sir!!!")

#
#
# first_num = float(input("Enter a 1st num: "))
# second_num = float(input("Enter a 2nd num: "))
# operator = str(input("Enter an operator: ")).strip()
#
# if operator == "+":
#     result = first_num + second_num
#     print(result)
# elif operator == "-":
#     result = first_num - second_num
#     print(result)
# elif operator == "*":
#     result = first_num * second_num
#     print(result)
# elif operator == "/":
#     result = first_num / second_num
#     print(result)
# else:
#     print(f"Invalid operator : {operator}")
#
# continu = str(input("Do you want to begin: ")).strip().lower()
# while continu == "yes":
#     first_num = float(input("Enter a 1st num: "))
#     second_num = float(input("Enter a 2nd num: "))
#     operator = str(input("Enter an operator: ")).strip()
#
#     if operator == "+":
#         result = first_num + second_num
#         print(result)
#     elif operator == "-":
#         result = first_num - second_num
#         print(result)
#     elif operator == "*":
#         result = first_num * second_num
#         print(result)
#     elif operator == "/":
#         result = first_num / second_num
#         print(result)
#     else:
#         print(f"Invalid operator : {operator}")
#
#     continu = str(input("Do you want to restart: ")).strip().lower()
#     if continu != "yes":
# #         break
# #
#
# import math
# import random
#
# print("Guess a number between 1 and 10(included)")
# choosen_num = random.randint(1,11)
# print(choosen_num)
# guess = int(input("Enter your number: "))
#
#
# while guess != choosen_num or guess == choosen_num:
#         if guess > choosen_num:
#             print("too big")
#             guess = int(input("Enter your number: "))
#         elif guess < choosen_num:
#             print("too small")
#             guess = int(input("Enter your number: "))
#         elif guess == choosen_num:
#             print(f"Yeah it's : {choosen_num}")
#             break
# #
# #
#
#
# print("-----Welcome to our Unit converter")
# unit = ["C","F","K"]
# while unit in ["C","F","K"] or unit not in ["C","F","K"]:
#     permission = str(input("Do you want to continue: ")).strip().lower()
#     unit = str(input("Enter a unit(\u00B0C, \u00B0K, \u00B0F): ")).strip().capitalize()
#     if permission == "yes":
#             if unit == "C":
#                 num = float(input("Enter a degree: "))
#                 toK = round(num + 273.15, 2)
#                 toF = round(num *(9/5) + 32, 2)
#                 print(f"Your results are: \n {toK}\u00B0K \n {toF}\u00B0F")
#             elif unit == "K":
#                 num = float(input("Enter a degree: "))
#                 toC = round(num - 273.15, 2)
#                 toF = round((num - 273.15) * (9 / 5) + 32, 2)
#                 print(f"Your results are: \n {toC}\u00B0C \n {toF}\u00B0F")
#             elif unit == "F":
#                 num = float(input("Enter a degree: "))
#                 toK = round((5/9) * (num - 32) + 273.15, 2)
#                 toC = round((num - 32) * (9 / 5), 2)
#                 print(f"Your results are: \n {toC}\u00B0K \n {toK}\u00B0F")
#             else:
#                 print("You've entered an unvalid unit")
#
#     else:
#         print("Goodbye!!!")
#         break
#

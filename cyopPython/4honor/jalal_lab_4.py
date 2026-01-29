'''Docstring for jalal_lab_4'''
import re

def phone_number():
    phone_input = input('Enter in your phone number with no dashes or parentheses: ')
    result = phone_input.isnumeric()
    # if phone_input
    while True:
        if result == True: 
            areacode = phone_input[0:3]
            middle_number = phone_input[3:6]
            last_four = phone_input[-4:]
            formatted_number = (f'{areacode}-{middle_number}-{last_four}')
            print(formatted_number)
            break
        if result == False:
            print('Your number was incorrect, would you like to try again?')
phone_number()
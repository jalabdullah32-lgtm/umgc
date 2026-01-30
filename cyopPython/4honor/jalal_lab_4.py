'''Docstring for jalal_lab_4'''
import re
import numpy as np

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
# phone_number()
#zipcode will be similar to above

def matrix():
    print('Example input: 1,2,3')
    matrix1_column1 = float(input('Please enter the first column of your matrix: '))
    matrix2_column2 = float(input('Please enter the second column of your matrix: '))
    matrix3_column3 = float(input('Please enter the third column of your matrix: '))



    random = np.array([[matrix1_column1],[matrix2_column2],[matrix3_column3]])    
    print(random)
matrix()

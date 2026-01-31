'''Docstring for jalal_lab_4'''
# import re
import sys
import numpy as np

def value_error():
    '''input validation function'''
    print('')
    print('One or more of your inputs is invalid. Would you like to try again?')
    print('Enter yes or no: ')
    continue_program = input()
    i = continue_program.upper()

    if i == 'YES':
        print('')
        return True

    if i == 'NO':
        print('')
        exit_program()
        return None


    print('')
    print('I am not sure what you mean, restarting program')
    return True

def exit_program():
    """exits program"""

    print("You have exited the program, thank you.")
    sys.exit()

def phone_number():
    '''user enters phonenumber and it is validated'''

    phone_input = input('Enter in your phone number with no dashes or parentheses: ')
    result = phone_input.isnumeric()
    # if phone_input
    while True:
        if result == True:
            areacode = phone_input[0:3]
            middle_number = phone_input[3:6]
            last_four = phone_input[-4:]
            formatted_number = f'{areacode}-{middle_number}-{last_four}'
            print(formatted_number)
            break
        if result == False:
            print('Your number was incorrect, would you like to try again?')
# phone_number()
#zipcode will be similar to above

def matrix_row_one():
    '''Docstring for jalal_lab_4'''

    while True:
        try:
            sample_row = np.array([0.0,0.0,0.0])
            print('This is the first row, of the first matrix')
            print('--------------------------------------------')

            def row_one():
                print(f'Your first row currently looks like {sample_row}')
                value_one = float(input('Please enter your first matrix value: '))
                sample_row[0] = value_one
                print(sample_row)

                value_two = float(input('\nPlease enter your second matrix value: '))
                sample_row[1] = value_two
                print(sample_row)

                value_three = float(input('\nPlease enter your third matrix value: '))
                sample_row[2] = value_three
                print(sample_row)

                global row_one_matrix
                row_one_matrix = sample_row

                #functionality that allows user to edit specific index? For now none.
                print("")
                print(f'Thank you, the first row of your matrix is {sample_row} ')
                # print(f'the first row of your matrix is: \n{row_one_matrix} '
                #         '\nAre there any values you would like to change?')
            row_one()
            break
        except ValueError:
            value_error()
def matrix_row_two():
    '''Docstring for jalal_lab_4'''

    while True:
        try:
            sample_row = np.array([0.0,0.0,0.0])
            print('\nThis is the second row, of the first matrix')
            print('--------------------------------------------')

            def row_two():
                print(f'Your first row currently looks like {sample_row}')
                value_one = float(input('\nPlease enter your first matrix value: '))
                sample_row[0] = value_one
                print(sample_row)

                value_two = float(input('\nPlease enter your second matrix value: '))
                sample_row[1] = value_two
                print(sample_row)

                value_three = float(input('\nPlease enter your third matrix value: '))
                sample_row[2] = value_three
                print(sample_row)

                global row_two_matrix
                row_two_matrix = sample_row

                #functionality that allows user to edit specific index? For now none.
                print("")
                print(f'Thank you, the second row of your matrix is {sample_row} ')

                # print(f'the second row of your matrix is: \n{sample_row} '
                #         '\nAre there any values you would like to change?')
            row_two()
            break
        except ValueError:
            value_error()
def matrix_row_three():
    '''Docstring for jalal_lab_4'''

    while True:
        try:
            sample_row = np.array([0.0,0.0,0.0])
            print('\nThis is the third and final row of the first matrix')
            print('--------------------------------------------')

            def row_three():
                print(f'Your first row currently looks like {sample_row}')
                value_one = float(input('Please enter your first matrix value: '))
                sample_row[0] = value_one
                print(sample_row)

                value_two = float(input('Please enter your second matrix value: '))
                sample_row[1] = value_two
                print(sample_row)

                value_three = float(input('Please enter your third matrix value: '))
                sample_row[2] = value_three
                print(sample_row)

                global row_three_matrix
                row_three_matrix = sample_row

                #functionality that allows user to edit specific index? For now none.
                print("")
                print(f'Thank you, the third row of your matrix is {sample_row} ')

                # print(f'the first third of your matrix is: \n{sample_row} '
                #         '\nAre there any values you would like to change?')
            row_three()
            break
        except ValueError:
            value_error()

def create_matrix_one():
    '''grabs matrix'''
    print('')
def run_matrix():
    '''grabs matrix'''
    matrix_row_one()
    matrix_row_two()
    matrix_row_three()
    matrix_one = np.array([row_one_matrix,row_two_matrix,row_three_matrix])

    print('--------------------------------------------')
    print(f'\n Matrix one = \n{matrix_one}')
run_matrix()

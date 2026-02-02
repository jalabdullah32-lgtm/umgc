'''Docstring for jalal_lab_4'''
# import re
import sys
import numpy as np

matrix_one = np.array([[1.,2.,3.],[4.,5.,6.],[7.,8.,9.]])
matrix_two = np.array([[13.7,11.4,2.1],[5.3,14.6,43.8],[10.5,9.3,5.1]])
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

    print("\nYou have exited the program, thank you.")
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
            print('----------------------------------------------')

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

                print("")
                print(f'The first row of your matrix is {sample_row} ')
            row_one()
            break
        except ValueError:
            value_error()
def matrix_row_two():
    '''Docstring for jalal_lab_4'''

    while True:
        try:
            sample_row = np.array([0.0,0.0,0.0])
            print('----------------------------------------------')

            def row_two():
                print(f'Your second row currently looks like {sample_row}')

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


                print("")
                print(f'The second row of your matrix is {sample_row} ')
            row_two()
            break
        except ValueError:
            value_error()
def matrix_row_three():
    '''Docstring for jalal_lab_4'''

    while True:
        try:
            sample_row = np.array([0.0,0.0,0.0])
            print('----------------------------------------------')

            def row_three():
                print(f'Your third row currently looks like {sample_row}')
                value_one = float(input('\nPlease enter your first matrix value: '))
                sample_row[0] = value_one
                print(sample_row)

                value_two = float(input('\nPlease enter your second matrix value: '))
                sample_row[1] = value_two
                print(sample_row)

                value_three = float(input('\nPlease enter your third matrix value: '))
                sample_row[2] = value_three
                print(sample_row)

                global row_three_matrix
                row_three_matrix = sample_row

                print("")
                print(f'The third row of your matrix is {sample_row} ')
            row_three()
            break
        except ValueError:
            value_error()
    '''grabs matrix'''
    print('')
def row_means(rm_value1, rm_value2, rm_value3):
    '''provides row means in cleaner format'''
    print(f'The mean value of each row in your matrix is: [{rm_value1}, {rm_value2}, {rm_value3}] ')
def column_means(cm_value1, cm_value2, cm_value3):
    '''provides column means in cleaner format'''
    print(f'The mean value of each column in your matrix is: [{cm_value1}, {cm_value2}, {cm_value3}] ')

def add_matrices(matrix_one,matrix_two):
    '''adds and transposes two and mean values  matrices'''

    adding_matrices = np.add(matrix_one,matrix_two)
    print(f'\nI added your matrices together, the output is: \n{adding_matrices}')

    transposed_matices_sum = np.transpose(adding_matrices)
    print(f'\nI transposed the sum of your matrices, the output is: \n{transposed_matices_sum}')

    row_mean = np.mean(adding_matrices, axis=1)
    column_mean = np.mean(adding_matrices, axis=0)

    rm_value1 = row_mean[0]
    rm_value2 = row_mean[1]
    rm_value3 = row_mean[2]

    cm_value1 = column_mean[0]
    cm_value2 = column_mean[1]
    cm_value3 = column_mean[2]

    print('')
    row_means(rm_value1, rm_value2, rm_value3)

    print('')
    column_means(cm_value1,cm_value2,cm_value3)
def subtract_matricies(matrix_one, matrix_two):
    '''subtracts and transposes two and mean values  matrices'''

    subtracting_matrices = np.subtract(matrix_one,matrix_two)
    print(f'\nI subtracted your matrices against eachother, the output is: \n{subtracting_matrices}')

    transposed_matices_sum = np.transpose(subtracting_matrices)
    print(f'\nI transposed the sum of your matrices, the output is: \n{transposed_matices_sum}')

    row_mean = np.mean(subtracting_matrices, axis=1)
    column_mean = np.mean(subtracting_matrices, axis=0)

    rm_value1 = row_mean[0]
    rm_value2 = row_mean[1]
    rm_value3 = row_mean[2]

    cm_value1 = column_mean[0]
    cm_value2 = column_mean[1]
    cm_value3 = column_mean[2]

    print('')
    row_means(rm_value1, rm_value2, rm_value3)

    print('')
    column_means(cm_value1,cm_value2,cm_value3)

def multiply_matrices(matrix_one, matrix_two):
    '''subtracts and transposes two and mean values  matrices'''
    multiplying_matrices = matrix_one @ matrix_two
    print(f'\nI multiplied your matrices against eachother, the output is: \n{multiplying_matrices}')

    transposed_matices_sum = np.transpose(multiplying_matrices)
    print(f'\nI transposed the product of your matrices, the output is: \n{transposed_matices_sum}')

    row_mean = np.mean(multiplying_matrices, axis=1)
    column_mean = np.mean(multiplying_matrices, axis=0)
    
    rm_value1 = row_mean[0]
    rm_value2 = row_mean[1]
    rm_value3 = row_mean[2]

    cm_value1 = column_mean[0]
    cm_value2 = column_mean[1]
    cm_value3 = column_mean[2]

    print('')
    row_means(rm_value1, rm_value2, rm_value3)

    print('')
    column_means(cm_value1,cm_value2,cm_value3)

def multiply_matrices_by_element(matrix_one, matrix_two):
    '''subtracts and transposes two and mean values  matrices'''

    element_by_element = matrix_one * matrix_two
    print('\nI multiplied your matrices against eachother, element by element. '
          f'the output is: \n{element_by_element}')

    transposed_matices_sum = np.transpose(element_by_element)
    print(f'\nI transposed the product of your matrices, the output is: \n{transposed_matices_sum}')

    row_mean = np.mean(element_by_element, axis=1)
    column_mean = np.mean(element_by_element, axis=0)

    rm_value1 = row_mean[0]
    rm_value2 = row_mean[1]
    rm_value3 = row_mean[2]

    cm_value1 = column_mean[0]
    cm_value2 = column_mean[1]
    cm_value3 = column_mean[2]

    print('')
    row_means(rm_value1, rm_value2, rm_value3)

    print('')
    column_means(cm_value1,cm_value2,cm_value3)

def create_matrices():
    '''creating matrices'''
    global matrix_one
    global matrix_two

    print('Creating matrix one')
    matrix_row_one()
    matrix_row_two()
    matrix_row_three()
    matrix_one = np.array([row_one_matrix,row_two_matrix,row_three_matrix])

    print('--------------------------------------------')

    print('\nCreating matrix two')
    matrix_row_one()
    matrix_row_two()
    matrix_row_three()
    matrix_two = np.array([row_one_matrix,row_two_matrix,row_three_matrix])

    print('--------------------------------------------')
    print(f'\n Matrix one = \n{matrix_one}')
    print(f'\n Matrix two = \n{matrix_two}')
def menu():
    '''creating matrices'''
    # create_matrices()

    while True:
        print('\n\n Matrix program')
        print('-------------------------------------------------')
        print('A. Add matrices')
        print('B. Subtract matrices')
        print('C. Multiply matrices')
        print('D. Multiply matrices element by element')
        print('E. Exit Program')
        desired_destination = input('Enter respective letter for desired operation: ')

        acceptable_inputs = ['A','B','C','D','E']
        x = desired_destination.upper()

        if x not in acceptable_inputs:
            if value_error():
                continue

        if x == 'A':
            add_matrices(matrix_one, matrix_two)

        if x == 'B':
            subtract_matricies(matrix_one, matrix_two)

        if x == 'C':
            multiply_matrices(matrix_one, matrix_two)

        if x == 'D':
            multiply_matrices_by_element(matrix_one, matrix_two)

        if x == 'E':
            exit_program()
menu()

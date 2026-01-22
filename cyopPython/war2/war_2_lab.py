'''docStringPlaceHolder'''
import math
import string
from datetime import date
#import random
import string_utils

def week_2_deliverables_menu():
    '''docStringPlaceHolder'''

    print('Welcome to week 2 deliverables:')
    print('A. Generate Secure Password')
    print('B. Calculate and format a percentage')
    print('C. When is July 4, 2026?')
    print('D. Use the Law of Cosines to calculate the leg of a triangle')
    print('E. Calculate the volume of a Right Circular Cylinder')
    print('F. Exit Program')
#def week_2_deliverables_choices():
def law_of_cosines():
    '''docStringPlaceHolder'''
    c = float(0.79863551004729284628400080406894)


    # user input for sides of triangle
    side_a = int(input('Enter input for side a: '))
    side_b = int(input('Enter input for side b: '))
    # side_c = int(input('Enter input for side c'))

    # side_a^2 + side_b^2 =185
    def cosine_func1():
        global answer_func1
        answer_func1 = pow(side_a, 2) + pow(side_b, 2)
    cosine_func1()

    # -2(side_a * side_b)= -176 = -140.55984976832354094598414151613
    def consine_func2():
        global answer_func2
        answer_func2 = -2 * side_a * side_b
    consine_func2()


    #cosine * func2 = -140.9080430334r444444
    def cosine_func4():
        global cosine_times_func2_answer
        cosine_times_func2_answer = answer_func2 * c
    cosine_func4()

    # cosine_times_func2_answer + func1
    def cosine_func5():
        global func4_plus_func1
        func4_plus_func1= cosine_times_func2_answer + answer_func1
    cosine_func5()

    #squre_root_func5
    def cosine_func6():
        squared = math.sqrt(func4_plus_func1)
        square_root = round(squared,2)
        print(f'Your inputed numbers equals {square_root}.')
    cosine_func6()
def days_until_july4():
    '''docStringPlaceHolder'''

    today = date.today()
    july4_2026 = date(2026, 7, 4)

    jul4_minus_today = july4_2026 - today
    x_days = jul4_minus_today.days

    print(f'July 4th is {x_days} days away. ')
def caulculate_and_format_percentage():
    '''docStringPlaceHolder'''
    numerator = int(input('Enter your Numerator: '))
    denominator = int(input('Enter your Denominator: '))
    decimals_to_include = int(input('Enter the amount of places you want: '))

    quotient = numerator / denominator
    float_output = quotient * 100

    #grabs int
    grab_integer = int(math.floor(float_output))

    #grabs decimal #'s
    grab_float = grab_integer - float_output

    #turns grab_float to a string (This will get sliced)
    float_to_string = str(grab_float)
    slice_float = float_to_string[3:]

    #user decimal points to include
    slice_float = slice_float[0:decimals_to_include]

    print(f'Your answer is {grab_integer}.{slice_float}')
def volume_of_right_circular_cylinder():
    '''docStringPlaceHolder'''
    #when using math.py, I got slightly diff answer.
    pi = 3.14
    user_radius_input = int(input('Enter your Radius: '))
    user_height_input = int(input('Enter you height: '))
    pow_radius = pow(user_radius_input,2)
    vol_circular_cylinder_formula = (pi * pow_radius) * user_height_input

    print(vol_circular_cylinder_formula)
def password_generator():
    '''docStringPlaceHolder'''
    #user input: length, strong, weak, medium


    password_inputs = string.digits + string.ascii_umgc + string.punctuation
    scrambled_password = string_utils.shuffle(password_inputs)

    print('weak, medium, strong')
    password_complexity = input('Chose your password complexity: ')

    if password_complexity == 'weak':
        weak_password = scrambled_password
        print(weak_password)


#week_2_deliverables_menu()
law_of_cosines()
#days_until_july4() done
# caulculate_and_format_percentage() doneZO
#volume_of_right_circular_cylinder() done
# password_generator()

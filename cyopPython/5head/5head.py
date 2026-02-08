'''jalal_abdullah lab_5'''
import sys
import statistics
import pandas as pd


population_data = pd.read_csv('pop_change.csv')
population_df = pd.DataFrame(population_data)
pop_shape = population_df.shape[0]

housing_data = pd.read_csv('housing.csv')
housing_df = pd.DataFrame(housing_data)

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

def load_apr1_data():
    '''contains data for apr population'''

    global pop_apr1
    global apr1_min
    global apr1_max
    global apr1_mean
    global standard_deviation_apr1

    # this gets population of everything in pop_apr1
    pop_apr1 = population_df['Pop Apr 1']
    # print(pop_apr1)

    # prints min/max of apr1Pop
    apr1_min = population_df['Pop Apr 1'].min()
    # print(apr1_min)

    apr1_max = population_df['Pop Apr 1'].max()
    # print(apr1_max)

    # prints mean of pop apr1
    apr1_mean = population_df['Pop Apr 1'].mean()
    # print(apr1_mean)

    # standard deviation??
    standard_deviation_apr1 = statistics.stdev(population_df['Pop Apr 1'])
    # print(standard_deviation)
def load_jul1_data():
    '''contains data for jul1 population'''

    global pop_jul1
    global jul1_min
    global jul1_max
    global jul1_mean
    global standard_deviation_jul1
    # this gets population of everything in pop_July1
    pop_jul1 = population_df['Pop Jul 1']
    # print(pop_jul1)

    # prints min/max of jul1Pop
    jul1_min = population_df['Pop Jul 1'].min()
    # print(jul1_min)

    jul1_max = population_df['Pop Jul 1'].max()
    # print(jul1_max)

    # prints mean of pop jul1
    jul1_mean = population_df['Pop Jul 1'].mean()
    # print(jul1_mean)

    # standard deviation
    standard_deviation_jul1 = statistics.stdev(population_df['Pop Jul 1'])
    # print(standard_deviation_jul1)
def load_housing_data():
    '''contains data for housing func'''
    global house_age
    global house_bedrooms
    global year_built
    global house_rooms
    global house_utilities
    global house_weight
    global house_n_units

    # gets ages
    house_age = housing_df['AGE']

    # get bedrooms
    house_bedrooms = housing_df['BEDRMS'].min()

    # get year_built
    year_built = housing_df['BUILT'].max()

    # gets_rooms
    house_rooms = housing_df['ROOMS'].mean()

    # gets_utility
    house_utilities = housing_df['UTILITY']

    #gets weight
    house_weight = housing_df['WEIGHT']

    #gets nunits
    house_n_units = housing_df['NUNITS']


def apr_func():
    '''shows user info on apr '''

    print('\nThe population stats of April 1 are:')
    print(f'Count = {pop_shape}')
    print(f'Mean = {apr1_mean}')
    print(f'Standard Deviation = {standard_deviation_apr1}')
    print(f'Min = {apr1_min}')
    print(f'Max = {apr1_max}')
def july_func():
    '''shows user info on jul '''

    print('\nThe population stats of July 1 are:')
    print(f'Count: {pop_shape}')
    print(f'Mean = {jul1_mean}')
    print(f'Standard Deviation = {standard_deviation_jul1}')
    print(f'Min = {jul1_min}')
    print(f'Max = {jul1_max}')
def user_population_data():
    '''runs population data'''
    while True:
        print('\nA. Population of April 1 \nB. Population of July 1\nC. Exit Program')
        column_to_analyze = input('Select a population to analyze, or exit the program: ')
        x = column_to_analyze.upper()

        acceptable_inputs = ['A','B','C']

        if x not in acceptable_inputs:
            if value_error():
                continue
        if x == 'A':
            load_apr1_data()
            apr_func()
        if x == 'B':
            load_jul1_data()
            july_func()
        if x == 'C':
            exit_program()
def update_population():
    '''user can update population change between apr and jul'''
    # my brain is so fried with the names, will fix
    def update_population_yo():
        while True:
            row_to_update = int(input('Yo are you an int: '))
            x = row_to_update.isnumeric()
            
            print('Man thats no good.')
            print(x)
    update_population_yo()
    while True:

        user_choice = input('A. Continue to update population \nB. Exit program')
        x = user_choice.upper()

        acceptable_inputs = ['A','B']

        if x not in acceptable_inputs:
            if value_error():
                continue
        if x == 'A':
            load_apr1_data()
            apr_func()
        if x == 'B':
            exit_program()
update_population()

def house_func():
    '''shows user info housing '''
    load_housing_data()

    print('\nThe housing stats are:')
    print(f'House age = {house_age}')
    print(f'Bedrooms = {house_bedrooms}')
    print(f'Year built = {year_built}')
    print(f'Rooms = {house_rooms}')
    print(f'House utilities = {house_utilities}')


def menu():
    '''entry point for programs'''
    while True:
        print('\n\n lab5 program')
        print('-------------------------------------------------')
        print('A. Population Data ')
        print('B. Housing Data')
        print('C. Exit Program')
        desired_destination = input('Enter respective letter for desired destination: ')


        acceptable_inputs = ['A','B','C']
        x = desired_destination.upper()

        if x not in acceptable_inputs:
            if value_error():
                continue

        if x == 'A':
            user_population_data()
        if x == 'B':
            house_func()
        if x == 'C':
            exit_program()
menu()

'''jalal_abdullah_lab_five '''
import sys
import statistics
import pandas as pd
import matplotlib.pyplot as plt

population_data = pd.read_csv('pop_change.csv', index_col=0)
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
    global min_house_age
    global max_house_age
    global mean_house_age

    global min_house_bedrooms
    global max_house_bedrooms
    global mean_house_bedrooms

    global min_year_built
    global max_year_built
    global mean_year_built

    global min_house_rooms
    global max_house_rooms
    global mean_house_rooms

    global min_house_utilities
    global max_house_utilities
    global mean_house_utilities

    global house_weight
    global house_n_units

    # gets ages
    min_house_age = housing_df['AGE'].min()
    max_house_age = housing_df['AGE'].max()
    mean_house_age = housing_df['AGE'].mean()
    # get bedrooms
    min_house_bedrooms = housing_df['BEDRMS'].min()
    max_house_bedrooms = housing_df['BEDRMS'].max()
    mean_house_bedrooms = housing_df['BEDRMS'].mean()

    # get year_built
    min_year_built = housing_df['BUILT'].min()
    max_year_built = housing_df['BUILT'].max()
    mean_year_built = housing_df['BUILT'].mean()
    # gets_rooms
    min_house_rooms = housing_df['ROOMS'].min()
    max_house_rooms = housing_df['ROOMS'].max()
    mean_house_rooms = housing_df['ROOMS'].mean()
    # gets_utility
    min_house_utilities = housing_df['UTILITY'].min()
    max_house_utilities = housing_df['UTILITY'].max()
    mean_house_utilities = housing_df['UTILITY'].mean()

    #gets weight
    house_weight = housing_df['WEIGHT']

    #gets nunits
    house_n_units = housing_df['NUNITS']
def apr_func():
    '''shows user info on apr and histogram '''

    print('\nThe population stats of April 1 are:')
    print(f'Count = {pop_shape}')
    print(f'Mean = {apr1_mean}')
    print(f'Standard Deviation = {standard_deviation_apr1}')
    print(f'Min = {apr1_min}')
    print(f'Max = {apr1_max}')

    plt.figure(figsize=(8, 5))
    plt.hist(pop_apr1, bins=20, alpha=0.7)
    plt.title('Histogram of Pop Apr1')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def july_func():
    '''shows user info on jul and histogram '''

    print('\nThe population stats of July 1 are:')
    print(f'Count: {pop_shape}')
    print(f'Mean = {jul1_mean}')
    print(f'Standard Deviation = {standard_deviation_jul1}')
    print(f'Min = {jul1_min}')
    print(f'Max = {jul1_max}')

    plt.figure(figsize=(8, 5))
    plt.hist(pop_jul1, bins=20, alpha=0.7)
    plt.title('Histogram of Pop Jul 1')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def user_population_data():
    '''allows user to view desired population
      month, or update program'''

    while True:
        print('\nA. Population of April 1 \nB. Population of July 1\nC. Update population\n'
              'D. Return to home\nE. Exit program')
        column_to_analyze = input('Select a population to analyze, or exit the program: ')
        x = column_to_analyze.upper()

        acceptable_inputs = ['A','B','C','D','E']

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
            update_population()
        if x == 'D':
            return
        if x == 'E':
            exit_program()
def update_population():
    '''user can update population between apr and jul'''
    while True:

        print('\nA. Continue to update population \nB. Return to home\nC. Exit program')
        user_choice = input('Enter a letter for your desired action: ')
        x = user_choice.upper()

        acceptable_inputs = ['A','B','C']

        if x not in acceptable_inputs:
            if value_error():
                continue
        if x == 'A':
            update_population1()
        if x == 'B':
            return
        if x == 'C':
            exit_program()

def update_population1():
    '''user selects row to update'''
    while True:
        row_to_update = input('\nEnter the row you wish to update. It can be between 0-555: ')
        try:
            x = int(row_to_update)

            if 0 <= x <= 555:
                update_population2(x)
                print('\nWould you like to update another row? Enter Yes or No: ')
                update_next_row = input()
                y = update_next_row.upper()

                if y == 'YES':
                    continue
                if y == 'NO':
                    return
                print('Not sure what you mean, exiting.')
                return


            print('This row cannot be found inside dataset, would you like to try again?')
            user_input = input('Enter yes or no: ')
            y = user_input.lower()

            if y == 'yes':
                continue
            if y == 'no':
                exit_program()
            else:
                print('I didnt understand that, restarting program')
                continue
        except ValueError:
            value_error()

def update_population2(x):
    '''shows user their selected row, and allows them to change it'''
    while True:
        selected_row = population_df.loc[x]

        print(f'\nThis is the current data for your selected row: \n {selected_row}')
        print('\nA. April\nB. July')
        user_input = input('Please select a value to update: ')
        y = user_input.upper()
        acceptable_inputs = ['A','B']

        if y not in acceptable_inputs:
            if value_error():
                continue

        # update apr
        if y == 'A':
            while True:
                try:
                    apr1_population_update = int(input('Please enter your updated population: '))
                    current_apr1_population = population_df.loc[x,'Pop Apr 1']
                    user_update = input(f"The current population of row "
                    f"{x} is {current_apr1_population}."
                    f" Would you like to change update it to "
                    f"{apr1_population_update}? Answer yes or no: ")

                    user_update.lower()
                    if user_update == 'yes':

                        population_df.loc[x,'Pop Apr 1'] = apr1_population_update
                        apr1_current_population = population_df.loc[x,'Pop Apr 1']
                        jul1_current_population = population_df.loc[x,'Pop Jul 1']

                        calculate_change(jul1_current_population,apr1_current_population)
                        population_df.loc[x,'Change Pop'] = population_change
                        population_df.to_csv('pop_change.csv')

                        print(f'\nHere is your updated population:\n{population_df.loc[x]}')
                        return
                    if user_update == 'no':
                        print('Returning to main menu')
                        return
                    print('Not updating population, and returning to main menu.')
                    return
                except ValueError:
                    value_error()

        # update jul
        if y == 'B':
            while True:
                try:
                    jul1_population_update = int(input('Please enter your updated population: '))
                    current_jul1_population = population_df.loc[x,'Pop Jul 1']
                    user_update = input(f"The current population of row "
                    f"{x} is {current_jul1_population}."
                    f" Would you like to change update it to "
                    f"{jul1_population_update}? Answer yes or no: ")

                    user_update.lower()
                    if user_update == 'yes':

                        population_df.loc[x,'Pop Jul 1'] = jul1_population_update
                        # change_pop func below thi line
                        apr1_current_population = population_df.loc[x,'Pop Apr 1']
                        jul1_current_population = population_df.loc[x,'Pop Jul 1']

                        calculate_change(jul1_current_population,apr1_current_population)
                        population_df.loc[x,'Change Pop'] = population_change

                        population_df.to_csv('pop_change.csv')
                        print(f'\nHere is your updated population:\n{population_df.loc[x]}')
                        return
                    if user_update == 'no':
                        print('Returning to main menu')
                        return
                    print('Not updating population, and returning to main menu.')
                    return
                except ValueError:
                    value_error()

def calculate_change(jul1,apr1):
    '''calculates change between months'''
    global population_change
    population_change = jul1 - apr1

def house_func():
    '''shows user info on houses '''
    load_housing_data()

    print('\nThe housing stats are:')

    print('\nHouse age:')
    print(f'Min = {min_house_age}')
    print(f'Mean = {mean_house_age}')
    print(f'Max = {max_house_age}')

    print('\nBedrooms:')
    print(f'Min = {min_house_bedrooms}')
    print(f'Mean = {mean_house_bedrooms}')
    print(f'Max = {max_house_bedrooms}')

    print('\nYear built:')
    print(f'Min = {min_year_built}')
    print(f'Mean = {mean_year_built}')
    print(f'Max = {max_year_built}')

    print('\nRooms:')
    print(f'Min = {min_house_rooms}')
    print(f'Mean = {mean_house_rooms}')
    print(f'Max = {max_house_rooms}')

    print('\nHouse utilities:')
    print(f'Min = {min_house_utilities}')
    print(f'Max = {max_house_utilities}')
    print(f'Mean = {mean_house_utilities}')

def menu():
    '''entry point for program'''
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

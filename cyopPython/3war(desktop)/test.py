import pandas as pd

#I like this out put. DataFrame gives me a weird 3 dot thing
#Maybe we use read_csv to return all states +
# df = pd.DataFrame(data)

#Good code here - allows me to get all of a states data from index_col
# data = pd.read_csv('state_info.csv',
#     index_col='State')

# def get_state_info():
#     first = data.loc['Maryland']
#     second = data.loc['Idaho']

#     print(first, "\n\n\n", second)
# data = pd.read_csv('state_info.csv',
#     index_col='State')


data = pd.read_csv('state_info.csv')
df = pd.DataFrame(data)


def get_state_info():
    df = pd.read_csv('state_info.csv',
        index_col='Postal')

    postal = input('Please enter your states postal name to see its details: ')
    selected_state = df.loc[postal]
    print(f'Your selected states information is: \n\n {selected_state}')
get_state_info()




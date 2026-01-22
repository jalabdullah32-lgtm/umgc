'''lol'''
import pandas as pd
# import csv

df = pd.read_csv('state_info.csv')

states = df['State']
postal = df['Postal']
capital = df['Capital']
population = df['Population']
flower = df['Flower']


# test_df = pd.DataFrame({'State': states, 'Postal': postal})

# state_lookup = input('I am looking for a state called: ')

print(df.info())
# if state_lookup not in states or postal:
#     print(f'I could not find {state_lookup} ')
# elif state_lookup in states | postal:
#     print(f'I found {state_lookup}')

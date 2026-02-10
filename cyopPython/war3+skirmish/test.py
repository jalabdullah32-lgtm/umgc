''''waste of time'''
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
from PIL import Image
from pathlib import Path
import pandas as pd






#I like this output. print df gives me a weird 3 dot thing
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


data = pd.read_csv('state_info_md.csv')
df = pd.DataFrame(data)

# print(data)

# plt.title("flower img")
# plt.xlabel("x pixel scaling")
# plt.ylabel("Y pixels scaling")

# image = mpimg.imread("md_flower.jpg")
# plt.imshow(image)
# plt.show()

def get_state_info():
    '''docstring_placeholder'''
    df_state_info = df
    df_state_info = pd.read_csv('state_info_md.csv',
        index_col='postal',)

    postal = input('Please enter your states postal name to see its details: ')
    selected_state = df_state_info.loc[postal]

    # get_image = selected_state.loc[4]
    # print(get_image)

    print(f'Your selected states information is: \n\n {selected_state}')
    # image = mpimg.imread("md_flower.jpg")
    # plt.imshow(image)
    # plt.show()    
get_state_info()

# 

# folder_dir = 'flowers'
# images = Path(folder_dir).glob('*.jpg')
# userSelection = input('What img do you want to see? ')
# for image in images:
#     print(image)


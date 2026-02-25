from difflib import *
def common_passwords(password):
    '''checks user password against common ones'''
    with open('CommonPasswords.txt',encoding="utf-8") as f:
        read_data = f.read()
    close_passwords = get_close_matches(password,[read_data])

    if len(close_passwords) == 0:
        return None
    if len(close_passwords) > 0:
        return 'The password you entered  was found in a list of common passwords'

password = 'dragonball'
common_passwords(password)
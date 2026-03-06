import difflib
import logging
logger = logging.getLogger(__name__)


def do_something():
    logger.info('Doing something')


def common_passwords(password):
    '''checks user password against common ones'''
    with open('CommonPasswords.txt','r',encoding="utf-8") as f:
        possibilities = [line.strip() for line in f]

    n = 3 
    cutoff = 0.7
    close_passwords = difflib.get_close_matches(password,possibilities,n,cutoff)
    print(close_passwords)

password = 'applepasswor'
common_passwords(password)



    #     file_content = ''
    #     line = f.readline()

    #     while line:
    #         file_content += line
    #         line.strip
    #         line = f.readline()
    # print(file_content)


    # word = password
    # possibilities = file_content
    # n = 3 
    # cutoff = 0.7
    # close_passwords = difflib.get_close_matches(word,possibilities,n,cutoff)
    # print(close_passwords)

# word = "learning"
# possibilities = ["love", "learn", "lean", "moving", "hearing"]
# n = 3
# cutoff = 0.7

# close_matches = difflib.get_close_matches(word, 
#                 possibilities, n, cutoff)

# print(close_matches)
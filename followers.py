from analyse import get_follower_data 
from check import check_tweeps
import os
from sys import platform

def analyse_user():
    print('Geef de twitter username (zonder @) in')
    print('en de datum vanaf wanneer je informatie wilt')
    print('over volgers. Let op de aangegeven datum notatie.\n\n')

    wie = input('Twitter username: ')
    datum = input('Vanaf welke datum (dd-mm-jjj): ')
    followers = get_follower_data(wie)
    test = check_tweeps(wie, datum)

    if platform == 'linux' or platform == 'linux2' or platform = 'darwin':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')

    print(followers)
    print('\n\n')
    print(test)

try:
    if platform == 'linux' or platform == 'linux2' or platform = 'darwin':
        os.system('rm *.json')
    elif platform == 'win32':
        os.system('del *.json')
except:
    print('No files to delete')

analyse_user()

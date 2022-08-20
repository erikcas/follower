from analyse import get_follower_data 
from check import check_tweeps
import os

def analyse_user():
    print('Geef de twitter username (zonder @) in')
    print('en de datum vanaf wanneer je informatie wilt')
    print('over volgers. Let op de aangegeven datum notatie.\n\n')

    wie = input('Twitter username: ')
    datum = input('Vanaf welke datum (dd-mm-jjj): ')
    followers = get_follower_data(wie)
    test = check_tweeps(wie, datum)

    os.system('clear')
    print(followers)
    print('\n\n')
    print(test)

os.system('rm -rf *.json')
analyse_user()

from analyse import get_follower_data 
from check import check_tweeps
import os
from sys import platform
from graphs import maak_grafiek

def analyse_user():
    print('Geef de twitter username (zonder @) in')
    print('en de datum vanaf wanneer je informatie wilt')
    print('over volgers. Let op de aangegeven datum notatie.')
    print('Geef ook aan of je bestaande data wilt gebruiken,')
    print('je kunt ook de data opnieuw gebruiken door "n" in te geven.\n\n')

    wie = input('Twitter username: ')
    datum = input('Vanaf welke datum (dd-mm-jjj): ')
    reuse_data = input('Data opnieuw ophalen (j|n): ')

    if reuse_data == 'j' or reuse_data == 'J':
        try:
            if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
                os.system('rm *.json')
            elif platform == 'win32':
                os.system('del *.json')
        except:
            print('No files to delete')
    elif reuse_data == 'n' or reuse_data == 'N':
        print('We gebruiken de bestaande data indien aanwezig.')
    else:
        print('Graag j of n ingeven. Voer het script opnieuw uit.')
        sys.exit()

    followers = get_follower_data(wie)
    twitter_data = check_tweeps(wie)

    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')

    print(followers)
    print(twitter_data)
    maak_grafiek(twitter_data, datum)

analyse_user()

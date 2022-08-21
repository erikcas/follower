from analyse import get_follower_data 
from check import check_tweeps
import os
import sys
from sys import platform
from graphs import maak_grafiek

def analyse_user():
    print('Geef de twitter username (zonder @) in')
    print('en de datum vanaf wanneer je informatie wilt')
    print('over volgers. Let op de aangegeven datum notatie.')
    print('Geef ook aan of je bestaande data wilt gebruiken,')
    print('je kunt ook de data opnieuw gebruiken door "n" in te geven.\n\n')

    # Wie gaan we zoeken
    wie = input('Twitter username: ')
    if not wie:
        print('Graag een twitter username ingeven. Start het script opnieuw.')
        sys.exit()
    # Vanaf welke datum aanmaak account
    datum = input('Account aangemaakt vanaf welke datum (dd-mm-jjj): ')
    # Zoeken we op volgerloze of tweetloze volgers
    wat = input('Kijken naar nul volgers of nul tweets (v|t): ')
    if wat == 'v' or wat == 'V':
        wat = 'Volgers'
    elif wat == 't' or wat == 'T':
        wat = 'Tweets'
    else:
        print('Graag een t (tweets) of een v (volgers) ingeven. Voer het script opnieuw uit.')
        sys.exit()
    # Behouden we de reeds opgehaalde data of halen we verse data op?
    reuse_data = input('Data opnieuw ophalen (j|n): ')
    if reuse_data == 'j' or reuse_data == 'J':
        try:
            if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
                os.system(f'rm *{wie}*.json')
            elif platform == 'win32':
                os.system('del *{wie}*.json')
        except:
            print('No files to delete')
        # Halen we de 5000 meest recente volgers op of alle volgers?
        tijd = input('Alle accounts of 5000 meest recente (a|r): ')
        if tijd =='a' or tijd == 'A':
            tijd = 'a'
        elif tijd == 'r' or tijd == 'R':
            tijd = 'r'
        else:
            print('Graag gevraagde invoer ingeven. Start het script opnieuw.')
            sys.exit()
    elif reuse_data == 'n' or reuse_data == 'N':
        # Gebruik de voorhanden data, indien aanwezig
        print('We gebruiken de bestaande data indien aanwezig.')
        print('Als geen data aanwezig blijkt, halen we deze op.')
        print('We halen standaard alleen de meest recente 5000 volgers op.')
        tijd = 'r'
    else:
        print('Graag j of n ingeven. Voer het script opnieuw uit.')
        sys.exit()

    followers = get_follower_data(wie, tijd)
    twitter_data = check_tweeps(wie)

    if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
        os.system('clear')
    elif platform == 'win32':
        os.system('cls')

    print(followers)
    print(twitter_data)
    maak_grafiek(wie, twitter_data, datum, wat, tijd)

analyse_user()

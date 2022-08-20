import sys
import json
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC

def check_tweeps(schermnaam, datum):
    nul_follow = 0
    has_follow = 0
    nul_tweeted = 0
    has_tweeted = 0
    twitteraars = 0
    aantal = 0
    #Twitter tijd is UTC dus even aanpassen
    twitter_datum = datetime.strptime(datum, '%d-%m-%Y').strftime('%Y-%m-%d')
    startDate = utc.localize(datetime.strptime(datum, '%d-%m-%Y'))
    startDate = startDate - timedelta(hours=2)
    with open(f'{schermnaam}_followers.json', 'r') as f:
        page = json.load(f)
        for creep in page:
            # Wanneer is deze lid geworden van twitter
            aanmaak = creep['created_at']
            aanmaak = datetime.strftime(datetime.strptime(aanmaak,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d')
            aanmaak = utc.localize(datetime.strptime(aanmaak, '%Y-%m-%d'))
            # Hoeveel volgers? En zet om naar een string voor de nul-check
            volgers = str(creep['followers_count'])
            # Hoeveel tweets? En zet om naar een string voor de nul-check
            tweets = str(creep['statuses_count'])
            # De check. Pak alleen de tweeps lid geworden na de ingegeven datum
            print(aanmaak)
            print(startDate)
            if aanmaak > startDate:
                twitteraars += 1
                print(f'{aanmaak}\t{volgers}\t{tweets}')
                if volgers == '0':
                    nul_follow += 1
                else:
                    has_follow += 1
                if tweets == '0':
                    nul_tweeted += 1
                else:
                    has_tweeted += 1
            aantal += 1
            
    # Procentueel
    procent_nul_volgers = int((nul_follow / twitteraars) * 100)
    procent_nul_tweets = int((nul_tweeted / twitteraars) * 100)
    # Print de samenvatting:
    res = ''
    res += f'Aantal gecheckte volgers: {aantal}\n'
    res += f'Aantal volgers van {schermnaam} met een twitteraccount aangemaakt na {datum}: {twitteraars}\n'
    res += f'\nVan die accounts hebben:\n'
    res += f'{nul_follow} volgers zelf geen volgers. Dat is afgerond {procent_nul_volgers} procent\n'
    res += f'{has_follow} volgers 1 of meer volgers.\n'
    res += f'{nul_tweeted} volgers zelf nog niets getweet. Dat is afgerond {procent_nul_tweets} procent\n'
    res += f'{has_tweeted} volgers 1 of meer tweets gepost.\n'

    return res
# Dit script vereist de tweepy en pytz module. Installeer:
# pip install tweepy
# pip install pytz
# Tweepy versie 4.10

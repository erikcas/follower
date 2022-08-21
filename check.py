import sys
import json
from datetime import datetime, timedelta
import pytz
import pandas as pd
utc=pytz.UTC

def check_tweeps(schermnaam, datum):
    rij = 0
    # Maak leeg dataframe
    df = pd.DataFrame()
    #Twitter tijd is UTC dus even aanpassen
    twitter_datum = datetime.strptime(datum, '%d-%m-%Y').strftime('%Y-%m-%d')
    startDate = utc.localize(datetime.strptime(datum, '%d-%m-%Y'))
    startDate = startDate - timedelta(hours=2)
    with open(f'{schermnaam}_followers.json', 'r') as f:
        page = json.load(f)
        for creep in page:
            # Schermnaam
            df.loc[rij, 'schermnaam'] = creep['screen_name']
            # Twitter user id
            df.loc[rij, 'user_id'] = creep['id_str']
            # Wanneer is deze lid geworden van twitter
            aanmaak = creep['created_at']
            aanmaak = datetime.strftime(datetime.strptime(aanmaak,'%a %b %d %H:%M:%S +0000 %Y'), '%Y-%m-%d')
            aanmaak = datetime.strptime(aanmaak, '%Y-%m-%d').strftime('%d-%m-%Y')
            df.loc[rij, 'created'] = aanmaak
            # Hoeveel volgers?
            df.loc[rij, 'volgers'] = creep['followers_count']
            # Hoeveel volgend?
            df.loc[rij, 'volgend'] = creep['friends_count']
            # Hoeveel tweets?
            df.loc[rij, 'tweets'] = creep['statuses_count']
            # De check. Pak alleen de tweeps lid geworden na de ingegeven datum
            rij += 1

    return df

# Dit script vereist de tweepy en pytz module. Installeer:
# pip install tweepy
# pip install pytz
# Tweepy versie 4.10
# usage: check_tweep.py <schermnaam> <rij recentste volgers> <dd-mm-jjjj>

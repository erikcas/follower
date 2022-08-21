import sys
import json
from datetime import datetime, timedelta
import pandas as pd

def check_tweeps(schermnaam):
    # Maak leeg dataframe
    df = pd.DataFrame()
    df = pd.read_json(f'{schermnaam}_followers.json')
    # Zet de datum om, zodat we kunnen vergelijken
    df['aanmaak'] = pd.to_datetime(df['created_at']).dt.date
    df = df[['screen_name', 'id_str', 'aanmaak', 'followers_count', 'friends_count', 'statuses_count']]
    return df

# Dit script vereist de tweepy en pytz module. Installeer:
# pip install tweepy
# pip install pytz
# Tweepy versie 4.10
# usage: check_tweep.py <schermnaam> <rij recentste volgers> <dd-mm-jjjj>

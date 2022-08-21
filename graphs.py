import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC

def maak_grafiek(twitter_data, datum):
    all_data = pd.DataFrame(twitter_data)
    #Twitter tijd is UTC dus even aanpassen
    startDate = (utc.localize(datetime.strptime(datum, '%d-%m-%Y'))
            - timedelta(hours = 2)).date()
    all_data = all_data[~(all_data['aanmaak'] < startDate)]
    all_data['aanmaak'] = pd.to_datetime(all_data['aanmaak'])
    # Haal de accounts met nul volgers op
    temp = all_data['followers_count'] == 0
    nul_follow = all_data[temp]
    all_data = all_data.groupby(by=all_data['aanmaak'].dt.date).count()
    nul_follow = nul_follow.groupby(by=nul_follow['aanmaak'].dt.date).count()

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(nul_follow.index, nul_follow['followers_count'], c='blue', label='Volgerloos')
    ax.plot(all_data.index, all_data['followers_count'], c='red', label='Alles')
    plt.legend(loc='upper left')
    plt.show()

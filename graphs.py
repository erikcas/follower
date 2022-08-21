import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime, timedelta
import pytz

utc=pytz.UTC

def maak_grafiek(wie, twitter_data, datum, wat,tijd):
    # Wat gaan we opzoeken? Tweets of volgers?
    if wat =='Volgers':
        zoeknaar = 'followers_count'
    else:
        zoeknaar = 'statuses_count'

    if tijd == 'a':
        soort = 'Alle accounts'
    elif tijd == 'r':
        soort = '5000 meest recente accounts'

    wat = wat.lower()
    # Even een leuke titel verzinnen
    titel = f'Volgers van @{wie}. Volgeraccounts aangemaakt op of na {datum}\n'
    titel += f'Totaal aantal {wat} (rood) vs. zonder (blauw)\n'
    titel += f'DISCLAIMER: <Account aangemaakt> op betekent NIET <volgend sinds>!'
 
    all_data = pd.DataFrame(twitter_data)
    #Twitter tijd is UTC dus even aanpassen
    startDate = (utc.localize(datetime.strptime(datum, '%d-%m-%Y'))
            - timedelta(hours = 2)).date()
    all_data = all_data[~(all_data['aanmaak'] < startDate)]
    all_data['aanmaak'] = pd.to_datetime(all_data['aanmaak'])
    # Haal de accounts met nul volgers op
    temp = all_data[zoeknaar] == 0
    nul_follow = all_data[temp]
    all_data = all_data.groupby(by=all_data['aanmaak'].dt.date).count()
    nul_follow = nul_follow.groupby(by=nul_follow['aanmaak'].dt.date).count()

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(nul_follow.index, nul_follow[zoeknaar], c='blue', label=f'{soort}. Geen {wat}')
    ax.plot(all_data.index, all_data[zoeknaar], c='red', label=f'{soort}. Totaal aantal {wat}')
    plt.legend(loc='upper left')
    plt.title(titel, fontsize=16)
    plt.show()
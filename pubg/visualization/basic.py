import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
import math


def killLoad():
    dir = '/Users/JoshLevin/PycharmProjects/data-visualizations/pubg/'

    print(str(datetime.datetime.now()))

    meta = pd.read_csv(filepath_or_buffer=dir+'source/pubg-match-deaths/aggregate/agg_match_stats_0.csv')
    print(str(datetime.datetime.now()))
    # Solo matches
    meta = meta[meta['party_size'] == 1]
    print('Have ' + str(meta.size) + ' solo matches')
    print('Have {0} distinct kill groups'.format(meta['player_kills'].drop_duplicates().size))
    print(str(datetime.datetime.now()))

    meta['total'] = meta.apply(lambda row: isWin(row['team_placement']), axis=1)

    print(str(datetime.datetime.now()))
    print(meta.columns)

    meta = meta[['player_kills','total']]

    print(meta.columns)

    meta = meta.groupby(['player_kills'], as_index=False).agg(
        [np.sum, np.size]
    ).rename(columns=
        {
           'player_kills' : 'kills',
           'sum' : 'win',
           'size' : 'matches',
        }
    )
    print(str(datetime.datetime.now()))

    print(meta)

    meta['w/l'] = meta.apply(lambda row: winPct(row), axis=1)

    print(str(datetime.datetime.now()))

    meta.to_csv('output.csv')

def isWin(val):
    if val == 1:
        return 1
    else:
        return 0

def winPct(row):
    return float(row['total']['win']) / float(row['total']['matches'])

# Takes as input
# INPUT: kills ; win ; matches ; winpct
# OUTPUT: Chart showing winpct/matches
def killVis():
    dir = '/Users/JoshLevin/PycharmProjects/data-visualizations/pubg/visualization/'

    df = pd.read_csv(dir + 'output.csv')

    plt.figure()

    ax = df.plot(kind='line', x='kills', y='wpct',
            xlim= (0,30))

    df.plot(kind='line', x='kills', y='matches',
            ax = ax,
            secondary_y=True,
            xlim=(0, 30))

    ax.right_ax.set_yscale='log'
    ax.legend(['Win Pct %', 'Matches (right)'])


    plt.show()


def minMapLoad():
    dir = '/Users/JoshLevin/PycharmProjects/data-visualizations/pubg/'

    deaths = pd.read_csv(filepath_or_buffer=dir+'source/pubg-match-deaths/deaths/kill_match_stats_final_0.csv')

    deaths = deaths[deaths['map'] == 'ERANGEL']

    deaths = deaths[['killer_position_x',
                     'killer_position_y',
                     'time']]


    #bins = [x for x in range(1, math.ceil(deaths['time'].max()/60) + 1)]
    # Bin by minute
    # deaths['time'] = pd.cut(deaths['time'],
    #                        bins=bins)

    # First minute deaths
    deaths = deaths[deaths['time'] < 60].dropna()

    deaths = [['killer_position_x', 'killer_position_y']]

    scale = lambda x : x * 4096 / 800000
    deaths = deaths.apply(scale)


    np.histogram2d(x=deaths['killer_position_x'], y=deaths['killer position y'], bins=100)

    fig, ax = plt.subplots(figsize=(24, 24))

    ax.set_xlim(0, 4096)
    ax.set_ylim(0, 4096)

    plt.show()

if __name__ == '__main__':
    minMapLoad()
#main()
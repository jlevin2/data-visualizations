import pandas as pd
import datetime
import numpy as np
import matplotlib


def main():
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


def vis():
    dir = '/Users/JoshLevin/PycharmProjects/data-visualizations/pubg/visualization/'

    df = pd.read_csv(dir + 'output.csv')

    df.plot(kind='line', x='kills', y='wpct')

    #df.plot(kind='line', x='kills', y='matches')

    matplotlib.pyplot.show()


if __name__ == '__main__':
    vis()
    #main()
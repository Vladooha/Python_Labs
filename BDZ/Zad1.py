import pandas as pd

def dead_count(series):
    dead = 0
    for alive_status in series:
        if alive_status == 0:
            dead += 1
    
    return dead

data = pd.read_csv('train.csv')
data_groupped = (data
    .loc[:, ['Sex', 'Pclass', 'Survived']]
    .groupby(['Sex', 'Pclass'])
    .agg({'Survived': ['sum', dead_count, 'count']}))
data_groupped.columns = ['survived_count', 'dead_count', 'total_count']
    
print(data_groupped)
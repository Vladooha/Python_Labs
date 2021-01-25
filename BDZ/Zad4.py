import pandas as pd

def parse_names(series):
    names = []
    for fullname in series:
        name = fullname.split(",")[0]
        names.append(name)
    
    return names

data = pd.read_csv('train.csv')
data_groupped = (data
    .loc[:, ['Name']]
    .transform(parse_names)
    .groupby(['Name'])
    .agg({'Name': ['count']})
    .apply(lambda x: x.sort_values(ascending=False).head(10)))
    
print(data_groupped)
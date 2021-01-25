import pandas as pd
import numpy as np
import math

SURVIVED_PROBAB = 1/2

PROBAB_WEIGHT = {
    'Pclass': 1/3,
    'Sex': 1/3,
    'Age': 1/12,
    'SibSp': 1/12,
    'Parch': 1/12,
    'Cabin': 1/12,
}

def parse_cabin(str):
    for cab_str in str.split(" "):
        try:
            return int(cab_str[1:])
        except Exception:
            continue
            
    return 0

def get_probab_by_median(value, median, max, min):
    if value > median:
        return (value - median) / (max - median)
    elif value < median:
        return (median - value) / (median - min)
    else:
        return 1;
    

data = pd.read_csv('train.csv')
data_survived = data[data['Survived'] == 1]

class_probab_table = {
    1: data_survived[data_survived['Pclass'] == 1].size / data[data['Pclass'] == 1].size,
    2: data_survived[data_survived['Pclass'] == 2].size / data[data['Pclass'] == 2].size,
    3: data_survived[data_survived['Pclass'] == 3].size / data[data['Pclass'] == 3].size,
}

sex_probab_table = {
    "male":     data_survived[data_survived['Sex'] == 'male'].size / data[data['Sex'] == 'male'].size,
    "female":   data_survived[data_survived['Sex'] == 'female'].size / data[data['Sex'] == 'female'].size,
}

median_age = np.nanmedian(data_survived['Age'].values)
max_age = data_survived['Age'].max()
min_age = data_survived['Age'].min()

median_sib = np.nanmedian(data_survived['SibSp'].values)
max_sib = data_survived['SibSp'].max()
min_sib = data_survived['SibSp'].min()

median_parch = np.nanmedian(data_survived['Parch'].values)
max_parch = data_survived['Parch'].max()
min_parch = data_survived['Parch'].min()

cabin_nums = []
for cabin_str in data_survived['Cabin'].values:
    if type(cabin_str) is float:
        continue
    cabin_nums.append(parse_cabin(cabin_str))
median_cabin = np.nanmedian(cabin_nums)
max_cabin = max(cabin_nums)
min_cabin = min(cabin_nums)
    

predicted = 0
data_test = pd.read_csv('test.csv')
predicted = {
    "PassengerId": [],
    "Survived": [],
}
for i, row in data_test.iterrows():
    predicted["PassengerId"].append(row['PassengerId'])

    class_probab = class_probab_table[row['Pclass']]
    sex_probab = sex_probab_table[row['Sex']]
    age_probab = get_probab_by_median(row['Age'], median_age, max_age, min_age)
    sib_probab = get_probab_by_median(row['SibSp'], median_sib, max_sib, min_sib)
    parch_probab = get_probab_by_median(row['Parch'], median_parch, max_parch, min_parch)
    cabin_probab = 0
    if type(row['Cabin']) is not float:
        cabin_probab = get_probab_by_median(parse_cabin(row['Cabin']), median_cabin, max_cabin, min_cabin)
    
    probab = (PROBAB_WEIGHT['Pclass'] * class_probab + PROBAB_WEIGHT['Sex'] * sex_probab + PROBAB_WEIGHT['Age'] * age_probab
        + PROBAB_WEIGHT['SibSp'] * sib_probab + PROBAB_WEIGHT['Parch'] * parch_probab + PROBAB_WEIGHT['Cabin'] * cabin_probab)
        
    result = 1 if probab > SURVIVED_PROBAB else 0
    predicted["Survived"].append(result)
    
data_predicted = pd.DataFrame(predicted)
data_predicted.to_csv('prediction.csv', index=False)

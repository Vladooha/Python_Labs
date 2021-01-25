import pandas as pd
import numpy as np
import math

def zeros(series):
    zeros_count = 0
    for cell in series:
        if 0 == cell:
            zeros_count += 1
    
    return zeros_count
    
def average(series):
    size = len(series)
    if 0 == size:
        return 0
    
    sum = 0
    for cell in series:
        cell_value = 0 if math.isnan(cell) else cell
        sum += cell_value
    
    return sum / size
        

data = pd.read_csv('train.csv')
numeric_columns = data.select_dtypes(include=np.number).columns
for column in numeric_columns:
    print("'{}' staticstics".format(column))
    column_statistic = (data
        .loc[:, ['Sex', column]]
        .groupby(['Sex'])
        .agg({column: ['sum', zeros, 'count', 'min', 'max', average]}))
    print(column_statistic)
    print('------')
import pandas as pd
import numpy as np

data = pd.read_csv('train.csv')
numeric_columns = data.select_dtypes(include=np.number).columns
for column in numeric_columns:
    median = np.nanmedian(data[column].values)
    print('[{}] Median is {}'.format(column, median))
    data[column].fillna(median, inplace = True)
    
data.to_csv('train_filled.csv')   
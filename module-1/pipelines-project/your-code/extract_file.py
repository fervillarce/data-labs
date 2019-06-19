
# coding: utf-8

# In[ ]:

import pandas as pd

def extract(csv_name):
    df = pd.read_csv(csv_name, header=0, encoding = 'unicode_escape')
    return df


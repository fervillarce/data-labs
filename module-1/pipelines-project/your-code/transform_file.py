
# coding: utf-8

# In[ ]:

import numpy as np

def erase_column_space(df):
    for column in df.columns:
        column = column.strip(" ")
    return df
    
def erase_space(df):
    df = df.str.strip()
    # You can also use df = df.apply(lambda s: str(s).strip())
    return df

def erase_columns_with_nulls(df):
    for col in df.columns:
        if (df[col].isnull().sum() / df.shape[0]) > 0.9:
            df.drop(col, axis=1, inplace = True)
    return df

def normalize_fatalfield(df):
    df['Fatal (Y/N)'].replace(['UNKNOWN', '#VALUE!'], np.NaN, inplace = True)
    # ¿Se puede hacer esto? df['Fatal (Y/N)'].replace(not in ['Y', 'N'], np.NaN, inplace = True)
    df['Fatal (Y/N)'].replace('F', 'Y', inplace = True)
    df['Fatal (Y/N)'] = df['Fatal (Y/N)'].apply(lambda s: str(s).upper())
    return df

def normalize_sex(df):
    pass

def normalize_date(df):
    # Esta no me gusta. df['Date'].replace(str.lower().startswith('reported '), '', inplace = True)
    # Elimar 'Reported' mediante regex
    df['Date'].str.replace('[Rr]eported\s*', '', regex=True)
    df['Date'].to_datetime()
    return df



# coding: utf-8

# In[ ]:


def obtain_countries_with_more_shark_attacks(clean_data):

    """
    Return the top 5 countries of shark attacks:
    top5 is a dataframe with absolute figures.
    top5_porcentage is a dataframe with porcentages.
    """
    top5 = clean_data['Country'].value_counts().head(6)
    #top5_porcentage = ((df['Country'].value_counts() / len(df['Country'])) * 100).head(6)
    #top5_attacks = clean_data[clean_data['Country',(clean_data['Country'] / len(clean_data['Country']) * 100].value_counts().head(6)
    return top5

def obtain_countries_with_more_fatal_attacks(clean_data):
    top5_fatal = clean_data['Country'][clean_data['Fatal (Y/N)'] == 'Y'].value_counts().head(6)
    #group = clean_data.groupby(by='Country')
    #group['Fatal (Y/N)'] == 'Y']
    return top5_fatal


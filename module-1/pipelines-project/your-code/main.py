
# coding: utf-8

# In[ ]:


import extract_file, transform_file, analize_file



def acquire():
    df = extract_file.extract('GSAF5.csv')
    return df

def wrangle(data):
    clean_data = transform_file.erase_column_space(data)
    # clean_data = transform_file.erase_space(clean_data) REVISAR FUNCIÓN
    clean_data = transform_file.erase_columns_with_nulls(clean_data)
    clean_data = transform_file.normalize_fatalfield(clean_data)
    #clean_data = transform_file.normalize_sex(clean_data) REVISAR FUNCIÓN
    # clean_data = transform_file.normalize_date(clean_data) REVISAR FUNCIÓN
    return clean_data

def analyze(data):
    top5 = analize_file.obtain_countries_with_more_shark_attacks(data)
    top5_fatal = analize_file.obtain_countries_with_more_fatal_attacks(data)
    return top5, top5_fatal

def visualize_analysis(*args):
    for arg in args:
        print(arg)
        print()

def load(csv_name):
    csv_name.to_csv("GSAF5_cleaned.csv")
    


def main():
    df = acquire()
    clean_df = wrangle(df)
    top5, top5_fatal = analyze(clean_df)
    visualize_analysis(top5, top5_fatal)
    load(clean_df)
    
    
if __name__ == "__main__":
    main()


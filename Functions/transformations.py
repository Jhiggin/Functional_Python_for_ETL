import pandas as pd

def split_columns(dataset, original_col, split_field):
    df = dataset[original_col].str.split(split_field, expand=True)
    return df 

def transform_state(dataset1, dataset2, join_column, join_method):
    df = pd.merge(dataset1, dataset2, on=join_column, how=join_method)
    return df
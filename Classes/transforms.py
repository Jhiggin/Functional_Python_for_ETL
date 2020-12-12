import pandas as pd

class transforms:

    def __init__(self, dataset, param0 = '', param1 = '', param2 = ''):
        self.dataset = dataset
        self.param0 = param0
        self.param1 = param1
        self.param2 = param2


    def split_columns(self):
        df = self.dataset[self.param0].str.split(self.param1, expand=True)
        return df 

    def transform_state(self):
        df = pd.merge(self.dataset, self.param0, on=self.param1, how='inner')
        return df

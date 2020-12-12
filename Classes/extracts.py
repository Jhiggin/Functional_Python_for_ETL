import pandas as pd

class extracts:

    def __init__(self, datasource):
        self.datasource = datasource

    def read_csv_file(self):
        df = pd.read_csv(filepath_or_buffer = self.datasource)
        return df

    def read_excel_file(self):
        df = pd.read_excel(io = self.datasource) 
        return df  
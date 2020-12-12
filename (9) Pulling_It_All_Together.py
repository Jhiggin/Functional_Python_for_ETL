from pandas.io.parsers import read_csv
from Functions.file_processes import *
from Functions.sql_processes import *
from Functions.transformations import *

import pandas as pd
import configparser

# Load Config
config = configparser.ConfigParser()
config.read('Config/config.ini')

# Initialize variables
extract_path = config['Production']['extract_path']
statecode_path = config['Production']['statecode_path']
output_path = config['Production']['output_path'] 

# Read file from directory
df = read_csv(extract_path)

# Split the key column based off the / character
df2 = split_columns(df, 'key', '/')

# Rename the columns created by the split
df2.rename(columns = {0:'Country_Code', 1:'State_Nbr', 2:'City', 3:'Street_Address'}, inplace = True)

# Merge the df and df2 dataframes
results = pd.merge(df, df2, left_index=True, right_index=True)

# Convert the data type of the state_nbr column to numeric
results['State_Nbr'] = pd.to_numeric(results['State_Nbr'])

# Read the state code list for validating the data
state_codes = read_csv(statecode_path)

# Join the results and state_code dataframes together to gather full state info
final = transform_state(results, state_codes, 'State_Nbr', 'inner')

# Write final results to dataframe
write_to_csv(final, output_path + 'breweries_scrubbed.csv')


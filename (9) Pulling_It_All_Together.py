from pandas.io.parsers import read_csv
from Functions.file_processes import *
from Functions.sql_processes import *
from Functions.transformations import *

import pandas as pd
import configparser
from datetime import datetime

# Load Config
config = configparser.ConfigParser()
config.read('Config/config.ini')

# Initialize variables
input_path = config['Production']['input_path']
statecode_path = config['Production']['statecode_path']
output_path = config['Production']['output_path']
conn_string = config['Production']['conn_string']

# Read file from directory
df_brew = read_csv(input_path)

# Split the key column based off the / character
key_split = split_columns(df_brew, 'key', '/')

# Rename the columns created by the split
key_split.rename(columns={0: 'Country_Code', 1: 'State_Nbr',
                          2: 'City', 3: 'Street_Address'}, inplace=True)

# Convert key_split to dataframe
df_key = pd.DataFrame(key_split)

# Drop columns that are not needed
df_key.drop([4, 5, 6], axis=1, inplace=True)

# Merge the df and df2 dataframes
results = pd.merge(df_brew, df_key, left_index=True, right_index=True)

# Convert the data type of the state_nbr column to numeric
results['State_Nbr'] = pd.to_numeric(results['State_Nbr'])

# Read the state code list for validating the data
state_codes = read_csv(statecode_path)

# Join the results and state_code dataframes together to gather full state info
final = transform_state(results, state_codes, 'State_Nbr', 'inner')

final['Import_Date'] = datetime.now()

# Remove columns not needed now that join has occurred
final.drop(['key', 'State_Nbr', 'lat', 'long', 'State'], axis=1, inplace=True)

# Rename the columns of the dataframe
final.rename(columns={'categories': 'Brewery_Category', 'name': 'Brewery_Name',
                      'phones': 'Phone_Number', 'postalCode': 'Zip_Code',
                      'websites': 'Brewery_Website', 'State_Code': 'State', 'Country_Code': 'Country'}, inplace=True)

# Produce final organized dataframe
final = final[['Brewery_Name', 'Brewery_Category', 'Brewery_Website',
              'Phone_Number', 'Street_Address', 'City', 'State', 'Country', 'Import_Date']]

# Write final results to dataframe
write_to_csv(final, output_path + 'breweries_scrubbed.csv')

# Write final to SQL Server
write_sql(final, 'Breweries', conn_string)


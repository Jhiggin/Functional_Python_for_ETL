import pandas as pd
import configparser
import numpy as np
import os
from classes.transformations import *

# Load Config
config_file = os.path.join(os.path.dirname(__file__), 'Config/config.ini')
config = configparser.ConfigParser()
config.read(config_file)

# Initialize variables
input_path = os.path.join(os.path.dirname(__file__), config['Production']['input_path'])
output_path = os.path.join(os.path.dirname(__file__), config['Production']['output_path'])
conn_string = config['Production']['conn_string']

# Load csv file to dataframe for processing
df = pd.read_csv(input_path)

# Clean up Status column
df['Status_Rocket'] = df['Status_Rocket'].replace(['StatusActive', 'StatusRetired'],['Active', 'Retired'])

# Split the location column into indivdual location columns
df[['Site','City', 'State', 'Country']] = df.Location.str.split(",", expand=True)

# Due to US based Location format being differnt than non-US, backfill nan rows with state field
df.Country.fillna(df.State, inplace=True)

# Backfill state with nan for non-US based rows
df.loc[df["Country"] != ' USA', "State"] = np.nan

# Split detail column
df[['RocketType','PayLoad']] = df.Detail.str.split("|", expand=True)

# Rename the columns of the dataframe
df.rename(columns={'Rocket': 'Rocket_Cost'}, inplace=True)

# Drop unecessary columns from dataframe
df.drop(['Location', 'Detail'], axis=1, inplace=True)

df.to_csv(output_path + 'rocket_data.csv', index=False)



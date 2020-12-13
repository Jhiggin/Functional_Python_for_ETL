from Queries.adw_queries import *
from Functions.sql_processes import *
from Functions.file_processes import *

import pandas as pd 
import sys 
import configparser
import os

# extract_name = sys.argv[1] # Passed in through SQL Agent Job
extract_name = 'test.xlsx'

# Load Config
config_file = os.path.join(os.path.dirname(__file__), 'Config/config.ini')
config = configparser.ConfigParser()
config.read(config_file)

# Initialize Variables
eng_conn = config['Dev']['conn_string']
extract_path = os.path.join(os.path.dirname(__file__),config['Dev']['extract_path'])

salesDF = read_sql(factsales_query, eng_conn)

write_to_excel(salesDF, extract_path + extract_name)
import pyodbc as sql
import pandas as pd
import sqlalchemy as sa

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.expression import insert, update, delete
from datetime import date

class error_handling:

    def __init__(self, exception, display, notify, log, connection_string):
        self.exception = exception
        self.display = display
        self.notify = notify
        self.log = log
        self.connection_string = connection_string

    def _err(exception, display, notify, log, connection_string):    
        if (log == 'True'):
            print('logging it')
        else:
            print('Not logging it')

        if (notify == 'True'):
            print('Error Message sent to email')
        else:
            print('Not sending an email')

        if (display == 'True'):
            print('Sending to console')
        else:
            print('Not sending to console')


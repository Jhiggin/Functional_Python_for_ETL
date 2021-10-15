import pyodbc as sql
import pandas as pd
import sqlalchemy as sa

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.expression import insert, update, delete
from datetime import date

from sqlalchemy.sql.operators import comma_op    
    
def read_sql(query, conn):
    engine = sa.create_engine(conn)
    connection = engine.connect()
    df = pd.read_sql_query(
         sql=query, con=conn
    )
    return df

def write_sql(dataset, table, conn):
     engine = sa.create_engine(conn)
     connection = engine.connect()
     dataset.to_sql(name = table, con = connection, if_exists = 'append', index = False)
     return

def log_to_sql(opName, table, message, recordsInserted, status, conn):
     metadate = MetaData()
     log_table = Table(
     "FileImportLog",
     metadate,
     # Column('RecordID', Integer, primary_key=True),
     Column('Operation', String(250)),
     Column('StatusCode', Integer),
     Column('RecordCount', Integer),
     Column('Message_Text', String(3000))
     )
     engine = sa.create_engine(conn)
     connection = engine.connect()
     stmt = insert(log_table).values(Operation=opName, StatusCode=status, RecordCount=recordsInserted, Message_Text=message)
     connection.execute(stmt)

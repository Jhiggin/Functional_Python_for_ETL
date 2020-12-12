import pyodbc as sql
import pandas as pd
import sqlalchemy as sa

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.expression import insert, update, delete
from datetime import date    
    
def read_sql(query, conn):
    engine = sa.create_engine(conn)
    connection = engine.connect()
    df = pd.read_sql_query(
         sql=query, con=conn
    )
    return df
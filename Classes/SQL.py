import pyodbc as sql
import pandas as pd
import sqlalchemy as sa

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, Boolean
from sqlalchemy.sql.expression import insert, update, delete
from datetime import date


class SQL:

    def __init__(self, query, conn):
        self.query = query
        self.conn = conn

    def create_connection(self):
        engine = sa.create_engine(self.conn)
        connection = engine.connect()
        return connection

    def read_sql(self):
        df = pd.read_sql_query(
            sql=self.query, con=self.conn
        )
        return df
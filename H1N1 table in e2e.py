#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 20:30:58 2021

@author: cindy
"""

!pip install pymysql
# Packages for SQL CONNECTION
from sqlalchemy import create_engine
import sqlalchemy
import pandas as pd

MYSQL_HOSTNAME = '20.127.8.44'
MYSQL_USER = 'dba'
MYSQL_PASSWORD = 'ahi2021'
MYSQL_DATABASE = 'e2e'


connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
engine = create_engine(connection_string)

print (engine.table_names())

csvfile = pd.read_csv('https://raw.githubusercontent.com/cindym02/E2E-Final-Assignment/main/H1N1_Flu_Vaccines.csv')
csvfile.to_sql('H1N1_Flu_Vaccines', con=engine, if_exists='append')









# End to End E2E Final Assignment How-To Guide
 
# Create a mysql user that can access all databases on that mysql installation called ‘DBA’ with password ‘ahi2021’
#CREATE USER ‘dba'@'%' IDENTIFIED BY ‘ahi2021’;
#GRANT ALL PRIVILEGES ON *.* TO 'dba'@'%' WITH GRANT OPTION;

# Create a new database called ‘e2e'
#create database e2e;
 
# Create a new table called ‘h1n1’ that lives within the ‘e2e’ database
!pip install pymysql
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

# Create a dump (.sql) file
sudo mysqldump e2e > database_dump.sql

# Using the SCP command from your terminal, move that file to your own local computer.
scp database_dump.sql cindy504@20.127.8.44:/home/cindy504

# Create a trigger
#delimiter $$
#CREATE TRIGGER h1n1_concern_trigger BEFORE INSERT ON H1N1_Flu_Vaccines
FOR EACH ROW
BEGIN
	 IF NEW.h1n1_concern >= 3 THEN
	  	SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'ERROR: H1N1 concern should be a numerical value between 0 and 3. Please try again';
	 END IF;
END; $$
delimiter ;

 
 
 
 
 
 
 
 
 
 
 

 

import mysql.connector as myconnect
from mysql.connector import Error

# create my sql connection
def connect(database= None):
    try:
        connection = myconnect.connect(host = 'localhost', password = 'Password@3103', user = 'root', database = database)
        print('connection successful')
    except Error:
        print(Error)
        print('Connection not successful')
    return connection
    
connection = connect()


# create mysql cursor
def connectcursor(query, connection = connection):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print('query executed')
        connection.commit()
        cursor.close()
    except Error:
        print(Error)

# create mysql database
query = 'create database UserData;'

connectcursor(query)

# use cursor to create table and columns to database 
dataconnect = connect(database = 'UserData')

def createtable(connection = dataconnect):
    query = '''create table User_info(
        id int primary key auto_increment,
        first_name varchar(100),
        middle_name varchar(100),
        last_name varchar(100), 
        age int,
        country varchar(12),
        phone varchar(11),
        about_life Text,
        Date_of_birth date,
        course varchar(19),
        registrationtime timestamp default current_timestamp);
        '''
    
    connectcursor(query = query, connection = dataconnect)

createtable()
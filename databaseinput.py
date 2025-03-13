# import libraries
import mysql.connector as myconnect
# insert values into the table
    
    
def insertdata(first_name, middle_name, last_name, age, country, phone, about_life, Date_of_birth, course):
    connection = myconnect.connect(host = 'localhost', password = 'Password@3103', user = 'root', database = 'UserData')

    cursor = connection.cursor()
    query = ''' insert into user_info (first_name, middle_name, last_name, age, country, phone, about_life, Date_of_birth, course)
        values(%s, %s, %s, %s, %s, %s, %s, %s, %s)'''
        
    cursor.execute(query, (first_name, middle_name, last_name, age, country, phone, about_life, Date_of_birth, course))
    
    connection.commit()
    cursor.close()
    connection.close()
    
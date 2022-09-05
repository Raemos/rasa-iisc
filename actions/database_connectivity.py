import mysql.connector

def NameUpdate(Name): 

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",  
        passwd="",
        database="rasa_slot") 
    mycursor = mydb.cursor() 
    sql='INSERT INTO slot (name) VALUES ("{0}");'.format(Name) 
    mycursor.execute(sql) 
    mydb.commit()
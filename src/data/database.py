import mysql.connector

class Database:

    def initSchema(self):
        conn = mysql.connector.connect(host="localhost",user="python",passwd="1234")
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS asmp;")
        conn.close()


    def executeNonQuery(self,query):
        conn = mysql.connector.connect(host="localhost",user="python",passwd="1234")
        cursor = conn.cursor()
        cursor.execute(query)
        conn.close()

db = Database()
db.initSchema()
    #opzetten data model
    # inschieten van meet record
    # ophalen van data

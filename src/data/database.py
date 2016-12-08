import mysql.connector
import os

class Database:

    def initSchema(self):
        initSriptFilePath = os.path.dirname(os.path.abspath(__file__))
        file = open(initSriptFilePath + "\init_schema.sql","r")
        self.executeNonQuery(file.read(), None)

    def executeNonQuery(self,query, database = "asmp"):
        if database is None:
            conn = mysql.connector.connect(host="localhost",user="python",passwd="1234")
        else:
            conn = mysql.connector.connect(host="localhost",user="python",passwd="1234")
            
        cursor = conn.cursor()
        cursor.execute(query)
        conn.close()

db = Database()
db.initSchema()
    #opzetten data model
    # inschieten van meet record
    # ophalen van data

import mysql.connector
import os

class Database:

    def initSchema(self):
        self.executeNonQuery("init_schema.sql", None)

    def insertMeasurement(self, measureMent):
        self.executeNonQuery("inset_measurement.sql", )
        
    def executeNonQuery(self, queryFile, database = "asmp"):
        initSriptFilePath = os.path.dirname(os.path.abspath(__file__))
        file = open(initSriptFilePath + "\\"+ queryFile ,"r")
        statements = file.read().split(";")

        conn = self.createConnection(database)
        cursor = conn.cursor()

        for statement in statements:
            cursor.execute(statement)

        conn.close()

    def createConnection(self, database = "asmp"):
        host = "localhost"
        user = "python"
        password = "1234"

        if database is None:
            return mysql.connector.connect(host=host,user=user,passwd=password)
        else:
            return mysql.connector.connect(host=host,user=user,passwd=password,database=database)
           

db = Database()
db.initSchema()
print("Klaar .. ")
    #opzetten data model
    # inschieten van meet record
    # ophalen van data

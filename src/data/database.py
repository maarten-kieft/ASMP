import mysql.connector
import os

class Database:

    def initSchema(self):
        self.executeNonQuery("init_schema.sql",None, None)

    def insertMeasurement(self, measurement):
        self.executeNonQuery("insert_measurement.sql", measurement)
        
    def executeNonQuery(self, queryFile, parameters, database = "asmp"):
        initSriptFilePath = os.path.dirname(os.path.abspath(__file__))
        file = open(initSriptFilePath + "\\"+ queryFile ,"r")
        statements = file.read().split(";")

        conn = self.createConnection(database)
        cursor = conn.cursor()

        for statement in statements:
            cursor.execute(statement.format(**parameters))

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
#db.initSchema()
m = {
    "return_total_normal": "0.50"
}


db.insertMeasurement(m)

print("Klaar .. ")
    #opzetten data model
    # inschieten van meet record
    # ophalen van data

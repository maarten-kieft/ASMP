import mysql.connector
import os

class Database:
    def initSchema(self):
        self.executeNonQuery("init_schema.sql",None, None)

    def insertMeasurement(self, measurement):
        self.executeNonQuery("insert_measurement.sql", measurement)
        
    def executeNonQuery(self, queryFile, parameters, database = "asmp"):
        statementFilePath = os.path.dirname(os.path.abspath(__file__))
        statementFile = open(statementFilePath + "\\"+ queryFile ,"r")
        statements = statementFile.read().split(";")
        conn = self.createConnection(database)
        cursor = conn.cursor()

        for statement in statements:
            if parameters is None:
                preparedStatement = statement
            else:
                preparedStatement = statement.format(**parameters)

            cursor.execute(preparedStatement)
            
        conn.commit()   
        conn.close()

    def createConnection(self, database = "asmp"):
        host = "localhost"
        user = "python"
        password = "1234"

        if database is None:
            return mysql.connector.connect(host=host,user=user,passwd=password)
        else:
            return mysql.connector.connect(host=host,user=user,passwd=password,database=database)

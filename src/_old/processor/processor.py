import serial
from time import sleep
from processor.interpreter import Interpreter
from processor.connector import Connector

class Processor:
    running = True 
    interpreter = Interpreter()
    connector = Connector()
    database = None

    def __init__(self, database):
        self.database = database
    
    def start(self):
        connection = self.connector.createConnection()
         
        print("Connecting")
        connection.open()
        
        print("Listening")
        self.listen(connection)
       
        print("Clossing connection")
        connection.close()

    
    def listen(self, connection):
        message = []
       
        while self.running:
            line = str(connection.readline().decode("utf-8")).strip()

            if len(line) == 0:
                continue
            
            if line[0] == "!":
                measurement = self.interpreter.interpretMessage(message)
                self.database.insertMeasurement(measurement)
                message = []
            else:
                message.append(line)

    def stop(self):
        self.running = False
        print("Stopping..")

import serial
from time import sleep
from interpreter import Interpreter
from connector import Connector
#from data.database import database

class Processor:
    running = True 
    interpreter = Interpreter()
    connector = Connector()
    
    def start(self):
        connection = self.createConnection()
         
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
                interpreter.interpretMessage(message)
                message = []
            else:
                message.append(line)

    def stop(self):
        self.running = False
        print("Stopping..")

    

message = ["1-0:1.8.1(000060.140*kWh)"]

Processor().interpreter.interpretMessage(message)

#processor = Processor().start()

#line
#processor.start()
#processor.stop()
#determine the right parser
#parse the message and return a measurement object
#store the measurement object in the database

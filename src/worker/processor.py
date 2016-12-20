import serial
from time import sleep
from worker.interpreter import Interpreter
from worker.connector import Connector
from web.models import MeterMeasurement

class Processor:
    running = True 
    interpreter = Interpreter()
    connector = Connector()

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
                #todo: convert dictionary to MeterMeasurement object, so we can use the new api
                #meterMeasurement = MeterMeasurement(usage_current = measurement["usage_current"])
              
                meterMeasurement.save()
                message = []
            else:
                message.append(line)

    def stop(self):
        self.running = False
        print("Stopping..")

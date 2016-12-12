import serial
import re
from time import sleep

class Processor:
    running = True 
    
    def start(self):
        connection = self.createConnection()
         
        print("Connecting")
        connection.open()
        
        print("Listening")
        self.listen(connection)
       
        print("Clossing connection")
        connection.close()

    def createConnection(self):
        connection = serial.Serial()
        connection.baudrate = 115200
        connection.bytesize=serial.EIGHTBITS
        connection.parity=serial.PARITY_NONE
        connection.stopbits=serial.STOPBITS_ONE
        connection.xonxoff=0
        connection.rtscts=0
        connection.timeout=1
        #connection.port="/dev/ttyUSB0"
        connection.port="COM3"

        return connection

    def listen(self, connection):
        message = []
       
        while self.running:
            line = str(connection.readline().decode("utf-8")).strip()

            if len(line) == 0:
                continue
            
            if line[0] == "!":
                self.interpretMessage(message)
                message = []
            else:
                message.append(line)

    def stop(self):
        self.running = False
        print("Stopping..")

    def interpretMessage(self, message):
        print("Interpreting message")
        measurement = {}

        
        for i, line in enumerate(message):
            lineNodes = self.parseLine(line)
            key = self.interpretLineKey(lineNodes[0])       
            value = self.interpretLineValue(lineNodes[1])

            if key is not None:
                measurement[key] = value
                print(key)
                print(value)
                                       
    def parseLine(self, line):
        print(line)

        pattern = re.compile("^([^\(]*)\(([^\)]*)\)$")
        line = "1-0:1.8.1(000060.140*kWh)"
        match = pattern.match(line)

        return (match.group(1),match.group(2))

    def interpretLineKey(self, keyNode):
        keyDictionary = {
            "0-0:96.1.1" : "meterId",
            "1-0:1.8.1" : "usage_low",
            "1-0:1.8.2" : "usage_normal",
            "1-0:2.8.1" : "return_low",
            "1-0:2.8.2" : "return_normal",
            "0-0:96.14.0" : "current_tarrif",
            "1-0:1.7.0" : "current_usage",
            "1-0:2.7.0" : "current_return"
        }

        return keyDictionary.get(keyNode,None)


    def interpretLineValue(self, valueNode):
        return valueNode


message = ["1-0:1.8.1(000060.140*kWh)"]

Processor().interpretMessage(message)

#processor = Processor().start()

#line
#processor.start()
#processor.stop()
#determine the right parser
#parse the message and return a measurement object
#store the measurement object in the database

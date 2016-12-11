import serial
from time import sleep

class Processor:
    running = True 
    
    def start(self):
        connection = self.createConnection()
         
        print("connecting")
        connection.open()
        
        print("listening")
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
            #print("ik heb een lijn")
            #print(line)
            if len(line) == 0:
                continue
            
            if line[0] == "!":
                self.parse(message)
                message = []
            else:
                message.append(line)

    def stop(self):
        self.running = False
        print("Stopping..")

    def parse(self, message):
        print("Parsing message")

        file = open("result.txt","w")

        for i, line in enumerate(message):
            print(i, line)
            file.write(line+"\n")

        file.close()


processor = Processor().start()

#line
#processor.start()
#processor.stop()
#determine the right parser
#parse the message and return a measurement object
#store the measurement object in the database

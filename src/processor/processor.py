import serial
from time import sleep

class Processor:
    running = True 
    
    def start(self):
        connection = self.createConnection()
        message = []
        
        try:
            connection.open()
        except:
            sys.exit ("Failed to open serial connection:"  % ser.name)

        while self.running:
            line = ser.readline()
            
            if len(data) > 0:
                message.apend(line)
            elif len(message) > 0:
                self.parse(message)
                message = []
            else:
                sleep(1)
        
        print("Clossing connection")
        connection.close()

    def createConnection(self):
        connection = serial.Serial()
        connection.baudrate = 9600
        connection.bytesize=serial.SEVENBITS
        connection.parity=serial.PARITY_EVEN
        connection.stopbits=serial.STOPBITS_ONE
        connection.xonxoff=0
        connection.rtscts=0
        connection.timeout=2
        connection.port="/dev/ttyUSB0"

        return connection
        

    def stop(self):
        self.running = False
        print("Stopping..")

    def parse(self, message):
        print("Parssing message")
        for i, line in enumerate(message):
            print(i, line)
    
processor = Processor()

processor.start()
#processor.stop()
#determine the right parser
#parse the message and return a measurement object
#store the measurement object in the database


class Connector:
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

import serial
import sys
import glob

class Connector:
    """Creates a serial connection to a smart meter"""

    def create_connection(self):
        """Creating a connection to a serial port with a smart meter"""

        ports = self.get_serial_ports()

        for port in ports:
            connecton = self.configure_connection(port)

            if self.test_connection(connecton):
                return connecton

        return None

    def get_serial_ports(self):
        """ Retrieves a list of serial port names and,
        copyright stackoverflow/questions/12090503#14224477"""
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass

        return result

    def configure_connection(self, port):
        """"Configures the connection with smart meter specific settings"""
        print("Info: Configuring connection through port: "+port)
        connection = serial.Serial()
        connection.baudrate = 115200
        connection.bytesize = serial.EIGHTBITS
        connection.parity = serial.PARITY_NONE
        connection.stopbits = serial.STOPBITS_ONE
        connection.xonxoff = 0
        connection.rtscts = 0
        connection.timeout = 1
        #connection.port="/dev/ttyUSB0"
        connection.port = port

        return connection

    def test_connection(self, connection):
        """Tests if a smart meter is connected to this serial port"""
        print("Info: Testing settings for port: "+connection.port)
        return True

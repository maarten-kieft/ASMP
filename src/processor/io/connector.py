import sys
import glob
import serial
import time;
from core.services.messageservice import MessageService

class Connector:
    """Creates a serial connection to a smart meter"""

    def acquire_connection(self):
        connection = None
       
        while connection is None:
            MessageService.log("processor","warning","Couldn't connect, sleeping 10 secs and retrying")
            time.sleep(10)
            connection = self.create_connection()

        return connection

    def create_connection(self):
        """Creating a connection to a serial port with a smart meter"""

        ports = self.get_serial_ports()
        MessageService.log("processor","info","Number of ports found: "+str(len(ports)))
        
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
            ports = glob.glob('/dev/tty[A-Za-z0-9]*')
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
        MessageService.log("processor","info","Configuring connection through port: "+port)
        connection = serial.Serial()
        connection.baudrate = 115200
        connection.bytesize = serial.EIGHTBITS
        connection.parity = serial.PARITY_NONE
        connection.stopbits = serial.STOPBITS_ONE
        connection.xonxoff = 0
        connection.rtscts = 0
        connection.timeout = 1
        connection.port = port

        return connection

    def test_connection(self, connection):
        """Tests if a smart meter is connected to this serial port"""
        MessageService.log("processor","info","Testing settings for port: "+connection.port)
        i = 0
        
        try:
            connection.open()
            while i < 20:
                i += 1
                line = str(connection.readline().decode("utf-8")).strip()

                if len(line) > 0:
                    MessageService.log("processor","info","Test ok!"+connection.port)
                    return True
        except:
            print("swallow exception, conclusion is the same, testing failed")        
        finally:
            connection.close()  

        MessageService.log("processor","info","Test failed"+connection.port)
        return False
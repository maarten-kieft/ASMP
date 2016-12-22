import serial
from time import sleep
from worker.parser import Parser
from worker.connector import Connector
from web.models import Meter, MeterMeasurement

class Processor:
    running = True 
    parser = Parser()
    connector = Connector()

    def start(self):
        connection = self.connector.createConnection()



        message = [
            "/KFM5KAIFA-METER",
            "1-3:0.2.8(42(4)",
            "0-0:1.0.0(161211191412W)",
            "0-0:96.1.1(4530303237303030358130313334353142)",
            "1-0:1.8.1(000060.140*kWh)",
            "1-0:1.8.2(000076.832*kWh)",
            "1-0:2.8.1(000000.000*kWh)",
            "1-0:2.8.2(000000.000*kWh)",
            "0-0:96.14.0(0001)",
            "1-0:1.7.0(00.577*kW)",
            "1-0:2.7.0(00.000*kW)",
            "0-0:96.7.21(00001)",
            "0-0:96.7.9(00001)",
            "1-0:99.97.0(1)(0-0:96.7.19)(000101000001W)(2147483647*s)",
            "1-0:32.32.0(00000)",
            "1-0:32.36.0(00000)",
            "0-0:96.13.1()",
            "0-0:96.13.0()",
            "1-0:31.7.0(002*A)",
            "1-0:21.7.0(00.580*kW)",
            "1-0:22.7.0(00.000*kW)"
        ]

        parsed_message = self.parser.parse_message(message)
        

        measurement = MeterMeasurement(**parsed_message)
        #measurement.meter = Meter.objects.get_or_create(name=parsed_message["meter_name"])[0]

        measurement.save()

        print("Done!")
        return



        #print("Connecting")
        #connection.open()

        #print("Listening")
        #self.listen(connection)

        #print("Clossing connection")
        #connection.close()

    
    def listen(self, connection):
        message = []
       
        while self.running:
            line = str(connection.readline().decode("utf-8")).strip()

            if len(line) == 0:
                continue
            
            if line[0] == "!":
                result = self.interpreter.interpret_message(message)
               
                result.measurement.save()
                message = []
            else:
                message.append(line)

    def stop(self):
        self.running = False
        print("Stopping..")

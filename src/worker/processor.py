"""Processing, intterpreting and storing serial messages"""
from datetime import datetime
import pytz
from worker.parser import Parser
from worker.connector import Connector
from web.models import Meter, MeterMeasurement

class Processor:
    """"Class responsible for listening for serial messages, interpreting and storing them"""
    running = True
    parser = Parser()
    connector = Connector()

    def start(self):
        """Starting the processor to listen for message, interpret and store them"""
        connection = self.connector.createConnection()

        print("Connecting")
        connection.open()

        print("Listening")
        self.listen(connection)

        print("Clossing connection")
        connection.close()

    def listen(self, connection):
        """Listen for serial messages, interpret them and store them"""
        message = []

        while self.running:
            line = str(connection.readline().decode("utf-8")).strip()

            if len(line) == 0:
                continue

            if line[0] == "!":
                parsed_message = self.parser.parse_message(message)
                measurement = self.interpret_message(parsed_message)
                measurement.save()

                message = []
            else:
                message.append(line)

    def interpret_message(self, parsed_message):
        """Interpret the parsed message"""
        meter = Meter.objects.get_or_create(name=parsed_message["meter_name"])[0]

        del parsed_message["meter_name"]
        measurement = MeterMeasurement(**parsed_message)
        measurement.meter = meter
        measurement.timestamp = datetime.now(pytz.utc)

        return measurement

    def stop(self):
        """Stopping the processor"""
        self.running = False
        print("Stopping..")

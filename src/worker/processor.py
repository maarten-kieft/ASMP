"""Processing, intterpreting and storing serial messages"""
from datetime import datetime
import pytz
import time
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

        print("Connecting")
        connection = self.connector.create_connection()

        while connection is None:
            print("Warning: Wasn't able to obtain a connection, sleeping for 10 secs and retrying")
            time.sleep(10)
            connection = self.connector.create_connection()

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
                self.process_message(message)
                message = []
            else:
                message.append(line)

    def process_message(self, message):
        """Processes a received message"""
        parsed_message = self.parser.parse_message(message)

        if self.is_valid_message(parsed_message):
            measurement = self.interpret_message(parsed_message)
            measurement.save()

    def is_valid_message(self, parsed_message):
        """Checks if the parsed message is complete"""

        return "meter_name" in parsed_message

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

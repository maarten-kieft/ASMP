from core.services.messageservice import MessageService
from core.services.measurementservice import MeasurementService
from processor.parser import Parser
from processor.connector import Connector

class Processor:
    """"Class responsible for listening for serial messages, interpreting and storing them"""
    running = True
    parser = Parser()
    connector = Connector()
    connection_initialized = False

    def start(self):
        """Starting the processor to listen for message, interpret and store them"""

        MessageService.log("processor","info","Connecting..")
        connection = self.connector.acquire_connection()
        connection.open()

        MessageService.log("processor","info","Connected")
        self.listen(connection)

        MessageService.log("processor","info","Closing connection")
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
        #skipping the first message, it seems to be competely broken
        if self.connection_initialized:
            parsed_message = self.parser.parse(message)
            MeasurementService.save_measurement(parsed_message)

        self.connection_initialized = True

    def is_valid_message(self, parsed_message):
        """Checks if the parsed message is complete"""

        return "meter_name" in parsed_message

    def stop(self):
        """Stopping the processor"""
        self.running = False
        print("Processor: Stopping..")

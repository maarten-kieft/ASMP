from core.services.measurementservice import MeasurementService
from core.services.logservice import LogService
from core.service.applicationservice import ApplicationService
from processor.io.connector import Connector
from processor.parsing.parser import Parser

class Processor:
    """"Class responsible for listening for serial messages, interpreting and storing them"""
    running = True
    parser = Parser()
    connector = Connector()
    connection_initialized = False
    message_format_saved = False

    def start(self):
        """Starting the processor to listen for message, interpret and store them"""

        LogService.log("processor", "info", "Connecting..")
        connection = self.connector.acquire_connection()
        connection.open()

        LogService.log("processor", "info", "Connected")
        self.listen(connection)

        LogService.log("processor", "info", "Closing connection")
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
            LogService.log_debug("processor","received new message:")

            if(self.message_format_saved == False):
                ApplicationService.save_meter_message_format(message)
                self.message_format_saved = True

            for line in message:
                LogService.log_debug("Processor",line)

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

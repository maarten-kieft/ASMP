import re
from decimal import Decimal
from datetime import datetime
from web.models import MeterMeasurement, Meter

class Interpreter:
    """Interpetes messages coming from the meter"""

    def interpret_message(self, message):
        """Inteprets the message from the meter into a readable format"""
        print("Interpreting message")
        message_dictionary = {}

        for line in message:
            line_nodes = self.parse_line(line)

            if line_nodes is None:
                continue

            key = self.interpret_line_key(line_nodes[0])
            value = self.interpret_line_value(key, line_nodes[1])

            if key is not None:
                print(key)
                message_dictionary[key] = value

        return self.create_measurement(message_dictionary)

    def create_measurement(self, message_dictionary):
        """Converts the names and values into a measurement object"""
        measurement = MeterMeasurement()
        measurement.timestamp = datetime.now()
        measurement.usage_current = message_dictionary["usage_current"]
        measurement.usage_total_low = message_dictionary["usage_total_low"]
        measurement.usage_total_normal = message_dictionary["usage_total_normal"]
        measurement.return_current = message_dictionary["return_current"]
        measurement.return_total_low = message_dictionary["return_total_low"]
        measurement.return_total_normal = message_dictionary["return_total_normal"]

        meter = Meter()
        meter.name = message_dictionary["meter_name"]

        return {meter: meter, measurement : measurement}

    def parse_line(self, line):
        """Parses the line into a key and value"""
        pattern = re.compile("^([^\(]*)\(([^\)]*)\)$")
        match = pattern.match(line)

        if match is None:
            return None

        return (match.group(1), match.group(2))

    def interpret_line_key(self, key_node):
        """Interprets the key of the line"""
        key_dictionary = {
            "0-0:96.1.1" : "meter_name",
            "1-0:1.8.1" : "usage_total_low",
            "1-0:1.8.2" : "usage_total_normal",
            "1-0:2.8.1" : "return_total_low",
            "1-0:2.8.2" : "return_total_normal",
            "0-0:96.14.0" : "current_tarrif",
            "1-0:1.7.0" : "usage_current",
            "1-0:2.7.0" : "return_current"
        }

        return key_dictionary.get(key_node, None)

    def interpret_line_value(self, key, value_node):
        """Interprets the value of the line"""
        if key is not None and ("usage_" in key or "return_" in key):
            return Decimal(value_node.replace("*kWh", "").replace("*kW", ""))

        return value_node

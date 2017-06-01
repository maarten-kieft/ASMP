import re
from decimal import Decimal
from datetime import datetime
from django.utils import timezone

class Parser:
    """Interpetes messages coming from the meter"""

    def parse_message(self, message):
        """Inteprets the message from the meter into a readable format"""
        print("Interpreting message")
        parsed_message = {}

        for line in message:
            line_nodes = self.parse_line(line)

            if line_nodes is None:
                continue

            key = self.parse_line_key(line_nodes[0])

            if key is not None:
                value = self.parse_line_value(key, line_nodes[1])
                parsed_message[key] = value

        return parsed_message

    def parse_line(self, line):
        """Parses the line into a key and value"""
        pattern = re.compile("^([^\(]*)\(([^\)]*)\)$")
        match = pattern.match(line)

        if match is None:
            return None

        return (match.group(1), match.group(2))

    def parse_line_key(self, key_node):
        """Interprets the key of the line"""
        key_dictionary = {
            "0-0:96.1.1" : "meter_name",
            "1-0:1.8.1" : "usage_total_low",
            "1-0:1.8.2" : "usage_total_normal",
            "1-0:2.8.1" : "return_total_low",
            "1-0:2.8.2" : "return_total_normal",
            "1-0:1.7.0" : "usage_current",
            "1-0:2.7.0" : "return_current"
        }

        return key_dictionary.get(key_node, None)

    def parse_line_value(self, key, value_node):
        """Interprets the value of the line"""
        value_node = value_node.replace("*kWh", "").replace("*kW", "")

        if key is not None and ("usage_" in key or "return_" in key):
            return Decimal(value_node)

        return value_node

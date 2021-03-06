import re
from decimal import Decimal

class Parser:
    """Interpetes messages coming from the meter"""

    def parse(self, message):
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
        pattern = re.compile("^([^\(]*)(\([^\)]*\))*\(([^\)]*)\)$")
        match = pattern.match(line)
       
        if match is None:
            return None

        return (match.group(1), match.group(len(match.groups())))

    def parse_line_key(self, key_node):
        """Interprets the key of the line"""
        key_dictionary = {
            "0-0:96.1.1" : "meter_name",
            "1-0:1.8.1" : "power_usage_total_low",
            "1-0:1.8.2" : "power_usage_total_normal",
            "1-0:2.8.1" : "power_supply_total_low",
            "1-0:2.8.2" : "power_supply_total_normal",
            "1-0:1.7.0" : "power_usage_current",
            "1-0:2.7.0" : "power_supply_current",
            "0-1:24.2.1": "gas_usage_total"
        }

        return key_dictionary.get(key_node, None)

    def parse_line_value(self, key, value_node):
        """Interprets the value of the line"""
        value_node = value_node.replace("*kWh", "").replace("*kW", "").replace("*m3", "")

        if key is not None and ("power_" in key or "gas_" in key):
            return Decimal(value_node)

        return value_node

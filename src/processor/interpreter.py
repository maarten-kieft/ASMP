import re
from decimal import Decimal

class Interpreter:
    def interpretMessage(self, message):
        print("Interpreting message")
        measurement = {}

        
        for i, line in enumerate(message):
            lineNodes = self.parseLine(line)
            key = self.interpretLineKey(lineNodes[0])       
            value = self.interpretLineValue(key,lineNodes[1])

            if key is not None:
                measurement[key] = value
                print(key)
                print(value)
                                       
    def parseLine(self, line):
        print(line)

        pattern = re.compile("^([^\(]*)\(([^\)]*)\)$")
        line = "1-0:1.8.1(000060.140*kWh)"
        match = pattern.match(line)

        return (match.group(1),match.group(2))

    def interpretLineKey(self, keyNode):
        keyDictionary = {
            "0-0:96.1.1" : "meterId",
            "1-0:1.8.1" : "usage_total_low",
            "1-0:1.8.2" : "usage_total_normal",
            "1-0:2.8.1" : "return_total_low",
            "1-0:2.8.2" : "return_total_normal",
            "0-0:96.14.0" : "current_tarrif",
            "1-0:1.7.0" : "usage_current",
            "1-0:2.7.0" : "return_current"
        }

        return keyDictionary.get(keyNode,None)


    def interpretLineValue(self, key, valueNode):
        if "usage_" in key or "return_" in key:
            return Decimal(valueNode.replace("*kWh","").replace("*kW",""))

        return valueNode

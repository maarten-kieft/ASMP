from processor.parsing.parser import Parser
from decimal import Decimal
from unittest import TestCase

class ParserTestCase(TestCase):

    def test_parse_power_and_gas(self):
        message = [
            "/KFM5KAIFA-METER",
            "1-3:0.2.8(42)",
            "0-0:1.0.0(171219182824W)",
            "0-0:96.1.1(4530303235303030303431353439353135)",
            "1-0:1.8.1(001602.853*kWh)",
            "1-0:1.8.2(002306.286*kWh)",
            "1-0:2.8.1(000130.123*kWh)",
            "1-0:2.8.2(000154.345*kWh)",
            "0-0:96.14.0(0002)",
            "1-0:1.7.0(00.713*kW)",
            "1-0:2.7.0(00.243*kW)",
            "0-0:96.7.21(00001)",
            "0-0:96.7.9(00001)",
            "1-0:99.97.0(2)(0-0:96.7.19)(170117061355W)(0000006886*s)(000101000001W)(2147483647*s)",
            "1-0:32.32.0(00000)",
            "1-0:32.36.0(00000)",
            "0-0:96.13.1()",
            "0-0:96.13.0()",
            "1-0:31.7.0(003*A)",
            "1-0:21.7.0(00.713*kW)",
            "1-0:22.7.0(00.243*kW)",
            "0-1:24.1.0(003)",
            "0-1:96.1.0(4730303435303031363039363330333136)",
            "0-1:24.2.1(171219180000W)(00743.920*m3)"]

        parser = Parser()
        measurement = parser.parse(message)

        self.assertEqual("4530303235303030303431353439353135",measurement["meter_name"])
        self.assertEqual(Decimal("1602.853"),measurement["power_usage_total_low"])
        self.assertEqual(Decimal("2306.286"),measurement["power_usage_total_normal"])
        self.assertEqual(Decimal("130.123"),measurement["power_supply_total_low"])
        self.assertEqual(Decimal("154.345"),measurement["power_supply_total_normal"])
        self.assertEqual(Decimal("0.713"),measurement["power_usage_current"])
        self.assertEqual(Decimal("0.243"),measurement["power_supply_current"])
        self.assertEqual(Decimal("743.920"),measurement["gas_usage_total"])

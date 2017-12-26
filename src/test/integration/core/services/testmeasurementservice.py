from django.db import transaction
from core.services.measurementservice import MeasurementService
from core.models import Measurement
from unittest import TestCase
from decimal import Decimal

class MeasurementServiceTestCase(TestCase):
   
    def test_save_measurement_power(self):
        with transaction.atomic():
            input = {
                "meter_name": "4530303235303030303431353439353135", 
                "power_usage_total_low": Decimal('1602.853'), 
                "power_usage_total_normal": Decimal('2306.286'), 
                "power_supply_total_low": Decimal('130.123'), 
                "power_supply_total_normal": Decimal('154.345'), 
                "power_usage_current": Decimal('0.713'), 
                "power_supply_current": Decimal('0.243')
            }

            Measurement.objects.all().delete()
            MeasurementService.save_measurement(input)
            last_measurements = Measurement.objects.all()

            self.assertEqual(len(last_measurements),1)
            self.assertEqual(last_measurements[0].power_usage_total_low,Decimal('1602.853'))
    

    def test_save_measurement_power_and_gas(self):
        with transaction.atomic():
            input = {
                "meter_name": "4530303235303030303431353439353135", 
                "power_usage_total_low": Decimal('1602.853'), 
                "power_usage_total_normal": Decimal('2306.286'), 
                "power_supply_total_low": Decimal('130.123'), 
                "power_supply_total_normal": Decimal('154.345'), 
                "power_usage_current": Decimal('0.713'), 
                "power_supply_current": Decimal('0.243'), 
                "gas_usage_total": Decimal('743.920')
            }

            Measurement.objects.all().delete()
            MeasurementService.save_measurement(input)
            last_measurements = Measurement.objects.all()

            self.assertEqual(len(last_measurements),1)
            self.assertEqual(last_measurements[0].power_usage_total_low,Decimal('1602.853'))
            self.assertEqual(last_measurements[0].gas_usage_total,Decimal('743.920'))
            
from django.db import transaction
from datetime import datetime, timedelta
from core.services.measurementservice import MeasurementService
from core.models import Measurement, Meter
from unittest import TestCase
from decimal import Decimal
import pytz

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
    
    def test_get_aggregate_measurements(self):
        with transaction.atomic():
            Measurement.objects.all().delete()
            Meter.objects.all().delete()
            meter = Meter.objects.get_or_create(name="integration-test-meter")[0]

            measurement1 = Measurement()
            measurement1.meter = meter
            measurement1.power_usage_total_low = Decimal('1602.853')
            measurement1.power_usage_total_normal = Decimal('2306.286')
            measurement1.power_supply_total_low = Decimal('130.123')
            measurement1.power_supply_total_normal = Decimal('154.345')
            measurement1.power_usage_current = Decimal('0.713')
            measurement1.power_supply_current = Decimal('0.243') 
            measurement1.gas_usage_total = Decimal('743.920')
            measurement1.timestamp = datetime(year=2017,month=1,day=1,hour=13,minute=15,tzinfo=pytz.utc)
            measurement1.save()

            measurement2 = Measurement()
            measurement2.meter = meter
            measurement2.power_usage_total_low = Decimal('1602.853')
            measurement2.power_usage_total_normal = Decimal('2406.286')
            measurement2.power_supply_total_low = Decimal('130.123')
            measurement2.power_supply_total_normal = Decimal('174.345')
            measurement2.power_usage_current = Decimal('0.713')
            measurement2.power_supply_current = Decimal('0.243') 
            measurement2.gas_usage_total = Decimal('843.920')
            measurement2.timestamp = datetime(year=2017,month=1,day=1,hour=13,minute=54,tzinfo=pytz.utc)
            measurement2.save()

            min = datetime(year=2017,month=1,day=1,hour=0,minute=0,tzinfo=pytz.utc)
            max = datetime(year=2018,month=1,day=1,hour=0,minute=0,tzinfo=pytz.utc)
            result = MeasurementService.get_aggregate_measurements(min,max)

            self.assertEqual(1,len(result))
            self.assertEqual(Decimal('3909.139'),result[0]["power_usage_start"])
            self.assertEqual(Decimal('4009.139'),result[0]["power_usage_end"])
            self.assertEqual(Decimal('284.468'),result[0]["power_supply_start"])
            self.assertEqual(Decimal('304.468'),result[0]["power_supply_end"])
            self.assertEqual(Decimal('743.920'),result[0]["gas_usage_start"])
            self.assertEqual(Decimal('843.920'),result[0]["gas_usage_end"])


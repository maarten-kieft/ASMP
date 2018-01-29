from unittest import TestCase
from core.services.applicationservice import ApplicationService
from core.models import Setting
from django.db import transaction

class ApplicationServiceTestCase(TestCase):

    def test_get_id(self):
        with transaction.atomic():
            Setting.objects.all().delete()
            id1 = ApplicationService.get_id()
            id2 = ApplicationService.get_id()

            self.assertEqual(id1,id2)

    def test_save_meter_message_format(self):
        
        with transaction.atomic():
            input = ["line1","line2"]
            ApplicationService.save_meter_message_format(input)
            output = ApplicationService.get_meter_message_format()
            
            self.assertEqual(2, len(output))
            self.assertEqual("line1", output[0])
            self.assertEqual("line2", output[1])


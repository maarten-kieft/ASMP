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


from django.test import TestCase
from core.services.applicationservice import ApplicationService
from core.models import Setting

class ApplicationServiceTestCase(TestCase):
    def setUp(self):
       Setting.objects.all().delete()

    def test_get_id(self):
        id1 = ApplicationService.get_id()
        id2 = ApplicationService.get_id()

        self.assertEqual(id1,id2)


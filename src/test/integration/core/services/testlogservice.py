from core.services.logservice import LogService
from core.models import LogMessage
from unittest import TestCase
from django.db import transaction

class LogServiceTestCase(TestCase):

    def test_log_warning(self):
        with transaction.atomic():
            LogMessage.objects.all().delete()
            LogService.log_warning("integration-test", "sample-warning")
            messages = LogService.get_recent()

            self.assertEqual(1,len(messages))
            self.assertEqual("sample-warning",messages[0].text)
            self.assertEqual("integration-test",messages[0].module)
            self.assertEqual("warning",messages[0].level)

    def test_log_error(self):
        with transaction.atomic():
            LogMessage.objects.all().delete()
            LogService.log_error("integration-test", "sample-error")
            messages = LogService.get_recent()

            self.assertEqual(1, len(messages))
            self.assertEqual("error", messages[0].level)

    def test_log_info(self):
        with transaction.atomic():
            LogMessage.objects.all().delete()    
            LogService.log_info("integration-test", "sample-error")
            messages = LogService.get_recent()

            self.assertEqual(1, len(messages))
            self.assertEqual("info", messages[0].level)

    def test_cleanup_singlemessage_remains(self):
        with transaction.atomic():
            LogMessage.objects.all().delete()
            LogService.log_warning("integration-test", "sample-warning")
            LogService.cleanup()
            messages = LogService.get_recent()

            self.assertEqual(1, len(messages))

    def test_cleanup_toomany_max(self):
        with transaction.atomic():
            LogMessage.objects.all().delete()

            for x in range(0, 251):
                LogService.log_warning("integration-test", "sample-warning")

            LogService.cleanup()
            messages = LogService.get_recent()
            self.assertEqual(250, len(messages))
from django.test import TestCase
from core.services.messageservice import MessageService
from core.models import Message

class MessageServiceTestCase(TestCase):
    def setUp(self):
       Message.objects.all().delete()

    def test_log_warning(self):
        MessageService.log_warning("integration-test","sample-warning")
        messages = MessageService.get_recent()

        self.assertEqual(1,len(messages))
        self.assertEqual("sample-warning",messages[0].text)
        self.assertEqual("integration-test",messages[0].module)
        self.assertEqual("warning",messages[0].level)

    def test_log_error(self):
        MessageService.log_error("integration-test", "sample-error")
        messages = MessageService.get_recent()

        self.assertEqual(1, len(messages))
        self.assertEqual("error", messages[0].level)

    def test_log_info(self):
        MessageService.log_info("integration-test", "sample-error")
        messages = MessageService.get_recent()

        self.assertEqual(1, len(messages))
        self.assertEqual("info", messages[0].level)

    def test_cleanup_singlemessage_remains(self):
        MessageService.log_warning("integration-test", "sample-warning")
        MessageService.cleanup()
        messages = MessageService.get_recent()

        self.assertEqual(1, len(messages))

    def test_cleanup_toomany_max(self):
        for x in range(0, 251):
            MessageService.log_warning("integration-test", "sample-warning")

        MessageService.cleanup()
        messages = MessageService.get_recent()

        self.assertEqual(250, len(messages))

from django.test import TestCase
from core.services.messageservice import MessageService

class CoreTestCase(TestCase):
  
    def test_cleanup_messages(self):
        """Test if cleaning up messages works"""
        MessageService.cleanup()

  
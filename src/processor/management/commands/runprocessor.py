import traceback
import time
from django.core.management.base import BaseCommand
from core.services.messageservice import  MessageService
from processor.processor import Processor


class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Starting the processor"""

        while True:
            try:
                processor = Processor()
                processor.start()
            except Exception:
                MessageService.log_error("processor", "Exception thrown:" + traceback.format_exc())
                time.sleep(20)

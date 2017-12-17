import traceback
import time
from django.core.management.base import BaseCommand
from core.services.logservice import  LogService
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
                LogService.log_error("processor", "Exception thrown:" + traceback.format_exc())
                time.sleep(20)

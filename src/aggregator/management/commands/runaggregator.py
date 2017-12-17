import time
import traceback
from django.core.management.base import BaseCommand
from core.services.logservice import LogService
from aggregator.aggregator import Aggregator

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Starting the aggregator"""

        while True:
            try:
                aggregator = Aggregator()
                aggregator.start()
            except Exception:
                LogService.log_error("aggregator", "Exception thrown:" + traceback.format_exc())
                time.sleep(20)


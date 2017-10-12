from django.core.management.base import BaseCommand
from core.services.messageservice import MessageService
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
                MessageService.log_error("updater", "Exception thrown:"+sys.exc_info()[0])



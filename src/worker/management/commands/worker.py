import threading
from worker.processor import Processor
from worker.aggregator import Aggregator
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Handle for this command"""
        processor = Processor()
        aggregator = Aggregator()

        processor_thread = threading.Thread(target=processor.start)
        aggregator_thread = threading.Thread(target=aggregator.start)

        processor_thread.start()
        aggregator_thread.start()

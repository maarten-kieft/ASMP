import threading
from worker.processor import Processor
from worker.aggregator import Aggregator
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Handle for this command"""
        aggregator = Aggregator()
        aggregator.start()
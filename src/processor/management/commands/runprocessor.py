import threading
from processor.processor import Processor
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Handle for this command"""
        processor = Processor()
        processor.start()
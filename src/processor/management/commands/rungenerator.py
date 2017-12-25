import threading
from processor.generator import Generator
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Handle for this command"""
        geneator = Generator()
        geneator.start()
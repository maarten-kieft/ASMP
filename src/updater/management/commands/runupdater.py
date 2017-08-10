import threading
from updater.updater import Updater
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Handle for this command"""
        updater = Updater()
        updater.start()
import threading
from updater.updater import Updater
from django.core.management.base import BaseCommand
from core.services.applicationservice import ApplicationService

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Handle for this command"""
        updater = Updater()
        updater.start()
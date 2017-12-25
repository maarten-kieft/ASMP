import time
import sys
import traceback
from django.core.management.base import BaseCommand
from core.services.logservice import LogService
from updater.updater import Updater

class Command(BaseCommand):
    """Command for manage.py"""

    def handle(self, *args, **kwargs):
        """Starting the updater"""

        while True:
            try:
                updater = Updater()
                updater.start()
                return
            except Exception:
                LogService.log_error("updater", "Exception thrown:" + traceback.format_exc())
                time.sleep(20)
from datetime import datetime, timedelta
from core.models import LogMessage
import pytz

class LogService:
    """Service to perform actions around messages"""
    log_count = 0

    @staticmethod
    def log_debug(module, text):
        """Logs a debug message into the database"""
        #LogService.log(module, "debug", text)
        return

    @staticmethod
    def log_info(module, text):
        """Logs a info message into the database"""
        LogService.log(module, "info", text)

    @staticmethod
    def log_warning(module, text):
        """Logs a warning message into the database"""
        LogService.log(module, "warning", text)

    @staticmethod
    def log_error(module, text):
        """Logs a error message into the database"""
        LogService.log(module, "error", text)

    @staticmethod
    def log(module, level, text):
        """Logs a message into the database"""
        print(module + " [" + level + "]: " + text)
        timestamp = datetime.now(pytz.utc)
        timestamp.replace(tzinfo=pytz.utc)

        message = LogMessage()
        message.module = module
        message.level = level
        message.text = text
        message.timestamp = timestamp
        message.save()

        LogService.log_count += 1
        if LogService.log_count >= 50:
            LogService.cleanup()

    @staticmethod
    def cleanup():
        LogService.log_count = 0
        messages = LogMessage.objects.all().order_by('-timestamp')[:250]
        LogMessage.objects.exclude(pk__in=messages).delete()

    @staticmethod
    def get_recent():
        """Get log messages ordered by timestamp"""
        
        return LogMessage.objects.order_by('module', '-timestamp', )

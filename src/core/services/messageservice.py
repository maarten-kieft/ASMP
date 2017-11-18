from datetime import datetime, timedelta
from core.models import Message
import pytz

class MessageService:
    """Service to perform actions around messages"""
    log_count = 0

    @staticmethod
    def log_debug(module, text):
        """Logs a debug message into the database"""
        MessageService.log(module, "debug", text)

    @staticmethod
    def log_info(module, text):
        """Logs a info message into the database"""
        MessageService.log(module, "info", text)

    @staticmethod
    def log_warning(module, text):
        """Logs a warning message into the database"""
        MessageService.log(module, "warning", text)

    @staticmethod
    def log_error(module, text):
        """Logs a error message into the database"""
        MessageService.log(module, "error", text)

    @staticmethod
    def log(module, level, text):
        """Logs a message into the database"""
        print(module + " [" + level + "]: " + text)
        timestamp = datetime.now(pytz.utc)
        timestamp.replace(tzinfo=pytz.utc)

        message = Message()
        message.module = module
        message.level = level
        message.text = text
        message.timestamp = timestamp
        message.save()

        MessageService.log_count += 1
        if MessageService.log_count >= 50:
            MessageService.cleanup()

    @staticmethod
    def cleanup():
        MessageService.log_count = 0
        messages = Message.objects.all().order_by('-timestamp')[:250]
        Message.objects.exclude(pk__in=messages).delete()

    @staticmethod
    def get_recent():
        """Get log messages ordered by timestamp"""
        
        return Message.objects.order_by('module','-timestamp',)

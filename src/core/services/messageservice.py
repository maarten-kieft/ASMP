from datetime import datetime, timedelta
from core.models import Message
import pytz

class MessageService:
    """Service to perform actions around messages"""
    log_count = 0

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
        message = {'timestamp' : datetime.now(pytz.utc), 'level': level}
        Message.objects.update_or_create(module=module, text=text, defaults=message)
        
        MessageService.log_count += 1
        if MessageService.log_count >= 50:
            MessageService.cleanup()

    @staticmethod
    def cleanup():
        MessageService.log_count = 0
        Message.objects.filter(timestamp__lt=(datetime.now() - timedelta(hours=1))).delete()
        
    @staticmethod
    def get_recent():
        """Get log messages ordered by timestamp"""
        
        return Message.objects.order_by('module','-timestamp',)

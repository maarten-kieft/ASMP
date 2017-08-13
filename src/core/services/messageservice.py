from datetime import datetime
from core.models import Message
import pytz

class MessageService:
    """Service to perform actions around messages"""

    @staticmethod
    def log_info(module,text):
        """Logs a info message into the database"""
        MessageService.log(module,"info",text)

    @staticmethod
    def log_warning(module,text):
        """Logs a info message into the database"""
        MessageService.log(module,"warning",text)

    @staticmethod
    def log(module,level,text):
        """Logs a message into the database"""
        print(module + " [" + level + "]: " + text)
        message = Message()
        message.module = module
        message.level = level
        message.text = text
        message.timestamp = datetime.now(pytz.utc)

        message.save()

    @staticmethod
    def get_recent():
        """Logs a message into the database"""
        
        return Message.objects.order_by('module','-timestamp',)

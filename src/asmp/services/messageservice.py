import pytz
from datetime import datetime
from web.models import Message

class MessageService:
    """Service to perform actions around messages"""

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

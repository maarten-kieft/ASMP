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
        message = Message()
        message.module = module
        message.level = level
        message.text = text
        message.timestamp = datetime.now(pytz.utc)
        message.save()

        MessageService.log_count += 1

        if MessageService.log_count >= 50:
            MessageService.cleanup()

    @staticmethod
    def cleanup():
        MessageService.log_count = 0

        #Delete messages older than 1 hour
        Message.objects.filter(timestamp__lt=(datetime.now() - timedelta(hours=1))).delete()
        
        #Delete duplicate messages
        unique_messages = Message.objects.values('module','text')
        import pdb;pdb.set_trace()
        #Delete message from each module which don't belong to the first 50
        
        # elke module mag er max 50 hebben
        # dubbele eruit


    @staticmethod
    def get_recent():
        """Get log messages ordered by timestamp"""
        
        return Message.objects.order_by('module','-timestamp',)

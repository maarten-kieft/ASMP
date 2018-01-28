from core.models import Setting
import uuid

class ApplicationService:
    """Get application settings, identifier"""

    @staticmethod
    def get_id():
        """Get the id of the application"""
        result = Setting.objects.filter(name="application_id")

        if len(result) > 0:
            return result[0].value

        return Setting.objects.create(name="application_id", value=uuid.uuid4().hex).value

    @staticmethod
    def save_meter_message_format(message):
        """Saved the received """
        concattedMessage =  "|".join(message)
        Setting.objects.get_or_create(name="raw_meter_message",value=message)

    @staticmethod
    def get_meter_message_format():
        """Saved the received """
        message_format = Setting.objects.get(name="raw_meter_message")

        if(message_format is None):
            return []

        return message_format.value.split("|")

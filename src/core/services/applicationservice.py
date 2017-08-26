from core.models import Setting
import uuid

class ApplicationService:
    """Get application settings, identifier"""

    @staticmethod
    def application_id():
        """Get the id of the application"""
        result = Setting.objects.filter(name="application_id")
        
        if len(result) > 0:
            return result[0].value
        
        return Setting.objects.create(name="application_id",value=uuid.uuid4().hex).value

        
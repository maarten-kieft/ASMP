from core.models import Setting
import uuid

class ApplicationService:
    """Get application settings, identifier"""

    @staticmethod
    def application_id():
        """Get the id of the application"""
        result = Setting.objects.filter(name="application_id")[0]
        if not result:
            result = Setting.objects.create(name="application_id",value=uuid.uuid4().hex)
        
        return result.value
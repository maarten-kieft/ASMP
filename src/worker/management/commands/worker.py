#from data.database import Database
from worker.processor import Processor
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    

    def handle(self, *args, **kwargs):
        processor = Processor()
        processor.start()
        

#database = Database()
#database.initSchema()

#processor = Processor(database)
#processor.start()

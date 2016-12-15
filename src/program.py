from data.database import Database
from processor.processor import Processor


database = Database()
database.initSchema()

processor = Processor(database)
processor.start()

from data.database import Database
from processor.processor import Processor


database = Database()
database.initSchema()

processor = Processor(database)
processor.start()

message = [
"/KFM5KAIFA-METER",
"1-3:0.2.8(42)",
"0-0:1.0.0(161211191412W)",
"0-0:96.1.1(4530303237303030358130313334353142)",
"1-0:1.8.1(000060.140*kWh)",
"1-0:1.8.2(000076.832*kWh)",
"1-0:2.8.1(000000.000*kWh)",
"1-0:2.8.2(000000.000*kWh)",
"0-0:96.14.0(0001)",
"1-0:1.7.0(00.577*kW)",
"1-0:2.7.0(00.000*kW)",
"0-0:96.7.21(00001)",
"0-0:96.7.9(00001)",
"1-0:99.97.0(1)(0-0:96.7.19)(000101000001W)(2147483647*s)",
"1-0:32.32.0(00000)",
"1-0:32.36.0(00000)",
"0-0:96.13.1()",
"0-0:96.13.0()",
"1-0:31.7.0(002*A)",
"1-0:21.7.0(00.580*kW)",
"1-0:22.7.0(00.000*kW)"
]

#measurement = processor.interpreter.interpretMessage(message)
#database.insertMeasurement(measurement)

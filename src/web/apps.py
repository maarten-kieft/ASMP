from django.apps import AppConfig
import subprocess

class WebConfig(AppConfig):
    name = 'web'

    #def ready(self):
        #generator_process = subprocess.Popen(['python', 'manage.py','rungenerator'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #if processor_process is None:
        #processor_process = subprocess.Popen(['python', 'manage.py','runprocessor'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        #generator_process = subprocess.Popen(['python', 'manage.py','rungenerator'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
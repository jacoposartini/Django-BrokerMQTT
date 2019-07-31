from django.apps import AppConfig
import sys
import MQTT.broker as Broker
from multiprocessing import Process

class MqttConfig(AppConfig):
    name = 'MQTT'
    def ready(self):
        if 'runserver' in sys.argv:
            p = Process(target=Broker.start)
            p.start()
        else:
            pass

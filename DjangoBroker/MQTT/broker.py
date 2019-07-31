import logging
import asyncio
import os
from hbmqtt.broker import Broker
from multiprocessing import Process
from django.conf import settings

logger = logging.getLogger(__name__)


config = {
    'listeners': {
        'default': {
            'type': 'tcp',
            'bind': '0.0.0.0:1883',
        },
        'ws-mqtt': {
            'bind': '0.0.0.0:8080',
            'type': 'ws',
            'max_connections': 10,
        },
    },
    'sys_interval': 10,
    'sqlite-database': settings.DATABASES['default']['NAME'],
	'auth': {
		'allow-anonymous': False,
		'plugins': [
			'auth_anonymous', 'auth_sqlite'
		]
	},
	'topic-check': {
		'enabled': True,
		'plugins': [
			'topic_sqlite'
		]
	}
}

broker = Broker(config)

@asyncio.coroutine
def start_server():
    yield from broker.start()

def start():
    formatter = "[%(asctime)s] :: %(levelname)s :: %(name)s :: %(message)s"

    logging.basicConfig(level=logging.INFO, format=formatter)

    asyncio.get_event_loop().run_until_complete(start_server())
    asyncio.get_event_loop().run_forever()

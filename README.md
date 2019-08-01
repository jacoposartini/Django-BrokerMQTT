# Django-BrokerMQTT

## install
To install, simply run the command:
```
	./install.sh
```
## configuration
To database migration and superuser creation use the command:
```
  python3 manage.py migrate && python3 manage.py createsuperuser
```
To change the settings of the broker edit the dictionary in the file ```DjangoBroker.MQTT.broker.py```
```
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
```
To modify the plugin queries look at this link:
```
  https://github.com/jacoposartini/SQLite3_HBMQTT_Plugins
```
## run
```
  python3 manage.py --noreload
```
## in case of bugs please contact me.

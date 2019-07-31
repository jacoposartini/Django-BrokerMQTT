from django.contrib import admin
from .models import AuthMQTT, Topic

admin.site.register(AuthMQTT)
admin.site.register(Topic)

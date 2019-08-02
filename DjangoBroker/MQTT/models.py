from django.db import models
from django.contrib.auth.models import User
from .utils import generate_random_string

class AuthMQTT(models.Model):
    user = models.OneToOneField(User,
                               on_delete=models.CASCADE,
                               related_name="mqtt_user")
    username = models.CharField(max_length=16, unique=True)
    password = models.CharField(max_length=16, unique=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        self.username = self.user.username[0:3] + generate_random_string(7)
        self.password = generate_random_string(10)
        super(AuthMQTT, self).save(*args, **kwargs)



class Topic(models.Model):
    topic = models.CharField(max_length=64, unique=True)
    mqtt_user = models.ForeignKey(AuthMQTT,
                               on_delete=models.CASCADE,
                               related_name="user_topics")
    def __str__(self):
        return self.topic

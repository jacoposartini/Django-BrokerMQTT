# Generated by Django 2.2.3 on 2019-07-30 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MQTT', '0002_auto_20190730_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]

# Generated by Django 2.2.3 on 2019-07-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MQTT', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='topic',
            field=models.CharField(default=0, max_length=64),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]

# Generated by Django 2.0.3 on 2018-03-27 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_system', '0005_messagenotification_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagenotification',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]

# Generated by Django 4.0.2 on 2024-06-17 21:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0009_alter_ticket_movie_session_alter_ticket_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-04 20:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_alter_event_creator_participant'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='title',
            field=models.CharField(default=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Events.event')),
        ),
    ]

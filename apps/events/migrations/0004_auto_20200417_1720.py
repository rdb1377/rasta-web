# Generated by Django 2.2.11 on 2020-04-17 17:20

from django.db import migrations
import django_jalali.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=django_jalali.db.models.jDateTimeField(blank=True, null=True),
        ),
    ]
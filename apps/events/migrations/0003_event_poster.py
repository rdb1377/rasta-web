# Generated by Django 2.2.11 on 2020-04-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200413_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='event_posters/'),
        ),
    ]
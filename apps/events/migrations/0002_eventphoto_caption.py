# Generated by Django 2.2.11 on 2020-05-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventphoto',
            name='caption',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
# Generated by Django 2.0.4 on 2018-04-28 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20180427_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='seats',
            field=models.IntegerField(default=4),
        ),
    ]
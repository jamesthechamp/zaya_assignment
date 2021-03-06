# Generated by Django 2.0.4 on 2018-04-29 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_long_position', models.DecimalField(decimal_places=5, max_digits=8)),
                ('from_lat_position', models.DecimalField(decimal_places=5, max_digits=8)),
                ('to_long_position', models.DecimalField(decimal_places=5, max_digits=8)),
                ('to_lat_position', models.DecimalField(decimal_places=5, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('wait', 'waiting'), ('start', 'in ride'), ('end', 'completed')], default='wait', max_length=5)),
                ('distance', models.FloatField(default=2.0)),
                ('fair', models.FloatField(default=16.0)),
                ('seats', models.IntegerField(default=4)),
            ],
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0011_auto_20200413_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incidents',
            name='category',
            field=models.CharField(choices=[('snapback', 'snapback'), ('Robot stopped', 'Robot stopped'), ('Audio error', 'Audio error'), ('Battery problem', 'Battery problem'), ('Hardware error', 'Hardware error'), ('Heartbeat flicker', 'Heartbeat flicker')], default='Snapback', max_length=100),
        ),
    ]

# Generated by Django 3.0.5 on 2020-04-06 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Active', 'ACTIVE'), ('Acknowledged', 'ACKNOWLEDGED'), ('Resolved', 'RESOLVED')], default='Active', max_length=100),
        ),
    ]

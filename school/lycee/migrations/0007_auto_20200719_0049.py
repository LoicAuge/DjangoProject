# Generated by Django 3.0.7 on 2020-07-18 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lycee', '0006_auto_20200716_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appel',
            name='heure_d',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='appel',
            name='heure_f',
            field=models.TimeField(null=True),
        ),
    ]
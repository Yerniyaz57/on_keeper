# Generated by Django 2.2 on 2019-09-19 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tableproducts',
            name='table',
            field=models.IntegerField(blank=True),
        ),
    ]
# Generated by Django 4.0.6 on 2022-07-15 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='amount',
            field=models.IntegerField(max_length=100),
        ),
    ]

# Generated by Django 2.2 on 2019-04-08 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_auto_20190407_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignedgear',
            name='char_class',
            field=models.CharField(max_length=20),
        ),
    ]

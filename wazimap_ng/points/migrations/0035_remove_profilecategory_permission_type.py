# Generated by Django 2.2.10 on 2020-08-26 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('points', '0034_auto_20200821_0613'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilecategory',
            name='permission_type',
        ),
    ]
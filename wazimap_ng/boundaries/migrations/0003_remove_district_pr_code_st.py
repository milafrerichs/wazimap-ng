# Generated by Django 2.2.8 on 2020-01-20 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('boundaries', '0002_district'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='pr_code_st',
        ),
    ]

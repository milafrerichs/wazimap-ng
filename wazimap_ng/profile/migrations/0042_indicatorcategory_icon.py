# Generated by Django 2.2.10 on 2020-06-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0041_profile_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='indicatorcategory',
            name='icon',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

# Generated by Django 2.2.10 on 2020-04-11 20:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0077_auto_20200411_2044'),
        ('profile', '0013_indicatorcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicatorsubcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.IndicatorCategory'),
        ),
    ]
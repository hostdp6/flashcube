# Generated by Django 2.2.3 on 2020-05-19 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('towers', '0024_auto_20200519_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

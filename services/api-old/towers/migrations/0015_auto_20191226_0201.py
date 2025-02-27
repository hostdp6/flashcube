# Generated by Django 2.2.3 on 2019-12-26 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('towers', '0014_auto_20191226_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpreferences',
            name='baseCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='base_category', to='towers.Category'),
        ),
        migrations.AlterField(
            model_name='userpreferences',
            name='learningCategories',
            field=models.ManyToManyField(blank=True, null=True, related_name='learning_categories', to='towers.Category'),
        ),
    ]

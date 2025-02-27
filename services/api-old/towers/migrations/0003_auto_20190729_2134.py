# Generated by Django 2.2.3 on 2019-07-29 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('towers', '0002_initial_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='cube',
            name='name',
            field=models.CharField(default=-1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tower',
            name='primary_category',
            field=models.ForeignKey(default=-1, on_delete=django.db.models.deletion.CASCADE, to='towers.Category'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tower',
            name='categories',
            field=models.ManyToManyField(related_name='categories', to='towers.Category'),
        ),
    ]

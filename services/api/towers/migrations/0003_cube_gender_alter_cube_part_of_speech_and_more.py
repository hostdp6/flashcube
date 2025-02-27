# Generated by Django 4.0.4 on 2022-05-23 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('towers', '0002_cube_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cube',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='cube',
            name='part_of_speech',
            field=models.CharField(choices=[('NN', 'NOUN'), ('PN', 'PRONOUN'), ('VB', 'VERB'), ('AJ', 'ADJECTIVE'), ('AD', 'ADVERB'), ('PR', 'PREPOSITION'), ('CJ', 'CONJUNCTION'), ('IJ', 'INTERJECTION'), ('NB', 'NUMBER'), ('AR', 'ARTICLE'), ('DT', 'DETERMINER')], max_length=2),
        ),
        migrations.AlterField(
            model_name='face',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='face_audio'),
        ),
        migrations.CreateModel(
            name='CategoryStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('DL', "Don't Learn"), ('LN', 'Learn Now'), ('AL', 'Already Learned')], default='DL', max_length=2)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='towers.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

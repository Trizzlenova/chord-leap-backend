# Generated by Django 2.0.7 on 2018-07-13 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logic', '0004_progression'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progression',
            name='chords',
        ),
        migrations.AddField(
            model_name='progression',
            name='array_of_chords',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
    ]

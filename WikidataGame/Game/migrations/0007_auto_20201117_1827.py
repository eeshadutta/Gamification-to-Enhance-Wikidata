# Generated by Django 3.1.2 on 2020-11-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0006_auto_20201117_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_eng',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_hin',
        ),
        migrations.AddField(
            model_name='question',
            name='question_object',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='question_property',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
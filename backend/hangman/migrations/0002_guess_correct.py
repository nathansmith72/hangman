# Generated by Django 3.0.5 on 2020-07-16 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='guess',
            name='correct',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
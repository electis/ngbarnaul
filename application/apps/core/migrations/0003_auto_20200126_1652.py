# Generated by Django 3.0.2 on 2020-01-26 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_tab'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='text_top',
            new_name='name',
        ),
    ]

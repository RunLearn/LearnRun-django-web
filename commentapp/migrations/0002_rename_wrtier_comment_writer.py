# Generated by Django 3.2.5 on 2021-08-10 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commentapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='wrtier',
            new_name='writer',
        ),
    ]

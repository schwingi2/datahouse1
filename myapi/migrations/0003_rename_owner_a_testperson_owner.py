# Generated by Django 4.2.2 on 2023-10-01 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0002_rename_owner_testperson_owner_a'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testperson',
            old_name='owner_a',
            new_name='owner',
        ),
    ]

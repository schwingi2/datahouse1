# Generated by Django 4.2.2 on 2023-10-01 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testperson',
            old_name='owner',
            new_name='owner_a',
        ),
    ]
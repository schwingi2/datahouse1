# Generated by Django 2.2.28 on 2023-03-31 19:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0008_auto_20230330_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='testperson',
            name='rec_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

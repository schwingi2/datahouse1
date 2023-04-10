# Generated by Django 3.0.8 on 2020-07-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0005_hochbeet2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hochbeet2',
            name='battery',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='hochbeet2',
            name='conductivity',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='hochbeet2',
            name='light',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='hochbeet2',
            name='moisture',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='hochbeet2',
            name='temperature',
            field=models.CharField(max_length=10),
        ),
    ]

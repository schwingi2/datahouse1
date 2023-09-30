# Generated by Django 2.2.28 on 2023-04-16 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hochbeet2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_time', models.DateTimeField(auto_now_add=True)),
                ('light', models.CharField(max_length=15)),
                ('battery', models.CharField(max_length=15)),
                ('temperature', models.CharField(max_length=15)),
                ('conductivity', models.CharField(max_length=15)),
                ('moisture', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Testperson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pers_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('name', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
                ('rec_time', models.DateTimeField(auto_now_add=True)),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Testperson', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-rec_time'],
            },
        ),
    ]

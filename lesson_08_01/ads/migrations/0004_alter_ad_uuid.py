# Generated by Django 5.0 on 2024-02-12 14:52

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ad_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('4560f909-8d65-494d-b8dd-d6f5522ecbe3'), editable=False, primary_key=True, serialize=False),
        ),
    ]